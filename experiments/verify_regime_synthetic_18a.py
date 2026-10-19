"""Independent verifier for P18.1: regenerates the synthetic data, per-regime statistics and the summary tables."""
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_regime_synthetic_18a"
NAMES = ["unit", "cycle", "op1", "op2", "op3"] + [f"s{i}" for i in range(1, 22)]
SENS = NAMES[5:]


def main():
    base = pd.read_csv(ROOT / "CMAPSSData/train_FD001.txt", sep=r"\s+", header=None, names=NAMES)
    rng = np.random.default_rng(20261018)
    centres = np.column_stack([rng.uniform(0, 42, 6), rng.uniform(0, 0.84, 6), rng.uniform(20, 100, 6)])
    regimes = rng.integers(0, 6, len(base))
    sigma = base[SENS].std(ddof=1).to_numpy()
    live = sigma > 1e-9
    shift = rng.normal(0.0, 1.0, (6, 21)) * (3 * sigma)
    factor = rng.uniform(0.9, 1.1, (6, 21))
    shift[:, ~live] = 0.0
    factor[:, ~live] = 1.0
    noise = rng.normal(0.0, 1.0, (len(base), 3)) * np.array([0.05, 0.002, 0.2])
    ops = centres[regimes] + noise
    sens = base[SENS].to_numpy(float) * factor[regimes] + shift[regimes]
    saved = json.loads((OUT / "synthetic_checksum.json").read_text(encoding="utf-8"))
    assert abs(sens.sum() - saved["sensors_sum"]) < 1e-6 * abs(saved["sensors_sum"])
    assert abs(ops.sum() - saved["ops_sum"]) < 1e-6 * abs(saved["ops_sum"]) and int(regimes.sum()) == saved["regimes_sum"]
    eff = np.load(OUT / "synthetic_effects.npz")
    np.testing.assert_allclose(eff["shift"], shift)
    np.testing.assert_allclose(eff["factor"], factor)
    # per-regime healthy statistics with true labels on a stand-in set of fitting engines
    import sys
    sys.path.insert(0, str(ROOT / "experiments"))
    from regime_normalisation import RegimeNormaliser
    syn = base.copy()
    syn[["op1", "op2", "op3"]] = ops
    syn[SENS] = sens
    fit = syn[syn.unit <= 25]
    lab = pd.Series(regimes, index=syn.index)
    z = RegimeNormaliser(k=6, labels=lab).fit(fit).transform(fit)
    healthy = (fit.cycle <= 20).to_numpy()
    for c in range(6):
        rows = healthy & (regimes[fit.index] == c)
        for j, s in enumerate(SENS):
            vals = fit[s].to_numpy(float)[rows]
            sd = vals.std(ddof=1)
            sd = 1.0 if sd < 1e-9 else sd
            expected = (fit[s].to_numpy(float) - vals.mean()) / sd
            sel = (regimes[fit.index] == c)
            assert np.allclose(z[s].to_numpy()[sel], expected[sel], atol=1e-9), (c, s)
    # summary tables recomputed from per-engine metrics
    pe = pd.read_csv(OUT / "per_engine.csv")
    summary = pd.read_csv(OUT / "summary.csv").set_index("variant")
    for variant, g in pe.groupby("variant"):
        s = summary.loc[variant]
        assert s.engines == len(g) == 100
        assert abs(s.availability - g.marker.notna().mean()) < 1e-12
        assert abs(s.marker_rmse - np.sqrt(np.nanmean(g.marker_error ** 2))) < 1e-9
        assert abs(s.rmse_after_mean - g.rmse_after.mean()) < 1e-9
    k1 = pd.read_csv(OUT / "k1_equivalence.csv")
    assert k1.same_rows.all()
    for folder in sorted(ART.glob("pilot_*")):
        mf = folder / "manifest.json"
        if folder == OUT or not mf.exists():
            continue
        for n_, h in json.loads(mf.read_text(encoding="utf-8")).items():
            assert hashlib.sha256((folder / n_).read_bytes()).hexdigest() == h, (folder.name, n_)
    result = dict(status="passed", variants=len(summary), regimes_checked=6 * 21, k1_folds=len(k1))
    (OUT / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
