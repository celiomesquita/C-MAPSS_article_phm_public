"""Information boundaries for P02 detector and local calibration."""

import unittest

import numpy as np
import pandas as pd

from pilot_fd001 import SENSORS, read_data
from pilot_fd001_02 import detector_score, margins, points_at


class P02Boundaries(unittest.TestCase):
    def test_detector_prefix_invariant_to_future_evaluation_values(self):
        data = read_data().query("unit <= 4").copy()
        altered = data.copy()
        altered.loc[(altered.unit == 4) & (altered.cycle > 100), SENSORS] *= 100
        a, sensors_a = detector_score(data, [1, 2, 3])
        b, sensors_b = detector_score(altered, [1, 2, 3])
        self.assertEqual(sensors_a, sensors_b)
        prefix = (data.unit == 4) & (data.cycle <= 100)
        np.testing.assert_allclose(a.loc[prefix], b.loc[prefix], equal_nan=True)
        p = points_at(data, a, 3.).get(4, np.inf)
        q = points_at(altered, b, 3.).get(4, np.inf)
        self.assertEqual(p if p <= 100 else None, q if q <= 100 else None)

    def test_local_band_is_defined_by_prediction_not_true_rul(self):
        cal = pd.DataFrame([{"unit": i, "raw": raw, "rul": rul}
                            for i in range(10) for raw, rul in [(20, 10), (40, 0)]])
        a = margins(cal)
        cal.loc[cal.raw == 40, "rul"] = -100
        b = margins(cal)
        self.assertEqual(a["local_margin"], b["local_margin"])
        self.assertNotEqual(a["global_margin"], b["global_margin"])
        self.assertEqual(a["local_engines"], 10)


if __name__ == "__main__":
    unittest.main()
