"""Independent verifier for P12.2: per-replicate loop reimplementation on a stratified subset of cells, invariants, signs, manifests."""
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_scale_bridge_12b"
SRC = ART / "pilot_policy_selection_13a/decisions.csv"
SEED, R = 20261018, 2000
SUBSETS = ("FD001", "FD003")
L_REF = (4000.0, 5000.0, 6000.0, 7000.0, 8425.0, 10000.0, 12000.0, 14000.0, 16500.0, 19000.0)
UTIL = (1400.0, 1600.0, 1900.0)
LLPS = (None, 20000.0, 25000.0, 30000.0)
POLICIES = ("AGE_D1", "HI_MARKER_D1", "ISO_LOWER98_M15_D1")


def raw_lives():
    d = pd.read_csv(SRC)
    d = d[d.dataset == "complete"]
    lives = {}
    for (s, r, p), g in d.groupby(["subset", "repeat", "policy_id"]):
        g = g.sort_values("unit")
        has = g.has_decision.to_numpy(bool)
        sched = np.nan_to_num(g.scheduled.to_numpy(float), nan=1e18)
        end = g.endpoint.to_numpy(float)
        u = np.where(has, np.minimum(sched, end), end)
        ev = np.where(~has, 1, np.where(g.exact_endpoint.to_numpy(bool), 2, np.where(g.late.to_numpy(bool), 3, 0)))
        lives[(s, int(r), p)] = (u, ev)
    return lives


def tau_b(x, y):
    n, c, d, tx, ty = len(x), 0, 0, 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            a, b = np.sign(x[i] - x[j]), np.sign(y[i] - y[j])
            if a == 0 and b == 0:
                continue
            if a == 0:
                tx += 1
            elif b == 0:
                ty += 1
            elif a == b:
                c += 1
            else:
                d += 1
    return (c - d) / np.sqrt((c + d + tx) * (c + d + ty))


def loop_replicate(u, e, k, rho, llp, horizon, ic, idx_row, init):
    """One replicate, pure Python, same semantics as the protocol."""
    t, j = 0.0, 0
    big = float("inf") if llp is None else llp
    if ic == 0:
        a, eng, rem, j = 0.0, idx_row[0], k * u[idx_row[0]], 1
    else:
        total, acc, eng = u.sum(), 0.0, len(u) - 1
        for i in range(len(u)):
            acc += u[i]
            if init[0] < acc / total:
                eng = i
                break
        rem = rho * k * u[eng] * (1.0 - init[1])
        a = init[2] * big if llp is not None else 0.0
    d = l = miss = exact = late = 0
    while True:
        t_llp, t_deg = t + (big - a), t + rem
        forced = t_llp <= t_deg
        t_ev = t_llp if forced else t_deg
        if t_ev > horizon:
            break
        if forced:
            l += 1
            a = 0.0
        else:
            d += 1
            miss += e[eng] == 1
            exact += e[eng] == 2
            late += e[eng] == 3
            a += rem
        t = t_ev
        eng = idx_row[j]
        j += 1
        rem = rho * k * u[eng]
    return d, l, miss, exact, late


