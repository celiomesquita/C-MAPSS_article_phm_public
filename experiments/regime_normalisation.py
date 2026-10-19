"""Operating-regime normalisation (P18.1): regime from operating settings only, per-regime healthy baseline per sensor."""
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

SENSORS = [f"s{i}" for i in range(1, 22)]
OPS = ["op1", "op2", "op3"]
HEALTHY_CYCLES = 20
K_DEFAULT = 6
SEED = 20261018


class RegimeNormaliser:
    def __init__(self, k=K_DEFAULT, seed=SEED, labels=None):
        self.k, self.seed, self.oracle_labels = k, seed, labels

    def fit(self, data):
        """Fit on fitting engines only; `data` has unit, cycle, op1..op3 and sensors."""
        ops = data[OPS].to_numpy(float)
        self.op_mean, self.op_std = ops.mean(axis=0), ops.std(axis=0, ddof=0)
        self.op_std = np.where(self.op_std < 1e-12, 1.0, self.op_std)
        if self.oracle_labels is None:
            self.km = KMeans(n_clusters=self.k, n_init=20, random_state=self.seed).fit((ops - self.op_mean) / self.op_std)
        regimes = self.assign(data)
        healthy = data.cycle.to_numpy() <= HEALTHY_CYCLES
        self.mean = np.zeros((self.k, len(SENSORS)))
        self.std = np.ones((self.k, len(SENSORS)))
        values = data[SENSORS].to_numpy(float)
        for c in range(self.k):
            rows = healthy & (regimes == c)
            if rows.sum() > 1:
                self.mean[c] = values[rows].mean(axis=0)
                s = values[rows].std(axis=0, ddof=1)
                self.std[c] = np.where(s < 1e-9, 1.0, s)
        return self

    def assign(self, data):
        if self.oracle_labels is not None:
            return self.oracle_labels.loc[data.index].to_numpy(int)
        return self.km.predict((data[OPS].to_numpy(float) - self.op_mean) / self.op_std)

    def transform(self, data):
        out = data.copy()
        regimes = self.assign(data)
        out[SENSORS] = (data[SENSORS].to_numpy(float) - self.mean[regimes]) / self.std[regimes]
        out["regime"] = regimes
        return out
