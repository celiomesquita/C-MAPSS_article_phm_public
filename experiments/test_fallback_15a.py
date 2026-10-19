import json
import unittest

import numpy as np
import pandas as pd

import pilot_fallback_15a as p


def frame(dec, endpoint):
    return pd.DataFrame(dict(decision=dec, endpoint=endpoint))


class FallbackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.d = pd.read_csv(p.SRC)
        cls.d = cls.d[cls.d.dataset == "complete"]

    def test_inputs_exclude_test_rul_fd002_fd004(self):
        for f in p.input_files():
            self.assertFalse(f.name.startswith(("test_FD", "RUL_FD")) or "FD002" in f.name or "FD004" in f.name)

    def test_control_age_definition_in_p13a(self):
        a = self.d[self.d.policy_id.str.startswith("AGE_D")]
        tau = a.control_age - a.delay
        observed = (tau < a.endpoint)
        self.assertTrue((observed == a.has_decision).all())
        self.assertTrue(((a.scheduled == a.control_age) | ~a.has_decision).all())

    def test_infinite_age_reproduces_original_rows(self):
        for base in p.BASES:
            for delay in (1, 2):
                b = self.d[(self.d.policy_id == f"{base}_D{delay}") & (self.d["subset"] == "FD001") & (self.d.repeat == 1)].sort_values("unit")
                h = p.hybrid(b, pd.Series(1e9, index=b.index), delay)
                self.assertTrue((h.status.to_numpy() == b.status.to_numpy()).all(), base)
                np.testing.assert_allclose(h.utilised.to_numpy(), b.utilised.to_numpy())
                self.assertFalse(h.age_acts.any())

    def test_hybrid_not_later_than_components(self):
        b = frame([100.0, np.nan, 150.0, 120.0], [200, 200, 140, 119])
        h = p.hybrid(b, pd.Series(130.0, index=b.index), 2)           # age decision 128 for T>128
        self.assertEqual(list(h.dec), [100.0, 128.0, 128.0, 120.0])
        self.assertEqual(list(h.age_acts), [False, True, True, False])
        self.assertEqual(list(h.status), ["preventive_schedule", "preventive_schedule", "preventive_schedule", "late_schedule"])

    def test_tie_prefers_phm_and_missing_stays_missing(self):
        b = frame([128.0, np.nan], [200, 100])
        h = p.hybrid(b, pd.Series(130.0, index=b.index), 2)
        self.assertEqual(list(h.age_acts), [False, False])
        self.assertEqual(h.status.iloc[1], "endpoint_without_decision")
        self.assertEqual(h.utilised.iloc[1], 100.0)

    def test_age_with_age_is_age(self):
        a = self.d[(self.d.policy_id == "AGE_D1") & (self.d["subset"] == "FD001") & (self.d.repeat == 1)].sort_values("unit")
        h = p.hybrid(a, a.control_age, 1)
        self.assertTrue((h.status.to_numpy() == a.status.to_numpy()).all())
        np.testing.assert_allclose(h.utilised.to_numpy(), a.utilised.to_numpy())

    def test_ages_use_only_development_engines_and_reproduce_p11_age(self):
        ends = p.endpoints()
        ages = p.age_table(ends)
        a = self.d[self.d.policy_id == "AGE_D1"].groupby(["subset", "repeat", "fold"]).control_age.first().reset_index()
        m = ages[ages.q == 0.0].merge(a, on=["subset", "repeat", "fold"])
        self.assertEqual(len(m), 60)
        self.assertTrue((m.age == m.control_age).all())
        for (s, r, f), g in ages.groupby(["subset", "repeat", "fold"]):
            self.assertTrue(g.sort_values("q").age.is_monotonic_increasing)
            self.assertTrue((g.dev_engines == 40).all())

    def test_no_engine_used_by_u_or_e_in_ages(self):
        for e in json.loads(p.SPLITS.read_text(encoding="utf-8")):
            dev = set(e["fit"]) | set(e["converter"])
            self.assertTrue(dev.isdisjoint(e["uncertainty"]) and dev.isdisjoint(e["evaluation"]))


if __name__ == "__main__":
    unittest.main()
