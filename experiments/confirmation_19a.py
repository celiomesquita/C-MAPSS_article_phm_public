"""P19.1: confirmation pipeline for FD002 and FD004 (protocol: protocolo_confirmacao_19a.md).

The module never reads FD002/FD004 at import. `open_confirmation` is the only reader and is locked by an
amendment in emendas.md; `rehearsal` runs the same code on FD001 + FD003 with synthetic regimes.
"""

import hashlib
import importlib.metadata
import itertools
import json
import math
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from scipy.stats import beta
from sklearn.cluster import KMeans
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import adjusted_rand_score, silhouette_score
from threadpoolctl import threadpool_limits

import pilot_f_uncertainty_10 as p10
import pilot_fd001_05 as p05
import pilot_removal_11 as p11
from pilot_extension_16a import US, engine_expectation
from pilot_fd001_04 import centred_sensors
from pilot_landmark_control_11a import marker_action
from regime_normalisation import OPS, SENSORS, RegimeNormaliser

ROOT = Path(__file__).resolve().parents[1]
FREEZE = ROOT / "experiments/congelamento_2026-10-18"
EMENDAS = FREEZE / "emendas.md"
MANIFEST = FREEZE / "manifest_hashes.json"
OUT = ROOT / "experiments/artifacts/confirmation_19a"
OUT_REHEARSAL = ROOT / "experiments/artifacts/confirmation_19a_ensaio"
MODULES = ["confirmation_19a.py", "test_confirmation_19a.py", "verify_confirmation_19a.py"]
AGE = 127
TARGET = .02
GRID = list(itertools.product([60, 100, 140], [1, 2], [0., .1]))
SEEDS = p10.SEEDS
CONFIG_SEED = 20261018
BOOT = 2000
EPS = 1e-9
METHODS = p10.METHODS
CONFIRMATION_FILES = {"FD002": "train_FD002.txt", "FD004": "train_FD004.txt"}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cp_upper(x, n, confidence=.95):
    """One-sided Clopper-Pearson upper bound for a binomial proportion."""
    assert 0 <= x <= n and n > 0
    return 1. if x >= n else float(beta.ppf(confidence, x+1, n-x))


def age_criterion(lives, age=AGE):
    lives = np.asarray(lives)
    hits = int((lives <= age).sum())
    upper = cp_upper(hits, len(lives))
    return dict(engines=int(len(lives)), hits=hits, upper95=upper, passes=bool(upper <= TARGET), age=age)


def max_passing_hits(n, confidence=.95):
    hits = 0
    while cp_upper(hits+1, n, confidence) <= TARGET:
        hits += 1
    return hits


# ---------------------------------------------------------------- partitions and configuration

def split_config(units, seed=CONFIG_SEED, sizes=(40, 20, 20)):
    ordered = np.random.default_rng(seed).permutation(np.asarray(sorted(units)))
    a, b, c = sizes
    group = dict(fit=sorted(ordered[:a].tolist()), calibration=sorted(ordered[a:a+b].tolist()),
                 selection=sorted(ordered[a+b:a+b+c].tolist()))
    rest = sorted(ordered[a+b+c:].tolist())
    return group, rest


def partitions(units, seed, n_folds=10, sizes=(25, 15, 50)):
    """Evaluation blocks cover every unit once; F/C/U are drawn from the other units (P10 layout)."""
    units = np.asarray(sorted(units))
    permutation = np.random.default_rng(seed).permutation(units)
    folds = []
    for k, block in enumerate(np.array_split(permutation, n_folds), start=1):
        remaining = np.setdiff1d(units, block)
        development = np.random.default_rng(seed+1000*k).permutation(remaining)
        f, c, u = sizes
        assert len(development) >= f+c+u
        fold = dict(fold=k, fit=sorted(development[:f].tolist()), converter=sorted(development[f:f+c].tolist()),
                    uncertainty=sorted(development[f+c:f+c+u].tolist()), evaluation=sorted(block.tolist()))
        groups = [set(fold[name]) for name in ["fit", "converter", "uncertainty", "evaluation"]]
        assert all(a.isdisjoint(b) for j, a in enumerate(groups) for b in groups[j+1:])
        folds.append(fold)
    assert sorted(sum([f["evaluation"] for f in folds], [])) == units.tolist()
    return folds


