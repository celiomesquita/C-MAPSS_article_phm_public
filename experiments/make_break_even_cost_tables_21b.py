"""LaTeX table for P21.2 from the P21.2 contrast_summary.csv (no hand transcription)."""

from pathlib import Path

import pandas as pd

import make_break_even_tables_21a as t

OUT = Path(__file__).resolve().parent / "artifacts/pilot_break_even_cost_21b"
S = pd.read_csv(OUT / "contrast_summary.csv", keep_default_na=False, na_values=[""])
LABELS = {"C3": r"Inspection on ISO point", "C4": r"Inspection on RF-slope point", "C5": r"Inspection on ISO lower-98\%",
          "C8": r"ISO point + inspection vs lower-98\%"}


def table():
    lines = []
    for cid, label in LABELS.items():
        for q in (0.005, 0.01, 0.02):
            cells = []
            for sub in t.SUBSETS:
                g = S[(S.contrast == cid) & (S.subset == sub) & (S.delay == 1) & (S.u == 0) & (S.scenario == "S2_W60_g1")
                      & (S.q_inspection == q)]
                assert len(g) == 1
                cells.append(t.cell(g))
            lines.append(f"{label if q == 0.005 else ''} & {q:g} & " + " & ".join(cells) + r" \\")
        lines.append(r"\addlinespace")
    return "\n".join(lines[:-1])


if __name__ == "__main__":
    (OUT / "table_cost.tex").write_text(table(), encoding="utf-8")
    print(table())
