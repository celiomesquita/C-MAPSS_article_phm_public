"""P19.2: stability of HI coefficients across folds from stored models (no data, no refitting)."""
import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT/"experiments/artifacts"
OUT = ART/"pilot_coefficient_stability_19b"
SOURCES = {"FD001": ART/"pilot_f_uncertainty_10", "FD003": ART/"pilot_f_uncertainty_10",
           "FD002": ART/"confirmation_19a", "FD004": ART/"confirmation_19a"}
MODULES = ["protocolo_estabilidade_coeficientes_19b.md", "coefficient_stability_19b.py", "test_coefficient_stability_19b.py",
           "verify_coefficient_stability_19b.py"]
ACTIVE = 1e-9


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def fold_record(bundle):
    s = bundle["health"]["stats"]
    return dict(zip(s["channels"], zip(np.asarray(s["direction"], float), np.asarray(bundle["health"]["beta"], float))))


def pair_metrics(a, b):
    common = sorted(set(a) & set(b), key=lambda c: int(c[1:]))
    wa = np.array([a[c][1] for c in common]); wb = np.array([b[c][1] for c in common])
    da = np.array([a[c][0] for c in common]); db = np.array([b[c][0] for c in common])
    rho = float(spearmanr(wa, wb).statistic) if len(common) > 2 and wa.std() > 0 and wb.std() > 0 else np.nan
    act_a = {c for c in a if a[c][1] > ACTIVE}
    act_b = {c for c in b if b[c][1] > ACTIVE}

    def top(r):
        return set(sorted(r, key=lambda c: (-r[c][1], int(c[1:])))[:3])

    return dict(common=len(common), spearman=rho, same_direction=float((da == db).mean()) if len(common) else np.nan,
                jaccard_active=len(act_a & act_b)/len(act_a | act_b) if act_a | act_b else np.nan,
                top3_overlap=len(top(a) & top(b))/3.)


def load(subset):
    folder = SOURCES[subset]
    return {repeat: [fold_record(joblib.load(folder/f"models_{subset}_r{repeat}_f{f}.joblib")) for f in range(1, 11)]
            for repeat in (1, 2, 3)}


def run():
    pairs, channels = [], []
    for subset in SOURCES:
        for repeat, records in load(subset).items():
            for (i, a), (j, b) in itertools.combinations(enumerate(records, start=1), 2):
                pairs.append(dict(subset=subset, repeat=repeat, fold_a=i, fold_b=j, **pair_metrics(a, b)))
            for c in sorted({c for r in records for c in r}, key=lambda c: int(c[1:])):
                present = [r for r in records if c in r]
                active = [r[c][1] for r in present if r[c][1] > ACTIVE]
                channels.append(dict(subset=subset, repeat=repeat, channel=c, retained=len(present)/10.,
                                     active=len(active)/10., positive_direction=float(np.mean([r[c][0] > 0 for r in present])),
                                     mean_weight_active=float(np.mean(active)) if active else np.nan,
                                     median_weight_active=float(np.median(active)) if active else np.nan))
    return pd.DataFrame(pairs), pd.DataFrame(channels)


def main():
    assert not (OUT/"metadata.json").exists()
    OUT.mkdir(parents=True, exist_ok=True)
    previous = {}
    for folder in sorted(ART.glob("pilot_*")):
        mf = folder/"manifest.json"
        if folder != OUT and mf.exists():
            for name, digest in json.loads(mf.read_text(encoding="utf-8")).items():
                assert sha(folder/name) == digest, (folder.name, name)
            previous[folder.name] = sha(mf)
    conf = ART/"confirmation_19a"/"manifest.json"
    for name, digest in json.loads(conf.read_text(encoding="utf-8")).items():
        assert sha(conf.parent/name) == digest, name
    start = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=previous,
                 sources={n: sha(ROOT/"experiments"/n) for n in MODULES})
    (OUT/"execution_start.json").write_text(json.dumps(start, indent=2), encoding="utf-8")
    pairs, channels = run()
    pairs.to_csv(OUT/"pairs.csv", index=False)
    channels.to_csv(OUT/"channels.csv", index=False)
    summary = pairs.groupby(["subset", "repeat"])[["spearman", "same_direction", "jaccard_active", "top3_overlap"]].median().reset_index()
    summary.to_csv(OUT/"summary.csv", index=False)
    (OUT/"metadata.json").write_text(json.dumps(start | dict(finished_utc=datetime.now(timezone.utc).isoformat(),
                                    pairs=len(pairs), previous_manifests_intact=True), indent=2), encoding="utf-8")
    (OUT/"manifest.json").write_text(json.dumps({p.name: sha(p) for p in sorted(OUT.iterdir())
                                                 if p.is_file() and p.name != "manifest.json"}, indent=2), encoding="utf-8")
    print(summary.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
