"""P20.2: one cycle per flight; renewal of archived engine decisions only."""
import argparse
import ast
import hashlib
import json
import platform
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import renewal_core_20b as core

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "experiments/literal_cycles_2026-10-19"
SUBSETS = ("FD001", "FD002", "FD003", "FD004")
R, H, COST = 2000, 32000., 6_000_000.
SEED = 20261019
INPUTS = ("pilot_policy_selection_13a", "confirmation_19a")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def manifest():
    files = {str(p.relative_to(OUT)).replace("\\", "/"): sha(p)
             for p in sorted(OUT.rglob("*")) if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(files, indent=2), encoding="utf-8")


def load_inputs():
    columns = ["subset", "repeat", "unit", "policy_id", "delay", "has_decision", "decision", "endpoint"]
    frames, provenance = [], {}
    for folder in INPUTS:
        src = ROOT / "experiments/artifacts" / folder / "decisions.csv"
        dst = OUT / "evidence_inputs" / f"{folder}.csv"
        if src.exists():
            f = pd.read_csv(src)
            f = f.loc[f.dataset.eq("complete") & f.policy_id.isin(
                [f"{b}_D{d}" for b in core.BASES for d in (1, 2)]), columns]
            dst.parent.mkdir(parents=True, exist_ok=True)
            f.to_csv(dst, index=False)
            provenance[folder] = dict(original_sha256=sha(src), selected_sha256=sha(dst), rows=len(f))
        else:
            bundled = Path(__file__).parent / "evidence_inputs" / f"{folder}.csv"
            if not bundled.exists():
                bundled = ROOT / "experiments/literal_cycles_2026-10-19/evidence_inputs" / f"{folder}.csv"
            f = pd.read_csv(bundled)
            dst.parent.mkdir(parents=True, exist_ok=True)
            if bundled.resolve() != dst.resolve():
                shutil.copyfile(bundled, dst)
            provenance[folder] = dict(selected_sha256=sha(dst), rows=len(f))
        frames.append(f)
    return pd.concat(frames, ignore_index=True), provenance


def draws(arms, subset_index, repeat, tag=0, r=R):
    nmax = int(np.ceil(H / min(a["util"].min() for a in arms.values()))) + 8
    rng = np.random.default_rng([SEED, subset_index, repeat, tag])
    engines = rng.integers(0, next(iter(arms.values()))["n"], (r, nmax))
    return engines, rng.random((r, nmax)), rng.random((3, r))


def simulate(arms, eng, v, init, llp):
    result = {}
    for name in sorted(arms):
        a = arms[name]
        ix = core.sample_atoms(a, core.cumulative_table(a), eng, v)
        result[name] = np.column_stack(core.simulate_draws(
            a["util"][ix], a["event"][ix], a["util"], a["prob"] / a["n"],
            a["event"], 1., 1., llp, H, 1, init))
    return result


