"""Independent verifier for P16.1: loop enumeration of monitoring-validity outcomes, summaries, HI@127 and rank correlation."""
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_extension_16a"
SRC = ART / "pilot_policy_selection_13a/decisions.csv"
P10 = ART / "pilot_f_uncertainty_10"
A = 127


def outcome(T, has, D, d, S, u):
    tau = A - d
    if has and D <= tau:
        return (min(S, T), float(S > T), float(S == T), 0.0, 0.0)
    end = int(D) if has else int(T) - 1
    util = late = exact = 0.0
    alive = 1.0
    age_p = 0.0
    for t in range(tau, end + 1):
        pf = alive * u
        sched = A if t == tau else t + d
        util += pf * min(sched, T)
        late += pf * (sched > T)
        exact += pf * (sched == T)
        if t == tau:
            age_p = pf
        alive *= (1 - u)
    if has:
        util += alive * min(S, T)
        late += alive * (S > T)
        exact += alive * (S == T)
        missing = 0.0
    else:
        util += alive * T
        missing = alive
    return (util, late, exact, missing, age_p)


def ranks(v):
    order = np.argsort(v, kind="mergesort")
    r = np.empty(len(v))
    sv = np.asarray(v)[order]
    i = 0
    while i < len(v):
        j = i
        while j + 1 < len(v) and sv[j + 1] == sv[i]:
            j += 1
        r[order[i:j + 1]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(x, y):
    a, b = ranks(np.asarray(x, float)), ranks(np.asarray(y, float))
    a, b = a - a.mean(), b - b.mean()
    return float((a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum()))


def main():
    d = pd.read_csv(SRC)
    d = d[d.dataset == "complete"]
    ex = pd.read_csv(OUT / "engine_expectations.csv.gz")
    raw = {(r.subset, r.repeat, r.fold, r.unit, r.policy_id): r for r in d.itertuples(index=False)}
    checked = 0
    for r in ex.itertuples(index=False):
        o = raw[(r.subset, r.repeat, r.fold, r.unit, f"{r.base}_D{r.delay}")]
        has = bool(o.has_decision) and np.isfinite(o.decision)
        res = outcome(float(o.endpoint), has, float(o.decision) if has else np.nan, int(o.delay), float(o.scheduled) if has else np.nan, r.u)
        got = (r.util, r.late, r.exact, r.missing, r.age_acts)
        assert all(abs(a - b) < 1e-9 for a, b in zip(res, got)), (r.subset, r.repeat, r.unit, r.base, r.delay, r.u, res, got)
        checked += 1
    s = pd.read_csv(OUT / "summary.csv")
    for row in s.itertuples(index=False):
        g = ex[(ex["subset"] == row.subset) & (ex.repeat == row.repeat) & (ex.base == row.base) & (ex.delay == row.delay) & (ex.u == row.u)]
        n = len(g)
        assert abs(row.rate - n / g.util.sum()) < 1e-12 and abs(row.saving_vs_127 - (1 - A * n / g.util.sum())) < 1e-12
        assert abs(row.late_per100 - 100 * g.late.mean()) < 1e-9
    # u=0 equals original, u=1 equals min(original, 127)
    for r in ex[ex.u == 0.0].itertuples(index=False):
        o = raw[(r.subset, r.repeat, r.fold, r.unit, f"{r.base}_D{r.delay}")]
        assert abs(r.util - o.utilised) < 1e-9
    for r in ex[ex.u == 1.0].itertuples(index=False):
        o = raw[(r.subset, r.repeat, r.fold, r.unit, f"{r.base}_D{r.delay}")]
        assert abs(r.util - min(o.utilised, A)) < 1e-9 or (not (bool(o.has_decision)) and abs(r.util - A) < 1e-9), (r,)
    # HI at 127 and Spearman for a sample of condition rows
    hi = pd.read_csv(OUT / "hi_at_127.csv")
    for (subset, repeat, fold), g in list(d.groupby(["subset", "repeat", "fold"]))[:6]:
        p = pd.read_csv(P10 / f"predictions_{subset}_r{repeat}_f{fold}_complete.csv.gz")
        p = p[(p.method == "ISO") & (p.cycle == A)].set_index("unit").hi
        mine = hi[(hi["subset"] == subset) & (hi.repeat == repeat) & (hi.fold == fold)].set_index("unit").hi127
        assert (abs(p.sort_index() - mine.sort_index()) < 1e-12).all()
    cond = pd.read_csv(OUT / "condition_dependence.csv")
    row = cond[(cond["subset"] == "FD001") & (cond.repeat == 1) & (cond.base == "ISO_LOWER98_M15") & (cond.delay == 1)].iloc[0]
    g = d[(d.subset == "FD001") & (d.repeat == 1) & (d.policy_id == "ISO_LOWER98_M15_D1")].merge(hi, on=["subset", "repeat", "fold", "unit"])
    ext = np.where(g.has_decision, g.scheduled, g.endpoint) - A
    assert abs(spearman(g.hi127, ext) - row.spearman_ext_hi127) < 1e-9
    for folder in sorted(ART.glob("pilot_*")):
        mf = folder / "manifest.json"
        if folder == OUT or not mf.exists():
            continue
        for n_, h in json.loads(mf.read_text(encoding="utf-8")).items():
            assert hashlib.sha256((folder / n_).read_bytes()).hexdigest() == h, (folder.name, n_)
    result = dict(status="passed", engine_u_rows_rebuilt=checked, summary_rows=len(s), hi_partitions_checked=6)
    (OUT / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
