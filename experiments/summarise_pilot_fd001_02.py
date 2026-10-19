"""Verify P02 information boundaries and summarise saved results without retraining."""

import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pilot_fd001_02 import OUT, ROOT, VARIANTS, margins


def run():
    meta = json.loads((OUT / "metadata.json").read_text())
    assert hashlib.sha256((ROOT / "CMAPSSData/train_FD001.txt").read_bytes()).hexdigest() == meta["data_sha256"]
    for relative, digest in meta["scripts"].items():
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == digest
    splits = json.loads((OUT / "splits.json").read_text())
    pred = pd.read_csv(OUT / "predictions.csv")
    decisions = pd.read_csv(OUT / "decisions_per_engine.csv")
    calibration = pd.read_csv(OUT / "margins.csv")
    choices = pd.read_csv(OUT / "policy_selection.csv")
    detectors = pd.read_csv(OUT / "detector_selection.csv")
    detection = pd.read_csv(OUT / "detections.csv")
    assert len(detection) == detection.unit.nunique() == 100
    assert not pred.duplicated(["fold", "model", "role", "unit", "cycle"]).any()
    assert (pred.rul == pred.end - pred.cycle).all()
    assert not decisions.duplicated(["fold", "model", "variant", "unit"]).any()
    for split in splits:
        fold = split["fold"]
        groups = [set(split[r]) for r in ["fit", "calibration", "selection", "evaluation"]]
        assert [len(g) for g in groups] == [40, 20, 20, 20]
        assert len(set.union(*groups)) == 100
        for role in ["calibration", "selection", "evaluation"]:
            assert set(pred.loc[(pred.fold == fold) & (pred.role == role), "unit"]) <= set(split[role])
        g = detectors.loc[detectors.fold == fold]
        feasible = g.loc[g.early_count <= 2]
        eligible = feasible if len(feasible) else g
        sort = (["coverage", "median_lead", "threshold"] if len(feasible)
                else ["early_count", "coverage", "median_lead", "threshold"])
        ascending = [False, False, True] if len(feasible) else [True, False, False, True]
        expected = eligible.sort_values(sort, ascending=ascending, kind="stable").iloc[0].candidate
        assert g.loc[g.chosen, "candidate"].tolist() == [expected]
        for model in pred.model.unique():
            block = choices.loc[(choices.fold == fold) & (choices.model == model)].copy()
            block["order"] = block.variant.map({v: i for i, v in enumerate(VARIANTS)})
            expected = block.sort_values(["endpoint_count", "mean_unused", "order"]).iloc[0].variant
            assert block.loc[block.chosen, "variant"].tolist() == [expected]
            assert len(decisions.loc[(decisions.fold == fold) & (decisions.model == model) & decisions.chosen]) == 20
            cal = pred.loc[(pred.fold == fold) & (pred.model == model) & (pred.role == "calibration")]
            calculated = margins(cal)
            saved = calibration.loc[(calibration.fold == fold) & (calibration.model == model)].iloc[0]
            for name in ["global_margin", "local_margin"]:
                if calculated[name] is not None:
                    assert np.isclose(calculated[name], saved[name])
    chosen = pd.read_csv(OUT / "selected_policy_summary.csv")
    assert (chosen.engines == 100).all()
    summary = pd.read_csv(OUT / "decision_summary.csv")
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))
    model_names = sorted(summary.model.unique())
    positions = np.arange(len(model_names))
    for i, variant in enumerate(VARIANTS):
        g = summary.loc[summary.variant == variant].set_index("model").reindex(model_names)
        bars = axes[0].bar(positions + (i - 1.5)*.19, g.mean_unused, width=.19,
                           label=variant.replace("_gate30", " gated"))
        axes[0].bar_label(bars, labels=[str(int(n)) for n in g.endpoints], fontsize=7, padding=2)
    axes[0].set_xticks(positions, model_names)
    axes[0].set(ylabel="Mean unused life (cycles)", ylim=(0, 116),
                title="Numbers above bars: endpoint events /100")
    axes[0].legend(fontsize=7, ncols=2, loc="upper left")
    global_mean = calibration.groupby("model").global_margin.mean()
    local_mean = calibration.groupby("model").local_margin.mean()
    idx = np.arange(len(global_mean))
    axes[1].bar(idx - .18, global_mean, width=.36, label="Global")
    axes[1].bar(idx + .18, local_mean, width=.36, label="Predicted RUL <=30")
    axes[1].set_xticks(idx, global_mean.index)
    axes[1].set(ylabel="Mean margin across folds (cycles)", title="Calibration on different prediction regions")
    axes[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "policy_tradeoff.png", dpi=180)
    plt.close(fig)
    ds = pd.read_csv(OUT / "detector_summary.csv").set_index("detector")
    metric = pd.read_csv(OUT / "metrics_per_engine.csv").groupby("model").agg(
        engines=("unit", "nunique"), mean_engine_rmse=("rmse", "mean"))
    metric.to_csv(OUT / "prediction_summary.csv")
    text = ("\n## Leitura dos resultados e próxima decisão\n\n"
            f"Com limiar fixo, {int(ds.loc['p_fixed2', 'alerts_by_40'])}/100 alertas ocorreram até o ciclo 40; "
            f"com selecção interna do detector, {int(ds.loc['p', 'alerts_by_40'])}/100. "
            f"As medianas de P foram {ds.loc['p_fixed2', 'median_P']:.1f} e {ds.loc['p', 'median_P']:.1f}. "
            "A mudança de referência altera o ciclo de alerta, mas não valida o início físico de degradação. "
            "A hipótese de estabilidade até 40 deverá ser confrontada em sensibilidade antes de fixar P.\n\n"
            f"A margem global média por modelo ficou entre {global_mean.min():.2f} e {global_mean.max():.2f} ciclos; "
            f"a local, entre {local_mean.min():.2f} e {local_mean.max():.2f}. "
            "Comparar global com global_gate30 isola a região de acção; comparar global_gate30 com local_gate30 "
            "isola a calibração da margem nessa região. Resultados externos de todas as variantes foram preservados, "
            "incluindo variantes não escolhidas internamente.\n\n"
            "Antes de congelar: resolver referência de HI/F e identificação operacional de P, verificar robustez "
            "da hipótese inicial e dos parâmetros 10/30, definir admissibilidade e antecedência, avaliar explicações "
            "e especificar o futuro braço de inspeção. A rodada não introduz inspeções nem congela o protocolo.\n\n"
            "![Contrastes de política e margens](policy_tradeoff.png)\n\n"
            "Verificações: separação de motores; predições sem duplicação; escolhas reproduzidas somente "
            "dos resultados internos; margens recalculadas das predições de calibração; hashes dos dados, "
            "código importado, código da rodada e protocolo intactos.\n")
    report = OUT / "relatorio.md"
    existing = report.read_text(encoding="utf-8").split("\n## Leitura dos resultados e próxima decisão")[0]
    report.write_text(existing + text, encoding="utf-8")
    verification = {"checks_passed": True, "evaluation_engines": 100,
                    "summary_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT / "verification.json").write_text(json.dumps(verification, indent=2), encoding="utf-8")
    manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir())
                if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(ds.to_string())
    print(calibration.groupby("model")[["global_margin", "local_margin", "local_engines"]].mean().to_string())
    print(metric.to_string())
    print(chosen.to_string(index=False))
    print("P02 artifact checks passed.")


if __name__ == "__main__":
    run()