def main():
    global OUT
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()
    OUT = args.output.resolve()
    assert not (OUT / "metadata.json").exists(), "preserve completed runs; choose another output directory"
    OUT.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    frames, provenance = load_inputs()
    inputs_before = {k: sha(ROOT / "experiments/artifacts" / k / "decisions.csv")
                     for k in INPUTS if (ROOT / "experiments/artifacts" / k / "decisions.csv").exists()}
    rows, pairs, stationary, replicates = [], [], [], []
    validation = {"max_llp_disagreement": 0., "max_probability_error": 0.}
    for di, subset in enumerate(SUBSETS):
        for repeat in (1, 2, 3):
            f = frames.loc[frames.subset.eq(subset) & frames.repeat.eq(repeat)]
            arms = core.arms_for({d: f.loc[f.delay.eq(d)] for d in (1, 2)})
            eng, v, init = draws(arms, di, repeat)
            results = simulate(arms, eng, v, init, 20000.)
            no_llp = simulate(arms, eng, v, init, None)
            llp_counts = np.stack([a[:, 1] for a in results.values()])
            validation["max_llp_disagreement"] = max(validation["max_llp_disagreement"], float(np.ptp(llp_counts, axis=0).max()))
            for name, a in arms.items():
                err = np.abs(np.bincount(a["engine"], weights=a["prob"], minlength=a["n"]) - 1).max()
                validation["max_probability_error"] = max(validation["max_probability_error"], float(err))
                got = results[name]
                tot = got[:, 0] + got[:, 1]
                events = got[:, 2:].sum(axis=1)
                se = tot.std(ddof=1) / np.sqrt(R)
                rows.append(dict(subset=subset, repeat=repeat, arm=name, n_engines=a["n"],
                                 degradation_visits=got[:, 0].mean(), llp_visits=got[:, 1].mean(),
                                 visits=tot.mean(), visits_mc_se=se, missing=got[:, 2].mean(),
                                 exact=got[:, 3].mean(), late=got[:, 4].mean(), events=events.mean(),
                                 events_mc_se=events.std(ddof=1)/np.sqrt(R),
                                 cost_usd=COST*tot.mean(), cost_usd_mc_se=COST*se,
                                 cost_usd_per_flight=COST*tot.mean()/H))
                x = no_llp[name][:, 0]
                expected = H*core.analytic_rate(a)
                z = (x.mean()-expected)/(x.std(ddof=1)/np.sqrt(R))
                stationary.append(dict(subset=subset, repeat=repeat, arm=name, mean=x.mean(), expected=expected, z=z))
                replicates.extend(dict(subset=subset, repeat=repeat, arm=name, replicate=j,
                                       degradation=int(row[0]), llp=int(row[1]), missing=int(row[2]), exact=int(row[3]), late=int(row[4]))
                                  for j, row in enumerate(got[:12]))
            for d in (1, 2):
                age = f"AGE127_D{d}"
                for name in results:
                    if not name.endswith(f"_D{d}") or name == age:
                        continue
                    refs = [age] + ([name.replace("HYB_", "PHM_", 1)] if name.startswith("HYB_") else [])
                    for ref in refs:
                        x = results[name][:, :2].sum(axis=1)-results[ref][:, :2].sum(axis=1)
                        pairs.append(dict(subset=subset, repeat=repeat, arm=name, reference=ref,
                                          delta_visits=x.mean(), delta_visits_mc_se=x.std(ddof=1)/np.sqrt(R),
                                          relative_saving=1-results[name][:, :2].sum()/results[ref][:, :2].sum()))
            print(subset, repeat, "complete", flush=True)
    cells = pd.DataFrame(rows)
    cells.to_csv(OUT / "cells.csv", index=False)
    pd.DataFrame(pairs).to_csv(OUT / "contrasts.csv", index=False)
    pd.DataFrame(stationary).to_csv(OUT / "validation_stationary.csv", index=False)
    pd.DataFrame(replicates).to_csv(OUT / "verification_replicates.csv", index=False)
    mean_columns = ["degradation_visits", "llp_visits", "visits", "events", "missing", "exact", "late", "cost_usd", "cost_usd_per_flight"]
    summary = cells.groupby(["subset", "arm"], as_index=False)[mean_columns].mean()
    for column in ("visits", "events", "cost_usd"):
        mc = cells.groupby(["subset", "arm"])[f"{column}_mc_se"].agg(lambda x: np.sqrt(np.square(x).sum())/len(x))
        summary[f"{column}_mc_se"] = [mc.loc[(r.subset, r.arm)] for r in summary.itertuples()]
    summary["two_positions_cost_usd"] = 2*summary.cost_usd
    summary.to_csv(OUT / "summary.csv", index=False)
    validation["stationary_max_abs_z"] = float(pd.DataFrame(stationary).z.abs().max())
    validation["passed"] = validation["stationary_max_abs_z"] < 4.5 and validation["max_llp_disagreement"] == 0 and validation["max_probability_error"] < 1e-12
    for k, digest in inputs_before.items():
        assert sha(ROOT / "experiments/artifacts" / k / "decisions.csv") == digest
    for name in ("twenty_year_20b_literal.py", "renewal_core_20b.py", "verify_twenty_year_20b_literal.py", "protocolo_vinte_anos_20b_literal.md"):
        shutil.copyfile(ROOT / "experiments" / name, OUT / name)
    original = ROOT / "experiments/twenty_year_20a.py"
    if original.exists():
        shutil.copyfile(original, OUT / "reference_twenty_year_20a.py")
        old_ast = ast.parse(original.read_text(encoding="utf-8"))
        new_ast = ast.parse((ROOT/"experiments/renewal_core_20b.py").read_text(encoding="utf-8"))
        old = {x.name: ast.dump(x) for x in old_ast.body if isinstance(x, ast.FunctionDef)}
        assert all(ast.dump(x) == old[x.name] for x in new_ast.body if isinstance(x, ast.FunctionDef))
    metadata = dict(finished_utc=datetime.now(timezone.utc).isoformat(), seconds=time.perf_counter()-start,
                    seed=SEED, replicates=R, xi=1., horizon_flights=H, llp=20000., rho=1., ic="mature",
                    sources=provenance, validation=validation, python=platform.python_version(),
                    numpy=np.__version__, pandas=pd.__version__, cells=len(cells),
                    interpretation="Monte Carlo errors conditional on archived empirical engine pools; not population risk")
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    manifest()
    print(json.dumps(validation, indent=2))
    assert validation["passed"], "validation failed; preserve this run and investigate"


if __name__ == "__main__":
    main()
