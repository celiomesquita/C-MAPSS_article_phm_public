"""Independent verifier for P20.1: scalar re-implementation of outcome distributions and of the renewal for sampled cells."""
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT/"experiments/artifacts"
OUT = ART/"pilot_twenty_year_20a"
AGE, STEP, W = 127, 5, 60
R = 2000
BASES = ["ISO_LOWER98_M15", "RF_SLOPE_LOWER98_M15", "HI_MARKER", "ISO_POINT_M15", "RF_SLOPE_POINT_M15"]
L_REF = (4000., 5000., 6000., 7000., 8425., 10000., 12000., 14000., 16500., 19000.)
UTIL = (1400., 1600., 1900.)
LLP = (None, 20000., 25000., 30000.)
SUBSETS = ("FD001", "FD002", "FD003", "FD004")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def outcomes(T, has, D, d, kind):
    """List of (probability, utilised, event) for one engine, scalar loops."""
    tau = AGE-d
    if kind == "AGE":
        has, D = True, tau
    grid = []
    if kind == "HYB":
        t = AGE
        while t <= T-1:
            grid.append(t)
            t += STEP
    start = min([tau]+grid[:1])
    out = []
    if has and D < start:
        s = int(D)+d
        return [(1., float(min(s, T)), 0 if s < T else (2 if s == T else 3))]
    end = int(D) if has else T-1
    alive = 1.
    for t in range(start, end+1):
        if has and t == D:
            h = 1.
        elif t in grid:
            h = 1.-min(max((T-t)/W, 0.), 1.)
        else:
            h = 0.
        if h > 0:
            s = t+d
            out.append((alive*h, float(min(s, T)), 0 if s < T else (2 if s == T else 3)))
        alive *= 1.-h
    if not has and alive > 0:
        out.append((alive, float(T), 1))
    total = sum(p for p, _, _ in out)
    return [(p/total, u, e) for p, u, e in out]


def engines_of(frame, delay, base):
    rows = frame.loc[frame.policy_id.eq(f"{base}_D{delay}")].sort_values("unit")
    return [(int(r.endpoint), bool(r.has_decision), float(r.decision) if bool(r.has_decision) else np.nan) for r in rows.itertuples()]


def arm_outcomes(frame):
    arms = {}
    for d in (1, 2):
        arms[f"AGE127_D{d}"] = [outcomes(T, h, D, d, "AGE") for T, h, D in engines_of(frame, d, BASES[0])]
        for base in BASES:
            eng = engines_of(frame, d, base)
            arms[f"PHM_{base}_D{d}"] = [outcomes(T, h, D, d, "PHM") for T, h, D in eng]
            arms[f"HYB_{base}_D{d}"] = [outcomes(T, h, D, d, "HYB") for T, h, D in eng]
    return arms


def pick(engine_outcomes, v):
    c = 0.
    for p, u, e in engine_outcomes:
        c += p
        if c > v:
            return u, e
    return engine_outcomes[-1][1], engine_outcomes[-1][2]


def renewal(arm, engines, v, init, k, rho, llp, horizon, ic):
    n = len(arm)
    mean_len = np.array([sum(p*u for p, u, _ in o) for o in arm])
    flat = [(p/n, u, e) for o in arm for p, u, e in o]
    wsum = sum(p*u for p, u, _ in flat)
    D = L = miss = exact = late = 0
    res = np.zeros((R, 5), int)
    for r in range(R):
        t = 0.
        big = math.inf if llp is None else llp
        if ic == 0:
            a = 0.
            u0, e0 = pick(arm[engines[r][0]], v[r][0])
            rem, ev, j = k*u0, e0, 1
        else:
            target, c = init[0][r]*wsum, 0.
            sel = flat[-1]
            for item in flat:
                c += item[0]*item[1]
                if c > target:
                    sel = item
                    break
            rem, ev = rho*k*sel[1]*(1.-init[1][r]), sel[2]
            a = init[2][r]*big if llp is not None else 0.
            j = 0
        counts = [0, 0, 0, 0, 0]
        while True:
            t_llp = t+(big-a)
            t_deg = t+rem
            is_llp = t_llp <= t_deg
            t_ev = t_llp if is_llp else t_deg
            if t_ev > horizon:
                break
            if is_llp:
                counts[1] += 1
                a = 0.
            else:
                counts[0] += 1
                counts[2] += ev == 1
                counts[3] += ev == 2
                counts[4] += ev == 3
                a += rem
            t = t_ev
            u, ev = pick(arm[engines[r][j]], v[r][j])
            rem = rho*k*u
            j += 1
        res[r] = counts
    return res


