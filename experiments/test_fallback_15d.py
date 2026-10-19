import math
import unittest

import pandas as pd

import pilot_fallback_15a as f
import pilot_fallback_15d as p


class Fallback15dTests(unittest.TestCase):
    def test_single_age_is_smallest_min_minus_one_of_examined_sets(self):
        ends = f.endpoints()
        self.assertEqual(set(p.AGES.values()), {int(min(e.min() for e in ends.values())) - 1})
        self.assertEqual(len(set(p.AGES.values())), 1)

    def test_no_evaluation_engine_reaches_endpoint_before_age(self):
        d = pd.read_csv(f.SRC)
        d = d[d.dataset == "complete"]
        self.assertTrue((d.endpoint > 127).all())

    def test_pooled_bounds_values(self):
        b = p.pooled_bounds().set_index(["sample", "confidence"]).upper
        self.assertAlmostEqual(b[("FD001+FD003", 0.95)], 1 - 0.05 ** (1 / 200), places=6)
        self.assertAlmostEqual(b[("FD001+FD003", 0.90)], 1 - 0.10 ** (1 / 200), places=6)
        self.assertAlmostEqual(b[("hipotetico FD001-FD004, n=709, 0 ocorrencias", 0.95)], 1 - 0.05 ** (1 / 709), places=6)

    def test_hybrid_decides_everywhere_without_events(self):
        h, _ = p.build()
        self.assertTrue(h.has.all())
        self.assertFalse((h.late | h.exact).any())

    def test_inputs_restricted(self):
        for fl in f.input_files():
            self.assertFalse(fl.name.startswith(("test_FD", "RUL_FD")) or "FD002" in fl.name or "FD004" in fl.name)


if __name__ == "__main__":
    unittest.main()
