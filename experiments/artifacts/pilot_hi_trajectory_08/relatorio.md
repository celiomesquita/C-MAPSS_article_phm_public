# P08 — trajetória do HI e atributos diretos dos sensores

Índice de saúde (HI) empírico congelado de P05/P06. Novos preditores de vida útil remanescente (RUL), cuja soma ao ciclo corrente prevê o F original. Regressão linear com penalização quadrática (Ridge) e floresta aleatória (RF); comparação da informação dentro de cada família. Sem alteração da fórmula HI, detecção de P, inspeções ou edição do artigo.

## Desenho e disponibilidade

Cinco folds por motor em cada subconjunto: HI previamente ajustado em F40, novos prognósticos ajustados em C20, seleção em S20 e avaliação em E20. No teste oficial, HI congelado a partir de F60 e prognóstico novamente ajustado somente em C20. São conjuntos já examinados; os resultados não são confirmação independente. A janela de 20 valores de HI só está disponível a partir do ciclo 39. Controles usam os mesmos ciclos. O primeiro cruzamento HI≤0,5 é preservado desde o ciclo 20, mesmo quando seus atributos temporais ainda não estão disponíveis.

Inclinação e curvatura são ajustes polinomiais locais; variabilidade é o desvio padrão amostral. SENSOR_RAW usa valores correntes com referência individual e escalas congeladas; SENSOR_MEAN usa médias de 15 ciclos; SENSOR_FULL acrescenta desvio padrão, raiz da média quadrática, assimetria, inclinação e curvatura. HI_FULL acrescenta inclinação, curvatura e variabilidade ao HI corrente. ISO_MATCHED é isotônico reajustado em C nos ciclos ≥39; ISO_FROZEN é o conversor anterior, que também usou ciclos 20–38.

## Primeiro marco HI≤0,5

Erro = F previsto menos endpoint real, em ciclos. RMSE = raiz do erro quadrático médio; MAE = erro absoluto médio. Viés positivo prevê F tarde. Métricas condicionais aos motores disponíveis; a antecipação real é retrospectiva, não informação observada pelo preditor.

| subset | dataset | method | total | available | no_crossing | early_window | rmse | mae | bias | actual_lead_median |
|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | complete | ISO_FROZEN | 100 | 100 | 0 | 0 | 17.85 | 14.12 | -0.18 | 39.50 |
| FD001 | complete | ISO_MATCHED | 100 | 100 | 0 | 0 | 17.82 | 14.05 | -0.47 | 39.50 |
| FD001 | complete | RF:HI | 100 | 100 | 0 | 0 | 18.69 | 15.08 | -0.52 | 39.50 |
| FD001 | complete | RF:HI_FULL | 100 | 100 | 0 | 0 | 16.98 | 13.11 | 1.62 | 39.50 |
| FD001 | complete | RF:SENSOR_FULL | 100 | 100 | 0 | 0 | 18.90 | 14.62 | 1.06 | 39.50 |
| FD001 | complete | RF:SENSOR_MEAN | 100 | 100 | 0 | 0 | 19.93 | 14.90 | 0.92 | 39.50 |
| FD001 | complete | RF:SENSOR_RAW | 100 | 100 | 0 | 0 | 20.38 | 15.02 | 1.48 | 39.50 |
| FD001 | complete | Ridge:HI | 100 | 100 | 0 | 0 | 25.18 | 22.04 | 17.52 | 39.50 |
| FD001 | complete | Ridge:HI_FULL | 100 | 100 | 0 | 0 | 25.70 | 21.80 | 19.32 | 39.50 |
| FD001 | complete | Ridge:SENSOR_FULL | 100 | 100 | 0 | 0 | 27.89 | 23.20 | 18.86 | 39.50 |
| FD001 | complete | Ridge:SENSOR_MEAN | 100 | 100 | 0 | 0 | 28.30 | 24.71 | 21.30 | 39.50 |
| FD001 | complete | Ridge:SENSOR_RAW | 100 | 100 | 0 | 0 | 27.07 | 23.53 | 19.02 | 39.50 |
| FD001 | truncated | ISO_FROZEN | 100 | 29 | 71 | 0 | 13.46 | 10.52 | 3.58 | 42.00 |
| FD001 | truncated | ISO_MATCHED | 100 | 29 | 71 | 0 | 13.38 | 10.41 | 3.14 | 42.00 |
| FD001 | truncated | RF:HI | 100 | 29 | 71 | 0 | 12.92 | 10.37 | 3.09 | 42.00 |
| FD001 | truncated | RF:HI_FULL | 100 | 29 | 71 | 0 | 12.01 | 9.68 | 5.06 | 42.00 |
| FD001 | truncated | RF:SENSOR_FULL | 100 | 29 | 71 | 0 | 14.73 | 10.36 | 3.07 | 42.00 |
| FD001 | truncated | RF:SENSOR_MEAN | 100 | 29 | 71 | 0 | 16.54 | 12.19 | 0.68 | 42.00 |
| FD001 | truncated | RF:SENSOR_RAW | 100 | 29 | 71 | 0 | 19.01 | 14.74 | 5.45 | 42.00 |
| FD001 | truncated | Ridge:HI | 100 | 29 | 71 | 0 | 26.79 | 24.56 | 23.05 | 42.00 |
| FD001 | truncated | Ridge:HI_FULL | 100 | 29 | 71 | 0 | 29.08 | 26.74 | 26.74 | 42.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | 100 | 29 | 71 | 0 | 34.33 | 32.55 | 32.21 | 42.00 |
| FD001 | truncated | Ridge:SENSOR_MEAN | 100 | 29 | 71 | 0 | 29.87 | 27.59 | 26.50 | 42.00 |
| FD001 | truncated | Ridge:SENSOR_RAW | 100 | 29 | 71 | 0 | 26.93 | 24.13 | 22.92 | 42.00 |
| FD003 | complete | ISO_FROZEN | 100 | 100 | 0 | 0 | 14.84 | 11.30 | -3.45 | 33.00 |
| FD003 | complete | ISO_MATCHED | 100 | 100 | 0 | 0 | 14.87 | 11.30 | -3.59 | 33.00 |
| FD003 | complete | RF:HI | 100 | 100 | 0 | 0 | 14.85 | 11.59 | -3.78 | 33.00 |
| FD003 | complete | RF:HI_FULL | 100 | 100 | 0 | 0 | 14.05 | 10.59 | -2.52 | 33.00 |
| FD003 | complete | RF:SENSOR_FULL | 100 | 100 | 0 | 0 | 14.40 | 11.07 | 0.46 | 33.00 |
| FD003 | complete | RF:SENSOR_MEAN | 100 | 100 | 0 | 0 | 16.44 | 12.40 | -0.87 | 33.00 |
| FD003 | complete | RF:SENSOR_RAW | 100 | 100 | 0 | 0 | 15.27 | 11.21 | -1.41 | 33.00 |
| FD003 | complete | Ridge:HI | 100 | 100 | 0 | 0 | 20.37 | 17.29 | 13.05 | 33.00 |
| FD003 | complete | Ridge:HI_FULL | 100 | 100 | 0 | 0 | 20.67 | 17.01 | 14.78 | 33.00 |
| FD003 | complete | Ridge:SENSOR_FULL | 100 | 100 | 0 | 0 | 29.78 | 23.40 | 18.72 | 33.00 |
| FD003 | complete | Ridge:SENSOR_MEAN | 100 | 100 | 0 | 0 | 23.96 | 19.72 | 12.34 | 33.00 |
| FD003 | complete | Ridge:SENSOR_RAW | 100 | 100 | 0 | 0 | 21.16 | 17.75 | 7.37 | 33.00 |
| FD003 | truncated | ISO_FROZEN | 100 | 22 | 78 | 0 | 15.87 | 11.92 | -6.31 | 37.00 |
| FD003 | truncated | ISO_MATCHED | 100 | 22 | 78 | 0 | 15.95 | 11.97 | -6.51 | 37.00 |
| FD003 | truncated | RF:HI | 100 | 22 | 78 | 0 | 16.27 | 12.13 | -5.29 | 37.00 |
| FD003 | truncated | RF:HI_FULL | 100 | 22 | 78 | 0 | 15.14 | 11.57 | -4.97 | 37.00 |
| FD003 | truncated | RF:SENSOR_FULL | 100 | 22 | 78 | 0 | 11.21 | 8.28 | -4.32 | 37.00 |
| FD003 | truncated | RF:SENSOR_MEAN | 100 | 22 | 78 | 0 | 15.69 | 12.59 | -7.05 | 37.00 |
| FD003 | truncated | RF:SENSOR_RAW | 100 | 22 | 78 | 0 | 16.05 | 11.86 | -8.43 | 37.00 |
| FD003 | truncated | Ridge:HI | 100 | 22 | 78 | 0 | 16.68 | 14.14 | 8.20 | 37.00 |
| FD003 | truncated | Ridge:HI_FULL | 100 | 22 | 78 | 0 | 17.00 | 14.40 | 10.31 | 37.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | 100 | 22 | 78 | 0 | 18.57 | 15.52 | 8.14 | 37.00 |
| FD003 | truncated | Ridge:SENSOR_MEAN | 100 | 22 | 78 | 0 | 18.70 | 15.48 | 7.98 | 37.00 |
| FD003 | truncated | Ridge:SENSOR_RAW | 100 | 22 | 78 | 0 | 16.83 | 14.51 | 2.74 | 37.00 |

