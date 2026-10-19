"""P14.1: concentration of M18 instability and adverse events by engine life (archived artefacts only)."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_long_life_14a"
P11 = ART / "pilot_removal_11"
P13A = ART / "pilot_policy_selection_13a"
P13E = ART / "pilot_hi_chain_13e"
SUBSETS = ("FD001", "FD003")
QUANTITIES = ("usable_marker", "ISO_LOWER98_M15_D1", "ISO_LOWER98_M15_D2", "HI_MARKER_D1", "HI_MARKER_D2")
PRIMARY = "usable_marker"
BOOT_SEED, N_BOOT, TAIL_Q, WIDE = 20261018, 2000, 0.90, 10.0
SOURCES = ["protocolo_vida_longa_14a.md", "pilot_long_life_14a.py", "test_long_life_14a.py", "verify_long_life_14a.py"]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def integrity():
    records = {}
    for folder in sorted(ART.glob("pilot_*")):
        manifest = folder / "manifest.json"
        if folder == OUT or not manifest.exists():
            continue
        for name, digest in json.loads(manifest.read_text(encoding="utf-8")).items():
            assert sha(folder / name) == digest, (folder.name, name)
        records[folder.name] = sha(manifest)
    return records


def input_files():
    files = [ROOT / f"CMAPSSData/train_{s}.txt" for s in SUBSETS]
    files += [P13E / "ranges.csv", P11 / "decisions.csv", P13A / "decisions.csv", P13E / "decisions.csv"]
    assert all(p.name.startswith("train_FD00") is False or p.stem in {f"train_{s}" for s in SUBSETS} for p in files)
    assert not any(p.name.startswith(("test_FD", "RUL_FD")) or "FD002" in p.name or "FD004" in p.name for p in files)
    return files


def lifetimes(subset):
    raw = pd.read_csv(ROOT / f"CMAPSSData/train_{subset}.txt", sep=r"\s+", header=None, usecols=[0, 1], names=["unit", "cycle"])
    return raw.groupby("unit").cycle.max().rename("T")


def boot_spearman(x, y, rng):
    x, y = np.asarray(x, float), np.asarray(y, float)
    rho = spearmanr(x, y).statistic
    n = len(x)
    draws = np.empty(N_BOOT)
    for b in range(N_BOOT):
        idx = rng.integers(0, n, n)
        draws[b] = spearmanr(x[idx], y[idx]).statistic
    lo, hi = np.nanpercentile(draws, [2.5, 97.5])
    return rho, lo, hi


def tail_metrics(T, width, tail_q=TAIL_Q, wide=WIDE):
    """Enrichment of the long-life tail among wide-range engines; NaN ranges are excluded beforehand."""
    T, width = np.asarray(T, float), np.asarray(width, float)
    tail = T >= np.quantile(T, tail_q)
    wide_mask = width > wide
    excess = np.clip(width - wide, 0, None)
    n_wide, n_wide_tail = int(wide_mask.sum()), int((wide_mask & tail).sum())
    frac = n_wide_tail / n_wide if n_wide else np.nan
    return dict(tail_cut=float(np.quantile(T, tail_q)), tail_engines=int(tail.sum()), tail_share=float(tail.mean()),
                wide_engines=n_wide, wide_in_tail=n_wide_tail, wide_tail_fraction=frac,
                enrichment=frac / tail.mean() if n_wide else np.nan,
                excess_total=float(excess.sum()),
                excess_tail_fraction=float(excess[tail].sum() / excess.sum()) if excess.sum() > 0 else np.nan)


def is_event(d):
    return (~d.has_decision.astype(bool)) | d.late.astype(bool) | d.exact_endpoint.astype(bool) | d.reached_endpoint.astype(bool)


def classify(summary):
    rows = summary[summary.quantity == PRIMARY].set_index("subset")
    ok = {s: (rows.loc[s, "rho_lo"] > 0, rows.loc[s, "enrichment"] >= 2) for s in SUBSETS}
    full = [s for s in SUBSETS if all(ok[s])]
    any_req = [s for s in SUBSETS if any(ok[s])]
    if len(full) == len(SUBSETS):
        label = "sustentada"
    elif full or any_req:
        label = "parcial"
    else:
        label = "nao_sustentada"
    return label, {s: dict(spearman_lo_positive=bool(a), enrichment_ge_2=bool(b)) for s, (a, b) in ok.items()}


def event_tables(T_by_subset):
    sources = [("P11", P11 / "decisions.csv", None), ("P13.1", P13A / "decisions.csv", None),
               ("P13.5", P13E / "decisions.csv", "chain")]
    rows = []
    for name, path, chain_col in sources:
        d = pd.read_csv(path)
        if "dataset" in d:
            d = d[d.dataset == "complete"]
        d = d.assign(event=is_event(d))
        groups = d.groupby(chain_col) if chain_col else [("-", d)]
        for chain, part in groups:
            for subset in SUBSETS:
                p = part[part.subset == subset]
                ev = p[p.event].groupby("unit").size().rename("events")
                rows.append(pd.DataFrame({"source": name, "chain": chain, "subset": subset, "unit": ev.index,
                                          "events": ev.values, "rows_total": len(p)}))
    per_unit = pd.concat(rows, ignore_index=True)
    out = []
    for subset in SUBSETS:
        T = T_by_subset[subset]
        cuts = np.quantile(T, [1 / 3, 2 / 3])
        sel = per_unit.subset == subset
        per_unit.loc[sel, "T"] = per_unit.loc[sel, "unit"].map(T)
        per_unit.loc[sel, "T_rank_desc"] = per_unit.loc[sel, "unit"].map(T.rank(ascending=False, method="min"))
        per_unit.loc[sel, "T_tercile"] = np.select([per_unit.loc[sel, "T"] <= cuts[0], per_unit.loc[sel, "T"] <= cuts[1]],
                                                   ["curta", "media"], "longa")
        out.append(dict(subset=subset, cut_1_3=cuts[0], cut_2_3=cuts[1]))
    terciles = (per_unit.groupby(["source", "chain", "subset", "T_tercile"])
                .agg(engines=("unit", "nunique"), event_rows=("events", "sum")).reset_index())
    return per_unit.sort_values(["source", "chain", "subset", "events"], ascending=[True, True, True, False]), terciles, pd.DataFrame(out)


def analyse():
    T_by = {s: lifetimes(s) for s in SUBSETS}
    ranges = pd.read_csv(P13E / "ranges.csv")
    ranges = ranges[ranges.chain == "M18"]
    markers = pd.read_csv(P13E / "decisions.csv", usecols=["unit", "usable_marker", "subset", "repeat", "chain", "policy_id"])
    first_marker = (markers[(markers.chain == "M18") & (markers.policy_id == "HI_MARKER_D1")]
                    .groupby(["subset", "unit"]).usable_marker.min().rename("min_marker"))
    rng = np.random.default_rng(BOOT_SEED)
    summary, engines = [], []
    for subset in SUBSETS:
        for quantity in QUANTITIES:
            r = ranges[(ranges.subset == subset) & (ranges.quantity == quantity)].copy()
            r["T"] = r.unit.map(T_by[subset])
            r["min_marker"] = [first_marker.get((subset, u), np.nan) for u in r.unit]
            finite = r[np.isfinite(r["range"])]
            rho, lo, hi = boot_spearman(finite["T"], finite["range"], rng)
            rel = finite["range"] / finite["T"]
            rrho, rlo, rhi = boot_spearman(finite["T"], rel, rng)
            mrho, mlo, mhi = boot_spearman(finite["min_marker"], finite["range"], rng)
            summary.append(dict(subset=subset, quantity=quantity, engines=len(r), finite=len(finite),
                                undefined=len(r) - len(finite), rho=rho, rho_lo=lo, rho_hi=hi,
                                rel_rho=rrho, rel_rho_lo=rlo, rel_rho_hi=rhi,
                                marker_rho=mrho, marker_rho_lo=mlo, marker_rho_hi=mhi,
                                **tail_metrics(finite["T"], finite["range"])))
            engines.append(r.assign(relative_range=r["range"] / r["T"]))
    summary = pd.DataFrame(summary)
    label, detail = classify(summary)
    per_unit, terciles, cuts = event_tables(T_by)
    return summary, pd.concat(engines, ignore_index=True), per_unit, terciles, cuts, label, detail


def figure(engines, path):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
    for ax, subset in zip(axes, SUBSETS):
        e = engines[(engines.subset == subset) & (engines.quantity == PRIMARY)]
        ax.scatter(e["T"], e["range"], s=14, color="#3b6ea8")
        for _, row in e[e["range"] > 30].iterrows():
            ax.annotate(f"u{int(row.unit)}", (row["T"], row["range"]), fontsize=8, xytext=(3, 3), textcoords="offset points")
        ax.axhline(WIDE, color="grey", lw=0.8, ls="--")
        ax.axvline(np.quantile(e["T"], TAIL_Q), color="grey", lw=0.8, ls=":")
        ax.set(title=subset, xlabel="Vida T (ciclos)", ylabel="Amplitude do marco entre repetições (ciclos)")
    fig.savefig(path, dpi=150)
    plt.close(fig)


def main():
    OUT.mkdir(exist_ok=True)
    previous = integrity()
    files = input_files()
    start = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=previous,
                 inputs={str(p.relative_to(ROOT)): sha(p) for p in files},
                 sources={n: sha(ROOT / "experiments" / n) for n in SOURCES})
    (OUT / "execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    summary, engines, per_unit, terciles, cuts, label, detail = analyse()
    summary.to_csv(OUT / "summary.csv", index=False)
    engines.to_csv(OUT / "engines.csv", index=False)
    per_unit.to_csv(OUT / "events_by_unit.csv", index=False)
    terciles.to_csv(OUT / "events_by_tercile.csv", index=False)
    cuts.to_csv(OUT / "tercile_cuts.csv", index=False)
    figure(engines, OUT / "range_vs_life.png")
    for n in SOURCES:
        (OUT / f"source_{n}").write_bytes((ROOT / "experiments" / n).read_bytes())
    (OUT / "classification.json").write_text(json.dumps(dict(primary=PRIMARY, label=label, detail=detail), indent=2), encoding="utf-8")
    assert integrity() == previous
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                   if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")
    print(label, json.dumps(detail))


if __name__ == "__main__":
    main()
