"""Render a mathematical policy legend from archived P02 results."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

root = Path(__file__).resolve().parents[1]
source = root / "experiments/artifacts/pilot_fd001_02"
destination = root / "LaTeX/manuscript/figures/pilot_policy_math.pdf"
destination.parent.mkdir(parents=True, exist_ok=True)
summary = pd.read_csv(source / "decision_summary.csv")
margins = pd.read_csv(source / "margins.csv").groupby("model")[["global_margin", "local_margin"]].mean()
names = sorted(summary.model.unique())
variants = ["raw", "global", "global_gate30", "local_gate30"]
labels = [r"$\pi_0$", r"$\pi_G$", r"$\pi_{G,b}$", r"$\pi_{L,b}$"]
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
x = np.arange(len(names))
for i, (variant, label) in enumerate(zip(variants, labels)):
    rows = summary.loc[summary.variant == variant].set_index("model").reindex(names)
    bars = axes[0].bar(x + (i-1.5)*.19, rows.mean_unused, width=.19, label=label)
    axes[0].bar_label(bars, labels=[str(int(v)) for v in rows.endpoints], padding=2, fontsize=8)
axes[0].set_xticks(x, names)
axes[0].set(ylabel=r"$\overline{U}^{\pi}$ (cycles)", ylim=(0, 116),
            title=r"$\sum_i E_i^{\pi}$ above each bar")
axes[0].legend(ncols=4, loc="upper left", fontsize=10)
axes[1].bar(x-.18, margins.loc[names, "global_margin"], width=.36, label=r"$\Delta_G$")
axes[1].bar(x+.18, margins.loc[names, "local_margin"], width=.36, label=r"$\Delta_L$")
axes[1].set_xticks(x, names)
axes[1].set(ylabel="Mean margin (cycles)", title=r"$\widehat r_i(t)\leq b,\quad b=30$")
axes[1].legend(fontsize=10)
fig.tight_layout()
fig.savefig(destination)
plt.close(fig)
