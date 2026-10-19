import unittest

import numpy as np
import pandas as pd
from sklearn.metrics import adjusted_rand_score

import pilot_regime_synthetic_18a as p
from pilot_fd003_06 import read_inputs
from regime_normalisation import OPS, SENSORS, RegimeNormaliser


class RegimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        base = read_inputs("train", "FD001")
        cls.base = base[base.unit <= 30].reset_index(drop=True)
        cls.syn, cls.labels, cls.effects = p.make_synthetic(cls.base)

    def test_kmeans_recovers_well_separated_regimes(self):
        n = RegimeNormaliser(k=6).fit(self.syn)
        self.assertAlmostEqual(adjusted_rand_score(self.labels, n.assign(self.syn)), 1.0, places=6)

    def test_healthy_window_is_standardised_per_regime(self):
        n = RegimeNormaliser(k=6, labels=self.labels).fit(self.syn)
        z = n.transform(self.syn)
        healthy = z[z.cycle <= 20]
        for c in range(6):
            g = healthy[healthy.regime == c]
            self.assertLess(abs(g["s2"].mean()), 1e-9)
            self.assertAlmostEqual(g["s2"].std(ddof=1), 1.0, places=9)

    def test_normalisation_removes_injected_affine_regime_effects(self):
        z_syn = RegimeNormaliser(k=6, labels=self.labels).fit(self.syn).transform(self.syn)
        z_base = RegimeNormaliser(k=1).fit(self.base).transform(self.base)
        for s in ("s2", "s11"):
            self.assertGreater(np.corrcoef(z_syn[s], z_base[s])[0, 1], 0.9)
        raw = np.corrcoef(self.syn["s2"], self.base["s2"])[0, 1]
        self.assertLess(raw, 0.8)

    def test_transform_is_row_wise_and_causal(self):
        n = RegimeNormaliser(k=6).fit(self.syn)
        full = n.transform(self.syn)
        part = n.transform(self.syn.iloc[:50])
        np.testing.assert_allclose(full[SENSORS].iloc[:50].to_numpy(), part[SENSORS].to_numpy())

    def test_k1_assigns_single_regime(self):
        n = RegimeNormaliser(k=1).fit(self.base)
        self.assertTrue((n.assign(self.base) == 0).all())

    def test_synthetic_reproducible_and_constant_sensors_untouched(self):
        again, labels, _ = p.make_synthetic(self.base)
        pd.testing.assert_frame_equal(self.syn, again)
        const = [s for s in SENSORS if self.base[s].std(ddof=1) < 1e-9]
        for s in const:
            self.assertTrue((self.syn[s] == self.base[s]).all())

    def test_fit_depends_only_on_given_frame(self):
        a = RegimeNormaliser(k=6).fit(self.syn[self.syn.unit <= 15])
        b = RegimeNormaliser(k=6).fit(self.syn[self.syn.unit <= 15])
        np.testing.assert_allclose(a.mean, b.mean)

    def test_scripts_do_not_reference_confirmation_subsets(self):
        from pathlib import Path
        for name in ("regime_normalisation.py", "pilot_regime_synthetic_18a.py"):
            text = Path(__file__).with_name(name).read_text(encoding="utf-8")
            self.assertNotIn("FD002", text)
            self.assertNotIn("FD004", text)


if __name__ == "__main__":
    unittest.main()
