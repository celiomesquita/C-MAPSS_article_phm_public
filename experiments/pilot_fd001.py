"""Exploratory sensor-only pilot; no physical HI or inspection simulation."""

import hashlib
import importlib.metadata
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import GroupKFold, GroupShuffleSplit
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "experiments/artifacts/pilot_fd001_01"
SENSORS = [f"s{i}" for i in range(1, 22)]
BASELINE = 20
WINDOW = 15
SEED = 20261016


def read_data():
    names = ["unit", "cycle", "op1", "op2", "op3"] + SENSORS
    data = pd.read_csv(ROOT / "CMAPSSData/train_FD001.txt", sep=r"\s+", header=None, names=names)
    data[["unit", "cycle"]] = data[["unit", "cycle"]].astype(int)
    data["end"] = data.groupby("unit")["cycle"].transform("max")
    data["rul"] = data["end"] - data["cycle"]
    return data


def smooth(data, window):
    return data.groupby("unit", sort=False)[SENSORS].transform(
        lambda s: s.rolling(window, min_periods=window).mean())


def detector(data, fit_ids, window, sigma, channels):
    means = smooth(data, window)
    # Per-engine baseline is available only after cycle BASELINE.
    centres = data.loc[data.cycle <= BASELINE].groupby("unit")[SENSORS].mean()
    residual = means - centres.loc[data.unit].set_axis(data.index)
    healthy = (data.cycle <= BASELINE) & data.unit.isin(fit_ids)
    scales = residual.loc[healthy].std(ddof=1)
    selected = scales.index[scales > 1e-6].tolist()
    z = residual[selected].abs().div(scales[selected])
    flag = ((z > sigma).sum(axis=1) >= channels) & (data.cycle > BASELINE)
    persistent = flag.groupby(data.unit).transform(lambda s: s.rolling(3, min_periods=3).sum()).eq(3)
    points = data.loc[persistent].groupby("unit").cycle.min()
    return points, selected, z.max(axis=1)


def features(data, selected):
    frames = []
    grouped = data.groupby("unit", sort=False)[selected]
    for label, method in [("mean", "mean"), ("std", "std"), ("rms", "rms"), ("skew", "skew")]:
        def rolling(s):
            r = s.rolling(WINDOW, min_periods=WINDOW)
            if method == "rms":
                return np.sqrt(s.pow(2).rolling(WINDOW, min_periods=WINDOW).mean())
            if method == "skew":
                # Window-local centring avoids future-dependent numerical centring in rolling.skew.
                def skew(a):
                    centred = a - np.mean(a)
                    second = np.mean(centred**2)
                    if second <= 1e-24:
                        return 0.
                    n = len(a)
                    return np.sqrt(n * (n - 1)) / (n - 2) * np.mean(centred**3) / second**1.5
                return r.apply(skew, raw=True)
            return getattr(r, method)()
        frames.append(grouped.transform(rolling).add_suffix("_" + label))
    return pd.concat(frames, axis=1).replace([np.inf, -np.inf], np.nan)


