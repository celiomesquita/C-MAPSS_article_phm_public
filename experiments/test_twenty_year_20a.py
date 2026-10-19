import unittest

import numpy as np
import pandas as pd

import inspection_arm_17b as ins
import pilot_scale_bridge_12b as bridge
import twenty_year_20a as m


class PmfTests(unittest.TestCase):
    def test_pmf_matches_exact_expectation_of_p17(self):
        rng = np.random.default_rng(5)
        for _ in range(60):
            T = int(rng.integers(128, 320)); has = bool(rng.integers(0, 2))
            D = int(rng.integers(100, T)) if has else np.nan
            d = int(rng.integers(1, 3))
            for inspect in (False, True):
                c, p, tail = m.decision_pmf(T, has, D, d, inspect)
                self.assertAlmostEqual(p.sum()+tail, 1., places=12)
                util = (p*np.minimum(c+d, T)).sum()+tail*T
                if inspect:
                    ref = ins.hybrid_expectation(T, has, D, d, 0., "S2", 60, 1., 0., 1.)
                else:
                    ref = ins._phm(T, has, D, d, 0.)
                self.assertAlmostEqual(util, ref["util"], places=9)
                self.assertAlmostEqual((p*((c+d) > T)).sum(), ref["late"], places=9)
                self.assertAlmostEqual(tail, ref["missing"], places=9)

    def test_age_arm_is_deterministic(self):
        frame = pd.DataFrame(dict(unit=[1, 2, 3], endpoint=[200, 127, 120], has_decision=False, decision=np.nan))
        a = m.build_atoms(frame, None, 2, "AGE")
        self.assertEqual(a["util"].tolist(), [127., 127., 120.])
        self.assertEqual(a["event"].tolist(), [0, 2, 3])
        self.assertTrue(np.allclose(a["prob"], 1.))


class SimulatorTests(unittest.TestCase):
    def test_single_outcome_arm_reproduces_p12_simulator(self):
        rng = np.random.default_rng(2)
        util = rng.integers(120, 300, 30).astype(float)
        ev = rng.integers(0, 4, 30)
        atoms = dict(engine=np.arange(30), util=util, event=ev, prob=np.ones(30), n=30)
        table = m.cumulative_table(atoms)
        for ic, llp, rho in [(0, None, 1.), (1, 20000., .8), (1, None, 1.), (0, 25000., .8)]:
            idx = rng.integers(0, 30, (50, 300))
            v = rng.random((50, 300))
            init = rng.random((3, 50))
            ref = bridge.simulate(util, ev, 40., rho, llp, 32000., ic, idx, init)
            sel = m.sample_atoms(atoms, table, idx, v)
            self.assertTrue((sel == idx).all())
            got = m.simulate_draws(util[sel], ev[sel], util, np.full(30, 1/30), ev, 40., rho, llp, 32000., ic, init)
            for a, b in zip(ref, got):
                np.testing.assert_array_equal(a, b)

    def test_inverse_cdf_sampling_matches_probabilities(self):
        atoms = dict(engine=np.array([0, 0, 1]), util=np.array([100., 200., 150.]), event=np.zeros(3, int),
                     prob=np.array([.25, .75, 1.]), n=2)
        table = m.cumulative_table(atoms)
        rng = np.random.default_rng(1)
        eng = np.zeros(200000, int); v = rng.random(200000)
        sel = m.sample_atoms(atoms, table, eng, v)
        self.assertAlmostEqual((sel == 0).mean(), .25, delta=.005)
        self.assertTrue(((m.sample_atoms(atoms, table, np.ones(10, int), rng.random(10))) == 2).all())

    def test_stationary_start_with_stochastic_outcomes_matches_renewal_rate(self):
        frame = pd.DataFrame(dict(unit=range(1, 7), endpoint=[150, 180, 210, 240, 270, 300], has_decision=False, decision=np.nan))
        atoms = m.build_atoms(frame, None, 1, "HYB")
        self.assertGreater(len(atoms["util"]), 6)
        arms = {"HYB": atoms}
        tables = {"HYB": m.cumulative_table(atoms)}
        rate = m.analytic_rate(atoms)
        k, horizon = 20., 32000.
        res = m.run_cell(arms, tables, k, 1., None, 1, horizon, [7, 7, 7])["HYB"][0]
        z = (res.mean()-horizon*rate/k)/(res.std(ddof=1)/np.sqrt(len(res)))
        self.assertLess(abs(z), 4.)

    def test_inputs_have_no_raw_confirmation_data(self):
        self.assertNotIn("train_FD", " ".join(str(p) for p in (m.SRC_DEV, m.SRC_CONF)))


if __name__ == "__main__":
    unittest.main()
