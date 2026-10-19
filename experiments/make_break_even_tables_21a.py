"""LaTeX tables for P21.1 generated from contrast_summary.csv (no hand transcription)."""

from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parent / "artifacts/pilot_break_even_21a"
S = pd.read_csv(OUT / "contrast_summary.csv", keep_default_na=False, na_values=[""])
SUBSETS = ["FD001", "FD002", "FD003", "FD004"]
MAIN = [("C1", r"Lower-98\% vs point (ISO)"), ("C3", r"Inspection on point (ISO)"), ("C5", r"Inspection on lower-98\% (ISO)"),
        ("C6", r"HI marker vs lower-98\% (ISO)"), ("C7", r"Lower-98\% (ISO) vs age 127"),
        ("C8", r"Point + inspection vs lower-98\%")]
SHORT = {"A_dominates": "A dom.", "B_dominates": "B dom.", "tie": "tie"}
SCEN = [("S2_W30_g1", r"$W=30$"), ("S2_W60_g1", r"$W=60$ (main)"), ("S2_W80_g1", r"$W=80$"), ("S2_W60_g2", r"$\gamma=2$"),
        ("S2_W60_g0.26", r"$\gamma=0.26$"), ("S2_W60_g1_pP0.02", r"$p_P=0.02$"), ("S1_W60_g1", r"S1 entry, $W=60$"),
        ("L1_window_s0.25", r"latent window $\sigma=0.25$"), ("L2_window_s0.5", r"latent window $\sigma=0.5$")]
DAGGER = r"$^\dagger$"


def fmt(x):
    return f"{x:.0f}" if x >= 100 else f"{x:.1f}" if x >= 10 else f"{x:.2f}"


def cell(g):
    cls = set(g.classes.iloc[0].split(";"))
    rng = f"{fmt(g.beta0_min.iloc[0])}--{fmt(g.beta0_max.iloc[0])}"
    flag = "" if g.beta0_bounded_repeats.iloc[0] == g.repeats.iloc[0] else DAGGER
    above, below = "A_preferred_above_beta0" in cls, "A_preferred_below_beta0" in cls
    rest = [SHORT[c] for c in ("A_dominates", "B_dominates", "tie") if c in cls]
    text = ""
    if above or below:
        text = (r"$<$" if below and not above else "") + rng + flag
    if rest:
        text = (text + " or " if text else "") + "/".join(rest)
    return text


def lookup(cid, sub, delay, scen):
    g = S[(S.contrast == cid) & (S.subset == sub) & (S.delay == delay) & (S.u == 0)]
    g = g[g.scenario.isna() | (g.scenario == scen)] if scen is None else g[g.scenario == scen]
    assert len(g) == 1, (cid, sub, delay, scen, len(g))
    return g


def main_table():
    lines = []
    for cid, label in MAIN:
        for d in (1, 2):
            scen = None if cid in ("C1", "C6", "C7") else "S2_W60_g1"
            cells = [cell(lookup(cid, sub, d, scen)) for sub in SUBSETS]
            lines.append(f"{label if d == 1 else ''} & {d} & " + " & ".join(cells) + r" \\")
        lines.append(r"\addlinespace")
    return "\n".join(lines[:-1])


def sensitivity_table(cid):
    return "\n".join(f"{label} & " + " & ".join(cell(lookup(cid, sub, 1, scen)) for sub in SUBSETS) + r" \\"
                     for scen, label in SCEN)


if __name__ == "__main__":
    (OUT / "table_main.tex").write_text(main_table(), encoding="utf-8")
    (OUT / "table_sens_C3.tex").write_text(sensitivity_table("C3"), encoding="utf-8")
    (OUT / "table_sens_C5.tex").write_text(sensitivity_table("C5"), encoding="utf-8")
    print(main_table())
