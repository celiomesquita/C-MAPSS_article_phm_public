"""P06: frozen-model reproduction and FD003 prospective boundaries."""

import hashlib
import unittest

import numpy as np
import pandas as pd

import pilot_fd001_05 as p05
from pilot_fd001 import SENSORS
from pilot_fd003_06 import SOURCE_MODELS, complete_labels, load_models, read_inputs


class P06Boundaries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.models = load_models(SOURCE_MODELS)

    def test_loading_reproduces_archived_fd001_predictions(self):
        inputs = p05.read_official_inputs().query("unit == 1").copy()
        saved = pd.read_csv(SOURCE_MODELS.parent / "predictions.csv").query("dataset == 'official' and unit == 1")
        for family, chosen in self.models.items():
            output = p05.transform_selected(inputs,chosen,family)
            reference = saved.query("family == @family")
            np.testing.assert_allclose(output.hi,reference.hi)
            np.testing.assert_allclose(output.predicted_rul,reference.predicted_rul)

    def test_transfer_uses_no_fd003_endpoint_or_future_values(self):
        data = complete_labels(read_inputs("train").query("unit <= 2").copy())
        changed = data.copy()
        changed.loc[changed.unit == 2,["end","rul"]] += 1000
        changed.loc[(changed.unit == 2) & (changed.cycle > 100),SENSORS] *= 100
        before = hashlib.sha256(SOURCE_MODELS.read_bytes()).hexdigest()
        for family, chosen in self.models.items():
            first = p05.transform_selected(data,chosen,family)
            second = p05.transform_selected(changed,chosen,family)
            prefix = (first.unit == 2) & (first.cycle <= 100)
            pd.testing.assert_frame_equal(first.loc[prefix],second.loc[prefix])
        self.assertEqual(before,hashlib.sha256(SOURCE_MODELS.read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
