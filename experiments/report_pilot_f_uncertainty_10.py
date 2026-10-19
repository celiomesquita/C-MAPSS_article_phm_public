"""P10: tables and figure from frozen calibration and evaluation artefacts."""

import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import pilot_f_uncertainty_10 as p10


def table(frame):
    rows = ["| " + " | ".join(frame.columns) + " |", "|" + "---|"*len(frame.columns)]
    for values in frame.itertuples(index=False, name=None):
        rows.append("| " + " | ".join(f"{v:.3f}" if isinstance(v, (float, np.floating)) else str(v) for v in values) + " |")
    return "\n".join(rows)


def main():
    out = p10.OUT
    bands = pd.read_csv(out / "band_summary.csv")
    reserves = pd.read_csv(out / "reserve_summary.csv")
    points = pd.read_csv(out / "point_summary.csv")
    pairs = pd.read_csv(out / "contrasts.csv")
    quantiles = pd.read_csv(out / "quantiles.csv")
    primary = bands.loc[bands.dataset.eq("complete") & bands.scope.eq("path") & bands.alpha.eq(.02)]
    availability = reserves.loc[reserves.dataset.eq("complete") & reserves.scope.eq("path") & reserves.alpha.eq(.02)]
    report = [
        "# P10 — calibração a 98% e antecedência disponível",
        "Protocolo: [especificação anterior aos ajustes](../../protocolo_incerteza_f_10.md). "
        "FD001 principal; FD003 robustez. Três repetições de dez dobras, com F25/C15/U50/E10 "
        "disjuntos por motor em cada ajuste. F aprende os parâmetros da mesma forma de índice de "
        "saúde (HI) adotada em M18; C ajusta conversores; U calibra exclusivamente os erros e E "
        "avalia. Os mesmos 100 motores completos são avaliados uma vez por repetição: não são "
        "300 motores independentes. ISO é regressão isotónica crescente; RF_SLOPE é floresta "
        "aleatória com HI e inclinação causal de 20 HI. Nenhum hiperparâmetro foi escolhido por U/E.",
        "O marco HI≤0,5 inicia a avaliação da previsão de F, sem definir P, F ou remoção. "
        "Somente ciclos observados são usados. O teste oficial truncado é secundário e utiliza "
        "apenas a primeira dobra de cada repetição; já foi examinado em rodadas anteriores.",
        "## Resultado primário: trajetória completa, nominal 98%",
        "Cada cobertura exige conter o endpoint T em todos os ciclos observados após o marco. "
        "A bilateral usa o quantil do máximo erro absoluto; a unilateral usa o máximo erro "
        "positivo. L=max(t,F̂−q_late). Antecedência é L−t no marco; largura é a mediana entre "
        "motores das larguras medianas por trajetória. Valores em ciclos; proporções entre zero e um.",
        table(primary[["subset", "repeat", "method", "path_available", "path_coverage", "path_lower_coverage",
                       "median_width", "conservative_lead_median", "collapsed_point_fraction", "calibration_n_min"]]),
        "![Cobertura e antecedência, nominal 98%](coverage_lead_98.png)",
        "## Disponibilidade de reserva e execução",
        "Diagnóstico A=1{L−t≥m+d}, para reserva m=15/12 e execução d=1/2. Não agenda "
        "retirada, não escolhe a âncora da reserva e não duplica uma margem na política. "
        "mark_fraction é a fração de motores disponíveis com A=1 no marco; any_fraction indica "
        "algum ciclo observado com A=1; cycle_fraction é a média, entre motores, da fração de "
        "seus ciclos com A=1. Nenhuma remoção ou inspeção foi simulada.",
        table(availability[["subset", "repeat", "method", "reserve", "delay", "path_available",
                            "point_available", "mark_fraction", "any_fraction", "cycle_fraction"]]),
        "## Erro pontual e contraste pareado no marco",
        "Raiz do erro quadrático médio (RMSE), erro absoluto médio (MAE) e viés de F̂−T. "
        "Diferença RF_SLOPE−ISO nos mesmos motores/ciclos, com intervalo descritivo de 95% "
        "por 2000 reamostragens pareadas por motor; separado da banda individual de F.",
        table(points.loc[points.event.eq("mark"), ["subset", "dataset", "repeat", "method", "total", "available", "rmse", "mae", "bias"]]),
        table(pairs.loc[pairs.event.eq("mark")]),
        "## Quantis e amostra efetiva",
        "Ordem corrigida k=ceil((n+1)(1−α)). Em U50, o alvo 98% usa k=50, isto é, "
        "o maior escore; n≤48 produziria +infinito. A tabela resume as dez dobras por "
        "domínio, repetição, método, escopo e nível, sem juntar motores para calibrar.",
        table(quantiles.groupby(["subset", "repeat", "method", "scope", "alpha"], as_index=False).agg(
            n_min=("n", "min"), n_max=("n", "max"), k_min=("k", "min"), k_max=("k", "max"),
            q_abs_min=("q_abs", "min"), q_abs_max=("q_abs", "max"),
            q_late_min=("q_late", "min"), q_late_max=("q_late", "max"))),
        "## Sensibilidade 95% e calibração somente no marco",
        "Níveis e escopos pré-especificados. A cobertura da trajetória com quantil somente "
        "do marco é diagnóstica: a calibração pontual não promete cobertura simultânea.",
        table(bands.loc[bands.dataset.eq("complete")]),
        "## Testes oficiais truncados: disponibilidade condicional",
        "A trajetória termina no truncamento. Rótulos de vida útil remanescente (RUL) "
        "determinam T somente para aferição, após prever. Motores sem marco não são imputados; "
        "cobertura entre disponíveis não representa toda a frota.",
        table(bands.loc[bands.dataset.eq("truncated") & bands.scope.eq("path") & bands.alpha.eq(.02)]),
        "## Limites de inferência",
        "98% é alvo preditivo nominal, não comprovação de ultrapassagem ≤2% pela futura política. "
        "A interpretação marginal exige intercambiabilidade e o mesmo domínio de disponibilidade. "
        "Uma dobra E10 tem resolução de dez pontos percentuais; os 100 motores de cada repetição "
        "têm resolução de um ponto. As repetições compartilham motores e modelos de dobras "
        "compartilham desenvolvimento. F25/C15/U50/E10 também reduz ajuste e altera avaliação "
        "frente a P09: diferenças não isolam o efeito de aumentar U. Não foram definidos "
        "o gatilho de incerteza elevada ou a âncora da reserva; não há conclusão operacional "
        "sobre voo após T. A forma HI permanece referência de trabalho, sem equivalência física.",
        "A ordem corrigida segue Lei et al. (2018), *Distribution-Free Predictive Inference for "
        "Regression*, DOI 10.1080/01621459.2017.1307116, seção 2: "
        "[fonte primária](https://www.stat.cmu.edu/~ryantibs/papers/conformal-jasa.pdf). "
        "O escore máximo por trajetória é a adaptação deste protocolo.",
        "## Verificação e reconstrução",
        "A reconstrução inicial encontrou arredondamento em comparações no limiar m+d. "
        "Emenda posterior aos ajustes: tolerância de 10⁻⁹ ciclo, sem mudança de classificações "
        "ou reajuste. Diagnósticos foram recalculados de previsões congeladas; versões originais "
        "foram preservadas. [Emenda](amendment_numeric_boundary.json).",
        "[Verificação](verification.json), [metadados](metadata.json), [partições](splits.json), "
        "[congelamentos anteriores à avaliação](freezes.json) e [manifesto](manifest.json). "
        "CSV preservados: scores, events, bands, quantiles, point_summary, band_summary, "
        "contrasts, reserves e reserve_summary. Previsões e modelos estão arquivados por dobra.",
    ]
    (out / "relatorio.md").write_text("\n\n".join(report)+"\n", encoding="utf-8")
    fig, axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    for ax, subset in zip(axes, ["FD001", "FD003"]):
        for method, colour in [("ISO", "#2463a6"), ("RF_SLOPE", "#ce661c")]:
            g = primary.loc[primary.subset.eq(subset) & primary.method.eq(method)]
            ax.scatter(g.conservative_lead_median, 100*g.path_lower_coverage, label=method, color=colour)
            for r in g.itertuples():
                ax.annotate(str(r.repeat), (r.conservative_lead_median, 100*r.path_lower_coverage), xytext=(4, 3), textcoords="offset points")
        ax.axhline(98, color="grey", linestyle="--", linewidth=1)
        ax.set(title=subset, xlabel="Median lower-bound lead at landmark (cycles)", ylim=(85, 101))
        ax.grid(alpha=.2)
        ax.legend()
    axes[0].set_ylabel("Whole-path lower coverage (%)")
    fig.tight_layout()
    fig.savefig(out / "coverage_lead_98.png", dpi=180)
    plt.close(fig)
    (out / "report_metadata.json").write_text(json.dumps(dict(
        script_sha256=p10.sha(p10.ROOT / "experiments/report_pilot_f_uncertainty_10.py"),
        source="band_summary.csv", primary_alpha=.02, figure_labels="repeat, not independent samples"), indent=2), encoding="utf-8")
    p10.refresh_manifest()


if __name__ == "__main__":
    main()