def models():
    return {
        "RF": RandomForestRegressor(n_estimators=150, max_depth=12, min_samples_leaf=5,
                                    n_jobs=4, random_state=SEED),
        "GBR": GradientBoostingRegressor(n_estimators=150, max_depth=3, learning_rate=.05,
                                        random_state=SEED),
        "XGB": XGBRegressor(n_estimators=150, max_depth=6, learning_rate=.05,
                            n_jobs=4, random_state=SEED, objective="reg:squarederror"),
        "LGBM": LGBMRegressor(n_estimators=150, max_depth=6, num_leaves=31,
                              learning_rate=.05, verbosity=-1, n_jobs=4, random_state=SEED),
    }


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    data = read_data()
    sensitivity, scores, decisions, predictions, splits, detectors, importances = [], [], [], [], [], [], []
    for fold, (development, evaluation) in enumerate(GroupKFold(5).split(data, groups=data.unit), 1):
        dev = data.iloc[development]
        inside, calibration = next(GroupShuffleSplit(n_splits=1, test_size=.25, random_state=SEED + fold)
                                   .split(dev, groups=dev.unit))
        fit_ids = sorted(dev.iloc[inside].unit.unique().tolist())
        cal_ids = sorted(dev.iloc[calibration].unit.unique().tolist())
        test_ids = sorted(data.iloc[evaluation].unit.unique().tolist())
        assert not (set(fit_ids) & set(cal_ids) or set(fit_ids) & set(test_ids) or set(cal_ids) & set(test_ids))
        splits.append({"fold": fold, "fit": fit_ids, "calibration": cal_ids, "evaluation": test_ids})
        # Sensitivity is reported, not used to choose settings on evaluation engines.
        for w in [5, 10, 15]:
            for k in [2., 3.]:
                for n in [1, 2]:
                    points, _, _ = detector(data, fit_ids, w, k, n)
                    for unit in test_ids:
                        end = int(data.loc[data.unit == unit, "end"].iloc[0])
                        p = points.get(unit, np.nan)
                        sensitivity.append({"fold": fold, "unit": unit, "window": w, "sigma": k,
                                            "channels": n, "p": p, "end": end,
                                            "lead": end - p if np.isfinite(p) else np.nan})
        points, selected, anomaly = detector(data, fit_ids, WINDOW, 2., 2)
        x = features(data, selected)
        # No endpoint enters x, baseline or detector.
        assert not any(c in x for c in ["end", "rul", "unit", "cycle"])
        active = (data.cycle >= data.unit.map(points)) & (data.cycle >= BASELINE + 1)
        valid = active & x.notna().all(axis=1)
        fit = valid & data.unit.isin(fit_ids)
        cal = valid & data.unit.isin(cal_ids)
        test = valid & data.unit.isin(test_ids)
        for unit in test_ids:
            detectors.append({"fold": fold, "unit": unit, "p": points.get(unit, np.nan),
                              "end": int(data.loc[data.unit == unit, "end"].iloc[0])})
        for name, model in models().items():
            print(f"fold={fold} model={name} rows={int(fit.sum())}", flush=True)
            # Equal total training weight per engine, irrespective of trajectory length.
            counts = data.loc[fit].groupby("unit").size()
            weights = 1. / data.loc[fit, "unit"].map(counts)
            weights = weights / weights.mean()
            model.fit(x.loc[fit], data.loc[fit, "rul"], sample_weight=weights)
            cal_pred = np.maximum(0., model.predict(x.loc[cal]))
            error = pd.Series(cal_pred - data.loc[cal, "rul"].to_numpy(), index=data.index[cal])
            # One residual per calibration engine: worst overestimate over its available history.
            maxima = error.groupby(data.loc[cal, "unit"]).max().clip(lower=0)
            margin = float(np.quantile(maxima, .9, method="higher"))
            pred = np.maximum(0., model.predict(x.loc[test]))
            safe = np.maximum(0., pred - margin)
            out = data.loc[test, ["unit", "cycle", "rul", "end"]].copy()
            out["fold"], out["model"], out["raw"], out["adjusted"] = fold, name, pred, safe
            out["margin"] = margin
            predictions.append(out)
            for mode in ["raw", "adjusted"]:
                for unit, g in out.groupby("unit"):
                    e = g[mode] - g.rul
                    scores.append({"fold": fold, "unit": int(unit), "model": name, "mode": mode,
                                   "rmse": float(np.sqrt(np.mean(e**2))),
                                   "overprediction_fraction": float((e > 0).mean()),
                                   "last_error": float(e.iloc[-1]), "margin": margin})
            for unit in test_ids:
                g = out.loc[out.unit == unit]
                end = int(data.loc[data.unit == unit, "end"].iloc[0])
                for mode in ["raw", "adjusted"]:
                    for trigger in [0, 5, 10]:
                        hits = g.loc[g[mode] <= trigger, "cycle"]
                        removal = int(hits.iloc[0]) if len(hits) else end
                        decisions.append({"fold": fold, "unit": unit, "model": name, "mode": mode,
                                          "trigger": trigger, "removal": removal, "end": end,
                                          "reached_endpoint": removal >= end, "unused": end - removal,
                                          "detection_available": unit in points.index})
            for c, value in zip(x.columns, model.feature_importances_):
                importances.append({"fold": fold, "model": name, "feature": c, "importance": float(value)})
        # Traditional and diagnostic-only reference actions, no future test lifetime used for tuning.
        age = int(np.quantile(data.loc[data.unit.isin(fit_ids)].groupby("unit").end.first(), .1, method="lower"))
        for unit in test_ids:
            end = int(data.loc[data.unit == unit, "end"].iloc[0])
            for name, when in [("age_q10", age), ("at_P", points.get(unit, end))]:
                removal = min(int(when), end)
                decisions.append({"fold": fold, "unit": unit, "model": name, "mode": "baseline",
                                  "trigger": -1, "removal": removal, "end": end,
                                  "reached_endpoint": removal >= end, "unused": end - removal,
                                  "detection_available": unit in points.index})

    pd.DataFrame(sensitivity).to_csv(OUT / "detector_sensitivity.csv", index=False)
    pd.DataFrame(detectors).to_csv(OUT / "detected_P.csv", index=False)
    metrics = pd.DataFrame(scores)
    metrics.to_csv(OUT / "metrics_per_engine.csv", index=False)
    summary = metrics.groupby(["model", "mode"]).agg(
        engines=("unit", "size"), mean_engine_rmse=("rmse", "mean"),
        mean_overprediction_fraction=("overprediction_fraction", "mean"),
        mean_margin=("margin", "mean")).reset_index()
    summary.to_csv(OUT / "prediction_summary.csv", index=False)
    decision = pd.DataFrame(decisions)
    decision.to_csv(OUT / "decisions_per_engine.csv", index=False)
    ds = decision.groupby(["model", "mode", "trigger"]).agg(
        engines=("unit", "size"), endpoint_count=("reached_endpoint", "sum"),
        mean_unused=("unused", "mean"), mean_exposure=("removal", "mean")).reset_index()
    ds["restorations_per_1000_cycles"] = 1000 / ds.mean_exposure
    ds.to_csv(OUT / "decision_summary.csv", index=False)
    pd.concat(predictions, ignore_index=True).to_csv(OUT / "predictions.csv", index=False)
    pd.DataFrame(importances).to_csv(OUT / "impurity_importances.csv", index=False)
    (OUT / "splits.json").write_text(json.dumps(splits, indent=2), encoding="utf-8")
    metadata = {"timestamp_utc": datetime.now(timezone.utc).isoformat(), "python": platform.python_version(),
                "seed": SEED, "outer_folds": 5, "baseline": BASELINE, "window": WINDOW,
                "sigma": 2, "persistence": 3, "channels": 2, "margin_quantile": .9,
                "data_sha256": hashlib.sha256((ROOT / "CMAPSSData/train_FD001.txt").read_bytes()).hexdigest(),
                "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "versions": {n: importlib.metadata.version(n) for n in
                             ["numpy", "pandas", "scikit-learn", "xgboost", "lightgbm", "matplotlib"]},
                "limits": ["Exploration only; no physical HI, inspection, SHAP, or operational safety claim",
                           "No hyperparameter search; calibration split is not final evaluation",
                           "Causal processing and engine-held-out folds; first 20 cycles assumed healthy",
                           "Endpoint counts are benchmark outcomes, not aircraft accidents",
                           "Renewal exposure ratio is conditional on iid AGAN lives and zero downtime; not validated"]}
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    plot_data = pd.DataFrame(sensitivity)
    fig, ax = plt.subplots(figsize=(8, 4))
    for (k, n), g in plot_data.groupby(["sigma", "channels"]):
        med = g.groupby("window").lead.median()
        ax.plot(med.index, med.values, marker="o", label=f"{k:g} sigma; {n} sensor(s)")
    ax.set(xlabel="Causal moving-average window (cycles)", ylabel="Median endpoint minus detected P (cycles)",
           title="FD001: detected planning window (not true onset accuracy)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "detector_sensitivity.png", dpi=160)
    plt.close(fig)
    print(summary.to_string(index=False), flush=True)
    print(ds.to_string(index=False), flush=True)


if __name__ == "__main__":
    run()