def subset(inputs, ids):
    return inputs.loc[inputs.unit.isin(ids)].reset_index(drop=True)


def select_config(inputs, group, k):
    """P05 grid and criterion for the empirical HI, on the dedicated configuration group."""
    normaliser = RegimeNormaliser(k=k).fit(subset(inputs, group["fit"]))
    ids = group["fit"]+group["calibration"]+group["selection"]
    data = p10.complete_labels(normaliser.transform(subset(inputs, ids)))
    centred = centred_sensors(data)
    stats = p05.fitting_stats(data, group["fit"], centred)
    z = p05.standardise(centred, stats)
    valid = data.cycle.ge(20).to_numpy()
    cal = (data.unit.isin(group["calibration"]) & data.cycle.ge(20)).to_numpy()
    val = (data.unit.isin(group["selection"]) & data.cycle.ge(20)).to_numpy()
    rows = []
    for tau, gamma, ridge in GRID:
        name = f"t{tau}_g{gamma}_r{ridge:g}"
        coefficients = p05.fit_empirical(data, z, group["fit"], tau=tau, gamma=gamma, ridge=ridge)
        hi = np.full(len(data), np.nan)
        hi[valid] = p05.empirical_hi(z[valid], coefficients)
        converter = IsotonicRegression(increasing=True, y_min=0., out_of_bounds="clip")
        converter.fit(hi[cal], data.loc[cal, "rul"], sample_weight=p05.equal_engine_weights(data.loc[cal, "unit"]))
        predicted = np.full(len(data), np.nan)
        predicted[val] = converter.predict(hi[val])
        rows.append(dict(candidate=name, tau=tau, gamma=gamma, ridge=ridge,
                         selection_rmse=p05.cut_rmse(data, predicted, group["selection"])))
    table = pd.DataFrame(rows)
    best = table.sort_values(["selection_rmse", "candidate"], kind="stable").iloc[0]
    table["chosen"] = table.candidate.eq(best.candidate)
    return dict(tau=int(best.tau), gamma=int(best.gamma), ridge=float(best.ridge)), table


@contextmanager
def registered(key, config):
    assert key not in p10.CONFIG
    p10.CONFIG[key] = config
    try:
        yield
    finally:
        del p10.CONFIG[key]


# ---------------------------------------------------------------- one fold

def regime_diagnostics(normaliser, fit_raw, seed):
    ops = (fit_raw[OPS].to_numpy(float)-normaliser.op_mean)/normaliser.op_std
    labels = normaliser.km.labels_
    rng = np.random.default_rng(seed)
    sample = rng.choice(len(ops), size=min(4000, len(ops)), replace=False)
    other = KMeans(n_clusters=normaliser.k, n_init=20, random_state=normaliser.seed+1).fit(ops).labels_
    silhouette = float(silhouette_score(ops[sample], labels[sample])) if len(set(labels[sample])) > 1 else np.nan
    return dict(silhouette=silhouette, smallest_cluster=int(np.bincount(labels, minlength=normaliser.k).min()),
                seed_agreement_ari=float(adjusted_rand_score(labels, other)))


def run_fold(inputs, partition, key, seed, k):
    raw = {name: subset(inputs, partition[name]) for name in ["fit", "converter", "uncertainty", "evaluation"]}
    normaliser = RegimeNormaliser(k=k).fit(raw["fit"])
    data = {name: normaliser.transform(frame) for name, frame in raw.items()}
    bundle = p10.fit_pipeline(data["fit"], data["converter"], key, seed)
    u_end = data["uncertainty"].groupby("unit").cycle.max()
    u_pred, u_health = p10.predict_inputs(bundle, data["uncertainty"])
    u_pred = p10.attach_labels(u_pred, u_end)
    u_pred["error"] = u_pred.predicted_rul-u_pred.rul
    u_scores, _ = p10.score_engines(u_pred, u_health, data["uncertainty"], u_end, partition["uncertainty"])
    quantiles = p10.calibrate(u_scores)
    e_end = data["evaluation"].groupby("unit").cycle.max()
    e_pred, e_health = p10.predict_inputs(bundle, data["evaluation"])
    e_pred = p10.attach_labels(e_pred, e_end)
    e_pred["error"] = e_pred.predicted_rul-e_pred.rul
    e_scores, e_events = p10.score_engines(e_pred, e_health, data["evaluation"], e_end, partition["evaluation"])
    bands = p10.evaluate_bands(e_pred, e_scores, e_events, quantiles)
    diagnostics = regime_diagnostics(normaliser, raw["fit"], seed)
    diagnostics.update(channels=int(len(bundle["health"]["stats"]["channels"])),
                       calibration_engines=int(u_scores.loc[u_scores.method.eq("ISO") & u_scores.available_path].shape[0]))
    return dict(bundle=bundle, quantiles=quantiles, u_pred=u_pred, u_scores=u_scores, e_pred=e_pred,
                e_scores=e_scores, e_events=e_events, bands=bands, diagnostics=diagnostics, e_end=e_end)


