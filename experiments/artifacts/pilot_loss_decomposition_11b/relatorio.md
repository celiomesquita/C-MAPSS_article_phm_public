# P11.2 — decomposição da perda

FD001 principal e FD003 robustez; três repetições de100 motores por domínio, reutilizados entre repetições. Modelos e políticas congelados, sem seleção em U/E. O oráculo conhece o endpoint: é referência diagnóstica, não política implementável.

O = informação desde o início; G = informação após primeira passagem HI≤0,5; A = informação após disponibilidade ≥39; real = política arquivada. A parcela posterior inclui previsão, quantil e regra, não apenas erro de prognóstico.

## Disponibilidade

| Domínio | Repetição | T−G mínimo | T−A mínimo | T−A mediano | Aquecimento máximo |
|---|---|---|---|---|---|
| FD001 | 1 | 11 | 11 | 36.5 | 0 |
| FD001 | 2 | 14 | 14 | 36 | 0 |
| FD001 | 3 | 14 | 14 | 36 | 0 |
| FD003 | 1 | 15 | 15 | 36 | 0 |
| FD003 | 2 | 10 | 10 | 37 | 0 |
| FD003 | 3 | 13 | 13 | 35 | 0 |

## Contraste principal: remoção ideal em T−1

Perda de planejamento por detecção/disponibilidade: zero em todas as repetições. As datas dos oráculos O/G/A coincidem neste contraste. Perda posterior pode coexistir com remoção excessivamente antecipada; vida e custo são necessários para identificá-la.

