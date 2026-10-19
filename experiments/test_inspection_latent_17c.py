import unittest

import numpy as np

import inspection_arm_17b as base
import inspection_latent_17c as m


class LatentTests(unittest.TestCase):
    def test_quadrature_moments(self):
        self.assertAlmostEqual(m.WGT.sum(), 1., places=12)
        self.assertAlmostEqual((m.WGT*m.X).sum(), 0., places=12)
        self.assertAlmostEqual((m.WGT*m.X**2).sum(), 1., places=10)
        self.assertAlmostEqual((m.WGT*m.X**4).sum(), 3., places=8)

    def test_zero_sigma_reproduces_independent_arm(self):
        for T, has, D, d in [(220, False, np.nan, 1), (260, True, 190, 2), (180, True, 150, 1)]:
            for kind in ("window", "gamma"):
                lat = m.latent_expectation(T, has, D, d, kind, 0.)
                ref = base.hybrid_expectation(T, has, D, d, 0., "S2", 60, 1., 0., 1.)
                for k in ref:
                    self.assertAlmostEqual(lat[k], ref[k], places=10)

    def test_matches_monte_carlo_over_latent(self):
        rng = np.random.default_rng(4)
        T, d = 230, 2
        z = rng.standard_normal(40000)
        vals = [base.hybrid_expectation(T, False, np.nan, d, 0., "S2", 60*np.exp(.5*x), 1., 0., 1.)["util"] for x in z[:4000]]
        lat = m.latent_expectation(T, False, np.nan, d, "window", .5)["util"]
        self.assertLess(abs(np.mean(vals)-lat), 4*np.std(vals)/np.sqrt(len(vals)))

    def test_never_postpones_and_dependence_changes_result(self):
        T, d = 240, 1
        lat = m.latent_expectation(T, False, np.nan, d, "window", .5)
        ind = base.hybrid_expectation(T, False, np.nan, d, 0., "S2", 60, 1., 0., 1.)
        self.assertLessEqual(lat["util"], base._phm(T, False, np.nan, d, 0.)["util"]+1e-9)
        self.assertNotAlmostEqual(lat["util"], ind["util"], places=3)


if __name__ == "__main__":
    unittest.main()
