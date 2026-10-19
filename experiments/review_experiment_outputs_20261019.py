"""Review archived aggregate results and reproduce the three-arm cost table.

No fitting, new policy selection, raw C-MAPSS reads or simulation is performed.
The public evidence_inputs directory supports reproducing the same summaries
without the private project's large archived outputs.
"""
from pathlib import Path
import hashlib
import json
import shutil

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "experiments/artifacts"
OUT = ROOT / "experiments/results_review_2026-10-19"
EVIDENCE = OUT / "evidence_inputs"
INPUTS = {}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(folder, filename):
    original = ARCHIVE / folder / filename
    packaged = EVIDENCE / folder / filename
    path = original if original.exists() else packaged
    frame = pd.read_csv(path)
    INPUTS[f"{folder}/{filename}"] = dict(sha256=sha(path), rows=len(frame))
    if path == original:
        packaged.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(original, packaged)
    return frame


def contrast_records(frame, folder, filename, estimate, low, high, direction, metric):
    records = []
    for _, row in frame.iterrows():
        delta, lower, upper = float(row[estimate]), float(row[low]), float(row[high])
        assert np.isfinite([delta, lower, upper]).all()
        gain = -delta if direction == "lower" else delta
        favourable = upper < 0 if direction == "lower" else lower > 0
        unfavourable = lower > 0 if direction == "lower" else upper < 0
        status = ("favourable_descriptive_interval" if favourable else
                  "unfavourable_descriptive_interval" if unfavourable else
                  "point_gain_interval_includes_zero" if gain > 0 else
                  "no_point_gain_interval_includes_zero")
        context = {k: v for k, v in row.items() if k not in [estimate, low, high]}
        records.append(dict(experiment=folder, source=filename, metric=metric,
                            preferred_direction=direction, estimate=delta,
                            ci_low=lower, ci_high=upper, status=status,
                            context=json.dumps(context, ensure_ascii=True)))
    return records


