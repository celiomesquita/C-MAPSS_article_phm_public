import unittest
import numpy as np
import pandas as pd
import pilot_policy_selection_13a as p


class PolicySelectionTests(unittest.TestCase):
    def test_disjoint_internal_training_and_validation(self):
        s = dict(fit=list(range(1, 26)), converter=list(range(26, 41)), seed=20261017, fold=1)
        parts = p.inner_partitions(s)
        self.assertEqual(parts, p.inner_partitions(s))
        self.assertEqual(sorted(x for v in parts for x in v['validation']), list(range(1, 41)))
        for v in parts:
            self.assertEqual([len(v[k]) for k in ['fit', 'unused', 'validation']], [25, 5, 10])
            self.assertEqual(len(set(v['fit']+v['unused']+v['validation'])), 40)

    def test_memory_and_wait_do_not_commit_future_decision(self):
        g = pd.DataFrame(dict(cycle=[20, 38, 39, 40], hi=[.4, .8, .8, .8]))
        self.assertEqual(p.condition_action(g, 'threshold', .5, 2)['scheduled'], 41)
        self.assertTrue(np.isnan(p.condition_action(g, 'wait', 2, 1)['decision']))
        g.loc[len(g)] = [41, .9]
        self.assertEqual(p.condition_action(g, 'wait', 2, 1)['scheduled'], 42)

    def test_future_and_labels_do_not_change_committed_action(self):
        g = pd.DataFrame(dict(cycle=[39, 40, 41], hi=[.6, .4, .2], end=[1, 1, 1]))
        a = p.condition_action(g, 'threshold', .5, 1)
        g['end'] = 99999
        np.testing.assert_equal(a, p.condition_action(g.iloc[:2], 'threshold', .5, 1))

    def metrics(self):
        return pd.DataFrame([dict(family='threshold', delay=1, value=h, total=40, decisions=40,
                                  events=e, mean_utilised=n) for h, e, n in [(.2, 1, 200), (.5, 0, 180), (.6, 0, 180)]])

    def test_risk_filter_and_prudent_threshold_tie(self):
        r = p.select_rules(self.metrics()).iloc[0]
        self.assertTrue(r.selection_feasible)
        self.assertEqual(r.selected_value, .6)
        self.assertEqual(r.feasible_candidates, 2)

    def test_shorter_wait_tie(self):
        g = self.metrics().iloc[1:].copy()
        g['family'], g['value'] = 'wait', [2, 5]
        self.assertEqual(p.select_rules(g).iloc[0].selected_value, 2)

    def test_no_feasible_candidate_is_explicit(self):
        g = self.metrics()
        g['events'] = [2, 1, 1]
        r = p.select_rules(g).iloc[0]
        self.assertFalse(r.selection_feasible)
        self.assertEqual(r.internal_events, 1)
        self.assertEqual(r.selected_value, .6)


if __name__ == '__main__':
    unittest.main()
