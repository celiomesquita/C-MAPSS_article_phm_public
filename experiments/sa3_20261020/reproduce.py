"""Separate calibration and reserve effects in archived P11 ISO decisions."""

import csv
import hashlib
import json
import math
import statistics
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "reproduced"
INPUTS = {
    "decisions": ROOT / "evidence_inputs/decisions.csv",
    "summary": ROOT / "evidence_inputs/summary.csv",
    "marker": ROOT / "evidence_inputs/controls.csv",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def write_csv(name, rows):
    with (OUT / name).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def metrics(rows):
    exposure = 0.0
    late = exact = missing = 0
    for row in rows:
        endpoint = float(row["endpoint"])
        has_decision = row["has_decision"] == "True"
        if has_decision:
            scheduled = float(row["scheduled"])
            assert scheduled == float(row["decision"]) + int(row["delay"])
            late += scheduled > endpoint
            exact += scheduled == endpoint
            utilised = min(scheduled, endpoint)
        else:
            missing += 1
            utilised = endpoint
        assert utilised == float(row["utilised"])
        exposure += utilised
        assert (row["late"] == "True") == (has_decision and float(row["scheduled"]) > endpoint)
        assert (row["exact_endpoint"] == "True") == (has_decision and float(row["scheduled"]) == endpoint)
        assert (row["reached_endpoint"] == "True") == (not has_decision or float(row["scheduled"]) >= endpoint)
    return dict(n=len(rows), mean_life=exposure / len(rows),
                restorations_per_10000=10000 * len(rows) / exposure,
                strict_late=late, exact=exact, missing=missing, events=late + exact + missing)


def main():
    hashes = {name: sha(path) for name, path in INPUTS.items()}
    groups = defaultdict(dict)
    for row in read_csv(INPUTS["decisions"]):
        if row["dataset"] == "complete" and row["method"] == "ISO" and row["anchor"] == "lower":
            key = (row["subset"], int(row["repeat"]), int(row["delay"]),
                   round(100 * (1 - float(row["alpha"]))), int(row["reserve"]))
            unit = int(row["unit"])
            assert unit not in groups[key]
            groups[key][unit] = row
    assert len(groups) == 48 and all(len(group) == 100 for group in groups.values())
    stored = {(row["subset"], int(row["repeat"]), row["policy_id"]): row
              for row in read_csv(INPUTS["summary"]) if row["dataset"] == "complete"}
    markers = defaultdict(dict)
    for row in read_csv(INPUTS["marker"]):
        if row["dataset"] == "complete":
            key = (row["subset"], int(row["repeat"]), int(row["delay"]))
            unit = int(row["unit"])
            assert unit not in markers[key]
            markers[key][unit] = row
    cells = []
    calculated = {}
    for key, group in sorted(groups.items()):
        subset, repeat, delay, level, reserve = key
        value = metrics(list(group.values()))
        saved = stored[(subset, repeat, f"ISO_LOWER{level}_M{reserve}_D{delay}")]
        for field, original in [("mean_life", "mean_utilised"),
                                ("restorations_per_10000", "restorations_per_10000_cycles"),
                                ("strict_late", "late_count"), ("exact", "exact_count"),
                                ("missing", "without_decision"), ("events", "reached_count")]:
            assert math.isclose(value[field], float(saved[original]), abs_tol=1e-10)
        calculated[key] = value
        cells.append(dict(subset=subset, repeat=repeat, delay=delay, level=level, reserve=reserve, **value))
    effects = []
    marker_rows = []
    definitions = [
        ("calibration_M15", (95, 15), (98, 15)),
        ("calibration_M12", (95, 12), (98, 12)),
        ("reserve_L98", (98, 12), (98, 15)),
        ("reserve_L95", (95, 12), (95, 15)),
        ("joint", (95, 12), (98, 15)),
    ]
    bases = sorted({key[:3] for key in groups})
    for base in bases:
        subset, repeat, delay = base
        reference = groups[base + (98, 15)]
        marker = markers[base]
        assert set(reference) == set(marker) == set(range(1, 101))
        marker_value = metrics(list(marker.values()))
        marker_rows.append(dict(subset=subset, repeat=repeat, delay=delay,
                                marker_mean_life=marker_value["mean_life"],
                                combined_gain_over_marker=calculated[base + (95, 12)]["mean_life"]
                                - marker_value["mean_life"]))
        for name, a, b in definitions:
            left, right = groups[base + a], groups[base + b]
            assert set(left) == set(right) == set(reference)
            for unit in left:
                for field in ["fold", "endpoint", "first_available"]:
                    assert left[unit][field] == right[unit][field] == reference[unit][field] == marker[unit][field]
            paired_life = statistics.mean(float(left[unit]["utilised"]) - float(right[unit]["utilised"])
                                          for unit in sorted(left))
            va, vb = calculated[base + a], calculated[base + b]
            assert math.isclose(paired_life, va["mean_life"] - vb["mean_life"], abs_tol=1e-10)
            row = dict(subset=subset, repeat=repeat, delay=delay, contrast=name,
                       arm_a=f"L{a[0]}_M{a[1]}", arm_b=f"L{b[0]}_M{b[1]}", n=100)
            row.update({"delta_" + field: va[field] - vb[field] for field in va if field != "n"})
            row["delta_mean_life"] = paired_life
            effects.append(row)
        interaction = dict(subset=subset, repeat=repeat, delay=delay, contrast="interaction",
                           arm_a="(L95_M12-L98_M12)", arm_b="(L95_M15-L98_M15)", n=100)
        for field in calculated[base + (98, 15)]:
            if field != "n":
                interaction["delta_" + field] = (calculated[base + (95, 12)][field]
                    - calculated[base + (98, 12)][field] - calculated[base + (95, 15)][field]
                    + calculated[base + (98, 15)][field])
        effects.append(interaction)
    assert len(effects) == 72 and len(marker_rows) == 12
    assert all(sha(path) == hashes[name] for name, path in INPUTS.items())
    OUT.mkdir(parents=True, exist_ok=True)
    write_csv("cells.csv", cells)
    write_csv("contrasts.csv", effects)
    write_csv("marker.csv", marker_rows)
    manifest = dict(action="SA3-02", recorded_utc=datetime.now(timezone.utc).isoformat(),
                    analysis="Exploratory paired contrasts of archived decisions; no model fitting or simulation",
                    inference="Descriptive; no confidence intervals, pooled repetitions or population-risk claim",
                    inputs={str(INPUTS[name].relative_to(ROOT)): digest for name, digest in hashes.items()},
                    script_sha256=sha(Path(__file__)), cells_checked_against_P11=48,
                    archived_decisions_checked=4800, marker_decisions_checked=1200, contrasts=72,
                    inputs_unchanged=True, status="passed",
                    outputs={name: sha(OUT / name) for name in ["cells.csv", "contrasts.csv", "marker.csv"]})
    (OUT / "verification.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))
    for subset in ["FD001", "FD003"]:
        for delay in [1, 2]:
            print(subset, "delay", delay)
            for contrast in [entry[0] for entry in definitions] + ["interaction"]:
                rows = [row for row in effects if row["subset"] == subset and row["delay"] == delay
                        and row["contrast"] == contrast]
                print(contrast, "life", [round(row["delta_mean_life"], 4) for row in rows],
                      "restorations", [round(row["delta_restorations_per_10000"], 4) for row in rows])


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    OUT = parser.parse_args().output
    main()
