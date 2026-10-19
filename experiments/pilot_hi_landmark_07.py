"""P07: retrospective landmarks from immutable P05/P06 predictions; no fitting."""

import hashlib
import importlib.metadata
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "experiments/artifacts/pilot_hi_landmark_07"
LEVELS = (.4, .5, .6)
OFFSETS = (-10, -5, 0, 5, 10, 20)
KEYS = ["domain", "dataset", "family", "alpha"]
FAMILIES = ("MARGEM", "EMPIRICO", "AAKR")
SOURCES = ("pilot_fd001_05", "pilot_fd003_06")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_integrity():
    records = {}
    for folder in sorted((ROOT / "experiments/artifacts").glob("pilot_fd00*")):
        manifest = folder / "manifest.json"
        if not manifest.exists():
            continue
        entries = json.loads(manifest.read_text(encoding="utf-8"))
        for name, digest in entries.items():
            assert sha(folder / name) == digest, (folder.name, name)
        records[folder.name] = {"manifest_sha256": sha(manifest), "files": len(entries)}
    return records


def read_predictions():
    frames = []
    for source in SOURCES:
        frame = pd.read_csv(ROOT / "experiments/artifacts" / source / "predictions.csv")
        frame["domain"] = "FD001" if source == SOURCES[0] else "FD003_refit"
        transfer = frame.dataset.str.startswith("transfer")
        frame.loc[transfer, "domain"] = "FD003_transfer"
        frame["dataset"] = frame.dataset.replace({"cv": "complete", "official": "truncated",
                                                  "transfer_complete": "complete",
                                                  "transfer_official": "truncated"})
        frames.append(frame)
    data = pd.concat(frames, ignore_index=True)
    assert not data.duplicated(["domain", "dataset", "family", "unit", "cycle"]).any()
    assert (data.cycle >= 20).all()
    np.testing.assert_allclose(data.end-data.cycle, data.actual_rul, atol=1e-10)
    assert np.isfinite(data[["hi", "predicted_rul", "actual_rul", "end"]]).all().all()
    return data


def extract_landmarks(data, levels=LEVELS):
    rows, histories, snapshots = [], [], []
    for group_key, raw in data.groupby(["domain", "dataset", "family", "unit"], sort=True):
        g = raw.sort_values("cycle").reset_index(drop=True)
        base = dict(zip(["domain", "dataset", "family", "unit"], group_key))
        assert g.end.nunique() == 1 and (np.diff(g.cycle) == 1).all()
        for alpha in levels:
            hits = g.loc[g.hi <= alpha]
            record = {**base, "alpha": alpha, "end": g.end.iloc[0],
                      "last_observed": g.cycle.iloc[-1], "crossed": not hits.empty}
            if hits.empty:
                record["status"] = "not_reached_complete" if base["dataset"] == "complete" else "not_reached_before_truncation"
                rows.append(record)
                continue
            first = hits.iloc[0]
            t = int(first.cycle)
            error = float(t+first.predicted_rul-first.end)
            after = g.loc[g.cycle >= t].copy()
            above = after.hi.gt(alpha).to_numpy()
            record.update(status="observed", crossing_cycle=t, crossing_hi=first.hi,
                          actual_lead=first.actual_rul, predicted_lead=first.predicted_rul,
                          predicted_f=t+first.predicted_rul, error=error,
                          recovery=bool(above.any()),
                          recovery_episodes=int(np.sum(above[1:] & ~above[:-1])),
                          downward_recrossings=int(np.sum(~above[1:] & above[:-1])))
            rows.append(record)
            after["offset"] = after.cycle-t
            after["error"] = after.cycle+after.predicted_rul-after.end
            after["initial_error"] = error
            after["alpha"] = alpha
            histories.append(after)
            indexed = g.set_index("cycle")
            for offset in OFFSETS:
                if t+offset not in indexed.index:
                    continue
                point = indexed.loc[t+offset]
                snapshots.append({**base, "alpha": alpha, "offset": offset,
                                  "cycle": t+offset, "actual_lead": point.actual_rul,
                                  "error": t+offset+point.predicted_rul-point.end,
                                  "initial_error": error})
    return pd.DataFrame(rows), pd.concat(histories, ignore_index=True), pd.DataFrame(snapshots)


