"""P11: causal removal replay from frozen P10 forecasts; no refitting or inspection."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "experiments/artifacts/pilot_f_uncertainty_10"
OUT = ROOT / "experiments/artifacts/pilot_removal_11"
EPS = 1e-9
SEED = 20261017


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def integrity():
    manifests = {}
    for folder in sorted((ROOT / "experiments/artifacts").glob("pilot_*")):
        manifest = folder / "manifest.json"
        if folder == OUT or not manifest.exists():
            continue
        for name, digest in json.loads(manifest.read_text(encoding="utf-8")).items():
            assert sha(folder / name) == digest, (folder.name, name)
        manifests[folder.name] = sha(manifest)
    return manifests


def read_inputs(kind, subset):
    raw = pd.read_csv(ROOT / f"CMAPSSData/{kind}_{subset}.txt", sep=r"\s+", header=None)
    return raw.rename(columns={0: "unit", 1: "cycle"})


def configurations():
    rules = []
    for method in ["ISO", "RF_SLOPE"]:
        for anchor, alpha in [("point", 0.), ("lower", .02), ("lower", .05)]:
            for reserve in [15, 12]:
                for delay in [1, 2]:
                    level = "POINT" if anchor == "point" else f"LOWER{round(100*(1-alpha))}"
                    rules.append(dict(policy_id=f"{method}_{level}_M{reserve}_D{delay}", method=method,
                                      anchor=anchor, alpha=alpha, reserve=reserve, delay=delay,
                                      phase="sensitivity" if alpha == .05 else "primary"))
    for delay in [1, 2]:
        rules.append(dict(policy_id=f"AGE_D{delay}", method="AGE", anchor="age", alpha=0.,
                          reserve=0, delay=delay, phase="control"))
    assert len(rules) == 26
    return rules


def fixed_age(endpoints, development):
    return int(endpoints.loc[development].min())-1


def decide(frame, reserve, delay, q_late=0.):
    # Only current/past sensor-derived predictors enter this decision.
    g = frame.loc[frame.in_domain].sort_values("cycle")
    if g.empty:
        return dict(decision=np.nan, scheduled=np.nan, first_available=np.nan,
                    initial_insufficient=False, bound_lead=np.nan, trigger_shortfall=np.nan)
    leads = np.maximum(0., g.predicted_rul.to_numpy()-q_late)
    hits = np.flatnonzero(leads <= reserve+delay+EPS)
    record = dict(decision=np.nan, scheduled=np.nan, first_available=int(g.cycle.iloc[0]),
                  initial_insufficient=bool(leads[0] < reserve+delay-EPS),
                  bound_lead=np.nan, trigger_shortfall=np.nan)
    if len(hits):
        k = hits[0]
        record.update(decision=int(g.cycle.iloc[k]), scheduled=int(g.cycle.iloc[k])+delay,
                      bound_lead=float(leads[k]), trigger_shortfall=float(max(0., reserve+delay-leads[k])))
    return record


def assess(action, endpoint, last, complete):
    has_decision = bool(np.isfinite(action["decision"]))
    scheduled = action["scheduled"]
    late = bool(scheduled > endpoint) if has_decision else False
    exact = bool(scheduled == endpoint) if has_decision else False
    reached = bool(scheduled >= endpoint or not has_decision) if complete else np.nan
    status = ("late_schedule" if late else "at_endpoint" if exact else "preventive_schedule") if has_decision else (
        "endpoint_without_decision" if complete else "right_censored")
    return action | dict(endpoint=int(endpoint), last_observed=int(last), has_decision=has_decision,
                         status=status, late=late, exact_endpoint=exact, reached_endpoint=reached,
                         execution_observed=bool(has_decision and scheduled < endpoint and scheduled <= last),
                         late_amount=float(max(0., scheduled-endpoint)) if has_decision else np.nan,
                         real_reserve=float(endpoint-scheduled) if has_decision else np.nan,
                         utilised=float(min(scheduled, endpoint) if has_decision else endpoint) if complete else np.nan,
                         unused=float(max(0., endpoint-scheduled)) if has_decision and complete else np.nan)


def summaries(decisions):
    rows = []
    for key, g in decisions.groupby(["subset", "dataset", "repeat", "policy_id"], sort=True):
        available = g.loc[g.has_decision]
        row = dict(zip(["subset", "dataset", "repeat", "policy_id"], key))
        for col in ["method", "anchor", "alpha", "reserve", "delay", "phase"]:
            row[col] = g[col].iloc[0]
        row.update(total=len(g), decisions=len(available), without_decision=int((~g.has_decision).sum()),
                   late_count=int(g.late.sum()), exact_count=int(g.exact_endpoint.sum()),
                   initial_insufficient_count=int(g.initial_insufficient.sum()),
                   conditional_late_fraction=float(available.late.mean()) if len(available) else np.nan,
                   median_real_reserve=float(available.real_reserve.median()),
                   observed_executions=int(g.execution_observed.sum()))
        if key[1] == "complete":
            n, exposure = len(g), float(g.utilised.sum())
            row.update(late_fraction=float(g.late.mean()), reached_count=int(g.reached_endpoint.sum()),
                       mean_utilised=float(g.utilised.mean()), mean_unused=float((g.endpoint-g.utilised).mean()),
                       cost_per_cycle=n/exposure, restorations_per_10000_cycles=10000*n/exposure,
                       passes_strict_screen=bool(len(available) == n and g.late.mean() <= .02+EPS),
                       passes_prudent_screen=bool(len(available) == n and g.late.mean() <= .02+EPS and not g.exact_endpoint.any()))
        rows.append(row)
    return pd.DataFrame(rows)


def paired_comparisons(decisions):
    rng = np.random.default_rng(SEED)
    rows = []
    complete = decisions.loc[decisions.dataset.eq("complete")]
    for key, g in complete.loc[complete.method.ne("AGE")].groupby(["subset", "repeat", "policy_id"], sort=True):
        subset, repeat, policy_id = key
        delay = int(g.delay.iloc[0])
        age = complete.loc[complete.subset.eq(subset) & complete.repeat.eq(repeat) & complete.policy_id.eq(f"AGE_D{delay}")]
        pair = g.merge(age, on=["unit", "fold"], suffixes=("_p", "_b")).sort_values("unit")
        assert len(pair) == 100
        a, b = pair.utilised_p.to_numpy(), pair.utilised_b.to_numpy()
        indices = rng.integers(0, len(pair), size=(2000, len(pair)))
        life_delta = (a[indices]-b[indices]).mean(axis=1)
        saving = 1-b[indices].mean(axis=1)/a[indices].mean(axis=1)
        rows.append(dict(subset=subset, repeat=repeat, policy_id=policy_id, delay=delay, common=len(pair),
                         delta_mean_life=float(np.mean(a-b)), life_ci_low=float(np.quantile(life_delta, .025)),
                         life_ci_high=float(np.quantile(life_delta, .975)),
                         relative_saving=float(1-np.mean(b)/np.mean(a)),
                         saving_ci_low=float(np.quantile(saving, .025)), saving_ci_high=float(np.quantile(saving, .975))))
    return pd.DataFrame(rows)


def frontier(summary):
    data = summary.loc[summary.dataset.eq("complete") & summary.phase.ne("sensitivity")].copy()
    data["non_dominated"] = False
    for _, g in data.groupby(["subset", "repeat", "delay"]):
        # Minimise missing decisions, late/exact schedules and unused lifetime.
        matrix = g[["without_decision", "late_count", "exact_count", "mean_unused"]].to_numpy(float)
        for j, idx in enumerate(g.index):
            dominated = np.any(np.all(matrix <= matrix[j]+EPS, axis=1) & np.any(matrix < matrix[j]-EPS, axis=1))
            data.loc[idx, "non_dominated"] = not dominated
    return data


def refresh_manifest():
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                  if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert not (OUT / "metadata.json").exists(), "Existing completed run must be preserved"
    before = integrity()
    splits = json.loads((SOURCE / "splits.json").read_text(encoding="utf-8"))
    rules = configurations()
    files = [Path(__file__), ROOT / "experiments/protocolo_remocao_11.md",
             ROOT / "experiments/test_pilot_removal_11.py", ROOT / "experiments/verify_pilot_removal_11.py",
             SOURCE / "splits.json", SOURCE / "quantiles.csv", SOURCE / "manifest.json"]
    files += sorted(SOURCE.glob("predictions_*_complete.csv.gz"))+sorted(SOURCE.glob("predictions_*_truncated.csv.gz"))
    files += [ROOT / f"CMAPSSData/{kind}_{subset}.txt" for subset in ["FD001", "FD003"] for kind in ["train", "test", "RUL"]]
    initial = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=before,
                   inputs={str(p.relative_to(ROOT)): sha(p) for p in files}, rules=rules, tolerance=EPS)
    (OUT / "execution_start.json").write_text(json.dumps(initial, indent=2), encoding="utf-8")
    quantiles = pd.read_csv(SOURCE / "quantiles.csv")
    decisions, controls = [], []
    train = {s: read_inputs("train", s).groupby("unit").cycle.max() for s in ["FD001", "FD003"]}
    for split in splits:
        subset, repeat, fold = split["subset"], split["repeat"], split["fold"]
        tag = f"{subset}_r{repeat}_f{fold}"
        ids = sorted(split["fit"]+split["converter"])
        age = fixed_age(train[subset], ids)
        controls.append(dict(subset=subset, repeat=repeat, fold=fold, development=ids, age=age,
                             minimum_development_endpoint=age+1, frozen_utc=datetime.now(timezone.utc).isoformat()))
        (OUT / "controls.json").write_text(json.dumps(controls, indent=2), encoding="utf-8")
        qrows = quantiles.loc[quantiles.subset.eq(subset) & quantiles.repeat.eq(repeat) & quantiles.fold.eq(fold) & quantiles.scope.eq("path")]
        for dataset in ["complete"]+(["truncated"] if fold == 1 else []):
            pred = pd.read_csv(SOURCE / f"predictions_{tag}_{dataset}.csv.gz")
            if dataset == "complete":
                endpoints = train[subset].loc[split["evaluation"]]
                lasts = endpoints
            else:
                lasts = read_inputs("test", subset).groupby("unit").cycle.max()
                endpoints = lasts+pd.Series(np.loadtxt(ROOT / f"CMAPSSData/RUL_{subset}.txt"), index=np.arange(1, 101))
            for unit in endpoints.index:
                endpoint, last = int(endpoints.loc[unit]), int(lasts.loc[unit])
                frames = {method: pred.loc[pred.unit.eq(unit) & pred.method.eq(method) & pred.cycle.lt(endpoint),
                                          ["unit", "cycle", "predicted_rul", "in_domain"]].copy()
                          for method in ["ISO", "RF_SLOPE"]}
                for rule in rules:
                    q = 0.
                    if rule["method"] == "AGE":
                        tau = age-rule["delay"]
                        assert tau >= 1
                        observed = tau <= last and tau < endpoint
                        action = dict(decision=tau if observed else np.nan, scheduled=age if observed else np.nan,
                                      first_available=1, initial_insufficient=False, bound_lead=np.nan, trigger_shortfall=np.nan)
                    else:
                        if rule["anchor"] == "lower":
                            q = float(qrows.loc[qrows.method.eq(rule["method"]) & np.isclose(qrows.alpha, rule["alpha"]), "q_late"].iloc[0])
                        action = decide(frames[rule["method"]], rule["reserve"], rule["delay"], q)
                    decisions.append(dict(subset=subset, repeat=repeat, fold=fold, dataset=dataset, unit=int(unit),
                                          q_late=q, control_age=age, **rule, **assess(action, endpoint, last, dataset == "complete")))
        print(tag, "replayed", flush=True)
    frame = pd.DataFrame(decisions)
    summary = summaries(frame)
    for name, data in [("decisions", frame), ("summary", summary), ("contrasts", paired_comparisons(frame)),
                        ("frontier", frontier(summary))]:
        data.to_csv(OUT / f"{name}.csv", index=False)
    assert integrity() == before
    metadata = initial | dict(finished_utc=datetime.now(timezone.utc).isoformat(), prior_artifacts_intact=True,
                             no_refitting=True, no_inspection=True, no_calendar_projection=True,
                             decision_rows=len(frame), configurations=len(rules), controls=len(controls))
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    refresh_manifest()
    print(summary.loc[summary.dataset.eq("complete") & summary.phase.ne("sensitivity"),
                      ["subset", "repeat", "policy_id", "late_count", "exact_count", "without_decision",
                       "mean_utilised", "passes_strict_screen"]].to_string(index=False))


if __name__ == "__main__":
    main()