| Domínio | Repetição | Política | Vida não aproveitada | Excesso frente a O (ciclos) | Excesso de custo frente a O (%) | Chegadas/100 | Tardias | Ausências |
|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | AGE_D1 | 71.59 | 70.59 | 52.40 | 3 | 0 | 3 |
| FD001 | 1 | AGE_D2 | 71.59 | 70.59 | 52.40 | 3 | 1 | 2 |
| FD001 | 1 | HI_MARKER_D1 | 38.29 | 37.29 | 22.19 | 0 | 0 | 0 |
| FD001 | 1 | HI_MARKER_D2 | 37.29 | 36.29 | 21.47 | 0 | 0 | 0 |
| FD001 | 1 | HI_THRESHOLD_SELECTED_D1 | 22.80 | 21.80 | 11.88 | 1 | 0 | 1 |
| FD001 | 1 | HI_THRESHOLD_SELECTED_D2 | 24.21 | 23.21 | 12.75 | 1 | 0 | 1 |
| FD001 | 1 | HI_WAIT_SELECTED_D1 | 28.29 | 27.29 | 15.33 | 1 | 0 | 0 |
| FD001 | 1 | HI_WAIT_SELECTED_D2 | 27.30 | 26.30 | 14.69 | 1 | 1 | 0 |
| FD001 | 1 | ISO_LOWER98_M15_D1 | 37.81 | 36.81 | 21.85 | 0 | 0 | 0 |
| FD001 | 1 | ISO_LOWER98_M15_D2 | 37.08 | 36.08 | 21.32 | 0 | 0 | 0 |
| FD001 | 1 | ISO_POINT_M15_D1 | 15.18 | 14.18 | 7.42 | 7 | 0 | 5 |
| FD001 | 1 | ISO_POINT_M15_D2 | 14.99 | 13.99 | 7.31 | 10 | 1 | 5 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D1 | 37.55 | 36.55 | 21.66 | 0 | 0 | 0 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D2 | 36.57 | 35.57 | 20.96 | 0 | 0 | 0 |
| FD001 | 1 | RF_SLOPE_POINT_M15_D1 | 15.50 | 14.50 | 7.60 | 6 | 0 | 6 |
| FD001 | 1 | RF_SLOPE_POINT_M15_D2 | 15.76 | 14.76 | 7.75 | 6 | 0 | 5 |
| FD001 | 2 | AGE_D1 | 75.29 | 74.29 | 56.70 | 1 | 0 | 1 |
| FD001 | 2 | AGE_D2 | 75.29 | 74.29 | 56.70 | 1 | 0 | 1 |
| FD001 | 2 | HI_MARKER_D1 | 39.62 | 38.62 | 23.17 | 0 | 0 | 0 |
| FD001 | 2 | HI_MARKER_D2 | 38.62 | 37.62 | 22.43 | 0 | 0 | 0 |
| FD001 | 2 | HI_THRESHOLD_SELECTED_D1 | 25.34 | 24.34 | 13.45 | 1 | 0 | 1 |
| FD001 | 2 | HI_THRESHOLD_SELECTED_D2 | 25.14 | 24.14 | 13.32 | 1 | 0 | 1 |
| FD001 | 2 | HI_WAIT_SELECTED_D1 | 29.62 | 28.62 | 16.20 | 0 | 0 | 0 |
| FD001 | 2 | HI_WAIT_SELECTED_D2 | 29.62 | 28.62 | 16.20 | 0 | 0 | 0 |
| FD001 | 2 | ISO_LOWER98_M15_D1 | 38.90 | 37.90 | 22.64 | 0 | 0 | 0 |
| FD001 | 2 | ISO_LOWER98_M15_D2 | 38.07 | 37.07 | 22.03 | 0 | 0 | 0 |
| FD001 | 2 | ISO_POINT_M15_D1 | 13.15 | 12.15 | 6.29 | 15 | 0 | 11 |
| FD001 | 2 | ISO_POINT_M15_D2 | 14.34 | 13.34 | 6.95 | 10 | 1 | 8 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D1 | 39.23 | 38.23 | 22.88 | 0 | 0 | 0 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D2 | 38.34 | 37.34 | 22.23 | 0 | 0 | 0 |
| FD001 | 2 | RF_SLOPE_POINT_M15_D1 | 15.44 | 14.44 | 7.57 | 8 | 0 | 7 |
| FD001 | 2 | RF_SLOPE_POINT_M15_D2 | 15.99 | 14.99 | 7.88 | 6 | 1 | 5 |
| FD001 | 3 | AGE_D1 | 76.19 | 75.19 | 57.79 | 1 | 0 | 1 |
| FD001 | 3 | AGE_D2 | 76.19 | 75.19 | 57.79 | 1 | 0 | 1 |
| FD001 | 3 | HI_MARKER_D1 | 39.23 | 38.23 | 22.88 | 0 | 0 | 0 |
| FD001 | 3 | HI_MARKER_D2 | 38.23 | 37.23 | 22.15 | 0 | 0 | 0 |
| FD001 | 3 | HI_THRESHOLD_SELECTED_D1 | 24.61 | 23.61 | 12.99 | 0 | 0 | 0 |
| FD001 | 3 | HI_THRESHOLD_SELECTED_D2 | 25.04 | 24.04 | 13.26 | 2 | 0 | 0 |
| FD001 | 3 | HI_WAIT_SELECTED_D1 | 29.73 | 28.73 | 16.27 | 0 | 0 | 0 |
| FD001 | 3 | HI_WAIT_SELECTED_D2 | 29.73 | 28.73 | 16.27 | 0 | 0 | 0 |
| FD001 | 3 | ISO_LOWER98_M15_D1 | 37.66 | 36.66 | 21.74 | 0 | 0 | 0 |
| FD001 | 3 | ISO_LOWER98_M15_D2 | 37.08 | 36.08 | 21.32 | 0 | 0 | 0 |
| FD001 | 3 | ISO_POINT_M15_D1 | 14.35 | 13.35 | 6.95 | 12 | 0 | 7 |
| FD001 | 3 | ISO_POINT_M15_D2 | 14.71 | 13.71 | 7.16 | 10 | 4 | 4 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D1 | 38.14 | 37.14 | 22.08 | 0 | 0 | 0 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D2 | 37.18 | 36.18 | 21.39 | 0 | 0 | 0 |
| FD001 | 3 | RF_SLOPE_POINT_M15_D1 | 15.38 | 14.38 | 7.53 | 9 | 0 | 6 |
| FD001 | 3 | RF_SLOPE_POINT_M15_D2 | 15.56 | 14.56 | 7.63 | 12 | 3 | 5 |
| FD003 | 1 | AGE_D1 | 101.04 | 100.04 | 68.45 | 2 | 0 | 2 |
| FD003 | 1 | AGE_D2 | 101.04 | 100.04 | 68.45 | 2 | 1 | 1 |
| FD003 | 1 | HI_MARKER_D1 | 38.34 | 37.34 | 17.88 | 0 | 0 | 0 |
| FD003 | 1 | HI_MARKER_D2 | 37.34 | 36.34 | 17.32 | 0 | 0 | 0 |
| FD003 | 1 | HI_THRESHOLD_SELECTED_D1 | 29.26 | 28.26 | 12.97 | 0 | 0 | 0 |
| FD003 | 1 | HI_THRESHOLD_SELECTED_D2 | 29.05 | 28.05 | 12.86 | 0 | 0 | 0 |
| FD003 | 1 | HI_WAIT_SELECTED_D1 | 30.64 | 29.64 | 13.69 | 0 | 0 | 0 |
| FD003 | 1 | HI_WAIT_SELECTED_D2 | 30.44 | 29.44 | 13.58 | 0 | 0 | 0 |
| FD003 | 1 | ISO_LOWER98_M15_D1 | 37.51 | 36.51 | 17.41 | 0 | 0 | 0 |
| FD003 | 1 | ISO_LOWER98_M15_D2 | 36.99 | 35.99 | 17.12 | 0 | 0 | 0 |
| FD003 | 1 | ISO_POINT_M15_D1 | 13.97 | 12.97 | 5.56 | 13 | 0 | 12 |
| FD003 | 1 | ISO_POINT_M15_D2 | 14.32 | 13.32 | 5.72 | 13 | 2 | 10 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D1 | 37.80 | 36.80 | 17.57 | 0 | 0 | 0 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D2 | 36.93 | 35.93 | 17.09 | 0 | 0 | 0 |
| FD003 | 1 | RF_SLOPE_POINT_M15_D1 | 17.80 | 16.80 | 7.32 | 6 | 0 | 5 |
| FD003 | 1 | RF_SLOPE_POINT_M15_D2 | 17.90 | 16.90 | 7.37 | 7 | 0 | 5 |
| FD003 | 2 | AGE_D1 | 101.96 | 100.96 | 69.51 | 1 | 0 | 1 |
| FD003 | 2 | AGE_D2 | 101.96 | 100.96 | 69.51 | 1 | 0 | 1 |
| FD003 | 2 | HI_MARKER_D1 | 42.22 | 41.22 | 20.11 | 0 | 0 | 0 |
| FD003 | 2 | HI_MARKER_D2 | 41.22 | 40.22 | 19.53 | 0 | 0 | 0 |
| FD003 | 2 | HI_THRESHOLD_SELECTED_D1 | 29.32 | 28.32 | 13.00 | 2 | 0 | 2 |
| FD003 | 2 | HI_THRESHOLD_SELECTED_D2 | 29.17 | 28.17 | 12.92 | 2 | 0 | 2 |
| FD003 | 2 | HI_WAIT_SELECTED_D1 | 34.23 | 33.23 | 15.60 | 1 | 0 | 1 |
| FD003 | 2 | HI_WAIT_SELECTED_D2 | 33.54 | 32.54 | 15.23 | 1 | 0 | 1 |
| FD003 | 2 | ISO_LOWER98_M15_D1 | 41.50 | 40.50 | 19.69 | 0 | 0 | 0 |
| FD003 | 2 | ISO_LOWER98_M15_D2 | 40.62 | 39.62 | 19.18 | 0 | 0 | 0 |
| FD003 | 2 | ISO_POINT_M15_D1 | 14.84 | 13.84 | 5.96 | 17 | 0 | 15 |
| FD003 | 2 | ISO_POINT_M15_D2 | 15.81 | 14.81 | 6.40 | 13 | 2 | 7 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D1 | 41.73 | 40.73 | 19.82 | 0 | 0 | 0 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D2 | 40.75 | 39.75 | 19.25 | 0 | 0 | 0 |
| FD003 | 2 | RF_SLOPE_POINT_M15_D1 | 18.70 | 17.70 | 7.75 | 9 | 0 | 6 |
| FD003 | 2 | RF_SLOPE_POINT_M15_D2 | 19.17 | 18.17 | 7.97 | 8 | 3 | 5 |
| FD003 | 3 | AGE_D1 | 98.59 | 97.59 | 65.67 | 2 | 0 | 2 |
| FD003 | 3 | AGE_D2 | 98.59 | 97.59 | 65.67 | 2 | 1 | 1 |
| FD003 | 3 | HI_MARKER_D1 | 38.04 | 37.04 | 17.71 | 0 | 0 | 0 |
| FD003 | 3 | HI_MARKER_D2 | 37.04 | 36.04 | 17.15 | 0 | 0 | 0 |
| FD003 | 3 | HI_THRESHOLD_SELECTED_D1 | 26.67 | 25.67 | 11.64 | 2 | 0 | 1 |
| FD003 | 3 | HI_THRESHOLD_SELECTED_D2 | 27.63 | 26.63 | 12.13 | 0 | 0 | 0 |
| FD003 | 3 | HI_WAIT_SELECTED_D1 | 29.04 | 28.04 | 12.85 | 0 | 0 | 0 |
| FD003 | 3 | HI_WAIT_SELECTED_D2 | 28.64 | 27.64 | 12.65 | 0 | 0 | 0 |
| FD003 | 3 | ISO_LOWER98_M15_D1 | 38.04 | 37.04 | 17.71 | 0 | 0 | 0 |
| FD003 | 3 | ISO_LOWER98_M15_D2 | 37.04 | 36.04 | 17.15 | 0 | 0 | 0 |
| FD003 | 3 | ISO_POINT_M15_D1 | 13.73 | 12.73 | 5.45 | 12 | 0 | 10 |
| FD003 | 3 | ISO_POINT_M15_D2 | 13.45 | 12.45 | 5.33 | 10 | 0 | 8 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D1 | 37.80 | 36.80 | 17.57 | 0 | 0 | 0 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D2 | 36.80 | 35.80 | 17.02 | 0 | 0 | 0 |
| FD003 | 3 | RF_SLOPE_POINT_M15_D1 | 16.14 | 15.14 | 6.55 | 6 | 0 | 5 |
| FD003 | 3 | RF_SLOPE_POINT_M15_D2 | 16.00 | 15.00 | 6.49 | 6 | 1 | 5 |