# ---------------------------------------------------------------- decisions

def policy_specs():
    specs = []
    for method in METHODS:
        for delay in (1, 2):
            specs.append(dict(policy_id=f"{method}_POINT_M15_D{delay}", method=method, anchor="point", alpha=0.,
                              reserve=15, delay=delay, phase="primary"))
            specs.append(dict(policy_id=f"{method}_LOWER98_M15_D{delay}", method=method, anchor="lower", alpha=.02,
                              reserve=15, delay=delay, phase="primary"))
            specs.append(dict(policy_id=f"{method}_LOWER98_M12_D{delay}", method=method, anchor="lower", alpha=.02,
                              reserve=12, delay=delay, phase="sensitivity"))
            specs.append(dict(policy_id=f"{method}_LOWER95_M15_D{delay}", method=method, anchor="lower", alpha=.05,
                              reserve=15, delay=delay, phase="sensitivity"))
    for delay in (1, 2):
        specs.append(dict(policy_id=f"HI_MARKER_D{delay}", method="HI", anchor="marker", alpha=0., reserve=0,
                          delay=delay, phase="control"))
        specs.append(dict(policy_id=f"AGE127_D{delay}", method="AGE", anchor="age", alpha=0., reserve=0,
                          delay=delay, phase="control"))
    return specs


def decisions_for(fold_result, domain, repeat, fold):
    quantiles = fold_result["quantiles"]
    prediction = fold_result["e_pred"]
    rows = []
    for unit, endpoint in fold_result["e_end"].items():
        frames = {m: prediction.loc[prediction.unit.eq(unit) & prediction.method.eq(m)] for m in METHODS}
        for spec in policy_specs():
            if spec["method"] in METHODS:
                q = 0.
                if spec["anchor"] == "lower":
                    q = float(quantiles.loc[quantiles.method.eq(spec["method"]) & quantiles.scope.eq("path")
                                            & np.isclose(quantiles.alpha, spec["alpha"]), "q_late"].iloc[0])
                action = p11.decide(frames[spec["method"]], spec["reserve"], spec["delay"], q)
            elif spec["method"] == "HI":
                action = marker_action(frames["ISO"], spec["delay"])
            else:
                action = dict(decision=AGE-spec["delay"], scheduled=AGE, first_available=np.nan,
                              initial_insufficient=False, bound_lead=np.nan, trigger_shortfall=np.nan)
            row = p11.assess(action, endpoint, endpoint, True)
            row.update(spec)
            row.update(subset=domain, dataset="complete", repeat=repeat, fold=fold, unit=int(unit))
            rows.append(row)
    return pd.DataFrame(rows)


def extension_rows(decisions, domain, repeat):
    bases = ["ISO_LOWER98_M15", "RF_SLOPE_LOWER98_M15", "ISO_POINT_M15", "RF_SLOPE_POINT_M15", "HI_MARKER"]
    rows = []
    for base in bases:
        for delay in (1, 2):
            g = decisions.loc[decisions.policy_id.eq(f"{base}_D{delay}")]
            for r in g.itertuples(index=False):
                has = bool(r.has_decision) and np.isfinite(r.decision)
                for u in US:
                    e = engine_expectation(float(r.endpoint), has, float(r.decision) if has else np.nan, delay,
                                           float(r.scheduled) if has else np.nan, u)
                    rows.append(dict(subset=domain, repeat=repeat, fold=r.fold, unit=r.unit, base=base, delay=delay, u=u,
                                     T=float(r.endpoint), **e))
    return pd.DataFrame(rows)


