"""P08: frozen empirical HI, causal feature ablations and sensor controls."""

import hashlib
import importlib.metadata
import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from threadpoolctl import threadpool_limits

import pilot_fd001_05 as p05
from pilot_fd001_04 import centred_sensors
from pilot_fd001 import smooth
from pilot_fd003_06 import load_models, read_inputs

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "experiments/artifacts/pilot_hi_trajectory_08"
SEED = 20261016
WINDOW = 20
HI_COLUMNS = {"HI": ["hi"], "HI_SLOPE": ["hi", "h_slope"],
              "HI_CURV": ["hi", "h_curv"], "HI_STD": ["hi", "h_std"],
              "HI_FULL": ["hi", "h_slope", "h_curv", "h_std"],
              "HI_NO_SLOPE": ["hi", "h_curv", "h_std"],
              "HI_NO_CURV": ["hi", "h_slope", "h_std"],
              "HI_NO_STD": ["hi", "h_slope", "h_curv"]}
EVENTS = {"landmark": 0, "plus5": 5, "plus10": 10, "plus20": 20}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_folder(subset):
    return ROOT / "experiments/artifacts" / ("pilot_fd001_05" if subset == "FD001" else "pilot_fd003_06")


def source_integrity():
    folders = sorted((ROOT / "experiments/artifacts").glob("pilot_fd00*"))
    folders.append(ROOT / "experiments/artifacts/pilot_hi_landmark_07")
    result = {}
    for folder in folders:
        manifest = folder / "manifest.json"
        if not manifest.exists():
            continue
        for name, digest in json.loads(manifest.read_text(encoding="utf-8")).items():
            assert sha(folder / name) == digest, (folder.name, name)
        result[folder.name] = sha(manifest)
    return result


def rolling_statistics(values, window=WINDOW):
    a = np.asarray(values, dtype=float)
    if a.ndim == 1:
        a = a[:, None]
    names = ("slope", "curv", "std", "rms", "skew")
    result = {name: np.full_like(a, np.nan) for name in names}
    if len(a) < window:
        return result
    windows = np.lib.stride_tricks.sliding_window_view(a, window, axis=0)
    u = np.arange(window)-(window-1)/2
    v = u*u-np.mean(u*u)
    centre = windows-windows.mean(axis=-1, keepdims=True)
    m2 = np.mean(centre**2, axis=-1)
    skew = np.zeros_like(m2)
    np.divide(np.mean(centre**3, axis=-1), m2**1.5, out=skew, where=m2 > 1e-24)
    skew *= np.sqrt(window*(window-1))/(window-2)
    stats = {"slope": np.sum(windows*u, axis=-1)/np.sum(u*u),
             "curv": 2*np.sum(windows*v, axis=-1)/np.sum(v*v),
             "std": np.std(windows, axis=-1, ddof=1),
             "rms": np.sqrt(np.mean(windows**2, axis=-1)), "skew": skew}
    for name in names:
        result[name][window-1:] = stats[name]
    return result


def build_features(inputs, frozen):
    data = inputs.drop(columns=["end", "rul"], errors="ignore").reset_index(drop=True)
    health = p05.transform_selected(data, frozen, "EMPIRICO")
    result = data[["unit", "cycle"]].copy()
    result["hi"] = health.hi
    result["frozen_rul"] = health.predicted_rul
    centred = centred_sensors(data)
    channels = frozen["stats"]["channels"]
    directions, scales = frozen["stats"]["direction"], frozen["stats"]["scale"]
    means = p05.standardise(centred, frozen["stats"])
    initial_means = smooth(data, 15).loc[data.cycle.eq(20), channels].copy()
    initial_means.index = data.loc[data.cycle.eq(20), "unit"]
    raw = (data[channels].to_numpy()-initial_means.loc[data.unit].to_numpy())*directions/scales
    for j, sensor in enumerate(channels):
        result[f"raw_{sensor}"] = raw[:, j]
        result[f"mean_{sensor}"] = means[:, j]
    feature_arrays = {f"{kind}_{sensor}": np.full(len(data), np.nan)
                      for sensor in channels for kind in ["sd", "rms", "skew", "slope", "curv"]}
    hi_arrays = {f"h_{kind}": np.full(len(data), np.nan) for kind in ["slope", "curv", "std"]}
    for _, g in data.groupby("unit", sort=False):
        idx = g.index.to_numpy()
        raw_stats = rolling_statistics(raw[idx])
        mean_stats = rolling_statistics(means[idx])
        for j, sensor in enumerate(channels):
            for name, kind in [("sd", "std"), ("rms", "rms"), ("skew", "skew")]:
                feature_arrays[f"{name}_{sensor}"][idx] = raw_stats[kind][:, j]
            for kind in ["slope", "curv"]:
                feature_arrays[f"{kind}_{sensor}"][idx] = mean_stats[kind][:, j]
        hi_idx = idx[data.loc[idx, "cycle"].to_numpy() >= 20]
        hi_stats = rolling_statistics(result.loc[hi_idx, "hi"].to_numpy())
        for kind in ["slope", "curv", "std"]:
            hi_arrays[f"h_{kind}"][hi_idx] = hi_stats[kind][:, 0]
    result = pd.concat([result, pd.DataFrame(hi_arrays, index=data.index),
                        pd.DataFrame(feature_arrays, index=data.index)], axis=1)
    reps = {name: list(columns) for name, columns in HI_COLUMNS.items()}
    reps["SENSOR_RAW"] = [f"raw_{s}" for s in channels]
    reps["SENSOR_MEAN"] = [f"mean_{s}" for s in channels]
    reps["SENSOR_FULL"] = [f"{kind}_{s}" for s in channels for kind in ["mean", "sd", "rms", "skew", "slope", "curv"]]
    valid = result.loc[result.cycle.ge(39)].copy()
    columns = sorted(set(sum(reps.values(), [])))
    assert np.isfinite(valid[columns]).all().all()
    return valid, health, reps


