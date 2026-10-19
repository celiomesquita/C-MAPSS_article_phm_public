"""P05 tests protect RUL alignment and prospective information boundaries."""

import unittest

import numpy as np
import pandas as pd
from sklearn.isotonic import IsotonicRegression

from pilot_fd001 import SENSORS, read_data
from pilot_fd001_04 import centred_sensors
from pilot_fd001_05 import (aakr_hi, attach_official_labels, empirical_hi, fit_aakr,
                            fitting_stats, reconstruct, standardise, transform_selected)


class P05Boundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_data().query("unit <= 4").copy()

    def test_labels_belong_to_last_test_cycle(self):
        observations = pd.DataFrame({"unit": [1,1,2,2], "cycle": [30,31,49,50]})
        labelled = attach_official_labels(observations, [112,20])
        np.testing.assert_array_equal(labelled.end, [143,143,70,70])
        np.testing.assert_array_equal(labelled.rul, [113,112,21,20])
        with self.assertRaises(ValueError):
            attach_official_labels(observations, [112])

    def test_endpoint_labels_and_future_values_do_not_enter_hi_or_prediction(self):
        centred = centred_sensors(self.data)
        stats = fitting_stats(self.data, [1,2,3], centred)
        model = np.ones(len(stats["channels"]))/len(stats["channels"])
        converter = IsotonicRegression(out_of_bounds="clip").fit([0.,1.], [0.,150.])
        chosen = {"stats": stats, "model": model, "converter": converter}
        changed = self.data.copy()
        changed.loc[changed.unit == 4, ["end","rul"]] += 1000
        changed.loc[(changed.unit == 4) & (changed.cycle > 100), SENSORS] *= 100
        first = transform_selected(self.data, chosen, "EMPIRICO")
        altered = transform_selected(changed, chosen, "EMPIRICO")
        mask = (first.unit == 4) & (first.cycle <= 100)
        pd.testing.assert_frame_equal(first.loc[mask], altered.loc[mask])
        revised_stats = fitting_stats(changed, [1,2,3], centred_sensors(changed))
        np.testing.assert_allclose(stats["scale"], revised_stats["scale"])
        np.testing.assert_allclose(stats["direction"], revised_stats["direction"])

    def test_terminal_anchor_excludes_query_engine_reference_patterns(self):
        centred = centred_sensors(self.data)
        stats = fitting_stats(self.data, [1,2,3], centred)
        z = standardise(centred, stats)
        original = fit_aakr(self.data, z, [1,2,3], list(range(5)), 5, 2.)
        altered_z = z.copy()
        mask = (self.data.unit == 1) & (self.data.cycle > self.data.end-5) & (self.data.cycle < self.data.end)
        altered_z[np.asarray(mask)] += 50
        revised = fit_aakr(self.data, altered_z, [1,2,3], list(range(5)), 5, 2.)
        self.assertAlmostEqual(original["loo_terminal_residuals"][0], revised["loo_terminal_residuals"][0])

    def test_kernel_remains_finite_far_from_reference(self):
        bank = np.array([[0.,0.], [1.,1.]])
        query = np.array([[1e6,1e6]])
        prediction = reconstruct(query, bank, .5, np.ones(2))
        self.assertTrue(np.isfinite(prediction).all())
        np.testing.assert_allclose(prediction, [[1.,1.]])

    def test_empirical_hi_has_initial_reference_and_sensor_direction(self):
        z = np.array([[0.,0.], [1.,2.], [3.,3.]])
        hi = empirical_hi(z, np.array([.2,.1]))
        np.testing.assert_allclose(hi, [1.,.6,.1])


if __name__ == "__main__":
    unittest.main()
