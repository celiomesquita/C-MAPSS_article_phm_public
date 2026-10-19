"""Unchanged numerical functions from corrected P20.1; NumPy/pandas only."""
import numpy as np
BASES = ['ISO_LOWER98_M15', 'RF_SLOPE_LOWER98_M15', 'HI_MARKER', 'ISO_POINT_M15', 'RF_SLOPE_POINT_M15']
AGE, STEP, WINDOW, GAMMA = 127, 5, 60, 1.0

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
