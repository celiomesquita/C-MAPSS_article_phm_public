"""P17.1: simulated borescope arm (protocolo_inspecao_17b.md). Archived decisions only; exact expectations."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_inspection_17b"
SOURCES = {"development": ART / "pilot_policy_selection_13a/decisions.csv",
           "confirmation": ART / "confirmation_19a/decisions.csv"}
MODULES = ["protocolo_inspecao_17b.md", "inspection_arm_17b.py", "test_inspection_arm_17b.py", "verify_inspection_arm_17b.py"]
AGE = 127
STEP = 5
US = (0.0, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 1.0)
BASES = ["ISO_POINT_M15", "RF_SLOPE_POINT_M15", "ISO_LOWER98_M15", "RF_SLOPE_LOWER98_M15", "HI_MARKER"]
PRIMARY = {"ISO_POINT_M15", "RF_SLOPE_POINT_M15"}
BOOT, SEED = 2000, 20261018


def scenarios():
    s = [dict(scenario="S2_W60_g1", entry="S2", W=60, gamma=1., p_P=0., p_F=1.)]
    for W in (30, 80):
        s.append(dict(scenario=f"S2_W{W}_g1", entry="S2", W=W, gamma=1., p_P=0., p_F=1.))
    for g in (0.26, 2.):
        s.append(dict(scenario=f"S2_W60_g{g:g}", entry="S2", W=60, gamma=g, p_P=0., p_F=1.))
    s.append(dict(scenario="S2_W60_g1_pP0.02", entry="S2", W=60, gamma=1., p_P=.02, p_F=1.))
    for W in (30, 60, 80):
        s.append(dict(scenario=f"S1_W{W}_g1", entry="S1", W=W, gamma=1., p_P=0., p_F=1.))
    return s


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def reject_probability(T, t, W, gamma, p_P, p_F):
    q = 1.-np.clip((T-np.asarray(t, float))/W, 0., 1.)
    return p_P+(p_F-p_P)*q**gamma


def inspection_times(T, entry, W):
    start = AGE if entry == "S2" else max(1, int(T)-int(W))
    return np.arange(start, int(T), STEP)          # T is not an inspection opportunity


def hybrid_expectation(T, has, D, d, u, entry, W, gamma, p_P, p_F):
    """Exact expectations for one engine; hybrid = PHM + inspection (rejection only advances the decision)."""
    T, tau = int(T), AGE-d
    times = inspection_times(T, entry, W)
    start = min(tau, int(times[0])) if len(times) else tau
    if has and int(D) < start:                      # PHM decided before any monitoring check or inspection
        sched = int(D)+d
        return dict(util=float(min(sched, T)), late=float(sched > T), exact=float(sched == T), missing=0.,
                    inspections=0., rejection=0.)
    end = int(D) if has else T-1
    t = np.arange(start, end+1)
    valid_loss = np.where(t >= tau, u, 0.)
    in_grid = np.isin(t, times)
    phm = (t == D) if has else np.zeros(len(t), bool)
    p = np.where(in_grid & ~phm, reject_probability(T, t, W, gamma, p_P, p_F), 0.)
    hazard = valid_loss+(1.-valid_loss)*np.where(phm, 1., p)
    survive = np.concatenate([[1.], np.cumprod(1.-hazard)])[:-1]
    first = survive*hazard
    sched = t+d
    tail = 0. if has else float(np.prod(1.-hazard))
    return dict(util=float((first*np.minimum(sched, T)).sum()+tail*T),
                late=float((first*(sched > T)).sum()), exact=float((first*(sched == T)).sum()), missing=tail,
                inspections=float((survive*(1.-valid_loss)*(in_grid & ~phm)).sum()),
                rejection=float((survive*(1.-valid_loss)*p).sum()))


def _phm(T, has, D, d, u):
    T, tau = int(T), AGE-d
    if has and int(D) <= tau:
        sched = int(D)+d
        return dict(util=float(min(sched, T)), late=float(sched > T), exact=float(sched == T), missing=0.)
    end = int(D) if has else T-1
    t = np.arange(tau, end+1)
    hazard = np.full(len(t), float(u))
    if has:
        hazard[-1] = 1.
    survive = np.concatenate([[1.], np.cumprod(1.-hazard)])[:-1]
    first = survive*hazard
    sched = t+d
    tail = 0. if has else float(np.prod(1.-hazard))
    return dict(util=float((first*np.minimum(sched, T)).sum()+tail*T), late=float((first*(sched > T)).sum()),
                exact=float((first*(sched == T)).sum()), missing=tail)


def load_decisions():
    frames = []
    for origin, path in SOURCES.items():
        d = pd.read_csv(path)
        d = d.loc[d.dataset.eq("complete")]
        d = d.assign(origin=origin)
        frames.append(d)
    d = pd.concat(frames, ignore_index=True)
    keep = []
    for base in BASES:
        for delay in (1, 2):
            keep.append(f"{base}_D{delay}")
    d = d.loc[d.policy_id.isin(keep)]
    return d[["origin", "subset", "repeat", "fold", "unit", "policy_id", "delay", "decision", "scheduled", "has_decision",
              "endpoint"]].reset_index(drop=True)


def expectations(decisions):
    rows = []
    configs = scenarios()
    for r in decisions.itertuples(index=False):
        has = bool(r.has_decision)
        D = float(r.decision) if has else np.nan
        base = r.policy_id.rsplit("_D", 1)[0]
        for cfg in configs:
            for u in (US if cfg["scenario"] == "S2_W60_g1" else (0.,)):
                h = hybrid_expectation(r.endpoint, has, D, int(r.delay), u, cfg["entry"], cfg["W"], cfg["gamma"],
                                       cfg["p_P"], cfg["p_F"])
                p = _phm(r.endpoint, has, D, int(r.delay), u)
                rows.append(dict(origin=r.origin, subset=r.subset, repeat=r.repeat, fold=r.fold, unit=r.unit, base=base,
                                 delay=int(r.delay), scenario=cfg["scenario"], u=u, T=int(r.endpoint),
                                 util_h=h["util"], late_h=h["late"], exact_h=h["exact"], missing_h=h["missing"],
                                 inspections=h["inspections"], rejection=h["rejection"],
                                 util_p=p["util"], late_p=p["late"], exact_p=p["exact"], missing_p=p["missing"]))
    return pd.DataFrame(rows)


def summarise(ex):
    rng = np.random.default_rng(SEED)
    rows = []
    keys = ["origin", "subset", "repeat", "base", "delay", "scenario", "u"]
    for key, g in ex.groupby(keys, sort=True):
        n = len(g)
        a, b = g.util_h.to_numpy(), g.util_p.to_numpy()
        idx = rng.integers(0, n, size=(BOOT, n))
        change = a[idx].sum(axis=1)**-1*b[idx].sum(axis=1)-1.      # rate_h / rate_p - 1 = sum(util_p)/sum(util_h) - 1
        rows.append(dict(zip(keys, key)) | dict(
            engines=n, rate_h_per_10000=float(10000*n/a.sum()), rate_p_per_10000=float(10000*n/b.sum()),
            rate_change=float(b.sum()/a.sum()-1.), rate_change_low=float(np.quantile(change, .025)),
            rate_change_high=float(np.quantile(change, .975)), life_ceded=float((b-a).mean()),
            late_h_per100=float(100*g.late_h.mean()), exact_h_per100=float(100*g.exact_h.mean()),
            missing_h_per100=float(100*g.missing_h.mean()), late_p_per100=float(100*g.late_p.mean()),
            exact_p_per100=float(100*g.exact_p.mean()), missing_p_per100=float(100*g.missing_p.mean()),
            inspections_per_engine=float(g.inspections.mean()), rejection_share=float(g.rejection.mean()),
            saving_vs_127=float(1-AGE*n/a.sum()), saving_vs_127_phm=float(1-AGE*n/b.sum())))
    return pd.DataFrame(rows)


def refresh_manifest(out):
    (out/"manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(out.iterdir())
                                                 if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")


def previous_integrity():
    records = {}
    for folder in sorted(ART.glob("pilot_*")):
        manifest = folder/"manifest.json"
        if folder == OUT or not manifest.exists():
            continue
        for name, digest in json.loads(manifest.read_text(encoding="utf-8")).items():
            assert sha(folder/name) == digest, (folder.name, name)
        records[folder.name] = sha(manifest)
    return records


def main():
    assert not (OUT/"metadata.json").exists(), "completed run must be preserved"
    OUT.mkdir(parents=True, exist_ok=True)
    before = previous_integrity()
    confirmation = ART/"confirmation_19a/manifest.json"
    for name, digest in json.loads(confirmation.read_text(encoding="utf-8")).items():
        assert sha(confirmation.parent/name) == digest, name
    start = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=before,
                 sources={n: sha(ROOT/"experiments"/n) for n in MODULES},
                 inputs={k: sha(v) for k, v in SOURCES.items()}, scenarios=scenarios())
    (OUT/"execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    decisions = load_decisions()
    ex = expectations(decisions)
    summary = summarise(ex)
    ex.to_csv(OUT/"expectations.csv.gz", index=False, compression="gzip")
    summary.to_csv(OUT/"summary.csv", index=False)
    assert before == previous_integrity()
    (OUT/"metadata.json").write_text(json.dumps(start | dict(finished_utc=datetime.now(timezone.utc).isoformat(),
                                    rows=len(ex), previous_manifests_intact=True), indent=2), encoding="utf-8")
    refresh_manifest(OUT)
    head = summary.loc[summary.scenario.eq("S2_W60_g1") & summary.u.eq(0.) & summary.delay.eq(1) & summary.repeat.eq(1)]
    pd.set_option("display.width", 220)
    print(head[["origin", "subset", "base", "rate_change", "rate_change_low", "rate_change_high", "life_ceded",
                "late_h_per100", "late_p_per100", "exact_h_per100", "exact_p_per100", "missing_h_per100",
                "missing_p_per100", "inspections_per_engine", "rejection_share"]].round(3).to_string(index=False))


if __name__ == "__main__":
    main()
