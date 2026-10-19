"""P21.1: break-even cost of end-of-life events (protocolo_equilibrio_eventos_21a.md). Archived expectations only."""

import hashlib
import json
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from inspection_arm_17b import _phm

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_break_even_21a"
MAIN = ART / "pilot_inspection_17b/expectations.csv.gz"
LATENT = ART / "pilot_inspection_latent_17c/expectations.csv.gz"
SELECTED_SRC = ART / "pilot_policy_selection_13a/decisions.csv"
SUMMARY_17B = ART / "pilot_inspection_17b/summary.csv"
LITERAL = ROOT / "experiments/literal_cycles_2026-10-19/cells.csv"
INPUT_HASHES = {
    MAIN: "f7ce6b0647deddf1cf2241cb3cf63e2d6fb17c4d7dc553a32891dcde917ecd60",
    LATENT: "3bfdf83cc0b797eeeb03a531af81e9f1cafedf1063e9cfc2a48c21a1ba21114c",
}
MODULES = ["protocolo_equilibrio_eventos_21a.md", "break_even_21a.py", "test_break_even_21a.py", "verify_break_even_21a.py"]
AGE = 127
BOOT, SEED = 4000, 20261021
BETAS = (0., .1, .25, .5, 1., 2., 5., 10., 20., 50., 100.)
MAIN_SCENARIO = "S2_W60_g1"
BASES = ["ISO_POINT_M15", "RF_SLOPE_POINT_M15", "ISO_LOWER98_M15", "RF_SLOPE_LOWER98_M15", "HI_MARKER"]
SELECTED = ["HI_THRESHOLD_SELECTED", "HI_WAIT_SELECTED"]
TOL = 1e-9
RATE_SCALE = 10000.
CODES = {0: "tie", 1: "A_dominates", 2: "B_dominates", 3: "A_preferred_above_beta0", 4: "A_preferred_below_beta0"}
# contrast id: (A, B, description); arms are (base, kind) with kind in PHM, HYB, AGE
CONTRASTS = {
    "C1": (("ISO_LOWER98_M15", "PHM"), ("ISO_POINT_M15", "PHM")),
    "C2": (("RF_SLOPE_LOWER98_M15", "PHM"), ("RF_SLOPE_POINT_M15", "PHM")),
    "C3": (("ISO_POINT_M15", "HYB"), ("ISO_POINT_M15", "PHM")),
    "C4": (("RF_SLOPE_POINT_M15", "HYB"), ("RF_SLOPE_POINT_M15", "PHM")),
    "C5": (("ISO_LOWER98_M15", "HYB"), ("ISO_LOWER98_M15", "PHM")),
    "C6": (("HI_MARKER", "PHM"), ("ISO_LOWER98_M15", "PHM")),
    "C7": (("ISO_LOWER98_M15", "PHM"), ("AGE127", "AGE")),
    "C8": (("ISO_POINT_M15", "HYB"), ("ISO_LOWER98_M15", "PHM")),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def classify(dW, dE, tol):
    """Codes of the cost comparison dW - beta*dE (A minus B restorations; events avoided by A)."""
    sw = np.where(dW > tol, 1, np.where(dW < -tol, -1, 0))
    se = np.where(dE > tol, 1, np.where(dE < -tol, -1, 0))
    a_dom = (sw <= 0) & (se >= 0) & ((sw < 0) | (se > 0))
    b_dom = (sw >= 0) & (se <= 0) & ((sw > 0) | (se < 0))
    return np.select([a_dom, b_dom, (sw > 0) & (se > 0), (sw < 0) & (se < 0)], [1, 2, 3, 4], default=0)


def prefer(dW, dE, beta, tol):
    """+1 where A is strictly cheaper at beta, -1 where B is, 0 for ties."""
    gap = np.asarray(dW) - beta*np.asarray(dE)
    return np.where(gap < -tol, 1, np.where(gap > tol, -1, 0))


def age_arm(T):
    T = np.asarray(T, float)
    return dict(util=np.minimum(T, AGE), late=(T < AGE).astype(float), exact=(T == AGE).astype(float),
                missing=np.zeros(len(T)))


def load_main():
    ex = pd.concat([pd.read_csv(MAIN), pd.read_csv(LATENT)], ignore_index=True)
    return ex.sort_values(["origin", "subset", "repeat", "delay", "fold", "unit"], kind="stable").reset_index(drop=True)


def load_selected():
    d = pd.read_csv(SELECTED_SRC)
    d = d.loc[d.dataset.eq("complete") & d.policy_id.str.rsplit("_D", n=1).str[0].isin(SELECTED)]
    return d.sort_values(["subset", "repeat", "delay", "fold", "unit", "policy_id"], kind="stable").reset_index(drop=True)


def build_arms(g, sel, T):
    """Arms of one (origin, subset, repeat, delay) cell, all aligned to the engine order (fold, unit)."""
    arms, phm_check = {}, 0.
    ref = None
    for (base, scen, u), h in g.groupby(["base", "scenario", "u"], sort=True):
        order = list(zip(h.fold, h.unit))
        if ref is None:
            ref = order
        assert order == ref, "engine order differs between arms"
        arms[(base, "HYB", scen, float(u))] = dict(
            util=h.util_h.to_numpy(), late=h.late_h.to_numpy(), exact=h.exact_h.to_numpy(), missing=h.missing_h.to_numpy())
        if scen == MAIN_SCENARIO:
            arms[(base, "PHM", "", float(u))] = dict(
                util=h.util_p.to_numpy(), late=h.late_p.to_numpy(), exact=h.exact_p.to_numpy(), missing=h.missing_p.to_numpy())
    for (base, scen, u), h in g.groupby(["base", "scenario", "u"], sort=True):       # PHM must not depend on the scenario at u=0
        if u == 0.:
            ref_p = arms[(base, "PHM", "", 0.)]["util"]
            phm_check = max(phm_check, float(np.abs(h.util_p.to_numpy()-ref_p).max()))
    t = g.loc[(g.base.eq(BASES[0])) & g.scenario.eq(MAIN_SCENARIO) & g.u.eq(0.)].sort_values(["fold", "unit"])
    arms[("AGE127", "AGE", "", 0.)] = age_arm(t["T"].to_numpy())
    if sel is not None:
        for name, h in sel.groupby(sel.policy_id.str.rsplit("_D", n=1).str[0]):
            h = h.sort_values(["fold", "unit"])
            assert list(zip(h.fold, h.unit)) == ref, "selected-rule engines differ from the expectation engines"
            rows = [_phm(r.endpoint, bool(r.has_decision), float(r.decision) if r.has_decision else np.nan, int(r.delay), 0.)
                    for r in h.itertuples(index=False)]
            arms[(name, "PHM", "", 0.)] = {k: np.array([x[k] for x in rows]) for k in ("util", "late", "exact", "missing")}
    return arms, ref, phm_check


def contrast_specs(arms):
    """All (contrast id, key A, key B, scenario, u) combinations available in the cell."""
    hyb = sorted({(k[2], k[3]) for k in arms if k[1] == "HYB"})
    phm_u = sorted({k[3] for k in arms if k[1] == "PHM" and k[0] == "ISO_LOWER98_M15"})
    out = []
    for cid, ((ba, ka), (bb, kb)) in CONTRASTS.items():
        if "HYB" in (ka, kb):
            for scen, u in hyb:
                keyA = (ba, ka, scen if ka == "HYB" else "", u) if ka != "AGE" else ("AGE127", "AGE", "", 0.)
                keyB = (bb, kb, scen if kb == "HYB" else "", u) if kb != "AGE" else ("AGE127", "AGE", "", 0.)
                out.append((cid, keyA, keyB, scen, u))
        else:
            for u in phm_u:
                keyA = (ba, ka, "", u) if ka != "AGE" else ("AGE127", "AGE", "", 0.)
                keyB = (bb, kb, "", u) if kb != "AGE" else ("AGE127", "AGE", "", 0.)
                out.append((cid, keyA, keyB, "", u))
    return out


def bootstrap_counts(n, key):
    rng = np.random.default_rng(key)
    return rng.multinomial(n, np.full(n, 1./n), size=BOOT).astype(float)


def analyse_cell(origin, subset, repeat, delay, arms, counts, cell_key):
    keys = sorted(arms)
    col = {k: i for i, k in enumerate(keys)}
    n = len(arms[keys[0]]["util"])
    U = np.column_stack([arms[k]["util"] for k in keys])
    E = np.column_stack([arms[k]["late"]+arms[k]["exact"]+arms[k]["missing"] for k in keys])
    SU, SE = counts @ U, counts @ E
    w0, e0 = n/U.sum(0), E.sum(0)/U.sum(0)
    wb, eb = n/SU, SE/SU
    base = dict(origin=origin, subset=subset, repeat=repeat, delay=delay, engines=n)
    rates = []
    for k, i in col.items():
        rates.append(base | dict(
            arm=k[0], kind=k[1], scenario=k[2], u=k[3], restoration_rate=RATE_SCALE*w0[i],
            restoration_rate_low=RATE_SCALE*np.quantile(wb[:, i], .025), restoration_rate_high=RATE_SCALE*np.quantile(wb[:, i], .975),
            event_rate=RATE_SCALE*e0[i], event_rate_low=RATE_SCALE*np.quantile(eb[:, i], .025),
            event_rate_high=RATE_SCALE*np.quantile(eb[:, i], .975), mean_life=float(U[:, i].mean()),
            late_per100=100*float(arms[k]["late"].mean()), exact_per100=100*float(arms[k]["exact"].mean()),
            missing_per100=100*float(arms[k]["missing"].mean()), events_per100=100*float(E[:, i].mean()),
            engines_with_event=int((E[:, i] > 1e-12).sum())))
    contrasts, prefs = [], []
    for cid, kA, kB, scen, u in contrast_specs(arms):
        if kA not in col or kB not in col:
            continue
        a, b = col[kA], col[kB]
        tol = TOL*w0[b]
        dW, dE = w0[a]-w0[b], e0[b]-e0[a]
        dWb, dEb = wb[:, a]-wb[:, b], eb[:, b]-eb[:, a]
        code = int(classify(dW, dE, tol))
        codes_b = classify(dWb, dEb, tol)
        dE_lo, dE_hi = np.quantile(dEb, [.025, .975])
        bounded = code in (3, 4) and (dE_lo > tol or dE_hi < -tol)
        beta0 = dW/dE if code in (3, 4) else np.nan
        same = codes_b == code
        ratio = dWb[same]/dEb[same] if code in (3, 4) and same.any() else np.array([np.nan])
        row_id = len(contrasts)
        contrasts.append(base | dict(
            row_id=row_id, contrast=cid, scenario=scen, u=u, A=f"{kA[0]}|{kA[1]}", B=f"{kB[0]}|{kB[1]}",
            rate_A=RATE_SCALE*w0[a], rate_B=RATE_SCALE*w0[b], event_rate_A=RATE_SCALE*e0[a], event_rate_B=RATE_SCALE*e0[b],
            dW=RATE_SCALE*dW, dW_low=RATE_SCALE*np.quantile(dWb, .025), dW_high=RATE_SCALE*np.quantile(dWb, .975),
            dE=RATE_SCALE*dE, dE_low=RATE_SCALE*dE_lo, dE_high=RATE_SCALE*dE_hi,
            cls=CODES[code], beta0=beta0, beta0_bounded=bool(bounded),
            beta0_low=float(np.quantile(ratio, .025)) if bounded else np.nan,
            beta0_high=float(np.quantile(ratio, .975)) if bounded else np.nan,
            boot_A_dominates=float((codes_b == 1).mean()), boot_B_dominates=float((codes_b == 2).mean()),
            boot_A_above=float((codes_b == 3).mean()), boot_A_below=float((codes_b == 4).mean()),
            boot_tie=float((codes_b == 0).mean()),
            engines_event_A=int((E[:, a] > 1e-12).sum()), engines_event_B=int((E[:, b] > 1e-12).sum()),
            events_per100_A=100*float(E[:, a].mean()), events_per100_B=100*float(E[:, b].mean())))
        for beta in BETAS:
            pb = prefer(dWb, dEb, beta, tol)
            prefs.append(dict(row_id=row_id, origin=origin, subset=subset, repeat=repeat, delay=delay, contrast=cid,
                              scenario=scen, u=u, beta=beta, point=int(prefer(dW, dE, beta, tol)),
                              boot_A_cheaper=float((pb == 1).mean()), boot_B_cheaper=float((pb == -1).mean())))
    # frontier: main scenario, u = 0
    main = [k for k in keys if (k[1] == "HYB" and k[2] == MAIN_SCENARIO and k[3] == 0.) or (k[1] in ("PHM", "AGE") and k[3] == 0.)]
    front = []
    for k in main:
        i = col[k]
        dom = [m[0]+"|"+m[1] for m in main if m != k and w0[col[m]] <= w0[i]*(1+TOL) and e0[col[m]] <= e0[i]+TOL*w0[i]
               and (w0[col[m]] < w0[i]*(1-TOL) or e0[col[m]] < e0[i]-TOL*w0[i])]
        front.append(base | dict(arm=k[0], kind=k[1], restoration_rate=RATE_SCALE*w0[i], event_rate=RATE_SCALE*e0[i],
                                 dominated=bool(dom), dominated_by=";".join(sorted(dom))))
    return rates, contrasts, prefs, front


def summarise_contrasts(c):
    keys = ["origin", "subset", "delay", "contrast", "scenario", "u"]
    rows = []
    for key, g in c.groupby(keys, sort=True):
        rows.append(dict(zip(keys, key)) | dict(
            repeats=len(g), dW_min=g.dW.min(), dW_max=g.dW.max(), dE_min=g.dE.min(), dE_max=g.dE.max(),
            beta0_min=g.beta0.min(), beta0_max=g.beta0.max(), beta0_bounded_repeats=int(g.beta0_bounded.sum()),
            classes=";".join(sorted(set(g.cls))), n_A_dominates=int((g.cls == "A_dominates").sum()),
            n_B_dominates=int((g.cls == "B_dominates").sum()),
            n_tradeoff=int(g.cls.isin(["A_preferred_above_beta0", "A_preferred_below_beta0"]).sum()),
            engines_event_B_min=int(g.engines_event_B.min()), engines_event_B_max=int(g.engines_event_B.max())))
    return pd.DataFrame(rows)


def validate(rates):
    s = pd.read_csv(SUMMARY_17B)
    out = {}
    r = rates.copy()
    r["u"] = r.u.astype(float)
    hy = r.loc[r.kind.eq("HYB") & r.arm.isin(BASES)].rename(columns={"arm": "base"})
    ph = r.loc[r.kind.eq("PHM") & r.arm.isin(BASES)].rename(columns={"arm": "base"})
    m = s.merge(hy[["origin", "subset", "repeat", "delay", "base", "scenario", "u", "restoration_rate"]],
                on=["origin", "subset", "repeat", "delay", "base", "scenario", "u"], how="left")
    d_h = (m.restoration_rate/m.rate_h_per_10000-1).abs()
    ph_ref = ph.rename(columns={"restoration_rate": "rp"})[["origin", "subset", "repeat", "delay", "base", "u", "rp"]]
    m2 = s.merge(ph_ref, on=["origin", "subset", "repeat", "delay", "base", "u"], how="left")
    d_p = (m2.rp/m2.rate_p_per_10000-1).abs()
    out["p17b_rows"] = int(len(s))
    out["p17b_unmatched_hybrid"] = int(d_h.isna().sum())
    out["p17b_unmatched_phm"] = int(d_p.isna().sum())
    out["p17b_max_rel_diff_hybrid"] = float(d_h.max())
    out["p17b_max_rel_diff_phm"] = float(d_p.max())
    out["p17b_pass"] = bool(d_h.max() <= TOL and d_p.max() <= TOL and not d_h.isna().any() and not d_p.isna().any())
    lit = pd.read_csv(LITERAL)
    lit["delay"] = lit.arm.str.extract(r"_D(\d)$").astype(int)
    lit["kind"] = lit.arm.str.split("_").str[0]
    lit["arm_name"] = lit.arm.str.replace(r"^(AGE127|PHM|HYB)_", "", regex=True).str.replace(r"_D\d$", "", regex=True)
    lit.loc[lit.kind.eq("AGE127"), "arm_name"] = "AGE127"
    lit["kind"] = lit.kind.replace({"AGE127": "AGE"})
    z = r.loc[(r.scenario.isin(["", MAIN_SCENARIO])) & r.u.eq(0.) & (r.arm.isin(BASES+["AGE127"]))]
    z = z.assign(mean_cycles=lit_scale(z))
    z = z.merge(lit, left_on=["subset", "repeat", "arm", "kind", "delay"], right_on=["subset", "repeat", "arm_name", "kind", "delay"], how="left",
                suffixes=("", "_lit"))
    z["rel_total"] = (z.mean_cycles/z.visits-1).abs()
    z["rel_degradation"] = (z.mean_cycles/z.degradation_visits-1).abs()
    out["p20b_rows"] = int(len(z))
    out["p20b_unmatched"] = int(z.visits.isna().sum())
    out["p20b_max_rel_diff_total_visits"] = float(z.rel_total.max())
    out["p20b_max_rel_diff_degradation_visits"] = float(z.rel_degradation.max())
    out["p20b_tolerance"] = 0.01
    out["p20b_pass_total"] = bool(z.rel_total.max() <= .01 and not z.visits.isna().any())
    worst = z.sort_values("rel_total", ascending=False).head(5)
    out["p20b_worst"] = [dict(subset=x.subset, repeat=int(x.repeat), arm=x.arm, kind=x.kind, delay=int(x.delay), total_rel=float(x.rel_total))
                         for x in worst.itertuples()]
    return out, z


def lit_scale(z):
    return 32000.*z.restoration_rate/RATE_SCALE


def main():
    t0 = time.time()
    OUT.mkdir(parents=True, exist_ok=True)
    for p, h in INPUT_HASHES.items():
        assert sha(p) == h, f"input hash differs: {p}"
    start = dict(started=datetime.now(timezone.utc).isoformat(), inputs={str(p.relative_to(ROOT)): sha(p) for p in
                 [MAIN, LATENT, SELECTED_SRC, SUMMARY_17B, LITERAL]}, modules={m: sha(ROOT/"experiments"/m) for m in MODULES})
    (OUT/"execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    ex, sel = load_main(), load_selected()
    sel_origin = {"development"}
    R, C, P, F = [], [], [], []
    phm_check = 0.
    cell_index = {k: i for i, k in enumerate(sorted(ex[["origin", "subset", "repeat"]].drop_duplicates().itertuples(index=False, name=None)))}
    for (origin, subset, repeat), cg in ex.groupby(["origin", "subset", "repeat"], sort=True):
        n = cg.loc[cg.delay.eq(1) & cg.base.eq(BASES[0]) & cg.scenario.eq(MAIN_SCENARIO) & cg.u.eq(0.)].shape[0]
        counts = bootstrap_counts(n, [SEED, cell_index[(origin, subset, repeat)]])
        for delay, g in cg.groupby("delay", sort=True):
            s = None
            if origin in sel_origin:
                s = sel.loc[sel.subset.eq(subset) & sel.repeat.eq(repeat) & sel.delay.eq(delay)]
            T = None
            arms, order, chk = build_arms(g, s, T)
            phm_check = max(phm_check, chk)
            r, c, p, f = analyse_cell(origin, subset, repeat, int(delay), arms, counts, None)
            R += r; C += c; P += p; F += f
        print(origin, subset, repeat, f"{time.time()-t0:.0f}s", flush=True)
    rates, contrasts, prefs, front = map(pd.DataFrame, (R, C, P, F))
    summary = summarise_contrasts(contrasts)
    val, lit = validate(rates)
    val["phm_scenario_independence_max_abs_diff"] = phm_check
    per_cell = contrasts.groupby(["origin", "subset", "repeat", "delay"]).size()
    val["contrasts_per_cell_delay"] = sorted(set(int(x) for x in per_cell))
    val["contrasts_per_cell_delay_expected"] = 108
    val["cells_delays"] = int(len(per_cell))
    val["inputs_ok"] = True
    rates.to_csv(OUT/"rates.csv", index=False)
    contrasts.to_csv(OUT/"contrasts.csv", index=False)
    summary.to_csv(OUT/"contrast_summary.csv", index=False)
    prefs.to_csv(OUT/"preference_curves.csv", index=False)
    front.to_csv(OUT/"frontier.csv", index=False)
    (OUT/"validation.json").write_text(json.dumps(val, indent=2), encoding="utf-8")
    for m in MODULES:
        (OUT/f"source_{m}").write_bytes((ROOT/"experiments"/m).read_bytes())
    meta = dict(finished=datetime.now(timezone.utc).isoformat(), seconds=time.time()-t0, python=sys.version, platform=platform.platform(),
                numpy=np.__version__, pandas=pd.__version__, boot=BOOT, seed=SEED, betas=list(BETAS),
                rows=dict(rates=len(rates), contrasts=len(contrasts), summary=len(summary), preference_curves=len(prefs), frontier=len(front)))
    (OUT/"metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    refresh_manifest()
    print(json.dumps(val, indent=2))
    print(json.dumps(meta, indent=2))


def refresh_manifest():
    files = sorted(p for p in OUT.iterdir() if p.is_file() and p.name != "manifest.json")
    (OUT/"manifest.json").write_text(json.dumps({p.name: sha(p) for p in files}, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