def main():
    lives = raw_lives()
    cells = pd.read_csv(OUT / "cells.csv.gz")
    pairs = pd.read_csv(OUT / "pairs.csv.gz")
    tbar = {}
    for s in SUBSETS:
        raw = pd.read_csv(ROOT / f"CMAPSSData/train_{s}.txt", sep=r"\s+", header=None, usecols=[0, 1], names=["unit", "cycle"])
        tbar[s] = float(raw.groupby("unit").cycle.max().mean())
    rates = {key: len(v[0]) / v[0].sum() for key, v in lives.items()}
    scen = list(itertools.product(LLPS, (0, 1), (1.0, 0.8)))
    checked = 0
    for sc, (llp, ic, rho) in enumerate(scen):
        for di, subset in enumerate(SUBSETS):
            repeat = 1 + (sc + di) % 3
            li = (sc * 3 + di * 5) % len(L_REF)
            ui = (sc + di) % len(UTIL)
            lref, u_yr = L_REF[li], UTIL[ui]
            k, horizon = lref / tbar[subset], 20 * u_yr
            u_min = min(lives[(subset, repeat, p)][0].min() for pp in [None] for p in {kk[2] for kk in lives})
            nmax = int(np.ceil(horizon / (min(rho, 1.0) * k * u_min))) + (int(np.ceil(horizon / llp)) if llp else 0) + 6
            rng = np.random.default_rng([SEED, di, repeat, li, ui, sc])
            idx = rng.integers(0, 100, (R, nmax))
            init = rng.random((3, R))
            res = {}
            for pol in POLICIES:
                u, e = lives[(subset, repeat, pol)]
                res[pol] = np.array([loop_replicate(u, e, k, rho, llp, horizon, ic, idx[r], init[:, r]) for r in range(R)], float)
                row = cells[(cells["subset"] == subset) & (cells["repeat"] == repeat) & (cells.L_ref == lref) & (cells.u_yr == u_yr) &
                            (cells.llp == (llp or 0.0)) & (cells.ic == ic) & (cells.rho == rho) & (cells.policy_id == pol)]
                assert len(row) == 1, (subset, repeat, lref, u_yr, llp, ic, rho, pol)
                row = row.iloc[0]
                r_ = res[pol]
                tot = r_[:, 0] + r_[:, 1]
                for name, val in (("d_mean", r_[:, 0].mean()), ("l_mean", r_[:, 1].mean()), ("tot_mean", tot.mean()),
                                  ("tot_sd", tot.std(ddof=1)), ("miss_mean", r_[:, 2].mean()), ("exact_mean", r_[:, 3].mean()),
                                  ("late_mean", r_[:, 4].mean())):
                    assert abs(row[name] - val) < 1e-9, (name, row[name], val)
                assert abs(row.analytic_rate - rates[(subset, repeat, pol)]) < 1e-15
                checked += 1
            for a_pol, b_pol in (("ISO_LOWER98_M15_D1", "HI_MARKER_D1"), ("ISO_LOWER98_M15_D1", "AGE_D1")):
                diff = (res[a_pol][:, 0] + res[a_pol][:, 1]) - (res[b_pol][:, 0] + res[b_pol][:, 1])
                se = diff.std(ddof=1) / np.sqrt(R)
                an = rates[(subset, repeat, a_pol)] - rates[(subset, repeat, b_pol)]
                if se == 0:
                    status = "indistinguivel" if diff.mean() == 0 else ("estavel" if np.sign(diff.mean()) == np.sign(an) else "invertido")
                elif abs(diff.mean()) < 2 * se:
                    status = "indistinguivel"
                else:
                    status = "estavel" if np.sign(diff.mean()) == np.sign(an) else "invertido"
                prow = pairs[(pairs["subset"] == subset) & (pairs["repeat"] == repeat) & (pairs.L_ref == lref) & (pairs.u_yr == u_yr) &
                             (pairs.llp == (llp or 0.0)) & (pairs.ic == ic) & (pairs.rho == rho) & (pairs.a == a_pol) & (pairs.b == b_pol)]
                assert len(prow) == 1
                prow = prow.iloc[0]
                assert abs(prow.diff_mean - diff.mean()) < 1e-9 and abs(prow.diff_se - se) < 1e-9 and prow.status == status
                assert np.sign(prow.analytic_diff) == np.sign(an) and abs(prow.analytic_diff - an) < 1e-15
    # invariants on the full table
    llp_rows = cells[cells.llp > 0].groupby(["subset", "repeat", "L_ref", "u_yr", "llp", "ic", "rho"]).l_mean.agg(lambda s: s.max() - s.min())
    assert llp_rows.max() < 1e-12
    k_calc = cells[["subset", "L_ref", "k"]].drop_duplicates()
    for _, r in k_calc.iterrows():
        assert abs(r.k - r.L_ref / tbar[r["subset"]]) < 1e-12
    stat = cells[(cells.llp == 0) & (cells.ic == 1) & (cells.rho == 1.0)]
    z = (stat.tot_mean - horizon_expected(stat)) / (stat.tot_sd / np.sqrt(R))
    assert z.abs().max() < 4.0, float(z.abs().max())
    kend = pd.read_csv(OUT / "kendall.csv.gz")
    sample = kend.iloc[::577]
    for _, r in sample.iterrows():
        sub = cells[(cells["subset"] == r["subset"]) & (cells["repeat"] == r["repeat"]) & (cells.L_ref == r.L_ref) & (cells.u_yr == r.u_yr) &
                    (cells.llp == r.llp) & (cells.ic == r.ic) & (cells.rho == r.rho)].sort_values("policy_id")
        assert len(sub) == 16
        assert abs(tau_b(sub.tot_mean.to_numpy(), sub.analytic_rate.to_numpy()) - r.kendall_tau) < 1e-9
    validation = json.loads((OUT / "validation.json").read_text(encoding="utf-8"))
    assert validation["stationary_pass"] and validation["long_horizon_pass"] and validation["llp_pass"]
    for folder in sorted(ART.glob("pilot_*")):
        mf = folder / "manifest.json"
        if folder == OUT or not mf.exists():
            continue
        for n, h in json.loads(mf.read_text(encoding="utf-8")).items():
            assert hashlib.sha256((folder / n).read_bytes()).hexdigest() == h, (folder.name, n)
    result = dict(status="passed", cell_policy_rows_replayed=checked, cells=len(cells), pairs=len(pairs),
                  max_abs_stationary_z=float(z.abs().max()), kendall_rows_checked=len(sample))
    (OUT / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(result)


def horizon_expected(df):
    return df.horizon_fc * df.analytic_rate / df.k


if __name__ == "__main__":
    main()
