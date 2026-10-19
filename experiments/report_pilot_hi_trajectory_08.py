"""Render P08 tables and paired-effect figure from archived outputs."""

import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import pilot_hi_trajectory_08 as p08


def table(frame):
    lines = ["| " + " | ".join(frame.columns) + " |", "|" + "---|"*len(frame.columns)]
    for row in frame.itertuples(index=False, name=None):
        lines.append("| " + " | ".join(f"{x:.2f}" if isinstance(x, (float, np.floating)) else str(x) for x in row) + " |")
    return "\n".join(lines)


def main():
    out = p08.OUT
    summary = pd.read_csv(out / "summary.csv")
    pairs = pd.read_csv(out / "contrasts.csv")
    ranks = pd.read_csv(out / "importance_ranks.csv")
    concordance = pd.read_csv(out / "rank_concordance.csv")
    selection = pd.read_csv(out / "selection.csv")
    methods = ["ISO_FROZEN", "ISO_MATCHED", "Ridge:HI", "Ridge:HI_FULL", "Ridge:SENSOR_RAW", "Ridge:SENSOR_MEAN", "Ridge:SENSOR_FULL",
               "RF:HI", "RF:HI_FULL", "RF:SENSOR_RAW", "RF:SENSOR_MEAN", "RF:SENSOR_FULL"]
    report = ["# P08 — trajetória do HI e atributos diretos dos sensores",
              "Índice de saúde (HI) empírico congelado de P05/P06. Novos preditores de vida útil remanescente "
              "(RUL), cuja soma ao ciclo corrente prevê o F original. Regressão linear com penalização quadrática "
              "(Ridge) e floresta aleatória (RF); comparação da informação dentro de cada família. "
              "Sem alteração da fórmula HI, detecção de P, inspeções ou edição do artigo.",
              "## Desenho e disponibilidade", 
              "Cinco folds por motor em cada subconjunto: HI previamente ajustado em F40, novos prognósticos "
              "ajustados em C20, seleção em S20 e avaliação em E20. No teste oficial, HI congelado a partir "
              "de F60 e prognóstico novamente ajustado somente em C20. São conjuntos já examinados; os resultados "
              "não são confirmação independente. A janela de 20 valores de HI só está disponível a partir "
              "do ciclo 39. Controles usam os mesmos ciclos. O primeiro cruzamento HI≤0,5 é preservado desde "
              "o ciclo 20, mesmo quando seus atributos temporais ainda não estão disponíveis.",
              "Inclinação e curvatura são ajustes polinomiais locais; variabilidade é o desvio padrão amostral. "
              "SENSOR_RAW usa valores correntes com referência individual e escalas congeladas; SENSOR_MEAN "
              "usa médias de 15 ciclos; SENSOR_FULL acrescenta desvio padrão, raiz da média quadrática, "
              "assimetria, inclinação e curvatura. HI_FULL acrescenta inclinação, curvatura e variabilidade "
              "ao HI corrente. ISO_MATCHED é isotônico reajustado em C nos ciclos ≥39; ISO_FROZEN é o conversor "
              "anterior, que também usou ciclos 20–38.",
              "## Primeiro marco HI≤0,5", 
              "Erro = F previsto menos endpoint real, em ciclos. RMSE = raiz do erro quadrático médio; "
              "MAE = erro absoluto médio. Viés positivo prevê F tarde. Métricas condicionais aos motores "
              "disponíveis; a antecipação real é retrospectiva, não informação observada pelo preditor.",
              table(summary.loc[summary.event.eq("landmark") & summary.method.isin(methods),
                                ["subset", "dataset", "method", "total", "available", "no_crossing", "early_window", "rmse", "mae", "bias", "actual_lead_median"]]),
              "## Contrastes principais no marco", 
              "Diferença = RMSE B−A; valores negativos favorecem B. Intervalos descritivos de 95% por 2.000 "
              "reamostragens pareadas de motores, sem garantia confirmatória ou preditiva individual. "
              "Todos os métodos usam a mesma passagem de HI e os mesmos motores/ciclos disponíveis."]
    main_pairs = pairs.loc[pairs.event.eq("landmark") &
                           ((pairs.method_a.str.endswith(":HI") & pairs.method_b.str.endswith(":HI_FULL")) |
                            (pairs.method_a.str.endswith(":SENSOR_RAW") & pairs.method_b.str.endswith(":SENSOR_MEAN")) |
                            (pairs.method_a.str.endswith(":SENSOR_MEAN") & pairs.method_b.str.endswith(":SENSOR_FULL")) |
                            (pairs.method_a.str.endswith(":HI_FULL") & pairs.method_b.str.endswith(":SENSOR_FULL")))]
    cols = ["subset", "dataset", "method_a", "method_b", "common", "rmse_a", "rmse_b", "delta_rmse", "ci_low", "ci_high"]
    report.extend([table(main_pairs[cols]), "![Contrastes pareados de informação](paired_effects.png)",
                   "## Ablações do HI — trajetórias completas",
                   "Omissões e adições são ajustadas novamente, mantendo família, motores e ciclos. "
                   "A penalização Ridge pode mudar pela seleção em S; RF mantém a mesma configuração em todas as representações.",
                   table(pairs.loc[pairs.dataset.eq("complete") & pairs.event.eq("landmark") &
                                   pairs.method_a.str.contains(":HI") & pairs.method_b.str.endswith(":HI_FULL"), cols]),
                   "## Atualizações e teste na última observação",
                   table(summary.loc[summary.event.isin(["plus5", "last"]) & summary.method.isin(methods),
                                     ["subset", "dataset", "event", "method", "total", "available", "rmse", "bias"]]),
                   "## Dependência dos atributos e estabilidade",
                   "Vinte permutações entre motores do mesmo fold ou teste, no marco 0,5. Todos os atributos "
                   "de cada sensor são permutados juntos. Para HI_FULL, os quatro grupos são permutados "
                   "separadamente. A tabela resume variação média de erro quadrático por grupo nos folds "
                   "ou no teste; folds têm a mesma ponderação. Valores negativos são preservados.",
                   table(ranks.groupby(["subset", "dataset", "method", "group"], as_index=False).agg(mean_delta_mse=("delta_mse", "mean"), mean_rank=("rank", "mean"))),
                   "Concordância abaixo é correlação de Spearman de ranks entre famílias no mesmo fold/teste "
                   "e entre folds da mesma família; estatística descritiva sobre poucos grupos e partições dependentes."])
    concordance["comparison"] = np.where(concordance.run_a.eq(concordance.run_b), "between_algorithms", "between_folds")
    report.extend([table(concordance.groupby(["subset", "dataset", "representation", "comparison"], as_index=False).agg(pairs=("spearman", "size"), valid=("spearman", "count"), median_spearman=("spearman", "median"), min_spearman=("spearman", "min"), max_spearman=("spearman", "max"))),
                   "Correlação entre sensores e permutações fora da distribuição limitam inferência causal. "
                   "Concordância de ranks não valida a fidelidade das explicações. Coeficientes Ridge "
                   "padronizados e importâncias por impureza RF estão arquivados como diagnósticos, "
                   "sem substituir permutações e ablações.",
                   "## Seleção e rastreabilidade",
                   table(selection.loc[selection.chosen & selection.run.eq("official"), ["subset", "representation", "algorithm", "alpha", "selection_rmse"]]),
                   "Modelos e escaladores foram congelados antes de anexar os rótulos do respectivo teste "
                   "oficial nesta execução. Protocolo, fontes, versões e hashes constam de metadata.json, "
                   "execution_start.json, freezes.json e manifest.json. Não há intervalo preditivo individual, "
                   "limiar admissível de erro/risco, fórmula HI definitiva ou benefício econômico demonstrado. "
                   "Resultados completos: events.csv, summary.csv, contrasts.csv, history_metrics.csv, "
                   "importance.csv, importance_ranks.csv e rank_concordance.csv."])
    (out / "relatorio.md").write_text("\n\n".join(report)+"\n", encoding="utf-8")
    fig, axes = plt.subplots(2, 2, figsize=(13, 8), layout="constrained")
    labels = ["HI: temporal history", "Sensors: extra statistics", "Sensors versus full HI"]
    for i, subset in enumerate(["FD001", "FD003"]):
        for j, dataset in enumerate(["complete", "truncated"]):
            ax = axes[i, j]
            for k, algorithm in enumerate(["Ridge", "RF"]):
                combinations = [(f"{algorithm}:HI", f"{algorithm}:HI_FULL"),
                                (f"{algorithm}:SENSOR_MEAN", f"{algorithm}:SENSOR_FULL"),
                                (f"{algorithm}:HI_FULL", f"{algorithm}:SENSOR_FULL")]
                for n, (a, b) in enumerate(combinations):
                    r = pairs.loc[pairs.subset.eq(subset) & pairs.dataset.eq(dataset) & pairs.event.eq("landmark") & pairs.method_a.eq(a) & pairs.method_b.eq(b)].iloc[0]
                    y = n+(k-.5)*.2
                    ax.errorbar(r.delta_rmse, y, xerr=[[max(0., r.delta_rmse-r.ci_low)], [max(0., r.ci_high-r.delta_rmse)]],
                                fmt="o", capsize=3, color=["#7570b3", "#1b9e77"][k], label=algorithm if n == 0 else None)
            ax.axvline(0, color="black", linewidth=.8)
            ax.set_yticks(range(3), labels)
            ax.set_title(f"{subset} / {dataset}")
            ax.set_xlabel("RMSE difference B−A (cycles); negative favours B")
            ax.grid(axis="x", alpha=.25)
            ax.legend()
    fig.suptitle("P08: paired differences at the same HI landmark; descriptive 95% intervals")
    fig.savefig(out / "paired_effects.png", dpi=160)
    plt.close(fig)
    (out / "report_metadata.json").write_text(json.dumps({"script_sha256": p08.sha(p08.ROOT / "experiments/report_pilot_hi_trajectory_08.py")}, indent=2), encoding="utf-8")
    p08.refresh_manifest()


if __name__ == "__main__":
    main()
