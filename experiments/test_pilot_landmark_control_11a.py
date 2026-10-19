import unittest

import numpy as np
import pandas as pd

import pilot_landmark_control_11a as p


class MarkerControlTests(unittest.TestCase):
    def test_first_usable_event_and_execution_delay(self):
        frame = pd.DataFrame(dict(cycle=[39, 40, 41, 42], in_domain=[False, False, True, True]))
        action = p.marker_action(frame, 2)
        self.assertEqual((action['decision'], action['scheduled']), (41, 43))

    def test_forecasts_labels_and_future_do_not_change_action(self):
        frame = pd.DataFrame(dict(cycle=[39, 40, 41], in_domain=[False, True, True],
                                  predicted_rul=[999., 999., 999.], end=-10., rul=-100.))
        action = p.marker_action(frame, 1)
        frame['predicted_rul'], frame['end'], frame['rul'] = 0., 99999., 12345.
        np.testing.assert_equal(action, p.marker_action(frame, 1))
        np.testing.assert_equal(action, p.marker_action(frame.iloc[:2], 1))

    def test_equal_warmup_and_memory_of_earlier_event(self):
        frame = pd.DataFrame(dict(cycle=[37, 38, 39, 40], in_domain=True))
        self.assertEqual(p.marker_action(frame, 2)['decision'], 39)
        # A later recovery of HI does not erase a previously observed crossing.
        frame['hi'] = [.4, .4, .7, .8]
        self.assertEqual(p.marker_action(frame, 2)['scheduled'], 41)

    def test_no_observed_marker_or_no_usable_features_has_no_action(self):
        frame = pd.DataFrame(dict(cycle=[39, 40], in_domain=False))
        self.assertTrue(np.isnan(p.marker_action(frame, 1)['decision']))
        self.assertTrue(np.isnan(p.marker_action(frame.iloc[:0], 1)['decision']))
        early = pd.DataFrame(dict(cycle=[20, 21], in_domain=True))
        self.assertTrue(np.isnan(p.marker_action(early, 1)['decision']))

    def test_lifetime_decomposition_and_cost_factors_are_not_added_percentages(self):
        old = pd.DataFrame([dict(subset='FD001', repeat=1, dataset='complete', delay=1,
                                 policy_id=policy, method=method, utilised=value)
                            for policy, method, value in [('ISO', 'ISO', 150.), ('AGE_D1', 'AGE', 100.)]])
        control = pd.DataFrame([dict(subset='FD001', repeat=1, dataset='complete', delay=1,
                                     policy_id='HI_MARKER_D1', utilised=120.)])
        r = p.decomposition(old, control).iloc[0]
        self.assertEqual(r.total_life_gain, 50.)
        self.assertEqual(r.marker_life_gain, 20.)
        self.assertEqual(r.prognosis_life_gain, 30.)
        self.assertAlmostEqual(r.prognosis_share, .6)
        self.assertAlmostEqual(r.cost_ratio_total, r.cost_ratio_marker*r.cost_ratio_incremental)
        self.assertNotAlmostEqual(1-r.cost_ratio_total, (1-r.cost_ratio_marker)+(1-r.cost_ratio_incremental))

    def test_missing_candidate_stays_in_pair_and_is_not_a_safety_gain(self):
        a = pd.DataFrame(dict(unit=[1, 2], fold=1, utilised=[150., 200.], has_decision=[True, False],
                              scheduled=[150., np.nan], reached_endpoint=[False, True]))
        b = pd.DataFrame(dict(unit=[1, 2], fold=1, utilised=[120., 120.], has_decision=True,
                              scheduled=[120., 120.], reached_endpoint=False))
        r = p.compare_pairs(a, b, np.random.default_rng(1))
        self.assertEqual(r['common'], 2)
        self.assertEqual(r['candidate_without_decision'], 1)
        self.assertEqual(r['candidate_reached'], 1)
        self.assertEqual(r['later_date'], 1)


if __name__ == '__main__':
    unittest.main()
