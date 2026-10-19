"""P15.4: PHM -> age fallback with the dataset-level conservative ages of P15.2 (train files only)."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import pilot_fallback_15a as f15a

ROOT = f15a.ROOT
ART = f15a.ART
OUT = ART / "pilot_fallback_15d"
AGES = {"FD001": 127, "FD003": 127}
SOURCES = ["protocolo_reserva_idade_15d.md", "pilot_fallback_15d.py", "test_fallback_15d.py", "verify_fallback_15d.py"]
sha, integrity = f15a.sha, None


def integrity_check(skip):
    records = {}
    for folder in sorted(ART.glob("pilot_*")):
        manifest = folder / "manifest.json"
        if folder == skip or not manifest.exists():
            continue
        for name, digest in json.loads(manifest.read_text(encoding="utf-8")).items():
            assert sha(folder / name) == digest, (folder.name, name)
        records[folder.name] = sha(manifest)
    return records


def build():
    d = pd.read_csv(f15a.SRC)
    d = d[d.dataset == "complete"].copy()
    rows = []
    for (subset, repeat, fold), g in d.groupby(["subset", "repeat", "fold"]):
        for delay in (1, 2):
            for base in f15a.BASES:
                b = g[g.policy_id == f"{base}_D{delay}"].sort_values("unit")
                h = f15a.hybrid(b, pd.Series(AGES[subset], index=b.index), delay)
                rows.append(b[["subset", "repeat", "fold", "unit"]].assign(base=base, delay=delay, q=-1.0, age=AGES[subset],
                                                                          **{c: h[c] for c in h}))
    return pd.concat(rows, ignore_index=True), d


def references(h, d):
    refs = {}
    for (subset, repeat, delay), g in h.groupby(["subset", "repeat", "delay"]):
        order = g[g.base == f15a.BASES[0]].sort_values(["fold", "unit"])[["fold", "unit"]]
        for name in ("AGE", "HI_MARKER"):
            r = d[(d.subset == subset) & (d.repeat == repeat) & (d.policy_id == f"{name}_D{delay}")]
            r = order.merge(r[["fold", "unit", "utilised"]], on=["fold", "unit"], how="left")
            assert r.utilised.notna().all()
            refs[(subset, repeat, delay, name)] = r.utilised.to_numpy(float)
    return refs


def pooled_bounds():
    import math
    def cp(k, n, conf):
        lo, hi = 0.0, 1.0
        for _ in range(200):
            mid = (lo + hi) / 2
            cdf = sum(math.comb(n, i) * mid ** i * (1 - mid) ** (n - i) for i in range(k + 1))
            lo, hi = (mid, hi) if cdf > 1 - conf else (lo, mid)
        return (lo + hi) / 2
    ends = f15a.endpoints()
    t = np.concatenate([ends[s].to_numpy(float) for s in f15a.SUBSETS])
    k = int((t <= 127).sum())
    rows = [dict(sample="FD001+FD003", n=len(t), hits=k, confidence=c, upper=cp(k, len(t), c)) for c in (0.80, 0.90, 0.95)]
    rows += [dict(sample="FD001 sozinho", n=100, hits=int((ends["FD001"].to_numpy() <= 127).sum()), confidence=0.95, upper=cp(0, 100, 0.95))]
    rows += [dict(sample="hipotetico FD001-FD004, n=709, 0 ocorrencias", n=709, hits=0, confidence=0.95, upper=cp(0, 709, 0.95))]
    return pd.DataFrame(rows)


def main():
    OUT.mkdir(exist_ok=True)
    previous = integrity_check(OUT)
    (OUT / "execution_start.json").write_text(json.dumps(dict(
        started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=previous, ages=AGES,
        inputs={str(p.relative_to(ROOT)): sha(p) for p in f15a.input_files()},
        sources={n: sha(ROOT / "experiments" / n) for n in SOURCES}), indent=2), encoding="utf-8")
    h, d = build()
    summary = f15a.summarise(h, d)
    refs = references(h, d)
    sav = f15a.savings(h, refs)
    central = f15a.central_scenario(h, None)
    pooled_bounds().to_csv(OUT / "pooled_bounds.csv", index=False)
    h.to_csv(OUT / "hybrid_decisions.csv.gz", index=False)
    summary.to_csv(OUT / "summary.csv", index=False)
    sav.to_csv(OUT / "savings.csv", index=False)
    central.to_csv(OUT / "central_scenario.csv", index=False)
    for n in SOURCES:
        (OUT / f"source_{n}").write_bytes((ROOT / "experiments" / n).read_bytes())
    assert integrity_check(OUT) == previous
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                   if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")
    pd.set_option("display.width", 220)
    print(pooled_bounds().round(5).to_string(index=False))
    print(summary.groupby(["subset", "base", "delay"]).agg(fb=("fallback_share", "mean"), life=("mean_utilised", "mean"),
          orig=("original_mean_utilised", "mean"), miss=("missing", "sum"), exact=("exact", "sum"), late=("strict_late", "sum")).round(3).to_string())
    print(sav[sav.delay == 1].groupby(["subset", "base", "reference"]).saving.mean().unstack().round(4).to_string())
    print(central[(central.delay == 1) & (central.L_ref == 8425)].groupby(["subset", "base", "llp"]).visits.mean().unstack().round(2).to_string())


if __name__ == "__main__":
    main()
