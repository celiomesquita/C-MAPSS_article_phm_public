"""P08 post-processing correction: rank again on common sensors before correlation."""

import json
from datetime import datetime, timezone

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

import pilot_hi_trajectory_08 as p08


def main():
    out = p08.OUT
    meta = json.loads((out / "metadata.json").read_text(encoding="utf-8"))
    snapshot = out / "pilot_hi_trajectory_08_executed.py"
    executed_digest = next(digest for name, digest in meta["inputs"].items() if name.replace("\\", "/") == "experiments/pilot_hi_trajectory_08.py")
    assert p08.sha(snapshot) == executed_digest
    assert p08.source_integrity() == meta["sources"]
    # Only the rank-correlation definition may differ from the executed script.
    expected = snapshot.read_text(encoding="utf-8").replace(
        'joined.iloc[:, 0].corr(joined.iloc[:, 1])',
        'joined.iloc[:, 0].corr(joined.iloc[:, 1], method="spearman")')
    current = p08.ROOT / "experiments/pilot_hi_trajectory_08.py"
    assert current.read_text(encoding="utf-8") == expected
    importance = pd.read_csv(out / "importance.csv")
    ranks, corrected = p08.importance_ranks(importance)
    for r in corrected.itertuples():
        group = ranks.loc[ranks.subset.eq(r.subset) & ranks.dataset.eq(r.dataset) & ranks.representation.eq(r.representation)]
        a = group.loc[group.run.eq(r.run_a) & group.method.eq(r.method_a)].set_index("group").delta_mse
        b = group.loc[group.run.eq(r.run_b) & group.method.eq(r.method_b)].set_index("group").delta_mse
        common = a.index.intersection(b.index)
        expected_value = spearmanr(a.loc[common], b.loc[common]).statistic
        np.testing.assert_allclose(r.spearman, expected_value, atol=1e-12)
    before = pd.read_csv(out / "rank_concordance_before_correction.csv")
    changed = ~np.isclose(before.spearman, corrected.spearman, atol=1e-12, equal_nan=True)
    corrected.to_csv(out / "rank_concordance.csv", index=False)
    record = dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),
                  reason="Common-sensor intersection can omit sensors, so Pearson correlation of the original full-set ranks is not always Spearman on the intersection. Re-rank within the common set.",
                  stage="after the initial results and full verification; post-processing only",
                  initial_attempt="Stopped before mutation because Windows metadata keys use backslashes; path matching corrected.",
                  hi_refitted=False, predictions_changed=False, errors_changed=False,
                  training_or_selection_changed=False, correlations_checked=len(corrected),
                  correlations_changed=int(changed.sum()), maximum_absolute_change=float(np.max(abs(before.spearman-corrected.spearman))),
                  executed_script_sha256=p08.sha(snapshot), corrected_script_sha256=p08.sha(current),
                  before_concordance_sha256=p08.sha(out / "rank_concordance_before_correction.csv"),
                  corrected_concordance_sha256=p08.sha(out / "rank_concordance.csv"),
                  prior_verification_sha256=p08.sha(out / "verification_before_rank_correction.json"),
                  correction_script_sha256=p08.sha(p08.ROOT / "experiments/correct_rank_concordance_08.py"))
    (out / "rank_correction.json").write_text(json.dumps(record, indent=2), encoding="utf-8")
    verification = json.loads((out / "verification_before_rank_correction.json").read_text(encoding="utf-8"))
    verification["rank_postprocessing_correction"] = record
    verification["original_manifests_intact"] = p08.source_integrity() == meta["sources"]
    (out / "verification.json").write_text(json.dumps(verification, indent=2), encoding="utf-8")
    p08.refresh_manifest()
    print(json.dumps(record))


if __name__ == "__main__":
    main()
