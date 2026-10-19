"""P12.1: AGAN renewal accounting per simulated exposure and parametrised horizon (frozen P13.1 rules, train files only)."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "experiments/artifacts"
OUT = ART / "pilot_renewal_12a"
SRC = ART / "pilot_policy_selection_13a/decisions.csv"
SUBSETS = ("FD001", "FD003")
SCALES = (1, 10, 50, 100, 150)               # flight cycles per simulated cycle: grid values, no recommendation
FLIGHT_CYCLES_20Y = 32000
H_VALIDATION = 1_000_000
R_REPS, BOOT, SEED = 2000, 2000, 20261018
COST_USD = 6_000_000
TOL = 0.01
EVENT_CODE = {"preventive_schedule": 0, "endpoint_without_decision": 1, "at_endpoint": 2, "late_schedule": 3}
SOURCES = ["protocolo_renovacao_12a.md", "pilot_renewal_12a.py", "test_renewal_12a.py", "verify_renewal_12a.py"]


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
    files = [SRC]
    assert not any(p.name.startswith(("test_FD", "RUL_FD")) or "FD002" in p.name or "FD004" in p.name for p in files)
    return files


def load_lives():
    d = pd.read_csv(SRC)
    d = d[d.dataset == "complete"].copy()
    d["event"] = d.status.map(EVENT_CODE)
    assert d.event.notna().all()
    lives = {}
    for (subset, repeat, policy), g in d.groupby(["subset", "repeat", "policy_id"]):
        g = g.sort_values("unit")
        lives[(subset, int(repeat), policy)] = dict(unit=g.unit.to_numpy(), utilised=g.utilised.to_numpy(float),
                                                    event=g.event.to_numpy(int), delay=int(g.delay.iloc[0]))
    return lives


def reference_of(policy, delay):
    return {"AGE": f"AGE_D{delay}", "HI_MARKER": f"HI_MARKER_D{delay}"}


def renewal(utilised, event, idx, horizon):
    """Restorations completed by `horizon` for sampled engine sequences idx[R, N]; returns counts, used and event counts."""
    cum = np.cumsum(utilised[idx], axis=1)
    count = (cum <= horizon).sum(axis=1)
    assert (count < idx.shape[1]).all(), "sequence too short for horizon"
    col = np.arange(idx.shape[1])[None, :]
    done = col < count[:, None]
    ev = event[idx]
    used = np.where(count > 0, cum[np.arange(len(count)), np.maximum(count - 1, 0)], 0.0)
    return count, used, [(done & (ev == c)).sum(axis=1) for c in (1, 2, 3)]


def sequences(subset, repeat, horizon_key, horizon, lives, n_engines=100):
    min_life = min(v["utilised"].min() for k, v in lives.items() if k[0] == subset and k[1] == repeat)
    nmax = int(np.ceil(horizon / min_life)) + 3
    rng = np.random.default_rng([SEED, SUBSETS.index(subset), repeat, horizon_key])
    return rng.integers(0, n_engines, (R_REPS, nmax))


def analytic(lives):
    rows = []
    for (subset, repeat, policy), v in sorted(lives.items()):
        n, exposure = len(v["utilised"]), float(v["utilised"].sum())
        rows.append(dict(subset=subset, repeat=repeat, policy_id=policy, delay=v["delay"], engines=n, exposure=exposure,
                         rate=n / exposure, mean_utilised=exposure / n, restorations_per_10000=10000 * n / exposure,
                         missing=int((v["event"] == 1).sum()), exact=int((v["event"] == 2).sum()), strict_late=int((v["event"] == 3).sum())))
    return pd.DataFrame(rows)


def analytic_contrasts(lives):
    rows = []
    rng = np.random.default_rng([SEED, 99])
    for (subset, repeat, policy), v in sorted(lives.items()):
        for ref_name in ("AGE", "HI_MARKER"):
            ref = f"{ref_name}_D{v['delay']}"
            if policy == ref:
                continue
            base = lives[(subset, repeat, ref)]
            assert (base["unit"] == v["unit"]).all()
            idx = rng.integers(0, len(v["unit"]), (BOOT, len(v["unit"])))
            rp = len(v["unit"]) / v["utilised"][idx].sum(axis=1)
            rb = len(v["unit"]) / base["utilised"][idx].sum(axis=1)
            diff = rp - rb
            rel = 1 - rp / rb
            point = 1 - (len(v["unit"]) / v["utilised"].sum()) / (len(v["unit"]) / base["utilised"].sum())
            rows.append(dict(subset=subset, repeat=repeat, policy_id=policy, reference=ref, delay=v["delay"],
                             rate_diff=len(v["unit"]) / v["utilised"].sum() - len(v["unit"]) / base["utilised"].sum(),
                             saving=point, saving_lo=np.percentile(rel, 2.5), saving_hi=np.percentile(rel, 97.5)))
    return pd.DataFrame(rows)


def horizon_tables(lives):
    rows, contrasts, validation = [], [], []
    for subset in SUBSETS:
        for repeat in (1, 2, 3):
            keys = sorted(k for k in lives if k[0] == subset and k[1] == repeat)
            grid = [(f"k{k}", FLIGHT_CYCLES_20Y / k, k) for k in SCALES] + [("validation", float(H_VALIDATION), 0)]
            for label, horizon, hk in grid:
                idx = sequences(subset, repeat, hk, horizon, lives)
                results = {}
                for (_, _, policy) in keys:
                    v = lives[(subset, repeat, policy)]
                    results[policy] = renewal(v["utilised"], v["event"], idx, horizon)
                for (_, _, policy) in keys:
                    count, used, ev = results[policy]
                    v = lives[(subset, repeat, policy)]
                    rate = len(v["utilised"]) / v["utilised"].sum()
                    row = dict(subset=subset, repeat=repeat, scale=label, scale_k=hk, horizon=horizon, policy_id=policy,
                               delay=v["delay"], restorations_mean=count.mean(), restorations_sd=count.std(ddof=1),
                               cost_usd_mean=COST_USD * count.mean(), used_exposure_mean=used.mean(),
                               residual_exposure_mean=(horizon - used).mean(),
                               missing_mean=ev[0].mean(), exact_mean=ev[1].mean(), strict_late_mean=ev[2].mean(),
                               analytic_rate=rate, sim_rate=count.mean() / horizon, edge_ratio=count.mean() / horizon / rate)
                    rows.append(row)
                    if label == "validation":
                        validation.append(dict(subset=subset, repeat=repeat, policy_id=policy, analytic_rate=rate,
                                               sim_rate=row["sim_rate"], relative_error=row["sim_rate"] / rate - 1,
                                               passes=bool(abs(row["sim_rate"] / rate - 1) <= TOL)))
                if label == "validation":
                    continue
                for (_, _, policy) in keys:
                    v = lives[(subset, repeat, policy)]
                    for ref_name in ("AGE", "HI_MARKER"):
                        ref = f"{ref_name}_D{v['delay']}"
                        if policy == ref:
                            continue
                        diff = results[policy][0] - results[ref][0]
                        contrasts.append(dict(subset=subset, repeat=repeat, scale=label, scale_k=hk, horizon=horizon,
                                              policy_id=policy, reference=ref, restorations_diff_mean=diff.mean(),
                                              restorations_diff_lo=np.percentile(diff, 2.5), restorations_diff_hi=np.percentile(diff, 97.5),
                                              cost_usd_diff_mean=COST_USD * diff.mean(),
                                              fraction_replicates_fewer=float((diff < 0).mean())))
    return pd.DataFrame(rows), pd.DataFrame(contrasts), pd.DataFrame(validation)


def figure(horizon, path):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
    for ax, subset in zip(axes, SUBSETS):
        for policy, color in [("AGE_D1", "#888888"), ("HI_MARKER_D1", "#d98e04"), ("ISO_LOWER98_M15_D1", "#3b6ea8")]:
            part = horizon[(horizon.subset == subset) & (horizon.policy_id == policy) & (horizon.scale != "validation")]
            m = part.groupby("horizon").restorations_mean.mean().sort_index()
            ax.plot(m.index, m.values, marker="o", label=policy, color=color)
        ax.set(title=f"{subset} (média das 3 repetições; não são motores independentes)", xlabel="Horizonte (ciclos simulados)",
               ylabel="Restaurações por posição", xscale="log", yscale="log")
        ax.legend(fontsize=8)
    fig.savefig(path, dpi=150)
    plt.close(fig)


def main():
    OUT.mkdir(exist_ok=True)
    previous = integrity()
    start = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=previous,
                 inputs={str(p.relative_to(ROOT)): sha(p) for p in input_files()},
                 sources={n: sha(ROOT / "experiments" / n) for n in SOURCES})
    (OUT / "execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    lives = load_lives()
    analytic(lives).to_csv(OUT / "rates.csv", index=False)
    analytic_contrasts(lives).to_csv(OUT / "rate_contrasts.csv", index=False)
    horizon, contrasts, validation = horizon_tables(lives)
    horizon.to_csv(OUT / "horizon.csv", index=False)
    contrasts.to_csv(OUT / "horizon_contrasts.csv", index=False)
    validation.to_csv(OUT / "validation.csv", index=False)
    figure(horizon, OUT / "restorations_vs_horizon.png")
    for n in SOURCES:
        (OUT / f"source_{n}").write_bytes((ROOT / "experiments" / n).read_bytes())
    assert integrity() == previous
    (OUT / "manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                   if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")
    print("validation passes:", int(validation.passes.sum()), "/", len(validation), "max |rel err|", validation.relative_error.abs().max())


if __name__ == "__main__":
    main()
