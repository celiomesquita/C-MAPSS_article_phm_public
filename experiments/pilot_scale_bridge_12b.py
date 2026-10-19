"""P12.2: scale bridge k, 20-year operational scenario and ordering stability (frozen P13.1 rules, train files only)."""
import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import kendalltau

import pilot_renewal_12a as p12a

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_scale_bridge_12b"
SRC = p12a.SRC
SUBSETS = p12a.SUBSETS
REFERENCE_CSV = ROOT / "references/cenario_economico_20anos/intervalos_referencia_k.csv"
L_REF = (4000.0, 5000.0, 6000.0, 7000.0, 8425.0, 10000.0, 12000.0, 14000.0, 16500.0, 19000.0)
UTILISATION = (1400.0, 1600.0, 1900.0)
LLP = (None, 20000.0, 25000.0, 30000.0)
IC = (0, 1)
RHO = (1.0, 0.8)
YEARS = 20
R_REPS, SEED = 2000, 20261018
Z_LIMIT, LONG_H = 4.0, 2_000_000.0
CENTRAL = dict(L_ref=8425.0, u=1600.0, llp=20000.0, ic=1, rho=1.0)
PAIRS = [("ISO_LOWER98_M15", "AGE"), ("HI_MARKER", "AGE"), ("ISO_LOWER98_M15", "HI_MARKER"),
         ("RF_SLOPE_LOWER98_M15", "ISO_LOWER98_M15"), ("HI_THRESHOLD_SELECTED", "HI_MARKER"),
         ("HI_WAIT_SELECTED", "HI_MARKER"), ("ISO_POINT_M15", "ISO_LOWER98_M15")]
SOURCES = ["protocolo_ponte_escala_12b.md", "pilot_scale_bridge_12b.py", "test_scale_bridge_12b.py", "verify_scale_bridge_12b.py"]


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
    files = [SRC, REFERENCE_CSV] + [ROOT / f"CMAPSSData/train_{s}.txt" for s in SUBSETS]
    assert not any(p.name.startswith(("test_FD", "RUL_FD")) or "FD002" in p.name or "FD004" in p.name for p in files)
    return files


def mean_lives():
    out = {}
    for s in SUBSETS:
        raw = pd.read_csv(ROOT / f"CMAPSSData/train_{s}.txt", sep=r"\s+", header=None, usecols=[0, 1], names=["unit", "cycle"])
        out[s] = float(raw.groupby("unit").cycle.max().mean())
    return out


def reference_median():
    d = pd.read_csv(REFERENCE_CSV)
    u = d[d.uso_na_calibracao == "sim"]
    return float(((u.lo_efc + u.hi_efc) / 2).median())


def scenario_seed(di, rep, li, ui, sc):
    return [SEED, di, rep, li, ui, sc]


def draws(u_all, k, rho, llp, horizon, di, rep, li, ui, sc):
    """Common random numbers for one cell: engine index stream and initial-condition uniforms."""
    nmax = int(np.ceil(horizon / (min(rho, 1.0) * k * u_all))) + (int(np.ceil(horizon / llp)) if llp else 0) + 6
    rng = np.random.default_rng(scenario_seed(di, rep, li, ui, sc))
    return rng.integers(0, 100, (R_REPS, nmax)), rng.random((3, R_REPS))


def simulate(u, e, k, rho, llp, horizon, ic, idx, init):
    """Vectorised renewal with LLP-forced visits; returns counts per replicate: D, L and endpoint events (missing, exact, late)."""
    n = idx.shape[0]
    rows = np.arange(n)
    t = np.zeros(n)
    big = np.inf if llp is None else float(llp)
    if ic == 0:
        a = np.zeros(n)
        eng = idx[:, 0]
        rem = k * u[eng]
        j = 1
    else:
        cdf = np.cumsum(u) / u.sum()
        eng = np.minimum(np.searchsorted(cdf, init[0], side="right"), len(u) - 1)
        rem = rho * k * u[eng] * (1.0 - init[1])
        a = init[2] * big if llp is not None else np.zeros(n)
        j = 0
    alive = np.ones(n, bool)
    d = np.zeros(n, int)
    l = np.zeros(n, int)
    miss = np.zeros(n, int)
    exact = np.zeros(n, int)
    late = np.zeros(n, int)
    while True:
        t_llp = t + (big - a)
        t_deg = t + rem
        is_llp = t_llp <= t_deg
        t_ev = np.where(is_llp, t_llp, t_deg)
        counted = alive & (t_ev <= horizon)
        by_deg = counted & ~is_llp
        d += by_deg
        l += counted & is_llp
        ev = e[eng]
        miss += by_deg & (ev == 1)
        exact += by_deg & (ev == 2)
        late += by_deg & (ev == 3)
        a = np.where(is_llp, 0.0, a + rem)
        t = t_ev
        alive = counted
        if not alive.any():
            break
        assert j < idx.shape[1], "draw stream exhausted"
        eng = idx[:, j]
        j += 1
        rem = rho * k * u[eng]
    return d, l, miss, exact, late


