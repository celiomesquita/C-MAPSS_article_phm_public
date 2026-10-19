"""Independent verifier for the confirmation pipeline outputs (rehearsal or confirmation).

Scope: recomputes quantiles, decisions, summaries, extension expectations, partition isolation and the age-limit
criterion from the stored predictions, splits and lives. It does not refit the HI; model fitting is covered by the
earlier verified pilots and by the unit tests.
Usage: py verify_confirmation_19a.py <output-dir> [expected-total-engines]
"""
import gzip
import hashlib
import json
from fractions import Fraction
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import brentq
from scipy.stats import binom

ROOT = Path(__file__).resolve().parents[1]
AGE = 127
TOL = 1e-9
U_GRID = (0.0, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 1.0)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def cp_upper_bisect(x, n, confidence=.95):
    if x >= n:
        return 1.
    return float(brentq(lambda p: binom.cdf(x, n, p)-(1-confidence), 1e-12, 1-1e-12, xtol=1e-14))


def quantile_of(scores, alpha):
    a = np.sort(np.asarray(scores, float))
    k = math.ceil((len(a)+1)*(1-Fraction(alpha).limit_denominator(1000)))
    return float(a[k-1]) if 1 <= k <= len(a) else float("inf")


def late_scores(pred, method):
    out = []
    for unit, g in pred.loc[pred.method.eq(method) & pred.in_domain.astype(bool)].groupby("unit"):
        out.append(max(0., float((g.predicted_rul-g.rul).max())))
    return out


def expectation(T, has, D, d, sched, u):
    tau = AGE-d
    if has and D <= tau:
        s = min(sched, T)
        return s, float(sched > T), float(sched == T), 0.
    end = int(D) if has else int(T)-1
    util = late = exact = 0.
    survive = 1.
    for t in range(tau, end+1):
        first = survive*u
        s = AGE if t == tau else t+d
        util += first*min(s, T)
        late += first*(s > T)
        exact += first*(s == T)
        survive *= 1-u
    if has:
        util += survive*min(sched, T)
        late += survive*float(sched > T)
        exact += survive*float(sched == T)
    else:
        util += survive*T
    return util, late, exact, (0. if has else survive)


def decide(g, reserve, delay, q):
    g = g.loc[g.in_domain.astype(bool)].sort_values("cycle")
    for cycle, rul in zip(g.cycle, g.predicted_rul):
        if max(0., rul-q) <= reserve+delay+TOL:
            return int(cycle)
    return None