## Contrastes principais no marco

Diferença = RMSE B−A; valores negativos favorecem B. Intervalos descritivos de 95% por 2.000 reamostragens pareadas de motores, sem garantia confirmatória ou preditiva individual. Todos os métodos usam a mesma passagem de HI e os mesmos motores/ciclos disponíveis.

| subset | dataset | method_a | method_b | common | rmse_a | rmse_b | delta_rmse | ci_low | ci_high |
|---|---|---|---|---|---|---|---|---|---|
| FD001 | complete | Ridge:HI | Ridge:HI_FULL | 100 | 25.18 | 25.70 | 0.52 | -1.09 | 2.35 |
| FD001 | complete | Ridge:SENSOR_RAW | Ridge:SENSOR_MEAN | 100 | 27.07 | 28.30 | 1.24 | -0.15 | 2.69 |
| FD001 | complete | Ridge:SENSOR_MEAN | Ridge:SENSOR_FULL | 100 | 28.30 | 27.89 | -0.41 | -2.06 | 1.13 |
| FD001 | complete | Ridge:HI_FULL | Ridge:SENSOR_FULL | 100 | 25.70 | 27.89 | 2.19 | 0.00 | 4.21 |
| FD001 | complete | RF:HI | RF:HI_FULL | 100 | 18.69 | 16.98 | -1.71 | -3.94 | 0.63 |
| FD001 | complete | RF:SENSOR_RAW | RF:SENSOR_MEAN | 100 | 20.38 | 19.93 | -0.46 | -3.47 | 2.33 |
| FD001 | complete | RF:SENSOR_MEAN | RF:SENSOR_FULL | 100 | 19.93 | 18.90 | -1.02 | -2.16 | 0.12 |
| FD001 | complete | RF:HI_FULL | RF:SENSOR_FULL | 100 | 16.98 | 18.90 | 1.92 | -0.74 | 4.38 |
| FD001 | truncated | Ridge:HI | Ridge:HI_FULL | 29 | 26.79 | 29.08 | 2.30 | -0.28 | 4.81 |
| FD001 | truncated | Ridge:SENSOR_RAW | Ridge:SENSOR_MEAN | 29 | 26.93 | 29.87 | 2.94 | 0.03 | 5.70 |
| FD001 | truncated | Ridge:SENSOR_MEAN | Ridge:SENSOR_FULL | 29 | 29.87 | 34.33 | 4.46 | 2.92 | 5.91 |
| FD001 | truncated | Ridge:HI_FULL | Ridge:SENSOR_FULL | 29 | 29.08 | 34.33 | 5.24 | 3.69 | 6.88 |
| FD001 | truncated | RF:HI | RF:HI_FULL | 29 | 12.92 | 12.01 | -0.91 | -5.53 | 3.51 |
| FD001 | truncated | RF:SENSOR_RAW | RF:SENSOR_MEAN | 29 | 19.01 | 16.54 | -2.47 | -6.43 | 0.85 |
| FD001 | truncated | RF:SENSOR_MEAN | RF:SENSOR_FULL | 29 | 16.54 | 14.73 | -1.81 | -3.72 | 0.09 |
| FD001 | truncated | RF:HI_FULL | RF:SENSOR_FULL | 29 | 12.01 | 14.73 | 2.72 | -1.86 | 7.85 |
| FD003 | complete | Ridge:HI | Ridge:HI_FULL | 100 | 20.37 | 20.67 | 0.31 | -2.34 | 3.05 |
| FD003 | complete | Ridge:SENSOR_RAW | Ridge:SENSOR_MEAN | 100 | 21.16 | 23.96 | 2.80 | 0.29 | 5.44 |
| FD003 | complete | Ridge:SENSOR_MEAN | Ridge:SENSOR_FULL | 100 | 23.96 | 29.78 | 5.82 | 3.25 | 8.32 |
| FD003 | complete | Ridge:HI_FULL | Ridge:SENSOR_FULL | 100 | 20.67 | 29.78 | 9.11 | 5.65 | 12.44 |
| FD003 | complete | RF:HI | RF:HI_FULL | 100 | 14.85 | 14.05 | -0.80 | -1.79 | 0.20 |
| FD003 | complete | RF:SENSOR_RAW | RF:SENSOR_MEAN | 100 | 15.27 | 16.44 | 1.17 | -0.32 | 2.63 |
| FD003 | complete | RF:SENSOR_MEAN | RF:SENSOR_FULL | 100 | 16.44 | 14.40 | -2.04 | -3.63 | -0.42 |
| FD003 | complete | RF:HI_FULL | RF:SENSOR_FULL | 100 | 14.05 | 14.40 | 0.35 | -1.31 | 2.27 |
| FD003 | truncated | Ridge:HI | Ridge:HI_FULL | 22 | 16.68 | 17.00 | 0.32 | -3.34 | 3.61 |
| FD003 | truncated | Ridge:SENSOR_RAW | Ridge:SENSOR_MEAN | 22 | 16.83 | 18.70 | 1.87 | -3.07 | 6.17 |
| FD003 | truncated | Ridge:SENSOR_MEAN | Ridge:SENSOR_FULL | 22 | 18.70 | 18.57 | -0.13 | -2.77 | 2.13 |
| FD003 | truncated | Ridge:HI_FULL | Ridge:SENSOR_FULL | 22 | 17.00 | 18.57 | 1.56 | -2.63 | 5.45 |
| FD003 | truncated | RF:HI | RF:HI_FULL | 22 | 16.27 | 15.14 | -1.13 | -4.69 | 1.56 |
| FD003 | truncated | RF:SENSOR_RAW | RF:SENSOR_MEAN | 22 | 16.05 | 15.69 | -0.36 | -3.00 | 2.47 |
| FD003 | truncated | RF:SENSOR_MEAN | RF:SENSOR_FULL | 22 | 15.69 | 11.21 | -4.48 | -8.23 | -1.98 |
| FD003 | truncated | RF:HI_FULL | RF:SENSOR_FULL | 22 | 15.14 | 11.21 | -3.92 | -6.30 | -1.18 |