## Antecedências diagnósticas de12/15 ciclos

Não alteram a reserva, o prazo de execução ou a política real. A parcela de detecção é comum às políticas com o mesmo acesso; idade é apenas contextual. As parcelas abaixo são proporções de motores (não percentuais do ganho sobre idade).

| Domínio | Repetição | d | ρ | Perda por sinal tardio | Perda por aquecimento | Atraso médio por acesso (ciclos) | A≤D /100 |
|---|---|---|---|---|---|---|---|
| FD001 | 1 | 1 | 12 | 1.0% | 0.0% | 0.02 | 99 |
| FD001 | 1 | 1 | 15 | 2.0% | 0.0% | 0.08 | 98 |
| FD001 | 1 | 2 | 12 | 2.0% | 0.0% | 0.04 | 98 |
| FD001 | 1 | 2 | 15 | 2.0% | 0.0% | 0.10 | 98 |
| FD001 | 2 | 1 | 12 | 0.0% | 0.0% | 0.00 | 100 |
| FD001 | 2 | 1 | 15 | 1.0% | 0.0% | 0.02 | 99 |
| FD001 | 2 | 2 | 12 | 0.0% | 0.0% | 0.00 | 100 |
| FD001 | 2 | 2 | 15 | 1.0% | 0.0% | 0.03 | 99 |
| FD001 | 3 | 1 | 12 | 0.0% | 0.0% | 0.00 | 100 |
| FD001 | 3 | 1 | 15 | 1.0% | 0.0% | 0.02 | 99 |
| FD001 | 3 | 2 | 12 | 0.0% | 0.0% | 0.00 | 100 |
| FD001 | 3 | 2 | 15 | 3.0% | 0.0% | 0.05 | 97 |
| FD003 | 1 | 1 | 12 | 0.0% | 0.0% | 0.00 | 100 |
| FD003 | 1 | 1 | 15 | 3.0% | 0.0% | 0.03 | 97 |
| FD003 | 1 | 2 | 12 | 0.0% | 0.0% | 0.00 | 100 |
| FD003 | 1 | 2 | 15 | 3.0% | 0.0% | 0.06 | 97 |
| FD003 | 2 | 1 | 12 | 1.0% | 0.0% | 0.03 | 99 |
| FD003 | 2 | 1 | 15 | 2.0% | 0.0% | 0.08 | 98 |
| FD003 | 2 | 2 | 12 | 1.0% | 0.0% | 0.04 | 99 |
| FD003 | 2 | 2 | 15 | 2.0% | 0.0% | 0.10 | 98 |
| FD003 | 3 | 1 | 12 | 0.0% | 0.0% | 0.00 | 100 |
| FD003 | 3 | 1 | 15 | 2.0% | 0.0% | 0.05 | 98 |
| FD003 | 3 | 2 | 12 | 1.0% | 0.0% | 0.01 | 99 |
| FD003 | 3 | 2 | 15 | 2.0% | 0.0% | 0.07 | 98 |

