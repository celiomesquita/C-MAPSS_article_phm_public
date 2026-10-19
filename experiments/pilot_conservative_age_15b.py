"""P15.2: conservative fixed ages per dataset (train files only; dataset-level, in-sample by construction)."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_conservative_age_15b"
SUBSETS = ("FD001", "FD003")
RISK = 0.02
CONF = (0.80, 0.90, 0.95)
SEED, B_CI, B_GOF = 20261018, 2000, 500
SOURCES = ["protocolo_idade_conservadora_15b.md", "pilot_conservative_age_15b.py", "test_conservative_age_15b.py",
           "verify_conservative_age_15b.py"]


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
    assert not any(p.name.startswith(("test_FD", "RUL_FD")) or "FD002" in p.name or "FD004" in p.name for p in files)
    return files


def lifetimes():
    out = {}
    for s in SUBSETS:
        raw = pd.read_csv(ROOT / f"CMAPSSData/train_{s}.txt", sep=r"\s+", header=None, usecols=[0, 1], names=["unit", "cycle"])
        out[s] = raw.groupby("unit").cycle.max().to_numpy(float)
    return out


def cp_upper(k, n, conf):
    """One-sided Clopper-Pearson upper confidence limit of a binomial proportion."""
    return 1.0 if k >= n else float(stats.beta.ppf(conf, k + 1, n - k))


def nonparametric_age(t, risk, conf):
    """Largest age A whose Clopper-Pearson upper bound for P(T <= A) is <= risk; None if even N(A)=0 fails."""
    n = len(t)
    if cp_upper(0, n, conf) > risk:
        return None
    return int(t.min()) - 1


def weibull_fit(t):
    c, _, scale = stats.weibull_min.fit(t, floc=0)
    return float(c), float(scale)


def lognorm_fit(t):
    logs = np.log(t)
    return float(logs.mean()), float(logs.std(ddof=0))


def quantile(family, params, q):
    if family == "weibull":
        c, scale = params
        return scale * (-np.log1p(-q)) ** (1.0 / c)
    mu, sigma = params
    return float(np.exp(mu + sigma * stats.norm.ppf(q)))


def cdf(family, params, x):
    if family == "weibull":
        c, scale = params
        return stats.weibull_min.cdf(x, c, scale=scale)
    mu, sigma = params
    return stats.norm.cdf((np.log(x) - mu) / sigma)


def sample(family, params, n, rng):
    if family == "weibull":
        c, scale = params
        return scale * rng.weibull(c, n)
    mu, sigma = params
    return np.exp(rng.normal(mu, sigma, n))


def fit(family, t):
    return weibull_fit(t) if family == "weibull" else lognorm_fit(t)


def gof(family, params, t):
    x = np.sort(t)
    n = len(x)
    f = np.clip(cdf(family, params, x), 1e-12, 1 - 1e-12)
    d = max(np.max(np.arange(1, n + 1) / n - f), np.max(f - np.arange(0, n) / n))
    i = np.arange(1, n + 1)
    ad = -n - np.mean((2 * i - 1) * (np.log(f) + np.log(1 - f[::-1])))
    return float(d), float(ad)


def parametric(family, t, rng):
    params = fit(family, t)
    q_hat = quantile(family, params, RISK)
    boots, d_b, a_b = [], [], []
    for _ in range(B_CI):
        boots.append(quantile(family, fit(family, sample(family, params, len(t), rng)), RISK))
    d0, a0 = gof(family, params, t)
    for _ in range(B_GOF):
        s = sample(family, params, len(t), rng)
        db, ab = gof(family, fit(family, s), s)
        d_b.append(db)
        a_b.append(ab)
    return dict(family=family, params=params, q_hat=float(q_hat), q_lower95=float(np.percentile(boots, 5)),
                ks=d0, ks_p=float(np.mean(np.array(d_b) >= d0)), ad=a0, ad_p=float(np.mean(np.array(a_b) >= a0)))


def loo_arrival_rate(t):
    """Fraction of held-out engines with T_i <= min(T_-i) - 1 (arrival under the min-1 rule)."""
    hits = 0
    for i in range(len(t)):
        rest = np.delete(t, i)
        hits += t[i] <= rest.min() - 1
    return hits / len(t)


def age_costs(t, age):
    util = np.minimum(t, age)
    return dict(mean_utilised=float(util.mean()), mean_unused=float(np.maximum(t - age, 0).mean()),
                arrivals=int((t <= age).sum()), restorations_per_10000=float(1e4 / util.mean()))


def main():
    OUT.mkdir(exist_ok=True)
    previous = integrity()
    (OUT / "execution_start.json").write_text(json.dumps(dict(
        started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=previous,
        inputs={str(p.relative_to(ROOT)): sha(p) for p in input_files()},
        sources={n: sha(ROOT / "experiments" / n) for n in SOURCES}), indent=2), encoding="utf-8")
    t_by = lifetimes()
    rng = np.random.default_rng(SEED)
    rows, desc, gofs = [], [], []
    for subset in SUBSETS:
        t = t_by[subset]
        qs = np.percentile(t, [1, 2.5, 5, 10, 50])
        desc.append(dict(subset=subset, n=len(t), minimum=t.min(), p1=qs[0], p2_5=qs[1], p5=qs[2], p10=qs[3], median=qs[4],
                         maximum=t.max(), mean=t.mean(), cv=t.std(ddof=1) / t.mean(), second_smallest=np.sort(t)[1]))
        rows.append(dict(subset=subset, estimator="E0", detail="min-1 (todos os 100 motores)", age=int(t.min()) - 1,
                         bound_p=np.nan, **age_costs(t, int(t.min()) - 1)))
        for conf in CONF:
            age = nonparametric_age(t, RISK, conf)
            rows.append(dict(subset=subset, estimator="E1", detail=f"Clopper-Pearson gamma={conf}", age=age if age is not None else np.nan,
                             bound_p=cp_upper(0, len(t), conf), feasible=age is not None,
                             **(age_costs(t, age) if age is not None else {})))
        for family in ("weibull", "lognormal"):
            r = parametric(family, t, rng)
            age = int(np.floor(r["q_lower95"])) - 1
            rows.append(dict(subset=subset, estimator="E2", detail=f"{family} lower95 do quantil 2%", age=age, bound_p=np.nan,
                             q_hat=r["q_hat"], q_lower95=r["q_lower95"], **age_costs(t, age)))
            gofs.append(dict(subset=subset, family=family, param1=r["params"][0], param2=r["params"][1], ks=r["ks"], ks_p=r["ks_p"],
                             ad=r["ad"], ad_p=r["ad_p"]))
        rows.append(dict(subset=subset, estimator="E3", detail="LOO: taxa de chegada com min-1", age=np.nan,
                         bound_p=loo_arrival_rate(t)))
    pd.DataFrame(desc).to_csv(OUT / "descriptives.csv", index=False)
    pd.DataFrame(rows).to_csv(OUT / "estimates.csv", index=False)
    pd.DataFrame(gofs).to_csv(OUT / "goodness_of_fit.csv", index=False)
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), constrained_layout=True)
    estimates = pd.DataFrame(rows)
    for ax, subset in zip(axes, SUBSETS):
        ax.hist(t_by[subset], bins=25, color="#9bb7d4")
        for _, r in estimates[(estimates["subset"] == subset) & estimates.age.notna()].iterrows():
            ax.axvline(r.age, ls="--", lw=0.8, color="#b04a4a")
            ax.text(r.age, ax.get_ylim()[1] * 0.9, f"{r.estimator}:{int(r.age)}", rotation=90, fontsize=7, va="top")
        ax.set(title=subset, xlabel="Vida até o endpoint T (ciclos)", ylabel="Motores")
    fig.savefig(OUT / "lives_and_ages.png", dpi=150)
    plt.close(fig)
    for n in SOURCES:
        (OUT / f"source_{n}").write_bytes((ROOT / "experiments" / n).read_bytes())
    assert integrity() == previous
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                   if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")
    pd.set_option("display.width", 220)
    print(pd.DataFrame(desc).round(2).to_string(index=False))
    print(estimates.round(4).to_string(index=False))
    print(pd.DataFrame(gofs).round(4).to_string(index=False))


if __name__ == "__main__":
    main()
