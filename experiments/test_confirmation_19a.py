import importlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import numpy as np
import pandas as pd

import confirmation_19a as c
import pilot_f_uncertainty_10 as p10
from regime_normalisation import SENSORS

EXPERIMENTS = c.ROOT / "experiments"


def fold_fixture():
    inputs = c.read_train(c.ROOT / "CMAPSSData/train_FD001.txt")
    partition = c.partitions(range(1, 101), p10.SEEDS[0])[0]
    config = dict(p10.CONFIG["FD001"])
    with c.registered("CONF_TEST", config):
        result = c.run_fold(inputs, partition, "CONF_TEST", p10.SEEDS[0], 6)
    return inputs, partition, config, result


class CriterionTests(unittest.TestCase):
    def test_clopper_pearson_thresholds_of_the_protocol(self):
        self.assertAlmostEqual(c.cp_upper(0, 509), 1-.05**(1/509), places=10)
        self.assertEqual(c.max_passing_hits(509), 4)
        self.assertLessEqual(c.cp_upper(4, 509), .02)
        self.assertGreater(c.cp_upper(5, 509), .02)
        self.assertEqual(c.max_passing_hits(709), 7)
        self.assertAlmostEqual(c.cp_upper(0, 709), .0042, places=4)
        self.assertEqual(c.cp_upper(5, 5), 1.)

    def test_age_criterion_counts_inclusive_limit(self):
        lives = np.r_[np.full(505, 200), [127, 126, 100, 127]]
        result = c.age_criterion(lives)
        self.assertEqual((result["engines"], result["hits"]), (509, 4))
        self.assertTrue(result["passes"])
        self.assertEqual(c.age_criterion(np.r_[lives, [128]])["hits"], 4)
        self.assertFalse(c.age_criterion(np.r_[lives[1:], [90, 90]])["passes"])


class PartitionTests(unittest.TestCase):
    def test_reproduces_p10_layout(self):
        for seed in p10.SEEDS:
            self.assertEqual(c.partitions(range(1, 101), seed), p10.partitions(seed))

    def test_config_group_is_disjoint_and_evaluation_covers_rest_once(self):
        group, rest = c.split_config(range(1, 261))
        ids = group["fit"]+group["calibration"]+group["selection"]
        self.assertEqual((len(ids), len(set(ids)), len(rest)), (80, 80, 180))
        self.assertTrue(set(ids).isdisjoint(rest))
        for seed in p10.SEEDS:
            folds = c.partitions(rest, seed)
            evaluation = sum([f["evaluation"] for f in folds], [])
            self.assertEqual(sorted(evaluation), sorted(rest))
            for f in folds:
                used = f["fit"]+f["converter"]+f["uncertainty"]+f["evaluation"]
                self.assertEqual(len(used), len(set(used)))
                self.assertTrue(set(used).isdisjoint(ids))
                self.assertEqual((len(f["fit"]), len(f["converter"]), len(f["uncertainty"])), (25, 15, 50))

    def test_fd004_sized_domain_is_feasible(self):
        group, rest = c.split_config(range(1, 250))
        self.assertEqual(len(rest), 169)
        c.partitions(rest, p10.SEEDS[0])


