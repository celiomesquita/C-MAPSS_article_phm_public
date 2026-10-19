"""P03: detector robustness with fixed forecasts and empirical HI diagnostics."""

import hashlib
import importlib.metadata
import itertools
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold

from pilot_fd001 import ROOT, SEED, SENSORS, features, models, read_data, smooth
from pilot_fd001_02 import margins, points_at, simulate, split_units

OUT = ROOT / "experiments/artifacts/pilot_fd001_03"
CONFIGS = list(itertools.product([30, 40, 50], [5, 10, 15], [3, 5]))


def sensor_score(data, fit_ids, window, persistence):
    means = smooth(data, window)
    centres = data.loc[data.cycle <= 20].groupby("unit")[SENSORS].mean()
    residuals = means - centres.loc[data.unit].set_axis(data.index)
    scales = residuals.loc[(data.cycle <= 20) & data.unit.isin(fit_ids)].std()
    sensors = scales.index[scales > 1e-6].tolist()
    z = residuals[sensors].abs().div(scales[sensors])
    second = pd.Series(np.partition(z.to_numpy(), -2, axis=1)[:, -2], index=data.index)
    second.loc[data.cycle <= 20] = np.nan
    score = second.groupby(data.unit).transform(
        lambda s: s.rolling(persistence, min_periods=persistence).min())
    return score, sensors


def choose_detector(data, score, fit_ids, selection_ids, b0):
    initial = (data.cycle.between(21, b0)) & data.unit.isin(fit_ids)
    maxima = score.loc[initial].groupby(data.loc[initial, "unit"]).max()
    candidates = [("fixed2", 2.)] + [(f"q{q}", max(2., float(np.quantile(maxima, q, method="higher"))))
                                     for q in [.9, .95, 1.]]
    ends = data.loc[data.unit.isin(selection_ids)].groupby("unit").end.first().reindex(selection_ids)
    rows = []
    for label, threshold in candidates:
        p = points_at(data, score, threshold).reindex(selection_ids)
        lead = ends-p
        rows.append({"candidate": label, "threshold": threshold, "early_count": int((p <= b0).sum()),
                     "coverage": int((lead > 0).sum()),
                     "median_lead": float(lead[lead > 0].median()) if (lead > 0).any() else 0.})
    feasible = [r for r in rows if r["early_count"] <= 2]
    if feasible:
        best = min(feasible, key=lambda r: (-r["coverage"], -r["median_lead"], r["threshold"]))
    else:
        best = min(rows, key=lambda r: (r["early_count"], -r["coverage"], -r["median_lead"], r["threshold"]))
    for r in rows:
        r["chosen"] = r["candidate"] == best["candidate"]
        r["selection_feasible"] = bool(feasible)
    return points_at(data, score, best["threshold"]), rows, best


def fit_hi_reference(data, fit_ids, sensors, quantile):
    means = smooth(data, 15)
    baseline = means.loc[data.cycle == 20].copy()
    baseline.index = data.loc[data.cycle == 20, "unit"]
    terminal = means.loc[data.cycle == data.end].copy()
    terminal.index = data.loc[data.cycle == data.end, "unit"]
    difference = terminal.loc[fit_ids, sensors] - baseline.loc[fit_ids, sensors]
    direction = np.sign(difference.median())
    scale = difference.mul(direction).quantile(quantile, interpolation="higher")
    reference = pd.DataFrame({"sensor": sensors, "direction": direction.values, "scale": scale.values})
    reference["eligible"] = (reference.direction != 0) & (reference.scale > 1e-6)
    return reference


