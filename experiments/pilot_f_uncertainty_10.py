"""P10: 98% endpoint calibration and reserve information availability."""

import hashlib
import importlib.metadata
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.isotonic import IsotonicRegression
from threadpoolctl import threadpool_limits

import pilot_fd001_05 as p05
from pilot_fd001_04 import centred_sensors
from pilot_fd003_06 import read_inputs
from pilot_hi_trajectory_08 import rolling_statistics

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "experiments/artifacts/pilot_f_uncertainty_10"
SEEDS = [20261017, 20261018, 20261019]
METHODS = ["ISO", "RF_SLOPE"]
CONFIG = {"FD001": dict(tau=100, gamma=1, ridge=.1), "FD003": dict(tau=60, gamma=2, ridge=0.)}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prior_integrity():
    records = {}
    for folder in sorted((ROOT / "experiments/artifacts").glob("pilot_*")):
        if folder == OUT or not (folder / "manifest.json").exists():
            continue
        for name, digest in json.loads((folder / "manifest.json").read_text(encoding="utf-8")).items():
            assert sha(folder / name) == digest, (folder.name, name)
        records[folder.name] = sha(folder / "manifest.json")
    return records


def partitions(seed):
    permutation = np.random.default_rng(seed).permutation(np.arange(1, 101))
    folds = []
    for k, block in enumerate(np.array_split(permutation, 10), start=1):
        remaining = np.setdiff1d(np.arange(1, 101), block)
        development = np.random.default_rng(seed+1000*k).permutation(remaining)
        fold = dict(fold=k, fit=sorted(development[:25].tolist()), converter=sorted(development[25:40].tolist()),
                    uncertainty=sorted(development[40:].tolist()), evaluation=sorted(block.tolist()))
        groups = [set(fold[name]) for name in ["fit", "converter", "uncertainty", "evaluation"]]
        assert all(a.isdisjoint(b) for j, a in enumerate(groups) for b in groups[j+1:])
        folds.append(fold)
    assert sorted(sum([f["evaluation"] for f in folds], [])) == list(range(1, 101))
    return folds


def complete_labels(inputs):
    data = inputs.reset_index(drop=True).copy()
    data["end"] = data.groupby("unit").cycle.transform("max")
    data["rul"] = data.end-data.cycle
    return data


def fit_health(fit_inputs, subset):
    data = complete_labels(fit_inputs.drop(columns=["end", "rul"], errors="ignore"))
    ids = sorted(data.unit.unique().tolist())
    centred = centred_sensors(data)
    stats = p05.fitting_stats(data, ids, centred)
    z = p05.standardise(centred, stats)
    beta = p05.fit_empirical(data, z, ids, **CONFIG[subset])
    return dict(stats=stats, beta=beta, config=CONFIG[subset], fit_units=ids)


def features(inputs, health_model):
    data = inputs.drop(columns=["end", "rul"], errors="ignore").reset_index(drop=True)
    z = p05.standardise(centred_sensors(data), health_model["stats"])
    values = p05.empirical_hi(z, health_model["beta"])
    available = data.cycle.ge(20)
    health = data.loc[available, ["unit", "cycle"]].copy()
    health["hi"] = values[np.asarray(available)]
    health["h_slope"] = np.nan
    for _, g in health.groupby("unit", sort=False):
        health.loc[g.index, "h_slope"] = rolling_statistics(g.hi.to_numpy())["slope"][:, 0]
    crossings = health.loc[health.hi.le(.5)].groupby("unit").cycle.min()
    health["crossing"] = health.unit.map(crossings)
    valid = health.loc[health.cycle.ge(39)].copy()
    valid["in_domain"] = valid.cycle.ge(valid.crossing)
    assert np.isfinite(valid[["hi", "h_slope"]]).all().all()
    return valid, health


def attach_labels(frame, endpoints):
    data = frame.copy()
    data["end"] = data.unit.map(endpoints)
    data["rul"] = data.end-data.cycle
    return data


