import unittest

import numpy as np
import pandas as pd

import pilot_hi_trajectory_08 as p08
from pilot_fd003_06 import load_models, read_inputs


class TrajectoryTests(unittest.TestCase):
    def test_local_polynomial_statistics(self):
        u = np.arange(20)-9.5
        stats = p08.rolling_statistics(4+3*u+2*u*u)
        self.assertAlmostEqual(stats["slope"][-1, 0], 3.)
        self.assertAlmostEqual(stats["curv"][-1, 0], 4.)
        self.assertTrue(np.isnan(stats["slope"][:19]).all())
        self.assertAlmostEqual(p08.rolling_statistics(np.ones(20))["std"][-1, 0], 0.)

    def test_features_causal_endpoint_independent_and_available_at_39(self):
        inputs = read_inputs("train", "FD001").query("unit in [1,2] and cycle <= 80").reset_index(drop=True)
        frozen = load_models(p08.source_folder("FD001") / "models_fold1.json")["EMPIRICO"]
        features, health, reps = p08.build_features(inputs, frozen)
        altered = inputs.copy()
        sensor_columns = [c for c in altered.columns if c.startswith("s")]
        altered.loc[altered.cycle.gt(60), sensor_columns] += 1000.
        altered["end"], altered["rul"] = 9999., -111.
        changed, _, _ = p08.build_features(altered, frozen)
        cols = sorted(set(sum(reps.values(), [])))
        np.testing.assert_allclose(features.loc[features.cycle.le(60), cols],
                                   changed.loc[changed.cycle.le(60), cols], atol=1e-10)
        prefix, _, _ = p08.build_features(inputs.loc[inputs.cycle.le(60)], frozen)
        np.testing.assert_allclose(features.loc[features.cycle.le(60), cols].to_numpy(), prefix[cols].to_numpy(), atol=1e-10)
        self.assertEqual(features.cycle.min(), 39)
        self.assertEqual(health.cycle.min(), 20)
        self.assertTrue({"unit", "cycle", "end", "rul"}.isdisjoint(cols))
        self.assertEqual(len(reps["HI_FULL"]), 4)
        self.assertEqual(len(reps["SENSOR_FULL"]), 6*len(reps["SENSOR_RAW"]))

    def test_event_before_window_is_not_postponed(self):
        inputs = pd.DataFrame({"unit": [1]*40, "cycle": np.arange(1, 41)})
        health = inputs.loc[inputs.cycle.ge(20)].copy()
        health["hi"] = np.where(health.cycle.ge(35), .4, 1.)
        grid = p08.event_grid(inputs, health, pd.Series({1: 100}), [1], "truncated").set_index("event")
        self.assertEqual(grid.loc["landmark", "cycle"], 35)
        self.assertEqual(grid.loc["landmark", "status"], "before_feature_availability")
        self.assertEqual(grid.loc["plus5", "status"], "available")
        self.assertEqual(grid.loc["plus10", "status"], "after_last_observation")

    def test_fit_uses_only_calibration_engines_and_scaler(self):
        rng = np.random.default_rng(1)
        units = np.repeat([1, 2, 3, 4], 60)
        cycles = np.tile(np.arange(39, 99), 4)
        frame = pd.DataFrame(dict(unit=units, cycle=cycles, end=100., rul=100.-cycles,
                                  hi=rng.uniform(size=len(units))))
        class Converter:
            def predict(self, values):
                return values*100
        partition = {"fit": [], "calibration": [1, 2], "selection": [3, 4]}
        records, rows, _ = p08.fit_converters(frame, partition, {"HI": ["hi"]}, {"converter": Converter()})
        self.assertEqual(records["Ridge:HI"]["fit_units"], [1, 2])
        weights = p08.p05.equal_engine_weights(frame.loc[frame.unit.isin([1, 2]), "unit"])
        expected = np.average(frame.loc[frame.unit.isin([1, 2]), "hi"], weights=weights)
        self.assertAlmostEqual(records["Ridge:HI"]["scaler"].mean_[0], expected)
        self.assertEqual(sum(r["chosen"] for r in rows), 2)


if __name__ == "__main__":
    unittest.main()
