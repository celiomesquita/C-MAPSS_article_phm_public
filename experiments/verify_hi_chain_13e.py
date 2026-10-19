"""Independent P13.5 verification: raw-sensor HI, features, predictions, quantiles, decisions and summaries."""
import hashlib
import json
import math
from pathlib import Path

import joblib
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "experiments/artifacts/pilot_hi_chain_13e"
P10 = ROOT / "experiments/artifacts/pilot_f_uncertainty_10"
P11 = ROOT / "experiments/artifacts/pilot_removal_11"
P11A = ROOT / "experiments/artifacts/pilot_landmark_control_11a"
P11B = ROOT / "experiments/artifacts/pilot_loss_decomposition_11b"
P13D = ROOT / "experiments/artifacts/pilot_hi_stabilization_13d"
SENSORS = [f"s{i}" for i in range(1, 22)]
TOL = 1e-9


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def raw(subset):
    names = ["unit", "cycle", "op1", "op2", "op3"] + SENSORS
    return pd.read_csv(ROOT / f"CMAPSSData/train_{subset}.txt", sep=r"\s+", header=None, names=names)


def engine_hi(g, weights):
    """Causal 15-cycle mean, centred at cycle 20; HI from cycle 20; slope over 20 HI values."""
    x = g[SENSORS].to_numpy(float)
    c = np.cumsum(np.vstack([np.zeros(21), x]), axis=0)
    means = np.full_like(x, np.nan)
    means[14:] = (c[15:]-c[:-15])/15
    cycles = g.cycle.to_numpy()
    i20 = int(np.flatnonzero(cycles == 20)[0])
    hi = np.clip(1-(means[i20:]-means[i20])@weights, 0, 1)
    u = np.arange(20)-9.5
    slope = np.full(len(hi), np.nan)
    if len(hi) >= 20:
        slope[19:] = np.convolve(hi, u[::-1], mode="valid")/np.sum(u*u)
    return cycles[i20:], hi, slope


def m18_weights(tag):
    h = joblib.load(P10 / f"models_{tag}.joblib")["health"]
    w = np.zeros(21)
    for sensor, b, d, s in zip(h["stats"]["channels"], h["beta"], h["stats"]["direction"], h["stats"]["scale"]):
        w[SENSORS.index(sensor)] = b*d/s
    return w


def own_quantile(values, alpha):
    a = np.sort(np.asarray(values, float))
    k = math.ceil((len(a)+1)*(1-alpha))
    return float(a[k-1]) if k <= len(a) else float("inf")


def own_decide(rows, endpoint, q, m, d):
    rows = rows.loc[rows.in_domain & rows.cycle.lt(endpoint)].sort_values("cycle")
    if m == 0:
        return float(rows.cycle.iloc[0]) if len(rows) else np.nan
    hit = rows.loc[np.maximum(0., rows.predicted_rul-q) <= m+d+TOL]
    return float(hit.cycle.iloc[0]) if len(hit) else np.nan


