"""Information boundaries and zero invariance for the empirical HI."""

import unittest

import numpy as np
import pandas as pd

from pilot_fd001 import SENSORS, read_data
from pilot_fd001_04 import choose_quantile, fit_reference, transform_hi


class P04Boundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = read_data().query("unit <= 4").copy()

    def test_endpoint_and_future_values_are_not_inputs(self):
        ref = fit_reference(self.data, [1, 2, 3], .9)
        changed = self.data.copy()
        changed.loc[changed.unit == 4, "end"] += 100
        changed.loc[(changed.unit == 4) & (changed.cycle > 100), SENSORS] *= 100
        new_ref = fit_reference(changed, [1, 2, 3], .9)
        pd.testing.assert_frame_equal(ref, new_ref)
        h, _ = transform_hi(self.data, ref)
        h_new, _ = transform_hi(changed, new_ref)
        prefix = (self.data.unit == 4) & (self.data.cycle <= 100)
        np.testing.assert_allclose(h.loc[prefix], h_new.loc[prefix], equal_nan=True)

    def test_deadband_changes_plateau_but_not_zero(self):
        ref = fit_reference(self.data, [1, 2, 3], .9)
        h0, _ = transform_hi(self.data, ref, 0)
        h2, _ = transform_hi(self.data, ref, 2)
        h3, _ = transform_hi(self.data, ref, 3)
        np.testing.assert_array_equal(h0 <= 0, h2 <= 0)
        np.testing.assert_array_equal(h0 <= 0, h3 <= 0)
        valid = h0.notna()
        self.assertTrue((h2.loc[valid] >= h0.loc[valid]-1e-12).all())
        self.assertTrue((h3.loc[valid] >= h2.loc[valid]-1e-12).all())
        np.testing.assert_allclose(h2.loc[self.data.cycle == 20], 1)
        self.assertTrue(h2.loc[self.data.cycle < 20].isna().all())

    def test_selection_uses_only_provided_internal_metrics(self):
        metrics = pd.DataFrame({"quantile": [.5, .5, .9, .9],
                                "crossed": [True, True, False, True],
                                "normalised_lead": [.2, .2, np.nan, .05]})
        self.assertEqual(choose_quantile(metrics, 1)[0], .5)
        self.assertEqual(choose_quantile(metrics, .25)[0], .9)


if __name__ == "__main__":
    unittest.main()
