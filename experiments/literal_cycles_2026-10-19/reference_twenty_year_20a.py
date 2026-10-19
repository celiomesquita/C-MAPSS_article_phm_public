"""P20.1: 20-year renewal scenario for four subsets and three arms (AGE127, PHM, PHM + inspection)."""

import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import pilot_scale_bridge_12b as bridge
from pilot_renewal_12a import EVENT_CODE

ROOT = bridge.ROOT
ART = bridge.ART
OUT = ART / "pilot_twenty_year_20a"
SRC_DEV = ART / "pilot_policy_selection_13a/decisions.csv"
SRC_CONF = ART / "confirmation_19a/decisions.csv"
SUBSETS = ("FD001", "FD002", "FD003", "FD004")
BASES = ["ISO_LOWER98_M15", "RF_SLOPE_LOWER98_M15", "HI_MARKER", "ISO_POINT_M15", "RF_SLOPE_POINT_M15"]
AGE, STEP = 127, 5
WINDOW, GAMMA = 60, 1.0
R_REPS, SEED = bridge.R_REPS, 20261018
Z_LIMIT = 4.5
SOURCES = ["protocolo_vinte_anos_20a.md", "twenty_year_20a.py", "test_twenty_year_20a.py", "verify_twenty_year_20a.py"]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def event_code(sched, T):
    return 0 if sched < T else (2 if sched == T else 3)


def decision_pmf(T, has, D, d, inspect):
    """Distribution of the decision cycle for one engine (always-valid monitoring). Returns (cycles, probs, tail_prob)."""
    T, tau = int(T), AGE-d
    times = np.arange(AGE, T, STEP) if inspect else np.array([], int)
    start = min(tau, int(times[0])) if len(times) else tau
    if has and int(D) < start:
        return np.array([int(D)]), np.array([1.]), 0.
    end = int(D) if has else T-1
    t = np.arange(start, end+1)
    phm = (t == D) if has else np.zeros(len(t), bool)
    in_grid = np.isin(t, times)
    q = 1.-np.clip((T-t)/WINDOW, 0., 1.)
    p = np.where(in_grid & ~phm, q**GAMMA, 0.)           # p_P = 0, p_F = 1
    hazard = np.where(phm, 1., p)
    survive = np.concatenate([[1.], np.cumprod(1.-hazard)])[:-1]
    prob = survive*hazard
    keep = prob > 0
    tail = 0. if has else float(np.prod(1.-hazard))
    return t[keep], prob[keep], tail


def build_atoms(frame, policy_id, d, kind):
    """Per-engine outcome atoms for an arm: arrays engine_index, util, event, prob (within-engine)."""
    rows = frame.sort_values("unit")
    eng, util, ev, pr = [], [], [], []
    for i, r in enumerate(rows.itertuples(index=False)):
        T = int(r.endpoint)
        if kind == "AGE":
            cycles, probs, tail = decision_pmf(T, True, AGE-d, d, False)
        else:
            has = bool(r.has_decision)
            cycles, probs, tail = decision_pmf(T, has, float(r.decision) if has else np.nan, d, kind == "HYB")
        for c, pcy in zip(cycles, probs):
            s = int(c)+d
            eng.append(i); util.append(float(min(s, T))); ev.append(event_code(s, T)); pr.append(float(pcy))
        if tail > 0:
            eng.append(i); util.append(float(T)); ev.append(1); pr.append(float(tail))
    eng, util, ev, pr = map(np.asarray, (eng, util, ev, pr))
    pr = pr/np.bincount(eng, weights=pr)[eng]               # remove rounding drift
    return dict(engine=eng, util=util, event=ev.astype(int), prob=pr, n=len(rows))


def cumulative_table(atoms):
    """Global monotone table so that a (engine, uniform) pair maps to an atom index with one searchsorted."""
    eng, pr = atoms["engine"], atoms["prob"]
    cum = np.zeros(len(pr))
    for i in range(atoms["n"]):
        sel = np.flatnonzero(eng == i)
        c = np.cumsum(pr[sel])
        c[-1] = 1.
        cum[sel] = c
    return eng+cum


def sample_atoms(atoms, table, engines, v):
    q = engines+np.minimum(v, 1.-1e-12)
    return np.minimum(np.searchsorted(table, q, side="right"), len(table)-1)