def main():
    checks = {}
    for folder in sorted((ROOT / "experiments/artifacts").glob("pilot_*")):
        if (folder / "manifest.json").exists():
            for name, digest in json.loads((folder / "manifest.json").read_text(encoding="utf-8")).items():
                assert sha(folder / name) == digest, (folder.name, name)
    checks["manifests_intact"] = True
    start = json.loads((OUT / "execution_start.json").read_text(encoding="utf-8"))
    assert not any(("test_FD" in k) or ("RUL_FD" in k) for k in start["inputs"])
    checks["official_test_or_rul_inputs"] = 0

    splits = json.loads((P10 / "splits.json").read_text(encoding="utf-8"))
    selections = pd.read_csv(P13D / "selections.csv").set_index(["subset", "repeat", "fold"])
    decisions = pd.read_csv(OUT / "decisions.csv")
    scores = pd.read_csv(OUT / "scores.csv")
    quantiles = pd.read_csv(OUT / "quantiles.csv")
    data = {s: raw(s) for s in ["FD001", "FD003"]}
    rebuilt, max_hi, max_pred, max_q = [], 0., 0., 0.
    for sp in splits:
        subset, repeat, fold = sp["subset"], sp["repeat"], sp["fold"]
        tag = f"{subset}_r{repeat}_f{fold}"
        selected = selections.loc[(subset, repeat, fold), "selected"]
        sel_model = joblib.load(P13D / f"selected_hi_{tag}.joblib")
        weights = {"M18": m18_weights(tag), "SEL": m18_weights(tag) if selected == "M18" else sel_model["effective"]}
        sources = {"M18": (P10 / f"predictions_{tag}_complete.csv.gz", P10 / f"predictions_{tag}_U.csv.gz"),
                   "SEL": (OUT / f"sel_predictions_{tag}_E.csv.gz", OUT / f"sel_predictions_{tag}_U.csv.gz")}
        bundle = joblib.load(OUT / f"sel_models_{tag}.joblib") if selected != "M18" else joblib.load(P10 / f"models_{tag}.joblib")
        for chain in ["M18", "SEL"]:
            e_pred = pd.read_csv(sources[chain][0])
            u_pred = pd.read_csv(sources[chain][1])
            for frame, units in [(e_pred, sp["evaluation"]), (u_pred, sp["uncertainty"])]:
                for unit in units:
                    g = data[subset].loc[data[subset].unit.eq(unit)].sort_values("cycle")
                    cycles, hi, slope = engine_hi(g, weights[chain])
                    keep = cycles >= 39
                    hits = cycles[hi <= .5]
                    crossing = float(hits[0]) if len(hits) else np.nan
                    for method in ["ISO", "RF_SLOPE"]:
                        f = frame.loc[frame.unit.eq(unit) & frame.method.eq(method)].sort_values("cycle")
                        assert (f.cycle.to_numpy() == cycles[keep]).all(), (tag, chain, unit)
                        max_hi = max(max_hi, float(np.max(abs(f.hi.to_numpy()-hi[keep]))),
                                     float(np.max(abs(f.h_slope.to_numpy()-slope[keep]))))
                        assert (f.in_domain.to_numpy() == (cycles[keep] >= crossing)).all()
            models = bundle if chain == "SEL" else joblib.load(P10 / f"models_{tag}.joblib")
            for method in ["ISO", "RF_SLOPE"]:
                record = models["predictors"][method]
                f = e_pred.loc[e_pred.method.eq(method)]
                x = f[record["columns"]].to_numpy()
                p = np.maximum(0., record["model"].predict(x[:, 0] if method == "ISO" else x))
                max_pred = max(max_pred, float(np.max(abs(p-f.predicted_rul.to_numpy()))))
            # Quantiles from U trajectories by an independent order statistic.
            u_pred["err"] = u_pred.predicted_rul-(u_pred.end-u_pred.cycle)
            q = {}
            for method in ["ISO", "RF_SLOPE"]:
                path = u_pred.loc[u_pred.method.eq(method) & u_pred.in_domain].groupby("unit").err.max().clip(lower=0)
                saved = quantiles.loc[quantiles.subset.eq(subset) & quantiles.repeat.eq(repeat) & quantiles.fold.eq(fold)
                                      & quantiles.chain.eq(chain) & quantiles.method.eq(method) & quantiles.scope.eq("path")]
                for alpha in [.02, .05]:
                    value = own_quantile(path.to_numpy(), alpha)
                    stored = float(saved.loc[np.isclose(saved.alpha, alpha), "q_late"].iloc[0])
                    max_q = max(max_q, abs(value-stored))
                    if alpha == .02:
                        q[method] = value
                assert int(saved.n.iloc[0]) == len(path)
            ends = e_pred.groupby("unit").end.first()
            for unit in sp["evaluation"]:
                T = int(ends.loc[unit])
                for method, anchor, d in [(m, a, d) for m in ["ISO", "RF_SLOPE"] for a in ["POINT", "LOWER98"] for d in [1, 2]] + \
                        [("HI", "MARKER", 1), ("HI", "MARKER", 2)]:
                    rows = e_pred.loc[e_pred.unit.eq(unit) & e_pred.method.eq("ISO" if method == "HI" else method)]
                    if method == "HI":
                        tau, policy = own_decide(rows, T, 0., 0, d), f"HI_MARKER_D{d}"
                    else:
                        tau = own_decide(rows, T, q[method] if anchor == "LOWER98" else 0., 15, d)
                        policy = f"{method}_{anchor}_M15_D{d}"
                    r = tau+d if np.isfinite(tau) else np.nan
                    utilised = min(r, T) if np.isfinite(r) else T
                    rebuilt.append(dict(subset=subset, repeat=repeat, fold=fold, chain=chain, unit=unit, policy_id=policy,
                                        v_decision=tau, v_utilised=float(utilised), v_late=bool(np.isfinite(r) and r > T),
                                        v_exact=bool(np.isfinite(r) and r == T), v_missing=bool(not np.isfinite(tau)),
                                        v_W_gap=float(T-utilised-1), v_J=int((tau if np.isfinite(tau) else T) > T-1-d)))
    v = pd.DataFrame(rebuilt)
    merged = decisions.merge(v, on=["subset", "repeat", "fold", "chain", "unit", "policy_id"], validate="one_to_one")
    assert len(merged) == len(decisions) == len(v) == 12000
    np.testing.assert_array_equal(merged.decision.to_numpy(float), merged.v_decision.to_numpy(float))
    np.testing.assert_array_equal(merged.utilised.to_numpy(float), merged.v_utilised.to_numpy(float))
    np.testing.assert_array_equal(merged.W_gap.to_numpy(float), merged.v_W_gap.to_numpy(float))
    assert (merged.late == merged.v_late).all() and (merged.exact_endpoint == merged.v_exact).all()
    assert (merged.has_decision == ~merged.v_missing).all() and (merged.J == merged.v_J).all()
    checks.update(decision_rows=len(merged), max_hi_slope_abs_difference=max_hi, max_prediction_abs_difference=max_pred,
                  max_quantile_abs_difference=max_q)
    assert max_hi < 1e-9 and max_pred < 1e-9 and max_q < 1e-9

    # M18 chain against archived P11/P11.1/P11.2 for all 60 partitions.
    m18 = decisions.loc[decisions.chain.eq("M18")]
    old = pd.concat([pd.read_csv(P11 / "decisions.csv"), pd.read_csv(P11A / "controls.csv")]).query("dataset == 'complete'")
    j = m18.merge(old, on=["subset", "repeat", "fold", "unit", "policy_id"], suffixes=("", "_old"), validate="one_to_one")
    assert len(j) == len(m18) == 6000
    np.testing.assert_array_equal(j.decision.to_numpy(float), j.decision_old.to_numpy(float))
    np.testing.assert_array_equal(j.utilised.to_numpy(float), j.utilised_old.to_numpy(float))
    comp = pd.read_csv(P11B / "components.csv").query("rho == 1")
    k = m18.merge(comp, on=["subset", "repeat", "fold", "unit", "policy_id"], suffixes=("", "_old"), validate="one_to_one")
    assert len(k) == 6000
    np.testing.assert_array_equal(k.W_gap.to_numpy(float), k.W_total.to_numpy(float))
    checks["m18_matches_p11_p11a_p11b_rows"] = len(j)

    # Partitions where SEL is M18 must be identical row by row.
    same = [key for key in selections.index if selections.loc[key, "selected"] == "M18"]
    for subset, repeat, fold in same:
        g = decisions.loc[decisions.subset.eq(subset) & decisions.repeat.eq(repeat) & decisions.fold.eq(fold)]
        a = g.loc[g.chain.eq("M18")].sort_values(["unit", "policy_id"]).decision.to_numpy(float)
        b = g.loc[g.chain.eq("SEL")].sort_values(["unit", "policy_id"]).decision.to_numpy(float)
        np.testing.assert_array_equal(a, b)
    checks["sel_identical_partitions"] = len(same)

    # Summaries and between-repeat ranges from the verified rows.
    summary = pd.read_csv(OUT / "decision_summary.csv").set_index(["subset", "chain", "repeat", "policy_id"])
    for key, g in merged.groupby(["subset", "chain", "repeat", "policy_id"]):
        s = summary.loc[key]
        assert s.without_decision == g.v_missing.sum() and s.late_count == g.v_late.sum() and s.exact_count == g.v_exact.sum()
        assert abs(s.mean_utilised-g.v_utilised.mean()) < 1e-9 and abs(s.mean_oracle_gap-g.v_W_gap.mean()) < 1e-9
    ranges = pd.read_csv(OUT / "ranges.csv")
    rule_rows = merged.loc[merged.policy_id.isin(["ISO_LOWER98_M15_D1", "ISO_LOWER98_M15_D2", "HI_MARKER_D1", "HI_MARKER_D2"])]
    for (subset, chain, unit, policy), g in rule_rows.groupby(["subset", "chain", "unit", "policy_id"]):
        values = g.v_decision.to_numpy(float)
        expected = values.max()-values.min() if np.isfinite(values).all() else np.nan
        stored = ranges.loc[ranges.subset.eq(subset) & ranges.chain.eq(chain) & ranges.unit.eq(unit) & ranges.quantity.eq(policy), "range"].iloc[0]
        assert (np.isnan(expected) and np.isnan(stored)) or expected == stored
    rs = pd.read_csv(OUT / "range_summary.csv")
    for r in rs.itertuples():
        g = ranges.loc[ranges.subset.eq(r.subset) & ranges.quantity.eq(r.quantity)].pivot(index="unit", columns="chain", values="range")
        assert abs(g.SEL.dropna().quantile(.95)-r.SEL_p95) < 1e-9 and abs(g.M18.dropna().quantile(.95)-r.M18_p95) < 1e-9
        pair = g.dropna()
        assert len(pair) == r.common and abs((pair.SEL-pair.M18).mean()-r.delta_mean) < 1e-9
    checks.update(summaries_checked=len(summary), ranges_checked=len(ranges), range_summaries_checked=len(rs), passed=True)
    (OUT / "verification.json").write_text(json.dumps(checks, indent=2), encoding="utf-8")
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    main()