def label_features(features, endpoints):
    labelled = features.copy()
    labelled["end"] = labelled.unit.map(endpoints)
    labelled["rul"] = labelled.end-labelled.cycle
    return labelled


def predict(record, data):
    x = data[record["columns"]].to_numpy()
    if record.get("scaler") is not None:
        x = record["scaler"].transform(x)
    if record["algorithm"].startswith("ISO"):
        x = x[:, 0]
    return np.maximum(0., record["model"].predict(x))


def selection_loss(selection, values):
    frame = selection[["unit", "cycle", "end", "rul"]].copy()
    frame["squared_error"] = (values-frame.rul)**2
    cuts = np.column_stack([np.floor(frame.end.to_numpy()*f).astype(int) for f in [.5, .7, .9]])
    mask = (cuts == frame.cycle.to_numpy()[:, None]).any(axis=1)
    return float(np.sqrt(frame.loc[mask].groupby("unit").squared_error.mean().mean()))


def fit_converters(features, partition, reps, frozen):
    train = features.loc[features.unit.isin(partition["calibration"])]
    selection = features.loc[features.unit.isin(partition["selection"])]
    assert set(train.unit).isdisjoint(set(selection.unit))
    assert set(train.unit) == set(partition["calibration"])
    weights = p05.equal_engine_weights(train.unit)
    records, rows, coefficients = {}, [], []
    for representation, columns in reps.items():
        x, y = train[columns].to_numpy(), train.rul.to_numpy()
        for algorithm in ["Ridge", "RF"]:
            best = None
            for alpha in ([.1, 1., 10., 100.] if algorithm == "Ridge" else [None]):
                scaler = StandardScaler().fit(x, sample_weight=weights) if algorithm == "Ridge" else None
                model = (Ridge(alpha=alpha, solver="svd") if algorithm == "Ridge" else
                         RandomForestRegressor(n_estimators=150, max_depth=12, min_samples_leaf=5,
                                               n_jobs=4, random_state=SEED))
                model.fit(scaler.transform(x) if scaler is not None else x, y, sample_weight=weights)
                record = dict(model=model, scaler=scaler, columns=columns, representation=representation,
                              algorithm=algorithm, alpha=alpha, fit_units=sorted(train.unit.unique().tolist()))
                loss = selection_loss(selection, predict(record, selection))
                row = dict(representation=representation, algorithm=algorithm, alpha=alpha, selection_rmse=loss)
                rows.append(row)
                key = (loss, alpha if alpha is not None else 0.)
                if best is None or key < best[0]:
                    best = key, record
            name = f"{algorithm}:{representation}"
            records[name] = best[1]
            record = best[1]
            for column, value in zip(columns, record["model"].coef_ if algorithm == "Ridge" else record["model"].feature_importances_):
                coefficients.append(dict(method=name, feature=column, value=float(value),
                                         kind="standardised_coefficient" if algorithm == "Ridge" else "impurity_importance"))
        print(representation, "fitted", flush=True)
    iso = IsotonicRegression(increasing=True, y_min=0., out_of_bounds="clip")
    iso.fit(train.hi, train.rul, sample_weight=weights)
    for name, model in [("ISO_MATCHED", iso), ("ISO_FROZEN", frozen["converter"])]:
        records[name] = dict(model=model, scaler=None, columns=["hi"], algorithm=name,
                             representation="HI", fit_units=sorted(train.unit.unique().tolist()))
    for row in rows:
        chosen = records[f"{row['algorithm']}:{row['representation']}"]
        row["chosen"] = row["alpha"] == chosen["alpha"]
    return records, rows, coefficients


