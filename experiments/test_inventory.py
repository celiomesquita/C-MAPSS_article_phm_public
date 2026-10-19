import tempfile
import unittest
from pathlib import Path

from inventory import rul, trajectory


class InventoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "fixture.txt"

    def test_duplicate_and_missing_cycles_are_rejected(self):
        self.path.write_text("1 1 2\n1 1 3\n1 3 4\n", encoding="ascii")
        result = trajectory(self.path, ["unit_id", "cycle", "sensor_1"], 1)
        self.assertEqual(len(result["errors"]), 2)

    def test_nonfinite_values_and_wrong_width_are_rejected(self):
        self.path.write_text("1 1 nan\n1 2\n", encoding="ascii")
        result = trajectory(self.path, ["unit_id", "cycle", "sensor_1"], 1)
        self.assertTrue(any("non-finite" in error for error in result["errors"]))
        self.assertTrue(any("columns" in error for error in result["errors"]))

    def test_rul_cardinality_and_negative_label_are_rejected(self):
        self.path.write_text("10\n-1\n", encoding="ascii")
        result = rul(self.path, 2)
        self.assertEqual(len(result["errors"]), 2)

    def test_unit_identifiers_are_local_and_cycles_restart(self):
        self.path.write_text("1 1 2\n1 2 3\n2 1 4\n", encoding="ascii")
        result = trajectory(self.path, ["unit_id", "cycle", "sensor_1"], 2)
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["cycles_per_unit"], {1: 2, 2: 1})


if __name__ == "__main__":
    unittest.main()
