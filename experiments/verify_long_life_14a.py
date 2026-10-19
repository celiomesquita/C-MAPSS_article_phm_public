"""Independent verifier for P14.1: lifetimes from archived endpoints, ranges from per-repeat decisions, own rank correlation."""
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_long_life_14a"
SUBSETS = ("FD001", "FD003")
QUANTITIES = ("usable_marker", "ISO_LOWER98_M15_D1", "ISO_LOWER98_M15_D2", "HI_MARKER_D1", "HI_MARKER_D2")
SEED, NB = 20261018, 2000


def ranks(v):
    order = np.argsort(v, kind="mergesort")
    r = np.empty(len(v))
    sv = v[order]
    i = 0
    while i < len(v):
        j = i
        while j + 1 < len(v) and sv[j + 1] == sv[i]:
            j += 1
        r[order[i:j + 1]] = (i + j) / 2 + 1
        i = j + 1
    return r


def rank_corr(x, y):
    a, b = ranks(np.asarray(x, float)), ranks(np.asarray(y, float))
    a, b = a - a.mean(), b - b.mean()
    den = np.sqrt((a * a).sum() * (b * b).sum())
    return np.nan if den == 0 else float((a * b).sum() / den)


def boot(x, y, rng):
    x, y = np.asarray(x, float), np.asarray(y, float)
    vals = []
    for _ in range(NB):
        i = rng.integers(0, len(x), len(x))
        vals.append(rank_corr(x[i], y[i]))
    lo, hi = np.nanpercentile(np.array(vals, float), [2.5, 97.5])
    return rank_corr(x, y), lo, hi


def main():
    d = pd.read_csv(ART / "pilot_hi_chain_13e/decisions.csv")
    m = d[d.chain == "M18"]
    T = m.groupby(["subset", "unit"]).endpoint.agg(["min", "max"])
    assert (T["min"] == T["max"]).all()
    T = T["min"]
    per_rep = {"usable_marker": m[m.policy_id == "HI_MARKER_D1"].pivot_table(index=["subset", "unit"], columns="repeat", values="usable_marker")}
    for q in QUANTITIES[1:]:
        per_rep[q] = m[m.policy_id == q].pivot_table(index=["subset", "unit"], columns="repeat", values="decision", dropna=False)
    first_marker = per_rep["usable_marker"].min(axis=1)
    main_summary = pd.read_csv(OUT / "summary.csv")
    main_engines = pd.read_csv(OUT / "engines.csv")
    rng = np.random.default_rng(SEED)
    checks = 0
    for s in SUBSETS:
        Ts = T.loc[s]
        for q in QUANTITIES:
            w = per_rep[q].loc[s]
            rng_ = (w.max(axis=1) - w.min(axis=1)).where(w.notna().all(axis=1))
            e = main_engines[(main_engines.subset == s) & (main_engines.quantity == q)].set_index("unit")
            np.testing.assert_allclose(e["range"].sort_index().to_numpy(), rng_.sort_index().to_numpy(), atol=1e-9)
            np.testing.assert_array_equal(e["T"].sort_index().to_numpy(), Ts.loc[e.index].sort_index().to_numpy())
            units = e.index  # runner's engine order (ranges.csv), needed to replay the same RNG draws
            x, y = Ts.loc[units].to_numpy(float), rng_.loc[units].to_numpy(float)
            fin = np.isfinite(y)
            x, y = x[fin], y[fin]
            mk = first_marker.loc[s].loc[units].to_numpy(float)[fin]
            got = [boot(x, y, rng), boot(x, y / x, rng), boot(mk, y, rng)]
            row = main_summary[(main_summary.subset == s) & (main_summary.quantity == q)].iloc[0]
            for (r, lo, hi), pre in zip(got, ["rho", "rel_rho", "marker_rho"]):
                np.testing.assert_allclose([r, lo, hi], [row[pre], row[pre + "_lo"], row[pre + "_hi"]], atol=1e-12)
            cut = np.quantile(x, 0.9)
            tail, wide = x >= cut, y > 10
            exc = np.clip(y - 10, 0, None)
            assert row.tail_engines == tail.sum() and row.wide_engines == wide.sum() and row.wide_in_tail == (tail & wide).sum()
            if wide.sum():
                np.testing.assert_allclose(row.enrichment, ((tail & wide).sum() / wide.sum()) / tail.mean(), atol=1e-12)
            if exc.sum():
                np.testing.assert_allclose(row.excess_tail_fraction, exc[tail].sum() / exc.sum(), atol=1e-12)
            checks += 1
    # events: count via status strings rather than boolean columns
    ev_main = pd.read_csv(OUT / "events_by_unit.csv")
    recount = []
    for name, path, chain in [("P11", "pilot_removal_11", None), ("P13.1", "pilot_policy_selection_13a", None), ("P13.5", "pilot_hi_chain_13e", "chain")]:
        x = pd.read_csv(ART / path / "decisions.csv")
        if "dataset" in x:
            x = x[x.dataset == "complete"]
        x = x[x.status != "preventive_schedule"]
        keys = ["subset", "unit"] + ([chain] if chain else [])
        c = x.groupby(keys).size().rename("events").reset_index()
        c["source"] = name
        c["chain"] = c[chain] if chain else "-"
        recount.append(c[["source", "chain", "subset", "unit", "events"]])
    recount = pd.concat(recount).sort_values(["source", "chain", "subset", "unit"]).reset_index(drop=True)
    mine = ev_main[["source", "chain", "subset", "unit", "events"]].sort_values(["source", "chain", "subset", "unit"]).reset_index(drop=True)
    pd.testing.assert_frame_equal(recount, mine, check_dtype=False)
    # previous manifests intact
    import hashlib
    for folder in sorted(ART.glob("pilot_*")):
        mf = folder / "manifest.json"
        if folder == OUT or not mf.exists():
            continue
        for n, h in json.loads(mf.read_text(encoding="utf-8")).items():
            assert hashlib.sha256((folder / n).read_bytes()).hexdigest() == h, (folder.name, n)
    result = dict(status="passed", summary_rows_checked=checks, event_rows_checked=len(recount),
                  lifetime_source="archived endpoint column of P13.5 decisions", rank_implementation="own average-rank Pearson")
    (OUT / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
