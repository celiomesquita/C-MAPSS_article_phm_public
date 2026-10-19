"""P21.2: break-even cost with a positive inspection cost (protocolo_custo_inspecao_21b.md). Archived expectations only."""

import json
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import break_even_21a as b21

ROOT = b21.ROOT
ART = b21.ART
OUT = ART / "pilot_break_even_cost_21b"
P21A = ART / "pilot_break_even_21a"
QS = (0., .005, .01, .02)
MODULES = ["protocolo_custo_inspecao_21b.md", "break_even_cost_21b.py", "test_break_even_cost_21b.py", "verify_break_even_cost_21b.py"]
BOOT, SEED, BETAS, TOL, RATE_SCALE, CODES = b21.BOOT, b21.SEED, b21.BETAS, b21.TOL, b21.RATE_SCALE, b21.CODES


def add_inspections(arms, g):
    """Attach the expected number of inspections per engine to every arm (zero without inspection)."""
    n = len(next(iter(arms.values()))["util"])
    for a in arms.values():
        a["insp"] = np.zeros(n)
    for (base, scen, u), h in g.groupby(["base", "scenario", "u"], sort=True):
        arms[(base, "HYB", scen, float(u))]["insp"] = h.inspections.to_numpy(float)
    return arms


def effective_rate(n, su, sn, q):
    return (n+q*sn)/su


def analyse_cell_cost(origin, subset, repeat, delay, arms, counts, q):
    keys = sorted(arms)
    col = {k: i for i, k in enumerate(keys)}
    n = len(arms[keys[0]]["util"])
    U = np.column_stack([arms[k]["util"] for k in keys])
    E = np.column_stack([arms[k]["late"]+arms[k]["exact"]+arms[k]["missing"] for k in keys])
    N = np.column_stack([arms[k].get("insp", np.zeros(n)) for k in keys])
    SU, SE, SN = counts @ U, counts @ E, counts @ N
    w0, e0, v0 = effective_rate(n, U.sum(0), N.sum(0), q), E.sum(0)/U.sum(0), N.sum(0)/U.sum(0)
    wb, eb = effective_rate(n, SU, SN, q), SE/SU
    base = dict(origin=origin, subset=subset, repeat=repeat, delay=delay, engines=n, q_inspection=q)
    rates = []
    for k, i in col.items():
        rates.append(base | dict(
            arm=k[0], kind=k[1], scenario=k[2], u=k[3], restoration_equivalent_rate=RATE_SCALE*w0[i],
            restoration_equivalent_low=RATE_SCALE*np.quantile(wb[:, i], .025), restoration_equivalent_high=RATE_SCALE*np.quantile(wb[:, i], .975),
            event_rate=RATE_SCALE*e0[i], inspection_rate=RATE_SCALE*v0[i], inspections_per_engine=float(N[:, i].mean()),
            mean_life=float(U[:, i].mean())))
    contrasts, prefs = [], []
    for cid, kA, kB, scen, u in b21.contrast_specs(arms):
        if kA not in col or kB not in col:
            continue
        a, b = col[kA], col[kB]
        tol = TOL*w0[b]
        dW, dE = w0[a]-w0[b], e0[b]-e0[a]
        dWb, dEb = wb[:, a]-wb[:, b], eb[:, b]-eb[:, a]
        code = int(b21.classify(dW, dE, tol))
        codes_b = b21.classify(dWb, dEb, tol)
        dE_lo, dE_hi = np.quantile(dEb, [.025, .975])
        bounded = code in (3, 4) and (dE_lo > tol or dE_hi < -tol)
        beta0 = dW/dE if code in (3, 4) else np.nan
        same = codes_b == code
        ratio = dWb[same]/dEb[same] if code in (3, 4) and same.any() else np.array([np.nan])
        row_id = len(contrasts)
        contrasts.append(base | dict(
            row_id=row_id, contrast=cid, scenario=scen, u=u, A=f"{kA[0]}|{kA[1]}", B=f"{kB[0]}|{kB[1]}",
            rate_A=RATE_SCALE*w0[a], rate_B=RATE_SCALE*w0[b], event_rate_A=RATE_SCALE*e0[a], event_rate_B=RATE_SCALE*e0[b],
            dNu=RATE_SCALE*(v0[a]-v0[b]), inspections_per_engine_A=float(N[:, a].mean()), inspections_per_engine_B=float(N[:, b].mean()),
            dW=RATE_SCALE*dW, dW_low=RATE_SCALE*np.quantile(dWb, .025), dW_high=RATE_SCALE*np.quantile(dWb, .975),
            dE=RATE_SCALE*dE, dE_low=RATE_SCALE*dE_lo, dE_high=RATE_SCALE*dE_hi,
            cls=CODES[code], beta0=beta0, beta0_bounded=bool(bounded),
            beta0_low=float(np.quantile(ratio, .025)) if bounded else np.nan,
            beta0_high=float(np.quantile(ratio, .975)) if bounded else np.nan,
            boot_A_dominates=float((codes_b == 1).mean()), boot_B_dominates=float((codes_b == 2).mean()),
            boot_A_above=float((codes_b == 3).mean()), boot_A_below=float((codes_b == 4).mean()), boot_tie=float((codes_b == 0).mean()),
            engines_event_A=int((E[:, a] > 1e-12).sum()), engines_event_B=int((E[:, b] > 1e-12).sum()),
            events_per100_A=100*float(E[:, a].mean()), events_per100_B=100*float(E[:, b].mean())))
        for beta in BETAS:
            pb = b21.prefer(dWb, dEb, beta, tol)
            prefs.append(dict(row_id=row_id, origin=origin, subset=subset, repeat=repeat, delay=delay, q_inspection=q, contrast=cid,
                              scenario=scen, u=u, beta=beta, point=int(b21.prefer(dW, dE, beta, tol)),
                              boot_A_cheaper=float((pb == 1).mean()), boot_B_cheaper=float((pb == -1).mean())))
    main = [k for k in keys if (k[1] == "HYB" and k[2] == b21.MAIN_SCENARIO and k[3] == 0.) or (k[1] in ("PHM", "AGE") and k[3] == 0.)]
    front = []
    for k in main:
        i = col[k]
        dom = [m[0]+"|"+m[1] for m in main if m != k and w0[col[m]] <= w0[i]*(1+TOL) and e0[col[m]] <= e0[i]+TOL*w0[i]
               and (w0[col[m]] < w0[i]*(1-TOL) or e0[col[m]] < e0[i]-TOL*w0[i])]
        front.append(base | dict(arm=k[0], kind=k[1], restoration_equivalent_rate=RATE_SCALE*w0[i], event_rate=RATE_SCALE*e0[i],
                                 dominated=bool(dom), dominated_by=";".join(sorted(dom))))
    return rates, contrasts, prefs, front


