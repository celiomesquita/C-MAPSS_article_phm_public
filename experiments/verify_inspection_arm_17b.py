"""Independent verifier for the inspection-arm outputs: scalar loops over cycles, no shared code with the module.
Usage: py verify_inspection_arm_17b.py"""
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT/"experiments/artifacts"
OUT = ART/"pilot_inspection_17b"
AGE = 127


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


CFG = {"S2_W60_g1": ("S2", 60, 1., 0.), "S2_W30_g1": ("S2", 30, 1., 0.), "S2_W80_g1": ("S2", 80, 1., 0.),
       "S2_W60_g0.26": ("S2", 60, .26, 0.), "S2_W60_g2": ("S2", 60, 2., 0.), "S2_W60_g1_pP0.02": ("S2", 60, 1., .02),
       "S1_W30_g1": ("S1", 30, 1., 0.), "S1_W60_g1": ("S1", 60, 1., 0.), "S1_W80_g1": ("S1", 80, 1., 0.)}


def one(T, has, D, d, u, entry, W, g, pP):
    T = int(T)
    tau = AGE-d
    first = AGE if entry == "S2" else max(1, T-W)
    grid = []
    t = first
    while t <= T-1:
        grid.append(t)
        t += 5
    start = min(tau, grid[0]) if grid else tau
    if has and D < start:
        s = int(D)+d
        return min(s, T), float(s > T), float(s == T), 0., 0., 0.
    util = late = exact = insp = rej = 0.
    alive = 1.
    t = start
    while True:
        if has and t > D:
            break
        if (not has) and t > T-1:
            util += alive*T
            miss = alive
            return util, late, exact, miss, insp, rej
        loss = u if t >= tau else 0.
        # invalid monitoring
        pr = alive*loss
        s = t+d
        util += pr*min(s, T)
        late += pr*(1. if s > T else 0.)
        exact += pr*(1. if s == T else 0.)
        ok = alive*(1.-loss)
        if has and t == D:
            util += ok*min(s, T)
            late += ok*(1. if s > T else 0.)
            exact += ok*(1. if s == T else 0.)
            return util, late, exact, 0., insp, rej
        if t in grid:
            q = 1.-min(max((T-t)/W, 0.), 1.)
            p = pP+(1.-pP)*q**g
            insp += ok
            rej += ok*p
            util += ok*p*min(s, T)
            late += ok*p*(1. if s > T else 0.)
            exact += ok*p*(1. if s == T else 0.)
            alive = ok*(1.-p)
        else:
            alive = ok
        t += 1
    return util, late, exact, 0., insp, rej


def phm(T, has, D, d, u):
    T = int(T)
    tau = AGE-d
    if has and D <= tau:
        s = int(D)+d
        return min(s, T), float(s > T), float(s == T), 0.
    util = late = exact = 0.
    alive = 1.
    t = tau
    end = int(D) if has else T-1
    while t <= end:
        h = 1. if (has and t == D) else u
        s = t+d
        util += alive*h*min(s, T)
        late += alive*h*(1. if s > T else 0.)
        exact += alive*h*(1. if s == T else 0.)
        alive *= 1.-h
        t += 1
    miss = 0. if has else alive
    return util+alive*T*(0. if has else 1.), late, exact, miss


def main():
    meta = json.loads((OUT/"metadata.json").read_text(encoding="utf-8"))
    for name, digest in json.loads((OUT/"manifest.json").read_text(encoding="utf-8")).items():
        assert sha(OUT/name) == digest, name
    for folder, digest in meta["previous_manifests"].items():
        assert sha(ART/folder/"manifest.json") == digest, folder
    for key, path in {"development": ART/"pilot_policy_selection_13a/decisions.csv",
                      "confirmation": ART/"confirmation_19a/decisions.csv"}.items():
        assert sha(path) == meta["inputs"][key], key
    ex = pd.read_csv(OUT/"expectations.csv.gz")
    src = pd.concat([pd.read_csv(ART/"pilot_policy_selection_13a/decisions.csv").assign(origin="development"),
                     pd.read_csv(ART/"confirmation_19a/decisions.csv").assign(origin="confirmation")])
    src = src.loc[src.dataset.eq("complete")].set_index(["origin", "subset", "repeat", "unit", "policy_id"])
    assert src.index.is_unique
    for r in ex.itertuples(index=False):
        row = src.loc[(r.origin, r.subset, r.repeat, r.unit, f"{r.base}_D{r.delay}")]
        has = bool(row.has_decision)
        D = float(row.decision) if has else np.nan
        assert int(row.endpoint) == r.T and int(row.delay) == r.delay
        entry, W, g, pP = CFG[r.scenario]
        u, l, e, mi, ins, rj = one(r.T, has, D, r.delay, r.u, entry, W, g, pP)
        assert abs(u-r.util_h) < 1e-8 and abs(l-r.late_h) < 1e-9 and abs(e-r.exact_h) < 1e-9 and abs(mi-r.missing_h) < 1e-9
        assert abs(ins-r.inspections) < 1e-8 and abs(rj-r.rejection) < 1e-9, r
        up, lp, ep, mp = phm(r.T, has, D, r.delay, r.u)
        assert abs(up-r.util_p) < 1e-8 and abs(lp-r.late_p) < 1e-9 and abs(ep-r.exact_p) < 1e-9 and abs(mp-r.missing_p) < 1e-9
        assert r.util_h <= r.util_p+1e-9 and r.missing_h <= r.missing_p+1e-9
    summary = pd.read_csv(OUT/"summary.csv")
    rng = np.random.default_rng(20261018)
    checked = 0
    for key, g in ex.groupby(["origin", "subset", "repeat", "base", "delay", "scenario", "u"], sort=True):
        n = len(g)
        a, b = g.util_h.to_numpy(), g.util_p.to_numpy()
        idx = rng.integers(0, n, size=(2000, n))
        change = b[idx].sum(axis=1)/a[idx].sum(axis=1)-1.
        s = summary.loc[(summary.origin == key[0]) & (summary.subset == key[1]) & (summary.repeat == key[2]) &
                        (summary.base == key[3]) & (summary.delay == key[4]) & (summary.scenario == key[5]) &
                        (summary.u == key[6])]
        assert len(s) == 1
        s = s.iloc[0]
        assert s.engines == n and abs(s.rate_h_per_10000-10000*n/a.sum()) < 1e-9
        assert abs(s.rate_change-(b.sum()/a.sum()-1.)) < 1e-12
        assert abs(s.rate_change_low-np.quantile(change, .025)) < 1e-12 and abs(s.rate_change_high-np.quantile(change, .975)) < 1e-12
        assert abs(s.life_ceded-(b-a).mean()) < 1e-9 and abs(s.saving_vs_127-(1-AGE*n/a.sum())) < 1e-12
        assert abs(s.late_h_per100-100*g.late_h.mean()) < 1e-9 and abs(s.missing_p_per100-100*g.missing_p.mean()) < 1e-9
        checked += 1
    assert checked == len(summary)
    print(json.dumps(dict(verified=True, expectation_rows=len(ex), summary_rows=checked), indent=2))


if __name__ == "__main__":
    main()
