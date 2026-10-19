"""P18.1: synthetic multi-regime stress test of the operating-regime normalisation, FD001 only."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.metrics import adjusted_rand_score, silhouette_score
from threadpoolctl import threadpool_limits

import pilot_f_uncertainty_10 as p10
from pilot_fd003_06 import read_inputs
from regime_normalisation import OPS, SENSORS, RegimeNormaliser

ROOT = p10.ROOT
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_regime_synthetic_18a"
SEED = 20261018
SYN_SEED = 20261018
N_REGIMES = 6
SOURCES = ["protocolo_normalizacao_regimes_18a.md", "regime_normalisation.py", "pilot_regime_synthetic_18a.py",
           "test_regime_normalisation_18a.py", "verify_regime_synthetic_18a.py"]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def integrity():
    records = {}
    for folder in sorted(ART.glob("pilot_*")):
        manifest = folder / "manifest.json"
        if folder == OUT or not manifest.exists():
            continue
        for name, digest in json.loads(manifest.read_text(encoding="utf-8")).items():
            assert sha(folder / name) == digest, (folder.name, name)
        records[folder.name] = sha(manifest)
    return records


def make_synthetic(base, seed=SYN_SEED):
    """Seeded synthetic regimes over real FD001 trajectories; returns frame, regime labels and effect parameters."""
    rng = np.random.default_rng(seed)
    centres = np.column_stack([rng.uniform(0, 42, N_REGIMES), rng.uniform(0, 0.84, N_REGIMES), rng.uniform(20, 100, N_REGIMES)])
    regimes = rng.integers(0, N_REGIMES, len(base))
    sigma = base[SENSORS].std(ddof=1).to_numpy(float)
    live = sigma > 1e-9
    shift = rng.normal(0.0, 1.0, (N_REGIMES, len(SENSORS))) * (3 * sigma)
    factor = rng.uniform(0.9, 1.1, (N_REGIMES, len(SENSORS)))
    shift[:, ~live] = 0.0
    factor[:, ~live] = 1.0
    noise = rng.normal(0.0, 1.0, (len(base), 3)) * np.array([0.05, 0.002, 0.2])
    out = base.copy()
    out[OPS] = centres[regimes] + noise
    out[SENSORS] = base[SENSORS].to_numpy(float) * factor[regimes] + shift[regimes]
    return out, pd.Series(regimes, index=base.index), dict(centres=centres, shift=shift, factor=factor)


def subset(frame, units):
    return frame.loc[frame.unit.isin(units)]


def evaluate(bundle, evaluation):
    predictions, _ = p10.predict_inputs(bundle, evaluation)
    rows = []
    iso = predictions[predictions.method == "ISO"]
    ends = evaluation.groupby("unit").cycle.max()
    for unit, g in iso.groupby("unit"):
        t_end = ends.loc[unit]
        d = g[g.in_domain].sort_values("cycle")
        true_all = t_end - g.cycle
        rho = spearmanr(g.hi, true_all).statistic if len(g) > 3 else np.nan
        if d.empty:
            rows.append(dict(unit=unit, marker=np.nan, marker_error=np.nan, rmse_after=np.nan, spearman_hi_rul=rho))
            continue
        true = t_end - d.cycle
        rows.append(dict(unit=unit, marker=float(d.cycle.iloc[0]), marker_error=float(d.predicted_rul.iloc[0] - true.iloc[0]),
                         rmse_after=float(np.sqrt(np.mean((d.predicted_rul - true) ** 2))), spearman_hi_rul=rho))
    present = {r["unit"] for r in rows}
    for unit in set(ends.index) - present:
        rows.append(dict(unit=unit, marker=np.nan, marker_error=np.nan, rmse_after=np.nan, spearman_hi_rul=np.nan))
    return pd.DataFrame(rows)


def run_variant(name, fit, converter, evaluation, seed):
    bundle = p10.fit_pipeline(fit, converter, "FD001", seed)
    return evaluate(bundle, evaluation), bundle


def main():
    OUT.mkdir(exist_ok=True)
    previous = integrity()
    (OUT / "execution_start.json").write_text(json.dumps(dict(
        started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=previous,
        sources={n: sha(ROOT / "experiments" / n) for n in SOURCES},
        inputs={"CMAPSSData/train_FD001.txt": sha(ROOT / "CMAPSSData/train_FD001.txt")}), indent=2), encoding="utf-8")
    base = read_inputs("train", "FD001")
    synthetic, labels, effects = make_synthetic(base)
    np.savez(OUT / "synthetic_effects.npz", **effects)
    (OUT / "synthetic_checksum.json").write_text(json.dumps(dict(
        sensors_sum=float(synthetic[SENSORS].to_numpy().sum()), ops_sum=float(synthetic[OPS].to_numpy().sum()),
        regimes_sum=int(labels.sum()))), encoding="utf-8")
    partitions = p10.partitions(p10.SEEDS[0])
    per_engine, diagnostics, equivalence = [], [], []
    with threadpool_limits(limits=1):
        for part in partitions:
            seed = p10.SEEDS[0] + part["fold"]
            fit_u, conv_u, eval_u = part["fit"], part["converter"], part["evaluation"]
            # T1: K=1 equivalence on the original FD001
            norm1 = RegimeNormaliser(k=1).fit(subset(base, fit_u))
            b0 = p10.fit_pipeline(subset(base, fit_u), subset(base, conv_u), "FD001", seed)
            b1 = p10.fit_pipeline(norm1.transform(subset(base, fit_u)), norm1.transform(subset(base, conv_u)), "FD001", seed)
            p0, _ = p10.predict_inputs(b0, subset(base, eval_u))
            p1, _ = p10.predict_inputs(b1, norm1.transform(subset(base, eval_u)))
            p0 = p0.sort_values(["method", "unit", "cycle"]).reset_index(drop=True)
            p1 = p1.sort_values(["method", "unit", "cycle"]).reset_index(drop=True)
            same_rows = len(p0) == len(p1) and (p0[["unit", "cycle", "method"]].to_numpy() == p1[["unit", "cycle", "method"]].to_numpy()).all()
            equivalence.append(dict(fold=part["fold"], same_rows=bool(same_rows),
                                    max_hi_diff=float(np.abs(p0.hi - p1.hi).max()) if same_rows else np.nan,
                                    max_rul_diff=float(np.abs(p0.predicted_rul - p1.predicted_rul).max()) if same_rows else np.nan,
                                    channels_original=int(len(b0["health"]["stats"]["channels"])),
                                    channels_k1=int(len(b1["health"]["stats"]["channels"]))))
            # T2 variants
            variants = {}
            variants["V0_original"] = (subset(base, fit_u), subset(base, conv_u), subset(base, eval_u))
            variants["V1_synthetic_raw"] = (subset(synthetic, fit_u), subset(synthetic, conv_u), subset(synthetic, eval_u))
            norm = RegimeNormaliser(k=N_REGIMES).fit(subset(synthetic, fit_u))
            variants["V2_synthetic_kmeans"] = tuple(norm.transform(subset(synthetic, u)) for u in (fit_u, conv_u, eval_u))
            oracle = RegimeNormaliser(k=N_REGIMES, labels=labels).fit(subset(synthetic, fit_u))
            variants["V3_synthetic_true_regimes"] = tuple(oracle.transform(subset(synthetic, u)) for u in (fit_u, conv_u, eval_u))
            f_ops = (subset(synthetic, fit_u)[OPS].to_numpy() - norm.op_mean) / norm.op_std
            diagnostics.append(dict(fold=part["fold"], silhouette=float(silhouette_score(f_ops, norm.km.labels_)),
                                    adjusted_rand=float(adjusted_rand_score(labels.loc[subset(synthetic, fit_u).index], norm.km.labels_)),
                                    smallest_cluster=int(np.bincount(norm.km.labels_).min())))
            for name, (f, c, e) in variants.items():
                metrics, _ = run_variant(name, f, c, e, seed)
                per_engine.append(metrics.assign(variant=name, fold=part["fold"]))
            print("fold", part["fold"], flush=True)
    pe = pd.concat(per_engine, ignore_index=True)
    pe.to_csv(OUT / "per_engine.csv", index=False)
    pd.DataFrame(diagnostics).to_csv(OUT / "clustering_diagnostics.csv", index=False)
    pd.DataFrame(equivalence).to_csv(OUT / "k1_equivalence.csv", index=False)
    summary = pe.groupby("variant").agg(engines=("unit", "size"), availability=("marker", lambda s: s.notna().mean()),
                                        marker_rmse=("marker_error", lambda s: float(np.sqrt(np.nanmean(s ** 2)))),
                                        marker_bias=("marker_error", "mean"),
                                        rmse_after_mean=("rmse_after", "mean"), spearman_mean=("spearman_hi_rul", "mean")).reset_index()
    summary.to_csv(OUT / "summary.csv", index=False)
    for n in SOURCES:
        (OUT / f"source_{n}").write_bytes((ROOT / "experiments" / n).read_bytes())
    assert integrity() == previous
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                   if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")
    pd.set_option("display.width", 200)
    print(summary.round(3).to_string(index=False))
    print(pd.DataFrame(equivalence).round(10).to_string(index=False))
    print(pd.DataFrame(diagnostics).round(3).to_string(index=False))


if __name__ == "__main__":
    main()