class OpeningLockTests(unittest.TestCase):
    def make_world(self, root, with_amendment=True, bad_hash=False):
        data = root / "data"
        data.mkdir()
        frames = {}
        rng = np.random.default_rng(1)
        for label, name in c.CONFIRMATION_FILES.items():
            rows = [[u, t, 1., 2., 3.]+list(rng.normal(size=21)) for u in (1, 2) for t in range(1, 6)]
            pd.DataFrame(rows).to_csv(data / name, sep=" ", header=False, index=False)
        manifest = {"dados": {f"CMAPSSData/{n}": {"sha256": c.sha(data / n)} for n in c.CONFIRMATION_FILES.values()}}
        if bad_hash:
            manifest["dados"]["CMAPSSData/train_FD002.txt"]["sha256"] = "0"*64
        (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        text = "# emendas\n"
        if with_amendment:
            text += "".join(f"{n} sha256={c.sha(EXPERIMENTS / n)}\n" for n in c.MODULES)
        (root / "emendas.md").write_text(text, encoding="utf-8")
        return dict(emendas=root / "emendas.md", manifest=root / "manifest.json", data_dir=data, out=root / "out",
                    experiments=EXPERIMENTS)

    def test_refuses_without_amendment(self):
        with tempfile.TemporaryDirectory() as d:
            world = self.make_world(Path(d), with_amendment=False)
            with mock.patch.object(c, "read_train", side_effect=AssertionError("data read")):
                with self.assertRaises(PermissionError):
                    c.open_confirmation(**world)
            self.assertFalse((world["out"] / "abertura.json").exists())

    def test_refuses_changed_data_before_reading(self):
        with tempfile.TemporaryDirectory() as d:
            world = self.make_world(Path(d), bad_hash=True)
            with mock.patch.object(c, "read_train", side_effect=AssertionError("data read")):
                with self.assertRaises(PermissionError):
                    c.open_confirmation(**world)

    def test_opens_once_and_marks(self):
        with tempfile.TemporaryDirectory() as d:
            world = self.make_world(Path(d))
            opened = c.open_confirmation(**world)
            self.assertEqual(sorted(opened), ["FD002", "FD004"])
            self.assertTrue((world["out"] / "abertura.json").exists())
            with self.assertRaises(PermissionError):
                c.open_confirmation(**world)

    def test_import_reads_no_confirmation_file(self):
        seen = []
        original = pd.read_csv

        def spy(path, *a, **k):
            seen.append(str(path))
            return original(path, *a, **k)

        with mock.patch.object(pd, "read_csv", spy), mock.patch.object(Path, "read_bytes", autospec=True,
                side_effect=lambda self: seen.append(str(self)) or b""):
            importlib.reload(c)
        self.assertFalse([s for s in seen if "FD002" in s or "FD004" in s])
        importlib.reload(c)


class PipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inputs, cls.partition, cls.config, cls.result = fold_fixture()

    def test_calibration_scores_come_only_from_uncertainty_engines(self):
        scores = self.result["u_scores"]
        self.assertTrue(set(scores.unit) <= set(self.partition["uncertainty"]))
        self.assertTrue(set(scores.unit).isdisjoint(self.partition["evaluation"]))
        pd.testing.assert_frame_equal(self.result["quantiles"], p10.calibrate(scores))

    def test_changing_evaluation_engines_leaves_quantiles_and_models_unchanged(self):
        altered = self.inputs.copy()
        mask = altered.unit.isin(self.partition["evaluation"]) & altered.cycle.gt(60)
        altered = altered.loc[~mask]
        with c.registered("CONF_TEST2", self.config):
            other = c.run_fold(altered, self.partition, "CONF_TEST2", p10.SEEDS[0], 6)
        pd.testing.assert_frame_equal(self.result["quantiles"], other["quantiles"])
        np.testing.assert_allclose(self.result["bundle"]["health"]["beta"], other["bundle"]["health"]["beta"])

    def test_predictions_are_causal_after_the_crossing(self):
        pred = self.result["e_pred"]
        iso = pred.loc[pred.method.eq("ISO") & pred.in_domain]
        unit = int(iso.unit.iloc[0])
        first = int(iso.loc[iso.unit.eq(unit), "cycle"].min())
        cut = first+5
        normaliser = c.RegimeNormaliser(k=6).fit(c.subset(self.inputs, self.partition["fit"]))
        raw = c.subset(self.inputs, [unit])
        truncated = normaliser.transform(raw.loc[raw.cycle <= cut])
        again, _ = p10.predict_inputs(self.result["bundle"], truncated)
        again = again.loc[again.method.eq("ISO") & again.in_domain].set_index("cycle").predicted_rul
        full = iso.loc[iso.unit.eq(unit)].set_index("cycle").predicted_rul.loc[:cut]
        np.testing.assert_allclose(again.loc[:cut].to_numpy(), full.to_numpy(), atol=1e-9)

    def test_policy_set_and_ordering(self):
        decisions = c.decisions_for(self.result, "T", 1, 1)
        specs = c.policy_specs()
        self.assertEqual(len(specs), 2*2*4+4)
        self.assertEqual(len(decisions), len(specs)*len(self.partition["evaluation"]))
        wide = decisions.pivot_table(index="unit", columns="policy_id", values="decision", aggfunc="first")
        for method in c.METHODS:
            for d in (1, 2):
                lower, point = wide[f"{method}_LOWER98_M15_D{d}"], wide[f"{method}_POINT_M15_D{d}"]
                both = lower.notna() & point.notna()
                self.assertTrue((lower[both] <= point[both]).all())
        age = decisions.loc[decisions.policy_id.eq("AGE127_D2")]
        self.assertTrue((age.decision == 125).all() and (age.scheduled == 127).all())
        self.assertTrue((age.late == (age.endpoint < 127)).all())
        marker = decisions.loc[decisions.policy_id.eq("HI_MARKER_D1")]
        self.assertTrue((marker.scheduled == marker.decision+1).all())

    def test_extension_at_zero_loss_keeps_phm_schedule(self):
        decisions = c.decisions_for(self.result, "T", 1, 1)
        ex = c.extension_rows(decisions, "T", 1)
        zero = ex.loc[ex.u.eq(0.)]
        base = decisions.loc[decisions.policy_id.eq("ISO_LOWER98_M15_D1")].set_index("unit")
        row = zero.loc[zero.base.eq("ISO_LOWER98_M15") & zero.delay.eq(1)].set_index("unit")
        expected = np.minimum(base.scheduled.where(base.has_decision, base.endpoint), base.endpoint)
        np.testing.assert_allclose(row.util.loc[expected.index].to_numpy(), expected.to_numpy())


class ConfigurationTests(unittest.TestCase):
    def test_selection_is_deterministic_and_inside_the_grid(self):
        inputs = c.read_train(c.ROOT / "CMAPSSData/train_FD001.txt")
        group, _ = c.split_config(inputs.unit.unique(), sizes=(40, 20, 20))
        a, table = c.select_config(inputs, group, 6)
        b, _ = c.select_config(inputs, group, 6)
        self.assertEqual(a, b)
        self.assertEqual(len(table), 12)
        self.assertEqual(int(table.chosen.sum()), 1)
        self.assertIn((a["tau"], a["gamma"], a["ridge"]), c.GRID)
        self.assertEqual(table.loc[table.chosen, "selection_rmse"].iloc[0], table.selection_rmse.min())


if __name__ == "__main__":
    unittest.main()
