import unittest

import numpy as np

import pilot_conservative_age_15b as p


class AgeTests(unittest.TestCase):
    def test_inputs_restricted(self):
        for f in p.input_files():
            self.assertFalse(f.name.startswith(("test_FD", "RUL_FD")) or "FD002" in f.name or "FD004" in f.name)

    def test_clopper_pearson_known_values(self):
        self.assertAlmostEqual(p.cp_upper(0, 100, 0.95), 1 - 0.05 ** (1 / 100), places=10)
        self.assertAlmostEqual(p.cp_upper(0, 100, 0.90), 1 - 0.10 ** (1 / 100), places=10)
        self.assertEqual(p.cp_upper(5, 5, 0.9), 1.0)

    def test_nonparametric_feasibility_depends_on_confidence(self):
        t = np.arange(130, 230, dtype=float)
        self.assertEqual(p.nonparametric_age(t, 0.02, 0.80), 129)
        self.assertIsNone(p.nonparametric_age(t, 0.02, 0.90))
        self.assertIsNone(p.nonparametric_age(t, 0.02, 0.95))

    def test_loo_counts_only_unique_minimum(self):
        t = np.array([100.0, 150.0, 160.0, 170.0])
        self.assertEqual(p.loo_arrival_rate(t), 0.25)
        t2 = np.array([100.0, 100.0, 150.0, 160.0])
        self.assertEqual(p.loo_arrival_rate(t2), 0.0)

    def test_weibull_roundtrip(self):
        rng = np.random.default_rng(1)
        s = p.sample("weibull", (4.0, 200.0), 5000, rng)
        c, scale = p.weibull_fit(s)
        self.assertAlmostEqual(c, 4.0, delta=0.2)
        self.assertAlmostEqual(scale, 200.0, delta=5.0)
        self.assertAlmostEqual(p.cdf("weibull", (4.0, 200.0), p.quantile("weibull", (4.0, 200.0), 0.02)), 0.02, places=10)

    def test_age_costs_arrivals(self):
        t = np.array([100.0, 120.0, 200.0])
        r = p.age_costs(t, 110)
        self.assertEqual(r["arrivals"], 1)
        self.assertAlmostEqual(r["mean_utilised"], (100 + 110 + 110) / 3)


if __name__ == "__main__":
    unittest.main()