def main():
    meta = json.loads((OUT/"metadata.json").read_text(encoding="utf-8"))
    for name, digest in json.loads((OUT/"manifest.json").read_text(encoding="utf-8")).items():
        assert sha(OUT/name) == digest, name
    for folder, digest in meta["previous_manifests"].items():
        assert sha(ART/folder/"manifest.json") == digest, folder
    assert sha(ART/"pilot_policy_selection_13a/decisions.csv") == meta["inputs"]["development"]
    assert sha(ART/"confirmation_19a/decisions.csv") == meta["inputs"]["confirmation"]
    v = meta["validation"]
    assert v["stationary_pass"] and v["long_horizon_pass"] and v["llp_pass"], v
    cells = pd.read_csv(OUT/"cells.csv.gz")
    pairs = pd.read_csv(OUT/"pairs.csv.gz")
    assert len(cells) == 5760*22 and len(pairs) == 5760*30, (len(cells), len(pairs))
    dev = pd.read_csv(ART/"pilot_policy_selection_13a/decisions.csv")
    conf = pd.read_csv(ART/"confirmation_19a/decisions.csv")
    allf = pd.concat([f.loc[f.dataset.eq("complete")] for f in (dev, conf)])
    lives_mean = {}
    for s in SUBSETS:
        if s in ("FD002", "FD004"):
            lives_mean[s] = float(pd.read_csv(ART/"confirmation_19a"/f"lives_{s}.csv")["T"].mean())
        else:
            raw = pd.read_csv(ROOT/f"CMAPSSData/train_{s}.txt", sep=r"\s+", header=None, usecols=[0, 1], names=["unit", "cycle"])
            lives_mean[s] = float(raw.groupby("unit").cycle.max().mean())
    rate_checked = cell_checked = 0
    sample_scen = list(itertools.product(LLP, (0, 1), (1., .8)))
    for di, subset in enumerate(SUBSETS):
        for repeat in (1, 2, 3):
            frame = allf.loc[allf.subset.eq(subset) & allf.repeat.eq(repeat)]
            arms = arm_outcomes(frame)
            n = len(next(iter(arms.values())))
            rates = {}
            for name, arm in arms.items():
                rates[name] = 1./np.mean([sum(p*u for p, u, _ in o) for o in arm])
                got = cells.loc[(cells.subset == subset) & (cells.repeat == repeat) & (cells.arm == name), "analytic_rate"]
                assert np.allclose(got, rates[name], rtol=1e-12, atol=0), (subset, repeat, name)
                rate_checked += 1
            if repeat != 1:
                continue
            umin = min(u for arm in arms.values() for o in arm for _, u, _ in o)
            combos = [(0, 0, 0), (4, 1, 3), (9, 2, 5), (2, 1, 7), (6, 0, 10), (8, 2, 12), (4, 1, 14), (1, 0, 15), (5, 2, 1), (3, 1, 9), (7, 0, 11), (4, 1, 2)]
            for li, ui, sc in combos:
                llp, ic, rho = sample_scen[sc]
                k = L_REF[li]/lives_mean[subset]
                horizon = 20*UTIL[ui]
                nmax = int(math.ceil(horizon/(min(rho, 1.)*k*umin)))+(int(math.ceil(horizon/llp)) if llp else 0)+6
                rng = np.random.default_rng([20261018, di, repeat, li, ui, sc])
                engines = rng.integers(0, n, (R, nmax))
                vv = rng.random((R, nmax))
                init = rng.random((3, R))
                for name in ("AGE127_D1", "PHM_ISO_POINT_M15_D2", "HYB_ISO_POINT_M15_D1", "HYB_HI_MARKER_D2"):
                    res = renewal(arms[name], engines, vv, init, k, rho, llp, horizon, ic)
                    row = cells.loc[(cells.subset == subset) & (cells.repeat == repeat) & (cells.L_ref == L_REF[li]) &
                                    (cells.u_yr == UTIL[ui]) & (cells.llp == (llp or 0.)) & (cells.ic == ic) &
                                    (cells.rho == rho) & (cells.arm == name)]
                    assert len(row) == 1
                    row = row.iloc[0]
                    tot = res[:, 0]+res[:, 1]
                    assert abs(row.d_mean-res[:, 0].mean()) < 1e-9 and abs(row.l_mean-res[:, 1].mean()) < 1e-9, (subset, li, ui, sc, name)
                    assert abs(row.miss_mean-res[:, 2].mean()) < 1e-9 and abs(row.exact_mean-res[:, 3].mean()) < 1e-9
                    assert abs(row.late_mean-res[:, 4].mean()) < 1e-9 and abs(row.tot_sd-tot.std(ddof=1)) < 1e-9
                    cell_checked += 1
    # pair classification and analytic sign from independent rates
    ok = pairs.copy()
    se0 = ok.diff_se == 0
    rule = np.where(se0, np.where(ok.diff_mean == 0, "indistinguivel", np.where(np.sign(ok.diff_mean) == np.sign(ok.analytic_diff), "estavel", "invertido")),
                    np.where(ok.diff_mean.abs() < 2*ok.diff_se, "indistinguivel", np.where(np.sign(ok.diff_mean) == np.sign(ok.analytic_diff), "estavel", "invertido")))
    assert (rule == ok.status).all()
    print(json.dumps(dict(verified=True, analytic_rates_checked=rate_checked, cells_resimulated=cell_checked,
                          cell_rows=len(cells), pair_rows=len(pairs)), indent=2))


if __name__ == "__main__":
    main()
