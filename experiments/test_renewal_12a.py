import unittest

import numpy as np

import pilot_renewal_12a as p


class RenewalTests(unittest.TestCase):
    def test_constructed_renewal(self):
        u = np.array([10.0, 20.0, 30.0])
        ev = np.array([0, 1, 3])
        idx = np.array([[0, 1, 2, 0, 0, 0]])                     # cumulative 10, 30, 60, 70, 80, 90
        count, used, events = p.renewal(u, ev, idx, 65.0)
        self.assertEqual(count[0], 3)                            # restorations at 10, 30, 60
        self.assertEqual(used[0], 60.0)
        self.assertEqual([e[0] for e in events], [1, 0, 1])      # one missing decision, one strict late among completed lives
        count, used, _ = p.renewal(u, ev, idx, 60.0)
        self.assertEqual(count[0], 3)                            # restoration exactly at horizon is counted
        count, used, _ = p.renewal(u, ev, idx, 9.0)
        self.assertEqual((count[0], used[0]), (0, 0.0))

    def test_same_sequences_across_policies(self):
        lives = p.load_lives()
        a = p.sequences("FD001", 1, 10, 3200.0, lives)
        b = p.sequences("FD001", 1, 10, 3200.0, lives)
        self.assertTrue((a == b).all())
        self.assertFalse((a == p.sequences("FD001", 2, 10, 3200.0, lives)).all())

    def test_missing_decision_life_equals_endpoint(self):
        import pandas as pd
        d = pd.read_csv(p.SRC)
        d = d[(d.dataset == "complete") & (d.status == "endpoint_without_decision")]
        self.assertGreater(len(d), 0)
        self.assertTrue((d.utilised == d.endpoint).all())

    def test_inputs_exclude_test_rul_fd002_fd004(self):
        for f in p.input_files():
            self.assertFalse(f.name.startswith(("test_FD", "RUL_FD")) or "FD002" in f.name or "FD004" in f.name)

    def test_simulation_matches_analytic_on_synthetic(self):
        rng = np.random.default_rng(1)
        u = rng.integers(100, 300, 100).astype(float)
        ev = np.zeros(100, int)
        horizon = 500_000.0
        idx = rng.integers(0, 100, (400, int(horizon / 100) + 3))
        count, _, _ = p.renewal(u, ev, idx, horizon)
        self.assertAlmostEqual(count.mean() / horizon, 100 / u.sum(), delta=0.01 * 100 / u.sum())

    def test_all_policies_100_engines_each(self):
        lives = p.load_lives()
        self.assertEqual(len(lives), 2 * 3 * 16)
        self.assertTrue(all(len(v["utilised"]) == 100 for v in lives.values()))


if __name__ == "__main__":
    unittest.main()
