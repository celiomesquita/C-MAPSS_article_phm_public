"""P15.1: candidate fallback policy - PHM decision when it exists, age rule otherwise (frozen P13.1 rules, train files only)."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import pilot_scale_bridge_12b as bridge

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_fallback_15a"
SRC = ART / "pilot_policy_selection_13a/decisions.csv"
SPLITS = ART / "pilot_f_uncertainty_10/splits.json"
SUBSETS = ("FD001", "FD003")
BASES = ("ISO_LOWER98_M15", "RF_SLOPE_LOWER98_M15", "ISO_POINT_M15", "RF_SLOPE_POINT_M15", "HI_MARKER",
         "HI_THRESHOLD_SELECTED", "HI_WAIT_SELECTED")
QS = (0.0, 0.05, 0.10, 0.25, 0.50)
SEED, BOOT = 20261018, 2000
EPS = 1e-9
CENTRAL_L = (5000.0, 8425.0, 12000.0)
SOURCES = ["protocolo_reserva_idade_15a.md", "pilot_fallback_15a.py", "test_fallback_15a.py", "verify_fallback_15a.py"]


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
    files = [SRC, SPLITS] + [ROOT / f"CMAPSSData/train_{s}.txt" for s in SUBSETS]
    assert not any(p.name.startswith(("test_FD", "RUL_FD")) or "FD002" in p.name or "FD004" in p.name for p in files)
    return files


def endpoints():
    out = {}
    for s in SUBSETS:
        raw = pd.read_csv(ROOT / f"CMAPSSData/train_{s}.txt", sep=r"\s+", header=None, usecols=[0, 1], names=["unit", "cycle"])
        out[s] = raw.groupby("unit").cycle.max()
    return out


def age_table(ends):
    """Fallback ages A_q per (subset, repeat, fold), from the development engines F and C only."""
    rows = []
    for e in json.loads(SPLITS.read_text(encoding="utf-8")):
        dev = list(e["fit"]) + list(e["converter"])
        t = ends[e["subset"]].loc[dev].to_numpy(float)
        for q in QS:
            rows.append(dict(subset=e["subset"], repeat=e["repeat"], fold=e["fold"], q=q,
                             age=int(np.floor(np.quantile(t, q))) - 1, dev_engines=len(dev)))
    return pd.DataFrame(rows)


def hybrid(base, age, delay):
    """base: rows of one PHM rule (decision NaN when absent); age: Series aligned by index (A_q). Returns hybrid columns."""
    endpoint = base.endpoint.to_numpy(float)
    dec_phm = base.decision.to_numpy(float)
    tau = age.to_numpy(float) - delay
    dec_age = np.where((tau >= 1) & (tau < endpoint), tau, np.nan)
    dec = np.fmin(dec_phm, dec_age)
    has = np.isfinite(dec)
    sched = np.where(has, dec + delay, np.nan)
    age_acts = np.isfinite(dec_age) & (~np.isfinite(dec_phm) | (dec_age < dec_phm))
    late = has & (sched > endpoint)
    exact = has & (sched == endpoint)
    status = np.where(~has, "endpoint_without_decision", np.where(late, "late_schedule", np.where(exact, "at_endpoint", "preventive_schedule")))
    utilised = np.where(has, np.minimum(sched, endpoint), endpoint)
    return pd.DataFrame(dict(dec=dec, sched=sched, has=has, age_acts=age_acts, late=late, exact=exact, status=status,
                             utilised=utilised, endpoint=endpoint), index=base.index)


def build():
    d = pd.read_csv(SRC)
    d = d[d.dataset == "complete"].copy()
    ends = endpoints()
    ages = age_table(ends)
    rows = []
    for (subset, repeat, fold), g in d.groupby(["subset", "repeat", "fold"]):
        for delay in (1, 2):
            for q in QS:
                a = ages[(ages["subset"] == subset) & (ages.repeat == repeat) & (ages.fold == fold) & (ages.q == q)].age.iloc[0]
                for base in BASES:
                    b = g[g.policy_id == f"{base}_D{delay}"].sort_values("unit")
                    h = hybrid(b, pd.Series(a, index=b.index), delay)
                    rows.append(b[["subset", "repeat", "fold", "unit"]].assign(base=base, delay=delay, q=q, age=a, **{c: h[c] for c in h}))
    return pd.concat(rows, ignore_index=True), d, ages


def summarise(h, d):
    out = []
    for (subset, repeat, base, delay, q), g in h.groupby(["subset", "repeat", "base", "delay", "q"]):
        n = len(g)
        original = d[(d.subset == subset) & (d.repeat == repeat) & (d.policy_id == f"{base}_D{delay}")].sort_values(["fold", "unit"])
        g = g.sort_values(["fold", "unit"])
        assert (original.unit.to_numpy() == g.unit.to_numpy()).all()
        out.append(dict(subset=subset, repeat=repeat, base=base, delay=delay, q=q, engines=n, decisions=int(g.has.sum()),
                        missing=int((~g.has).sum()), exact=int(g.exact.sum()), strict_late=int(g.late.sum()),
                        mean_utilised=float(g.utilised.mean()), rate=float(n / g.utilised.sum()),
                        fallback_share=float(g.age_acts.mean()), fallback_age_median=float(g.age.median()),
                        original_mean_utilised=float(original.utilised.mean()), original_rate=float(n / original.utilised.sum()),
                        original_missing=int((~original.has_decision.astype(bool)).sum()), original_exact=int(original.exact_endpoint.sum()),
                        original_late=int(original.late.sum()),
                        life_given_up=float(original.utilised.mean() - g.utilised.mean()),
                        strict_screen=bool(g.has.all() and g.late.mean() <= .02 + EPS),
                        prudent_screen=bool(g.has.all() and g.late.mean() <= .02 + EPS and not g.exact.any())))
    return pd.DataFrame(out)


def references(h, d):
    """Utilised lives of the controls per (subset, repeat, delay), ordered like the hybrid rows."""
    refs = {}
    for (subset, repeat, delay), g in h.groupby(["subset", "repeat", "delay"]):
        order = g[(g.base == BASES[0]) & (g.q == 0.0)].sort_values(["fold", "unit"])[["fold", "unit"]]
        for name in ("AGE", "HI_MARKER"):
            r = d[(d.subset == subset) & (d.repeat == repeat) & (d.policy_id == f"{name}_D{delay}")]
            r = order.merge(r[["fold", "unit", "utilised"]], on=["fold", "unit"], how="left")
            assert r.utilised.notna().all()
            refs[(subset, repeat, delay, name)] = r.utilised.to_numpy(float)
    return refs


def savings(h, refs):
    rng = np.random.default_rng([SEED, 7])
    rows = []
    for (subset, repeat, base, delay, q), g in h.groupby(["subset", "repeat", "base", "delay", "q"]):
        g = g.sort_values(["fold", "unit"])
        u = g.utilised.to_numpy(float)
        n = len(u)
        idx = rng.integers(0, n, (BOOT, n))
        for name in ("AGE", "HI_MARKER"):
            ref = refs[(subset, repeat, delay, name)]
            point = 1 - ref.sum() / u.sum()
            boot = 1 - (ref[idx].sum(axis=1) / u[idx].sum(axis=1))
            rows.append(dict(subset=subset, repeat=repeat, base=base, delay=delay, q=q, reference=name, saving=point,
                             saving_lo=np.percentile(boot, 2.5), saving_hi=np.percentile(boot, 97.5)))
    return pd.DataFrame(rows)


def central_scenario(h, ends_by_subset):
    tbar = bridge.mean_lives()
    rows = []
    for (subset, repeat), part in h.groupby(["subset", "repeat"]):
        di = bridge.SUBSETS.index(subset)
        u_all = float(part.utilised.min())
        rules = {key: g.sort_values(["fold", "unit"]) for key, g in part.groupby(["base", "delay", "q"])}
        for li, lref in enumerate(bridge.L_REF):
            if lref not in CENTRAL_L:
                continue
            k = lref / tbar[subset]
            for sc, llp in enumerate((None, 20000.0)):
                horizon = 20 * 1600.0
                idx, init = bridge.draws(u_all, k, 1.0, llp, horizon, di, repeat, li, 1, sc)
                for (base, delay, q), g in rules.items():
                    u = g.utilised.to_numpy(float)
                    ev = np.where(~g.has.to_numpy(bool), 1, np.where(g.exact.to_numpy(bool), 2, np.where(g.late.to_numpy(bool), 3, 0)))
                    dcount, lcount, miss, exact, late = bridge.simulate(u, ev, k, 1.0, llp, horizon, 1, idx, init)
                    rows.append(dict(subset=subset, repeat=repeat, base=base, delay=delay, q=q, L_ref=lref, k=k, llp=llp or 0.0,
                                     visits=float((dcount + lcount).mean()), d_visits=float(dcount.mean()),
                                     llp_visits=float(lcount.mean()), events=float((miss + exact + late).mean())))
    return pd.DataFrame(rows)


def figure(summary, path):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4), constrained_layout=True)
    for ax, subset in zip(axes, SUBSETS):
        for base, color in [("ISO_LOWER98_M15", "#3b6ea8"), ("HI_MARKER", "#d98e04"), ("ISO_POINT_M15", "#b04a4a")]:
            part = summary[(summary["subset"] == subset) & (summary.base == base) & (summary.delay == 1)]
            m = part.groupby("q").mean_utilised.mean()
            ax.plot(m.index, m.values, marker="o", label=f"{base} + idade", color=color)
            ax.axhline(part.original_mean_utilised.mean(), color=color, ls=":", lw=0.8)
        ax.set(title=f"{subset}, prazo 1 (pontilhado: regra PHM original)", xlabel="Quantil q da idade de reserva (desenvolvimento)",
               ylabel="Vida média aproveitada (ciclos simulados)")
        ax.legend(fontsize=8)
    fig.savefig(path, dpi=150)
    plt.close(fig)


def main():
    OUT.mkdir(exist_ok=True)
    previous = integrity()
    (OUT / "execution_start.json").write_text(json.dumps(dict(
        started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=previous,
        inputs={str(p.relative_to(ROOT)): sha(p) for p in input_files()},
        sources={n: sha(ROOT / "experiments" / n) for n in SOURCES}), indent=2), encoding="utf-8")
    h, d, ages = build()
    summary = summarise(h, d)
    refs = references(h, d)
    sav = savings(h, refs)
    central = central_scenario(h, None)
    ages.to_csv(OUT / "fallback_ages.csv", index=False)
    h.to_csv(OUT / "hybrid_decisions.csv.gz", index=False)
    summary.to_csv(OUT / "summary.csv", index=False)
    sav.to_csv(OUT / "savings.csv", index=False)
    central.to_csv(OUT / "central_scenario.csv", index=False)
    figure(summary, OUT / "life_vs_q.png")
    for n in SOURCES:
        (OUT / f"source_{n}").write_bytes((ROOT / "experiments" / n).read_bytes())
    assert integrity() == previous
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                   if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")
    print(summary.groupby(["subset", "base", "q"]).agg(fallback=("fallback_share", "mean"), life=("mean_utilised", "mean"),
                                                       orig=("original_mean_utilised", "mean"), missing=("missing", "sum"),
                                                       exact=("exact", "sum"), late=("strict_late", "sum")).round(3).to_string())


if __name__ == "__main__":
    main()
