"""P13.5: full-chain comparison of frozen P13.4 HI indications against M18 (train files only)."""
import hashlib
import importlib.metadata
import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits

import hi_chain_core_13e as core
import pilot_f_uncertainty_10 as p10

ROOT = p10.ROOT
OUT = ROOT / "experiments/artifacts/pilot_hi_chain_13e"
P10 = p10.OUT
P13D = ROOT / "experiments/artifacts/pilot_hi_stabilization_13d"
BOOT_SEED = 20261017
CASES = {"FD001": [83], "FD003": [55]}
SOURCES = ["protocolo_cadeia_hi_13e.md", "hi_chain_core_13e.py", "pilot_hi_chain_13e.py", "test_hi_chain_13e.py",
           "pilot_f_uncertainty_10.py", "pilot_removal_11.py", "pilot_landmark_control_11a.py", "pilot_fd001.py",
           "pilot_fd001_04.py", "pilot_fd001_05.py", "pilot_fd003_06.py", "pilot_hi_trajectory_08.py"]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def integrity():
    records = {}
    for folder in sorted((ROOT / "experiments/artifacts").glob("pilot_*")):
        manifest = folder / "manifest.json"
        if folder == OUT or not manifest.exists():
            continue
        for name, digest in json.loads(manifest.read_text(encoding="utf-8")).items():
            assert sha(folder / name) == digest, (folder.name, name)
        records[folder.name] = sha(manifest)
    return records


def input_files():
    files = [ROOT / "experiments" / name for name in SOURCES]
    files += [P10 / "splits.json", P10 / "quantiles.csv", P13D / "selections.csv", P13D / "selected_vs_m18.csv"]
    files += sorted(P10.glob("predictions_*_complete.csv.gz")) + sorted(P10.glob("quantiles_*.csv"))
    files += sorted(P13D.glob("selected_hi_*.joblib"))
    files += [ROOT / f"CMAPSSData/train_{s}.txt" for s in p10.CONFIG]
    assert not any(p.name.startswith(("test_FD", "RUL_FD")) for p in files)
    return files


def assert_reproduces_p10(tag, result):
    archived = pd.read_csv(P10 / f"predictions_{tag}_complete.csv.gz")
    keys = ["method", "unit", "cycle"]
    a = archived.sort_values(keys).reset_index(drop=True)
    b = result["e_pred"].sort_values(keys).reset_index(drop=True)
    assert len(a) == len(b) and (a[keys].to_numpy() == b[keys].to_numpy()).all(), tag
    for column in ["hi", "h_slope", "predicted_rul", "error"]:
        np.testing.assert_allclose(b[column], a[column], atol=1e-9, rtol=0, err_msg=f"{tag} {column}")
    assert (a.in_domain.to_numpy() == b.in_domain.to_numpy()).all(), tag
    qa = pd.read_csv(P10 / f"quantiles_{tag}.csv").sort_values(["method", "scope", "alpha"]).reset_index(drop=True)
    qb = result["quantiles"].sort_values(["method", "scope", "alpha"]).reset_index(drop=True)
    for column in ["n", "k", "q_abs", "q_late"]:
        np.testing.assert_allclose(qb[column], qa[column], atol=1e-9, rtol=0, err_msg=f"{tag} {column}")


