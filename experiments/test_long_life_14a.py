import unittest

import numpy as np
import pandas as pd

import pilot_long_life_14a as p


class LongLifeTests(unittest.TestCase):
    def test_inputs_restricted_to_train_fd001_fd003(self):
        names = [f.name for f in p.input_files()]
        self.assertIn("train_FD001.txt", names)
        self.assertIn("train_FD003.txt", names)
        self.assertFalse(any(n.startswith(("test_", "RUL_")) or "FD002" in n or "FD004" in n for n in names))

    def test_missing_range_not_zero(self):
        r = pd.DataFrame({"range": [1.0, np.nan, 50.0]})
        finite = r[np.isfinite(r["range"])]
        self.assertEqual(len(finite), 2)
        self.assertNotIn(0.0, finite["range"].tolist())

    def test_tail_metrics_constructed_example(self):
        T = np.arange(1, 11, dtype=float)                       # tail cut q0.9 = 9.1 -> engine 10 only
        width = np.array([0, 0, 12, 0, 0, 0, 0, 0, 0, 30.0])     # wide: engines 3 and 10
        m = p.tail_metrics(T, width)
        self.assertEqual(m["tail_engines"], 1)
        self.assertEqual(m["wide_engines"], 2)
        self.assertEqual(m["wide_in_tail"], 1)
        self.assertAlmostEqual(m["enrichment"], 0.5 / 0.1)
        self.assertAlmostEqual(m["excess_tail_fraction"], 20 / 22)

    def test_bootstrap_reproducible(self):
        x, y = np.arange(30.0), np.arange(30.0) ** 1.5 + np.sin(np.arange(30.0))
        a = p.boot_spearman(x, y, np.random.default_rng(p.BOOT_SEED))
        b = p.boot_spearman(x, y, np.random.default_rng(p.BOOT_SEED))
        self.assertEqual(a, b)

    def test_event_classification_matches_status(self):
        d = pd.read_csv(p.P11 / "decisions.csv")
        d = d[d.dataset == "complete"]
        ev = p.is_event(d)
        self.assertTrue((d.loc[~ev, "status"] == "preventive_schedule").all())
        self.assertTrue((d.loc[ev, "status"] != "preventive_schedule").all())

    def test_classify_rule(self):
        s = pd.DataFrame({"subset": ["FD001", "FD003"], "quantity": p.PRIMARY,
                          "rho_lo": [0.1, -0.1], "enrichment": [2.5, 3.0]})
        self.assertEqual(p.classify(s)[0], "parcial")
        s["rho_lo"] = [0.1, 0.2]
        self.assertEqual(p.classify(s)[0], "sustentada")
        s["rho_lo"], s["enrichment"] = [-0.1, -0.1], [1.0, 1.5]
        self.assertEqual(p.classify(s)[0], "nao_sustentada")


if __name__ == "__main__":
    unittest.main()
