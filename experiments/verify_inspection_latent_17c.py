"""Independent verifier for P17.2: scalar P17.1 process (verify_inspection_arm_17b.one) with own Gauss-Hermite nodes."""
import json
from pathlib import Path

import numpy as np
import pandas as pd

import verify_inspection_arm_17b as v17

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT/"experiments/artifacts"
OUT = ART/"pilot_inspection_latent_17c"


def main():
    meta = json.loads((OUT/"metadata.json").read_text(encoding="utf-8"))
    for name, digest in json.loads((OUT/"manifest.json").read_text(encoding="utf-8")).items():
        assert v17.sha(OUT/name) == digest, name
    for folder, digest in meta["previous_manifests"].items():
        assert v17.sha(ART/folder/"manifest.json") == digest, folder
    x, w = np.polynomial.hermite_e.hermegauss(meta["nodes"])
    w = w/np.sqrt(2*np.pi)
    assert abs(w.sum()-1) < 1e-12
    ex = pd.read_csv(OUT/"expectations.csv.gz")
    src = pd.concat([pd.read_csv(ART/"pilot_policy_selection_13a/decisions.csv").assign(origin="development"),
                     pd.read_csv(ART/"confirmation_19a/decisions.csv").assign(origin="confirmation")])
    src = src.loc[src.dataset.eq("complete")].set_index(["origin", "subset", "repeat", "unit", "policy_id"])
    kinds = {v["scenario"]: (v["kind"], v["sigma"]) for v in meta["variants"]}
    assert len(ex) == len(src.loc[src.index.get_level_values(4).isin(ex.base+"_D1") | src.index.get_level_values(4).isin(ex.base+"_D2")])*3
    for r in ex.itertuples(index=False):
        row = src.loc[(r.origin, r.subset, r.repeat, r.unit, f"{r.base}_D{r.delay}")]
        has = bool(row.has_decision)
        D = float(row.decision) if has else np.nan
        kind, sigma = kinds[r.scenario]
        acc = np.zeros(6)
        for xi, wi in zip(x, w):
            W, g = (60.*np.exp(sigma*xi), 1.) if kind == "window" else (60., float(np.exp(sigma*xi)))
            acc += wi*np.array(v17.one(r.T, has, D, r.delay, 0., "S2", W, g, 0.))
        got = np.array([r.util_h, r.late_h, r.exact_h, r.missing_h, r.inspections, r.rejection])
        assert np.allclose(acc, got, atol=1e-8), (r, acc, got)
        assert r.util_h <= r.util_p+1e-9
    print(json.dumps(dict(verified=True, rows=len(ex)), indent=2))


if __name__ == "__main__":
    main()
