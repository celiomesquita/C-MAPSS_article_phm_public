"""Verify portable SA3 outputs independently from the archived per-engine rows."""

import argparse
import csv
import hashlib
import json
import math
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent


def rows(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=HERE / "reproduced")
    output = parser.parse_args().output
    for name in ["cells.csv", "contrasts.csv", "marker.csv"]:
        assert (output / name).read_bytes() == (HERE / "reference" / name).read_bytes(), name
    groups = defaultdict(dict)
    for row in rows(HERE / "evidence_inputs/decisions.csv"):
        key = row["subset"], int(row["repeat"]), int(row["delay"]), round(100 * (1-float(row["alpha"]))), int(row["reserve"])
        groups[key][int(row["unit"])] = min(float(row["endpoint"]), float(row["scheduled"]))
    checked = 0
    for row in rows(output / "contrasts.csv"):
        base = row["subset"], int(row["repeat"]), int(row["delay"])
        def value(level, reserve):
            sample = groups[base + (level, reserve)]
            assert set(sample) == set(range(1, 101))
            return sample
        def mean(sample):
            return math.fsum(sample.values()) / 100
        def rate(sample):
            return 1e6 / math.fsum(sample.values())
        if row["contrast"] == "interaction":
            terms = [(1, value(95, 12)), (-1, value(98, 12)), (-1, value(95, 15)), (1, value(98, 15))]
        else:
            def arm(text):
                level, reserve = text.split("_")
                return value(int(level[1:]), int(reserve[1:]))
            terms = [(1, arm(row["arm_a"])), (-1, arm(row["arm_b"]))]
        life = sum(sign * mean(sample) for sign, sample in terms)
        restoration = sum(sign * rate(sample) for sign, sample in terms)
        assert math.isclose(life, float(row["delta_mean_life"]), abs_tol=1e-10)
        assert math.isclose(restoration, float(row["delta_restorations_per_10000"]), abs_tol=1e-10)
        checked += 1
    assert checked == 72
    p10 = HERE.parents[1] / "experiments/pilot_f_uncertainty_10.py"
    lf = p10.read_bytes().replace(b"\r\n", b"\n")
    assert hashlib.sha256(lf).hexdigest() == "bec9cf1780e1bfa142a58b1080d8d52fe8ab4b2c00087f0ba11d10c54ab8e131"
    original = lf.replace(b"\n", b"\r\n").splitlines(keepends=True)
    original[285] = original[285].replace(b"\r\n", b"\n")
    assert hashlib.sha256(b"".join(original)).hexdigest() == "2d99ce838a9164282949fb4f88642675b354caead3e50bd316b4d0caae231d92"
    print(json.dumps(dict(status="passed", exact_output_files=3, independent_contrasts=checked,
                          p10_historical_bytes_reconstructed=True)))


if __name__ == "__main__":
    main()
