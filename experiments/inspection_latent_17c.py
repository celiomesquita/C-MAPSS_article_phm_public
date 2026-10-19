"""P17.2: latent per-engine detectability in the inspection arm (protocolo_inspecao_latente_17c.md)."""

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import inspection_arm_17b as base

ROOT, ART = base.ROOT, base.ART
OUT = ART/"pilot_inspection_latent_17c"
NODES = 21
MODULES = ["protocolo_inspecao_latente_17c.md", "inspection_latent_17c.py", "test_inspection_latent_17c.py",
           "verify_inspection_latent_17c.py"]
VARIANTS = [dict(scenario="L1_window_s0.25", kind="window", sigma=.25), dict(scenario="L2_window_s0.5", kind="window", sigma=.5),
            dict(scenario="L3_gamma_s0.5", kind="gamma", sigma=.5)]
X, WGT = np.polynomial.hermite_e.hermegauss(NODES)
WGT = WGT/WGT.sum()


def latent_expectation(T, has, D, d, kind, sigma, u=0.):
    keys = ("util", "late", "exact", "missing", "inspections", "rejection")
    total = dict.fromkeys(keys, 0.)
    for x, w in zip(X, WGT):
        W, g = (60.*np.exp(sigma*x), 1.) if kind == "window" else (60., float(np.exp(sigma*x)))
        h = base.hybrid_expectation(T, has, D, d, u, "S2", W, g, 0., 1.)
        for key in keys:
            total[key] += w*h[key]
    return total


def expectations(decisions):
    rows = []
    for r in decisions.itertuples(index=False):
        has = bool(r.has_decision)
        D = float(r.decision) if has else np.nan
        b = r.policy_id.rsplit("_D", 1)[0]
        p = base._phm(r.endpoint, has, D, int(r.delay), 0.)
        i = base.hybrid_expectation(r.endpoint, has, D, int(r.delay), 0., "S2", 60, 1., 0., 1.)
        for v in VARIANTS:
            h = latent_expectation(r.endpoint, has, D, int(r.delay), v["kind"], v["sigma"])
            rows.append(dict(origin=r.origin, subset=r.subset, repeat=r.repeat, fold=r.fold, unit=r.unit, base=b,
                             delay=int(r.delay), scenario=v["scenario"], u=0., T=int(r.endpoint), util_h=h["util"],
                             late_h=h["late"], exact_h=h["exact"], missing_h=h["missing"], inspections=h["inspections"],
                             rejection=h["rejection"], util_p=p["util"], late_p=p["late"], exact_p=p["exact"],
                             missing_p=p["missing"], util_indep=i["util"], rejection_indep=i["rejection"]))
    return pd.DataFrame(rows)


def summarise(ex):
    s = base.summarise(ex)
    extra = ex.groupby(["origin", "subset", "repeat", "base", "delay", "scenario", "u"], sort=True).apply(
        lambda g: pd.Series(dict(rate_change_independent=float(g.util_p.sum()/g.util_indep.sum()-1.))), include_groups=False).reset_index()
    return s.merge(extra, on=["origin", "subset", "repeat", "base", "delay", "scenario", "u"])


def main():
    assert not (OUT/"metadata.json").exists(), "completed run must be preserved"
    OUT.mkdir(parents=True, exist_ok=True)
    before = base.previous_integrity()
    start = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=before,
                 sources={n: base.sha(ROOT/"experiments"/n) for n in MODULES},
                 inputs={k: base.sha(v) for k, v in base.SOURCES.items()}, nodes=NODES, variants=VARIANTS)
    (OUT/"execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    ex = expectations(base.load_decisions())
    summary = summarise(ex)
    ex.to_csv(OUT/"expectations.csv.gz", index=False, compression="gzip")
    summary.to_csv(OUT/"summary.csv", index=False)
    assert before == base.previous_integrity()
    (OUT/"metadata.json").write_text(json.dumps(start | dict(finished_utc=datetime.now(timezone.utc).isoformat(), rows=len(ex),
                                    previous_manifests_intact=True), indent=2), encoding="utf-8")
    base.refresh_manifest(OUT)
    h = summary.loc[summary.delay.eq(1) & summary.base.isin(["ISO_POINT_M15", "ISO_LOWER98_M15"])]
    print(h.groupby(["subset", "base", "scenario"])[["rate_change", "rate_change_independent", "life_ceded"]].mean().round(3).to_string())


if __name__ == "__main__":
    main()
