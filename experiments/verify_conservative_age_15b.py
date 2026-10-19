"""Independent verifier for P15.2: descriptives, binomial inversion, order-statistic ages, LOO and parametric bootstrap with own fitting."""
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_conservative_age_15b"
SUBSETS = ("FD001", "FD003")
SEED, B_CI, B_GOF, RISK = 20261018, 2000, 500, 0.02


def binom_cdf(k, n, p):
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))


def cp_upper(k, n, conf):
    """Largest p with P(Bin(n,p) <= k) >= 1 - conf, by bisection on the binomial CDF."""
    if k >= n:
        return 1.0
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if binom_cdf(k, n, mid) > 1 - conf:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def weibull_mle(x):
    lx = np.log(x)

    def score(c):
        xc = x ** c
        return (xc * lx).sum() / xc.sum() - 1.0 / c - lx.mean()

    c = brentq(score, 0.05, 100.0, xtol=1e-12)
    return c, float(np.mean(x ** c) ** (1.0 / c))


def lognorm_mle(x):
    l = np.log(x)
    return float(l.mean()), float(np.sqrt(np.mean((l - l.mean()) ** 2)))


def q_weibull(c, s, q):
    return s * (-math.log(1 - q)) ** (1 / c)


def q_lognorm(mu, sg, q):
    from statistics import NormalDist
    return math.exp(mu + sg * NormalDist().inv_cdf(q))


def main():
    t_by = {}
    for s in SUBSETS:
        raw = pd.read_csv(ROOT / f"CMAPSSData/train_{s}.txt", sep=r"\s+", header=None, usecols=[0, 1], names=["u", "c"])
        t_by[s] = np.array(sorted(raw.groupby("u").c.max()), float)
    desc = pd.read_csv(OUT / "descriptives.csv").set_index("subset")
    est = pd.read_csv(OUT / "estimates.csv")
    gof = pd.read_csv(OUT / "goodness_of_fit.csv")
    rng = np.random.default_rng(SEED)
    checks = 0
    for s in SUBSETS:
        t = t_by[s]
        n = len(t)
        d = desc.loc[s]
        assert d.n == n and d.minimum == t[0] and d.maximum == t[-1] and d.second_smallest == t[1]
        assert abs(d["mean"] - t.mean()) < 1e-9
        e0 = est[(est["subset"] == s) & (est.estimator == "E0")].iloc[0]
        assert e0.age == t[0] - 1 and e0.arrivals == 0
        assert abs(e0.mean_utilised - np.minimum(t, t[0] - 1).mean()) < 1e-9
        for conf in (0.80, 0.90, 0.95):
            r = est[(est["subset"] == s) & (est.estimator == "E1") & est.detail.str.contains(f"gamma={conf}")].iloc[0]
            p_u = cp_upper(0, n, conf)
            assert abs(r.bound_p - p_u) < 1e-9
            if p_u <= RISK:
                assert r.feasible and r.age == t[0] - 1
            else:
                assert not r.feasible and np.isnan(r.age)
            checks += 1
        e3 = est[(est["subset"] == s) & (est.estimator == "E3")].iloc[0]
        hits = sum(1 for i in range(n) if t[i] <= min(np.delete(t, i)) - 1)
        assert abs(e3.bound_p - hits / n) < 1e-12
        for family, fit, qf in (("weibull", weibull_mle, q_weibull), ("lognormal", lognorm_mle, q_lognorm)):
            p1, p2 = fit(t)
            q_hat = qf(p1, p2, RISK)

            def draw():
                if family == "weibull":
                    return p2 * rng.weibull(p1, n)
                return np.exp(rng.normal(p1, p2, n))

            boots = [qf(*fit(draw()), RISK) for _ in range(B_CI)]
            for _ in range(B_GOF):
                fit(draw())
            lower = float(np.percentile(boots, 5))
            row = est[(est["subset"] == s) & (est.estimator == "E2") & est.detail.str.contains(family)].iloc[0]
            assert abs(row.q_hat - q_hat) / q_hat < 1e-5, (s, family, row.q_hat, q_hat)
            assert abs(row.q_lower95 - lower) / lower < 1e-4, (s, family, row.q_lower95, lower)
            assert row.age == int(math.floor(lower)) - 1
            g = gof[(gof["subset"] == s) & (gof.family == family)].iloc[0]
            assert abs(g.param1 - p1) / abs(p1) < 1e-4 and abs(g.param2 - p2) / abs(p2) < 1e-4
            checks += 1
    for folder in sorted(ART.glob("pilot_*")):
        mf = folder / "manifest.json"
        if folder == OUT or not mf.exists():
            continue
        for n_, h in json.loads(mf.read_text(encoding="utf-8")).items():
            assert hashlib.sha256((folder / n_).read_bytes()).hexdigest() == h, (folder.name, n_)
    result = dict(status="passed", checks=checks, note="goodness-of-fit p-values are not independently replayed beyond parameters")
    (OUT / "verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(result)


if __name__ == "__main__":
    main()
