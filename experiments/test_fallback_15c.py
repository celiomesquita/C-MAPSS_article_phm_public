import json
import unittest

import numpy as np
import pandas as pd

import pilot_conservative_age_15b as c
import pilot_fallback_15a as f
import pilot_fallback_15c as p


class Fallback15cTests(unittest.TestCase):
    def test_ages_equal_p15b_estimates(self):
        est = pd.read_csv(p.ART / "pilot_conservative_age_15b/estimates.csv")
        for s, a in p.AGES.items():
            self.assertEqual(int(est[(est["subset"] == s) & (est.estimator == "E0")].age.iloc[0]), a)

    def test_no_evaluation_engine_reaches_endpoint_before_age(self):
        d = pd.read_csv(f.SRC)
        d = d[d.dataset == "complete"]
        for s, a in p.AGES.items():
            self.assertTrue((d[d["subset"] == s].endpoint > a).all())

    def test_hybrid_never_later_than_components_and_decides_everywhere(self):
        h, d = p.build()
        self.assertTrue(h.has.all())
        self.assertFalse((h.late | h.exact).any())
        self.assertTrue((h.sched <= h.age).all())

    def test_inputs_restricted(self):
        for fl in f.input_files():
            self.assertFalse(fl.name.startswith(("test_FD", "RUL_FD")) or "FD002" in fl.name or "FD004" in fl.name)


if __name__ == "__main__":
    unittest.main()