def lives_table():
    return p12a.load_lives()


def run_cell(lives, subset, repeat, k, rho, llp, ic, horizon, di, li, ui, sc, policies):
    u_all = min(v["utilised"].min() for kk, v in lives.items() if kk[0] == subset and kk[1] == repeat)
    idx, init = draws(u_all, k, rho, llp, horizon, di, repeat, li, ui, sc)
    return {pol: simulate(lives[(subset, repeat, pol)]["utilised"], lives[(subset, repeat, pol)]["event"], k, rho, llp, horizon, ic, idx, init)
            for pol in policies}


def classify(diff_mean, diff_se, analytic_diff):
    if diff_se == 0:
        return "indistinguivel" if diff_mean == 0 else ("estavel" if np.sign(diff_mean) == np.sign(analytic_diff) else "invertido")
    if abs(diff_mean) < 2 * diff_se:
        return "indistinguivel"
    return "estavel" if np.sign(diff_mean) == np.sign(analytic_diff) else "invertido"


def main():
    OUT.mkdir(exist_ok=True)
    previous = integrity()
    start = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=previous,
                 inputs={str(p.relative_to(ROOT)): sha(p) for p in input_files()},
                 sources={n: sha(ROOT / "experiments" / n) for n in SOURCES})
    (OUT / "execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    assert abs(reference_median() - 8425.0) < 1e-9
    lives = lives_table()
    tbar = mean_lives()
    rates = pd.read_csv(ART / "pilot_renewal_12a/rates.csv").set_index(["subset", "repeat", "policy_id"])["rate"].to_dict()
    policies = sorted({k[2] for k in lives})
    cells, pairs, kend = [], [], []
    for di, subset in enumerate(SUBSETS):
        for repeat in (1, 2, 3):
            for li, lref in enumerate(L_REF):
                k = lref / tbar[subset]
                for ui, u_yr in enumerate(UTILISATION):
                    horizon = YEARS * u_yr
                    for sc, (llp, ic, rho) in enumerate(itertools.product(LLP, IC, RHO)):
                        res = run_cell(lives, subset, repeat, k, rho, llp, ic, horizon, di, li, ui, sc, policies)
                        base = dict(subset=subset, repeat=repeat, L_ref=lref, k=k, u_yr=u_yr, horizon_fc=horizon,
                                    llp=llp if llp else 0.0, ic=ic, rho=rho)
                        for pol, (d, l, miss, exact, late) in res.items():
                            tot = d + l
                            rate = rates[(subset, repeat, pol)]
                            cells.append(dict(base, policy_id=pol, delay=lives[(subset, repeat, pol)]["delay"],
                                              d_mean=d.mean(), d_sd=d.std(ddof=1), l_mean=l.mean(), l_sd=l.std(ddof=1),
                                              tot_mean=tot.mean(), tot_sd=tot.std(ddof=1), miss_mean=miss.mean(),
                                              exact_mean=exact.mean(), late_mean=late.mean(), analytic_rate=rate,
                                              expected_stationary=horizon * rate / k))
                        for dly in (1, 2):
                            for a_name, b_name in PAIRS:
                                a_pol, b_pol = f"{a_name}_D{dly}", f"{b_name}_D{dly}"
                                da, la = res[a_pol][0], res[a_pol][1]
                                db, lb = res[b_pol][0], res[b_pol][1]
                                diff = (da + la) - (db + lb)
                                diffd = da - db
                                se = diff.std(ddof=1) / np.sqrt(R_REPS)
                                an = rates[(subset, repeat, a_pol)] - rates[(subset, repeat, b_pol)]
                                pairs.append(dict(base, delay=dly, a=a_pol, b=b_pol, diff_mean=diff.mean(), diff_se=se,
                                                  diffd_mean=diffd.mean(), diffd_se=diffd.std(ddof=1) / np.sqrt(R_REPS),
                                                  analytic_diff=an, status=classify(diff.mean(), se, an)))
                        tots = [cells[-len(res) + i]["tot_mean"] for i in range(len(res))]
                        rts = [cells[-len(res) + i]["analytic_rate"] for i in range(len(res))]
                        tau = kendalltau(tots, rts).statistic
                        kend.append(dict(base, kendall_tau=tau))
    cells = pd.DataFrame(cells)
    pairs = pd.DataFrame(pairs)
    kend = pd.DataFrame(kend)
    cells.to_csv(OUT / "cells.csv.gz", index=False)
    pairs.to_csv(OUT / "pairs.csv.gz", index=False)
    kend.to_csv(OUT / "kendall.csv.gz", index=False)
    # validation 1: stationary start without LLP, rho=1, matches H*rate/k at every grid horizon
    sel = cells[(cells.llp == 0) & (cells.ic == 1) & (cells.rho == 1.0)].copy()
    sel["z"] = (sel.tot_mean - sel.expected_stationary) / (sel.tot_sd / np.sqrt(R_REPS))
    # validation 2: long horizon, both initial conditions, no LLP
    long_rows = []
    for di, subset in enumerate(SUBSETS):
        for repeat in (1, 2, 3):
            k = 8425.0 / tbar[subset]
            res = run_cell(lives, subset, repeat, k, 1.0, None, 0, LONG_H, di, 99, 99, 99, ["AGE_D1", "HI_MARKER_D1", "ISO_LOWER98_M15_D1"])
            res1 = run_cell(lives, subset, repeat, k, 1.0, None, 1, LONG_H, di, 99, 99, 98, ["AGE_D1", "HI_MARKER_D1", "ISO_LOWER98_M15_D1"])
            for pol in res:
                rate = rates[(subset, repeat, pol)]
                for label, r in (("IC0", res), ("IC1", res1)):
                    sim = r[pol][0].mean() / LONG_H
                    long_rows.append(dict(subset=subset, repeat=repeat, policy_id=pol, ic=label, sim_rate_per_fc=sim,
                                          analytic_rate_per_fc=rate / k, relative_error=sim / (rate / k) - 1))
    long = pd.DataFrame(long_rows)
    # validation 3: LLP-forced visits identical across policies within a cell
    llp_sd = cells[cells.llp > 0].groupby(["subset", "repeat", "L_ref", "u_yr", "llp", "ic", "rho"]).l_mean.agg(lambda s: s.max() - s.min())
    validation = dict(stationary_cells=len(sel), stationary_max_abs_z=float(sel.z.abs().max()),
                      stationary_pass=bool(sel.z.abs().max() < Z_LIMIT), long_horizon_max_abs_rel_error=float(long.relative_error.abs().max()),
                      long_horizon_pass=bool(long.relative_error.abs().max() <= 0.01),
                      llp_equal_across_policies_max_range=float(llp_sd.max()), llp_pass=bool(llp_sd.max() < 1e-12))
    sel.to_csv(OUT / "validation_stationary.csv", index=False)
    long.to_csv(OUT / "validation_long_horizon.csv", index=False)
    (OUT / "validation.json").write_text(json.dumps(validation, indent=2), encoding="utf-8")
    # stability summaries
    factor_cols = {"subset": "subset", "k_band": None, "u_yr": "u_yr", "llp": "llp", "ic": "ic", "rho": "rho"}
    pairs["k_band"] = pd.cut(pairs.k, [0, 30, 50, 80, 1000], labels=["<30", "30-50", "50-80", ">80"])
    pairs["pair"] = pairs.a.str.replace(r"_D[12]$", "", regex=True) + " vs " + pairs.b.str.replace(r"_D[12]$", "", regex=True)
    rows = []
    for factor in factor_cols:
        g = pairs.groupby(["pair", factor], observed=True).status.value_counts().unstack(fill_value=0)
        g["n"] = g.sum(axis=1)
        for col in ("estavel", "indistinguivel", "invertido"):
            if col not in g:
                g[col] = 0
        g = g.reset_index().rename(columns={factor: "level"})
        g.insert(1, "factor", factor)
        rows.append(g[["pair", "factor", "level", "n", "estavel", "indistinguivel", "invertido"]])
    stability = pd.concat(rows, ignore_index=True)
    stability.to_csv(OUT / "stability.csv", index=False)
    overall = pairs.groupby("pair").status.value_counts().unstack(fill_value=0)
    overall.to_csv(OUT / "stability_overall.csv")
    central = cells[(cells.L_ref == CENTRAL["L_ref"]) & (cells.u_yr == CENTRAL["u"]) & (cells.llp == CENTRAL["llp"]) &
                    (cells.ic == CENTRAL["ic"]) & (cells.rho == CENTRAL["rho"])]
    central.to_csv(OUT / "central_scenario.csv", index=False)
    figure(cells, OUT / "restorations_20y.png")
    for n in SOURCES:
        (OUT / f"source_{n}").write_bytes((ROOT / "experiments" / n).read_bytes())
    assert integrity() == previous
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                   if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")
    print(json.dumps(validation, indent=2))
    print(overall)


def figure(cells, path):
    fig, axes = plt.subplots(1, 2, figsize=(11, 4), constrained_layout=True)
    for ax, subset in zip(axes, SUBSETS):
        for policy, color in [("AGE_D1", "#888888"), ("HI_MARKER_D1", "#d98e04"), ("ISO_LOWER98_M15_D1", "#3b6ea8")]:
            part = cells[(cells.subset == subset) & (cells.policy_id == policy) & (cells.u_yr == 1600.0) & (cells.llp == 0.0) &
                         (cells.ic == 1) & (cells.rho == 1.0)]
            m = part.groupby("L_ref").tot_mean.mean()
            ax.plot(m.index, m.values, marker="o", label=policy, color=color)
        ax.set(title=f"{subset}, 20 anos, 1.600 FC/ano, sem LLP, frota madura", xlabel="Intervalo de referência L_ref (EFC)",
               ylabel="Visitas por posição (média de 3 repetições)", yscale="log")
        ax.legend(fontsize=8)
    fig.savefig(path, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