def error_stats(values):
    a = np.asarray(values, dtype=float)
    if not len(a):
        return dict(rmse=np.nan, mae=np.nan, bias=np.nan, late_fraction=np.nan)
    return dict(rmse=float(np.sqrt(np.mean(a*a))), mae=float(np.mean(np.abs(a))),
                bias=float(np.mean(a)), late_fraction=float(np.mean(a > 0)))


def landmark_summary(marks):
    rows = []
    for key, g in marks.groupby(KEYS, sort=True):
        hits = g.loc[g.crossed]
        record = dict(zip(KEYS, key))
        record.update(total=len(g), crossed=len(hits), missing=len(g)-len(hits),
                      coverage=len(hits)/len(g), **error_stats(hits.error))
        for col in ["crossing_cycle", "actual_lead", "predicted_lead", "crossing_hi"]:
            for q, label in [(.25, "q25"), (.5, "median"), (.75, "q75")]:
                record[f"{col}_{label}"] = hits[col].quantile(q) if len(hits) else np.nan
        record["recovered_engines"] = int(hits.recovery.sum()) if len(hits) else 0
        rows.append(record)
    return pd.DataFrame(rows)


def offset_summary(marks, snapshots):
    rows = []
    for key, g in marks.groupby(KEYS, sort=True):
        for offset in OFFSETS:
            mask = np.ones(len(snapshots), dtype=bool)
            for name, value in zip(KEYS, key):
                mask &= snapshots[name].eq(value)
            s = snapshots.loc[mask & snapshots.offset.eq(offset)]
            row = {**dict(zip(KEYS, key)), "offset": offset, "available": len(s),
                   "crossed": int(g.crossed.sum()), **error_stats(s.error)}
            row["initial_rmse_same_engines"] = error_stats(s.initial_error)["rmse"]
            row["delta_rmse_from_initial"] = row["rmse"]-row["initial_rmse_same_engines"]
            rows.append(row)
    return pd.DataFrame(rows)


def paired_record(a, b, label, alpha, dataset, mode, predictions, rng):
    pair = a.loc[a.crossed].merge(b.loc[b.crossed], on="unit", suffixes=("_a", "_b"))
    row = dict(comparison=label, dataset=dataset, alpha=alpha, timing=mode,
               common=len(pair), crossed_a=int(a.crossed.sum()), crossed_b=int(b.crossed.sum()))
    if pair.empty:
        return row
    if mode == "own_landmarks":
        ea, eb = pair.error_a.to_numpy(), pair.error_b.to_numpy()
    else:
        errors = []
        lookup = predictions.set_index(["domain", "dataset", "family", "unit", "cycle"])
        for r in pair.itertuples():
            cycle = int(max(r.crossing_cycle_a, r.crossing_cycle_b))
            values = []
            for suffix in ["a", "b"]:
                p = lookup.loc[(getattr(r, f"domain_{suffix}"), dataset,
                                getattr(r, f"family_{suffix}"), r.unit, cycle)]
                values.append(cycle+p.predicted_rul-p.end)
            errors.append(values)
        ea, eb = np.asarray(errors).T
    row.update(rmse_a=error_stats(ea)["rmse"], rmse_b=error_stats(eb)["rmse"])
    row["delta_rmse_b_minus_a"] = row["rmse_b"]-row["rmse_a"]
    idx = rng.integers(0, len(ea), size=(2000, len(ea)))
    delta = np.sqrt(np.mean(eb[idx]**2, axis=1))-np.sqrt(np.mean(ea[idx]**2, axis=1))
    row["ci_low"], row["ci_high"] = np.quantile(delta, [.025, .975])
    return row