![Contrastes pareados de informação](paired_effects.png)

## Ablações do HI — trajetórias completas

Omissões e adições são ajustadas novamente, mantendo família, motores e ciclos. A penalização Ridge pode mudar pela seleção em S; RF mantém a mesma configuração em todas as representações.

| subset | dataset | method_a | method_b | common | rmse_a | rmse_b | delta_rmse | ci_low | ci_high |
|---|---|---|---|---|---|---|---|---|---|
| FD001 | complete | Ridge:HI | Ridge:HI_FULL | 100 | 25.18 | 25.70 | 0.52 | -1.09 | 2.35 |
| FD001 | complete | Ridge:HI_SLOPE | Ridge:HI_FULL | 100 | 26.85 | 25.70 | -1.14 | -1.72 | -0.61 |
| FD001 | complete | Ridge:HI_CURV | Ridge:HI_FULL | 100 | 24.49 | 25.70 | 1.21 | -0.58 | 3.12 |
| FD001 | complete | Ridge:HI_STD | Ridge:HI_FULL | 100 | 27.32 | 25.70 | -1.62 | -2.26 | -1.01 |
| FD001 | complete | Ridge:HI_NO_SLOPE | Ridge:HI_FULL | 100 | 27.04 | 25.70 | -1.34 | -2.03 | -0.61 |
| FD001 | complete | Ridge:HI_NO_CURV | Ridge:HI_FULL | 100 | 25.58 | 25.70 | 0.12 | -0.08 | 0.34 |
| FD001 | complete | Ridge:HI_NO_STD | Ridge:HI_FULL | 100 | 26.56 | 25.70 | -0.86 | -1.47 | -0.23 |
| FD001 | complete | RF:HI | RF:HI_FULL | 100 | 18.69 | 16.98 | -1.71 | -3.94 | 0.63 |
| FD001 | complete | RF:HI_SLOPE | RF:HI_FULL | 100 | 16.67 | 16.98 | 0.31 | -0.43 | 1.10 |
| FD001 | complete | RF:HI_CURV | RF:HI_FULL | 100 | 18.23 | 16.98 | -1.25 | -3.43 | 1.13 |
| FD001 | complete | RF:HI_STD | RF:HI_FULL | 100 | 17.12 | 16.98 | -0.14 | -1.21 | 0.94 |
| FD001 | complete | RF:HI_NO_SLOPE | RF:HI_FULL | 100 | 17.28 | 16.98 | -0.30 | -0.70 | 0.02 |
| FD001 | complete | RF:HI_NO_CURV | RF:HI_FULL | 100 | 16.67 | 16.98 | 0.31 | -0.37 | 1.08 |
| FD001 | complete | RF:HI_NO_STD | RF:HI_FULL | 100 | 16.91 | 16.98 | 0.07 | -0.28 | 0.50 |
| FD003 | complete | Ridge:HI | Ridge:HI_FULL | 100 | 20.37 | 20.67 | 0.31 | -2.34 | 3.05 |
| FD003 | complete | Ridge:HI_SLOPE | Ridge:HI_FULL | 100 | 22.14 | 20.67 | -1.47 | -2.60 | -0.34 |
| FD003 | complete | Ridge:HI_CURV | Ridge:HI_FULL | 100 | 19.67 | 20.67 | 1.00 | -1.50 | 3.72 |
| FD003 | complete | Ridge:HI_STD | Ridge:HI_FULL | 100 | 22.71 | 20.67 | -2.04 | -3.18 | -0.94 |
| FD003 | complete | Ridge:HI_NO_SLOPE | Ridge:HI_FULL | 100 | 22.13 | 20.67 | -1.46 | -2.48 | -0.46 |
| FD003 | complete | Ridge:HI_NO_CURV | Ridge:HI_FULL | 100 | 21.12 | 20.67 | -0.44 | -0.73 | -0.12 |
| FD003 | complete | Ridge:HI_NO_STD | Ridge:HI_FULL | 100 | 21.57 | 20.67 | -0.90 | -1.89 | 0.10 |
| FD003 | complete | RF:HI | RF:HI_FULL | 100 | 14.85 | 14.05 | -0.80 | -1.79 | 0.20 |
| FD003 | complete | RF:HI_SLOPE | RF:HI_FULL | 100 | 14.00 | 14.05 | 0.04 | -0.57 | 0.71 |
| FD003 | complete | RF:HI_CURV | RF:HI_FULL | 100 | 15.19 | 14.05 | -1.14 | -2.00 | -0.22 |
| FD003 | complete | RF:HI_STD | RF:HI_FULL | 100 | 13.82 | 14.05 | 0.22 | -0.32 | 0.85 |
| FD003 | complete | RF:HI_NO_SLOPE | RF:HI_FULL | 100 | 14.08 | 14.05 | -0.03 | -0.16 | 0.12 |
| FD003 | complete | RF:HI_NO_CURV | RF:HI_FULL | 100 | 13.89 | 14.05 | 0.16 | -0.43 | 0.85 |
| FD003 | complete | RF:HI_NO_STD | RF:HI_FULL | 100 | 14.18 | 14.05 | -0.14 | -0.23 | -0.04 |