def event_grid(inputs, health, endpoints, units, dataset):
    rows = []
    for unit in units:
        g = health.loc[health.unit.eq(unit)]
        hits = g.loc[g.hi.le(.5)]
        crossing = int(hits.cycle.min()) if len(hits) else np.nan
        last = int(inputs.loc[inputs.unit.eq(unit), "cycle"].max())
        targets = {name: crossing+offset for name, offset in EVENTS.items()}
        if dataset == "truncated":
            targets["last"] = last
        for event, cycle in targets.items():
            status = ("no_observed_crossing" if np.isnan(cycle) else "before_feature_availability" if cycle < 39 else
                      "after_last_observation" if cycle > last else "available")
            rows.append(dict(unit=unit, event=event, cycle=cycle, crossing_cycle=crossing,
                             end=endpoints.loc[unit], last_observed=last, status=status))
    return pd.DataFrame(rows)


def permutation_importance(records, features, grid):
    available = grid.loc[grid.event.eq("landmark") & grid.status.eq("available")]
    sample = features.merge(available[["unit", "cycle"]], on=["unit", "cycle"], how="inner").sort_values("unit")
    rows = []
    for algorithm in ["Ridge", "RF"]:
        for representation in ["HI_FULL", "SENSOR_FULL"]:
            method = f"{algorithm}:{representation}"
            record = records[method]
            groups = ({name: [name] for name in HI_COLUMNS["HI_FULL"]} if representation == "HI_FULL" else
                      {sensor: [c for c in record["columns"] if c.endswith("_"+sensor)]
                       for sensor in sorted({c.split("_")[-1] for c in record["columns"]})})
            if len(sample) < 2:
                continue
            base = (predict(record, sample)-sample.rul.to_numpy())**2
            rng = np.random.default_rng(SEED)
            for group, columns in groups.items():
                for repeat in range(20):
                    changed = sample.copy()
                    order = rng.permutation(len(sample))
                    changed[columns] = sample[columns].to_numpy()[order]
                    squared = (predict(record, changed)-sample.rul.to_numpy())**2
                    rows.append(dict(method=method, representation=representation, group=group,
                                     repeat=repeat, engines=len(sample), delta_mse=float(np.mean(squared-base))))
    return rows


def evaluate(records, features, inputs, health, endpoints, units, dataset, subset, run):
    selected = features.loc[features.unit.isin(units)].copy()
    grid = event_grid(inputs, health, endpoints, units, dataset)
    event_rows, histories, prediction_frames = [], [], []
    for method, record in records.items():
        frame = selected[["unit", "cycle", "hi", "end", "rul"]].copy()
        frame["predicted_rul"] = predict(record, selected)
        frame["error"] = frame.predicted_rul-frame.rul
        frame["method"] = method
        prediction_frames.append(frame)
        events = grid.merge(frame[["unit", "cycle", "hi", "rul", "predicted_rul", "error"]],
                            on=["unit", "cycle"], how="left")
        events["method"] = method
        assert events.loc[events.status.eq("available"), "error"].notna().all()
        event_rows.append(events)
        for unit, g in frame.groupby("unit"):
            histories.append(dict(method=method, unit=unit, cycles=len(g), rmse=float(np.sqrt(np.mean(g.error**2))),
                                  mae=float(np.mean(abs(g.error)))))
    predictions = pd.concat(prediction_frames, ignore_index=True)
    predictions.to_csv(OUT / f"predictions_{subset}_{run}.csv.gz", index=False, compression="gzip")
    importance = permutation_importance(records, selected, grid)
    outputs = [pd.concat(event_rows, ignore_index=True), pd.DataFrame(histories), pd.DataFrame(importance)]
    for frame in outputs:
        frame["subset"], frame["dataset"], frame["run"] = subset, dataset, run
    return outputs


