"""Validate saved pilot outputs and produce an exploratory report."""

import hashlib
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "experiments/artifacts/pilot_fd001_01"


def table(frame):
    rows = ["| " + " | ".join(map(str, frame.columns)) + " |",
            "| " + " | ".join(["---"] * len(frame.columns)) + " |"]
    rows += ["| " + " | ".join(f"{v:.3f}" if isinstance(v, float) else str(v) for v in row) + " |"
             for row in frame.itertuples(index=False, name=None)]
    return "\n".join(rows)


def run():
    pred = pd.read_csv(OUT / "predictions.csv")
    summary = pd.read_csv(OUT / "prediction_summary.csv")
    decisions = pd.read_csv(OUT / "decision_summary.csv")
    detector = pd.read_csv(OUT / "detected_P.csv")
    sensitivity = pd.read_csv(OUT / "detector_sensitivity.csv")
    splits = json.loads((OUT / "splits.json").read_text())
    assert len(detector) == 100 and detector.unit.nunique() == 100
    assert (summary.engines == 100).all(), "Report missing-engine coverage before accepting metrics"
    assert (decisions.engines == 100).all()
    for split in splits:
        fit, cal, test = map(set, [split["fit"], split["calibration"], split["evaluation"]])
        assert len(fit) == 60 and len(cal) == len(test) == 20
        assert not (fit & cal or fit & test or cal & test)
        assert set(pred.loc[pred.fold == split["fold"], "unit"]) == test
    assert not pred.duplicated(["fold", "model", "unit", "cycle"]).any()
    assert (pred.adjusted <= pred.raw + 1e-10).all()
    assert (pred.adjusted >= 0).all()
    assert (pred.rul == pred.end - pred.cycle).all()
    onset = pred.unit.map(detector.set_index("unit").p)
    assert (pred.cycle >= onset).all()
    sens = sensitivity.groupby(["window", "sigma", "channels"]).agg(
        motores=("unit", "size"), detecções=("p", "count"),
        P_mediano=("p", "median"), antecedência_mediana=("lead", "median"),
        alertas_até_40=("p", lambda s: int((s <= 40).sum()))).reset_index()
    sens.to_csv(OUT / "detector_summary.csv", index=False)
    # One chosen setting is fixed in the protocol, not selected on the following table.
    text = """# Resultados do primeiro piloto FD001

Rodada P01, exploratória. Foram avaliados 100 motores completos em cinco folds externos, com 60 motores de ajuste, 20 de calibração e 20 de avaliação por fold. Cada motor aparece uma única vez na avaliação. Nenhum dado do teste oficial truncado foi utilizado.

**Achados da configuração inicial.** O alerta P teve mediana no ciclo 24 e ocorreu até o ciclo 40 em 100/100 motores. Isso exige investigar se o detector identifica degradação ou afastamentos precoces da referência; não há rótulo independente para resolver essa questão nesta rodada. A configuração de janela 5/três desvios/dois sensores levou a mediana a 73,5, ilustrando a sensibilidade, sem estabelecer qual P está correcto.

Os RMSE médios por motor das previsões originais ficaram entre 32,17 e 33,61 ciclos. A margem média por fold variou entre 86,67 e 102,64 ciclos conforme o modelo, aumentando o RMSE ajustado para 76,14–84,18 ciclos. Com gatilho de dez ciclos, os modelos originais chegaram ao endpoint em 1–8 motores; após a margem, em nenhum, mas descartaram em média 95,53–130,94 ciclos. A ausência observada de chegadas ao endpoint não demonstra segurança; o compromisso mostra conservadorismo excessivo a investigar. Essas métricas ao longo da história não são directamente comparáveis ao RMSE no último ponto do teste oficial de outros trabalhos.

## Detecção de P

Média móvel causal, referência inicial de 20 ciclos, limiares estatísticos e persistência de três ciclos. A configuração inicial é janela 15, dois desvios e pelo menos dois sensores. A tabela mostra sensibilidade; não selecciona retrospectivamente uma configuração vencedora. Alertas até 40 são apenas diagnóstico de início muito precoce, não falsos positivos confirmados. O FD001 não oferece rótulo independente de P físico.

""" + table(sens) + """

## Prognóstico

RMSE médio calculado primeiro dentro de cada motor e depois entre motores; somente ciclos pós-P com atributos disponíveis. A margem usa o quantil 0,9 dos máximos erros de sobrestimação por motor de calibração. Ela pode sacrificar precisão e vida aproveitada. As colunas `raw` e `adjusted` distinguem previsão original e previsão após subtrair a margem. Sem afirmação de cobertura garantida ou segurança operacional.

""" + table(summary) + """

## Decisões sequenciais exploratórias

Remoção no primeiro ciclo com RUL prevista abaixo ou igual ao gatilho; sem disparo, chega-se ao endpoint. `endpoint_count` inclui remoção no próprio endpoint. `mean_unused` é vida não aproveitada, em ciclos. `age_q10` usa uma idade definida somente nas vidas de ajuste; `at_P` remove no alerta. São controles exploratórios, não referências optimizadas.

""" + table(decisions) + """

## Interpretação e limites

Chegada ao endpoint representa falha no benchmark, não acidente aeronáutico. Uma política sem chegadas ao endpoint nesta amostra não fica certificada ou demonstrada segura. Não foi fixada admissibilidade operacional, portanto não há política economicamente óptima seleccionada.

A taxa por 1.000 ciclos é uma razão exploratória de contagem/exposição. Sua interpretação como renovação requer vidas iid sob AGAN e ausência de indisponibilidade, hipóteses ainda não validadas. Nenhum custo complementar foi incluído. Com custo fixo por evento, alterar apenas sua escala não altera o ranking.

Ainda não há HI físico, inspeção ou fusão PHM + inspeção nesta rodada. Também não há SHAP ou validação de explicações; as importâncias de impureza guardadas são somente diagnósticas. CatBoost e SHAP não estavam instalados no ambiente global. Não houve busca de hiperparâmetros; modelos têm parâmetros iniciais fixos, sem equivalência alegada de capacidade ou esforço computacional. Não se demonstra superioridade geral de uma família.

O primeiro ensaio foi interrompido depois de um teste de causalidade identificar instabilidade de `rolling.skew`: modificar observações futuras alterava numericamente atributos anteriores. A assimetria foi substituída por cálculo centrado estritamente em cada janela; os dois testes de fronteira de informação passaram antes da rodada válida. Os resultados abaixo do protocolo corrigido não foram usados para ajustar configurações durante a execução.

As próximas adaptações são exploratórias e devem considerar alertas precoces, conservadorismo da margem e comparação com controles simples. A referência de condição e a geração independente das inspeções continuam por definir. Os folds já examinados não serão tratados como teste intocado numa confirmação posterior.

## Artefatos

[Protocolo](../../protocolo_piloto_fd001_01.md), `metadata.json`, `splits.json`, `predictions.csv`, `metrics_per_engine.csv`, `prediction_summary.csv`, `decisions_per_engine.csv`, `decision_summary.csv`, `detector_sensitivity.csv`, `detector_summary.csv`, `detected_P.csv`, `impurity_importances.csv` e `detector_sensitivity.png`. O manifesto registra hashes de todos os arquivos desta rodada. Não houve alteração nos dados brutos.
"""
    (OUT / "relatorio.md").write_text(text, encoding="utf-8")
    metadata = json.loads((OUT / "metadata.json").read_text())
    assert hashlib.sha256((ROOT / "CMAPSSData/train_FD001.txt").read_bytes()).hexdigest() == metadata["data_sha256"]
    assert hashlib.sha256((ROOT / "experiments/pilot_fd001.py").read_bytes()).hexdigest() == metadata["script_sha256"]
    manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir())
                if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(sens.to_string(index=False))
    print(summary.to_string(index=False))
    print(decisions.to_string(index=False))
    print("Artifact checks passed; raw data and run script hashes unchanged.")


if __name__ == "__main__":
    run()
