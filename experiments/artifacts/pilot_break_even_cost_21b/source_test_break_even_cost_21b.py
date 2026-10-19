import unittest

import numpy as np

import break_even_21a as b21
import break_even_cost_21b as m


def arm(util, insp=0., missing=0.):
    util = np.asarray(util, float)
    z = np.zeros(len(util))
    return dict(util=util, late=z.copy(), exact=z.copy(), missing=z+missing, insp=z+insp)


class InspectionCostTests(unittest.TestCase):
    def test_effective_rate(self):
        # 10 lives of 100 cycles, 4 inspections per life, q=0.01 -> (10 + 0.01*40)/1000
        self.assertAlmostEqual(m.effective_rate(10, 1000., 40., .01), 10.4/1000)

    def test_known_threshold_with_inspection_cost(self):
        # B: PHM, 100-cycle lives, 0.5 events per life. A: hybrid, 80-cycle lives, no events, 2 inspections per life.
        n = 20
        arms = {("ISO_POINT_M15", "PHM", "", 0.): arm([100.]*n, missing=.5),
                ("ISO_POINT_M15", "HYB", "S2_W60_g1", 0.): arm([80.]*n, insp=2.),
                ("ISO_LOWER98_M15", "PHM", "", 0.): arm([100.]*n), ("AGE127", "AGE", "", 0.): b21.age_arm([200]*n)}
        counts = b21.bootstrap_counts(n, [b21.SEED, 0])
        for q, expected in [(0., (20/1600-20/2000)/(10/2000)), (.01, ((20+.01*40)/1600-20/2000)/(10/2000))]:
            _, c, _, _ = m.analyse_cell_cost("development", "FD001", 1, 1, arms, counts, q)
            row = next(r for r in c if r["contrast"] == "C3")
            self.assertEqual(row["cls"], "A_preferred_above_beta0")
            self.assertAlmostEqual(row["beta0"], expected, places=9)
        self.assertGreater(((20+.01*40)/1600-20/2000), (20/1600-20/2000))

    def test_non_hybrid_arms_have_no_inspection(self):
        n = 10
        arms = {("A", "PHM", "", 0.): arm([100.]*n), ("AGE127", "AGE", "", 0.): b21.age_arm([200]*n)}
        counts = b21.bootstrap_counts(n, [b21.SEED, 1])
        r, _, _, _ = m.analyse_cell_cost("development", "FD001", 1, 1, arms, counts, .02)
        self.assertEqual(max(x["inspection_rate"] for x in r), 0.)

    def test_zero_q_reproduces_p21a_logic(self):
        n = 30
        arms = {("ISO_LOWER98_M15", "PHM", "", 0.): arm([80.]*n), ("ISO_POINT_M15", "PHM", "", 0.): arm([100.]*n, missing=.5),
                ("AGE127", "AGE", "", 0.): b21.age_arm([200]*n)}
        counts = b21.bootstrap_counts(n, [b21.SEED, 0])
        _, c, _, _ = m.analyse_cell_cost("development", "FD001", 1, 1, arms, counts, 0.)
        _, c0, _, _ = b21.analyse_cell("development", "FD001", 1, 1, {k: {x: v for x, v in a.items() if x != "insp"} for k, a in arms.items()}, counts, None)
        for r, r0 in zip(c, c0):
            self.assertEqual(r["cls"], r0["cls"])
            self.assertAlmostEqual(r["dW"], r0["dW"], places=12)

    def test_constants(self):
        self.assertEqual(m.QS, (0., .005, .01, .02))


if __name__ == "__main__":
    unittest.main()
