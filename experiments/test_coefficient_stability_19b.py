import unittest

import joblib

import coefficient_stability_19b as m


def rec(channels, weights, directions=None):
    directions = directions or [1.]*len(channels)
    return dict(zip(channels, zip(directions, weights)))


class StabilityTests(unittest.TestCase):
    def test_identical_records(self):
        a = rec(["s2", "s3", "s4", "s7"], [.1, .3, .2, 0.])
        r = m.pair_metrics(a, a)
        self.assertAlmostEqual(r["spearman"], 1.)
        self.assertEqual((r["jaccard_active"], r["same_direction"], r["top3_overlap"]), (1., 1., 1.))

    def test_direction_flip_and_missing_channel(self):
        a = rec(["s2", "s3", "s4", "s7"], [.1, .3, .2, 0.], [1, 1, -1, 1])
        b = rec(["s2", "s3", "s4"], [.1, .3, .2], [1, 1, 1])
        r = m.pair_metrics(a, b)
        self.assertEqual(r["common"], 3)
        self.assertAlmostEqual(r["same_direction"], 2/3)
        self.assertEqual(r["jaccard_active"], 1.)

    def test_reversed_ranking(self):
        a = rec(["s2", "s3", "s4"], [.1, .2, .3])
        b = rec(["s2", "s3", "s4"], [.3, .2, .1])
        self.assertAlmostEqual(m.pair_metrics(a, b)["spearman"], -1.)

    def test_real_model_files_load(self):
        r = m.fold_record(joblib.load(m.SOURCES["FD001"]/"models_FD001_r1_f1.joblib"))
        self.assertTrue(r and all(c.startswith("s") for c in r))


if __name__ == "__main__":
    unittest.main()
