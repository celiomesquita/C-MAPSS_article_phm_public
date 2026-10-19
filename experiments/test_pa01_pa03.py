"""Regression checks for the PA01--PA03 editorial closure; no fitted model is changed."""
import unittest

import numpy as np
import pandas as pd

import coefficient_stability_19b as stability
import explainability_core_13b as core
import inspection_arm_17b as inspection
import pilot_explainability_13b as replay
from test_inspection_arm_17b import brute


class ContributionConventionTests(unittest.TestCase):
    def test_published_equation_matches_base_contributions(self):
        raw = np.random.default_rng(20261019).normal(size=(160, 21)).cumsum(axis=0)
        health = dict(stats=dict(channels=['s2', 's7', 's11'],
                                direction=np.array([-1., 1., -1.]),
                                scale=np.array([.07, 2., 300.])),
                      beta=np.array([.3, 0., 1.7]))
        contributions, channels, weights = core.base_contributions(raw, health)
        means = pd.DataFrame(raw).rolling(15, min_periods=15).mean().to_numpy()
        departure = means[19:, channels] - means[19, channels]
        normalised = departure * health['stats']['direction'] / health['stats']['scale']
        published = normalised * health['beta']
        np.testing.assert_allclose(contributions[19:, channels], published, atol=1e-12)
        np.testing.assert_allclose(published, departure * weights, atol=1e-12)
        total = published.sum(axis=1)
        expected = np.clip(1. - np.maximum(total, 0.), 0., 1.)
        actual, radial, _ = core.bounded_contributions(contributions[19:])
        np.testing.assert_allclose(actual, expected, atol=1e-12)
        np.testing.assert_allclose(radial.sum(axis=1), 1. - actual, atol=1e-12)
        np.testing.assert_array_equal(contributions[19], np.zeros(21))

    def test_rectification_clipping_and_signed_cancellation(self):
        signed = np.array([[-2., 1.], [2., -1.5], [2., 1.], [0., 0.]])
        health, radial, total = core.bounded_contributions(signed)
        np.testing.assert_allclose(health, [1., .5, 0., 1.])
        np.testing.assert_allclose(total, [-1., .5, 3., 0.])
        self.assertLess(radial[1, 1], 0.)
        np.testing.assert_allclose(radial.sum(axis=1), 1. - health)

    def test_stability_uses_beta_not_raw_deviation_weights(self):
        bundle = dict(health=dict(stats=dict(channels=['s1', 's2', 's3'],
                                            direction=np.array([-1., 1., -1.]),
                                            scale=np.array([100., .001, 2.])),
                                 beta=np.array([.9, .3, .6])))
        record = stability.fold_record(bundle)
        self.assertEqual(record, {'s1': (-1., .9), 's2': (1., .3), 's3': (-1., .6)})
        altered = dict(health=dict(bundle['health']))
        altered['health']['stats'] = dict(bundle['health']['stats'], scale=np.ones(3))
        self.assertEqual(record, stability.fold_record(altered))


class PrefixBoundaryTests(unittest.TestCase):
    def test_joint_and_channel_limits_are_inclusive(self):
        noise = dict(active=np.array([0, 1]), nu=np.ones(2), centre=np.zeros(21),
                     precision=np.eye(2), md_limit=1., channel_limits=np.ones(2))
        raw = np.zeros((3, 21))
        raw[1:, 0] = 1.
        outside = core.support(raw, np.arange(1, 4), np.zeros((1, 21)), noise)
        np.testing.assert_array_equal(outside, [[False, False]])
        noise['channel_limits'][0] = .99
        self.assertTrue(core.support(raw, np.arange(1, 4), np.zeros((1, 21)), noise)[0, 0])
        noise['channel_limits'][:] = 10.
        noise['md_limit'] = .99
        self.assertTrue(core.support(raw, np.arange(1, 4), np.zeros((1, 21)), noise)[0, 0])

    def test_destination_six_through_decision_inclusive(self):
        outside = np.zeros((1, 78), dtype=bool)
        for destination, included in [(5, False), (6, True), (58, True), (59, False)]:
            outside[:] = False
            outside[0, destination - 2] = True
            self.assertEqual(bool(replay.prefix_support(outside, 58)[0]), not included)

    def test_original_and_perturbed_prefix_both_required(self):
        cycles = np.arange(20, 80)
        paths = np.ones((2, len(cycles)))
        forecasts = paths * 100.
        variants = pd.DataFrame([dict(variant=variant, kind='channel', direction='s1',
                                      sensor='s1', epsilon=1., sign=1) for variant in (0, 1)])
        rows = pd.DataFrame([dict(method='AGE', selected_value=0., delay=2, reserve=15,
                                 q_late=0., control_age=60, endpoint=80, policy_id='age',
                                 decision=58., scheduled=60., has_decision=True,
                                 reached_endpoint=False, selection_feasible=np.nan)])
        for offending in (0, 1):
            outside = np.zeros((2, 78), dtype=bool)
            outside[offending, 4] = True
            result = replay.policy_records(rows, {}, paths, cycles, forecasts, forecasts,
                                           variants, outside, 'global')
            self.assertFalse(result[1]['within_support'])