def paired_comparisons(marks, data):
    rng = np.random.default_rng(20261016)
    rows = []
    for dataset in ["complete", "truncated"]:
        for alpha in LEVELS:
            g = marks.loc[marks.dataset.eq(dataset) & marks.alpha.eq(alpha)]
            comparisons = []
            for domain in sorted(g.domain.unique()):
                for fa, fb in itertools.combinations(FAMILIES, 2):
                    comparisons.append((g.loc[g.domain.eq(domain) & g.family.eq(fa)],
                                        g.loc[g.domain.eq(domain) & g.family.eq(fb)],
                                        f"{domain}:{fa}->{fb}"))
            for family in FAMILIES:
                comparisons.append((g.loc[g.domain.eq("FD003_transfer") & g.family.eq(family)],
                                    g.loc[g.domain.eq("FD003_refit") & g.family.eq(family)],
                                    f"FD003_transfer->refit:{family}"))
            for a, b, label in comparisons:
                for mode in ["own_landmarks", "common_cycle"]:
                    rows.append(paired_record(a, b, label, alpha, dataset, mode, data, rng))
    return pd.DataFrame(rows)


def markdown_table(frame):
    columns = list(frame.columns)
    lines = ["| " + " | ".join(columns) + " |", "|" + "---|"*len(columns)]
    for row in frame.itertuples(index=False, name=None):
        vals = [f"{v:.2f}" if isinstance(v, (float, np.floating)) else str(v) for v in row]
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def write_report(summary, offsets, pairs):
    cols = ["domain", "dataset", "family", "crossed", "missing", "actual_lead_median",
            "predicted_lead_median", "rmse", "mae", "bias", "recovered_engines"]
    sections = ["# P07 — previsão do F original a partir de HI=0,5",
                "Análise exploratória retrospectiva das predições congeladas de P05/P06, sem novo treino. "
                "HI=0,5 não redefine F, P, remoção ou início de inspeções. Unidades: ciclos. "
                "Completo = avaliação externa por motor; truncado = teste oficial já examinado. "
                "Não se comparam linhas com coberturas diferentes como se fossem a mesma população.",
                "## Marco principal", markdown_table(summary.loc[summary.alpha.eq(.5), cols]),
                "RMSE, MAE e viés são condicionais ao cruzamento. Viés positivo prevê F tarde; "
                "é erro de previsão, não uma decisão de remoção. A antecedência real é retrospectiva. "
                "Ausências completas e ausências até truncamento estão discriminadas em landmarks.csv.",
                "## Sensibilidade (sem seleção do melhor limiar)",
                markdown_table(summary[["domain", "dataset", "family", "alpha", "crossed", "actual_lead_median", "rmse", "bias"]]),
                "## Comparações nos mesmos motores e no mesmo ciclo", 
                "A = primeira família/domínio do rótulo; B = segunda. Diferenças B−A. "
                "Ciclo comum = máximo dos dois primeiros cruzamentos. Intervalos de bootstrap pareado "
                "com 2.000 reamostragens são descritivos e não corrigem reutilização dos dados.",
                markdown_table(pairs.loc[pairs.alpha.eq(.5) & pairs.timing.eq("common_cycle"),
                                        ["comparison", "dataset", "common", "rmse_a", "rmse_b", "delta_rmse_b_minus_a", "ci_low", "ci_high"]]),
                "## Atualização após cinco ciclos", 
                markdown_table(offsets.loc[offsets.alpha.eq(.5) & offsets.offset.eq(5),
                                          ["domain", "dataset", "family", "available", "crossed", "initial_rmse_same_engines", "rmse", "delta_rmse_from_initial"]]),
                "O comparador conserva F previsto no marco. Os CSVs incluem todos os ciclos subsequentes "
                "e deslocamentos −10/−5/0/+5/+10/+20, com coberturas próprias. Comparações anteriores ao "
                "marco são retrospectivas; não permitem antecipar causalmente seu instante. Recuperações "
                "são retornos de HI acima do limiar depois da primeira passagem.",
                "## Limites de interpretação", 
                "O conversor usa HI corrente. A concentração das previsões no limiar deve ser examinada "
                "junto da dispersão das vidas reais: cruzar o mesmo nível não demonstra prognóstico "
                "individualizado. As famílias podem cruzar em instantes diferentes; por isso estão "
                "arquivadas comparações em ciclos comuns e em marcos próprios. Não há tolerância "
                "operacional validada, adoção definitiva do HI, inspeção simulada ou protocolo principal "
                "congelado. Modelos FD001 transferidos foram ajustados nas trajetórias completas FD001, "
                "mas não nas trajetórias FD003 avaliadas nesse braço. Os domínios não são motores pareados."]
    (OUT / "relatorio.md").write_text("\n\n".join(sections)+"\n", encoding="utf-8")