def fit_pipeline(fit_inputs, converter_inputs, subset, seed):
    health_model = fit_health(fit_inputs, subset)
    frame, _ = features(converter_inputs, health_model)
    data = attach_labels(frame, converter_inputs.groupby("unit").cycle.max())
    weights = p05.equal_engine_weights(data.unit)
    predictors = {}
    for method in METHODS:
        columns = ["hi", "h_slope"] if method == "RF_SLOPE" else ["hi"]
        if method == "ISO":
            model = IsotonicRegression(increasing=True, y_min=0., out_of_bounds="clip")
            model.fit(data.hi.to_numpy(), data.rul.to_numpy(), sample_weight=weights)
        else:
            model = RandomForestRegressor(n_estimators=150, max_depth=12, min_samples_leaf=5,
                                          n_jobs=4, random_state=seed)
            model.fit(data[columns].to_numpy(), data.rul.to_numpy(), sample_weight=weights)
        predictors[method] = dict(model=model, columns=columns,
                                  fit_units=sorted(data.unit.unique().tolist()))
    return dict(health=health_model, predictors=predictors, subset=subset, seed=seed)


def predict_inputs(bundle, inputs):
    frame, health = features(inputs, bundle["health"])
    outputs = []
    for method in METHODS:
        record = bundle["predictors"][method]
        x = frame[record["columns"]].to_numpy()
        prediction = record["model"].predict(x[:, 0] if method == "ISO" else x)
        out = frame.copy()
        out["predicted_rul"] = np.maximum(0., prediction)
        out["method"] = method
        outputs.append(out)
    return pd.concat(outputs, ignore_index=True), health


def score_engines(predictions, health, inputs, endpoints, units):
    records, events = [], []
    for unit in units:
        h = health.loc[health.unit.eq(unit)]
        hits = h.loc[h.hi.le(.5), "cycle"]
        crossing = int(hits.min()) if len(hits) else np.nan
        last = int(inputs.loc[inputs.unit.eq(unit), "cycle"].max())
        for method in METHODS:
            g = predictions.loc[predictions.unit.eq(unit) & predictions.method.eq(method)].sort_values("cycle")
            path = g.loc[g.in_domain]
            record = dict(unit=unit, method=method, crossing=crossing, end=endpoints.loc[unit], last=last,
                          available_path=len(path) > 0, available_point=False, cycles=len(path),
                          path_abs=np.nan, path_late=np.nan, point_abs=np.nan, point_late=np.nan)
            if len(path):
                errors = path.error.to_numpy()
                record.update(path_abs=float(np.max(abs(errors))), path_late=float(max(0., np.max(errors))),
                              path_rmse=float(np.sqrt(np.mean(errors**2))), path_bias=float(np.mean(errors)),
                              positive_fraction=float(np.mean(errors > 0)))
            targets = {"mark": crossing, "plus5": crossing+5, "plus10": crossing+10,
                       "plus20": crossing+20, "last": last if np.isfinite(crossing) and last >= crossing else np.nan}
            for name, cycle in targets.items():
                status = "no_observed_crossing" if np.isnan(cycle) else "before_features" if cycle < 39 else "after_last" if cycle > last else "available"
                event = dict(unit=unit, method=method, event=name, cycle=cycle, crossing=crossing,
                             end=endpoints.loc[unit], status=status)
                if status == "available":
                    point = g.loc[g.cycle.eq(cycle)].iloc[0]
                    event.update(predicted_rul=point.predicted_rul, actual_rul=point.rul,
                                 error=point.error, hi=point.hi)
                    if name == "mark":
                        record.update(available_point=True, point_abs=float(abs(point.error)),
                                      point_late=float(max(point.error, 0.)))
                events.append(event)
            records.append(record)
    return pd.DataFrame(records), pd.DataFrame(events)


def corrected_quantile(scores, alpha):
    a = np.sort(np.asarray(scores, dtype=float))
    assert np.isfinite(a).all() and (a >= 0).all()
    n = len(a)
    k = int(math.ceil((n+1)*(1-alpha)))
    return (float(a[k-1]) if k <= n else float("inf")), n, k


def calibrate(scores):
    rows = []
    for method in METHODS:
        for scope in ["point", "path"]:
            sample = scores.loc[scores.method.eq(method) & scores[f"available_{scope}"]]
            for alpha in [.02, .05]:
                qa, n, k = corrected_quantile(sample[f"{scope}_abs"], alpha)
                ql, _, _ = corrected_quantile(sample[f"{scope}_late"], alpha)
                rows.append(dict(method=method, scope=scope, alpha=alpha, n=n, k=k, q_abs=qa, q_late=ql))
    return pd.DataFrame(rows)


