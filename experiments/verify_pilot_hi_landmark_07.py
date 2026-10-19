"""Verify P07 events, metrics, common-time comparisons and descriptive intervals."""

import json

import numpy as np
import pandas as pd

import pilot_hi_landmark_07 as p07


def main():
    out = p07.OUT
    meta = json.loads((out / "metadata.json").read_text(encoding="utf-8"))
    for name, digest in meta["inputs"].items():
        assert p07.sha(p07.ROOT / name) == digest, name
    assert p07.source_integrity() == meta["source_integrity"]
    for name, digest in json.loads((out / "manifest.json").read_text(encoding="utf-8")).items():
        assert p07.sha(out / name) == digest, name
    raw = p07.read_predictions()
    index = {key: g.sort_values("cycle").set_index("cycle") for key, g in
             raw.groupby(["domain", "dataset", "family", "unit"])}
    marks = pd.read_csv(out / "landmarks.csv")
    summary = pd.read_csv(out / "summary.csv")
    offsets = pd.read_csv(out / "offset_predictions.csv")
    offset_summary = pd.read_csv(out / "offset_summary.csv")
    history = pd.read_csv(out / "forecast_updates.csv")
    pairs = pd.read_csv(out / "paired_comparisons.csv")
    assert len(marks) == 5400 and len(summary) == 54 and len(pairs) == 144
    expected_updates = 0
    checked = 0
    for r in marks.itertuples():
        g = index[(r.domain, r.dataset, r.family, r.unit)]
        cycles = g.index[g.hi.le(r.alpha)]
        assert r.crossed == bool(len(cycles))
        if not len(cycles):
            assert np.isnan(r.crossing_cycle)
            assert r.status == ("not_reached_complete" if r.dataset == "complete" else "not_reached_before_truncation")
            continue
        t = int(cycles[0])
        point = g.loc[t]
        assert r.crossing_cycle == t
        np.testing.assert_allclose([r.actual_lead, r.error, r.predicted_f],
                                   [point.end-t, point.predicted_rul-point.actual_rul, t+point.predicted_rul], atol=1e-10)
        assert r.recovery == bool(g.loc[t:].hi.gt(r.alpha).any())
        expected_updates += len(g.loc[t:])
        checked += 1
    assert len(history) == expected_updates
    np.testing.assert_allclose(history.error, history.cycle+history.predicted_rul-history.end, atol=1e-10)
    assert (history.offset >= 0).all()
    for r in offsets.itertuples():
        point = index[(r.domain, r.dataset, r.family, r.unit)].loc[r.cycle]
        np.testing.assert_allclose(r.error, r.cycle+point.predicted_rul-point.end, atol=1e-10)
    for r in summary.itertuples():
        g = marks.loc[marks.domain.eq(r.domain) & marks.dataset.eq(r.dataset) & marks.family.eq(r.family) & marks.alpha.eq(r.alpha)]
        hits = g.loc[g.crossed]
        assert r.total == len(g) == 100 and r.crossed == len(hits)
        assert r.recovered_engines == int(hits.recovery.sum())
        np.testing.assert_allclose([r.rmse, r.mae, r.bias],
                                   [np.sqrt(np.mean(hits.error**2)), np.mean(abs(hits.error)), np.mean(hits.error)], atol=1e-10)
    for r in offset_summary.itertuples():
        g = offsets.loc[offsets.domain.eq(r.domain) & offsets.dataset.eq(r.dataset) & offsets.family.eq(r.family) & offsets.alpha.eq(r.alpha) & offsets.offset.eq(r.offset)]
        assert r.available == len(g)
        if len(g):
            np.testing.assert_allclose([r.rmse, r.initial_rmse_same_engines],
                                       [np.sqrt(np.mean(g.error**2)), np.sqrt(np.mean(g.initial_error**2))], atol=1e-10)
    rng = np.random.default_rng(20261016)
    for r in pairs.itertuples():
        domain, families = r.comparison.split(":")
        if "->" in domain:
            da, db = "FD003_transfer", "FD003_refit"
            fa = fb = families
        else:
            da = db = domain
            fa, fb = families.split("->")
        group = marks.loc[marks.dataset.eq(r.dataset) & marks.alpha.eq(r.alpha) & marks.crossed]
        a = group.loc[group.domain.eq(da) & group.family.eq(fa)].set_index("unit")
        b = group.loc[group.domain.eq(db) & group.family.eq(fb)].set_index("unit")
        units = a.index.intersection(b.index).sort_values()
        assert r.common == len(units)
        if not len(units):
            continue
        errors_a, errors_b = [], []
        for unit in units:
            ta, tb = int(a.loc[unit, "crossing_cycle"]), int(b.loc[unit, "crossing_cycle"])
            if r.timing == "common_cycle":
                ta = tb = max(ta, tb)
            for dest, dom, fam, cycle in [(errors_a, da, fa, ta), (errors_b, db, fb, tb)]:
                p = index[(dom, r.dataset, fam, unit)].loc[cycle]
                dest.append(cycle+p.predicted_rul-p.end)
        ea, eb = np.asarray(errors_a), np.asarray(errors_b)
        sample = rng.integers(0, len(units), size=(2000, len(units)))
        intervals = np.quantile(np.sqrt(np.mean(eb[sample]**2, axis=1))-np.sqrt(np.mean(ea[sample]**2, axis=1)), [.025, .975])
        np.testing.assert_allclose([r.rmse_a, r.rmse_b, r.ci_low, r.ci_high],
                                   [np.sqrt(np.mean(ea**2)), np.sqrt(np.mean(eb**2)), *intervals], atol=1e-10)
    result = {"status": "passed", "landmark_records": len(marks), "observed_landmarks": checked,
              "subsequent_forecasts": len(history), "paired_rows": len(pairs),
              "all_source_manifests_intact": True, "bootstrap_reproduced": True,
              "verifier_sha256": p07.sha(p07.ROOT / "experiments/verify_pilot_hi_landmark_07.py")}
    (out / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    manifest = {p.name: p07.sha(p) for p in sorted(out.iterdir()) if p.is_file() and p.name != "manifest.json"}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