def summarise(c):
    keys = ["origin", "subset", "delay", "q_inspection", "contrast", "scenario", "u"]
    rows = []
    for key, g in c.groupby(keys, sort=True, dropna=False):
        rows.append(dict(zip(keys, key)) | dict(
            repeats=len(g), dW_min=g.dW.min(), dW_max=g.dW.max(), dE_min=g.dE.min(), dE_max=g.dE.max(),
            dNu_min=g.dNu.min(), dNu_max=g.dNu.max(), beta0_min=g.beta0.min(), beta0_max=g.beta0.max(),
            beta0_bounded_repeats=int(g.beta0_bounded.sum()), classes=";".join(sorted(set(g.cls))),
            n_A_dominates=int((g.cls == "A_dominates").sum()), n_B_dominates=int((g.cls == "B_dominates").sum()),
            n_tradeoff=int(g.cls.isin(["A_preferred_above_beta0", "A_preferred_below_beta0"]).sum()),
            engines_event_B_min=int(g.engines_event_B.min()), engines_event_B_max=int(g.engines_event_B.max())))
    return pd.DataFrame(rows)


def validate(rates, contrasts):
    out = {}
    ref = pd.read_csv(P21A / "contrasts.csv", keep_default_na=False, na_values=[""])
    key = ["origin", "subset", "repeat", "delay", "contrast", "scenario", "u"]
    c0 = contrasts.loc[contrasts.q_inspection.eq(0.)].assign(scenario=lambda d: d.scenario.replace("", np.nan))
    m = ref.merge(c0, on=key, suffixes=("_a", "_b"), how="outer", indicator=True)
    out["q0_rows_unmatched"] = int((m["_merge"] != "both").sum())
    both = m.loc[m["_merge"] == "both"]
    diffs = {}
    for col in ["rate_A", "rate_B", "event_rate_A", "event_rate_B", "dW", "dE", "dW_low", "dW_high", "dE_low", "dE_high",
                "beta0", "beta0_low", "beta0_high", "boot_A_dominates", "boot_B_dominates", "boot_A_above", "boot_A_below", "boot_tie"]:
        a, b = both[col+"_a"].to_numpy(float), both[col+"_b"].to_numpy(float)
        both_nan = np.isnan(a) & np.isnan(b)
        diffs[col] = float(np.max(np.where(both_nan, 0., np.abs(a-b)/np.maximum(np.abs(a), 1e-12)))) if len(a) else 0.
    out["q0_max_rel_diff"] = diffs
    out["q0_class_mismatch"] = int((both.cls_a != both.cls_b).sum())
    out["q0_bounded_mismatch"] = int((both.beta0_bounded_a.astype(bool) != both.beta0_bounded_b.astype(bool)).sum())
    out["q0_pass"] = bool(out["q0_rows_unmatched"] == 0 and max(diffs.values()) <= 1e-9 and out["q0_class_mismatch"] == 0
                          and out["q0_bounded_mismatch"] == 0)
    s = pd.read_csv(b21.SUMMARY_17B)
    h = rates.loc[rates.q_inspection.eq(0.) & rates.kind.eq("HYB") & rates.arm.isin(b21.BASES)].rename(columns={"arm": "base"})
    mm = s.merge(h[["origin", "subset", "repeat", "delay", "base", "scenario", "u", "inspections_per_engine"]],
                 on=["origin", "subset", "repeat", "delay", "base", "scenario", "u"], suffixes=("_s", "_h"), how="left")
    d = (mm.inspections_per_engine_h-mm.inspections_per_engine_s).abs()/np.maximum(mm.inspections_per_engine_s.abs(), 1e-12)
    out["p17b_inspections_unmatched"] = int(d.isna().sum())
    out["p17b_inspections_max_rel_diff"] = float(d.max())
    out["p17b_inspections_pass"] = bool(d.max() <= 1e-9 and not d.isna().any())
    nonhyb = rates.loc[~rates.kind.eq("HYB"), "inspections_per_engine"]
    out["non_hybrid_inspections_max"] = float(nonhyb.max())
    # monotonicity: A hybrid and B PHM of the same base (C3, C4, C5): restoration-equivalent of A minus B must not fall with q
    mono = True
    for cid in ("C3", "C4", "C5"):
        g = contrasts.loc[contrasts.contrast.eq(cid)].sort_values("q_inspection")
        piv = g.pivot_table(index=["origin", "subset", "repeat", "delay", "scenario", "u"], columns="q_inspection", values="dW")
        mono = mono and bool((piv.diff(axis=1).iloc[:, 1:] >= -1e-12).all().all())
    out["monotone_in_q"] = mono
    return out