## Atualizações e teste na última observação

| subset | dataset | event | method | total | available | rmse | bias |
|---|---|---|---|---|---|---|---|
| FD001 | complete | plus5 | ISO_FROZEN | 100 | 100 | 17.11 | 0.31 |
| FD001 | complete | plus5 | ISO_MATCHED | 100 | 100 | 17.08 | 0.04 |
| FD001 | complete | plus5 | RF:HI | 100 | 100 | 17.41 | -0.19 |
| FD001 | complete | plus5 | RF:HI_FULL | 100 | 100 | 16.57 | 0.04 |
| FD001 | complete | plus5 | RF:SENSOR_FULL | 100 | 100 | 18.34 | 0.18 |
| FD001 | complete | plus5 | RF:SENSOR_MEAN | 100 | 100 | 19.04 | 0.38 |
| FD001 | complete | plus5 | RF:SENSOR_RAW | 100 | 100 | 19.81 | 3.05 |
| FD001 | complete | plus5 | Ridge:HI | 100 | 100 | 22.07 | 14.43 |
| FD001 | complete | plus5 | Ridge:HI_FULL | 100 | 100 | 21.53 | 14.93 |
| FD001 | complete | plus5 | Ridge:SENSOR_FULL | 100 | 100 | 26.02 | 16.34 |
| FD001 | complete | plus5 | Ridge:SENSOR_MEAN | 100 | 100 | 26.33 | 18.66 |
| FD001 | complete | plus5 | Ridge:SENSOR_RAW | 100 | 100 | 28.57 | 19.54 |
| FD001 | truncated | last | ISO_FROZEN | 100 | 97 | 26.87 | 9.00 |
| FD001 | truncated | plus5 | ISO_FROZEN | 100 | 25 | 12.76 | 1.82 |
| FD001 | truncated | last | ISO_MATCHED | 100 | 97 | 25.23 | 7.69 |
| FD001 | truncated | plus5 | ISO_MATCHED | 100 | 25 | 12.72 | 1.47 |
| FD001 | truncated | last | RF:HI | 100 | 97 | 28.22 | 9.71 |
| FD001 | truncated | plus5 | RF:HI | 100 | 25 | 15.04 | 3.16 |
| FD001 | truncated | last | RF:HI_FULL | 100 | 97 | 28.68 | 11.20 |
| FD001 | truncated | plus5 | RF:HI_FULL | 100 | 25 | 14.64 | -1.56 |
| FD001 | truncated | last | RF:SENSOR_FULL | 100 | 97 | 32.36 | 15.56 |
| FD001 | truncated | plus5 | RF:SENSOR_FULL | 100 | 25 | 13.11 | -0.44 |
| FD001 | truncated | last | RF:SENSOR_MEAN | 100 | 97 | 30.10 | 13.48 |
| FD001 | truncated | plus5 | RF:SENSOR_MEAN | 100 | 25 | 15.18 | -2.15 |
| FD001 | truncated | last | RF:SENSOR_RAW | 100 | 97 | 25.40 | 11.81 |
| FD001 | truncated | plus5 | RF:SENSOR_RAW | 100 | 25 | 18.09 | 3.77 |
| FD001 | truncated | last | Ridge:HI | 100 | 97 | 22.95 | 12.57 |
| FD001 | truncated | plus5 | Ridge:HI | 100 | 25 | 21.06 | 17.26 |
| FD001 | truncated | last | Ridge:HI_FULL | 100 | 97 | 22.18 | 12.44 |
| FD001 | truncated | plus5 | Ridge:HI_FULL | 100 | 25 | 24.34 | 20.49 |
| FD001 | truncated | last | Ridge:SENSOR_FULL | 100 | 97 | 23.55 | 13.52 |
| FD001 | truncated | plus5 | Ridge:SENSOR_FULL | 100 | 25 | 29.83 | 27.67 |
| FD001 | truncated | last | Ridge:SENSOR_MEAN | 100 | 97 | 23.42 | 13.68 |
| FD001 | truncated | plus5 | Ridge:SENSOR_MEAN | 100 | 25 | 24.72 | 21.50 |
| FD001 | truncated | last | Ridge:SENSOR_RAW | 100 | 97 | 23.03 | 11.69 |
| FD001 | truncated | plus5 | Ridge:SENSOR_RAW | 100 | 25 | 26.10 | 22.84 |
| FD003 | complete | plus5 | ISO_FROZEN | 100 | 100 | 14.31 | -4.06 |
| FD003 | complete | plus5 | ISO_MATCHED | 100 | 100 | 14.35 | -4.20 |
| FD003 | complete | plus5 | RF:HI | 100 | 100 | 14.44 | -4.02 |
| FD003 | complete | plus5 | RF:HI_FULL | 100 | 100 | 14.05 | -3.38 |
| FD003 | complete | plus5 | RF:SENSOR_FULL | 100 | 100 | 13.95 | -0.80 |
| FD003 | complete | plus5 | RF:SENSOR_MEAN | 100 | 100 | 16.06 | -0.63 |
| FD003 | complete | plus5 | RF:SENSOR_RAW | 100 | 100 | 14.30 | 0.96 |
| FD003 | complete | plus5 | Ridge:HI | 100 | 100 | 15.95 | 6.77 |
| FD003 | complete | plus5 | Ridge:HI_FULL | 100 | 100 | 18.16 | 7.06 |
| FD003 | complete | plus5 | Ridge:SENSOR_FULL | 100 | 100 | 27.60 | 14.17 |
| FD003 | complete | plus5 | Ridge:SENSOR_MEAN | 100 | 100 | 21.59 | 7.05 |
| FD003 | complete | plus5 | Ridge:SENSOR_RAW | 100 | 100 | 20.93 | 8.26 |
| FD003 | truncated | last | ISO_FROZEN | 100 | 99 | 23.44 | -2.37 |
| FD003 | truncated | plus5 | ISO_FROZEN | 100 | 20 | 15.22 | -7.75 |
| FD003 | truncated | last | ISO_MATCHED | 100 | 99 | 22.89 | -3.18 |
| FD003 | truncated | plus5 | ISO_MATCHED | 100 | 20 | 15.29 | -7.88 |
| FD003 | truncated | last | RF:HI | 100 | 99 | 24.80 | -1.16 |
| FD003 | truncated | plus5 | RF:HI | 100 | 20 | 15.52 | -5.86 |
| FD003 | truncated | last | RF:HI_FULL | 100 | 99 | 25.04 | -0.09 |
| FD003 | truncated | plus5 | RF:HI_FULL | 100 | 20 | 10.62 | -4.54 |
| FD003 | truncated | last | RF:SENSOR_FULL | 100 | 99 | 24.50 | 1.47 |
| FD003 | truncated | plus5 | RF:SENSOR_FULL | 100 | 20 | 10.57 | -5.39 |
| FD003 | truncated | last | RF:SENSOR_MEAN | 100 | 99 | 26.17 | -0.91 |
| FD003 | truncated | plus5 | RF:SENSOR_MEAN | 100 | 20 | 14.23 | -7.96 |
| FD003 | truncated | last | RF:SENSOR_RAW | 100 | 99 | 34.01 | 8.68 |
| FD003 | truncated | plus5 | RF:SENSOR_RAW | 100 | 20 | 12.08 | -6.76 |
| FD003 | truncated | last | Ridge:HI | 100 | 99 | 20.40 | 6.01 |
| FD003 | truncated | plus5 | Ridge:HI | 100 | 20 | 12.43 | 3.96 |
| FD003 | truncated | last | Ridge:HI_FULL | 100 | 99 | 21.17 | 7.76 |
| FD003 | truncated | plus5 | Ridge:HI_FULL | 100 | 20 | 9.71 | 4.95 |
| FD003 | truncated | last | Ridge:SENSOR_FULL | 100 | 99 | 23.23 | 6.71 |
| FD003 | truncated | plus5 | Ridge:SENSOR_FULL | 100 | 20 | 15.06 | 2.46 |
| FD003 | truncated | last | Ridge:SENSOR_MEAN | 100 | 99 | 21.29 | 5.12 |
| FD003 | truncated | plus5 | Ridge:SENSOR_MEAN | 100 | 20 | 16.34 | 3.88 |
| FD003 | truncated | last | Ridge:SENSOR_RAW | 100 | 99 | 25.40 | 9.33 |
| FD003 | truncated | plus5 | Ridge:SENSOR_RAW | 100 | 20 | 12.60 | 5.34 |