def tagged(frame, **labels):
    out = frame.copy()
    for k, v in labels.items():
        out[k] = v
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=False)
    before = integrity()
    files = input_files()
    start = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=before,
                 inputs={str(p.relative_to(ROOT)): sha(p) for p in files}, rules=core.rules(),
                 alpha=core.ALPHA, reserve=core.RESERVE, tolerance=core.EPS, bootstrap_seed=BOOT_SEED,
                 official_test_or_rul_read=False,
                 packages={n: importlib.metadata.version(n) for n in ["numpy", "pandas", "scikit-learn", "scipy", "joblib"]})
    (OUT / "execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    for name in SOURCES:
        (OUT / f"source_{name}").write_bytes((ROOT / "experiments" / name).read_bytes())

    splits = json.loads((P10 / "splits.json").read_text(encoding="utf-8"))
    selections = pd.read_csv(P13D / "selections.csv")
    flags = pd.read_csv(P13D / "selected_vs_m18.csv")[["subset", "repeat", "fold", "max_tail_worsened"]]
    train = {s: p10.read_inputs("train", s) for s in p10.CONFIG}
    all_decisions, all_events, all_bands, all_scores, all_quantiles, provenance = [], [], [], [], [], []
    for sp in splits:
        subset, repeat, fold = sp["subset"], sp["repeat"], sp["fold"]
        tag = f"{subset}_r{repeat}_f{fold}"
        seed = p10.SEEDS[repeat-1]
        assert seed == sp["seed"]
        take = lambda ids: train[subset].loc[train[subset].unit.isin(ids)].reset_index(drop=True)
        groups = [set(sp[k]) for k in ["fit", "converter", "uncertainty", "evaluation"]]
        assert all(a.isdisjoint(b) for i, a in enumerate(groups) for b in groups[i+1:])
        u_inputs, e_inputs = take(sp["uncertainty"]), take(sp["evaluation"])

        m18 = p10.fit_pipeline(take(sp["fit"]), take(sp["converter"]), subset, seed)
        m18_result = core.calibrate_and_evaluate(m18, u_inputs, e_inputs, sp["uncertainty"], sp["evaluation"])
        assert_reproduces_p10(tag, m18_result)

        choice = selections.loc[selections.subset.eq(subset) & selections.repeat.eq(repeat) & selections.fold.eq(fold)].iloc[0]
        selected = joblib.load(P13D / f"selected_hi_{tag}.joblib")
        assert selected["candidate"] == choice.selected and selected["subset"] == subset
        assert sorted(selected["fit_units"]) == sorted(sp["fit"])
        assert sorted(selected["selection_development"]) == sorted(sp["fit"]+sp["converter"])
        assert set(selected["selection_development"]).isdisjoint(sp["uncertainty"]+sp["evaluation"])
        if choice.selected == "M18":
            np.testing.assert_allclose(selected["effective"], core.m18_effective(m18["health"]), atol=1e-8, rtol=1e-7)
            sel_result, sel_bundle = m18_result, m18
        else:
            health = core.weights_health(selected["effective"], subset, sp["fit"], choice.selected)
            sel_bundle = core.fit_converters(health, take(sp["converter"]), subset, seed)
            sel_result = core.calibrate_and_evaluate(sel_bundle, u_inputs, e_inputs, sp["uncertainty"], sp["evaluation"])
        joblib.dump(sel_bundle, OUT / f"sel_models_{tag}.joblib", compress=3)
        sel_result["quantiles"].to_csv(OUT / f"sel_quantiles_{tag}.csv", index=False)
        sel_result["e_pred"].to_csv(OUT / f"sel_predictions_{tag}_E.csv.gz", index=False, compression="gzip")
        sel_result["u_pred"].to_csv(OUT / f"sel_predictions_{tag}_U.csv.gz", index=False, compression="gzip")
        labels = dict(subset=subset, repeat=repeat, fold=fold)
        provenance.append(labels | dict(selected=choice.selected, selection_eligible=bool(choice.selection_eligible),
                                        contingency_ineligible=bool(not choice.selection_eligible),
                                        sel_identical_to_m18=bool(choice.selected == "M18"),
                                        sel_models_sha256=sha(OUT / f"sel_models_{tag}.joblib"),
                                        sel_quantiles_sha256=sha(OUT / f"sel_quantiles_{tag}.csv"),
                                        frozen_utc=datetime.now(timezone.utc).isoformat()))
        for chain, result in [("M18", m18_result), ("SEL", sel_result)]:
            meta = labels | dict(chain=chain, candidate="M18" if chain == "M18" else choice.selected)
            frame = core.decisions(result["e_pred"], result["quantiles"], result["endpoints"])
            all_decisions.append(tagged(frame, **meta))
            all_events.append(tagged(result["events"], **meta))
            all_bands.append(tagged(result["bands"], **meta))
            all_scores.append(tagged(result["u_scores"], dataset="calibration", **meta))
            all_scores.append(tagged(result["scores"], dataset="evaluation", **meta))
            all_quantiles.append(tagged(result["quantiles"], **meta))
        print(f"{tag}: M18 reproduced; SEL={choice.selected}", flush=True)
    (OUT / "provenance.json").write_text(json.dumps(provenance, indent=2), encoding="utf-8")

    decisions = pd.concat(all_decisions, ignore_index=True)
    events = pd.concat(all_events, ignore_index=True)
    bands = pd.concat(all_bands, ignore_index=True)
    ranges = core.between_repeat_ranges(decisions)
    differences = core.chain_differences(decisions, flags)
    cases = decisions.loc[[u in CASES[s] for s, u in zip(decisions.subset, decisions.unit)]]
    outputs = {"decisions": decisions, "events": events, "bands": bands,
               "scores": pd.concat(all_scores, ignore_index=True), "quantiles": pd.concat(all_quantiles, ignore_index=True),
               "decision_summary": core.decision_summary(decisions), "prognosis_summary": core.prognosis_summary(events, bands),
               "ranges": ranges, "range_summary": core.range_summary(ranges, BOOT_SEED),
               "contrasts": core.paired_contrasts(decisions, events, BOOT_SEED),
               "chain_differences": differences, "tail_summary": core.tail_summary(differences),
               "cases": cases[["subset", "repeat", "fold", "chain", "candidate", "unit", "endpoint", "policy_id",
                               "usable_marker", "decision", "scheduled", "status", "utilised"]]}
    for name, frame in outputs.items():
        frame.to_csv(OUT / f"{name}.csv", index=False)
    assert integrity() == before
    assert all(sha(ROOT / k) == v for k, v in start["inputs"].items())
    metadata = start | dict(finished_utc=datetime.now(timezone.utc).isoformat(), previous_manifests_intact=True,
                            partitions=len(splits), decision_rows=len(decisions), m18_reproduced_p10=True,
                            new_selection_in_C_U_E=False, inspections=False, reserve_reduction=False)
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                   if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")
    print(outputs["range_summary"].to_string(index=False))


if __name__ == "__main__":
    with threadpool_limits(limits=1):
        main()
