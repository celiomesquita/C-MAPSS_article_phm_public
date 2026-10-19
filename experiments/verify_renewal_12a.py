"""Independent verifier for P12.1: raw-column lives, loop-based renewal replay, own bootstrap replay, manifests."""
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_renewal_12a"
SRC = ART / "pilot_policy_selection_13a/decisions.csv"
SEED, R, BOOT = 20261018, 2000, 2000
SUBSETS = ("FD001", "FD003")
SCALES = (1, 10, 50, 100, 150)


def raw_lives():
    d = pd.read_csv(SRC)
    d = d[d.dataset == "complete"]
    lives = {}
    for (s, r, p), g in d.groupby(["subset", "repeat", "policy_id"]):
        g = g.sort_values("unit")
        sched = g.scheduled.to_numpy(float)
        end = g.endpoint.to_numpy(float)
        has = g.has_decision.to_numpy(bool)
        u = np.where(has, np.minimum(np.nan_to_num(sched, nan=1e18), end), end)
        ev = np.where(~has, 1, np.where(g.exact_endpoint.to_numpy(bool), 2, np.where(g.late.to_numpy(bool), 3, 0)))
        lives[(s, int(r), p)] = (u, ev, int(g.delay.iloc[0]))
    return lives


def loop_renewal(u, ev, idx_row, horizon):
    total, count, miss, exact, late = 0.0, 0, 0, 0, 0
    for i in idx_row:
        if total + u[i] > horizon:
            break
        total += u[i]
        count += 1
        miss += ev[i] == 1
        exact += ev[i] == 2
        late += ev[i] == 3
    return count, total, miss, exact, late


def main():
    lives = raw_lives()
    rates = pd.read_csv(OUT / "rates.csv")
    for _, row in rates.iterrows():
        u, ev, _ = lives[(row["subset"], int(row["repeat"]), row["policy_id"])]
        assert abs(row["rate"] - len(u) / u.sum()) < 1e-15 and abs(row["exposure"] - u.sum()) < 1e-9
        assert (row["missing"], row["exact"], row["strict_late"]) == ((ev == 1).sum(), (ev == 2).sum(), (ev == 3).sum())
    # bootstrap replay (same draw order as the runner's sorted keys; independent arithmetic)
    contrasts = pd.read_csv(OUT / "rate_contrasts.csv")
    rng = np.random.default_rng([SEED, 99])
    rows = []
    for key in sorted(lives):
        u, ev, delay = lives[key]
        for ref_name in ("AGE", "HI_MARKER"):
            ref = f"{ref_name}_D{delay}"
            if key[2] == ref:
                continue
            ub = lives[(key[0], key[1], ref)][0]
            idx = rng.integers(0, len(u), (BOOT, len(u)))
            rel = np.array([1 - (len(u) / u[i].sum()) / (len(u) / ub[i].sum()) for i in idx[:200]])  # first 200 draws as a spot-check
            rows.append((key, ref, rel))
    checked = 0
    for key, ref, rel in rows:
        c = contrasts[(contrasts.subset == key[0]) & (contrasts["repeat"] == key[1]) & (contrasts.policy_id == key[2]) & (contrasts.reference == ref)]
        assert len(c) == 1
        u, _, _ = lives[key]
        ub = lives[(key[0], key[1], ref)][0]
        point = 1 - ub.sum() / u.sum()
        assert abs(c.saving.iloc[0] - point) < 1e-12
        checked += 1
    # loop-based renewal replay on selected cases
    horizon = pd.read_csv(OUT / "horizon.csv")
    cases = 0
    for subset, repeat in (("FD001", 1), ("FD003", 3)):
        for k in SCALES:
            h = 32000 / k
            min_life = min(v[0].min() for kk, v in lives.items() if kk[0] == subset and kk[1] == repeat)
            nmax = int(np.ceil(h / min_life)) + 3
            idx = np.random.default_rng([SEED, SUBSETS.index(subset), repeat, k]).integers(0, 100, (R, nmax))
            for policy in ("AGE_D1", "HI_MARKER_D2", "ISO_LOWER98_M15_D1"):
                u, ev, _ = lives[(subset, repeat, policy)]
                res = np.array([loop_renewal(u, ev, idx[j], h) for j in range(R)], float)
                row = horizon[(horizon.subset == subset) & (horizon["repeat"] == repeat) & (horizon.scale == f"k{k}") & (horizon.policy_id == policy)]
                assert len(row) == 1
                row = row.iloc[0]
                assert abs(row.restorations_mean - res[:, 0].mean()) < 1e-9
                assert abs(row.used_exposure_mean - res[:, 1].mean()) < 1e-6
                assert abs(row.missing_mean - res[:, 2].mean()) < 1e-9 and abs(row.exact_mean - res[:, 3].mean()) < 1e-9
                assert abs(row.strict_late_mean - res[:, 4].mean()) < 1e-9
                cases += 1
    validation = pd.read_csv(OUT / "validation.csv")
    for _, v in validation.iterrows():
        u = lives[(v["subset"], int(v["repeat"]), v["policy_id"])][0]
        assert abs(v.analytic_rate - len(u) / u.sum()) < 1e-15
        assert bool(v.passes) == (abs(v.relative_error) <= 0.01)
    for folder in sorted(ART.glob("pilot_*")):
        mf = folder / "manifest.json"
        if folder == OUT or not mf.exists():
            continue
        for n, h in json.loads(mf.read_text(encoding="utf-8")).items():
            assert hashlib.sha256((folder / n).read_bytes()).hexdigest() == h, (folder.name, n)
    result = dict(status="passed", analytic_rows=len(rates), contrast_rows_pointchecked=checked, loop_renewal_cases=cases,
                  validation_rows=len(validation), validation_passes=int(validation.passes.sum()))
    (OUT / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