def evaluate_bands(predictions, scores, events, quantiles):
    rows = []
    for q in quantiles.itertuples():
        units = scores.loc[scores.method.eq(q.method)]
        for r in units.itertuples():
            record = dict(unit=r.unit, method=q.method, scope=q.scope, alpha=q.alpha,
                          q_abs=q.q_abs, q_late=q.q_late, calibration_n=q.n,
                          available_path=r.available_path, available_point=r.available_point,
                          finite_abs=bool(np.isfinite(q.q_abs)), finite_late=bool(np.isfinite(q.q_late)))
            if r.available_path:
                g = predictions.loc[predictions.method.eq(q.method) & predictions.unit.eq(r.unit) & predictions.in_domain]
                upper = g.cycle+g.predicted_rul+q.q_abs
                lower = np.maximum(g.cycle, g.cycle+g.predicted_rul-q.q_abs)
                conservative = np.maximum(g.cycle, g.cycle+g.predicted_rul-q.q_late)
                record.update(path_coverage=bool(r.path_abs <= q.q_abs+1e-10),
                              path_lower_coverage=bool(r.path_late <= q.q_late+1e-10),
                              median_width=float(np.median(upper-lower)),
                              collapsed_fraction=float(np.mean(np.isclose(conservative, g.cycle, atol=1e-10))))
            if r.available_point:
                point = events.loc[events.method.eq(q.method) & events.unit.eq(r.unit) & events.event.eq("mark")].iloc[0]
                lower = max(point.cycle, point.cycle+point.predicted_rul-q.q_late)
                record.update(point_coverage=bool(abs(point.error) <= q.q_abs+1e-10),
                              point_lower_coverage=bool(point.error <= q.q_late+1e-10),
                              conservative_lead=float(lower-point.cycle),
                              collapsed_point=bool(np.isclose(lower, point.cycle, atol=1e-10)))
            rows.append(record)
    return pd.DataFrame(rows)


def point_summary(events):
    rows = []
    for key, g in events.groupby(["subset", "dataset", "repeat", "method", "event"], sort=True):
        a = g.loc[g.status.eq("available")]
        errors = a.error.to_numpy()
        rows.append(dict(zip(["subset", "dataset", "repeat", "method", "event"], key)) |
                    dict(total=len(g), available=len(a), no_crossing=int(g.status.eq("no_observed_crossing").sum()),
                         before_features=int(g.status.eq("before_features").sum()),
                         rmse=float(np.sqrt(np.mean(errors**2))) if len(a) else np.nan,
                         mae=float(np.mean(abs(errors))) if len(a) else np.nan,
                         bias=float(np.mean(errors)) if len(a) else np.nan,
                         positive_fraction=float(np.mean(errors > 0)) if len(a) else np.nan,
                         late_error_mean=float(np.mean(np.maximum(errors, 0.))) if len(a) else np.nan,
                         actual_lead_median=float(a.actual_rul.median()) if len(a) else np.nan))
    return pd.DataFrame(rows)


def band_summary(bands):
    rows = []
    for key, g in bands.groupby(["subset", "dataset", "repeat", "method", "scope", "alpha"], sort=True):
        path = g.loc[g.available_path]
        point = g.loc[g.available_point]
        row = dict(zip(["subset", "dataset", "repeat", "method", "scope", "alpha"], key))
        row.update(total=len(g), path_available=len(path), point_available=len(point),
                   finite_abs_fraction=float(path.finite_abs.mean()), finite_late_fraction=float(path.finite_late.mean()),
                   path_coverage=float(path.path_coverage.mean()), path_lower_coverage=float(path.path_lower_coverage.mean()),
                   point_coverage=float(point.point_coverage.mean()), point_lower_coverage=float(point.point_lower_coverage.mean()),
                   median_width=float(path.median_width.median()), collapsed_point_fraction=float(point.collapsed_point.mean()),
                   conservative_lead_median=float(point.conservative_lead.median()),
                   calibration_n_min=int(g.calibration_n.min()))
        rows.append(row)
    return pd.DataFrame(rows)