def extension_summary(ex):
    out = []
    for (domain, repeat, base, delay, u), g in ex.groupby(["subset", "repeat", "base", "delay", "u"]):
        n = len(g)
        out.append(dict(subset=domain, repeat=repeat, base=base, delay=delay, u=u, engines=n,
                        mean_life=float(g.util.mean()), rate=float(n/g.util.sum()),
                        saving_vs_127=float(1-AGE*n/g.util.sum()), late_per100=float(100*g.late.mean()),
                        exact_per100=float(100*g.exact.mean()), missing_per100=float(100*g.missing.mean()),
                        age_removal_share=float(g.age_acts.mean()), extended_share=float(g.extended.mean())))
    return pd.DataFrame(out)


def contrasts(decisions, seed=CONFIG_SEED):
    rng = np.random.default_rng(seed)
    rows = []
    for (domain, repeat, policy), g in decisions.groupby(["subset", "repeat", "policy_id"], sort=True):
        delay = int(g.delay.iloc[0])
        if g.method.iloc[0] == "AGE":
            continue
        for reference in [f"AGE127_D{delay}", f"HI_MARKER_D{delay}"]:
            if reference == policy:
                continue
            base = decisions.loc[decisions.subset.eq(domain) & decisions.repeat.eq(repeat) & decisions.policy_id.eq(reference)]
            pair = g.merge(base, on=["unit", "fold"], suffixes=("_p", "_b")).sort_values("unit")
            assert len(pair) == len(g)
            a, b = pair.utilised_p.to_numpy(), pair.utilised_b.to_numpy()
            idx = rng.integers(0, len(pair), size=(BOOT, len(pair)))
            saving = 1-b[idx].mean(axis=1)/a[idx].mean(axis=1)
            rows.append(dict(subset=domain, repeat=repeat, policy_id=policy, reference=reference, delay=delay,
                             common=len(pair), delta_mean_life=float(np.mean(a-b)),
                             relative_saving=float(1-np.mean(b)/np.mean(a)),
                             saving_ci_low=float(np.quantile(saving, .025)), saving_ci_high=float(np.quantile(saving, .975))))
    return pd.DataFrame(rows)


def event_bounds(summary):
    s = summary.loc[summary.dataset.eq("complete")].copy()
    s["late_upper95"] = [cp_upper(int(x), int(n)) for x, n in zip(s.late_count, s.total)]
    s["reached_upper95"] = [cp_upper(int(x), int(n)) for x, n in zip(s.reached_count, s.total)]
    return s


def marker_ranges(scores):
    s = scores.loc[scores.method.eq("ISO") & scores.crossing.notna()]
    wide = s.pivot_table(index=["subset", "unit"], columns="repeat", values="crossing")
    wide["range"] = wide.max(axis=1)-wide.min(axis=1)
    return wide.reset_index()


# ---------------------------------------------------------------- orchestration