def simulate_draws(u_draw, e_draw, atom_u, atom_w, atom_e, k, rho, llp, horizon, ic, init):
    """Renewal with LLP-forced visits (same logic as P12.2 `simulate`), on pre-resolved life draws."""
    n = u_draw.shape[0]
    t = np.zeros(n)
    big = np.inf if llp is None else float(llp)
    if ic == 0:
        a = np.zeros(n)
        rem = k*u_draw[:, 0]
        ev = e_draw[:, 0]
        j = 1
    else:
        weight = atom_w*atom_u
        cdf = np.cumsum(weight)/weight.sum()
        first = np.minimum(np.searchsorted(cdf, init[0], side="right"), len(atom_u)-1)
        rem = rho*k*atom_u[first]*(1.-init[1])
        ev = atom_e[first]
        a = init[2]*big if llp is not None else np.zeros(n)
        j = 0
    alive = np.ones(n, bool)
    d = np.zeros(n, int); l = np.zeros(n, int)
    miss = np.zeros(n, int); exact = np.zeros(n, int); late = np.zeros(n, int)
    while True:
        t_llp = t+(big-a)
        t_deg = t+rem
        is_llp = t_llp <= t_deg
        t_ev = np.where(is_llp, t_llp, t_deg)
        counted = alive & (t_ev <= horizon)
        by_deg = counted & ~is_llp
        d += by_deg
        l += counted & is_llp
        miss += by_deg & (ev == 1); exact += by_deg & (ev == 2); late += by_deg & (ev == 3)
        a = np.where(is_llp, 0., a+rem)
        t = t_ev
        alive = counted
        if not alive.any():
            break
        assert j < u_draw.shape[1], "draw stream exhausted"
        rem = rho*k*u_draw[:, j]
        ev = e_draw[:, j]
        j += 1
    return d, l, miss, exact, late


def arms_for(frame_by_delay):
    arms = {}
    for d, frame in frame_by_delay.items():
        arms[f"AGE127_D{d}"] = build_atoms(frame.loc[frame.policy_id.eq(f"{BASES[0]}_D{d}")], None, d, "AGE")
        for base in BASES:
            sub = frame.loc[frame.policy_id.eq(f"{base}_D{d}")]
            arms[f"PHM_{base}_D{d}"] = build_atoms(sub, base, d, "PHM")
            arms[f"HYB_{base}_D{d}"] = build_atoms(sub, base, d, "HYB")
    return arms


def analytic_rate(atoms):
    """Renewal rate per simulated cycle: 1 / E[utilised life] with engine and outcome drawn independently."""
    per_engine = np.bincount(atoms["engine"], weights=atoms["prob"]*atoms["util"], minlength=atoms["n"])
    return 1./per_engine.mean()


def run_cell(arms, tables, k, rho, llp, ic, horizon, seed_list):
    names = sorted(arms)
    nmax = int(np.ceil(horizon/(min(rho, 1.)*k*min(a["util"].min() for a in arms.values()))))+(int(np.ceil(horizon/llp)) if llp else 0)+6
    rng = np.random.default_rng(seed_list)
    n_eng = arms[names[0]]["n"]
    engines = rng.integers(0, n_eng, (R_REPS, nmax))
    v = rng.random((R_REPS, nmax))
    init = rng.random((3, R_REPS))
    out = {}
    for name in names:
        atoms = arms[name]
        sel = sample_atoms(atoms, tables[name], engines, v)
        w = atoms["prob"]/n_eng
        out[name] = simulate_draws(atoms["util"][sel], atoms["event"][sel], atoms["util"], w, atoms["event"], k, rho, llp, horizon, ic, init)
    return out


def load_frames():
    dev = pd.read_csv(SRC_DEV)
    conf = pd.read_csv(SRC_CONF)
    cols = ["subset", "repeat", "unit", "policy_id", "delay", "has_decision", "decision", "endpoint"]
    return pd.concat([f.loc[f.dataset.eq("complete"), cols] for f in (dev, conf)], ignore_index=True)


def mean_lives():
    out = dict(bridge.mean_lives())
    for s in ("FD002", "FD004"):
        out[s] = float(pd.read_csv(ART/"confirmation_19a"/f"lives_{s}.csv")["T"].mean())
    return out


def grid():
    for li, lref in enumerate(bridge.L_REF):
        for ui, u_yr in enumerate(bridge.UTILISATION):
            for sc, (llp, ic, rho) in enumerate(itertools.product(bridge.LLP, bridge.IC, bridge.RHO)):
                yield li, lref, ui, u_yr, sc, llp, ic, rho


