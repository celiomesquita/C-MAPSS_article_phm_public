import unittest

import numpy as np

import pilot_scale_bridge_12b as p


def one_engine(horizon, k, rho, llp, ic, reps=1, u=100.0, e=0, init=None):
    uu, ee = np.array([u]), np.array([e])
    idx = np.zeros((reps, 400), int)
    init = np.zeros((3, reps)) if init is None else init
    return p.simulate(uu, ee, k, rho, llp, horizon, ic, idx, init)


class BridgeTests(unittest.TestCase):
    def test_llp_forced_visits_constructed(self):
        d, l, *_ = one_engine(6000.0, 10.0, 1.0, 2500.0, 0)
        self.assertEqual((int(d[0]), int(l[0])), (5, 2))    # D at 1000,2000,3500,4500,6000 ; L at 2500,5000

    def test_rho_only_later_lives(self):
        d, l, *_ = one_engine(3000.0, 10.0, 0.8, None, 0)
        self.assertEqual((int(d[0]), int(l[0])), (3, 0))    # 1000, 1800, 2600

    def test_restoration_at_horizon_counted_and_not_beyond(self):
        d, *_ = one_engine(1000.0, 10.0, 1.0, None, 0)
        self.assertEqual(int(d[0]), 1)
        d, *_ = one_engine(999.0, 10.0, 1.0, None, 0)
        self.assertEqual(int(d[0]), 0)

    def test_stationary_start_matches_rate(self):
        rng = np.random.default_rng(3)
        u = rng.integers(100, 300, 100).astype(float)
        e = np.zeros(100, int)
        reps, k, horizon = 4000, 20.0, 9000.0
        idx = rng.integers(0, 100, (reps, 200))
        init = rng.random((3, reps))
        d, *_ = p.simulate(u, e, k, 1.0, None, horizon, 1, idx, init)
        se = d.std(ddof=1) / np.sqrt(reps)
        self.assertLess(abs(d.mean() - horizon * (100 / u.sum()) / k) / se, 4.0)

    def test_llp_visits_equal_across_rule_sets(self):
        rng = np.random.default_rng(5)
        idx = rng.integers(0, 100, (500, 300))
        init = rng.random((3, 500))
        out = []
        for scale in (80.0, 150.0):
            u = rng.integers(100, 300, 100) * scale / 100
            out.append(p.simulate(u, np.zeros(100, int), 30.0, 1.0, 20000.0, 32000.0, 1, idx, init)[1])
        self.assertTrue((out[0] == out[1]).all())

    def test_ic1_llp_age_uniform_and_initial_count(self):
        d, l, *_ = one_engine(30.0, 10.0, 1.0, 20000.0, 1, reps=2, init=np.array([[0.0, 0.0], [0.0, 0.5], [0.999, 0.0]]))
        self.assertEqual(l[0], 1)    # LLP at 99.9% of the limit forces a visit within 20 FC

    def test_inputs_exclude_test_rul_fd002_fd004(self):
        for f in p.input_files():
            self.assertFalse(f.name.startswith(("test_FD", "RUL_FD")) or "FD002" in f.name or "FD004" in f.name)

    def test_seed_reproducible(self):
        a = p.draws(111.0, 40.0, 1.0, 20000.0, 32000.0, 0, 1, 2, 1, 3)
        b = p.draws(111.0, 40.0, 1.0, 20000.0, 32000.0, 0, 1, 2, 1, 3)
        self.assertTrue((a[0] == b[0]).all() and (a[1] == b[1]).all())

    def test_reference_median_is_documented_value(self):
        self.assertAlmostEqual(p.reference_median(), 8425.0)

    def test_classification(self):
        self.assertEqual(p.classify(-1.0, 0.1, -0.5), "estavel")
        self.assertEqual(p.classify(1.0, 0.1, -0.5), "invertido")
        self.assertEqual(p.classify(0.1, 0.1, -0.5), "indistinguivel")


if __name__ == "__main__":
    unittest.main()
