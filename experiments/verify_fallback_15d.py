"""Independent verifier for P15.3: per-engine loop reconstruction with fixed dataset ages, rates and manifests."""
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_fallback_15d"
SRC = ART / "pilot_policy_selection_13a/decisions.csv"
AGES = {"FD001": 127, "FD003": 127}


def main():
    d = pd.read_csv(SRC)
    d = d[d.dataset == "complete"]
    est = pd.read_csv(ART / "pilot_conservative_age_15b/estimates.csv")
    mins = []
    for s in AGES:
        raw = pd.read_csv(ROOT / f"CMAPSSData/train_{s}.txt", sep=r"\s+", header=None, usecols=[0, 1])
        mins.append(raw.groupby(0)[1].max().min())
    assert set(AGES.values()) == {int(min(mins)) - 1}
    hyb = pd.read_csv(OUT / "hybrid_decisions.csv.gz").set_index(["subset", "repeat", "fold", "unit", "base", "delay"])
    original = {(r.subset, r.repeat, r.fold, r.unit, r.policy_id): r for r in d.itertuples(index=False)}
    checked = 0
    for (subset, repeat, fold, unit, base, delay), r in hyb.iterrows():
        o = original[(subset, repeat, fold, unit, f"{base}_D{delay}")]
        T = float(o.endpoint)
        tau = AGES[subset] - delay
        dec_age = tau if (tau >= 1 and tau < T) else None
        dec_phm = float(o.decision) if (o.has_decision and np.isfinite(o.decision)) else None
        cands = [x for x in (dec_phm, dec_age) if x is not None]
        dec = min(cands)
        sched = dec + delay
        status = "late_schedule" if sched > T else "at_endpoint" if sched == T else "preventive_schedule"
        acts = dec_age is not None and (dec_phm is None or dec_age < dec_phm)
        assert r.status == status == "preventive_schedule" and abs(r.utilised - min(sched, T)) < 1e-12 and bool(r.age_acts) == acts
        checked += 1
    summary = pd.read_csv(OUT / "summary.csv")
    for _, s in summary.iterrows():
        g = hyb.xs((s["subset"], s["repeat"], s["base"], s["delay"]), level=("subset", "repeat", "base", "delay"))
        assert abs(s["rate"] - len(g) / g.utilised.sum()) < 1e-12 and s["missing"] == 0 and s["exact"] == 0 and s["strict_late"] == 0
        assert abs(s["fallback_share"] - g.age_acts.mean()) < 1e-12
    for folder in sorted(ART.glob("pilot_*")):
        mf = folder / "manifest.json"
        if folder == OUT or not mf.exists():
            continue
        for n, h in json.loads(mf.read_text(encoding="utf-8")).items():
            assert hashlib.sha256((folder / n).read_bytes()).hexdigest() == h, (folder.name, n)
    result = dict(status="passed", hybrid_rows_rebuilt=checked, summary_rows=len(summary))
    (OUT / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