def summarise(events):
    rows = []
    for key, g in events.groupby(["subset", "dataset", "method", "event"], sort=True):
        a = g.loc[g.status.eq("available")]
        e = a.error.to_numpy()
        rows.append(dict(zip(["subset", "dataset", "method", "event"], key)) |
                    dict(total=len(g), available=len(a), no_crossing=int(g.status.eq("no_observed_crossing").sum()),
                         early_window=int(g.status.eq("before_feature_availability").sum()),
                         after_last=int(g.status.eq("after_last_observation").sum()),
                         rmse=float(np.sqrt(np.mean(e**2))) if len(e) else np.nan,
                         mae=float(np.mean(abs(e))) if len(e) else np.nan,
                         bias=float(np.mean(e)) if len(e) else np.nan,
                         late_fraction=float(np.mean(e > 0)) if len(e) else np.nan,
                         actual_lead_median=float((a.end-a.cycle).median())))
    return pd.DataFrame(rows)


def contrasts(events):
    rng = np.random.default_rng(SEED)
    comparisons = []
    for alg in ["Ridge", "RF"]:
        full = f"{alg}:HI_FULL"
        for rep in HI_COLUMNS:
            if rep != "HI_FULL":
                comparisons.append((f"{alg}:{rep}", full))
        comparisons.extend([(f"{alg}:SENSOR_RAW", f"{alg}:SENSOR_MEAN"),
                            (f"{alg}:SENSOR_MEAN", f"{alg}:SENSOR_FULL"),
                            (full, f"{alg}:SENSOR_FULL"), ("ISO_MATCHED", full), ("ISO_FROZEN", full)])
    rows = []
    for key, g in events.groupby(["subset", "dataset", "event"], sort=True):
        for a, b in comparisons:
            ga = g.loc[g.method.eq(a) & g.status.eq("available")]
            gb = g.loc[g.method.eq(b) & g.status.eq("available")]
            pair = ga.merge(gb, on=["unit", "cycle"], suffixes=("_a", "_b"))
            ea, eb = pair.error_a.to_numpy(), pair.error_b.to_numpy()
            row = dict(zip(["subset", "dataset", "event"], key)) | dict(method_a=a, method_b=b, total=len(g.unit.unique()), common=len(pair))
            if len(pair):
                boot = rng.integers(0, len(pair), size=(2000, len(pair)))
                delta = np.sqrt(np.mean(eb[boot]**2, axis=1))-np.sqrt(np.mean(ea[boot]**2, axis=1))
                row.update(rmse_a=float(np.sqrt(np.mean(ea**2))), rmse_b=float(np.sqrt(np.mean(eb**2))),
                           delta_rmse=float(np.sqrt(np.mean(eb**2))-np.sqrt(np.mean(ea**2))),
                           ci_low=float(np.quantile(delta, .025)), ci_high=float(np.quantile(delta, .975)))
            rows.append(row)
    return pd.DataFrame(rows)


def importance_ranks(importance):
    ranks = importance.groupby(["subset", "dataset", "run", "method", "representation", "group"], as_index=False).delta_mse.mean()
    ranks["rank"] = ranks.groupby(["subset", "dataset", "run", "method"]).delta_mse.rank(ascending=False, method="average")
    rows = []
    for key, g in ranks.groupby(["subset", "dataset", "representation"], sort=True):
        vectors = {(r, m): h.set_index("group")["rank"] for (r, m), h in g.groupby(["run", "method"])}
        import itertools
        for (ra, ma), (rb, mb) in itertools.combinations(vectors, 2):
            if not ((ra == rb and ma != mb) or (ra != rb and ma == mb)):
                continue
            joined = pd.concat([vectors[(ra, ma)], vectors[(rb, mb)]], axis=1).dropna()
            correlation = float(joined.iloc[:, 0].corr(joined.iloc[:, 1], method="spearman")) if len(joined) >= 2 else np.nan
            rows.append(dict(zip(["subset", "dataset", "representation"], key)) |
                        dict(run_a=ra, method_a=ma, run_b=rb, method_b=mb, groups=len(joined), spearman=correlation))
    return ranks, pd.DataFrame(rows)