def refresh_manifest(out):
    (out/"manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(out.iterdir())
                                                 if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")


def main():
    assert not (OUT/"metadata.json").exists(), "completed run must be preserved"
    OUT.mkdir(parents=True, exist_ok=True)
    previous = {}
    for folder in sorted(ART.glob("pilot_*")):
        mf = folder/"manifest.json"
        if folder != OUT and mf.exists():
            for name, digest in json.loads(mf.read_text(encoding="utf-8")).items():
                assert sha(folder/name) == digest, (folder.name, name)
            previous[folder.name] = sha(mf)
    start = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=previous,
                 sources={n: sha(ROOT/"experiments"/n) for n in SOURCES},
                 inputs={"development": sha(SRC_DEV), "confirmation": sha(SRC_CONF)})
    (OUT/"execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    frames = load_frames()
    tbar = mean_lives()
    cells, pairs = [], []
    for di, subset in enumerate(SUBSETS):
        for repeat in (1, 2, 3):
            f = frames.loc[frames.subset.eq(subset) & frames.repeat.eq(repeat)]
            arms = arms_for({d: f.loc[f.delay.eq(d)] for d in (1, 2)})
            tables = {n: cumulative_table(a) for n, a in arms.items()}
            rates = {n: analytic_rate(a) for n, a in arms.items()}
            print(subset, repeat, len(arms), "arms", flush=True)
            for li, lref, ui, u_yr, sc, llp, ic, rho in grid():
                k = lref/tbar[subset]
                horizon = bridge.YEARS*u_yr
                res = run_cell(arms, tables, k, rho, llp, ic, horizon, [SEED, di, repeat, li, ui, sc])
                base = dict(subset=subset, repeat=repeat, L_ref=lref, k=k, u_yr=u_yr, horizon_fc=horizon,
                            llp=llp if llp else 0., ic=ic, rho=rho)
                for name, (dv, lv, miss, exact, late) in res.items():
                    tot = dv+lv
                    cells.append(dict(base, arm=name, d_mean=dv.mean(), l_mean=lv.mean(), tot_mean=tot.mean(),
                                      tot_sd=tot.std(ddof=1), miss_mean=miss.mean(), exact_mean=exact.mean(),
                                      late_mean=late.mean(), analytic_rate=rates[name],
                                      expected_stationary=horizon*rates[name]/k))
                for dly in (1, 2):
                    ref = f"AGE127_D{dly}"
                    for name in res:
                        if name == ref or not name.endswith(f"_D{dly}"):
                            continue
                        comparisons = [(name, ref)]
                        if name.startswith("HYB_"):
                            comparisons.append((name, name.replace("HYB_", "PHM_", 1)))
                        for a, b in comparisons:
                            diff = (res[a][0]+res[a][1])-(res[b][0]+res[b][1])
                            se = diff.std(ddof=1)/np.sqrt(R_REPS)
                            an = rates[a]-rates[b]
                            pairs.append(dict(base, delay=dly, a=a, b=b, diff_mean=diff.mean(), diff_se=se,
                                              analytic_diff=an, status=bridge.classify(diff.mean(), se, an)))
    cells = pd.DataFrame(cells)
    pairs = pd.DataFrame(pairs)
    cells.to_csv(OUT/"cells.csv.gz", index=False)
    pairs.to_csv(OUT/"pairs.csv.gz", index=False)
    sel = cells[(cells.llp == 0) & (cells.ic == 1) & (cells.rho == 1.)].copy()
    sel["z"] = (sel.tot_mean-sel.expected_stationary)/(sel.tot_sd/np.sqrt(R_REPS))
    sel.to_csv(OUT/"validation_stationary.csv", index=False)
    llp_range = cells[cells.llp > 0].groupby(["subset", "repeat", "L_ref", "u_yr", "llp", "ic", "rho"]).l_mean.agg(lambda s: s.max()-s.min())
    validation = dict(stationary_cells=len(sel), stationary_max_abs_z=float(sel.z.abs().max()),
                      stationary_pass=bool(sel.z.abs().max() < Z_LIMIT), llp_equal_max_range=float(llp_range.max()),
                      llp_pass=bool(llp_range.max() < 1e-12))
    # long horizon, both initial conditions, no LLP, one repetition per subset
    long_rows = []
    for di, subset in enumerate(SUBSETS):
        f = frames.loc[frames.subset.eq(subset) & frames.repeat.eq(1)]
        arms = arms_for({1: f.loc[f.delay.eq(1)]})
        tables = {n: cumulative_table(a) for n, a in arms.items()}
        k = 8425./tbar[subset]
        for ic in (0, 1):
            res = run_cell(arms, tables, k, 1., None, ic, bridge.LONG_H, [SEED, di, 99, 99, 99, ic])
            for name, (dv, *_) in res.items():
                rate = analytic_rate(arms[name])/k
                long_rows.append(dict(subset=subset, arm=name, ic=ic, relative_error=dv.mean()/bridge.LONG_H/rate-1.))
    long = pd.DataFrame(long_rows)
    long.to_csv(OUT/"validation_long_horizon.csv", index=False)
    validation.update(long_horizon_max_abs_rel_error=float(long.relative_error.abs().max()),
                      long_horizon_pass=bool(long.relative_error.abs().max() <= .01))
    (OUT/"validation.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")
    for n in SOURCES:
        (OUT/f"source_{n}").write_bytes((ROOT/"experiments"/n).read_bytes())
    (OUT/"metadata.json").write_text(json.dumps(start | dict(finished_utc=datetime.now(timezone.utc).isoformat(),
                                    validation=validation, cells=len(cells), pairs=len(pairs)), indent=2), encoding="utf-8")
    refresh_manifest(OUT)
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