def contrasts(events):
    rng = np.random.default_rng(SEEDS[0])
    rows = []
    for key, g in events.groupby(["subset", "dataset", "repeat", "event"], sort=True):
        for reference in ["ISO"]:
            a = g.loc[g.method.eq(reference) & g.status.eq("available")]
            b = g.loc[g.method.eq("RF_SLOPE") & g.status.eq("available")]
            pair = a.merge(b, on=["unit", "cycle"], suffixes=("_a", "_b"))
            record = dict(zip(["subset", "dataset", "repeat", "event"], key)) | dict(reference=reference, common=len(pair))
            if len(pair):
                ea, eb = pair.error_a.to_numpy(), pair.error_b.to_numpy()
                idx = rng.integers(0, len(pair), size=(2000, len(pair)))
                delta = np.sqrt(np.mean(eb[idx]**2, axis=1))-np.sqrt(np.mean(ea[idx]**2, axis=1))
                record.update(delta_rmse=float(np.sqrt(np.mean(eb**2))-np.sqrt(np.mean(ea**2))),
                              ci_low=float(np.quantile(delta, .025)), ci_high=float(np.quantile(delta, .975)))
            rows.append(record)
    return pd.DataFrame(rows)


def reserve_diagnostics(predictions, scores, quantiles):
    """Information availability only; no removal schedule or reserve anchor adopted."""
    rows = []
    for q in quantiles.itertuples():
        for r in scores.loc[scores.method.eq(q.method)].itertuples():
            path = predictions.loc[predictions.unit.eq(r.unit) & predictions.method.eq(q.method) & predictions.in_domain]
            leads = np.maximum(0., path.predicted_rul.to_numpy()-q.q_late)
            for reserve in [15, 12]:
                for delay in [1, 2]:
                    record = dict(unit=r.unit, method=q.method, scope=q.scope, alpha=q.alpha,
                                  reserve=reserve, delay=delay, available_path=r.available_path,
                                  available_point=r.available_point)
                    if len(path):
                        ok = leads >= reserve+delay-1e-9
                        record.update(any_available=bool(ok.any()), cycle_fraction=float(ok.mean()))
                        if r.available_point:
                            record['mark_available'] = bool(ok[path.cycle.to_numpy() == r.crossing][0])
                    rows.append(record)
    return pd.DataFrame(rows)


def reserve_summary(reserves):
    rows = []
    keys = ['subset', 'dataset', 'repeat', 'method', 'scope', 'alpha', 'reserve', 'delay']
    for key, g in reserves.groupby(keys, sort=True):
        path = g.loc[g.available_path]
        point = g.loc[g.available_point]
        rows.append(dict(zip(keys, key)) | dict(total=len(g), path_available=len(path),
                    point_available=len(point), mark_fraction=float(point.mark_available.mean()),
                    any_fraction=float(path.any_available.mean()), cycle_fraction=float(path.cycle_fraction.mean())))
    return pd.DataFrame(rows)


