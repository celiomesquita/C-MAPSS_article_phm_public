"""P16.1: PHM extension above the 127-cycle no-monitoring limit, with exact expectations over monitoring validity (train files only)."""
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

import pilot_fallback_15a as f15a

ROOT = f15a.ROOT
ART = f15a.ART
OUT = ART / "pilot_extension_16a"
P10 = ART / "pilot_f_uncertainty_10"
SRC = f15a.SRC
SUBSETS = f15a.SUBSETS
BASES = f15a.BASES
A = 127
US = (0.0, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 1.0)
SEED, BOOT = 20261018, 2000
SOURCES = ["protocolo_extensao_phm_16a.md", "pilot_extension_16a.py", "test_extension_16a.py", "verify_extension_16a.py"]


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
    files = [SRC] + sorted(P10.glob("predictions_*_complete.csv.gz")) + [ROOT / f"CMAPSSData/train_{s}.txt" for s in SUBSETS]
    assert not any(p.name.startswith(("test_FD", "RUL_FD")) or "FD002" in p.name or "FD004" in p.name for p in files)
    return files


def engine_expectation(T, has, D, d, orig_sched, u, age=A):
    """Exact expectation for one engine. Returns util, late, exact, missing, age_removal probabilities."""
    tau = age - d
    if has and D <= tau:                                             # PHM decided at or before the age gate: unaffected
        util = min(orig_sched, T)
        return dict(util=util, late=float(orig_sched > T), exact=float(orig_sched == T), missing=0.0, age_acts=0.0, extended=0.0)
    end = int(D) if has else int(T) - 1
    t = np.arange(tau, end + 1)                                        # validity checks at cycles tau..end
    p_first = u * (1 - u) ** (t - tau)
    sched = np.where(t == tau, age, t + d).astype(float)
    p_all = (1 - u) ** (end - tau + 1)
    util = (p_first * np.minimum(sched, T)).sum() + p_all * (min(orig_sched, T) if has else T)
    late = (p_first * (sched > T)).sum() + (p_all * float(orig_sched > T) if has else 0.0)
    exact = (p_first * (sched == T)).sum() + (p_all * float(orig_sched == T) if has else 0.0)
    missing = 0.0 if has else p_all
    return dict(util=float(util), late=float(late), exact=float(exact), missing=float(missing), age_acts=float(p_first[0]),
                extended=float(1 - p_first[0]))


def load():
    d = pd.read_csv(SRC)
    d = d[d.dataset == "complete"].copy()
    return d


def expectations(d):
    rows = []
    for base in BASES:
        for delay in (1, 2):
            g = d[d.policy_id == f"{base}_D{delay}"]
            for r in g.itertuples(index=False):
                has = bool(r.has_decision) and np.isfinite(r.decision)
                for u in US:
                    e = engine_expectation(float(r.endpoint), has, float(r.decision) if has else np.nan, delay,
                                           float(r.scheduled) if has else np.nan, u)
                    rows.append(dict(subset=r.subset, repeat=r.repeat, fold=r.fold, unit=r.unit, base=base, delay=delay, u=u,
                                     T=float(r.endpoint), orig_sched=float(r.scheduled) if has else np.nan, **e))
    return pd.DataFrame(rows)


def summary(ex):
    out = []
    for (subset, repeat, base, delay, u), g in ex.groupby(["subset", "repeat", "base", "delay", "u"]):
        n = len(g)
        out.append(dict(subset=subset, repeat=repeat, base=base, delay=delay, u=u, engines=n, mean_life=float(g.util.mean()),
                        rate=float(n / g.util.sum()), saving_vs_127=float(1 - A * n / g.util.sum()),
                        late_per100=float(100 * g.late.mean()), exact_per100=float(100 * g.exact.mean()),
                        missing_per100=float(100 * g.missing.mean()), age_removal_share=float(g.age_acts.mean()),
                        extended_share=float(g.extended.mean())))
    return pd.DataFrame(out)


