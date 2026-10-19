"""Independent verification of P21.1 (break_even_21a.py): rebuilds arms, contrasts, bootstrap and frontier from the raw sources."""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_break_even_21a"
SCEN_MAIN = "S2_W60_g1"
BETAS = [0., .1, .25, .5, 1., 2., 5., 10., 20., 50., 100.]
BOOT, SEED = 4000, 20261021
CLASS = {0: "tie", 1: "A_dominates", 2: "B_dominates", 3: "A_preferred_above_beta0", 4: "A_preferred_below_beta0"}
SELECTED = ["HI_THRESHOLD_SELECTED", "HI_WAIT_SELECTED"]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def close(a, b, rtol=1e-9, atol=1e-12):
    a, b = np.asarray(a, float), np.asarray(b, float)
    return bool(np.all((np.isnan(a) & np.isnan(b)) | (np.abs(a-b) <= atol+rtol*np.abs(b))))


def sign(x, tol):
    return 1 if x > tol else (-1 if x < -tol else 0)


def code_scalar(dW, dE, tol):
    sw, se = sign(dW, tol), sign(dE, tol)
    if sw <= 0 and se >= 0 and (sw < 0 or se > 0):
        return 1
    if sw >= 0 and se <= 0 and (sw > 0 or se < 0):
        return 2
    if sw > 0 and se > 0:
        return 3
    if sw < 0 and se < 0:
        return 4
    return 0


def engine_vectors(main, latent, sel, origin, subset, repeat, delay, arm, kind, scen, u):
    """Per-engine (util, event probability) sorted by (fold, unit), straight from the raw files."""
    if kind == "AGE":
        t = main.loc[(main.origin == origin) & (main.subset == subset) & (main.repeat == repeat) & (main.delay == delay)
                     & (main.base == "ISO_POINT_M15") & (main.scenario == SCEN_MAIN) & (main.u == 0.)].sort_values(["fold", "unit"])
        T = t["T"].to_numpy(float)
        return np.minimum(T, 127.), (T <= 127.).astype(float), list(zip(t.fold, t.unit))
    if arm in SELECTED:
        d = sel.loc[(sel.subset == subset) & (sel.repeat == repeat) & (sel.delay == delay)
                    & (sel.policy_id == f"{arm}_D{delay}")].sort_values(["fold", "unit"])
        ev = (d.late.astype(bool) | d.exact_endpoint.astype(bool) | ~d.has_decision.astype(bool)).astype(float)
        return d.utilised.to_numpy(float), ev.to_numpy(), list(zip(d.fold, d.unit))
    src = latent if str(scen).startswith("L") else main
    sc = scen if kind == "HYB" else SCEN_MAIN
    h = src.loc[(src.origin == origin) & (src.subset == subset) & (src.repeat == repeat) & (src.delay == delay)
                & (src.base == arm) & (src.scenario == sc) & (src.u == u)].sort_values(["fold", "unit"])
    if kind == "HYB":
        return h.util_h.to_numpy(float), (h.late_h+h.exact_h+h.missing_h).to_numpy(float), list(zip(h.fold, h.unit))
    return h.util_p.to_numpy(float), (h.late_p+h.exact_p+h.missing_p).to_numpy(float), list(zip(h.fold, h.unit))