def plot_summary(summary):
    fig, axes = plt.subplots(2, 3, figsize=(14, 8), layout="constrained")
    colors = {"MARGEM": "#7570b3", "EMPIRICO": "#1b9e77", "AAKR": "#d95f02"}
    for col, domain in enumerate(["FD001", "FD003_refit", "FD003_transfer"]):
        for row, dataset in enumerate(["complete", "truncated"]):
            ax = axes[row, col]
            g = summary.loc[summary.domain.eq(domain) & summary.dataset.eq(dataset) & summary.alpha.eq(.5)]
            for r in g.itertuples():
                ax.scatter(r.actual_lead_median, r.rmse, s=25+2*r.crossed, color=colors[r.family], label=r.family)
                delta = (5, -14) if r.family == "AAKR" else (5, 5)
                ax.annotate(f"{r.crossed}/100", (r.actual_lead_median, r.rmse), xytext=delta, textcoords="offset points", fontsize=8)
            ax.set_title(f"{domain} / {dataset}")
            ax.set_xlabel("Median true remaining cycles at first HI ≤ 0.5")
            ax.set_ylabel("Endpoint prediction RMSE (cycles)")
            ax.grid(alpha=.2)
            ax.margins(.35)
            ax.legend(fontsize=7, loc="upper left")
    fig.suptitle("P07: conditional error and lead; coverage differs between methods")
    fig.savefig(OUT / "landmark_error_lead.png", dpi=160)
    plt.close(fig)


def main():
    before = source_integrity()
    data = read_predictions()
    marks, histories, snapshots = extract_landmarks(data)
    summary = landmark_summary(marks)
    offsets = offset_summary(marks, snapshots)
    pairs = paired_comparisons(marks, data)
    OUT.mkdir(parents=True, exist_ok=True)
    for name, frame in [("landmarks", marks), ("forecast_updates", histories),
                        ("offset_predictions", snapshots), ("summary", summary),
                        ("offset_summary", offsets), ("paired_comparisons", pairs)]:
        frame.to_csv(OUT / f"{name}.csv", index=False)
    write_report(summary, offsets, pairs)
    plot_summary(summary)
    assert before == source_integrity()
    metadata = {"created_utc": datetime.now(timezone.utc).isoformat(), "training": False,
                "seed": 20261016, "bootstrap": 2000, "levels": LEVELS, "offsets": OFFSETS,
                "source_integrity": before, "python_packages": {p: importlib.metadata.version(p) for p in ["numpy", "pandas", "matplotlib"]},
                "inputs": {str(path.relative_to(ROOT)): sha(path) for path in
                           [ROOT / "experiments/protocolo_marco_hi_50.md", Path(__file__),
                            ROOT / "experiments/test_pilot_hi_landmark_07.py"]+
                           [ROOT / "experiments/artifacts" / source / "predictions.csv" for source in SOURCES]}}
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    manifest = {p.name: sha(p) for p in sorted(OUT.iterdir()) if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(summary.loc[summary.alpha.eq(.5), ["domain", "dataset", "family", "crossed", "actual_lead_median", "rmse", "bias"]].to_string(index=False))


if __name__ == "__main__":
    main()