def condition_dependence(d):
    hi = []
    for (subset, repeat, fold), g in d.groupby(["subset", "repeat", "fold"]):
        p = pd.read_csv(P10 / f"predictions_{subset}_r{repeat}_f{fold}_complete.csv.gz")
        p = p[(p.method == "ISO") & (p.cycle == A)][["unit", "hi"]].assign(subset=subset, repeat=repeat, fold=fold)
        hi.append(p)
    hi = pd.concat(hi, ignore_index=True).rename(columns={"hi": "hi127"})
    rows = []
    for base in BASES:
        for delay in (1, 2):
            g = d[d.policy_id == f"{base}_D{delay}"].merge(hi, on=["subset", "repeat", "fold", "unit"], how="left")
            g = g.assign(extension=np.where(g.has_decision, g.scheduled, g.endpoint) - A)
            for (subset, repeat), h in g.groupby(["subset", "repeat"]):
                ok = h.hi127.notna()
                rho_hi = spearmanr(h.hi127[ok], h.extension[ok]).statistic if ok.sum() > 3 else np.nan
                rho_T = spearmanr(h.endpoint, h.extension).statistic
                tert = pd.qcut(h.hi127[ok], 3, labels=["baixo", "medio", "alto"], duplicates="drop")
                means = h.extension[ok].groupby(tert, observed=True).mean()
                rows.append(dict(subset=subset, repeat=repeat, base=base, delay=delay, engines=len(h), with_hi=int(ok.sum()),
                                 extended_share=float((h.extension > 0).mean()), mean_extension=float(h.extension.mean()),
                                 recovered_headroom=float((h.extension.clip(lower=0).sum()) / (h.endpoint - A).sum()),
                                 spearman_ext_hi127=rho_hi, spearman_ext_T=rho_T,
                                 ext_hi_low=float(means.get("baixo", np.nan)), ext_hi_mid=float(means.get("medio", np.nan)),
                                 ext_hi_high=float(means.get("alto", np.nan))))
    return pd.DataFrame(rows), hi


def boot_savings(d):
    rng = np.random.default_rng([SEED, 16])
    rows = []
    for (subset, repeat, policy), g in d[d.policy_id.str.replace(r"_D[12]$", "", regex=True).isin(BASES)].groupby(["subset", "repeat", "policy_id"]):
        u = g.utilised.to_numpy(float)
        n = len(u)
        idx = rng.integers(0, n, (BOOT, n))
        b = 1 - A * n / u[idx].sum(axis=1)
        rows.append(dict(subset=subset, repeat=repeat, policy_id=policy, saving=float(1 - A * n / u.sum()),
                         lo=float(np.percentile(b, 2.5)), hi=float(np.percentile(b, 97.5))))
    return pd.DataFrame(rows)


def figure(s, path):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4), constrained_layout=True)
    for ax, subset in zip(axes, SUBSETS):
        for base, color in [("ISO_LOWER98_M15", "#3b6ea8"), ("HI_MARKER", "#d98e04"), ("ISO_POINT_M15", "#b04a4a")]:
            p = s[(s["subset"] == subset) & (s.base == base) & (s.delay == 1)].groupby("u").mean_life.mean()
            ax.plot(range(len(p)), p.values, marker="o", color=color, label=base)
        ax.axhline(A, color="grey", ls=":")
        ax.set_xticks(range(len(US)))
        ax.set_xticklabels([str(u) for u in US], rotation=45, fontsize=7)
        ax.set(title=f"{subset}, prazo 1", xlabel="Probabilidade de monitoramento inválido por ciclo (u)", ylabel="Vida média esperada (ciclos simulados)")
        ax.legend(fontsize=8)
    fig.savefig(path, dpi=150)
    plt.close(fig)


def main():
    OUT.mkdir(exist_ok=True)
    previous = integrity()
    (OUT / "execution_start.json").write_text(json.dumps(dict(
        started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=previous, age=A,
        inputs={str(p.relative_to(ROOT)): sha(p) for p in input_files()},
        sources={n: sha(ROOT / "experiments" / n) for n in SOURCES}), indent=2), encoding="utf-8")
    d = load()
    ex = expectations(d)
    s = summary(ex)
    cond, hi = condition_dependence(d)
    boot = boot_savings(d)
    ex.to_csv(OUT / "engine_expectations.csv.gz", index=False)
    s.to_csv(OUT / "summary.csv", index=False)
    cond.to_csv(OUT / "condition_dependence.csv", index=False)
    hi.to_csv(OUT / "hi_at_127.csv", index=False)
    boot.to_csv(OUT / "saving_vs_127_u0.csv", index=False)
    figure(s, OUT / "life_vs_availability.png")
    for n in SOURCES:
        (OUT / f"source_{n}").write_bytes((ROOT / "experiments" / n).read_bytes())
    assert integrity() == previous
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                   if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")
    pd.set_option("display.width", 220)
    print(s[s.delay == 1].groupby(["subset", "base", "u"]).agg(life=("mean_life", "mean"), sav=("saving_vs_127", "mean"),
          late=("late_per100", "mean"), exact=("exact_per100", "mean"), miss=("missing_per100", "mean")).round(3).to_string())
    print(cond[cond.delay == 1].groupby(["subset", "base"]).agg(ext=("extended_share", "mean"), mext=("mean_extension", "mean"),
          rec=("recovered_headroom", "mean"), rhi=("spearman_ext_hi127", "mean"), rT=("spearman_ext_T", "mean"),
          lo=("ext_hi_low", "mean"), mid=("ext_hi_mid", "mean"), hi=("ext_hi_high", "mean")).round(3).to_string())


if __name__ == "__main__":
    main()