def main(out, expected_total=None):
    out = Path(out)
    meta = json.loads((out / "metadata.json").read_text(encoding="utf-8"))
    for name, digest in json.loads((out / "manifest.json").read_text(encoding="utf-8")).items():
        assert sha(out / name) == digest, name
    for folder, digest in meta["previous_manifests"].items():
        assert sha(ROOT / "experiments/artifacts" / folder / "manifest.json") == digest, folder
    labels = sorted(p.name[len("splits_"):-5] for p in out.glob("splits_*.json"))
    decisions = pd.read_csv(out / "decisions.csv")
    summary = pd.read_csv(out / "summary.csv")
    quantile_table = pd.read_csv(out / "quantiles.csv")
    checked = dict(quantiles=0, decisions=0, summaries=0, extension=0, partitions=0)
    lives_all = []
    for label in labels:
        splits = json.loads((out / f"splits_{label}.json").read_text(encoding="utf-8"))
        config = json.loads((out / f"config_{label}.json").read_text(encoding="utf-8"))
        group = config["group"]
        reserved = set(group["fit"]+group["calibration"]+group["selection"])
        rest = set(config["remaining"])
        assert len(reserved) == 80 and reserved.isdisjoint(rest)
        table = pd.read_csv(out / f"config_selection_{label}.csv")
        best = table.sort_values(["selection_rmse", "candidate"], kind="stable").iloc[0]
        assert bool(table.set_index("candidate").chosen.loc[best.candidate]) and table.chosen.sum() == 1
        assert (config["config"]["tau"], config["config"]["gamma"], config["config"]["ridge"]) == (best.tau, best.gamma, best.ridge)
        lives = pd.read_csv(out / f"lives_{label}.csv")
        lives_all.append(lives)
        life = lives.set_index("unit").T
        by_repeat = {}
        for s in splits:
            sets = [set(s[k]) for k in ["fit", "converter", "uncertainty", "evaluation"]]
            assert all(a.isdisjoint(b) for i, a in enumerate(sets) for b in sets[i+1:])
            assert set().union(*sets) <= rest and set().union(*sets).isdisjoint(reserved)
            by_repeat.setdefault(s["repeat"], []).extend(s["evaluation"])
            tag = f"{label}_r{s['repeat']}_f{s['fold']}"
            upred = pd.read_csv(out / f"predictions_{tag}_U.csv.gz")
            epred = pd.read_csv(out / f"predictions_{tag}_E.csv.gz")
            qs = pd.read_csv(out / f"quantiles_{tag}.csv")
            assert set(upred.unit) <= set(s["uncertainty"]) and set(epred.unit) <= set(s["evaluation"])
            assert (upred.rul == upred.groupby("unit").cycle.transform("max")-upred.cycle).all()
            # lives agree with predictions' endpoint labels
            ends = epred.groupby("unit").apply(lambda g: float((g.cycle+g.rul).iloc[0]), include_groups=False)
            assert all(abs(ends.loc[u]-lives.set_index("unit").T.loc["T", u]) < 1e-9 for u in ends.index)
            for method in ["ISO", "RF_SLOPE"]:
                sc = late_scores(upred, method)
                for alpha in (.02, .05):
                    ref = quantile_of(sc, alpha)
                    got = float(qs.loc[qs.method.eq(method) & qs.scope.eq("path") & np.isclose(qs.alpha, alpha), "q_late"].iloc[0])
                    assert (ref == got) or abs(ref-got) < 1e-9, (tag, method, alpha, ref, got)
                    checked["quantiles"] += 1
            # decisions
            specs = []
            for method in ["ISO", "RF_SLOPE"]:
                for d in (1, 2):
                    for pid, a, m in [("POINT_M15", None, 15), ("LOWER98_M15", .02, 15), ("LOWER98_M12", .02, 12), ("LOWER95_M15", .05, 15)]:
                        specs.append((f"{method}_{pid}_D{d}", method, a, m, d))
            for unit in s["evaluation"]:
                T = int(life.loc["T", unit])
                dec_u = decisions.loc[decisions.subset.eq(label) & decisions.repeat.eq(s["repeat"]) & decisions.unit.eq(unit)]
                assert len(dec_u) == 20
                for pid, method, a, m, d in specs:
                    q = 0. if a is None else float(qs.loc[qs.method.eq(method) & qs.scope.eq("path") & np.isclose(qs.alpha, a), "q_late"].iloc[0])
                    g = epred.loc[epred.unit.eq(unit) & epred.method.eq(method)]
                    expect = decide(g, m, d, q)
                    row = dec_u.loc[dec_u.policy_id.eq(pid)].iloc[0]
                    assert (expect is None and not row.has_decision) or (expect is not None and row.decision == expect and row.scheduled == expect+d), (tag, unit, pid)
                    sched = None if expect is None else expect+d
                    assert bool(row.late) == (sched is not None and sched > T) and bool(row.exact_endpoint) == (sched is not None and sched == T)
                    checked["decisions"] += 1
                for d in (1, 2):
                    g = epred.loc[epred.unit.eq(unit) & epred.method.eq("ISO") & epred.cycle.ge(39) & epred.in_domain.astype(bool)]
                    row = dec_u.loc[dec_u.policy_id.eq(f"HI_MARKER_D{d}")].iloc[0]
                    if g.empty:
                        assert not row.has_decision and np.isnan(row.decision)
                    else:
                        marker = int(g.cycle.min())
                        assert row.decision == marker and row.scheduled == marker+d
                    row = dec_u.loc[dec_u.policy_id.eq(f"AGE127_D{d}")].iloc[0]
                    assert row.decision == AGE-d and row.scheduled == AGE and bool(row.late) == (T < AGE) and bool(row.exact_endpoint) == (T == AGE)
                    checked["decisions"] += 2
            checked["partitions"] += 1
        evaluated = {r: sorted(v) for r, v in by_repeat.items()}
        assert all(v == sorted(rest) for v in evaluated.values())
    # summaries
    for (subset_, repeat, policy), g in decisions.groupby(["subset", "repeat", "policy_id"]):
        row = summary.loc[summary.subset.eq(subset_) & summary.repeat.eq(repeat) & summary.policy_id.eq(policy)].iloc[0]
        n = len(g)
        assert row.total == n and row.decisions == int(g.has_decision.sum()) and row.late_count == int(g.late.sum())
        assert row.exact_count == int(g.exact_endpoint.sum()) and row.reached_count == int(g.reached_endpoint.sum())
        assert abs(row.restorations_per_10000_cycles-10000*n/g.utilised.sum()) < 1e-9
        assert abs(row.late_upper95-cp_upper_bisect(int(g.late.sum()), n)) < 1e-7
        assert abs(row.reached_upper95-cp_upper_bisect(int(g.reached_endpoint.sum()), n)) < 1e-7
        checked["summaries"] += 1
    # extension expectations
    ex = pd.read_csv(out / "extension.csv")
    base_ids = ["ISO_LOWER98_M15", "RF_SLOPE_LOWER98_M15", "ISO_POINT_M15", "RF_SLOPE_POINT_M15", "HI_MARKER"]
    assert len(ex) == len(decisions.groupby(["subset", "repeat", "unit"]))*len(base_ids)*2*len(U_GRID)
    index = decisions.set_index(["subset", "repeat", "unit", "policy_id"])
    for r in ex.itertuples(index=False):
        row = index.loc[(r.subset, r.repeat, r.unit, f"{r.base}_D{r.delay}")]
        has = bool(row.has_decision)
        util, late, exact, missing = expectation(float(row.endpoint), has, float(row.decision) if has else np.nan, r.delay,
                                                 float(row.scheduled) if has else np.nan, r.u)
        assert abs(util-r.util) < 1e-9 and abs(late-r.late) < 1e-9 and abs(exact-r.exact) < 1e-9 and abs(missing-r.missing) < 1e-9
        checked["extension"] += 1
    # age-limit criterion
    all_lives = pd.concat(lives_all)
    if expected_total is not None:
        assert len(all_lives) == int(expected_total), (len(all_lives), expected_total)
    age = json.loads((out / "age_limit.json").read_text(encoding="utf-8"))
    hits = int((all_lives["T"] <= AGE).sum())
    upper = cp_upper_bisect(hits, len(all_lives))
    assert age["pooled"]["hits"] == hits and age["pooled"]["engines"] == len(all_lives)
    assert abs(age["pooled"]["upper95"]-upper) < 1e-7 and age["pooled"]["passes"] == (upper <= .02)
    print(json.dumps(dict(verified=True, **checked, age_hits=hits, age_upper95=upper, engines=len(all_lives)), indent=2))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