![Descarte adicional frente ao oráculo](excess_unused_life.png)

Barras: média das três repetições; segmentos: mínimo/máximo entre repetições, não intervalos de confiança. Limiar/espera selecionados têm eventos/ausências em alguns contrastes; menor descarte não significa maior admissibilidade.

![Perda de oportunidade por acesso tardio](access_loss.png)

As decomposições completas de oportunidade perdida J, atraso B, vida descartada W, custo e respectivos intervalos estão em [summary.csv](summary.csv). O escopo `feasible_access` é diagnóstico condicionado a A≤D, com contagem de excluídos; não substitui a população completa ou sustenta inferência de risco.

## Limites

Zero eventos observados não demonstra risco populacional ≤2%. Não há penalidade corretiva adicional; parcelas econômicas assinadas são preservadas. Um braço com ausência/chegada não se torna admissível por apresentar menor custo. As quatro escolhas P13.1 sem candidato interno viável continuam identificadas. O bootstrap de2.000 amostras é pareado por motor/domínio/repetição, condicionado aos modelos/seleções, sem reaprendizagem.

[Protocolo](../../protocolo_decomposicao_perda_11b.md), [verificação independente](verification.json), [componentes individuais](components.csv), [diagnósticos de previsão](diagnostics.csv) e [manifesto](manifest.json).