## Dependência dos atributos e estabilidade

Vinte permutações entre motores do mesmo fold ou teste, no marco 0,5. Todos os atributos de cada sensor são permutados juntos. Para HI_FULL, os quatro grupos são permutados separadamente. A tabela resume variação média de erro quadrático por grupo nos folds ou no teste; folds têm a mesma ponderação. Valores negativos são preservados.

| subset | dataset | method | group | mean_delta_mse | mean_rank |
|---|---|---|---|---|---|
| FD001 | complete | RF:HI_FULL | h_curv | 10.05 | 2.60 |
| FD001 | complete | RF:HI_FULL | h_slope | 17.10 | 2.80 |
| FD001 | complete | RF:HI_FULL | h_std | 31.99 | 1.80 |
| FD001 | complete | RF:HI_FULL | hi | 1.98 | 2.80 |
| FD001 | complete | RF:SENSOR_FULL | s11 | -2.73 | 12.00 |
| FD001 | complete | RF:SENSOR_FULL | s12 | 2.89 | 5.80 |
| FD001 | complete | RF:SENSOR_FULL | s13 | 3.90 | 8.40 |
| FD001 | complete | RF:SENSOR_FULL | s14 | 34.04 | 6.20 |
| FD001 | complete | RF:SENSOR_FULL | s15 | -5.31 | 8.80 |
| FD001 | complete | RF:SENSOR_FULL | s17 | 1.66 | 8.60 |
| FD001 | complete | RF:SENSOR_FULL | s2 | 10.32 | 8.00 |
| FD001 | complete | RF:SENSOR_FULL | s20 | 12.03 | 5.20 |
| FD001 | complete | RF:SENSOR_FULL | s21 | 5.60 | 6.60 |
| FD001 | complete | RF:SENSOR_FULL | s3 | -0.87 | 11.40 |
| FD001 | complete | RF:SENSOR_FULL | s4 | 24.23 | 5.20 |
| FD001 | complete | RF:SENSOR_FULL | s7 | 14.41 | 5.60 |
| FD001 | complete | RF:SENSOR_FULL | s8 | -5.64 | 10.00 |
| FD001 | complete | RF:SENSOR_FULL | s9 | 18.02 | 3.20 |
| FD001 | complete | Ridge:HI_FULL | h_curv | 2.26 | 3.00 |
| FD001 | complete | Ridge:HI_FULL | h_slope | 26.33 | 1.80 |
| FD001 | complete | Ridge:HI_FULL | h_std | 27.04 | 2.40 |
| FD001 | complete | Ridge:HI_FULL | hi | 1.71 | 2.80 |
| FD001 | complete | Ridge:SENSOR_FULL | s11 | 12.12 | 7.00 |
| FD001 | complete | Ridge:SENSOR_FULL | s12 | 12.73 | 5.20 |
| FD001 | complete | Ridge:SENSOR_FULL | s13 | 2.89 | 9.60 |
| FD001 | complete | Ridge:SENSOR_FULL | s14 | 34.85 | 3.40 |
| FD001 | complete | Ridge:SENSOR_FULL | s15 | 3.28 | 10.00 |
| FD001 | complete | Ridge:SENSOR_FULL | s17 | 10.80 | 6.60 |
| FD001 | complete | Ridge:SENSOR_FULL | s2 | 12.41 | 8.40 |
| FD001 | complete | Ridge:SENSOR_FULL | s20 | 1.79 | 8.60 |
| FD001 | complete | Ridge:SENSOR_FULL | s21 | 9.60 | 6.80 |
| FD001 | complete | Ridge:SENSOR_FULL | s3 | -7.42 | 11.00 |
| FD001 | complete | Ridge:SENSOR_FULL | s4 | 0.82 | 8.80 |
| FD001 | complete | Ridge:SENSOR_FULL | s7 | 21.91 | 5.40 |
| FD001 | complete | Ridge:SENSOR_FULL | s8 | -3.73 | 8.60 |
| FD001 | complete | Ridge:SENSOR_FULL | s9 | 14.24 | 5.60 |
| FD001 | truncated | RF:HI_FULL | h_curv | 18.51 | 3.00 |
| FD001 | truncated | RF:HI_FULL | h_slope | 21.16 | 2.00 |
| FD001 | truncated | RF:HI_FULL | h_std | 74.01 | 1.00 |
| FD001 | truncated | RF:HI_FULL | hi | 16.15 | 4.00 |
| FD001 | truncated | RF:SENSOR_FULL | s11 | 6.18 | 5.00 |
| FD001 | truncated | RF:SENSOR_FULL | s12 | 1.03 | 10.00 |
| FD001 | truncated | RF:SENSOR_FULL | s13 | 5.54 | 6.00 |
| FD001 | truncated | RF:SENSOR_FULL | s14 | 70.40 | 2.00 |
| FD001 | truncated | RF:SENSOR_FULL | s15 | -0.35 | 11.00 |
| FD001 | truncated | RF:SENSOR_FULL | s17 | -1.80 | 12.00 |
| FD001 | truncated | RF:SENSOR_FULL | s2 | 3.56 | 8.00 |
| FD001 | truncated | RF:SENSOR_FULL | s20 | 4.19 | 7.00 |
| FD001 | truncated | RF:SENSOR_FULL | s21 | 9.34 | 4.00 |
| FD001 | truncated | RF:SENSOR_FULL | s3 | 2.47 | 9.00 |
| FD001 | truncated | RF:SENSOR_FULL | s4 | 20.08 | 3.00 |
| FD001 | truncated | RF:SENSOR_FULL | s7 | -5.18 | 14.00 |
| FD001 | truncated | RF:SENSOR_FULL | s8 | -2.54 | 13.00 |
| FD001 | truncated | RF:SENSOR_FULL | s9 | 76.58 | 1.00 |
| FD001 | truncated | Ridge:HI_FULL | h_curv | -5.45 | 4.00 |
| FD001 | truncated | Ridge:HI_FULL | h_slope | 46.04 | 1.00 |
| FD001 | truncated | Ridge:HI_FULL | h_std | 29.07 | 2.00 |
| FD001 | truncated | Ridge:HI_FULL | hi | 0.09 | 3.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s11 | 5.06 | 7.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s12 | 8.28 | 6.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s13 | 4.39 | 8.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s14 | 14.59 | 4.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s15 | -4.88 | 14.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s17 | 17.57 | 3.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s2 | 0.45 | 11.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s20 | -2.70 | 12.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s21 | 1.90 | 10.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s3 | 8.96 | 5.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s4 | 21.61 | 2.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s7 | -3.04 | 13.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s8 | 3.65 | 9.00 |
| FD001 | truncated | Ridge:SENSOR_FULL | s9 | 23.59 | 1.00 |
| FD003 | complete | RF:HI_FULL | h_curv | -4.36 | 3.00 |
| FD003 | complete | RF:HI_FULL | h_slope | 21.30 | 2.20 |
| FD003 | complete | RF:HI_FULL | h_std | 3.96 | 2.40 |
| FD003 | complete | RF:HI_FULL | hi | 3.01 | 2.40 |
| FD003 | complete | RF:SENSOR_FULL | s11 | 1.83 | 7.60 |
| FD003 | complete | RF:SENSOR_FULL | s12 | 1.16 | 6.00 |
| FD003 | complete | RF:SENSOR_FULL | s13 | -4.44 | 10.20 |
| FD003 | complete | RF:SENSOR_FULL | s14 | 17.49 | 4.00 |
| FD003 | complete | RF:SENSOR_FULL | s15 | 10.42 | 5.20 |
| FD003 | complete | RF:SENSOR_FULL | s17 | 2.72 | 8.20 |
| FD003 | complete | RF:SENSOR_FULL | s2 | 6.92 | 5.60 |
| FD003 | complete | RF:SENSOR_FULL | s20 | -0.45 | 9.20 |
| FD003 | complete | RF:SENSOR_FULL | s21 | -1.12 | 10.60 |
| FD003 | complete | RF:SENSOR_FULL | s3 | 0.17 | 8.60 |
| FD003 | complete | RF:SENSOR_FULL | s4 | 11.66 | 6.80 |
| FD003 | complete | RF:SENSOR_FULL | s6 | 17.96 | 6.00 |
| FD003 | complete | RF:SENSOR_FULL | s7 | -17.72 | 9.40 |
| FD003 | complete | RF:SENSOR_FULL | s8 | -4.74 | 10.20 |
| FD003 | complete | RF:SENSOR_FULL | s9 | 28.62 | 5.20 |
| FD003 | complete | Ridge:HI_FULL | h_curv | -0.26 | 2.80 |
| FD003 | complete | Ridge:HI_FULL | h_slope | 58.24 | 1.40 |
| FD003 | complete | Ridge:HI_FULL | h_std | 22.10 | 2.40 |
| FD003 | complete | Ridge:HI_FULL | hi | -1.07 | 3.40 |
| FD003 | complete | Ridge:SENSOR_FULL | s11 | -9.04 | 8.80 |
| FD003 | complete | Ridge:SENSOR_FULL | s12 | 58.44 | 7.40 |
| FD003 | complete | Ridge:SENSOR_FULL | s13 | -17.86 | 12.00 |
| FD003 | complete | Ridge:SENSOR_FULL | s14 | -29.45 | 10.60 |
| FD003 | complete | Ridge:SENSOR_FULL | s15 | 95.41 | 3.80 |
| FD003 | complete | Ridge:SENSOR_FULL | s17 | -15.02 | 10.00 |
| FD003 | complete | Ridge:SENSOR_FULL | s2 | 11.85 | 6.00 |
| FD003 | complete | Ridge:SENSOR_FULL | s20 | 241.04 | 1.80 |
| FD003 | complete | Ridge:SENSOR_FULL | s21 | 256.43 | 3.40 |
| FD003 | complete | Ridge:SENSOR_FULL | s3 | -19.76 | 10.00 |
| FD003 | complete | Ridge:SENSOR_FULL | s4 | 22.01 | 5.60 |
| FD003 | complete | Ridge:SENSOR_FULL | s6 | 54.42 | 1.00 |
| FD003 | complete | Ridge:SENSOR_FULL | s7 | 89.08 | 7.20 |
| FD003 | complete | Ridge:SENSOR_FULL | s8 | -41.35 | 12.40 |
| FD003 | complete | Ridge:SENSOR_FULL | s9 | -9.81 | 8.80 |
| FD003 | truncated | RF:HI_FULL | h_curv | -33.43 | 4.00 |
| FD003 | truncated | RF:HI_FULL | h_slope | 46.59 | 1.00 |
| FD003 | truncated | RF:HI_FULL | h_std | -14.46 | 3.00 |
| FD003 | truncated | RF:HI_FULL | hi | -0.45 | 2.00 |
| FD003 | truncated | RF:SENSOR_FULL | s11 | 21.96 | 3.00 |
| FD003 | truncated | RF:SENSOR_FULL | s12 | 7.01 | 4.00 |
| FD003 | truncated | RF:SENSOR_FULL | s13 | 0.98 | 11.00 |
| FD003 | truncated | RF:SENSOR_FULL | s14 | 41.79 | 2.00 |
| FD003 | truncated | RF:SENSOR_FULL | s15 | 0.74 | 12.00 |
| FD003 | truncated | RF:SENSOR_FULL | s17 | 2.10 | 8.00 |
| FD003 | truncated | RF:SENSOR_FULL | s2 | 1.90 | 9.00 |
| FD003 | truncated | RF:SENSOR_FULL | s20 | -0.89 | 14.00 |
| FD003 | truncated | RF:SENSOR_FULL | s21 | 3.36 | 6.00 |
| FD003 | truncated | RF:SENSOR_FULL | s3 | 0.41 | 13.00 |
| FD003 | truncated | RF:SENSOR_FULL | s4 | 65.74 | 1.00 |
| FD003 | truncated | RF:SENSOR_FULL | s7 | 5.57 | 5.00 |
| FD003 | truncated | RF:SENSOR_FULL | s8 | 2.74 | 7.00 |
| FD003 | truncated | RF:SENSOR_FULL | s9 | 1.59 | 10.00 |
| FD003 | truncated | Ridge:HI_FULL | h_curv | 5.34 | 3.00 |
| FD003 | truncated | Ridge:HI_FULL | h_slope | 10.76 | 2.00 |
| FD003 | truncated | Ridge:HI_FULL | h_std | 18.15 | 1.00 |
| FD003 | truncated | Ridge:HI_FULL | hi | -1.96 | 4.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s11 | -3.23 | 9.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s12 | 50.49 | 3.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s13 | -45.22 | 14.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s14 | -17.13 | 11.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s15 | 20.29 | 7.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s17 | 4.76 | 8.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s2 | -21.15 | 12.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s20 | 94.83 | 1.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s21 | 25.19 | 6.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s3 | -15.75 | 10.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s4 | 62.35 | 2.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s7 | 38.54 | 5.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s8 | -44.89 | 13.00 |
| FD003 | truncated | Ridge:SENSOR_FULL | s9 | 48.18 | 4.00 |

