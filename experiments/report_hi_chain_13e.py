"""P13.5 figure: between-repeat marker ranges and conservative-rule life change, from saved outputs only."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "experiments/artifacts/pilot_hi_chain_13e"


def main():
    ranges = pd.read_csv(OUT / "ranges.csv").query("quantity == 'usable_marker'")
    decisions = pd.read_csv(OUT / "decisions.csv").query("policy_id == 'ISO_LOWER98_M15_D1'")
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    for j, subset in enumerate(["FD001", "FD003"]):
        ax = axes[0, j]
        for chain, style in [("M18", "-"), ("SEL", "--")]:
            r = ranges.loc[ranges.subset.eq(subset) & ranges.chain.eq(chain)]
            v = np.sort(r.range.dropna().to_numpy())
            label = f"{chain} (indefinidos: {int(r.range.isna().sum())})"
            ax.step(np.r_[0, v], np.r_[0, np.arange(1, len(v)+1)/len(r)], style, where="post", label=label)
        ax.set_xscale("symlog", linthresh=10)
        ax.set_title(f"{subset}: amplitude do marco entre repetições")
        ax.set_xlabel("ciclos (escala simlog)")
        ax.set_ylabel("fração de motores")
        ax.legend(fontsize=8)
        ax = axes[1, j]
        w = decisions.loc[decisions.subset.eq(subset)].pivot_table(index=["repeat", "unit"], columns="chain", values="utilised")
        delta = (w.SEL-w.M18).reset_index(name="delta")
        events = decisions.loc[decisions.subset.eq(subset) & decisions.chain.eq("SEL") & decisions.reached_endpoint]
        for repeat in [1, 2, 3]:
            x = delta.loc[delta.repeat.eq(repeat), "delta"].to_numpy()
            ax.scatter(np.full(len(x), repeat)+np.random.default_rng(repeat).uniform(-.2, .2, len(x)), x, s=8, alpha=.5)
        for e in events.itertuples():
            ax.annotate(f"motor {e.unit}: {e.status}", (e.repeat, float(delta.loc[delta.repeat.eq(e.repeat) & delta.unit.eq(e.unit), "delta"].iloc[0])),
                        fontsize=7, color="crimson")
        ax.axhline(0, color="k", lw=.6)
        ax.set_xticks([1, 2, 3])
        ax.set_xlabel("repetição")
        ax.set_ylabel("vida aproveitada SEL−M18, ciclos")
        ax.set_title(f"{subset}: ISO inferior 98%, reserva 15, prazo 1")
    fig.tight_layout()
    fig.savefig(OUT / "chain_comparison.png", dpi=150)


if __name__ == "__main__":
    main()
