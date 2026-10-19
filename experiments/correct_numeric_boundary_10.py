"""Rebuild only P10 reserve diagnostics with a 1e-9-cycle comparison tolerance."""

import json
from datetime import datetime, timezone

import numpy as np
import pandas as pd

import pilot_f_uncertainty_10 as p10


def main():
    out = p10.OUT
    assert not (out / "amendment_numeric_boundary.json").exists(), "Amendment already applied"
    original = pd.read_csv(out / "before_numeric_amendment_reserves.csv")
    scores = pd.read_csv(out / "scores.csv")
    quantiles = pd.read_csv(out / "quantiles.csv")
    frames = []
    for split in json.loads((out / "splits.json").read_text(encoding="utf-8")):
        subset, repeat, fold = split["subset"], split["repeat"], split["fold"]
        q = quantiles.loc[quantiles.subset.eq(subset) & quantiles.repeat.eq(repeat) & quantiles.fold.eq(fold)]
        for dataset in ["complete"]+(["truncated"] if fold == 1 else []):
            pred = pd.read_csv(out / f"predictions_{subset}_r{repeat}_f{fold}_{dataset}.csv.gz")
            s = scores.loc[scores.subset.eq(subset) & scores.repeat.eq(repeat) & scores.fold.eq(fold) & scores.dataset.eq(dataset)]
            frame = p10.reserve_diagnostics(pred, s, q)
            frame["subset"], frame["dataset"], frame["repeat"], frame["fold"] = subset, dataset, repeat, fold
            frames.append(frame)
    revised = pd.concat(frames, ignore_index=True)
    pd.testing.assert_frame_equal(original.drop(columns=["mark_available", "cycle_fraction", "any_available"]),
                                  revised.drop(columns=["mark_available", "cycle_fraction", "any_available"]), check_dtype=False)
    changes = {}
    for col in ["mark_available", "any_available", "cycle_fraction"]:
        a, b = original[col].fillna(-1).to_numpy(dtype=float), revised[col].fillna(-1).to_numpy(dtype=float)
        changes[col] = dict(changed_rows=int(np.sum(abs(a-b) > 1e-12)), max_difference=float(max(abs(a-b))))
    revised.to_csv(out / "reserves.csv", index=False)
    p10.reserve_summary(revised).to_csv(out / "reserve_summary.csv", index=False)
    unchanged = {p.name: p10.sha(p) for p in out.iterdir() if p.name.startswith(("models_", "predictions_", "quantiles_"))}
    current_files = ["pilot_f_uncertainty_10.py", "verify_pilot_f_uncertainty_10.py", "test_pilot_f_uncertainty_10.py",
                     "protocolo_incerteza_f_10.md", "correct_numeric_boundary_10.py"]
    record = dict(timestamp_utc=datetime.now(timezone.utc).isoformat(), reason="Floating-point equality at reserve+delay",
                  tolerance_cycles=1e-9, refitted_models=False, changes=changes,
                  unchanged_frozen_files=unchanged,
                  current_sources={f"experiments/{name}": p10.sha(p10.ROOT / "experiments" / name) for name in current_files})
    (out / "amendment_numeric_boundary.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    p10.refresh_manifest()
    print(json.dumps(changes))


if __name__ == "__main__":
    main()