def refresh_manifest():
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir()) if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    before = prior_integrity()
    files = [ROOT / "experiments/protocolo_incerteza_f_10.md", Path(__file__),
             ROOT / "experiments/verify_pilot_f_uncertainty_10.py",
             ROOT / "experiments/test_pilot_f_uncertainty_10.py"]
    files += [ROOT / f"experiments/{name}.py" for name in ["pilot_fd001", "pilot_fd001_04", "pilot_fd001_05", "pilot_fd003_06", "pilot_hi_trajectory_08"]]
    files += [ROOT / f"CMAPSSData/{kind}_{subset}.txt" for subset in CONFIG for kind in ["train", "test", "RUL"]]
    initial = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=before,
                   inputs={str(p.relative_to(ROOT)): sha(p) for p in files},
                   seeds=SEEDS, configuration=CONFIG)
    (OUT / "execution_start.json").write_text(json.dumps(initial, indent=2), encoding="utf-8")
    all_scores, all_events, all_bands, all_quantiles, all_reserves, splits, freezes = [], [], [], [], [], [], []
    for subset in CONFIG:
        inputs = read_inputs("train", subset)
        for repeat, seed in enumerate(SEEDS, start=1):
            for partition in partitions(seed):
                fold = partition["fold"]
                tag = f"{subset}_r{repeat}_f{fold}"
                print(tag, "fit", flush=True)
                selection = lambda ids: inputs.loc[inputs.unit.isin(ids)].reset_index(drop=True)
                bundle = fit_pipeline(selection(partition["fit"]), selection(partition["converter"]), subset, seed)
                model_path = OUT / f"models_{tag}.joblib"
                joblib.dump(bundle, model_path, compress=3)
                u_inputs = selection(partition["uncertainty"])
                u_pred, u_health = predict_inputs(bundle, u_inputs)
                u_end = u_inputs.groupby("unit").cycle.max()
                u_pred = attach_labels(u_pred, u_end)
                u_pred["error"] = u_pred.predicted_rul-u_pred.rul
                u_scores, _ = score_engines(u_pred, u_health, u_inputs, u_end, partition["uncertainty"])
                quantiles = calibrate(u_scores)
                quantile_path = OUT / f"quantiles_{tag}.csv"
                quantiles.to_csv(quantile_path, index=False)
                freezes.append(dict(subset=subset, repeat=repeat, fold=fold, models_sha256=sha(model_path),
                                    quantiles_sha256=sha(quantile_path), timestamp_utc=datetime.now(timezone.utc).isoformat()))
                (OUT / "freezes.json").write_text(json.dumps(freezes, indent=2), encoding="utf-8")
                u_pred.to_csv(OUT / f"predictions_{tag}_U.csv.gz", index=False, compression="gzip")
                u_scores = u_scores.assign(subset=subset, repeat=repeat, fold=fold, dataset="calibration")
                all_scores.append(u_scores)
                quantiles = quantiles.assign(subset=subset, repeat=repeat, fold=fold)
                all_quantiles.append(quantiles)
                splits.append(dict(subset=subset, repeat=repeat, seed=seed, **partition))
                evaluations = [("complete", selection(partition["evaluation"]), partition["evaluation"])]
                if fold == 1:
                    evaluations.append(("truncated", read_inputs("test", subset), list(range(1, 101))))
                for dataset, evaluation_inputs, units in evaluations:
                    prediction, health = predict_inputs(bundle, evaluation_inputs)
                    end = evaluation_inputs.groupby("unit").cycle.max()
                    if dataset == "truncated":
                        labels = np.loadtxt(ROOT / f"CMAPSSData/RUL_{subset}.txt")
                        end = end+pd.Series(labels, index=np.arange(1, 101))
                    prediction = attach_labels(prediction, end)
                    prediction["error"] = prediction.predicted_rul-prediction.rul
                    scores, events = score_engines(prediction, health, evaluation_inputs, end, units)
                    bands = evaluate_bands(prediction, scores, events, quantiles)
                    reserves = reserve_diagnostics(prediction, scores, quantiles)
                    prediction.to_csv(OUT / f"predictions_{tag}_{dataset}.csv.gz", index=False, compression="gzip")
                    for frame in [scores, events, bands, reserves]:
                        frame["subset"], frame["dataset"], frame["repeat"], frame["fold"] = subset, dataset, repeat, fold
                    all_scores.append(scores); all_events.append(events); all_bands.append(bands); all_reserves.append(reserves)
                print(tag, "complete", flush=True)
    events = pd.concat(all_events, ignore_index=True)
    scores = pd.concat(all_scores, ignore_index=True)
    bands = pd.concat(all_bands, ignore_index=True)
    quantiles = pd.concat(all_quantiles, ignore_index=True)
    points = point_summary(events)
    intervals = band_summary(bands)
    pairs = contrasts(events)
    reserves = pd.concat(all_reserves, ignore_index=True)
    for name, frame in [("scores", scores), ("events", events), ("bands", bands), ("quantiles", quantiles),
                        ("point_summary", points), ("band_summary", intervals), ("contrasts", pairs), ("reserves", reserves), ("reserve_summary", reserve_summary(reserves))]:
        frame.to_csv(OUT / f"{name}.csv", index=False)
    (OUT / "splits.json").write_text(json.dumps(splits, indent=2), encoding="utf-8")
    assert before == prior_integrity()
    metadata = initial | dict(finished_utc=datetime.now(timezone.utc).isoformat(),
                             previous_manifests_intact=True, hi_form_changed=False, calibration_engines_exclusive=True,
                             packages={name: importlib.metadata.version(name) for name in ["numpy", "pandas", "scikit-learn", "scipy", "joblib"]})
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    refresh_manifest()
    print(points.loc[points.event.eq("mark"), ["subset", "dataset", "repeat", "method", "available", "rmse", "bias"]].to_string(index=False))
    print(intervals.loc[intervals.dataset.eq("complete") & intervals.scope.eq("path") & intervals.alpha.eq(.02),
                        ["subset", "repeat", "method", "path_available", "path_coverage", "path_lower_coverage", "median_width", "conservative_lead_median", "collapsed_point_fraction"]].to_string(index=False))


if __name__ == "__main__":
    with threadpool_limits(limits=1):
        main()
