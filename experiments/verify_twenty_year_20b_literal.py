"""Independent scalar P20.1 implementation, reused to verify literal-cycle P20.2."""
import argparse
import ast
import json
import math
from pathlib import Path
import numpy as np
import pandas as pd
import renewal_core_20b as core
import twenty_year_20b_literal as run
AGE, STEP, W = 127, 5, 60
R=12
BASES = ['ISO_LOWER98_M15', 'RF_SLOPE_LOWER98_M15', 'HI_MARKER', 'ISO_POINT_M15', 'RF_SLOPE_POINT_M15']

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
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=run.OUT)
    args = parser.parse_args()
    out = args.output.resolve()
    for relative, digest in json.loads((out/"manifest.json").read_text()).items():
        assert run.sha(out/relative) == digest, relative
    frames = pd.concat([pd.read_csv(out/"evidence_inputs"/f"{name}.csv") for name in run.INPUTS], ignore_index=True)
    stored = pd.read_csv(out/"verification_replicates.csv")
    checked, atom_count = 0, 0
    for di, subset in enumerate(run.SUBSETS):
        for repeat in (1, 2, 3):
            f = frames.loc[frames.subset.eq(subset) & frames.repeat.eq(repeat)]
            scalar = arm_outcomes(f)
            arms = core.arms_for({d: f.loc[f.delay.eq(d)] for d in (1, 2)})
            # Recreate full production streams before taking the first 12 replicas.
            nmax = int(np.ceil(32000/min(a["util"].min() for a in arms.values())))+8
            rng = np.random.default_rng([20261019, di, repeat, 0])
            eng = rng.integers(0, next(iter(arms.values()))["n"], (2000, nmax))
            v = rng.random((2000, nmax))
            init = rng.random((3, 2000))
            for name, expected in scalar.items():
                a = arms[name]
                for i, o in enumerate(expected):
                    sel = a["engine"] == i
                    np.testing.assert_allclose(a["prob"][sel], [p for p, u, e in o], atol=1e-13)
                    np.testing.assert_array_equal(a["util"][sel], [u for p, u, e in o])
                    np.testing.assert_array_equal(a["event"][sel], [e for p, u, e in o])
                    atom_count += len(o)
                got = renewal(expected, eng[:12], v[:12], init[:, :12], 1., 1., 20000., 32000., 1)
                reference = stored.loc[stored.subset.eq(subset) & stored.repeat.eq(repeat) & stored.arm.eq(name)].sort_values("replicate")
                np.testing.assert_array_equal(got, reference[["degradation", "llp", "missing", "exact", "late"]].to_numpy())
                checked += 1
            print(subset, repeat, "scalar verification passed", flush=True)
    rng = np.random.default_rng(127)
    init = rng.random((3, 64))
    life = np.full((64, 260), 127.)
    event = np.zeros_like(life, int)
    for ic in (0, 1):
        got = core.simulate_draws(life, event, np.array([127.]), np.array([1.]), np.array([0]), 1., 1., None, 32000., ic, init)
        expected = np.full(64, 32000//127) if ic == 0 else np.floor((32000-127*(1-init[1]))/127).astype(int)+1
        np.testing.assert_array_equal(got[0], expected)
        assert all(not arr.any() for arr in got[1:])
    copied = ast.parse((out/"renewal_core_20b.py").read_text())
    reference_path = out/"reference_twenty_year_20a.py"
    if not reference_path.exists():
        reference_path = run.ROOT/"experiments/literal_cycles_2026-10-19/reference_twenty_year_20a.py"
    reference = ast.parse(reference_path.read_text())
    defs = {x.name: ast.dump(x) for x in reference.body if isinstance(x, ast.FunctionDef)}
    assert all(ast.dump(x) == defs[x.name] for x in copied.body if isinstance(x, ast.FunctionDef))
    assert json.loads((out/"metadata.json").read_text())["validation"]["passed"]
    report = dict(passed=True, arms_checked=checked, scalar_replicates_per_arm=12,
                  outcome_atoms_checked=atom_count, deterministic_age_new_and_mature=True,
                  unchanged_numerical_functions=8)
    (out/"verification.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    run.OUT = out
    run.manifest()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