def main():
    problems = []

    def check(name, ok):
        print(("ok   " if ok else "FAIL ") + name, flush=True)
        if not ok:
            problems.append(name)

    main_ex = pd.read_csv(ART / "pilot_inspection_17b/expectations.csv.gz")
    latent = pd.read_csv(ART / "pilot_inspection_latent_17c/expectations.csv.gz")
    sel = pd.read_csv(ART / "pilot_policy_selection_13a/decisions.csv")
    sel = sel.loc[sel.dataset == "complete"]
    contrasts = pd.read_csv(OUT / "contrasts.csv", keep_default_na=False, na_values=[""])
    prefs = pd.read_csv(OUT / "preference_curves.csv", keep_default_na=False, na_values=[""])
    rates = pd.read_csv(OUT / "rates.csv", keep_default_na=False, na_values=[""])
    front = pd.read_csv(OUT / "frontier.csv", keep_default_na=False, na_values=[""])
    summary = pd.read_csv(OUT / "contrast_summary.csv", keep_default_na=False, na_values=[""])
    manifest = json.loads((OUT / "manifest.json").read_text(encoding="utf-8"))
    check("manifest hashes", all(sha(OUT / k) == v for k, v in manifest.items()))
    meta = json.loads((OUT / "metadata.json").read_text(encoding="utf-8"))
    check("bootstrap configuration", meta["boot"] == BOOT and meta["seed"] == SEED)

    # contrasts per cell and delay: complete and unique
    key = ["origin", "subset", "repeat", "delay"]
    cnt = contrasts.groupby(key).size()
    check("108 contrasts per cell and delay", set(cnt) == {108} and len(cnt) == 24)
    check("no duplicated contrast", not contrasts.duplicated(key+["contrast", "scenario", "u"]).any())

    cell_index = {k: i for i, k in enumerate(sorted(contrasts[["origin", "subset", "repeat"]].drop_duplicates().itertuples(index=False, name=None)))}
    bad, nrow = 0, 0
    pref_ok = True
    for (origin, subset, repeat), cg in contrasts.groupby(["origin", "subset", "repeat"], sort=True):
        n = int(cg.engines.iloc[0])
        rng = np.random.default_rng([SEED, cell_index[(origin, subset, repeat)]])
        counts = rng.multinomial(n, np.full(n, 1./n), size=BOOT).astype(float)
        cache = {}

        def vec(delay, arm_label, scen, u):
            arm, kind = arm_label.split("|")
            k = (delay, arm_label, scen if kind == "HYB" else "", u if kind != "AGE" else 0.)
            if k not in cache:
                ut, ev, order = engine_vectors(main_ex, latent, sel, origin, subset, repeat, delay, arm, kind, scen, u)
                if len(ut) != n:
                    raise AssertionError(("engine count", k, len(ut), n))
                cache[k] = (ut, ev, order)
            return cache[k]
        for r in cg.itertuples(index=False):
            uA, eA, oA = vec(r.delay, r.A, r.scenario if isinstance(r.scenario, str) else "", r.u)
            uB, eB, oB = vec(r.delay, r.B, r.scenario if isinstance(r.scenario, str) else "", r.u)
            if oA != oB:
                bad += 1
                continue
            wA, wB = n/uA.sum(), n/uB.sum()
            gA, gB = eA.sum()/uA.sum(), eB.sum()/uB.sum()
            tol = 1e-9*wB
            dW, dE = wA-wB, gB-gA
            code = code_scalar(dW, dE, tol)
            sU = np.einsum("bn,n->b", counts, uA), np.einsum("bn,n->b", counts, uB)
            sE = np.einsum("bn,n->b", counts, eA), np.einsum("bn,n->b", counts, eB)
            wAb, wBb = n/sU[0], n/sU[1]
            gAb, gBb = sE[0]/sU[0], sE[1]/sU[1]
            dWb, dEb = wAb-wBb, gBb-gAb
            ok = (close(1e4*wA, r.rate_A) and close(1e4*wB, r.rate_B) and close(1e4*dW, r.dW) and close(1e4*dE, r.dE)
                  and close(1e4*gA, r.event_rate_A) and close(1e4*gB, r.event_rate_B) and CLASS[code] == r.cls
                  and close(1e4*np.quantile(dWb, .025), r.dW_low) and close(1e4*np.quantile(dWb, .975), r.dW_high)
                  and close(1e4*np.quantile(dEb, .025), r.dE_low) and close(1e4*np.quantile(dEb, .975), r.dE_high)
                  and int((eA > 1e-12).sum()) == r.engines_event_A and int((eB > 1e-12).sum()) == r.engines_event_B
                  and close(100*eA.mean(), r.events_per100_A) and close(100*eB.mean(), r.events_per100_B))
            if code in (3, 4):
                ok = ok and close(dW/dE, r.beta0)
            else:
                ok = ok and np.isnan(r.beta0)
            sw = np.array([sign(x, tol) for x in dWb]); se = np.array([sign(x, tol) for x in dEb])
            full = [float(np.mean((sw <= 0) & (se >= 0) & ((sw < 0) | (se > 0)))), float(np.mean((sw >= 0) & (se <= 0) & ((sw > 0) | (se < 0)))),
                    float(np.mean((sw > 0) & (se > 0))), float(np.mean((sw < 0) & (se < 0))), float(np.mean((sw == 0) & (se == 0)))]
            ok = ok and close(full, [r.boot_A_dominates, r.boot_B_dominates, r.boot_A_above, r.boot_A_below, r.boot_tie])
            if not ok:
                bad += 1
            nrow += 1
            pr = prefs.loc[prefs.row_id.eq(r.row_id) & prefs.origin.eq(origin) & prefs.subset.eq(subset) & prefs.repeat.eq(repeat)
                           & prefs.delay.eq(r.delay)]
            for beta in BETAS:
                q = pr.loc[np.isclose(pr.beta, beta)]
                gap = dWb-beta*dEb
                pa, pb = float(np.mean(gap < -tol)), float(np.mean(gap > tol))
                g0 = dW-beta*dE
                point = 1 if g0 < -tol else (-1 if g0 > tol else 0)
                if len(q) != 1 or not (close(q.boot_A_cheaper.iloc[0], pa) and close(q.boot_B_cheaper.iloc[0], pb) and int(q.point.iloc[0]) == point):
                    pref_ok = False
            # bounded break-even and its interval
            lo, hi = np.quantile(dEb, [.025, .975])
            bounded = code in (3, 4) and (lo > tol or hi < -tol)
            if bool(r.beta0_bounded) != bool(bounded):
                bad += 1
            if bounded:
                ratio = np.array([a/b for a, b, c in zip(dWb, dEb, [code_scalar(x, y, tol) for x, y in zip(dWb, dEb)]) if c == code])
                if not (close(np.quantile(ratio, .025), r.beta0_low) and close(np.quantile(ratio, .975), r.beta0_high)):
                    bad += 1
    check(f"{nrow} contrast rows rebuilt from raw sources", bad == 0 and nrow == len(contrasts))
    check("preference curves (point and bootstrap) rebuilt", pref_ok and len(prefs) == len(contrasts)*len(BETAS))

    # rates: independent re-aggregation for every arm
    r_bad = 0
    for r in rates.itertuples(index=False):
        scen = r.scenario if isinstance(r.scenario, str) else ""
        ut, ev, _ = engine_vectors(main_ex, latent, sel, r.origin, r.subset, r.repeat, r.delay, r.arm, r.kind, scen, r.u)
        if not (close(1e4*len(ut)/ut.sum(), r.restoration_rate) and close(1e4*ev.sum()/ut.sum(), r.event_rate)
                and int((ev > 1e-12).sum()) == r.engines_with_event and close(ut.mean(), r.mean_life)):
            r_bad += 1
    check(f"{len(rates)} arm rates rebuilt (selected rules from archived columns)", r_bad == 0)

    # frontier: recompute dominance from rates.csv with strict scalar loops
    f_bad = 0
    for (origin, subset, repeat, delay), g in front.groupby(key):
        for a in g.itertuples(index=False):
            dom = [b for b in g.itertuples(index=False) if (b.arm, b.kind) != (a.arm, a.kind)
                   and b.restoration_rate <= a.restoration_rate*(1+1e-9) and b.event_rate <= a.event_rate+1e-9*a.restoration_rate
                   and (b.restoration_rate < a.restoration_rate*(1-1e-9) or b.event_rate < a.event_rate-1e-9*a.restoration_rate)]
            if bool(a.dominated) != bool(dom):
                f_bad += 1
    check("frontier dominance recomputed", f_bad == 0)

    # per-repeat range summary
    s_bad = 0
    for k, g in contrasts.groupby(["origin", "subset", "delay", "contrast", "scenario", "u"], dropna=False):
        s = summary.loc[(summary.origin == k[0]) & (summary.subset == k[1]) & (summary.delay == k[2]) & (summary.contrast == k[3])
                        & (summary.u == k[5])]
        s = s.loc[s.scenario.isna()] if (isinstance(k[4], float) or k[4] == "") else s.loc[s.scenario == k[4]]
        if len(s) != 1 or not (close(g.dW.min(), s.dW_min.iloc[0]) and close(g.dW.max(), s.dW_max.iloc[0])
                               and close(g.dE.min(), s.dE_min.iloc[0]) and close(g.dE.max(), s.dE_max.iloc[0])
                               and int(g.engines_event_B.max()) == int(s.engines_event_B_max.iloc[0])):
            s_bad += 1
    check("repeat ranges summarised correctly", s_bad == 0)

    val = json.loads((OUT / "validation.json").read_text(encoding="utf-8"))
    check("P17.1 rates reproduced to 1e-9", val["p17b_pass"])
    check("P20.2 total visits agree within 1%", val["p20b_pass_total"])
    check("PHM independent of the inspection scenario", val["phm_scenario_independence_max_abs_diff"] <= 1e-12)
    print(json.dumps({k: v for k, v in val.items() if k.startswith("p20b_max") or k.startswith("p17b_max")}, indent=2))
    if problems:
        print("FAILED:", problems)
        sys.exit(1)
    print("P21.1 verification passed")


if __name__ == "__main__":
    main()
