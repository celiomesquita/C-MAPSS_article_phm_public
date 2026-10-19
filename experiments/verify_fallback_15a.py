"""Independent verifier for P15.1: per-engine loop reconstruction of hybrid decisions, rates, savings and manifests."""
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_fallback_15a"
SRC = ART / "pilot_policy_selection_13a/decisions.csv"
SPLITS = ART / "pilot_f_uncertainty_10/splits.json"
SUBSETS = ("FD001", "FD003")
BASES = ("ISO_LOWER98_M15", "RF_SLOPE_LOWER98_M15", "ISO_POINT_M15", "RF_SLOPE_POINT_M15", "HI_MARKER",
         "HI_THRESHOLD_SELECTED", "HI_WAIT_SELECTED")
QS = (0.0, 0.05, 0.10, 0.25, 0.50)


def main():
    d = pd.read_csv(SRC)
    d = d[d.dataset == "complete"]
    ends = {}
    for s in SUBSETS:
        raw = pd.read_csv(ROOT / f"CMAPSSData/train_{s}.txt", sep=r"\s+", header=None, usecols=[0, 1], names=["unit", "cycle"])
        ends[s] = raw.groupby("unit").cycle.max().to_dict()
    # fallback ages by plain sorting and nearest-rank-lower interpolation
    ages = {}
    for e in json.loads(SPLITS.read_text(encoding="utf-8")):
        dev = sorted(ends[e["subset"]][u] for u in list(e["fit"]) + list(e["converter"]))
        for q in QS:
            pos = q * (len(dev) - 1)
            lo = int(np.floor(pos))
            value = dev[lo] + (pos - lo) * (dev[min(lo + 1, len(dev) - 1)] - dev[lo])
            ages[(e["subset"], e["repeat"], e["fold"], q)] = int(np.floor(value)) - 1
    saved = pd.read_csv(OUT / "fallback_ages.csv")
    for _, r in saved.iterrows():
        assert ages[(r["subset"], int(r["repeat"]), int(r["fold"]), r["q"])] == int(r["age"])
    hyb = pd.read_csv(OUT / "hybrid_decisions.csv.gz")
    hyb = hyb.set_index(["subset", "repeat", "fold", "unit", "base", "delay", "q"])
    checked = 0
    original = {}
    for row in d.itertuples(index=False):
        original[(row.subset, row.repeat, row.fold, row.unit, row.policy_id)] = row
    for (subset, repeat, fold, unit, base, delay, q), r in hyb.iterrows():
        o = original[(subset, repeat, fold, unit, f"{base}_D{delay}")]
        T = float(o.endpoint)
        a = ages[(subset, repeat, fold, q)]
        tau = a - delay
        dec_age = tau if (tau >= 1 and tau < T) else None
        dec_phm = float(o.decision) if (o.has_decision and np.isfinite(o.decision)) else None
        cands = [x for x in (dec_phm, dec_age) if x is not None]
        dec = min(cands) if cands else None
        if dec is None:
            status, sched, util = "endpoint_without_decision", None, T
        else:
            sched = dec + delay
            status = "late_schedule" if sched > T else "at_endpoint" if sched == T else "preventive_schedule"
            util = min(sched, T)
        acts = dec_age is not None and (dec_phm is None or dec_age < dec_phm)
        assert r.status == status and abs(r.utilised - util) < 1e-12 and bool(r.age_acts) == acts, (subset, repeat, fold, unit, base, delay, q)
        checked += 1
    summary = pd.read_csv(OUT / "summary.csv")
    for _, s in summary.iterrows():
        g = hyb.xs((s["subset"], s["repeat"], s["base"], s["delay"], s["q"]), level=("subset", "repeat", "base", "delay", "q"))
        assert abs(s["rate"] - len(g) / g.utilised.sum()) < 1e-12
        assert s["missing"] == (g.status == "endpoint_without_decision").sum()
        assert s["exact"] == (g.status == "at_endpoint").sum() and s["strict_late"] == (g.status == "late_schedule").sum()
        assert abs(s["fallback_share"] - g.age_acts.mean()) < 1e-12
    sav = pd.read_csv(OUT / "savings.csv")
    for _, s in sav.sample(200, random_state=1).iterrows():
        g = hyb.xs((s["subset"], s["repeat"], s["base"], s["delay"], s["q"]), level=("subset", "repeat", "base", "delay", "q"))
        ref = d[(d.subset == s["subset"]) & (d.repeat == s["repeat"]) & (d.policy_id == f"{s['reference']}_D{int(s['delay'])}")]
        point = 1 - ref.utilised.sum() / g.utilised.sum()
        assert abs(point - s["saving"]) < 1e-12 and s["saving_lo"] <= s["saving"] + 1e-9
    for folder in sorted(ART.glob("pilot_*")):
        mf = folder / "manifest.json"
        if folder == OUT or not mf.exists():
            continue
        for n, h in json.loads(mf.read_text(encoding="utf-8")).items():
            assert hashlib.sha256((folder / n).read_bytes()).hexdigest() == h, (folder.name, n)
    result = dict(status="passed", hybrid_rows_rebuilt=checked, summary_rows=len(summary), savings_rows_spot_checked=200, fallback_ages=len(saved))
    (OUT / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
