"""P09 tables and uncertainty trade-offs from archived predictions."""

import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import pilot_f_uncertainty_09 as p09


def table(frame):
    rows = ["| " + " | ".join(frame.columns) + " |", "|" + "---|"*len(frame.columns)]
    for values in frame.itertuples(index=False, name=None):
        rows.append("| " + " | ".join(f"{v:.3f}" if isinstance(v, (float, np.floating)) else str(v) for v in values) + " |")
    return "\n".join(rows)


def main():
    out = p09.OUT
    points = pd.read_csv(out / "point_summary.csv")
    bands = pd.read_csv(out / "band_summary.csv")
    quantiles = pd.read_csv(out / "quantiles.csv")
    pairs = pd.read_csv(out / "contrasts.csv")
    main_bands = bands.loc[bands.dataset.eq("complete") & bands.scope.eq("path")]
    limits = main_bands.groupby(["subset", "method", "alpha"], as_index=False).agg(
        coverage_min=("path_coverage", "min"), coverage_max=("path_coverage", "max"),
        lower_coverage_min=("path_lower_coverage", "min"), lower_coverage_max=("path_lower_coverage", "max"),
        width_min=("median_width", "min"), width_max=("median_width", "max"),
        conservative_lead_min=("conservative_lead_median", "min"), conservative_lead_max=("conservative_lead_median", "max"))
    report = ["# P09 — robustez e incerteza de F após o marco HI≤0,5",
              "Índice de saúde (HI) de M18, com a mesma forma funcional e parâmetros reaprendidos em cada "
              "partição. Três repetições de cinco folds por motor em FD001 e FD003. F40 ajusta o HI, C20 "
              "ajusta a conversão para vida útil remanescente (RUL), U20 calibra exclusivamente a incerteza "
              "e E20 avalia. Não há seleção de configurações em U/E. Os testes oficiais truncados usam "
              "somente o modelo/calibração do fold 1 de cada repetição, sem ajuste adicional.",
              "ISO = isotônico crescente; RF_HI = floresta aleatória com HI corrente; RF_SLOPE = mesma "
              "floresta com HI e inclinação causal de 20 valores. Todos usam ciclos ≥39. Hiperparâmetros "
              "da convenção HI e das florestas foram pré-fixados; a separação nesta rodada é nova, mas "
              "os dados já informaram escolhas anteriores. São resultados exploratórios.",
              "## Prognóstico no primeiro marco", 
              "RMSE = raiz do erro quadrático médio; MAE = erro absoluto médio. Erro = F previsto menos "
              "endpoint real, em ciclos; viés positivo prevê F tarde. As métricas são condicionais à "
              "disponibilidade do marco. Cada repetição tem os mesmos 100 motores, não uma nova amostra de 100.",
              table(points.loc[points.event.eq("mark"), ["subset", "dataset", "repeat", "method", "total", "available", "rmse", "mae", "bias", "positive_fraction", "actual_lead_median"]]),
              "## Comparações pareadas no marco", 
              "Diferença = RF_SLOPE menos referência, nos mesmos motores e ciclos. Intervalos descritivos "
              "de 95% por bootstrap pareado de 2.000 amostras por motor, separadamente em cada repetição. "
              "Esses intervalos são distintos das bandas preditivas de F calibradas em U.",
              table(pairs.loc[pairs.event.eq("mark")]),
              "## Bandas da trajetória completa — variação entre repetições",
              "Valores mínimos/máximos entre três repetições; não intervalos de confiança sobre 300 motores. "
              "alpha=0,10 e 0,05 correspondem a alvos nominais de 90% e 95%. A largura é a mediana entre "
              "motores de suas larguras medianas ao longo da trajetória. O limite inferior L fornece "
              "antecedência estimada L−t no marco; não a antecedência real até F ou uma ordem de remoção.",
              table(limits), "![Cobertura, largura e antecedência estimada](uncertainty_tradeoff.png)",
              "## Cobertura por motor e por repetição", 
              "path_coverage exige que T esteja na banda em TODOS os ciclos observados desde a passagem "
              "com atributos disponíveis; path_lower_coverage exige L(t)≤T em todos esses ciclos. "
              "As duas bandas têm calibrações diferentes, bilateral e unilateral. Um alvo nominal não "
              "é um requisito aeronáutico de safety. As coberturas observadas podem ficar abaixo do alvo "
              "em uma divisão finita; isso não refuta por si uma propriedade marginal sob permutabilidade.",
              table(main_bands[["subset", "repeat", "method", "alpha", "path_available", "path_coverage", "path_lower_coverage", "median_width", "conservative_lead_median", "collapsed_point_fraction", "calibration_n_min", "finite_abs_fraction"]]),
              "## Calibrar no marco não equivale a calibrar a trajetória",
              "scope=point usa somente o erro no primeiro marco de cada motor U. scope=path usa o maior "
              "erro da trajetória, um escore por motor. A tabela compara ambos os usos no alvo nominal de "
              "90%; aplicar a banda pontual em todos os ciclos não lhe concede cobertura simultânea.",
              table(bands.loc[bands.dataset.eq("complete") & bands.alpha.eq(.1), ["subset", "repeat", "method", "scope", "point_coverage", "path_coverage", "point_lower_coverage", "path_lower_coverage"]]),
              "## Teste truncado — apenas a trajetória observada", 
              "Motores sem passagem não recebem sensores ou cruzamentos futuros inventados. A RUL oficial "
              "permite avaliar T, mas não observar a qualidade das previsões depois do truncamento. "
              "Assim, cobertura de toda a trajetória observada no teste não é cobertura de toda a vida.",
              table(bands.loc[bands.dataset.eq("truncated") & bands.scope.eq("path"), ["subset", "repeat", "method", "alpha", "total", "path_available", "point_available", "path_coverage", "path_lower_coverage", "median_width", "conservative_lead_median"]]),
              "## Calibração e fontes", 
              "Quantil = escore ordenado de rank ceil((n+1)(1−alpha)), com +infinito quando esse rank "
              "excede n. Os quantis individuais de cada partição estão em quantiles.csv; não se substitui "
              "o caso não finito por um máximo amostral. Parâmetros HI, modelos e quantis foram congelados "
              "antes da avaliação, com rastreabilidade em execution_start.json, freezes.json e metadata.json.",
              table(quantiles.groupby(["subset", "method", "scope", "alpha"], as_index=False).agg(n_min=("n", "min"), n_max=("n", "max"), q_abs_min=("q_abs", "min"), q_abs_max=("q_abs", "max"), q_late_min=("q_late", "min"), q_late_max=("q_late", "max"))),
              "A ordem estatística corrigida e a separação ajuste/calibração seguem "
              "[Lei et al. (2018), seção 2 e seção 2.2/Algoritmo 2](https://www.stat.cmu.edu/~ryantibs/papers/conformal-jasa.pdf), "
              "DOI 10.1080/01621459.2017.1307116. O escore máximo temporal por motor e o domínio após "
              "o marco são nossa adaptação experimental. Permutabilidade, reutilização histórica, "
              "pequena calibração e mudança de distribuição limitam a interpretação; não há garantia "
              "condicional por estado, validação física do HI ou admissibilidade operacional demonstrada.",
              "Não foram escolhidas políticas de remoção, tolerâncias operacionais ou custos adicionais. "
              "Não houve inspeções, alteração da forma HI, busca de outra fórmula ou edição do artigo M17. "
              "Todos os resultados, repetições, casos ausentes e diferenças desfavoráveis permanecem arquivados."]
    (out / "relatorio.md").write_text("\n\n".join(report)+"\n", encoding="utf-8")
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), layout="constrained")
    colors = {"ISO": "#7570b3", "RF_HI": "#d95f02", "RF_SLOPE": "#1b9e77"}
    markers = {1: "o", 2: "s", 3: "^"}
    for i, subset in enumerate(["FD001", "FD003"]):
        sample = main_bands.loc[main_bands.subset.eq(subset) & main_bands.alpha.eq(.1)]
        for r in sample.itertuples():
            for j, x, y in [(0, r.median_width, r.path_coverage), (1, r.conservative_lead_median, r.path_lower_coverage)]:
                axes[i, j].scatter(x, 100*y, color=colors[r.method], marker=markers[r.repeat], s=65,
                                   label=r.method if r.repeat == 1 else None)
        for j in range(2):
            axes[i, j].axhline(90, color="black", linestyle="--", linewidth=1)
            axes[i, j].set_title(subset+" / complete trajectories")
            axes[i, j].grid(alpha=.2)
            axes[i, j].legend(fontsize=8)
        axes[i, 0].set_xlabel("Median bilateral band width (cycles)")
        axes[i, 0].set_ylabel("Whole observed-path coverage (%)")
        axes[i, 1].set_xlabel("Median conservative lead at landmark, L−t (cycles)")
        axes[i, 1].set_ylabel("Whole-path lower-bound coverage (%)")
    fig.suptitle("P09: nominal 90%; repetition 1 = circle, 2 = square, 3 = triangle")
    fig.savefig(out / "uncertainty_tradeoff.png", dpi=160)
    plt.close(fig)
    (out / "report_metadata.json").write_text(json.dumps({"script_sha256": p09.sha(p09.ROOT / "experiments/report_pilot_f_uncertainty_09.py"),
                                                          "markers": {"circle": 1, "square": 2, "triangle": 3}}, indent=2), encoding="utf-8")
    p09.refresh_manifest()


if __name__ == "__main__":
    main()