def run_domain(inputs, label, out, *, seeds=SEEDS, n_folds=10, sizes=(25, 15, 50), config_sizes=(40, 20, 20), k=6):
    key = f"CONF_{label}"
    group, rest = split_config(inputs.unit.unique(), sizes=config_sizes)
    config, table = select_config(inputs, group, k)
    table.assign(subset=label).to_csv(out / f"config_selection_{label}.csv", index=False)
    (out / f"config_{label}.json").write_text(json.dumps(dict(config=config, group=group, remaining=rest), indent=2), encoding="utf-8")
    records = dict(decisions=[], scores=[], bands=[], quantiles=[], regime=[], events=[])
    splits = []
    with registered(key, config):
        for repeat, seed in enumerate(seeds, start=1):
            for partition in partitions(rest, seed, n_folds, sizes):
                fold = partition["fold"]
                tag = f"{label}_r{repeat}_f{fold}"
                print(tag, flush=True)
                result = run_fold(inputs, partition, key, seed, k)
                joblib.dump(result["bundle"], out / f"models_{tag}.joblib", compress=3)
                result["quantiles"].to_csv(out / f"quantiles_{tag}.csv", index=False)
                result["u_pred"].to_csv(out / f"predictions_{tag}_U.csv.gz", index=False, compression="gzip")
                result["e_pred"].to_csv(out / f"predictions_{tag}_E.csv.gz", index=False, compression="gzip")
                records["decisions"].append(decisions_for(result, label, repeat, fold))
                tags = dict(subset=label, repeat=repeat, fold=fold)
                records["scores"].append(result["e_scores"].assign(**tags))
                records["bands"].append(result["bands"].assign(dataset="complete", **tags))
                records["events"].append(result["e_events"].assign(**tags))
                records["quantiles"].append(result["quantiles"].assign(**tags))
                records["regime"].append(dict(**tags, **result["diagnostics"]))
                splits.append(dict(subset=label, repeat=repeat, seed=seed, **partition))
    (out / f"splits_{label}.json").write_text(json.dumps(splits, indent=2), encoding="utf-8")
    return {name: (pd.concat(v, ignore_index=True) if name != "regime" else pd.DataFrame(v)) for name, v in records.items()}, config


def assemble(parts, out, lives):
    names = ["decisions", "scores", "bands", "quantiles", "regime", "events"]
    frames = {n: pd.concat([p[n] for p in parts], ignore_index=True) for n in names}
    decisions = frames["decisions"]
    summary = p11.summaries(decisions)
    extension = pd.concat([extension_rows(g, d, r) for (d, r), g in decisions.groupby(["subset", "repeat"])], ignore_index=True)
    extension_totals = extension_summary(extension)
    band_summary = p10.band_summary(frames["bands"])
    outputs = dict(decisions=decisions, scores=frames["scores"], bands=frames["bands"], quantiles=frames["quantiles"],
                   regime_diagnostics=frames["regime"], events=frames["events"], summary=event_bounds(summary),
                   contrasts=contrasts(decisions), extension=extension, extension_summary=extension_totals,
                   band_summary=band_summary, marker_ranges=marker_ranges(frames["scores"]))
    for name, frame in outputs.items():
        frame.to_csv(out / f"{name}.csv", index=False)
    criterion = {d: age_criterion(v) for d, v in lives.items()}
    criterion["pooled"] = age_criterion(np.concatenate(list(lives.values())))
    return outputs, criterion