Concordância abaixo é correlação de Spearman de ranks entre famílias no mesmo fold/teste e entre folds da mesma família; estatística descritiva sobre poucos grupos e partições dependentes.

| subset | dataset | representation | comparison | pairs | valid | median_spearman | min_spearman | max_spearman |
|---|---|---|---|---|---|---|---|---|
| FD001 | complete | HI_FULL | between_algorithms | 5 | 5 | 0.60 | -0.40 | 1.00 |
| FD001 | complete | HI_FULL | between_folds | 20 | 20 | -0.20 | -1.00 | 0.80 |
| FD001 | complete | SENSOR_FULL | between_algorithms | 5 | 5 | 0.44 | 0.06 | 0.61 |
| FD001 | complete | SENSOR_FULL | between_folds | 20 | 20 | 0.09 | -0.29 | 0.54 |
| FD001 | truncated | HI_FULL | between_algorithms | 1 | 1 | 0.60 | 0.60 | 0.60 |
| FD001 | truncated | SENSOR_FULL | between_algorithms | 1 | 1 | 0.51 | 0.51 | 0.51 |
| FD003 | complete | HI_FULL | between_algorithms | 5 | 5 | 0.20 | 0.00 | 1.00 |
| FD003 | complete | HI_FULL | between_folds | 20 | 20 | 0.10 | -1.00 | 0.80 |
| FD003 | complete | SENSOR_FULL | between_algorithms | 5 | 5 | 0.09 | -0.29 | 0.49 |
| FD003 | complete | SENSOR_FULL | between_folds | 20 | 20 | 0.32 | -0.39 | 0.77 |
| FD003 | truncated | HI_FULL | between_algorithms | 1 | 1 | 0.00 | 0.00 | 0.00 |
| FD003 | truncated | SENSOR_FULL | between_algorithms | 1 | 1 | 0.09 | 0.09 | 0.09 |

