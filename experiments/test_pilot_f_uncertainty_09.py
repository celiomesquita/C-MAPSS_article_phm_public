import unittest

import numpy as np
import pandas as pd

import pilot_f_uncertainty_09 as p09


class EndpointUncertaintyTests(unittest.TestCase):
    def test_new_partitions_are_disjoint_and_cover_each_engine(self):
        previous = None
        for seed in p09.SEEDS:
            folds = p09.partitions(seed)
            self.assertEqual(sorted(sum([f["evaluation"] for f in folds], [])), list(range(1, 101)))
            for fold in folds:
                groups = [set(fold[k]) for k in ["fit", "converter", "uncertainty", "evaluation"]]
                self.assertEqual([len(g) for g in groups], [40, 20, 20, 20])
                self.assertEqual(len(set.union(*groups)), 100)
            if previous is not None:
                self.assertNotEqual(folds[0]["evaluation"], previous)
            previous = folds[0]["evaluation"]

    def test_corrected_quantile_preserves_insufficient_sample_infinity(self):
        q, n, k = p09.corrected_quantile(np.arange(1, 21), .1)
        self.assertEqual((q, n, k), (19., 20, 19))
        self.assertEqual(p09.corrected_quantile(np.arange(1, 21), .05), (20., 20, 20))
        self.assertTrue(np.isinf(p09.corrected_quantile(np.arange(18), .05)[0]))
        self.assertTrue(np.isinf(p09.corrected_quantile([], .1)[0]))
        self.assertEqual(p09.corrected_quantile(np.arange(1, 20), .05)[0], 19.)

    def test_point_and_simultaneous_coverage_differ(self):
        inputs = pd.DataFrame(dict(unit=1, cycle=np.arange(1, 44)))
        health = inputs.loc[inputs.cycle.ge(20)].copy()
        health["hi"] = np.where(health.cycle.ge(40), .4, 1.)
        predictions = []
        for method in p09.METHODS:
            frame = pd.DataFrame(dict(unit=1, cycle=np.arange(39, 44), method=method,
                                      hi=[1., .4, .4, .4, .4], crossing=40., in_domain=[False, True, True, True, True],
                                      end=50., rul=[11., 10., 9., 8., 7.], error=[0., 1., 2., 6., 3.]))
            frame["predicted_rul"] = frame.rul+frame.error
            predictions.append(frame)
        predictions = pd.concat(predictions, ignore_index=True)
        scores, events = p09.score_engines(predictions, health, inputs, pd.Series({1: 50}), [1])
        self.assertTrue((scores.point_abs == 1.).all())
        self.assertTrue((scores.path_abs == 6.).all())
        quantiles = pd.DataFrame([dict(method=m, scope=s, alpha=.1, n=20, k=19,
                                       q_abs=q, q_late=q) for m in p09.METHODS for s, q in [("point", 1.), ("path", 6.)]])
        bands = p09.evaluate_bands(predictions, scores, events, quantiles)
        self.assertTrue(bands.loc[bands.scope.eq("point"), "point_coverage"].all())
        self.assertFalse(bands.loc[bands.scope.eq("point"), "path_coverage"].any())
        self.assertTrue(bands.loc[bands.scope.eq("path"), "path_coverage"].all())

    def test_refitted_health_uses_only_fit_engines_and_predictions_are_causal(self):
        inputs = p09.read_inputs("train", "FD001")
        fit = inputs.loc[inputs.unit.isin([1, 2, 3, 4])].copy()
        converter = inputs.loc[inputs.unit.isin([5, 6])].copy()
        bundle = p09.fit_pipeline(fit, converter, "FD001", p09.SEEDS[0])
        self.assertEqual(bundle["health"]["fit_units"], [1, 2, 3, 4])
        for record in bundle["predictors"].values():
            self.assertEqual(record["fit_units"], [5, 6])
        evaluation = inputs.loc[inputs.unit.eq(7) & inputs.cycle.le(85)].copy()
        predictions, _ = p09.predict_inputs(bundle, evaluation)
        altered = evaluation.copy()
        altered.loc[altered.cycle.gt(60), [f"s{i}" for i in range(1, 22)]] += 1000.
        altered["end"], altered["rul"] = -999., 12345.
        changed, _ = p09.predict_inputs(bundle, altered)
        np.testing.assert_allclose(predictions.loc[predictions.cycle.le(60), "predicted_rul"],
                                   changed.loc[changed.cycle.le(60), "predicted_rul"], atol=1e-9)
        prefix, _ = p09.predict_inputs(bundle, evaluation.loc[evaluation.cycle.le(60)])
        np.testing.assert_allclose(predictions.loc[predictions.cycle.le(60), "predicted_rul"], prefix.predicted_rul, atol=1e-9)
        contaminated = fit.assign(end=-1., rul=123456.)
        other = p09.fit_health(contaminated, "FD001")
        np.testing.assert_array_equal(other["beta"], bundle["health"]["beta"])


if __name__ == "__main__":
    unittest.main()
