import unittest

import numpy as np
import pandas as pd

import pilot_hi_landmark_07 as p07


def trajectory(unit, hi, dataset="complete", family="MARGEM"):
    cycles = np.arange(20, 20+len(hi))
    return pd.DataFrame(dict(domain="FD001", dataset=dataset, family=family, unit=unit,
                             cycle=cycles, hi=hi, predicted_rul=10., end=50., actual_rul=50-cycles))


class LandmarkTests(unittest.TestCase):
    def test_first_crossing_recovery_and_unobserved_future(self):
        data = pd.concat([trajectory(1, [1., .5, .6, .4]),
                          trajectory(2, [.9, .8, .7], "truncated")])
        marks, history, snapshots = p07.extract_landmarks(data, [.5])
        hit = marks.loc[marks.unit.eq(1)].iloc[0]
        miss = marks.loc[marks.unit.eq(2)].iloc[0]
        self.assertEqual(hit.crossing_cycle, 21)
        self.assertEqual(hit.error, -19)
        self.assertEqual(hit.actual_lead, 29)
        self.assertEqual(hit.recovery_episodes, 1)
        self.assertEqual(hit.downward_recrossings, 1)
        self.assertFalse(miss.crossed)
        self.assertEqual(miss.status, "not_reached_before_truncation")
        self.assertEqual(len(history), 3)
        self.assertEqual(list(snapshots.offset), [0])
        self.assertTrue((history.initial_error == -19).all())

    def test_paired_intersection_and_common_time(self):
        a = pd.concat([trajectory(1, [.8, .4, .3]), trajectory(2, [.8, .4, .3])])
        b = pd.concat([trajectory(1, [.8, .7, .4], family="EMPIRICO"),
                       trajectory(2, [.8, .7, .6], family="EMPIRICO")])
        b["predicted_rul"] = 12.
        data = pd.concat([a, b])
        marks, _, _ = p07.extract_landmarks(data, [.5])
        aa, bb = marks.loc[marks.family.eq("MARGEM")], marks.loc[marks.family.eq("EMPIRICO")]
        row = p07.paired_record(aa, bb, "pair", .5, "complete", "common_cycle", data, np.random.default_rng(1))
        self.assertEqual(row["common"], 1)
        self.assertEqual(row["crossed_a"], 2)
        self.assertEqual(row["rmse_a"], 18)
        self.assertEqual(row["rmse_b"], 16)
        self.assertEqual(row["delta_rmse_b_minus_a"], -2)

    def test_crossing_does_not_depend_on_future_endpoint(self):
        data = trajectory(1, [1., .8, .4, .3])
        before, _, _ = p07.extract_landmarks(data, [.5])
        data["end"] += 100
        data["actual_rul"] += 100
        after, _, _ = p07.extract_landmarks(data, [.5])
        self.assertEqual(before.crossing_cycle.iloc[0], after.crossing_cycle.iloc[0])
        self.assertEqual(before.predicted_f.iloc[0], after.predicted_f.iloc[0])
        self.assertEqual(before.error.iloc[0]-100, after.error.iloc[0])


if __name__ == "__main__":
    unittest.main()