def transform_hi(data, reference):
    means = smooth(data, 15)
    baseline = means.loc[data.cycle == 20].copy()
    baseline.index = data.loc[data.cycle == 20, "unit"]
    ref = reference.loc[reference.eligible].set_index("sensor")
    channels = ref.index.tolist()
    centred = means[channels] - baseline.loc[data.unit, channels].set_axis(data.index)
    health = (1-centred.mul(ref.direction).div(ref.scale)).clip(0, 1).min(axis=1)
    health.loc[data.cycle < 20] = np.nan
    return health


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    data = read_data()
    source = ROOT / "CMAPSSData/train_FD001.txt"
    initial_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    detector_rows, detection_rows, predictions, decisions, references, hi_rows, hi_metrics = [], [], [], [], [], [], []
    cal_rows, partitions, metrics = [], [], []
    for fold, (dev_idx, test_idx) in enumerate(GroupKFold(5).split(data, groups=data.unit), 1):
        fit_ids, cal_ids, selection_ids = split_units(data.iloc[dev_idx], fold)
        test_ids = sorted(data.iloc[test_idx].unit.unique().tolist())
        partitions.append({"fold": fold, "fit": fit_ids, "calibration": cal_ids,
                           "selection": selection_ids, "evaluation": test_ids})
        assert len(set(fit_ids+cal_ids+selection_ids+test_ids)) == 100
        cache = {(w,d): sensor_score(data, fit_ids, w, d) for w,d in itertools.product([5,10,15],[3,5])}
        points_by_config = {}
        for b0, w, d in CONFIGS:
            name = f"B0_{b0}_w_{w}_d_{d}"
            score, _ = cache[w,d]
            p, rows, best = choose_detector(data, score, fit_ids, selection_ids, b0)
            points_by_config[name] = p
            for row in rows:
                detector_rows.append({"fold": fold, "config": name, "b0": b0, "window": w,
                                      "persistence": d, **row})
            for unit in test_ids:
                end = int(data.loc[data.unit == unit, "end"].iloc[0])
                detection_rows.append({"fold": fold, "config": name, "b0": b0, "window": w,
                                       "persistence": d, "unit": unit, "end": end,
                                       "p": p.get(unit, np.nan), "threshold": best["threshold"]})
        sensors = cache[15,3][1]
        x = features(data, sensors)
        valid = (data.cycle >= 21) & x.notna().all(axis=1)
        fit = valid & data.unit.isin(fit_ids)
        counts = data.loc[fit].groupby("unit").size()
        weights = 1/data.loc[fit, "unit"].map(counts)
        weights /= weights.mean()
        for name, model in models().items():
            print(f"fold={fold} model={name} fitting_rows={int(fit.sum())}", flush=True)
            model.fit(x.loc[fit], data.loc[fit, "rul"], sample_weight=weights)
            parts = {}
            for role, ids in [("calibration", cal_ids), ("selection", selection_ids), ("evaluation", test_ids)]:
                mask = valid & data.unit.isin(ids)
                out = data.loc[mask, ["unit", "cycle", "rul", "end"]].copy()
                out["raw"] = np.maximum(0., model.predict(x.loc[mask]))
                out["fold"], out["model"], out["role"] = fold, name, role
                parts[role] = out
                predictions.append(out)
            calibration = margins(parts["calibration"])
            cal_rows.append({"fold": fold, "model": name, **calibration})
            for unit, g in parts["evaluation"].groupby("unit"):
                metrics.append({"fold": fold, "model": name, "unit": int(unit),
                                "rmse": float(np.sqrt(np.mean((g.raw-g.rul)**2)))})
            for config, p in points_by_config.items():
                out = parts["evaluation"]
                out = out.loc[out.cycle >= out.unit.map(p)]
                for variant in ["raw", "local_gate30"]:
                    result = simulate(data, out, test_ids, variant, calibration)
                    if not result.empty:
                        result["fold"], result["model"], result["config"] = fold, name, config
                        decisions.append(result)
        for q in [.5, .9]:
            ref = fit_hi_reference(data, fit_ids, sensors, q)
            health = transform_hi(data, ref)
            ref["fold"], ref["quantile"] = fold, q
            references.append(ref)
            for unit in test_ids:
                mask = (data.unit == unit) & (data.cycle >= 20)
                rows = data.loc[mask, ["unit", "cycle", "end"]].copy()
                rows["hi"] = health.loc[mask]
                rows["fold"], rows["quantile"] = fold, q
                hi_rows.append(rows)
                zeros = rows.loc[rows.hi <= 0, "cycle"]
                f_hat = float(zeros.iloc[0]) if len(zeros) else np.nan
                hi_metrics.append({"fold": fold, "quantile": q, "unit": unit,
                                   "end": int(rows.end.iloc[0]), "estimated_F": f_hat,
                                   "endpoint_hi": float(rows.hi.iloc[-1]),
                                   "earliest_P": min(p.get(unit, np.inf) for p in points_by_config.values())})
    frames = {"detector_selection": pd.DataFrame(detector_rows), "detections": pd.DataFrame(detection_rows),
              "predictions": pd.concat(predictions, ignore_index=True), "decisions_per_engine": pd.concat(decisions, ignore_index=True),
              "hi_reference": pd.concat(references, ignore_index=True), "hi_trajectories": pd.concat(hi_rows, ignore_index=True),
              "hi_metrics": pd.DataFrame(hi_metrics), "margins": pd.DataFrame(cal_rows), "metrics_per_engine": pd.DataFrame(metrics)}
    for name, frame in frames.items():
        frame.to_csv(OUT / f"{name}.csv", index=False)
    (OUT / "splits.json").write_text(json.dumps(partitions, indent=2), encoding="utf-8")
    assert hashlib.sha256(source.read_bytes()).hexdigest() == initial_hash
    sources = [Path(__file__), ROOT / "experiments/pilot_fd001.py", ROOT / "experiments/pilot_fd001_02.py",
               ROOT / "experiments/protocolo_piloto_fd001_03.md"]
    metadata = {"timestamp_utc": datetime.now(timezone.utc).isoformat(), "seed": SEED,
                "python": platform.python_version(), "data_sha256": initial_hash,
                "configs": CONFIGS, "example_engines": [1,2,3],
                "versions": {n: importlib.metadata.version(n) for n in ["numpy","pandas","scikit-learn","xgboost","lightgbm"]},
                "source_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
                "limits": ["No physical P/F labels", "No inspection", "HI reference uses fitting endpoints only",
                           "Forecasts trained from cycle 21; P02/P03 are not a controlled retraining contrast",
                           "No configuration winner chosen from outer results"]}
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir())
                if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("P03 fits and diagnostics completed.", flush=True)


if __name__ == "__main__":
    run()
