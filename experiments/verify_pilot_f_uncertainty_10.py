"""Verify P10 frozen parameters, endpoint forecasts and engine-level calibration."""

import json
import math

import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits

import pilot_f_uncertainty_10 as p09


def main():
    out = p09.OUT
    metadata = json.loads((out / "metadata.json").read_text(encoding="utf-8"))
    assert p09.prior_integrity() == metadata["previous_manifests"]
    archive_path = out / "frozen_input_archive.json"
    archive = json.loads(archive_path.read_text(encoding="utf-8")) if archive_path.exists() else {}
    for name, digest in metadata["inputs"].items():
        assert p09.sha(p09.ROOT / archive.get(name, name)) == digest, name
    amendment = out / "amendment_numeric_boundary.json"
    if amendment.exists():
        record = json.loads(amendment.read_text(encoding="utf-8"))
        for name, digest in record["current_sources"].items():
            assert p09.sha(p09.ROOT / name) == digest, name
        for name, digest in record["unchanged_frozen_files"].items():
            assert p09.sha(out / name) == digest, name
    for name, digest in json.loads((out / "manifest.json").read_text(encoding="utf-8")).items():
        assert p09.sha(out / name) == digest, name
    splits = json.loads((out / "splits.json").read_text(encoding="utf-8"))
    freezes = json.loads((out / "freezes.json").read_text(encoding="utf-8"))
    scores = pd.read_csv(out / "scores.csv")
    events = pd.read_csv(out / "events.csv")
    bands = pd.read_csv(out / "bands.csv")
    quantiles = pd.read_csv(out / "quantiles.csv")
    assert len(splits) == len(freezes) == 60
    assert len(scores) == 8400 and len(events) == 12000 and len(bands) == 9600 and len(quantiles) == 480
    max_error, forecast_rows, band_checks = 0., 0, 0
    for partition in splits:
        subset, repeat, fold = partition["subset"], partition["repeat"], partition["fold"]
        print("verify", subset, repeat, fold, flush=True)
        tag = f"{subset}_r{repeat}_f{fold}"
        fixed = p09.partitions(partition["seed"])[fold-1]
        for name in fixed:
            assert partition[name] == fixed[name]
        inputs = p09.read_inputs("train", subset)
        bundle = joblib.load(out / f"models_{tag}.joblib")
        assert bundle["health"]["fit_units"] == partition["fit"]
        refit = p09.fit_health(inputs.loc[inputs.unit.isin(partition["fit"])], subset)
        np.testing.assert_allclose(refit["beta"], bundle["health"]["beta"], atol=1e-10)
        assert refit["stats"]["channels"] == bundle["health"]["stats"]["channels"]
        np.testing.assert_allclose(refit["stats"]["scale"], bundle["health"]["stats"]["scale"], atol=1e-10)
        np.testing.assert_array_equal(refit["stats"]["direction"], bundle["health"]["stats"]["direction"])
        for method, record in bundle["predictors"].items():
            assert record["fit_units"] == partition["converter"]
            assert record["columns"] == (["hi", "h_slope"] if method == "RF_SLOPE" else ["hi"])
        frozen = next(r for r in freezes if r["subset"] == subset and r["repeat"] == repeat and r["fold"] == fold)
        assert p09.sha(out / f"models_{tag}.joblib") == frozen["models_sha256"]
        assert p09.sha(out / f"quantiles_{tag}.csv") == frozen["quantiles_sha256"]
        qrows = quantiles.loc[quantiles.subset.eq(subset) & quantiles.repeat.eq(repeat) & quantiles.fold.eq(fold)]
        u_scores = scores.loc[scores.subset.eq(subset) & scores.repeat.eq(repeat) & scores.fold.eq(fold) & scores.dataset.eq("calibration")]
        for q in qrows.itertuples():
            sample = u_scores.loc[u_scores.method.eq(q.method) & u_scores[f"available_{q.scope}"]]
            rank = math.ceil((len(sample)+1)*(1-q.alpha))
            assert q.n == len(sample) and q.k == rank
            for kind in ["abs", "late"]:
                a = np.sort(sample[f"{q.scope}_{kind}"].to_numpy())
                expected = a[rank-1] if rank <= len(a) else float("inf")
                np.testing.assert_allclose(getattr(q, f"q_{kind}"), expected, atol=1e-9)
        datasets = ["U", "complete"]+(["truncated"] if fold == 1 else [])
        for dataset in datasets:
            ids = partition["uncertainty"] if dataset == "U" else partition["evaluation"] if dataset == "complete" else list(range(1, 101))
            raw = p09.read_inputs("test", subset) if dataset == "truncated" else inputs.loc[inputs.unit.isin(ids)].reset_index(drop=True)
            expected, health = p09.predict_inputs(bundle, raw)
            end = raw.groupby("unit").cycle.max()
            if dataset == "truncated":
                end = end+pd.Series(np.loadtxt(p09.ROOT / f"CMAPSSData/RUL_{subset}.txt"), index=np.arange(1, 101))
            actual = pd.read_csv(out / f"predictions_{tag}_{dataset}.csv.gz")
            sort = ["method", "unit", "cycle"]
            a, b = actual.sort_values(sort), expected.sort_values(sort)
            np.testing.assert_array_equal(a[sort], b[sort])
            diff = np.max(abs(a.predicted_rul.to_numpy()-b.predicted_rul.to_numpy()))
            assert diff < 1e-8
            max_error = max(max_error, float(diff))
            forecast_rows += len(actual)
            np.testing.assert_allclose(actual.end, actual.unit.map(end), atol=1e-10)
            np.testing.assert_allclose(actual.error, actual.predicted_rul-(actual.end-actual.cycle), atol=1e-9)
            label = "calibration" if dataset == "U" else dataset
            saved = scores.loc[scores.subset.eq(subset) & scores.repeat.eq(repeat) & scores.fold.eq(fold) & scores.dataset.eq(label)]
            for r in saved.itertuples():
                g = actual.loc[actual.unit.eq(r.unit) & actual.method.eq(r.method)].sort_values("cycle")
                h = health.loc[health.unit.eq(r.unit)]
                hit = h.loc[h.hi.le(.5), "cycle"]
                crossing = hit.min() if len(hit) else np.nan
                np.testing.assert_allclose(r.crossing, crossing, equal_nan=True)
                np.testing.assert_array_equal(g.in_domain, g.cycle.ge(crossing))
                path = g.loc[g.in_domain]
                assert r.available_path == bool(len(path))
                assert r.available_point == bool(np.isfinite(crossing) and crossing >= 39)
                if len(path):
                    np.testing.assert_allclose([r.path_abs, r.path_late],
                                               [max(abs(path.error)), max(0., max(path.error))], atol=1e-9)
                if r.available_point:
                    point = g.loc[g.cycle.eq(crossing)].iloc[0]
                    np.testing.assert_allclose([r.point_abs, r.point_late], [abs(point.error), max(0., point.error)], atol=1e-9)
            if dataset == "U":
                continue
            ev = events.loc[events.subset.eq(subset) & events.repeat.eq(repeat) & events.fold.eq(fold) & events.dataset.eq(dataset)]
            for r in ev.itertuples():
                if r.status == "available":
                    point = actual.loc[actual.unit.eq(r.unit) & actual.method.eq(r.method) & actual.cycle.eq(r.cycle)].iloc[0]
                    np.testing.assert_allclose(r.error, point.error, atol=1e-9)
            bs = bands.loc[bands.subset.eq(subset) & bands.repeat.eq(repeat) & bands.fold.eq(fold) & bands.dataset.eq(dataset)]
            for r in bs.itertuples():
                g = actual.loc[actual.unit.eq(r.unit) & actual.method.eq(r.method) & actual.in_domain]
                if not len(g):
                    assert not r.available_path
                    continue
                point_f = g.cycle+g.predicted_rul
                lower = np.maximum(g.cycle, point_f-r.q_abs)
                upper = point_f+r.q_abs
                conservative = np.maximum(g.cycle, point_f-r.q_late)
                assert r.path_coverage == bool(((g.end >= lower-1e-9) & (g.end <= upper+1e-9)).all())
                assert r.path_lower_coverage == bool((g.end >= conservative-1e-9).all())
                np.testing.assert_allclose(r.median_width, np.median(upper-lower), atol=1e-9)
                np.testing.assert_allclose(r.collapsed_fraction, np.mean(np.isclose(conservative, g.cycle, atol=1e-10)), atol=1e-10)
                band_checks += 1
    for file, rebuilt in [("point_summary.csv", p09.point_summary(events)), ("band_summary.csv", p09.band_summary(bands)), ("contrasts.csv", p09.contrasts(events))]:
        pd.testing.assert_frame_equal(pd.read_csv(out / file), rebuilt, check_dtype=False, atol=1e-9, rtol=1e-9)
    # Independently reproduce paired RMSE estimates and bootstrap intervals.
    rng = np.random.default_rng(p09.SEEDS[0])
    pairs = pd.read_csv(out / "contrasts.csv")
    assert len(pairs) == 60
    for r in pairs.itertuples():
        g = events.loc[events.subset.eq(r.subset) & events.dataset.eq(r.dataset) & events.repeat.eq(r.repeat) & events.event.eq(r.event) & events.status.eq("available")]
        matched = g.loc[g.method.eq(r.reference)].merge(g.loc[g.method.eq("RF_SLOPE")], on=["unit", "cycle"], suffixes=("_a", "_b"))
        assert len(matched) == r.common
        if not len(matched):
            continue
        ea, eb = matched.error_a.to_numpy(), matched.error_b.to_numpy()
        idx = rng.integers(0, len(ea), size=(2000, len(ea)))
        delta = np.sqrt(np.mean(eb[idx]**2, axis=1))-np.sqrt(np.mean(ea[idx]**2, axis=1))
        np.testing.assert_allclose([r.delta_rmse, r.ci_low, r.ci_high],
                                   [np.sqrt(np.mean(eb**2))-np.sqrt(np.mean(ea**2)), *np.quantile(delta, [.025, .975])], atol=1e-9)
    reserves = pd.read_csv(out / 'reserves.csv')
    assert len(reserves) == 38400
    # Independent reconstruction from saved per-cycle forecasts, without diagnostic helper.
    reserve_checks = 0
    for partition in splits:
        subset, repeat, fold = partition['subset'], partition['repeat'], partition['fold']
        tag = f'{subset}_r{repeat}_f{fold}'
        for dataset in ['complete']+(['truncated'] if fold == 1 else []):
            pred = pd.read_csv(out / f'predictions_{tag}_{dataset}.csv.gz')
            saved = reserves.loc[reserves.subset.eq(subset) & reserves.repeat.eq(repeat) & reserves.fold.eq(fold) & reserves.dataset.eq(dataset)]
            qs = quantiles.loc[quantiles.subset.eq(subset) & quantiles.repeat.eq(repeat) & quantiles.fold.eq(fold)]
            for r in saved.itertuples():
                g = pred.loc[pred.unit.eq(r.unit) & pred.method.eq(r.method) & pred.in_domain]
                if not len(g):
                    assert not r.available_path
                    continue
                q = qs.loc[qs.method.eq(r.method) & qs.scope.eq(r.scope) & np.isclose(qs.alpha, r.alpha)].iloc[0]
                flags = (g.cycle+g.predicted_rul-q.q_late-g.cycle) >= r.reserve+r.delay-1e-9
                assert bool(r.any_available) == bool(flags.any())
                np.testing.assert_allclose(r.cycle_fraction, flags.mean(), atol=1e-10)
                if r.available_point:
                    mark = g.loc[g.cycle.eq(g.crossing)].iloc[0]
                    assert bool(r.mark_available) == bool(mark.predicted_rul-q.q_late >= r.reserve+r.delay-1e-9)
                reserve_checks += 1
    pd.testing.assert_frame_equal(pd.read_csv(out / 'reserve_summary.csv'), p09.reserve_summary(reserves), check_dtype=False, atol=1e-9, rtol=1e-9)
    result = dict(reserve_rows_checked=reserve_checks, status="passed", prediction_rows_rebuilt=forecast_rows, maximum_prediction_difference=max_error,
                  score_rows_checked=len(scores), quantile_rows_checked=len(quantiles),
                  band_rows_checked=band_checks, paired_contrasts_checked=len(pairs),
                  prior_manifests_intact=p09.prior_integrity() == metadata["previous_manifests"],
                  verifier_sha256=p09.sha(p09.ROOT / "experiments/verify_pilot_f_uncertainty_10.py"))
    (out / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    p09.refresh_manifest()
    print(json.dumps(result))


if __name__ == "__main__":
    with threadpool_limits(limits=1):
        main()
