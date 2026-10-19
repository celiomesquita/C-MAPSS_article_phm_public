"""Independent verifier for P19.2: re-reads the stored models and redoes every pair metric with scalar loops."""
import hashlib
import json
import math
from pathlib import Path

import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT/"experiments/artifacts"
OUT = ART/"pilot_coefficient_stability_19b"
SRC = {"FD001": ART/"pilot_f_uncertainty_10", "FD003": ART/"pilot_f_uncertainty_10",
       "FD002": ART/"confirmation_19a", "FD004": ART/"confirmation_19a"}


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ranks(v):
    order = sorted(range(len(v)), key=lambda i: v[i])
    r = [0.]*len(v)
    i = 0
    while i < len(order):
        j = i
        while j+1 < len(order) and v[order[j+1]] == v[order[i]]:
            j += 1
        for k in range(i, j+1):
            r[order[k]] = (i+j)/2.+1.
        i = j+1
    return r


def pearson(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    sx = math.sqrt(sum((a-mx)**2 for a in x))
    sy = math.sqrt(sum((b-my)**2 for b in y))
    return float("nan") if sx == 0 or sy == 0 else sum((a-mx)*(b-my) for a, b in zip(x, y))/(sx*sy)


def main():
    for name, digest in json.loads((OUT/"manifest.json").read_text(encoding="utf-8")).items():
        assert sha(OUT/name) == digest, name
    pairs = pd.read_csv(OUT/"pairs.csv")
    n = 0
    for subset, folder in SRC.items():
        for repeat in (1, 2, 3):
            recs = []
            for f in range(1, 11):
                b = joblib.load(folder/f"models_{subset}_r{repeat}_f{f}.joblib")
                recs.append({c: (float(d), float(w)) for c, d, w in
                             zip(b["health"]["stats"]["channels"], b["health"]["stats"]["direction"], b["health"]["beta"])})
            for i in range(10):
                for j in range(i+1, 10):
                    a, b = recs[i], recs[j]
                    common = sorted(set(a) & set(b), key=lambda c: int(c[1:]))
                    row = pairs[(pairs.subset == subset) & (pairs.repeat == repeat) & (pairs.fold_a == i+1) & (pairs.fold_b == j+1)]
                    assert len(row) == 1
                    row = row.iloc[0]
                    assert row.common == len(common)
                    wa, wb = [a[c][1] for c in common], [b[c][1] for c in common]
                    rho = pearson(ranks(wa), ranks(wb)) if len(common) > 2 else float("nan")
                    assert (math.isnan(rho) and math.isnan(row.spearman)) or abs(rho-row.spearman) < 1e-9
                    assert abs(sum(a[c][0] == b[c][0] for c in common)/len(common)-row.same_direction) < 1e-12
                    aa = {c for c in a if a[c][1] > 1e-9}
                    bb = {c for c in b if b[c][1] > 1e-9}
                    assert abs(len(aa & bb)/len(aa | bb)-row.jaccard_active) < 1e-12
                    ta = sorted(a, key=lambda c: (-a[c][1], int(c[1:])))[:3]
                    tb = sorted(b, key=lambda c: (-b[c][1], int(c[1:])))[:3]
                    assert abs(len(set(ta) & set(tb))/3.-row.top3_overlap) < 1e-12
                    n += 1
    assert n == len(pairs) == 4*3*45
    print(json.dumps(dict(verified=True, pairs=n), indent=2))


if __name__ == "__main__":
    main()
