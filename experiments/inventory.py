"""Validate raw C-MAPSS files and produce an auditable inventory (stdlib only)."""

import argparse
import csv
import hashlib
import json
import math
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trajectory(path, columns, expected_units):
    errors = []
    lengths = {}
    minima = [math.inf] * len(columns)
    maxima = [-math.inf] * len(columns)
    rows = 0
    previous_unit = 0
    for line_no, line in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        if not line.strip():
            continue
        tokens = line.split()
        if len(tokens) != len(columns):
            errors.append(f"line {line_no}: {len(tokens)} columns, expected {len(columns)}")
            continue
        try:
            values = [float(token) for token in tokens]
        except ValueError:
            errors.append(f"line {line_no}: non-numeric value")
            continue
        if not all(math.isfinite(value) for value in values):
            errors.append(f"line {line_no}: non-finite value")
            continue
        if any(value < 1 or not value.is_integer() for value in values[:2]):
            errors.append(f"line {line_no}: invalid unit/cycle")
            continue
        unit, cycle = map(int, values[:2])
        if unit < previous_unit:
            errors.append(f"line {line_no}: units not sorted")
        if cycle != lengths.get(unit, 0) + 1:
            errors.append(f"line {line_no}: duplicate, missing or unordered cycle for unit {unit}")
        previous_unit = unit
        lengths[unit] = cycle
        rows += 1
        minima = [min(a, b) for a, b in zip(minima, values)]
        maxima = [max(a, b) for a, b in zip(maxima, values)]
    if sorted(lengths) != list(range(1, expected_units + 1)):
        errors.append(f"unit IDs differ from 1..{expected_units}")
    return {
        "rows": rows,
        "units": len(lengths),
        "cycles_per_unit": lengths,
        "min_cycles": min(lengths.values(), default=None),
        "max_cycles": max(lengths.values(), default=None),
        "column_ranges": {
            name: {"min": lo if math.isfinite(lo) else None,
                   "max": hi if math.isfinite(hi) else None}
            for name, lo, hi in zip(columns, minima, maxima)
        },
        "constant_sensors": [name for name, lo, hi in zip(columns, minima, maxima)
                             if name.startswith("sensor_") and lo == hi],
        "errors": errors,
    }


def rul(path, expected_units):
    values, errors = [], []
    for line_no, line in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        if not line.strip():
            continue
        try:
            tokens = line.split()
            if len(tokens) != 1:
                raise ValueError
            value = float(tokens[0])
            if not math.isfinite(value) or value < 0 or not value.is_integer():
                raise ValueError
            values.append(int(value))
        except ValueError:
            errors.append(f"line {line_no}: invalid RUL label")
    if len(values) != expected_units:
        errors.append(f"{len(values)} RUL labels, expected {expected_units}")
    return {"rows": len(values), "min_rul": min(values, default=None),
            "max_rul": max(values, default=None), "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path,
                        default=ROOT / "experiments/configs/inventory.json")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    data_dir = ROOT / config["data_dir"]
    output_dir = ROOT / config["output_dir"]
    files = []
    before = {path.name: digest(path) for path in sorted(data_dir.iterdir()) if path.is_file()}
    for subset, counts in config["subsets"].items():
        for kind in ("train", "test", "RUL"):
            path = data_dir / f"{kind}_{subset}.txt"
            expected = counts["train_units" if kind == "train" else "test_units"]
            result = (rul(path, expected) if kind == "RUL"
                      else trajectory(path, config["columns"], expected))
            files.append({"path": path.relative_to(ROOT).as_posix(), "subset": subset,
                          "kind": kind, "bytes": path.stat().st_size,
                          "sha256": before[path.name], **result})
    after = {path.name: digest(path) for path in sorted(data_dir.iterdir()) if path.is_file()}
    unchanged = before == after
    passed = unchanged and all(not item["errors"] for item in files)
    report = {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": digest(Path(__file__)),
        "config_sha256": digest(args.config),
        "python": sys.version,
        "platform": platform.platform(),
        "raw_files_unchanged": unchanged,
        "passed": passed,
        "columns": config["columns"],
        "files": files,
        "source_manifest": before,
        "notes": [
            "The readme's final sensor index is inconsistent: 26 total columns = 2 identifiers + 3 settings + 21 sensors.",
            "FD004 readme counts are reversed relative to supplied files: train has 249 units, test and RUL have 248.",
            "Unit IDs are local to each subset and train/test partition.",
            "RUL label row i maps to official test unit i; no future sensor trajectory is supplied.",
            "Native RUL is not time to a constructed THC=0.5 threshold.",
            "Constant-sensor summaries are inventory only; feature selection must be fitted on training partitions.",
            "Hashes establish a local baseline, not authenticity against an external source."
        ],
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "inventory.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    with (output_dir / "summary.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=["subset", "kind", "rows", "units",
                                                   "min_cycles", "max_cycles", "errors"])
        writer.writeheader()
        for item in files:
            writer.writerow({key: len(item["errors"]) if key == "errors" else item.get(key, "")
                             for key in writer.fieldnames})
    packages = subprocess.run([sys.executable, "-m", "pip", "freeze"],
                              capture_output=True, text=True, check=True)
    (output_dir / "environment.freeze.txt").write_text(packages.stdout, encoding="utf-8")
    print(f"{'PASS' if passed else 'FAIL'}: {len(files)} data files; raw files unchanged={unchanged}")
    for item in files:
        print(f"{item['subset']} {item['kind']}: {item['rows']} rows, "
              f"{item.get('units', '-')} units, {len(item['errors'])} errors")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