class MonitoringTransitionTests(unittest.TestCase):
    def action(self, crossing, forecast=0.):
        cycles = np.arange(20, 180)
        paths = np.ones((1, len(cycles)))
        if crossing is not None:
            paths[0, crossing - 20] = .4
        forecasts = np.full_like(paths, forecast)
        rows = pd.DataFrame([dict(method='ISO', selected_value=0., delay=2, reserve=15,
                                 q_late=0., control_age=127, endpoint=180, policy_id='iso')])
        return core.actions(rows, cycles, paths, forecasts, forecasts)[0]

    def test_valid_monitoring_without_landmark_does_not_trigger(self):
        action = self.action(None)
        self.assertTrue(action['missing'][0])
        self.assertTrue(np.isnan(action['first_available'][0]))
        result = inspection.hybrid_expectation(180, False, np.nan, 2, 0., 'S2', 60, 1., 0., 0.)
        self.assertEqual(result['util'], 180.)
        self.assertEqual(result['missing'], 1.)
        self.assertGreater(result['inspections'], 0.)

    def test_post_gate_landmark_and_memory_after_hi_recovery(self):
        for crossing, decision in [(20, 39), (39, 39), (128, 128), (150, 150)]:
            action = self.action(crossing)
            self.assertEqual(action['decision'][0], decision)
            self.assertEqual(action['scheduled'][0], decision + 2)

    def test_active_prognosis_can_have_no_decision(self):
        action = self.action(100, forecast=100.)
        self.assertEqual(action['first_available'][0], 100.)
        self.assertTrue(action['missing'][0])

    def test_rejection_precedes_a_later_prognostic_decision(self):
        result = inspection.hybrid_expectation(200, True, 150, 2, 0., 'S2', 60, 1., 1., 1.)
        self.assertEqual(result['util'], 129.)
        self.assertEqual(result['rejection'], 1.)
        self.assertEqual(result['inspections'], 1.)

    def test_gate_loss_removes_at_127_without_inspection(self):
        for delay in (1, 2):
            result = inspection.hybrid_expectation(200, False, np.nan, delay, 1., 'S2', 60, 1., 1., 1.)
            self.assertEqual(result['util'], 127.)
            self.assertEqual(result['inspections'], 0.)
            self.assertEqual(result['rejection'], 0.)

    def test_first_inspection_127_not_age_gate(self):
        for delay in (1, 2):
            result = inspection.hybrid_expectation(200, False, np.nan, delay, 0., 'S2', 60, 1., 1., 1.)
            self.assertEqual(result['util'], 127. + delay)
            self.assertEqual(result['inspections'], 1.)
            self.assertEqual(result['rejection'], 1.)
        self.assertEqual(inspection.inspection_times(127, 'S2', 60).tolist(), [])
        self.assertEqual(inspection.inspection_times(132, 'S2', 60).tolist(), [127])
        self.assertEqual(inspection.inspection_times(133, 'S2', 60).tolist(), [127, 132])

    def test_phm_precedes_inspection_at_same_cycle(self):
        for delay in (1, 2):
            for decision in (127, 132):
                result = inspection.hybrid_expectation(200, True, decision, delay, 0., 'S2', 60, 1., 0., 0.)
                self.assertEqual(result['util'], decision + delay)
                self.assertEqual(result['inspections'], float(decision == 132))
                self.assertEqual(result['rejection'], 0.)
            result = inspection.hybrid_expectation(200, True, 127, delay, .25, 'S2', 60, 1., 1., 1.)
            self.assertEqual(result['inspections'], 0.)
            self.assertEqual(result['rejection'], 0.)

    def test_gate_edges_and_precedences_against_scalar_enumeration(self):
        for delay in (1, 2):
            gate = 127 - delay
            for decision in (gate - 1, gate, gate + 1, 127, 132, None):
                for invalidity in (0., .25, 1.):
                    for rejection in (0., 1.):
                        arguments = (200, decision is not None, decision if decision is not None else np.nan,
                                     delay, invalidity, 'S2', 60, 1., rejection, rejection)
                        actual = inspection.hybrid_expectation(*arguments)
                        expected = brute(*arguments)
                        for metric in actual:
                            self.assertAlmostEqual(actual[metric], expected[metric], places=11,
                                                   msg=(arguments, metric))


if __name__ == '__main__':
    unittest.main()