Correlação entre sensores e permutações fora da distribuição limitam inferência causal. Concordância de ranks não valida a fidelidade das explicações. Coeficientes Ridge padronizados e importâncias por impureza RF estão arquivados como diagnósticos, sem substituir permutações e ablações.

## Seleção e rastreabilidade

| subset | representation | algorithm | alpha | selection_rmse |
|---|---|---|---|---|
| FD001 | HI | Ridge | 0.10 | 26.06 |
| FD001 | HI | RF | nan | 22.35 |
| FD001 | HI_SLOPE | Ridge | 0.10 | 26.26 |
| FD001 | HI_SLOPE | RF | nan | 26.00 |
| FD001 | HI_CURV | Ridge | 0.10 | 25.88 |
| FD001 | HI_CURV | RF | nan | 23.12 |
| FD001 | HI_STD | Ridge | 0.10 | 26.40 |
| FD001 | HI_STD | RF | nan | 28.25 |
| FD001 | HI_FULL | Ridge | 1.00 | 26.04 |
| FD001 | HI_FULL | RF | nan | 27.88 |
| FD001 | HI_NO_SLOPE | Ridge | 0.10 | 26.33 |
| FD001 | HI_NO_SLOPE | RF | nan | 27.62 |
| FD001 | HI_NO_CURV | Ridge | 1.00 | 26.13 |
| FD001 | HI_NO_CURV | RF | nan | 27.88 |
| FD001 | HI_NO_STD | Ridge | 1.00 | 26.17 |
| FD001 | HI_NO_STD | RF | nan | 24.35 |
| FD001 | SENSOR_RAW | Ridge | 1.00 | 26.70 |
| FD001 | SENSOR_RAW | RF | nan | 23.00 |
| FD001 | SENSOR_MEAN | Ridge | 1.00 | 26.86 |
| FD001 | SENSOR_MEAN | RF | nan | 26.21 |
| FD001 | SENSOR_FULL | Ridge | 10.00 | 28.42 |
| FD001 | SENSOR_FULL | RF | nan | 27.68 |
| FD003 | HI | Ridge | 0.10 | 30.48 |
| FD003 | HI | RF | nan | 32.09 |
| FD003 | HI_SLOPE | Ridge | 0.10 | 29.25 |
| FD003 | HI_SLOPE | RF | nan | 38.51 |
| FD003 | HI_CURV | Ridge | 0.10 | 30.40 |
| FD003 | HI_CURV | RF | nan | 29.65 |
| FD003 | HI_STD | Ridge | 0.10 | 29.63 |
| FD003 | HI_STD | RF | nan | 26.81 |
| FD003 | HI_FULL | Ridge | 0.10 | 29.36 |
| FD003 | HI_FULL | RF | nan | 28.50 |
| FD003 | HI_NO_SLOPE | Ridge | 0.10 | 29.61 |
| FD003 | HI_NO_SLOPE | RF | nan | 26.87 |
| FD003 | HI_NO_CURV | Ridge | 0.10 | 29.38 |
| FD003 | HI_NO_CURV | RF | nan | 28.48 |
| FD003 | HI_NO_STD | Ridge | 0.10 | 29.23 |
| FD003 | HI_NO_STD | RF | nan | 32.36 |
| FD003 | SENSOR_RAW | Ridge | 0.10 | 32.11 |
| FD003 | SENSOR_RAW | RF | nan | 26.87 |
| FD003 | SENSOR_MEAN | Ridge | 1.00 | 31.98 |
| FD003 | SENSOR_MEAN | RF | nan | 31.41 |
| FD003 | SENSOR_FULL | Ridge | 1.00 | 31.53 |
| FD003 | SENSOR_FULL | RF | nan | 27.79 |

Modelos e escaladores foram congelados antes de anexar os rótulos do respectivo teste oficial nesta execução. Protocolo, fontes, versões e hashes constam de metadata.json, execution_start.json, freezes.json e manifest.json. Não há intervalo preditivo individual, limiar admissível de erro/risco, fórmula HI definitiva ou benefício econômico demonstrado. Resultados completos: events.csv, summary.csv, contrasts.csv, history_metrics.csv, importance.csv, importance_ranks.csv e rank_concordance.csv.
