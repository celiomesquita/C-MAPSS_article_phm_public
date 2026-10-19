# Resultados do primeiro piloto FD001

Rodada P01, exploratória. Foram avaliados 100 motores completos em cinco folds externos, com 60 motores de ajuste, 20 de calibração e 20 de avaliação por fold. Cada motor aparece uma única vez na avaliação. Nenhum dado do teste oficial truncado foi utilizado.

**Achados da configuração inicial.** O alerta P teve mediana no ciclo 24 e ocorreu até o ciclo 40 em 100/100 motores. Isso exige investigar se o detector identifica degradação ou afastamentos precoces da referência; não há rótulo independente para resolver essa questão nesta rodada. A configuração de janela 5/três desvios/dois sensores levou a mediana a 73,5, ilustrando a sensibilidade, sem estabelecer qual P está correcto.

Os RMSE médios por motor das previsões originais ficaram entre 32,17 e 33,61 ciclos. A margem média por fold variou entre 86,67 e 102,64 ciclos conforme o modelo, aumentando o RMSE ajustado para 76,14–84,18 ciclos. Com gatilho de dez ciclos, os modelos originais chegaram ao endpoint em 1–8 motores; após a margem, em nenhum, mas descartaram em média 95,53–130,94 ciclos. A ausência observada de chegadas ao endpoint não demonstra segurança; o compromisso mostra conservadorismo excessivo a investigar. Essas métricas ao longo da história não são directamente comparáveis ao RMSE no último ponto do teste oficial de outros trabalhos.

## Detecção de P

Média móvel causal, referência inicial de 20 ciclos, limiares estatísticos e persistência de três ciclos. A configuração inicial é janela 15, dois desvios e pelo menos dois sensores. A tabela mostra sensibilidade; não selecciona retrospectivamente uma configuração vencedora. Alertas até 40 são apenas diagnóstico de início muito precoce, não falsos positivos confirmados. O FD001 não oferece rótulo independente de P físico.

| window | sigma | channels | motores | detecções | P_mediano | antecedência_mediana | alertas_até_40 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5 | 2.000 | 1 | 100 | 100 | 24.000 | 173.500 | 100 |
| 5 | 2.000 | 2 | 100 | 100 | 27.000 | 169.000 | 92 |
| 5 | 3.000 | 1 | 100 | 100 | 36.000 | 163.000 | 60 |
| 5 | 3.000 | 2 | 100 | 100 | 73.500 | 122.000 | 7 |
| 10 | 2.000 | 1 | 100 | 100 | 23.000 | 173.500 | 100 |
| 10 | 2.000 | 2 | 100 | 100 | 26.000 | 171.500 | 98 |
| 10 | 3.000 | 1 | 100 | 100 | 29.000 | 166.000 | 95 |
| 10 | 3.000 | 2 | 100 | 100 | 37.000 | 160.500 | 61 |
| 15 | 2.000 | 1 | 100 | 100 | 23.000 | 175.000 | 100 |
| 15 | 2.000 | 2 | 100 | 100 | 24.000 | 172.500 | 100 |
| 15 | 3.000 | 1 | 100 | 100 | 26.000 | 169.000 | 99 |
| 15 | 3.000 | 2 | 100 | 100 | 29.000 | 168.000 | 96 |

## Prognóstico

RMSE médio calculado primeiro dentro de cada motor e depois entre motores; somente ciclos pós-P com atributos disponíveis. A margem usa o quantil 0,9 dos máximos erros de sobrestimação por motor de calibração. Ela pode sacrificar precisão e vida aproveitada. As colunas `raw` e `adjusted` distinguem previsão original e previsão após subtrair a margem. Sem afirmação de cobertura garantida ou segurança operacional.

| model | mode | engines | mean_engine_rmse | mean_overprediction_fraction | mean_margin |
| --- | --- | --- | --- | --- | --- |
| GBR | adjusted | 100 | 76.135 | 0.003 | 86.672 |
| GBR | raw | 100 | 32.174 | 0.572 | 86.672 |
| LGBM | adjusted | 100 | 82.790 | 0.002 | 98.674 |
| LGBM | raw | 100 | 32.975 | 0.568 | 98.674 |
| RF | adjusted | 100 | 84.181 | 0.002 | 102.640 |
| RF | raw | 100 | 33.608 | 0.576 | 102.640 |
| XGB | adjusted | 100 | 84.118 | 0.001 | 101.026 |
| XGB | raw | 100 | 33.403 | 0.566 | 101.026 |

## Decisões sequenciais exploratórias

Remoção no primeiro ciclo com RUL prevista abaixo ou igual ao gatilho; sem disparo, chega-se ao endpoint. `endpoint_count` inclui remoção no próprio endpoint. `mean_unused` é vida não aproveitada, em ciclos. `age_q10` usa uma idade definida somente nas vidas de ajuste; `at_P` remove no alerta. São controles exploratórios, não referências optimizadas.

