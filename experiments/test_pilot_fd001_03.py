"""Causality and endpoint isolation for the P03 empirical proxy."""

import unittest

import numpy as np

from pilot_fd001 import SENSORS, read_data
from pilot_fd001_03 import fit_hi_reference, sensor_score, transform_hi


class P03Boundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_data().query("unit <= 4").copy()

    def test_future_evaluation_sensor_values_do_not_change_past_scores_or_hi(self):
        changed = self.data.copy()
        changed.loc[(changed.unit == 4) & (changed.cycle > 100), SENSORS] *= 100
        score, sensors = sensor_score(self.data, [1,2,3], 10, 5)
        altered, _ = sensor_score(changed, [1,2,3], 10, 5)
        prefix = (changed.unit == 4) & (changed.cycle <= 100)
        np.testing.assert_allclose(score.loc[prefix], altered.loc[prefix], equal_nan=True)
        ref = fit_hi_reference(self.data, [1,2,3], sensors, .9)
        original_hi = transform_hi(self.data, ref)
        altered_hi = transform_hi(changed, ref)
        np.testing.assert_allclose(original_hi.loc[prefix], altered_hi.loc[prefix], equal_nan=True)

    def test_evaluation_endpoint_does_not_calibrate_reference_or_transform(self):
        _, sensors = sensor_score(self.data, [1,2,3], 15, 3)
        original = fit_hi_reference(self.data, [1,2,3], sensors, .5)
        changed = self.data.copy()
        changed.loc[changed.unit == 4, "end"] += 100
        altered = fit_hi_reference(changed, [1,2,3], sensors, .5)
        np.testing.assert_allclose(original[["direction","scale"]], altered[["direction","scale"]])
        np.testing.assert_allclose(transform_hi(self.data, original), transform_hi(changed, altered), equal_nan=True)

    def test_initial_hi_is_one_without_reference_to_detected_P(self):
        _, sensors = sensor_score(self.data, [1,2,3], 15, 3)
        ref = fit_hi_reference(self.data, [1,2,3], sensors, .9)
        hi = transform_hi(self.data, ref)
        np.testing.assert_allclose(hi.loc[self.data.cycle == 20], 1.)
        self.assertTrue(hi.loc[self.data.cycle < 20].isna().all())


if __name__ == "__main__":
    unittest.main()
