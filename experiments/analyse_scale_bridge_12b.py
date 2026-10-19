"""Descriptive summaries of P12.2 outputs (post-run; no new simulation)."""
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "experiments/artifacts/pilot_scale_bridge_12b"
POL = ["AGE_D1", "HI_MARKER_D1", "HI_THRESHOLD_SELECTED_D1", "HI_WAIT_SELECTED_D1", "ISO_LOWER98_M15_D1", "RF_SLOPE_LOWER98_M15_D1",
       "ISO_POINT_M15_D1", "RF_SLOPE_POINT_M15_D1"]


def main():
    c = pd.read_csv(OUT / "cells.csv.gz")
    k = pd.read_csv(OUT / "kendall.csv.gz")
    p = pd.read_csv(OUT / "pairs.csv.gz")
    cen = c[(c.L_ref == 8425) & (c.u_yr == 1600) & (c.llp == 20000) & (c.ic == 1) & (c.rho == 1.0) & (c.policy_id.isin(POL))]
    cen = cen.groupby(["subset", "policy_id"]).agg(k=("k", "first"), horizon_fc=("horizon_fc", "first"), d_visits=("d_mean", "mean"),
                                                 llp_visits=("l_mean", "mean"), total_visits=("tot_mean", "mean"),
                                                 miss=("miss_mean", "mean"), exact=("exact_mean", "mean"), late=("late_mean", "mean")).reset_index()
    age = cen[cen.policy_id == "AGE_D1"].set_index("subset").total_visits
    cen["saving_vs_age"] = 1 - cen.total_visits / cen.subset.map(age)
    cen["cost_usd_millions_6m"] = cen.total_visits * 6.0
    cen.to_csv(OUT / "summary_central.csv", index=False)
    a = c[(c.u_yr == 1600) & (c.rho == 1.0) & (c.policy_id.isin(["AGE_D1", "ISO_LOWER98_M15_D1"]))].pivot_table(
        index=["subset", "llp", "ic", "L_ref"], columns="policy_id", values="tot_mean")
    a["saving_vs_age"] = 1 - a["ISO_LOWER98_M15_D1"] / a["AGE_D1"]
    a.reset_index().to_csv(OUT / "summary_saving_by_lref.csv", index=False)
    m = c[c.policy_id.isin(["ISO_LOWER98_M15_D1", "HI_MARKER_D1"])].pivot_table(
        index=["subset", "repeat", "L_ref", "u_yr", "llp", "ic", "rho"], columns="policy_id", values="tot_mean")
    m["relative_diff"] = (m["ISO_LOWER98_M15_D1"] - m["HI_MARKER_D1"]) / m["HI_MARKER_D1"]
    m.groupby("subset").relative_diff.describe().to_csv(OUT / "summary_iso_vs_marker_relative.csv")
    k["k_band"] = pd.cut(k.k, [0, 30, 50, 80, 1000], labels=["<30", "30-50", "50-80", ">80"])
    rows = [k.groupby(f, observed=True).kendall_tau.agg(["mean", "min", "count"]).assign(factor=f).reset_index().rename(columns={f: "level"})
            for f in ["subset", "k_band", "llp", "ic", "rho", "u_yr"]]
    pd.concat(rows).to_csv(OUT / "summary_kendall.csv", index=False)
    ic0 = c[(c.llp == 0) & (c.ic == 0) & (c.rho == 1.0) & (c.policy_id == "ISO_LOWER98_M15_D1")]
    ic0 = ic0.assign(edge_ratio=ic0.tot_mean / ic0.expected_stationary).groupby(["subset", "L_ref"]).edge_ratio.mean().reset_index()
    ic0.to_csv(OUT / "summary_edge_ic0.csv", index=False)
    inv = p[p.status == "invertido"]
    inv.assign(abs_analytic=inv.analytic_diff.abs()).groupby(["a", "b"]).abs_analytic.describe().to_csv(OUT / "summary_inverted_analytic_gap.csv")
    print(cen.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
