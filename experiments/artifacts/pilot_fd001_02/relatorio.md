# P02 — resultados exploratórios sem inspeção

Cinco folds por motor, com 40/20/20/20 motores para ajuste/calibração/selecção/avaliação. Todos os limiares e variantes escolhidos apenas na partição interna de selecção. Os motores externos já foram explorados em P01; não há confirmação independente.

## Detector

| detector | detected | median_P | alerts_by_40 | median_lead |
| --- | --- | --- | --- | --- |
| p_fixed2 | 100 | 24.000 | 100 | 172.500 |
| p | 100 | 69.500 | 6 | 128.000 |

A calibração assume ciclos 21–40 estáveis. Alertas precoces são diagnóstico dessa hipótese, não falsos positivos confirmados. Ausência de detecção é preservada. Não se mede P físico.

## Todas as variantes

| model | variant | engines | endpoints | mean_unused | mean_exposure |
| --- | --- | --- | --- | --- | --- |
| GBR | global | 100 | 0 | 71.980 | 134.330 |
| GBR | global_gate30 | 100 | 0 | 30.550 | 175.760 |
| GBR | local_gate30 | 100 | 0 | 26.080 | 180.230 |
| GBR | raw | 100 | 4 | 9.500 | 196.810 |
| LGBM | global | 100 | 0 | 86.890 | 119.420 |
| LGBM | global_gate30 | 100 | 0 | 31.080 | 175.230 |
| LGBM | local_gate30 | 100 | 0 | 24.140 | 182.170 |
| LGBM | raw | 100 | 0 | 9.600 | 196.710 |
| RF | global | 100 | 0 | 88.520 | 117.790 |
| RF | global_gate30 | 100 | 0 | 28.530 | 177.780 |
| RF | local_gate30 | 100 | 0 | 23.830 | 182.480 |
| RF | raw | 100 | 1 | 9.470 | 196.840 |
| XGB | global | 100 | 0 | 91.310 | 115.000 |
| XGB | global_gate30 | 100 | 0 | 31.320 | 174.990 |
| XGB | local_gate30 | 100 | 0 | 25.090 | 181.220 |
| XGB | raw | 100 | 1 | 9.780 | 196.530 |

`raw`: sem margem; `global`: margem de máximos por motor; `global_gate30`: mesma margem apenas na região prevista ≤30; `local_gate30`: margem estimada nessa região. Gatilho ≤10 e acção imediata, sem antecedência logística validada.

## Variante escolhida internamente por modelo

| model | engines | endpoints | mean_unused | mean_exposure |
| --- | --- | --- | --- | --- |
| GBR | 100 | 0 | 26.080 | 180.230 |
| LGBM | 100 | 0 | 9.600 | 196.710 |
| RF | 100 | 1 | 12.180 | 194.130 |
| XGB | 100 | 1 | 12.560 | 193.750 |

A selecção minimiza primeiro chegadas ao endpoint, depois vida não usada. Não demonstra safety nem selecciona um modelo vencedor. Mais exposição só é economicamente preferível dentro de um domínio admissível ainda não estabelecido. A diferença para P01 também inclui menor conjunto de treino; não é efeito isolado do detector. Nenhuma inspeção foi simulada.

## Rastreabilidade

[Protocolo](../../protocolo_piloto_fd001_02.md). CSVs guardam todas as escolhas, margens, predições e decisões por motor. Metadados guardam hashes, versões e partições; manifesto cobre todos os artefactos. Sem alterações aos dados ou resultados de P01. O protocolo principal não está congelado.

## Leitura dos resultados e próxima decisão

Com limiar fixo, 100/100 alertas ocorreram até o ciclo 40; com selecção interna do detector, 6/100. As medianas de P foram 24.0 e 69.5. A mudança de referência altera o ciclo de alerta, mas não valida o início físico de degradação. A hipótese de estabilidade até 40 deverá ser confrontada em sensibilidade antes de fixar P.

A margem global média por modelo ficou entre 59.11 e 69.87 ciclos; a local, entre 14.11 e 15.53. Comparar global com global_gate30 isola a região de acção; comparar global_gate30 com local_gate30 isola a calibração da margem nessa região. Resultados externos de todas as variantes foram preservados, incluindo variantes não escolhidas internamente.

Antes de congelar: resolver referência de HI/F e identificação operacional de P, verificar robustez da hipótese inicial e dos parâmetros 10/30, definir admissibilidade e antecedência, avaliar explicações e especificar o futuro braço de inspeção. A rodada não introduz inspeções nem congela o protocolo.

![Contrastes de política e margens](policy_tradeoff.png)

Verificações: separação de motores; predições sem duplicação; escolhas reproduzidas somente dos resultados internos; margens recalculadas das predições de calibração; hashes dos dados, código importado, código da rodada e protocolo intactos.
