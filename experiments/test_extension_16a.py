import unittest

import numpy as np

import pilot_extension_16a as p


def brute(T, has, D, d, orig_sched, u, age=127):
    tau = age - d
    if has and D <= tau:
        return min(orig_sched, T)
    end = D if has else T - 1
    total, alive = 0.0, 1.0
    for t in range(tau, end + 1):
        sched = age if t == tau else t + d
        total += alive * u * min(sched, T)
        alive *= (1 - u)
    return total + alive * (min(orig_sched, T) if has else T)


class ExtensionTests(unittest.TestCase):
    def test_u0_reproduces_original(self):
        e = p.engine_expectation(200, True, 170, 2, 172, 0.0)
        self.assertAlmostEqual(e["util"], 172.0)
        e = p.engine_expectation(200, False, np.nan, 1, np.nan, 0.0)
        self.assertAlmostEqual(e["util"], 200.0)
        self.assertAlmostEqual(e["missing"], 1.0)

    def test_u1_is_age_limit_for_engines_in_extension_zone(self):
        e = p.engine_expectation(200, True, 170, 2, 172, 1.0)
        self.assertAlmostEqual(e["util"], 127.0)
        e = p.engine_expectation(200, True, 110, 2, 112, 1.0)
        self.assertAlmostEqual(e["util"], 112.0)          # decided before the gate: unaffected

    def test_formula_matches_brute_force(self):
        cases = [(200, True, 170, 2, 172), (140, True, 135, 2, 137), (131, False, np.nan, 1, np.nan), (135, True, 133, 1, 134),
                 (129, True, 128, 2, 130)]
        for T, has, D, d, S in cases:
            for u in (0.001, 0.02, 0.3):
                e = p.engine_expectation(T, has, D, d, S, u)
                self.assertAlmostEqual(e["util"], brute(T, has, D, d, S, u), places=9, msg=(T, D, d, u))

    def test_late_events_only_from_loss_close_to_endpoint(self):
        e = p.engine_expectation(129, True, 128, 2, 130, 0.5)
        self.assertGreater(e["late"], 0.0)
        e = p.engine_expectation(300, True, 200, 2, 202, 0.0)
        self.assertEqual(e["late"], 0.0)

    def test_monte_carlo_agrees(self):
        rng = np.random.default_rng(7)
        T, D, d, S, u = 150, 140, 2, 142, 0.03
        tau = 125
        total, late = 0.0, 0
        N = 200000
        for _ in range(N):
            valid = rng.random(D - tau + 1) >= u
            if valid.all():
                sched = S
            else:
                t = tau + int(np.argmax(~valid))
                sched = 127 if t == tau else t + d
            total += min(sched, T)
            late += sched > T
        e = p.engine_expectation(T, True, D, d, S, u)
        self.assertAlmostEqual(total / N, e["util"], delta=0.05)
        self.assertAlmostEqual(late / N, e["late"], delta=0.005)

    def test_life_never_below_127_when_decision_after_gate(self):
        for u in (0.0, 0.01, 0.5, 1.0):
            e = p.engine_expectation(250, True, 200, 1, 201, u)
            self.assertGreaterEqual(e["util"], 127.0 - 1e-9)

    def test_inputs_restricted(self):
        for f in p.input_files():
            self.assertFalse(f.name.startswith(("test_FD", "RUL_FD")) or "FD002" in f.name or "FD004" in f.name)


if __name__ == "__main__":
    unittest.main()
