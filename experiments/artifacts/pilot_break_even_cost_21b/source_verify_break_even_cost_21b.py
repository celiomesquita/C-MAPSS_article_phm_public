"""Independent verification of P21.2 (break_even_cost_21b.py) from the raw archived expectations."""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

import verify_break_even_21a as v

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_break_even_cost_21b"
QS = [0., .005, .01, .02]
BOOT, SEED = v.BOOT, v.SEED
BETAS = v.BETAS


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def close(a, b, rtol=1e-9, atol=1e-12):
    return v.close(a, b, rtol, atol)


def classify_vec(dW, dE, tol):
    sw = np.sign(np.where(np.abs(dW) <= tol, 0., dW))
    se = np.sign(np.where(np.abs(dE) <= tol, 0., dE))
    out = np.zeros(np.shape(dW), dtype=int)
    out[(sw <= 0) & (se >= 0) & ~((sw == 0) & (se == 0))] = 1
    out[(sw >= 0) & (se <= 0) & ~((sw == 0) & (se == 0))] = 2
    out[(sw > 0) & (se > 0)] = 3
    out[(sw < 0) & (se < 0)] = 4
    return out


def inspections(main, latent, origin, subset, repeat, delay, arm, kind, scen, u):
    if kind != "HYB":
        return None
    src = latent if str(scen).startswith("L") else main
    h = src.loc[(src.origin == origin) & (src.subset == subset) & (src.repeat == repeat) & (src.delay == delay)
                & (src.base == arm) & (src.scenario == scen) & (src.u == u)].sort_values(["fold", "unit"])
    return h.inspections.to_numpy(float)


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

    def rd(name):
        return pd.read_csv(OUT / name, keep_default_na=False, na_values=[""])
    contrasts, prefs, rates, front, summary = rd("contrasts.csv"), rd("preference_curves.csv"), rd("rates.csv"), rd("frontier.csv"), rd("contrast_summary.csv")
    manifest = json.loads((OUT / "manifest.json").read_text(encoding="utf-8"))
    check("manifest hashes", all(sha(OUT / k) == x for k, x in manifest.items()))
    meta = json.loads((OUT / "metadata.json").read_text(encoding="utf-8"))
    check("configuration (B, seed, q grid)", meta["boot"] == BOOT and meta["seed"] == SEED and meta["qs"] == QS)
    key = ["origin", "subset", "repeat", "delay", "q_inspection"]
    cnt = contrasts.groupby(key).size()
    check("108 contrasts per cell, delay and q", set(cnt) == {108} and len(cnt) == 24*len(QS))
    check("no duplicated contrast", not contrasts.duplicated(key+["contrast", "scenario", "u"]).any())

    cell_index = {k: i for i, k in enumerate(sorted(contrasts[["origin", "subset", "repeat"]].drop_duplicates().itertuples(index=False, name=None)))}
    bad = nrow = 0
    pref_ok = True
    for (origin, subset, repeat), cg in contrasts.groupby(["origin", "subset", "repeat"], sort=True):
        n = int(cg.engines.iloc[0])
        rng = np.random.default_rng([SEED, cell_index[(origin, subset, repeat)]])
        counts = rng.multinomial(n, np.full(n, 1./n), size=BOOT).astype(float)
        cache = {}

        def vec(delay, label, scen, u):
            arm, kind = label.split("|")
            k = (delay, label, scen if kind == "HYB" else "", u if kind != "AGE" else 0.)
            if k not in cache:
                ut, ev, order = v.engine_vectors(main_ex, latent, sel, origin, subset, repeat, delay, arm, kind, scen, u)
                ins = inspections(main_ex, latent, origin, subset, repeat, delay, arm, kind, scen, u)
                cache[k] = (ut, ev, np.zeros(n) if ins is None else ins, order)
            return cache[k]
        for r in cg.itertuples(index=False):
            scen = r.scenario if isinstance(r.scenario, str) else ""
            uA, eA, nA, oA = vec(r.delay, r.A, scen, r.u)
            uB, eB, nB, oB = vec(r.delay, r.B, scen, r.u)
            if oA != oB:
                bad += 1
                continue
            q = r.q_inspection
            wA, wB = (n+q*nA.sum())/uA.sum(), (n+q*nB.sum())/uB.sum()
            gA, gB = eA.sum()/uA.sum(), eB.sum()/uB.sum()
            tol = 1e-9*wB
            dW, dE = wA-wB, gB-gA
            code = int(classify_vec(np.array(dW), np.array(dE), tol))

            def dot(x):
                return np.einsum("bn,n->b", counts, x)
            wAb, wBb = (n+q*dot(nA))/dot(uA), (n+q*dot(nB))/dot(uB)
            gAb, gBb = dot(eA)/dot(uA), dot(eB)/dot(uB)
            dWb, dEb = wAb-wBb, gBb-gAb
            cb = classify_vec(dWb, dEb, tol)
            lo, hi = np.quantile(dEb, [.025, .975])
            bounded = code in (3, 4) and (lo > tol or hi < -tol)
            ok = (close(1e4*wA, r.rate_A) and close(1e4*wB, r.rate_B) and close(1e4*gA, r.event_rate_A) and close(1e4*gB, r.event_rate_B)
                  and close(1e4*dW, r.dW) and close(1e4*dE, r.dE) and v.CLASS[code] == r.cls
                  and close(1e4*np.quantile(dWb, .025), r.dW_low) and close(1e4*np.quantile(dWb, .975), r.dW_high)
                  and close(1e4*lo, r.dE_low) and close(1e4*hi, r.dE_high)
                  and close(1e4*(nA.sum()/uA.sum()-nB.sum()/uB.sum()), r.dNu)
                  and close(nA.mean(), r.inspections_per_engine_A) and close(nB.mean(), r.inspections_per_engine_B)
                  and int((eA > 1e-12).sum()) == r.engines_event_A and int((eB > 1e-12).sum()) == r.engines_event_B
                  and close([float(np.mean(cb == c)) for c in (1, 2, 3, 4, 0)],
                            [r.boot_A_dominates, r.boot_B_dominates, r.boot_A_above, r.boot_A_below, r.boot_tie])
                  and bool(r.beta0_bounded) == bool(bounded))
            ok = ok and (close(dW/dE, r.beta0) if code in (3, 4) else np.isnan(r.beta0))
            if bounded:
                ratio = dWb[cb == code]/dEb[cb == code]
                ok = ok and close(np.quantile(ratio, .025), r.beta0_low) and close(np.quantile(ratio, .975), r.beta0_high)
            bad += 0 if ok else 1
            nrow += 1
            pr = prefs.loc[prefs.row_id.eq(r.row_id) & prefs.origin.eq(origin) & prefs.subset.eq(subset) & prefs.repeat.eq(repeat)
                           & prefs.delay.eq(r.delay) & np.isclose(prefs.q_inspection, q)]
            for beta in BETAS:
                p = pr.loc[np.isclose(pr.beta, beta)]
                gap = dWb-beta*dEb
                g0 = dW-beta*dE
                point = 1 if g0 < -tol else (-1 if g0 > tol else 0)
                if len(p) != 1 or not (close(p.boot_A_cheaper.iloc[0], float(np.mean(gap < -tol))) and close(p.boot_B_cheaper.iloc[0], float(np.mean(gap > tol)))
                                       and int(p.point.iloc[0]) == point):
                    pref_ok = False
    check(f"{nrow} contrast rows rebuilt from raw sources (all q)", bad == 0 and nrow == len(contrasts))
    check("preference curves rebuilt", pref_ok and len(prefs) == len(contrasts)*len(BETAS))

    r_bad = 0
    for r in rates.itertuples(index=False):
        scen = r.scenario if isinstance(r.scenario, str) else ""
        ut, ev, _ = v.engine_vectors(main_ex, latent, sel, r.origin, r.subset, r.repeat, r.delay, r.arm, r.kind, scen, r.u)
        ins = inspections(main_ex, latent, r.origin, r.subset, r.repeat, r.delay, r.arm, r.kind, scen, r.u)
        ins = np.zeros(len(ut)) if ins is None else ins
        w = (len(ut)+r.q_inspection*ins.sum())/ut.sum()
        if not (close(1e4*w, r.restoration_equivalent_rate) and close(1e4*ev.sum()/ut.sum(), r.event_rate)
                and close(1e4*ins.sum()/ut.sum(), r.inspection_rate) and close(ins.mean(), r.inspections_per_engine)):
            r_bad += 1
    check(f"{len(rates)} arm rates rebuilt", r_bad == 0)

    f_bad = 0
    for k, g in front.groupby(key):
        for a in g.itertuples(index=False):
            dom = [b for b in g.itertuples(index=False) if (b.arm, b.kind) != (a.arm, a.kind)
                   and b.restoration_equivalent_rate <= a.restoration_equivalent_rate*(1+1e-9)
                   and b.event_rate <= a.event_rate+1e-9*a.restoration_equivalent_rate
                   and (b.restoration_equivalent_rate < a.restoration_equivalent_rate*(1-1e-9) or b.event_rate < a.event_rate-1e-9*a.restoration_equivalent_rate)]
            if bool(a.dominated) != bool(dom):
                f_bad += 1
    check("frontier dominance recomputed", f_bad == 0)

    s_bad = 0
    for k, g in contrasts.groupby(["origin", "subset", "delay", "q_inspection", "contrast", "scenario", "u"], dropna=False):
        s = summary.loc[(summary.origin == k[0]) & (summary.subset == k[1]) & (summary.delay == k[2]) & np.isclose(summary.q_inspection, k[3])
                        & (summary.contrast == k[4]) & (summary.u == k[6])]
        s = s.loc[s.scenario.isna()] if (isinstance(k[5], float) or k[5] == "") else s.loc[s.scenario == k[5]]
        if len(s) != 1 or not (close(g.dW.min(), s.dW_min.iloc[0]) and close(g.dW.max(), s.dW_max.iloc[0]) and close(g.dE.min(), s.dE_min.iloc[0])
                               and close(g.dNu.max(), s.dNu_max.iloc[0]) and int(g.beta0_bounded.sum()) == int(s.beta0_bounded_repeats.iloc[0])):
            s_bad += 1
    check("repeat ranges summarised correctly", s_bad == 0)

    val = json.loads((OUT / "validation.json").read_text(encoding="utf-8"))
    check("q=0 reproduces P21.1", val["q0_pass"])
    check("inspection counts reproduce P17.1 summary", val["p17b_inspections_pass"])
    check("non-hybrid arms have no inspections", val["non_hybrid_inspections_max"] == 0.)
    check("restoration-equivalent cost of the hybrid arm is monotone in q", val["monotone_in_q"])
    if problems:
        print("FAILED:", problems)
        sys.exit(1)
    print("P21.2 verification passed")


if __name__ == "__main__":
    main()