def main():
    t0 = time.time()
    OUT.mkdir(parents=True, exist_ok=True)
    for p, h in b21.INPUT_HASHES.items():
        assert b21.sha(p) == h, f"input hash differs: {p}"
    start = dict(started=datetime.now(timezone.utc).isoformat(), qs=list(QS),
                 inputs={str(p.relative_to(ROOT)): b21.sha(p) for p in [b21.MAIN, b21.LATENT, b21.SELECTED_SRC, b21.SUMMARY_17B, P21A/"contrasts.csv"]},
                 modules={m: b21.sha(ROOT/"experiments"/m) for m in MODULES})
    (OUT/"execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    ex, sel = b21.load_main(), b21.load_selected()
    R, C, P, F = [], [], [], []
    cell_index = {k: i for i, k in enumerate(sorted(ex[["origin", "subset", "repeat"]].drop_duplicates().itertuples(index=False, name=None)))}
    for (origin, subset, repeat), cg in ex.groupby(["origin", "subset", "repeat"], sort=True):
        n = cg.loc[cg.delay.eq(1) & cg.base.eq(b21.BASES[0]) & cg.scenario.eq(b21.MAIN_SCENARIO) & cg.u.eq(0.)].shape[0]
        counts = b21.bootstrap_counts(n, [SEED, cell_index[(origin, subset, repeat)]])
        for delay, g in cg.groupby("delay", sort=True):
            s = sel.loc[sel.subset.eq(subset) & sel.repeat.eq(repeat) & sel.delay.eq(delay)] if origin == "development" else None
            arms, _, _ = b21.build_arms(g, s, None)
            arms = add_inspections(arms, g)
            for q in QS:
                r, c, p, f = analyse_cell_cost(origin, subset, repeat, int(delay), arms, counts, q)
                R += r; C += c; P += p; F += f
        print(origin, subset, repeat, f"{time.time()-t0:.0f}s", flush=True)
    rates, contrasts, prefs, front = map(pd.DataFrame, (R, C, P, F))
    summary = summarise(contrasts)
    val = validate(rates, contrasts)
    per = contrasts.groupby(["origin", "subset", "repeat", "delay", "q_inspection"]).size()
    val["contrasts_per_cell_delay_q"] = sorted(set(int(x) for x in per))
    val["cells_delays_q"] = int(len(per))
    rates.to_csv(OUT/"rates.csv", index=False)
    contrasts.to_csv(OUT/"contrasts.csv", index=False)
    summary.to_csv(OUT/"contrast_summary.csv", index=False)
    prefs.to_csv(OUT/"preference_curves.csv", index=False)
    front.to_csv(OUT/"frontier.csv", index=False)
    (OUT/"validation.json").write_text(json.dumps(val, indent=2), encoding="utf-8")
    for m in MODULES:
        (OUT/f"source_{m}").write_bytes((ROOT/"experiments"/m).read_bytes())
    meta = dict(finished=datetime.now(timezone.utc).isoformat(), seconds=time.time()-t0, python=sys.version, platform=platform.platform(),
                numpy=np.__version__, pandas=pd.__version__, boot=BOOT, seed=SEED, betas=list(BETAS), qs=list(QS),
                rows=dict(rates=len(rates), contrasts=len(contrasts), summary=len(summary), preference_curves=len(prefs), frontier=len(front)))
    (OUT/"metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    refresh_manifest()
    print(json.dumps(val, indent=2))
    print(json.dumps(meta, indent=2))


def refresh_manifest():
    files = sorted(p for p in OUT.iterdir() if p.is_file() and p.name != "manifest.json")
    (OUT/"manifest.json").write_text(json.dumps({p.name: b21.sha(p) for p in files}, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
