import unittest

import numpy as np
import pandas as pd

import pilot_removal_11 as p11


def frame(leads, start=40):
    return pd.DataFrame(dict(unit=1, cycle=np.arange(start, start+len(leads)),
                             predicted_rul=leads, in_domain=True))


class RemovalDecisionTests(unittest.TestCase):
    def test_fixed_comparison_budget(self):
        rules = pd.DataFrame(p11.configurations())
        self.assertEqual(rules.phase.value_counts().to_dict(), dict(primary=16, sensitivity=8, control=2))
        self.assertEqual(rules.policy_id.nunique(), 26)

    def test_first_trigger_commits_date_despite_later_optimism(self):
        g = frame([20., 17., 100., 100.])
        r = p11.decide(g, 15, 2)
        self.assertEqual((r['decision'], r['scheduled']), (41, 43))
        self.assertFalse(r['initial_insufficient'])
        self.assertEqual(p11.decide(g.iloc[:2], 15, 2)['scheduled'], r['scheduled'])

    def test_insufficient_initial_lead_never_backdates_or_shortens_execution(self):
        r = p11.decide(frame([5., 4., 3.]), 15, 2)
        self.assertEqual((r['decision'], r['scheduled']), (40, 42))
        self.assertTrue(r['initial_insufficient'])
        self.assertEqual(r['trigger_shortfall'], 12.)

    def test_more_conservative_bound_cannot_delay_first_trigger(self):
        g = frame([30., 25., 20., 17., 12.])
        central = p11.decide(g, 15, 2)
        lower = p11.decide(g, 15, 2, 10.)
        self.assertLessEqual(lower['scheduled'], central['scheduled'])
        self.assertEqual(p11.decide(frame([17.+1e-12]), 15, 2)['decision'], 40)

    def test_future_labels_do_not_enter_decision(self):
        g = frame([20., 18., 16., 12.])
        a = p11.decide(g, 15, 2)
        g['end'], g['rul'] = -1000., 10000.
        np.testing.assert_equal(p11.decide(g, 15, 2), a)
        g.loc[g.cycle.gt(a['decision']), 'predicted_rul'] = 9999.
        np.testing.assert_equal(p11.decide(g, 15, 2), a)

    def test_exact_endpoint_overrun_and_no_decision_are_distinct(self):
        action = p11.decide(frame([17.]), 15, 2)
        exact = p11.assess(action, 42, 42, True)
        late = p11.assess(action, 41, 41, True)
        self.assertTrue(exact['exact_endpoint'])
        self.assertFalse(exact['late'])
        self.assertTrue(late['late'])
        self.assertEqual(late['utilised'], 41.)
        missing = p11.assess(p11.decide(frame([30.]), 15, 2), 42, 42, True)
        self.assertEqual(missing['status'], 'endpoint_without_decision')
        self.assertTrue(missing['reached_endpoint'])
        self.assertFalse(missing['late'])

    def test_truncation_is_censoring_not_full_life_or_failure(self):
        result = p11.assess(p11.decide(frame([30., 25.]), 15, 2), 100, 41, False)
        self.assertEqual(result['status'], 'right_censored')
        self.assertTrue(np.isnan(result['utilised']))
        self.assertTrue(np.isnan(result['reached_endpoint']))
        action = p11.decide(frame([17.]), 15, 2)
        result = p11.assess(action, 100, 40, False)
        self.assertTrue(result['has_decision'])
        self.assertFalse(result['execution_observed'])

    def test_age_control_uses_only_development_endpoints(self):
        endpoints = pd.Series({1: 160, 2: 150, 3: 10, 4: 900})
        age = p11.fixed_age(endpoints, [1, 2])
        endpoints.loc[[3, 4]] = [1, 10000]
        self.assertEqual(age, 149)
        self.assertEqual(p11.fixed_age(endpoints, [1, 2]), age)


if __name__ == '__main__':
    unittest.main()
