import unittest

import numpy as np
import pandas as pd

import break_even_21a as m


def arm(util, late=0., exact=0., missing=0.):
    util = np.asarray(util, float)
    z = np.zeros(len(util))
    return dict(util=util, late=z+late, exact=z+exact, missing=z+missing)


class BreakEvenTests(unittest.TestCase):
    def test_classification_covers_nine_sign_combinations(self):
        tol = 1e-9
        table = {(-1, 1): 1, (-1, 0): 1, (0, 1): 1, (0, 0): 0, (1, -1): 2, (1, 0): 2, (0, -1): 2, (1, 1): 3, (-1, -1): 4}
        for (sw, se), expected in table.items():
            self.assertEqual(int(m.classify(sw*1e-3, se*1e-3, tol)), expected, (sw, se))

    def test_known_break_even(self):
        # A: 10 lives of 80 cycles, no events. B: 10 lives of 100 cycles, 0.5 events per life.
        A, B = arm([80.]*10), arm([100.]*10, missing=.5)
        wA, wB = 10/800, 10/1000
        eA, eB = 0., 5/1000
        dW, dE = wA-wB, eB-eA
        self.assertAlmostEqual(dW/dE, .5)
        tol = 1e-9*wB
        self.assertEqual(int(m.classify(dW, dE, tol)), 3)
        self.assertEqual(int(m.prefer(dW, dE, .25, tol)), -1)        # below break-even B (fewer restorations) is cheaper
        self.assertEqual(int(m.prefer(dW, dE, .5, tol)), 0)
        self.assertEqual(int(m.prefer(dW, dE, 1., tol)), 1)

    def test_dominance_and_no_events_avoided(self):
        tol = 1e-12
        self.assertEqual(int(m.classify(-.001, 0., tol)), 1)         # fewer restorations, equal events: A dominates
        self.assertEqual(int(m.classify(.001, 0., tol)), 2)          # A only costs: B dominates, beta0 undefined
        self.assertEqual(int(m.classify(.0, .0, tol)), 0)

    def test_reverse_tradeoff_has_threshold_below(self):
        tol = 1e-12
        dW, dE = -.002, -.004                                        # A restores less but has more events
        self.assertEqual(int(m.classify(dW, dE, tol)), 4)
        self.assertAlmostEqual(dW/dE, .5)
        self.assertEqual(int(m.prefer(dW, dE, .25, tol)), 1)
        self.assertEqual(int(m.prefer(dW, dE, 1., tol)), -1)

    def test_age_arm(self):
        a = m.age_arm([100, 127, 128, 300])
        self.assertEqual(a["util"].tolist(), [100, 127, 127, 127])
        self.assertEqual(a["late"].tolist(), [1, 0, 0, 0])
        self.assertEqual(a["exact"].tolist(), [0, 1, 0, 0])

    def test_bootstrap_counts_are_valid_multinomial(self):
        c = m.bootstrap_counts(25, [m.SEED, 3])
        self.assertEqual(c.shape, (m.BOOT, 25))
        self.assertTrue((c.sum(1) == 25).all())
        np.testing.assert_array_equal(c, m.bootstrap_counts(25, [m.SEED, 3]))
        self.assertAlmostEqual(c.mean(), 1., places=2)

    def test_identical_engines_collapse_intervals(self):
        arms = {("A", "PHM", "", 0.): arm([80.]*30), ("B", "PHM", "", 0.): arm([100.]*30, missing=.5),
                ("ISO_LOWER98_M15", "PHM", "", 0.): arm([80.]*30), ("ISO_POINT_M15", "PHM", "", 0.): arm([100.]*30, missing=.5),
                ("AGE127", "AGE", "", 0.): m.age_arm([200]*30)}
        counts = m.bootstrap_counts(30, [m.SEED, 0])
        _, c, p, _ = m.analyse_cell("development", "FD001", 1, 1, arms, counts, None)
        row = next(r for r in c if r["contrast"] == "C1")
        self.assertEqual(row["cls"], "A_preferred_above_beta0")
        self.assertAlmostEqual(row["beta0"], .5)
        self.assertAlmostEqual(row["dW_low"], row["dW_high"])
        self.assertTrue(row["beta0_bounded"])
        self.assertAlmostEqual(row["beta0_low"], .5)
        curve = {q["beta"]: q for q in p if q["row_id"] == row["row_id"]}
        self.assertEqual(curve[0.]["boot_B_cheaper"], 1.)
        self.assertEqual(curve[1.]["boot_A_cheaper"], 1.)
        self.assertEqual(curve[.5]["boot_A_cheaper"], 0.)
        c7 = next(r for r in c if r["contrast"] == "C7")
        self.assertEqual(c7["cls"], "B_dominates")      # 80-cycle lives restore more often than age 127, no events either way
        self.assertTrue(np.isnan(c7["beta0"]))

    def test_unbounded_when_event_difference_includes_zero(self):
        rng = np.random.default_rng(1)
        n = 40
        base = rng.uniform(150, 200, n)
        ev = np.zeros(n)
        ev[0] = .02                                                  # a single engine carries all of B's events
        arms = {("ISO_LOWER98_M15", "PHM", "", 0.): arm(base+5), ("ISO_POINT_M15", "PHM", "", 0.): arm(base),
                ("AGE127", "AGE", "", 0.): m.age_arm([200]*n)}
        arms[("ISO_POINT_M15", "PHM", "", 0.)]["missing"] = ev
        counts = m.bootstrap_counts(n, [m.SEED, 1])
        _, c, _, _ = m.analyse_cell("development", "FD001", 1, 1, arms, counts, None)
        row = next(r for r in c if r["contrast"] == "C1")
        self.assertEqual(row["engines_event_B"], 1)
        self.assertEqual(row["cls"], "A_dominates")                  # longer life and fewer events: no break-even

    def test_pre_computed_inputs_are_pinned(self):
        for path, digest in m.INPUT_HASHES.items():
            self.assertEqual(m.sha(path), digest)


if __name__ == "__main__":
    unittest.main()