def main():
    OUT.mkdir(exist_ok=True)
    inventory = []
    excluded = {"inventory", "confirmation_19a_ensaio", "pilot_twenty_year_20a_failed_run1",
                "pilot_break_even_21a", "pilot_break_even_cost_21b", "pilot_break_even_cost_21b_failed_run1"}
    if ARCHIVE.exists():
        folders = [p for p in sorted(ARCHIVE.iterdir()) if p.is_dir() and p.name not in excluded]
        for folder in folders:
            for path in sorted(folder.iterdir()):
                if path.name in ["conclusoes.md", "relatorio.md", "metadata.json", "verification.json"] or (
                    path.suffix == ".csv" and any(k in path.stem for k in ["summary", "contrasts", "bootstrap", "comparison"])):
                    inventory.append(dict(experiment=folder.name, file=path.name,
                                          bytes=path.stat().st_size, sha256=sha(path)))
        pd.DataFrame(inventory).to_csv(OUT / "reviewed_source_inventory.csv", index=False)
        assert len(folders) == 32

    specifications = [
        ("pilot_fd001_05", "bootstrap.csv", "difference", "p025", "p975", "lower", "RMSE"),
        ("pilot_fd003_06", "bootstrap.csv", "difference", "p025", "p975", "lower", "RMSE"),
        ("pilot_hi_landmark_07", "paired_comparisons.csv", "delta_rmse_b_minus_a", "ci_low", "ci_high", "lower", "RMSE"),
        ("pilot_hi_trajectory_08", "contrasts.csv", "delta_rmse", "ci_low", "ci_high", "lower", "RMSE"),
        ("pilot_f_uncertainty_09", "contrasts.csv", "delta_rmse", "ci_low", "ci_high", "lower", "RMSE"),
        ("pilot_f_uncertainty_10", "contrasts.csv", "delta_rmse", "ci_low", "ci_high", "lower", "RMSE"),
    ]
    records = []
    for folder, name, estimate, low, high, direction, metric in specifications:
        frame = load(folder, name)
        records.extend(contrast_records(frame, folder, name, estimate, low, high, direction, metric))
    for folder in ["pilot_removal_11", "pilot_landmark_control_11a", "pilot_policy_selection_13a"]:
        frame = load(folder, "contrasts.csv")
        for estimate, low, high, metric in [
            ("delta_mean_life", "life_ci_low", "life_ci_high", "utilised_life"),
            ("relative_saving", "saving_ci_low", "saving_ci_high", "relative_restoration_saving"),
        ]:
            records.extend(contrast_records(frame, folder, "contrasts.csv", estimate, low, high, "higher", metric))
    chain = load("pilot_hi_chain_13e", "contrasts.csv")
    for measure, direction in [("mean_utilised", "higher"), ("mark_rmse", "lower")]:
        records.extend(contrast_records(chain.loc[chain.measure.eq(measure)],
                                        "pilot_hi_chain_13e", "contrasts.csv", "delta",
                                        "ci_low", "ci_high", direction, measure))
    ledger = pd.DataFrame(records)
    ledger.to_csv(OUT / "contrast_ledger.csv", index=False)

    early = load("pilot_fd001_02", "decision_summary.csv")
    a = early.loc[early.variant.eq("global_gate30")].set_index("model")
    b = early.loc[early.variant.eq("local_gate30")].set_index("model")
    gain = b.mean_exposure - a.mean_exposure
    assert np.isclose(gain.min(), 4.47) and np.isclose(gain.max(), 6.94)
    assert a.endpoints.eq(0).all() and b.endpoints.eq(0).all()
    pd.DataFrame(dict(global_region_life=a.mean_exposure, local_region_life=b.mean_exposure,
                      gain_cycles=gain, global_region_events=a.endpoints,
                      local_region_events=b.endpoints)).to_csv(OUT / "early_margin_gains.csv")

    history = load("pilot_hi_trajectory_08", "contrasts.csv")
    sensor = history.loc[history.subset.eq("FD003") & history.event.eq("landmark") &
                         history.method_a.eq("RF:SENSOR_MEAN") & history.method_b.eq("RF:SENSOR_FULL")]
    assert len(sensor) == 2 and sensor.ci_high.lt(0).all()
    sensor.to_csv(OUT / "direct_sensor_gains.csv", index=False)

    bands = load("pilot_f_uncertainty_09", "band_summary.csv")
    temporal = bands.loc[bands.subset.eq("FD003") & bands.dataset.eq("complete") &
                         bands.method.eq("RF_SLOPE") & bands.alpha.eq(.1)]
    assert len(temporal) == 6
    temporal.to_csv(OUT / "point_vs_path_calibration.csv", index=False)
    load("pilot_hi_stabilization_13d", "summary.csv").to_csv(OUT / "internal_stabilisation.csv", index=False)
    load("pilot_hi_chain_13e", "prognosis_summary.csv").to_csv(OUT / "chain_prognosis.csv", index=False)
    load("pilot_removal_11", "summary.csv").to_csv(OUT / "removal_sensitivities.csv", index=False)
    load("confirmation_19a", "summary.csv").to_csv(OUT / "confirmation_sensitivities.csv", index=False)
    load("pilot_inspection_17b", "summary.csv").to_csv(OUT / "inspection_scenarios.csv", index=False)
    load("pilot_hi_trajectory_08", "summary.csv")
    load("pilot_hi_landmark_07", "summary.csv")

    source = ARCHIVE / "pilot_twenty_year_20a/cells.csv.gz"
    packaged = EVIDENCE / "pilot_twenty_year_20a/cells_central.csv"
    if source.exists():
        source_hash = sha(source)
        cells = pd.read_csv(source)
        central = cells.loc[cells.L_ref.eq(8425) & cells.u_yr.eq(1600) & cells.llp.eq(20000) &
                            cells.ic.eq(1) & cells.rho.eq(1) & cells.arm.str.endswith("_D1")].copy()
        packaged.parent.mkdir(parents=True, exist_ok=True)
        central.to_csv(packaged, index=False)
        assert sha(source) == source_hash
    else:
        central = pd.read_csv(packaged)
        source_hash = None
    INPUTS["pilot_twenty_year_20a/cells_central.csv"] = dict(
        sha256=sha(packaged), rows=len(central), selection="central scenario, execution lead 1",
        original_cells_sha256=source_hash)
    central["events"] = central[["miss_mean", "exact_mean", "late_mean"]].sum(axis=1)
    selected = central.loc[central.arm.isin([
        "AGE127_D1", "PHM_ISO_LOWER98_M15_D1", "HYB_ISO_LOWER98_M15_D1"])].copy()
    assert len(selected) == 36
    selected["cost_musd_5"] = 5 * selected.tot_mean
    selected["cost_musd_6"] = 6 * selected.tot_mean
    selected["cost_musd_7"] = 7 * selected.tot_mean
    costs = selected.groupby(["subset", "arm"])[
        ["tot_mean", "events", "cost_musd_5", "cost_musd_6", "cost_musd_7"]].mean()
    costs.to_csv(OUT / "long_term_restoration_costs.csv")
    scale = selected.groupby("subset").k.first().to_frame("flight_cycles_per_simulated_cycle")
    scale["age_gate_flight_cycles"] = 127 * scale.flight_cycles_per_simulated_cycle
    scale.to_csv(OUT / "cycle_scale.csv")

    manifest = dict(scope="post-confirmation review of archived aggregate results; no refitting or simulation",
                    script_sha256=sha(Path(__file__)), inputs=INPUTS,
                    contrasts=len(ledger), experimental_series=32,
                    outputs={p.name: sha(p) for p in sorted(OUT.glob("*.csv"))})
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("Experimental series: 32; directional contrast records:", len(ledger))
    print(ledger.groupby(["metric", "status"]).size().to_string())
    print(costs[["tot_mean", "cost_musd_6"]].round(4).to_string())


if __name__ == "__main__":
    main()