def refresh_manifest(out):
    (out / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(out.iterdir())
                                                  if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")


def previous_integrity():
    records = {}
    for folder in sorted((ROOT / "experiments/artifacts").glob("pilot_*")):
        manifest = folder / "manifest.json"
        if folder.name.startswith("confirmation_19a") or not manifest.exists():
            continue
        for name, digest in json.loads(manifest.read_text(encoding="utf-8")).items():
            assert sha(folder / name) == digest, (folder.name, name)
        records[folder.name] = sha(manifest)
    return records


def execute(domains, out, *, label_note, extra=None, **params):
    out.mkdir(parents=True, exist_ok=True)
    before = previous_integrity()
    sources = {name: sha(ROOT / "experiments" / name) for name in MODULES}
    start = dict(started_utc=datetime.now(timezone.utc).isoformat(), note=label_note, previous_manifests=before,
                 sources=sources, params={k: v for k, v in params.items()}, extra=extra or {})
    (out / "execution_start.json").write_text(json.dumps(start, indent=2, default=str), encoding="utf-8")
    parts, configs, lives = [], {}, {}
    with threadpool_limits(limits=1):
        for label, inputs in domains.items():
            lives[label] = inputs.groupby("unit").cycle.max().to_numpy()
            pd.DataFrame(dict(subset=label, unit=sorted(inputs.unit.unique()), T=inputs.groupby("unit").cycle.max().sort_index().to_numpy())
                         ).to_csv(out / f"lives_{label}.csv", index=False)
            part, config = run_domain(inputs, label, out, **params)
            parts.append(part)
            configs[label] = config
    outputs, criterion = assemble(parts, out, lives)
    (out / "age_limit.json").write_text(json.dumps(criterion, indent=2), encoding="utf-8")
    assert before == previous_integrity()
    meta = start | dict(finished_utc=datetime.now(timezone.utc).isoformat(), previous_manifests_intact=True,
                        configs=configs, age_limit=criterion,
                        packages={n: importlib.metadata.version(n) for n in ["numpy", "pandas", "scikit-learn", "scipy", "joblib"]})
    (out / "metadata.json").write_text(json.dumps(meta, indent=2, default=str), encoding="utf-8")
    refresh_manifest(out)
    return outputs, criterion


# ---------------------------------------------------------------- inputs

def read_train(path):
    raw = pd.read_csv(path, sep=r"\s+", header=None, names=["unit", "cycle", "op1", "op2", "op3"]+SENSORS)
    raw[["unit", "cycle"]] = raw[["unit", "cycle"]].astype(int)
    return raw


def check_lock(emendas=EMENDAS, manifest=MANIFEST, data_dir=ROOT/"CMAPSSData", experiments=ROOT/"experiments", files=None):
    """Lock checks only (amendment hashes and frozen data hashes); does not parse or mark anything."""
    files = files or CONFIRMATION_FILES
    text = Path(emendas).read_text(encoding="utf-8")
    for name in MODULES:
        digest = sha(Path(experiments)/name)
        if f"{name} sha256={digest}" not in text:
            raise PermissionError(f"No pre-opening amendment for the current {name}")
    frozen = json.loads(Path(manifest).read_text(encoding="utf-8"))["dados"]
    expected = {Path(k).name: v["sha256"] for k, v in frozen.items()}
    for filename in files.values():
        if sha(Path(data_dir)/filename) != expected[filename]:
            raise PermissionError(f"{filename} does not match the frozen hash")
    return expected


def open_confirmation(emendas=EMENDAS, manifest=MANIFEST, data_dir=ROOT/"CMAPSSData", out=OUT,
                      experiments=ROOT/"experiments", files=None):
    """The only reader of FD002/FD004. Locked by a pre-opening amendment, matching hashes and a single-use marker."""
    files = files or CONFIRMATION_FILES
    expected = check_lock(emendas, manifest, data_dir, experiments, files)
    marker = Path(out)/"abertura.json"
    if marker.exists():
        raise PermissionError("Confirmation was already opened; see abertura.json and emendas.md")
    Path(out).mkdir(parents=True, exist_ok=True)
    marker.write_text(json.dumps(dict(opened_utc=datetime.now(timezone.utc).isoformat(),
                                      modules={n: sha(Path(experiments)/n) for n in MODULES}, files=expected), indent=2), encoding="utf-8")
    return {label: read_train(Path(data_dir)/filename) for label, filename in files.items()}


def rehearsal_domain():
    """FD001 + FD003 with synthetic six-regime effects: code test only, no scientific claim."""
    from pilot_regime_synthetic_18a import make_synthetic
    a = read_train(ROOT/"CMAPSSData/train_FD001.txt")
    b = read_train(ROOT/"CMAPSSData/train_FD003.txt")
    b = b.assign(unit=b.unit+100)
    synthetic, _, _ = make_synthetic(pd.concat([a, b], ignore_index=True))
    return synthetic.reset_index(drop=True)


def main(argv):
    if argv[:1] == ["--rehearsal"]:
        domains = {"REHEARSAL": rehearsal_domain()}
        outputs, criterion = execute(domains, OUT_REHEARSAL, label_note="code rehearsal on FD001+FD003, synthetic regimes",
                                     seeds=SEEDS[:1], n_folds=5, sizes=(25, 15, 50), config_sizes=(40, 20, 20), k=6)
    elif argv[:1] == ["--confirm"]:
        domains = open_confirmation()
        outputs, criterion = execute(domains, OUT, label_note="single-use confirmation on FD002 and FD004")
    else:
        print("usage: confirmation_19a.py --rehearsal | --confirm")
        return
    print(json.dumps(criterion, indent=2))
    print(outputs["summary"].loc[outputs["summary"].phase.ne("sensitivity"),
          ["subset", "repeat", "policy_id", "total", "decisions", "late_count", "exact_count", "mean_utilised",
           "restorations_per_10000_cycles"]].to_string(index=False))


if __name__ == "__main__":
    main(sys.argv[1:])
