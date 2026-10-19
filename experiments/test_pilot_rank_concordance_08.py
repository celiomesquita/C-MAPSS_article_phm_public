import unittest

import pandas as pd

import pilot_hi_trajectory_08 as p08


class CommonSensorRankTest(unittest.TestCase):
    def test_spearman_reranks_on_the_common_sensor_set(self):
        rows = []
        for method, scores in [("RF:SENSOR_FULL", {"s1": 4., "s2": 3., "s3": 2., "s4": 1.}),
                               ("Ridge:SENSOR_FULL", {"s1": 30., "s2": 20., "s4": 10.})]:
            for sensor, score in scores.items():
                rows.append(dict(subset="FD001", dataset="complete", run="fold1", method=method,
                                 representation="SENSOR_FULL", group=sensor, delta_mse=score))
        _, concordance = p08.importance_ranks(pd.DataFrame(rows))
        self.assertEqual(len(concordance), 1)
        self.assertEqual(concordance.groups.iloc[0], 3)
        self.assertAlmostEqual(concordance.spearman.iloc[0], 1.)


if __name__ == "__main__":
    unittest.main()