| model | mode | trigger | engines | endpoint_count | mean_unused | mean_exposure | restorations_per_1000_cycles |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GBR | adjusted | 0 | 100 | 0 | 81.010 | 125.300 | 7.981 |
| GBR | adjusted | 5 | 100 | 0 | 88.250 | 118.060 | 8.470 |
| GBR | adjusted | 10 | 100 | 0 | 95.530 | 110.780 | 9.027 |
| GBR | raw | 0 | 100 | 90 | 0.700 | 205.610 | 4.864 |
| GBR | raw | 5 | 100 | 51 | 2.880 | 203.430 | 4.916 |
| GBR | raw | 10 | 100 | 8 | 8.470 | 197.840 | 5.055 |
| LGBM | adjusted | 0 | 100 | 0 | 110.220 | 96.090 | 10.407 |
| LGBM | adjusted | 5 | 100 | 0 | 121.990 | 84.320 | 11.860 |
| LGBM | adjusted | 10 | 100 | 0 | 128.000 | 78.310 | 12.770 |
| LGBM | raw | 0 | 100 | 98 | 0.040 | 206.270 | 4.848 |
| LGBM | raw | 5 | 100 | 36 | 3.400 | 202.910 | 4.928 |
| LGBM | raw | 10 | 100 | 2 | 9.150 | 197.160 | 5.072 |
| RF | adjusted | 0 | 100 | 0 | 111.600 | 94.710 | 10.559 |
| RF | adjusted | 5 | 100 | 0 | 119.680 | 86.630 | 11.543 |
| RF | adjusted | 10 | 100 | 0 | 126.240 | 80.070 | 12.489 |
| RF | raw | 0 | 100 | 100 | 0.000 | 206.310 | 4.847 |
| RF | raw | 5 | 100 | 18 | 3.760 | 202.550 | 4.937 |
| RF | raw | 10 | 100 | 1 | 8.500 | 197.810 | 5.055 |
| XGB | adjusted | 0 | 100 | 0 | 115.730 | 90.580 | 11.040 |
| XGB | adjusted | 5 | 100 | 0 | 123.850 | 82.460 | 12.127 |
| XGB | adjusted | 10 | 100 | 0 | 130.940 | 75.370 | 13.268 |
| XGB | raw | 0 | 100 | 96 | 0.110 | 206.200 | 4.850 |
| XGB | raw | 5 | 100 | 27 | 3.890 | 202.420 | 4.940 |
| XGB | raw | 10 | 100 | 3 | 8.820 | 197.490 | 5.064 |
| age_q10 | baseline | -1 | 100 | 10 | 53.110 | 153.200 | 6.527 |
| at_P | baseline | -1 | 100 | 0 | 181.940 | 24.370 | 41.034 |

## Interpretação e limites

Chegada ao endpoint representa falha no benchmark, não acidente aeronáutico. Uma política sem chegadas ao endpoint nesta amostra não fica certificada ou demonstrada segura. Não foi fixada admissibilidade operacional, portanto não há política economicamente óptima seleccionada.

A taxa por 1.000 ciclos é uma razão exploratória de contagem/exposição. Sua interpretação como renovação requer vidas iid sob AGAN e ausência de indisponibilidade, hipóteses ainda não validadas. Nenhum custo complementar foi incluído. Com custo fixo por evento, alterar apenas sua escala não altera o ranking.

Ainda não há HI físico, inspeção ou fusão PHM + inspeção nesta rodada. Também não há SHAP ou validação de explicações; as importâncias de impureza guardadas são somente diagnósticas. CatBoost e SHAP não estavam instalados no ambiente global. Não houve busca de hiperparâmetros; modelos têm parâmetros iniciais fixos, sem equivalência alegada de capacidade ou esforço computacional. Não se demonstra superioridade geral de uma família.

O primeiro ensaio foi interrompido depois de um teste de causalidade identificar instabilidade de `rolling.skew`: modificar observações futuras alterava numericamente atributos anteriores. A assimetria foi substituída por cálculo centrado estritamente em cada janela; os dois testes de fronteira de informação passaram antes da rodada válida. Os resultados abaixo do protocolo corrigido não foram usados para ajustar configurações durante a execução.

As próximas adaptações são exploratórias e devem considerar alertas precoces, conservadorismo da margem e comparação com controles simples. A referência de condição e a geração independente das inspeções continuam por definir. Os folds já examinados não serão tratados como teste intocado numa confirmação posterior.

## Artefatos

[Protocolo](../../protocolo_piloto_fd001_01.md), `metadata.json`, `splits.json`, `predictions.csv`, `metrics_per_engine.csv`, `prediction_summary.csv`, `decisions_per_engine.csv`, `decision_summary.csv`, `detector_sensitivity.csv`, `detector_summary.csv`, `detected_P.csv`, `impurity_importances.csv` e `detector_sensitivity.png`. O manifesto registra hashes de todos os arquivos desta rodada. Não houve alteração nos dados brutos.
