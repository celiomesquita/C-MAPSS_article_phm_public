"""Rebuild frozen P08 predictions and independently check paired event metrics."""

import json

import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits

import pilot_hi_trajectory_08 as p08


def main():
    out = p08.OUT
    meta = json.loads((out / "metadata.json").read_text(encoding="utf-8"))
    amendment_path = out / "rank_correction.json"
    amendment = json.loads(amendment_path.read_text(encoding="utf-8")) if amendment_path.exists() else {}
    assert p08.source_integrity() == meta["sources"]
    for name, digest in meta["inputs"].items():
        if name.replace("\\", "/") == "experiments/pilot_hi_trajectory_08.py" and digest == amendment.get("executed_script_sha256"):
            assert p08.sha(out / "pilot_hi_trajectory_08_executed.py") == digest
            assert p08.sha(p08.ROOT / name) == amendment["corrected_script_sha256"]
        else:
            assert p08.sha(p08.ROOT / name) == digest, name
    for name, digest in json.loads((out / "manifest.json").read_text(encoding="utf-8")).items():
        assert p08.sha(out / name) == digest, name
    start = json.loads((out / "execution_start.json").read_text(encoding="utf-8"))
    assert start["protocol_sha256"] == p08.sha(p08.ROOT / "experiments/protocolo_trajetoria_hi_08.md")
    executed_script = out / "pilot_hi_trajectory_08_executed.py" if start["script_sha256"] == amendment.get("executed_script_sha256") else p08.ROOT / "experiments/pilot_hi_trajectory_08.py"
    assert start["script_sha256"] == p08.sha(executed_script)
    freezes = json.loads((out / "freezes.json").read_text(encoding="utf-8"))
    assert len(freezes) == 12
    events = pd.read_csv(out / "events.csv")
    summary = pd.read_csv(out / "summary.csv")
    contrasts = pd.read_csv(out / "contrasts.csv")
    selection = pd.read_csv(out / "selection.csv")
    importance = pd.read_csv(out / "importance.csv")
    history = pd.read_csv(out / "history_metrics.csv")
    assert len(events) == 43200 and len(summary) == 432 and len(contrasts) == 432
    max_error, prediction_count, importance_checks = 0., 0, 0
    for subset in ["FD001", "FD003"]:
        splits = json.loads((p08.source_folder(subset) / "splits.json").read_text(encoding="utf-8"))
        for run, partition in [(f"fold{p['fold']}", p) for p in splits["cv"]]+[("official", splits["official_training"])]:
            print("verify", subset, run, flush=True)
            kind = "test" if run == "official" else "train"
            dataset = "truncated" if run == "official" else "complete"
            inputs = p08.read_inputs(kind, subset)
            endpoints = inputs.groupby("unit").cycle.max()
            if kind == "test":
                endpoints = endpoints+pd.Series(np.loadtxt(p08.ROOT / f"CMAPSSData/RUL_{subset}.txt"), index=np.arange(1, 101))
            frozen = p08.load_models(p08.source_folder(subset) / f"models_{run}.json")["EMPIRICO"]
            frame, health, reps = p08.build_features(inputs, frozen)
            frame = p08.label_features(frame, endpoints)
            if kind == "test":
                train_inputs = p08.read_inputs("train", subset)
                training, _, _ = p08.build_features(train_inputs, frozen)
                training = p08.label_features(training, train_inputs.groupby("unit").cycle.max())
            else:
                training = frame
            records = joblib.load(out / f"models_{subset}_{run}.joblib")
            assert len(records) == 24
            freeze = next(r for r in freezes if r["subset"] == subset and r["run"] == run)
            assert p08.sha(out / f"models_{subset}_{run}.joblib") == freeze["models_sha256"]
            assert p08.sha(p08.source_folder(subset) / f"models_{run}.json") == freeze["source_model_sha256"]
            predictions = pd.read_csv(out / f"predictions_{subset}_{run}.csv.gz")
            units = list(range(1, 101)) if run == "official" else partition["evaluation"]
            assert set(predictions.unit).issubset(set(units))
            assert not predictions.duplicated(["method", "unit", "cycle"]).any()
            assert set(units).isdisjoint(partition["calibration"]) if run != "official" else True
            selected = frame.loc[frame.unit.isin(units)]
            e = events.loc[events.subset.eq(subset) & events.run.eq(run)]
            for method, record in records.items():
                assert record["fit_units"] == sorted(partition["calibration"])
                assert set(record["columns"]).isdisjoint({"unit", "cycle", "end", "rul", "frozen_rul"})
                actual = predictions.loc[predictions.method.eq(method)].sort_values(["unit", "cycle"])
                rebuilt = selected[["unit", "cycle"]].copy()
                rebuilt["prediction"] = p08.predict(record, selected)
                rebuilt = rebuilt.sort_values(["unit", "cycle"])
                np.testing.assert_array_equal(actual[["unit", "cycle"]], rebuilt[["unit", "cycle"]])
                diff = float(np.max(abs(actual.predicted_rul.to_numpy()-rebuilt.prediction.to_numpy())))
                assert diff < 1e-8
                max_error = max(max_error, diff)
                prediction_count += len(actual)
                np.testing.assert_allclose(actual.error, actual.predicted_rul-actual.rul, atol=1e-10)
                np.testing.assert_allclose(actual.end-actual.cycle, actual.rul, atol=1e-10)
                for unit in units:
                    h = health.loc[health.unit.eq(unit)]
                    hits = h.loc[h.hi.le(.5), "cycle"]
                    crossing = hits.min() if len(hits) else np.nan
                    last = inputs.loc[inputs.unit.eq(unit), "cycle"].max()
                    unit_events = e.loc[e.method.eq(method) & e.unit.eq(unit)]
                    for r in unit_events.itertuples():
                        target = last if r.event == "last" else crossing+p08.EVENTS[r.event]
                        status = "no_observed_crossing" if np.isnan(target) else "before_feature_availability" if target < 39 else "after_last_observation" if target > last else "available"
                        assert r.status == status
                        np.testing.assert_allclose(r.cycle, target, equal_nan=True)
                        if status == "available":
                            point = actual.loc[actual.unit.eq(unit) & actual.cycle.eq(target)].iloc[0]
                            np.testing.assert_allclose(r.error, point.error, atol=1e-9)
                if record["algorithm"] == "Ridge":
                    train = training.loc[training.unit.isin(partition["calibration"])]
                    weights = p08.p05.equal_engine_weights(train.unit)
                    expected = np.average(train[record["columns"]].to_numpy(), axis=0, weights=weights)
                    np.testing.assert_allclose(record["scaler"].mean_, expected, atol=1e-10)
                    candidates = selection.loc[selection.subset.eq(subset) & selection.run.eq(run) & selection.algorithm.eq("Ridge") & selection.representation.eq(record["representation"])]
                    best = candidates.sort_values(["selection_rmse", "alpha"]).iloc[0]
                    assert best.chosen and best.alpha == record["alpha"]
                if record["algorithm"] in ["Ridge", "RF"]:
                    selection_inputs = training.loc[training.unit.isin(partition["selection"])]
                    loss = p08.selection_loss(selection_inputs, p08.predict(record, selection_inputs))
                    saved_loss = selection.loc[selection.subset.eq(subset) & selection.run.eq(run) & selection.algorithm.eq(record["algorithm"]) & selection.representation.eq(record["representation"]) & selection.chosen, "selection_rmse"]
                    np.testing.assert_allclose(saved_loss.iloc[0], loss, atol=1e-8)
            landmark = e.loc[e.method.eq("RF:HI_FULL") & e.event.eq("landmark") & e.status.eq("available"), ["unit", "cycle"]]
            sample = selected.merge(landmark, on=["unit", "cycle"]).sort_values("unit")
            for algorithm in ["Ridge", "RF"]:
                for representation in ["HI_FULL", "SENSOR_FULL"]:
                    method = f"{algorithm}:{representation}"
                    record = records[method]
                    groups = ({name: [name] for name in p08.HI_COLUMNS["HI_FULL"]} if representation == "HI_FULL" else
                              {s: [c for c in record["columns"] if c.endswith("_"+s)] for s in sorted({c.split("_")[-1] for c in record["columns"]})})
                    rng = np.random.default_rng(p08.SEED)
                    base = (p08.predict(record, sample)-sample.rul.to_numpy())**2
                    for group, columns in groups.items():
                        for repeat in range(20):
                            order = rng.permutation(len(sample))
                            if repeat:
                                continue
                            changed = sample.copy()
                            changed[columns] = sample[columns].to_numpy()[order]
                            delta = np.mean((p08.predict(record, changed)-sample.rul.to_numpy())**2-base)
                            saved = importance.loc[importance.subset.eq(subset) & importance.run.eq(run) & importance.method.eq(method) & importance.group.eq(group) & importance.repeat.eq(0)]
                            assert len(saved) == 1
                            np.testing.assert_allclose(saved.delta_mse.iloc[0], delta, atol=1e-8)
                            importance_checks += 1
            for r in history.loc[history.subset.eq(subset) & history.run.eq(run)].itertuples():
                g = predictions.loc[predictions.method.eq(r.method) & predictions.unit.eq(r.unit)]
                np.testing.assert_allclose(r.rmse, np.sqrt(np.mean(g.error**2)), atol=1e-9)
    for r in summary.itertuples():
        g = events.loc[events.subset.eq(r.subset) & events.dataset.eq(r.dataset) & events.method.eq(r.method) & events.event.eq(r.event)]
        a = g.loc[g.status.eq("available")]
        assert len(g) == r.total == 100 and len(a) == r.available
        np.testing.assert_allclose([r.rmse, r.mae, r.bias], [np.sqrt(np.mean(a.error**2)), np.mean(abs(a.error)), np.mean(a.error)], atol=1e-9)
    rng = np.random.default_rng(p08.SEED)
    for r in contrasts.itertuples():
        g = events.loc[events.subset.eq(r.subset) & events.dataset.eq(r.dataset) & events.event.eq(r.event) & events.status.eq("available")]
        a, b = g.loc[g.method.eq(r.method_a)], g.loc[g.method.eq(r.method_b)]
        pair = a.merge(b, on=["unit", "cycle"], suffixes=("_a", "_b"))
        assert len(pair) == r.common
        ea, eb = pair.error_a.to_numpy(), pair.error_b.to_numpy()
        idx = rng.integers(0, len(pair), size=(2000, len(pair)))
        delta = np.sqrt(np.mean(eb[idx]**2, axis=1))-np.sqrt(np.mean(ea[idx]**2, axis=1))
        np.testing.assert_allclose([r.rmse_a, r.rmse_b, r.delta_rmse, r.ci_low, r.ci_high],
                                   [np.sqrt(np.mean(ea**2)), np.sqrt(np.mean(eb**2)), np.sqrt(np.mean(eb**2))-np.sqrt(np.mean(ea**2)), *np.quantile(delta, [.025, .975])], atol=1e-8)
    ranks, concordance = p08.importance_ranks(importance)
    pd.testing.assert_frame_equal(ranks, pd.read_csv(out / "importance_ranks.csv"), check_dtype=False, atol=1e-9)
    pd.testing.assert_frame_equal(concordance, pd.read_csv(out / "rank_concordance.csv"), check_dtype=False, atol=1e-9)
    verification = dict(status="passed", events=len(events), predictions_rebuilt=prediction_count,
                        maximum_prediction_difference=max_error, contrasts_and_intervals_checked=len(contrasts),
                        importance_permutations_spot_checked=importance_checks,
                        original_manifests_intact=True, hi_refitted=False,
                        verifier_sha256=p08.sha(p08.ROOT / "experiments/verify_pilot_hi_trajectory_08.py"))
    (out / "verification.json").write_text(json.dumps(verification, indent=2), encoding="utf-8")
    p08.refresh_manifest()
    print(json.dumps(verification))


if __name__ == "__main__":
    with threadpool_limits(limits=1):
        main()
