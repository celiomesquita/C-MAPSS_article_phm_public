"""Check the pilot's temporal and engine-partition information boundaries."""

import unittest

import numpy as np

from pilot_fd001 import SENSORS, detector, features, read_data


class InformationBoundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_data().query("unit <= 4").copy()

    def test_future_values_do_not_change_past_inputs_or_alarm(self):
        original = self.data
        changed = original.copy()
        changed.loc[(changed.unit == 4) & (changed.cycle > 100), SENSORS] *= 100
        p0, sensors, z0 = detector(original, [1, 2, 3], 15, 2, 2)
        p1, sensors1, z1 = detector(changed, [1, 2, 3], 15, 2, 2)
        self.assertEqual(sensors, sensors1)
        prefix = (original.unit == 4) & (original.cycle <= 100)
        np.testing.assert_allclose(z0.loc[prefix], z1.loc[prefix], equal_nan=True)
        np.testing.assert_allclose(features(original, sensors).loc[prefix],
                                   features(changed, sensors).loc[prefix], equal_nan=True)
        self.assertEqual(p0.get(4) if p0.get(4, np.inf) <= 100 else None,
                         p1.get(4) if p1.get(4, np.inf) <= 100 else None)

    def test_evaluation_engines_do_not_fit_reference_dispersion(self):
        original = self.data
        changed = original.copy()
        changed.loc[changed.unit == 4, SENSORS] *= 100
        p0, sensors, z0 = detector(original, [1, 2, 3], 15, 2, 2)
        p1, sensors1, z1 = detector(changed, [1, 2, 3], 15, 2, 2)
        self.assertEqual(sensors, sensors1)
        train = original.unit <= 3
        np.testing.assert_allclose(z0.loc[train], z1.loc[train], equal_nan=True)
        for unit in [1, 2, 3]:
            self.assertEqual(p0.get(unit), p1.get(unit))


if __name__ == "__main__":
    unittest.main()
