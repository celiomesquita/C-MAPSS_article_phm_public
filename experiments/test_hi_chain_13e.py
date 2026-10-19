import json
import unittest

import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits

import hi_chain_core_13e as core
import pilot_f_uncertainty_10 as p10
import pilot_hi_chain_13e as runner

ROOT = p10.ROOT
P11 = ROOT / "experiments/artifacts/pilot_removal_11"
P11A = ROOT / "experiments/artifacts/pilot_landmark_control_11a"
P11B = ROOT / "experiments/artifacts/pilot_loss_decomposition_11b"


def split(subset, repeat, fold):
    splits = json.loads((p10.OUT / "splits.json").read_text(encoding="utf-8"))
    return next(s for s in splits if (s["subset"], s["repeat"], s["fold"]) == (subset, repeat, fold))


class ChainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.train = {s: p10.read_inputs("train", s) for s in p10.CONFIG}

    def take(self, subset, ids):
        return self.train[subset].loc[self.train[subset].unit.isin(ids)].reset_index(drop=True)

    def test_weight_interface_reproduces_m18_hi(self):
        for subset in p10.CONFIG:
            sp = split(subset, 2, 3)
            health = p10.fit_health(self.take(subset, sp["fit"]), subset)
            alternative = core.weights_health(core.m18_effective(health), subset, sp["fit"], "M18")
            evaluation = self.take(subset, sp["evaluation"])
            a, ha = p10.features(evaluation, health)
            b, hb = p10.features(evaluation, alternative)
            np.testing.assert_allclose(hb.hi, ha.hi, atol=1e-10, rtol=0)
            self.assertTrue(ha.crossing.equals(hb.crossing))
            self.assertTrue((a.in_domain.to_numpy() == b.in_domain.to_numpy()).all())

    def test_m18_chain_reproduces_archived_p10(self):
        sp = split("FD003", 1, 4)
        with threadpool_limits(limits=1):
            bundle = p10.fit_pipeline(self.take("FD003", sp["fit"]), self.take("FD003", sp["converter"]), "FD003", sp["seed"])
            result = core.calibrate_and_evaluate(bundle, self.take("FD003", sp["uncertainty"]),
                                                 self.take("FD003", sp["evaluation"]), sp["uncertainty"], sp["evaluation"])
        runner.assert_reproduces_p10("FD003_r1_f4", result)

    def test_converter_refit_equals_p10_pipeline(self):
        sp = split("FD001", 3, 7)
        fit, conv = self.take("FD001", sp["fit"]), self.take("FD001", sp["converter"])
        with threadpool_limits(limits=1):
            original = p10.fit_pipeline(fit, conv, "FD001", sp["seed"])
            refit = core.fit_converters(original["health"], conv, "FD001", sp["seed"])
        evaluation = self.take("FD001", sp["evaluation"])
        a, _ = p10.predict_inputs(original, evaluation)
        b, _ = p10.predict_inputs(refit, evaluation)
        # Parallel tree averaging changes floating-point summation order.
        np.testing.assert_allclose(a.predicted_rul.to_numpy(), b.predicted_rul.to_numpy(), atol=1e-9, rtol=0)

    def test_decisions_match_p11_p11a_and_p11b(self):
        old = pd.read_csv(P11 / "decisions.csv")
        markers = pd.read_csv(P11A / "controls.csv")
        components = pd.read_csv(P11B / "components.csv")
        for subset, repeat, fold in [("FD001", 1, 5), ("FD003", 2, 2)]:
            tag = f"{subset}_r{repeat}_f{fold}"
            pred = pd.read_csv(p10.OUT / f"predictions_{tag}_complete.csv.gz")
            quantiles = pd.read_csv(p10.OUT / f"quantiles_{tag}.csv")
            ends = pred.groupby("unit").end.first()
            new = core.decisions(pred, quantiles, ends)
            reference = pd.concat([
                old.loc[old.subset.eq(subset) & old.repeat.eq(repeat) & old.fold.eq(fold) & old.dataset.eq("complete")],
                markers.loc[markers.subset.eq(subset) & markers.repeat.eq(repeat) & markers.fold.eq(fold)]])
            merged = new.merge(reference, on=["unit", "policy_id"], suffixes=("", "_ref"), validate="one_to_one")
            self.assertEqual(len(merged), len(new))
            for column in ["decision", "scheduled", "utilised"]:
                np.testing.assert_array_equal(merged[column].to_numpy(float), merged[f"{column}_ref"].to_numpy(float))
            for column in ["late", "exact_endpoint", "reached_endpoint", "has_decision"]:
                self.assertTrue((merged[column] == merged[f"{column}_ref"]).all(), column)
            c = components.loc[components.subset.eq(subset) & components.repeat.eq(repeat) & components.fold.eq(fold)
                               & components.rho.eq(1) & components.policy_id.isin(new.policy_id.unique())]
            joined = new.merge(c, on=["unit", "policy_id"], suffixes=("", "_ref"), validate="one_to_one")
            self.assertEqual(len(joined), len(new))
            np.testing.assert_array_equal(joined.W_gap.to_numpy(float), joined.W_total.to_numpy(float))
            np.testing.assert_array_equal(joined.J.to_numpy(int), joined.J_total.to_numpy(int))
            np.testing.assert_array_equal(joined.usable_marker.to_numpy(float), joined.A.to_numpy(float))

    def test_selected_provenance_and_m18_identity(self):
        selections = pd.read_csv(runner.P13D / "selections.csv")
        self.assertEqual(len(selections), 60)
        for r in selections.itertuples():
            tag = f"{r.subset}_r{r.repeat}_f{r.fold}"
            sp, model = split(r.subset, r.repeat, r.fold), joblib.load(runner.P13D / f"selected_hi_{tag}.joblib")
            self.assertEqual(model["candidate"], r.selected)
            self.assertEqual(sorted(model["fit_units"]), sorted(sp["fit"]))
            self.assertTrue(set(model["selection_development"]).isdisjoint(sp["uncertainty"]+sp["evaluation"]))
            if r.selected == "M18":
                old = joblib.load(p10.OUT / f"models_{tag}.joblib")["health"]
                np.testing.assert_allclose(model["effective"], core.m18_effective(old), atol=1e-8, rtol=1e-7)
        self.assertEqual(int((~selections.selection_eligible).sum()), 1)

    def test_range_missing_is_not_zero(self):
        rows = []
        for repeat, (a, b) in enumerate([(100., np.nan), (100., 120.), (100., 110.)], start=1):
            for unit, value in [(1, a), (2, b)]:
                rows.append(dict(subset="FD001", chain="M18", unit=unit, repeat=repeat, policy_id="ISO_LOWER98_M15_D1",
                                 decision=value, usable_marker=value))
        r = core.between_repeat_ranges(pd.DataFrame(rows))
        first = r.loc[r.quantity.eq("usable_marker")].set_index("unit")
        self.assertEqual(first.loc[1, "range"], 0.)
        self.assertTrue(np.isnan(first.loc[2, "range"]))
        self.assertEqual(first.loc[2, "missing_repeats"], 1)

    def test_oracle_terms(self):
        self.assertEqual(core.oracle_terms(dict(decision=np.nan), 200, 1), dict(oracle_deadline=198, W_gap=-1., J=1, B=2.))
        self.assertEqual(core.oracle_terms(dict(decision=198.), 200, 1), dict(oracle_deadline=198, W_gap=0., J=0, B=0.))
        self.assertEqual(core.oracle_terms(dict(decision=150.), 200, 2)["W_gap"], 47.)

    def test_inputs_exclude_official_tests(self):
        files = runner.input_files()
        self.assertFalse(any("test_FD" in p.name or "RUL_FD" in p.name for p in files))
        self.assertEqual([r["policy_id"] for r in core.rules()][:4],
                         ["ISO_POINT_M15_D1", "ISO_POINT_M15_D2", "ISO_LOWER98_M15_D1", "ISO_LOWER98_M15_D2"])


if __name__ == "__main__":
    unittest.main()