def refresh_manifest():
    manifest = {p.name: sha(p) for p in sorted(OUT.iterdir()) if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    sources = source_integrity()
    start = dict(timestamp_utc=datetime.now(timezone.utc).isoformat(), sources=sources,
                 protocol_sha256=sha(ROOT / "experiments/protocolo_trajetoria_hi_08.md"),
                 script_sha256=sha(Path(__file__)))
    (OUT / "execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    all_events, all_history, all_importance, selections, coefficients, freezes = [], [], [], [], [], []
    for subset in ["FD001", "FD003"]:
        splits = json.loads((source_folder(subset) / "splits.json").read_text(encoding="utf-8"))
        inputs = read_inputs("train", subset)
        endpoints = inputs.groupby("unit").cycle.max()
        for run, partition in [(f"fold{p['fold']}", p) for p in splits["cv"]]+[("official", splits["official_training"])]:
            print(subset, run, "starting", flush=True)
            groups = [set(partition[k]) for k in ["fit", "calibration", "selection"]]
            if run != "official":
                groups.append(set(partition["evaluation"]))
            assert all(a.isdisjoint(b) for i, a in enumerate(groups) for b in groups[i+1:])
            frozen = load_models(source_folder(subset) / f"models_{run}.json")["EMPIRICO"]
            features, health, reps = build_features(inputs, frozen)
            features = label_features(features, endpoints)
            records, rows, coefs = fit_converters(features, partition, reps, frozen)
            model_path = OUT / f"models_{subset}_{run}.joblib"
            joblib.dump(records, model_path, compress=3)
            freeze = dict(subset=subset, run=run, timestamp_utc=datetime.now(timezone.utc).isoformat(),
                          models_sha256=sha(model_path), source_model_sha256=sha(source_folder(subset) / f"models_{run}.json"),
                          fit_units=partition["calibration"], selection_units=partition["selection"])
            freezes.append(freeze)
            (OUT / "freezes.json").write_text(json.dumps(freezes, indent=2), encoding="utf-8")
            for row in rows:
                row.update(subset=subset, run=run)
            for row in coefs:
                row.update(subset=subset, run=run)
            selections.extend(rows)
            coefficients.extend(coefs)
            if run == "official":
                test_inputs = read_inputs("test", subset)
                test_features, test_health, _ = build_features(test_inputs, frozen)
                # Official outcomes are attached only after the new models are frozen.
                labels = np.loadtxt(ROOT / f"CMAPSSData/RUL_{subset}.txt")
                test_endpoints = test_inputs.groupby("unit").cycle.max()+pd.Series(labels, index=np.arange(1, 101))
                test_features = label_features(test_features, test_endpoints)
                outputs = evaluate(records, test_features, test_inputs, test_health, test_endpoints, list(range(1, 101)), "truncated", subset, run)
            else:
                outputs = evaluate(records, features, inputs, health, endpoints, partition["evaluation"], "complete", subset, run)
            all_events.append(outputs[0]); all_history.append(outputs[1]); all_importance.append(outputs[2])
            print(subset, run, "completed", flush=True)
    events = pd.concat(all_events, ignore_index=True)
    history = pd.concat(all_history, ignore_index=True)
    importance = pd.concat(all_importance, ignore_index=True)
    summary = summarise(events)
    pairs = contrasts(events)
    ranks, concordance = importance_ranks(importance)
    for name, frame in [("events", events), ("history_metrics", history), ("importance", importance),
                        ("summary", summary), ("contrasts", pairs), ("importance_ranks", ranks),
                        ("rank_concordance", concordance), ("selection", pd.DataFrame(selections)),
                        ("coefficients", pd.DataFrame(coefficients))]:
        frame.to_csv(OUT / f"{name}.csv", index=False)
    assert sources == source_integrity()
    paths = [ROOT / "experiments/protocolo_trajetoria_hi_08.md", Path(__file__),
             ROOT / "experiments/test_pilot_hi_trajectory_08.py"]
    paths += [ROOT / f"experiments/{name}" for name in ["pilot_fd001.py", "pilot_fd001_04.py", "pilot_fd001_05.py", "pilot_fd003_06.py"]]
    for subset in ["FD001", "FD003"]:
        paths += [ROOT / f"CMAPSSData/{kind}_{subset}.txt" for kind in ["train", "test", "RUL"]]
        paths += list(source_folder(subset).glob("models_*.json"))+[source_folder(subset) / "splits.json"]
    metadata = dict(created_utc=datetime.now(timezone.utc).isoformat(), seed=SEED, sources=sources,
                    window=WINDOW, hi_refitted=False, predictive_interval_claim=False,
                    inputs={str(p.relative_to(ROOT)): sha(p) for p in paths},
                    packages={p: importlib.metadata.version(p) for p in ["numpy", "pandas", "scikit-learn", "joblib"]})
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    refresh_manifest()
    print(summary.loc[summary.event.eq("landmark") & summary.method.isin(["ISO_FROZEN", "ISO_MATCHED", "RF:HI", "RF:HI_FULL", "RF:SENSOR_FULL", "Ridge:HI", "Ridge:HI_FULL", "Ridge:SENSOR_FULL"]), ["subset", "dataset", "method", "available", "rmse", "bias"]].to_string(index=False))


if __name__ == "__main__":
    with threadpool_limits(limits=1):
        main()
