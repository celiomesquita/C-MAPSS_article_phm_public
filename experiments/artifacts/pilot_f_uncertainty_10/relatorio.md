# P10 — calibração a 98% e antecedência disponível

Protocolo: [especificação anterior aos ajustes](../../protocolo_incerteza_f_10.md). FD001 principal; FD003 robustez. Três repetições de dez dobras, com F25/C15/U50/E10 disjuntos por motor em cada ajuste. F aprende os parâmetros da mesma forma de índice de saúde (HI) adotada em M18; C ajusta conversores; U calibra exclusivamente os erros e E avalia. Os mesmos 100 motores completos são avaliados uma vez por repetição: não são 300 motores independentes. ISO é regressão isotónica crescente; RF_SLOPE é floresta aleatória com HI e inclinação causal de 20 HI. Nenhum hiperparâmetro foi escolhido por U/E.

O marco HI≤0,5 inicia a avaliação da previsão de F, sem definir P, F ou remoção. Somente ciclos observados são usados. O teste oficial truncado é secundário e utiliza apenas a primeira dobra de cada repetição; já foi examinado em rodadas anteriores.

## Resultado primário: trajetória completa, nominal 98%

Cada cobertura exige conter o endpoint T em todos os ciclos observados após o marco. A bilateral usa o quantil do máximo erro absoluto; a unilateral usa o máximo erro positivo. L=max(t,F̂−q_late). Antecedência é L−t no marco; largura é a mediana entre motores das larguras medianas por trajetória. Valores em ciclos; proporções entre zero e um.

| subset | repeat | method | path_available | path_coverage | path_lower_coverage | median_width | conservative_lead_median | collapsed_point_fraction | calibration_n_min |
|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | ISO | 100 | 0.990 | 0.990 | 63.933 | 13.000 | 0.000 | 50 |
| FD001 | 1 | RF_SLOPE | 100 | 0.990 | 0.990 | 65.164 | 1.783 | 0.460 | 50 |
| FD001 | 2 | ISO | 100 | 1.000 | 0.990 | 66.360 | 14.426 | 0.000 | 50 |
| FD001 | 2 | RF_SLOPE | 100 | 0.970 | 0.970 | 62.902 | 5.252 | 0.260 | 50 |
| FD001 | 3 | ISO | 100 | 1.000 | 0.980 | 65.723 | 15.702 | 0.000 | 50 |
| FD001 | 3 | RF_SLOPE | 100 | 0.980 | 1.000 | 61.736 | 7.441 | 0.260 | 50 |
| FD003 | 1 | ISO | 100 | 1.000 | 0.990 | 69.917 | 11.000 | 0.000 | 49 |
| FD003 | 1 | RF_SLOPE | 100 | 0.990 | 0.950 | 74.795 | 1.920 | 0.390 | 49 |
| FD003 | 2 | ISO | 100 | 0.980 | 0.950 | 72.645 | 14.000 | 0.000 | 50 |
| FD003 | 2 | RF_SLOPE | 100 | 0.990 | 0.970 | 77.993 | 0.000 | 0.650 | 50 |
| FD003 | 3 | ISO | 100 | 1.000 | 0.980 | 68.455 | 13.982 | 0.000 | 49 |
| FD003 | 3 | RF_SLOPE | 100 | 0.980 | 0.990 | 66.898 | 0.000 | 0.520 | 49 |

![Cobertura e antecedência, nominal 98%](coverage_lead_98.png)

## Disponibilidade de reserva e execução

Diagnóstico A=1{L−t≥m+d}, para reserva m=15/12 e execução d=1/2. Não agenda retirada, não escolhe a âncora da reserva e não duplica uma margem na política. mark_fraction é a fração de motores disponíveis com A=1 no marco; any_fraction indica algum ciclo observado com A=1; cycle_fraction é a média, entre motores, da fração de seus ciclos com A=1. Nenhuma remoção ou inspeção foi simulada.

| subset | repeat | method | reserve | delay | path_available | point_available | mark_fraction | any_fraction | cycle_fraction |
|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | ISO | 12 | 1 | 100 | 100 | 0.600 | 0.600 | 0.074 |
| FD001 | 1 | ISO | 12 | 2 | 100 | 100 | 0.410 | 0.440 | 0.053 |
| FD001 | 1 | ISO | 15 | 1 | 100 | 100 | 0.250 | 0.270 | 0.012 |
| FD001 | 1 | ISO | 15 | 2 | 100 | 100 | 0.140 | 0.150 | 0.006 |
| FD001 | 1 | RF_SLOPE | 12 | 1 | 100 | 100 | 0.180 | 0.260 | 0.033 |
| FD001 | 1 | RF_SLOPE | 12 | 2 | 100 | 100 | 0.170 | 0.230 | 0.029 |
| FD001 | 1 | RF_SLOPE | 15 | 1 | 100 | 100 | 0.120 | 0.180 | 0.023 |
| FD001 | 1 | RF_SLOPE | 15 | 2 | 100 | 100 | 0.120 | 0.180 | 0.020 |
| FD001 | 2 | ISO | 12 | 1 | 100 | 100 | 0.550 | 0.570 | 0.076 |
| FD001 | 2 | ISO | 12 | 2 | 100 | 100 | 0.510 | 0.520 | 0.064 |
| FD001 | 2 | ISO | 15 | 1 | 100 | 100 | 0.370 | 0.370 | 0.019 |
| FD001 | 2 | ISO | 15 | 2 | 100 | 100 | 0.300 | 0.300 | 0.017 |
| FD001 | 2 | RF_SLOPE | 12 | 1 | 100 | 100 | 0.190 | 0.300 | 0.034 |
| FD001 | 2 | RF_SLOPE | 12 | 2 | 100 | 100 | 0.170 | 0.240 | 0.028 |
| FD001 | 2 | RF_SLOPE | 15 | 1 | 100 | 100 | 0.130 | 0.210 | 0.023 |
| FD001 | 2 | RF_SLOPE | 15 | 2 | 100 | 100 | 0.110 | 0.190 | 0.021 |
| FD001 | 3 | ISO | 12 | 1 | 100 | 100 | 0.790 | 0.790 | 0.104 |
| FD001 | 3 | ISO | 12 | 2 | 100 | 100 | 0.690 | 0.690 | 0.076 |
| FD001 | 3 | ISO | 15 | 1 | 100 | 100 | 0.450 | 0.470 | 0.040 |
| FD001 | 3 | ISO | 15 | 2 | 100 | 100 | 0.350 | 0.370 | 0.029 |
| FD001 | 3 | RF_SLOPE | 12 | 1 | 100 | 100 | 0.250 | 0.360 | 0.045 |
| FD001 | 3 | RF_SLOPE | 12 | 2 | 100 | 100 | 0.220 | 0.310 | 0.037 |
| FD001 | 3 | RF_SLOPE | 15 | 1 | 100 | 100 | 0.160 | 0.220 | 0.028 |
| FD001 | 3 | RF_SLOPE | 15 | 2 | 100 | 100 | 0.140 | 0.190 | 0.026 |
| FD003 | 1 | ISO | 12 | 1 | 100 | 100 | 0.300 | 0.310 | 0.035 |
| FD003 | 1 | ISO | 12 | 2 | 100 | 100 | 0.300 | 0.310 | 0.032 |
| FD003 | 1 | ISO | 15 | 1 | 100 | 100 | 0.280 | 0.290 | 0.023 |
| FD003 | 1 | ISO | 15 | 2 | 100 | 100 | 0.100 | 0.100 | 0.008 |
| FD003 | 1 | RF_SLOPE | 12 | 1 | 100 | 100 | 0.200 | 0.290 | 0.028 |
| FD003 | 1 | RF_SLOPE | 12 | 2 | 100 | 100 | 0.180 | 0.270 | 0.024 |
| FD003 | 1 | RF_SLOPE | 15 | 1 | 100 | 100 | 0.140 | 0.250 | 0.017 |
| FD003 | 1 | RF_SLOPE | 15 | 2 | 100 | 100 | 0.130 | 0.230 | 0.013 |
| FD003 | 2 | ISO | 12 | 1 | 100 | 100 | 0.630 | 0.660 | 0.082 |
| FD003 | 2 | ISO | 12 | 2 | 100 | 100 | 0.520 | 0.560 | 0.057 |
| FD003 | 2 | ISO | 15 | 1 | 100 | 100 | 0.260 | 0.300 | 0.022 |
| FD003 | 2 | ISO | 15 | 2 | 100 | 100 | 0.260 | 0.300 | 0.021 |
| FD003 | 2 | RF_SLOPE | 12 | 1 | 100 | 100 | 0.130 | 0.220 | 0.029 |
| FD003 | 2 | RF_SLOPE | 12 | 2 | 100 | 100 | 0.110 | 0.190 | 0.024 |
| FD003 | 2 | RF_SLOPE | 15 | 1 | 100 | 100 | 0.090 | 0.170 | 0.020 |
| FD003 | 2 | RF_SLOPE | 15 | 2 | 100 | 100 | 0.070 | 0.140 | 0.017 |
| FD003 | 3 | ISO | 12 | 1 | 100 | 100 | 0.620 | 0.630 | 0.071 |
| FD003 | 3 | ISO | 12 | 2 | 100 | 100 | 0.480 | 0.490 | 0.041 |
| FD003 | 3 | ISO | 15 | 1 | 100 | 100 | 0.140 | 0.150 | 0.010 |
| FD003 | 3 | ISO | 15 | 2 | 100 | 100 | 0.000 | 0.000 | 0.000 |
| FD003 | 3 | RF_SLOPE | 12 | 1 | 100 | 100 | 0.140 | 0.270 | 0.021 |
| FD003 | 3 | RF_SLOPE | 12 | 2 | 100 | 100 | 0.120 | 0.240 | 0.018 |
| FD003 | 3 | RF_SLOPE | 15 | 1 | 100 | 100 | 0.110 | 0.170 | 0.010 |
| FD003 | 3 | RF_SLOPE | 15 | 2 | 100 | 100 | 0.110 | 0.140 | 0.009 |

## Erro pontual e contraste pareado no marco

Raiz do erro quadrático médio (RMSE), erro absoluto médio (MAE) e viés de F̂−T. Diferença RF_SLOPE−ISO nos mesmos motores/ciclos, com intervalo descritivo de 95% por 2000 reamostragens pareadas por motor; separado da banda individual de F.

| subset | dataset | repeat | method | total | available | rmse | mae | bias |
|---|---|---|---|---|---|---|---|---|
| FD001 | complete | 1 | ISO | 100 | 100 | 16.142 | 12.878 | -0.891 |
| FD001 | complete | 1 | RF_SLOPE | 100 | 100 | 15.291 | 12.312 | 2.756 |
| FD001 | complete | 2 | ISO | 100 | 100 | 17.537 | 13.827 | -0.468 |
| FD001 | complete | 2 | RF_SLOPE | 100 | 100 | 17.132 | 13.899 | 0.188 |
| FD001 | complete | 3 | ISO | 100 | 100 | 15.444 | 11.991 | -1.609 |
| FD001 | complete | 3 | RF_SLOPE | 100 | 100 | 13.247 | 10.526 | 0.052 |
| FD001 | truncated | 1 | ISO | 100 | 29 | 14.519 | 11.382 | -3.268 |
| FD001 | truncated | 1 | RF_SLOPE | 100 | 29 | 16.100 | 12.634 | -1.416 |
| FD001 | truncated | 2 | ISO | 100 | 30 | 16.350 | 13.084 | 9.483 |
| FD001 | truncated | 2 | RF_SLOPE | 100 | 30 | 15.944 | 12.879 | 10.510 |
| FD001 | truncated | 3 | ISO | 100 | 29 | 15.087 | 11.353 | -4.525 |
| FD001 | truncated | 3 | RF_SLOPE | 100 | 29 | 14.358 | 10.703 | -1.328 |
| FD003 | complete | 1 | ISO | 100 | 100 | 16.748 | 12.759 | -1.675 |
| FD003 | complete | 1 | RF_SLOPE | 100 | 100 | 17.352 | 13.086 | -0.784 |
| FD003 | complete | 2 | ISO | 100 | 100 | 36.576 | 19.396 | -1.049 |
| FD003 | complete | 2 | RF_SLOPE | 100 | 100 | 33.827 | 17.906 | -2.704 |
| FD003 | complete | 3 | ISO | 100 | 100 | 18.313 | 13.343 | -0.439 |
| FD003 | complete | 3 | RF_SLOPE | 100 | 100 | 16.923 | 12.078 | -0.371 |
| FD003 | truncated | 1 | ISO | 100 | 27 | 14.802 | 11.853 | 0.592 |
| FD003 | truncated | 1 | RF_SLOPE | 100 | 27 | 16.720 | 13.987 | 3.848 |
| FD003 | truncated | 2 | ISO | 100 | 26 | 19.723 | 15.208 | -7.527 |
| FD003 | truncated | 2 | RF_SLOPE | 100 | 26 | 18.348 | 13.721 | -2.478 |
| FD003 | truncated | 3 | ISO | 100 | 23 | 12.702 | 9.953 | 1.514 |
| FD003 | truncated | 3 | RF_SLOPE | 100 | 23 | 12.167 | 9.755 | 2.148 |

| subset | dataset | repeat | event | reference | common | delta_rmse | ci_low | ci_high |
|---|---|---|---|---|---|---|---|---|
| FD001 | complete | 1 | mark | ISO | 100 | -0.850 | -3.674 | 1.950 |
| FD001 | complete | 2 | mark | ISO | 100 | -0.406 | -2.286 | 1.507 |
| FD001 | complete | 3 | mark | ISO | 100 | -2.197 | -4.346 | 0.037 |
| FD001 | truncated | 1 | mark | ISO | 29 | 1.582 | -0.885 | 4.978 |
| FD001 | truncated | 2 | mark | ISO | 30 | -0.406 | -5.559 | 5.345 |
| FD001 | truncated | 3 | mark | ISO | 29 | -0.729 | -2.607 | 1.532 |
| FD003 | complete | 1 | mark | ISO | 100 | 0.605 | -0.934 | 2.031 |
| FD003 | complete | 2 | mark | ISO | 100 | -2.749 | -5.683 | 0.422 |
| FD003 | complete | 3 | mark | ISO | 100 | -1.390 | -3.444 | 0.427 |
| FD003 | truncated | 1 | mark | ISO | 27 | 1.918 | -1.093 | 4.643 |
| FD003 | truncated | 2 | mark | ISO | 26 | -1.375 | -6.003 | 3.105 |
| FD003 | truncated | 3 | mark | ISO | 23 | -0.535 | -4.322 | 2.558 |

## Quantis e amostra efetiva

Ordem corrigida k=ceil((n+1)(1−α)). Em U50, o alvo 98% usa k=50, isto é, o maior escore; n≤48 produziria +infinito. A tabela resume as dez dobras por domínio, repetição, método, escopo e nível, sem juntar motores para calibrar.

| subset | repeat | method | scope | alpha | n_min | n_max | k_min | k_max | q_abs_min | q_abs_max | q_late_min | q_late_max |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | ISO | path | 0.020 | 50 | 50 | 50 | 50 | 36.612 | 53.867 | 14.895 | 31.844 |
| FD001 | 1 | ISO | path | 0.050 | 50 | 50 | 49 | 49 | 34.383 | 49.867 | 13.895 | 28.795 |
| FD001 | 1 | ISO | point | 0.020 | 50 | 50 | 50 | 50 | 36.365 | 53.867 | 11.910 | 30.720 |
| FD001 | 1 | ISO | point | 0.050 | 50 | 50 | 49 | 49 | 32.365 | 49.867 | 11.203 | 28.795 |
| FD001 | 1 | RF_SLOPE | path | 0.020 | 50 | 50 | 50 | 50 | 35.295 | 56.132 | 22.541 | 56.132 |
| FD001 | 1 | RF_SLOPE | path | 0.050 | 50 | 50 | 49 | 49 | 34.725 | 45.075 | 21.745 | 44.486 |
| FD001 | 1 | RF_SLOPE | point | 0.020 | 50 | 50 | 50 | 50 | 32.491 | 56.132 | 19.106 | 56.132 |
| FD001 | 1 | RF_SLOPE | point | 0.050 | 50 | 50 | 49 | 49 | 23.640 | 44.121 | 16.623 | 42.714 |
| FD001 | 2 | ISO | path | 0.020 | 50 | 50 | 50 | 50 | 39.281 | 54.737 | 12.844 | 39.281 |
| FD001 | 2 | ISO | path | 0.050 | 50 | 50 | 49 | 49 | 34.281 | 53.737 | 12.844 | 34.281 |
| FD001 | 2 | ISO | point | 0.020 | 50 | 50 | 50 | 50 | 39.281 | 54.737 | 11.263 | 39.281 |
| FD001 | 2 | ISO | point | 0.050 | 50 | 50 | 49 | 49 | 34.281 | 53.737 | 7.263 | 34.281 |
| FD001 | 2 | RF_SLOPE | path | 0.020 | 50 | 50 | 50 | 50 | 36.760 | 49.308 | 23.015 | 43.826 |
| FD001 | 2 | RF_SLOPE | path | 0.050 | 50 | 50 | 49 | 49 | 36.309 | 44.976 | 21.393 | 41.367 |
| FD001 | 2 | RF_SLOPE | point | 0.020 | 50 | 50 | 50 | 50 | 31.302 | 45.144 | 15.877 | 40.382 |
| FD001 | 2 | RF_SLOPE | point | 0.050 | 50 | 50 | 49 | 49 | 30.555 | 43.620 | 12.692 | 38.062 |
| FD001 | 3 | ISO | path | 0.020 | 50 | 50 | 50 | 50 | 39.927 | 51.583 | 16.923 | 31.629 |
| FD001 | 3 | ISO | path | 0.050 | 50 | 50 | 49 | 49 | 38.994 | 50.583 | 15.417 | 25.629 |
| FD001 | 3 | ISO | point | 0.020 | 50 | 50 | 50 | 50 | 38.102 | 51.583 | 16.381 | 29.677 |
| FD001 | 3 | ISO | point | 0.050 | 50 | 50 | 49 | 49 | 38.102 | 50.583 | 14.417 | 24.359 |
| FD001 | 3 | RF_SLOPE | path | 0.020 | 50 | 50 | 50 | 50 | 36.852 | 47.236 | 25.598 | 40.682 |
| FD001 | 3 | RF_SLOPE | path | 0.050 | 50 | 50 | 49 | 49 | 35.815 | 44.453 | 18.864 | 39.352 |
| FD001 | 3 | RF_SLOPE | point | 0.020 | 50 | 50 | 50 | 50 | 34.519 | 47.236 | 15.116 | 34.956 |
| FD001 | 3 | RF_SLOPE | point | 0.050 | 50 | 50 | 49 | 49 | 30.972 | 44.453 | 14.058 | 33.684 |
| FD003 | 1 | ISO | path | 0.020 | 49 | 50 | 49 | 50 | 42.853 | 59.439 | 20.468 | 33.156 |
| FD003 | 1 | ISO | path | 0.050 | 49 | 50 | 48 | 49 | 33.156 | 51.403 | 18.597 | 29.249 |
| FD003 | 1 | ISO | point | 0.020 | 49 | 50 | 49 | 50 | 41.526 | 59.439 | 18.597 | 33.156 |
| FD003 | 1 | ISO | point | 0.050 | 49 | 50 | 48 | 49 | 33.156 | 51.403 | 17.597 | 24.604 |
| FD003 | 1 | RF_SLOPE | path | 0.020 | 49 | 50 | 49 | 50 | 38.785 | 68.762 | 26.260 | 63.602 |
| FD003 | 1 | RF_SLOPE | path | 0.050 | 49 | 50 | 48 | 49 | 35.473 | 52.725 | 25.171 | 43.012 |
| FD003 | 1 | RF_SLOPE | point | 0.020 | 49 | 50 | 49 | 50 | 37.781 | 68.762 | 20.813 | 46.460 |
| FD003 | 1 | RF_SLOPE | point | 0.050 | 49 | 50 | 48 | 49 | 31.105 | 47.554 | 17.515 | 40.834 |
| FD003 | 2 | ISO | path | 0.020 | 50 | 50 | 50 | 50 | 40.720 | 256.068 | 18.747 | 74.048 |
| FD003 | 2 | ISO | path | 0.050 | 50 | 50 | 49 | 49 | 29.643 | 208.696 | 15.247 | 69.048 |
| FD003 | 2 | ISO | point | 0.020 | 50 | 50 | 50 | 50 | 34.656 | 254.696 | 16.515 | 74.048 |
| FD003 | 2 | ISO | point | 0.050 | 50 | 50 | 49 | 49 | 28.643 | 208.696 | 14.055 | 68.104 |
| FD003 | 2 | RF_SLOPE | path | 0.020 | 50 | 50 | 50 | 50 | 45.327 | 260.254 | 22.512 | 136.853 |
| FD003 | 2 | RF_SLOPE | path | 0.050 | 50 | 50 | 49 | 49 | 40.084 | 209.350 | 21.708 | 131.732 |
| FD003 | 2 | RF_SLOPE | point | 0.020 | 50 | 50 | 50 | 50 | 37.916 | 238.258 | 21.708 | 107.627 |
| FD003 | 2 | RF_SLOPE | point | 0.050 | 50 | 50 | 49 | 49 | 31.642 | 209.350 | 15.568 | 92.484 |
| FD003 | 3 | ISO | path | 0.020 | 49 | 50 | 49 | 50 | 24.652 | 94.955 | 20.409 | 32.357 |
| FD003 | 3 | ISO | path | 0.050 | 49 | 50 | 48 | 49 | 24.098 | 80.955 | 19.569 | 27.922 |
| FD003 | 3 | ISO | point | 0.020 | 49 | 50 | 49 | 50 | 24.098 | 94.955 | 19.048 | 31.490 |
| FD003 | 3 | ISO | point | 0.050 | 49 | 50 | 48 | 49 | 24.098 | 80.955 | 17.982 | 27.357 |
| FD003 | 3 | RF_SLOPE | path | 0.020 | 49 | 50 | 49 | 50 | 30.511 | 78.654 | 30.511 | 54.704 |
| FD003 | 3 | RF_SLOPE | path | 0.050 | 49 | 50 | 48 | 49 | 29.802 | 77.784 | 27.697 | 46.700 |
| FD003 | 3 | RF_SLOPE | point | 0.020 | 49 | 50 | 49 | 50 | 25.593 | 73.135 | 23.308 | 54.704 |
| FD003 | 3 | RF_SLOPE | point | 0.050 | 49 | 50 | 48 | 49 | 24.849 | 59.099 | 13.997 | 38.483 |

## Sensibilidade 95% e calibração somente no marco

Níveis e escopos pré-especificados. A cobertura da trajetória com quantil somente do marco é diagnóstica: a calibração pontual não promete cobertura simultânea.

| subset | dataset | repeat | method | scope | alpha | total | path_available | point_available | finite_abs_fraction | finite_late_fraction | path_coverage | path_lower_coverage | point_coverage | point_lower_coverage | median_width | collapsed_point_fraction | conservative_lead_median | calibration_n_min |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | complete | 1 | ISO | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.990 | 0.990 | 0.990 | 63.933 | 0.000 | 13.000 | 50 |
| FD001 | complete | 1 | ISO | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.970 | 0.990 | 0.980 | 60.718 | 0.000 | 16.308 | 50 |
| FD001 | complete | 1 | ISO | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.970 | 0.990 | 0.990 | 62.621 | 0.000 | 14.000 | 50 |
| FD001 | complete | 1 | ISO | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.960 | 0.930 | 0.980 | 0.980 | 59.438 | 0.000 | 19.000 | 50 |
| FD001 | complete | 1 | RF_SLOPE | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.990 | 1.000 | 1.000 | 65.164 | 0.460 | 1.783 | 50 |
| FD001 | complete | 1 | RF_SLOPE | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.980 | 0.980 | 0.990 | 0.990 | 61.816 | 0.310 | 5.832 | 50 |
| FD001 | complete | 1 | RF_SLOPE | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.940 | 0.990 | 0.980 | 61.350 | 0.270 | 7.242 | 50 |
| FD001 | complete | 1 | RF_SLOPE | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.900 | 0.910 | 0.970 | 0.970 | 53.870 | 0.150 | 12.585 | 50 |
| FD001 | complete | 2 | ISO | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 1.000 | 0.990 | 1.000 | 0.990 | 66.360 | 0.000 | 14.426 | 50 |
| FD001 | complete | 2 | ISO | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.950 | 0.970 | 0.960 | 0.970 | 63.675 | 0.000 | 17.226 | 50 |
| FD001 | complete | 2 | ISO | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.980 | 1.000 | 0.990 | 66.183 | 0.000 | 14.426 | 50 |
| FD001 | complete | 2 | ISO | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.950 | 0.930 | 0.950 | 0.970 | 62.338 | 0.000 | 20.000 | 50 |
| FD001 | complete | 2 | RF_SLOPE | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.970 | 0.970 | 0.990 | 0.990 | 62.902 | 0.260 | 5.252 | 50 |
| FD001 | complete | 2 | RF_SLOPE | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.960 | 0.960 | 0.990 | 0.990 | 59.834 | 0.160 | 7.034 | 50 |
| FD001 | complete | 2 | RF_SLOPE | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.960 | 0.940 | 0.990 | 0.990 | 58.601 | 0.170 | 8.679 | 50 |
| FD001 | complete | 2 | RF_SLOPE | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.910 | 0.840 | 0.970 | 0.970 | 56.238 | 0.010 | 16.138 | 50 |
| FD001 | complete | 3 | ISO | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 1.000 | 0.980 | 1.000 | 0.980 | 65.723 | 0.000 | 15.702 | 50 |
| FD001 | complete | 3 | ISO | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.980 | 0.940 | 0.980 | 0.950 | 61.981 | 0.000 | 19.431 | 50 |
| FD001 | complete | 3 | ISO | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.970 | 0.990 | 0.980 | 65.308 | 0.000 | 16.000 | 50 |
| FD001 | complete | 3 | ISO | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.980 | 0.940 | 0.980 | 0.950 | 61.981 | 0.000 | 20.176 | 50 |
| FD001 | complete | 3 | RF_SLOPE | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.980 | 1.000 | 1.000 | 1.000 | 61.736 | 0.260 | 7.441 | 50 |
| FD001 | complete | 3 | RF_SLOPE | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.970 | 0.950 | 1.000 | 0.990 | 59.559 | 0.200 | 9.935 | 50 |
| FD001 | complete | 3 | RF_SLOPE | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.960 | 0.940 | 1.000 | 0.990 | 59.892 | 0.110 | 11.743 | 50 |
| FD001 | complete | 3 | RF_SLOPE | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.920 | 0.850 | 0.990 | 0.970 | 56.652 | 0.010 | 14.943 | 50 |
| FD003 | complete | 1 | ISO | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 1.000 | 0.990 | 1.000 | 0.990 | 69.917 | 0.000 | 11.000 | 49 |
| FD003 | complete | 1 | ISO | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.960 | 0.990 | 0.960 | 62.833 | 0.000 | 16.167 | 49 |
| FD003 | complete | 1 | ISO | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 1.000 | 0.980 | 1.000 | 0.990 | 69.917 | 0.000 | 11.746 | 49 |
| FD003 | complete | 1 | ISO | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.910 | 0.990 | 0.960 | 62.833 | 0.000 | 17.500 | 49 |
| FD003 | complete | 1 | RF_SLOPE | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.950 | 0.990 | 0.980 | 74.795 | 0.390 | 1.920 | 49 |
| FD003 | complete | 1 | RF_SLOPE | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.960 | 0.910 | 0.980 | 0.970 | 63.682 | 0.260 | 6.839 | 49 |
| FD003 | complete | 1 | RF_SLOPE | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.970 | 0.900 | 0.990 | 0.980 | 66.213 | 0.170 | 10.107 | 49 |
| FD003 | complete | 1 | RF_SLOPE | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.930 | 0.850 | 0.980 | 0.940 | 59.715 | 0.120 | 13.318 | 49 |
| FD003 | complete | 2 | ISO | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.980 | 0.950 | 0.980 | 0.980 | 72.645 | 0.000 | 14.000 | 50 |
| FD003 | complete | 2 | ISO | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.960 | 0.950 | 0.960 | 0.970 | 63.190 | 0.000 | 17.000 | 50 |
| FD003 | complete | 2 | ISO | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.970 | 0.950 | 0.980 | 0.970 | 72.432 | 0.000 | 14.000 | 50 |
| FD003 | complete | 2 | ISO | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.940 | 0.920 | 0.960 | 0.960 | 62.618 | 0.000 | 18.262 | 50 |
| FD003 | complete | 2 | RF_SLOPE | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.990 | 0.970 | 0.990 | 0.990 | 77.993 | 0.650 | 0.000 | 50 |
| FD003 | complete | 2 | RF_SLOPE | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.960 | 0.960 | 0.970 | 0.990 | 70.767 | 0.540 | 0.000 | 50 |
| FD003 | complete | 2 | RF_SLOPE | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.930 | 0.870 | 0.980 | 0.970 | 70.472 | 0.360 | 5.600 | 50 |
| FD003 | complete | 2 | RF_SLOPE | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.910 | 0.740 | 0.950 | 0.950 | 62.434 | 0.170 | 11.494 | 50 |
| FD003 | complete | 3 | ISO | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 1.000 | 0.980 | 1.000 | 0.980 | 68.455 | 0.000 | 13.982 | 49 |
| FD003 | complete | 3 | ISO | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.960 | 0.980 | 0.960 | 0.980 | 60.518 | 0.000 | 14.822 | 49 |
| FD003 | complete | 3 | ISO | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 1.000 | 0.960 | 1.000 | 0.980 | 68.006 | 0.000 | 15.000 | 49 |
| FD003 | complete | 3 | ISO | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.960 | 0.950 | 0.960 | 0.980 | 60.082 | 0.000 | 17.000 | 49 |
| FD003 | complete | 3 | RF_SLOPE | path | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.980 | 0.990 | 0.990 | 1.000 | 66.898 | 0.520 | 0.000 | 49 |
| FD003 | complete | 3 | RF_SLOPE | path | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.960 | 0.960 | 0.980 | 0.990 | 60.883 | 0.390 | 3.959 | 49 |
| FD003 | complete | 3 | RF_SLOPE | point | 0.020 | 100 | 100 | 100 | 1.000 | 1.000 | 0.920 | 0.920 | 0.980 | 0.990 | 62.407 | 0.330 | 6.553 | 49 |
| FD003 | complete | 3 | RF_SLOPE | point | 0.050 | 100 | 100 | 100 | 1.000 | 1.000 | 0.870 | 0.880 | 0.950 | 0.990 | 52.018 | 0.080 | 10.983 | 49 |

## Testes oficiais truncados: disponibilidade condicional

A trajetória termina no truncamento. Rótulos de vida útil remanescente (RUL) determinam T somente para aferição, após prever. Motores sem marco não são imputados; cobertura entre disponíveis não representa toda a frota.

| subset | dataset | repeat | method | scope | alpha | total | path_available | point_available | finite_abs_fraction | finite_late_fraction | path_coverage | path_lower_coverage | point_coverage | point_lower_coverage | median_width | collapsed_point_fraction | conservative_lead_median | calibration_n_min |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | truncated | 1 | ISO | path | 0.020 | 100 | 29 | 29 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 78.666 | 0.000 | 13.000 | 50 |
| FD001 | truncated | 1 | RF_SLOPE | path | 0.020 | 100 | 29 | 29 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 78.146 | 0.276 | 4.739 | 50 |
| FD001 | truncated | 2 | ISO | path | 0.020 | 100 | 30 | 30 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 78.562 | 0.000 | 16.000 | 50 |
| FD001 | truncated | 2 | RF_SLOPE | path | 0.020 | 100 | 30 | 30 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 72.183 | 0.300 | 3.220 | 50 |
| FD001 | truncated | 3 | ISO | path | 0.020 | 100 | 29 | 29 | 1.000 | 1.000 | 0.966 | 0.966 | 0.966 | 0.966 | 77.531 | 0.000 | 20.000 | 50 |
| FD001 | truncated | 3 | RF_SLOPE | path | 0.020 | 100 | 29 | 29 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 75.510 | 0.000 | 11.312 | 50 |
| FD003 | truncated | 1 | ISO | path | 0.020 | 100 | 27 | 27 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 81.993 | 0.000 | 11.000 | 50 |
| FD003 | truncated | 1 | RF_SLOPE | path | 0.020 | 100 | 27 | 27 | 1.000 | 1.000 | 1.000 | 0.963 | 1.000 | 1.000 | 86.320 | 0.111 | 12.773 | 50 |
| FD003 | truncated | 2 | ISO | path | 0.020 | 100 | 26 | 26 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 99.537 | 0.000 | 14.000 | 50 |
| FD003 | truncated | 2 | RF_SLOPE | path | 0.020 | 100 | 26 | 26 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 84.125 | 0.308 | 6.010 | 50 |
| FD003 | truncated | 3 | ISO | path | 0.020 | 100 | 23 | 23 | 1.000 | 1.000 | 0.957 | 1.000 | 0.957 | 1.000 | 49.304 | 0.000 | 16.000 | 50 |
| FD003 | truncated | 3 | RF_SLOPE | path | 0.020 | 100 | 23 | 23 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 60.249 | 0.130 | 7.744 | 50 |

## Limites de inferência

98% é alvo preditivo nominal, não comprovação de ultrapassagem ≤2% pela futura política. A interpretação marginal exige intercambiabilidade e o mesmo domínio de disponibilidade. Uma dobra E10 tem resolução de dez pontos percentuais; os 100 motores de cada repetição têm resolução de um ponto. As repetições compartilham motores e modelos de dobras compartilham desenvolvimento. F25/C15/U50/E10 também reduz ajuste e altera avaliação frente a P09: diferenças não isolam o efeito de aumentar U. Não foram definidos o gatilho de incerteza elevada ou a âncora da reserva; não há conclusão operacional sobre voo após T. A forma HI permanece referência de trabalho, sem equivalência física.

A ordem corrigida segue Lei et al. (2018), *Distribution-Free Predictive Inference for Regression*, DOI 10.1080/01621459.2017.1307116, seção 2: [fonte primária](https://www.stat.cmu.edu/~ryantibs/papers/conformal-jasa.pdf). O escore máximo por trajetória é a adaptação deste protocolo.

## Verificação e reconstrução

A reconstrução inicial encontrou arredondamento em comparações no limiar m+d. Emenda posterior aos ajustes: tolerância de 10⁻⁹ ciclo, sem mudança de classificações ou reajuste. Diagnósticos foram recalculados de previsões congeladas; versões originais foram preservadas. [Emenda](amendment_numeric_boundary.json).

[Verificação](verification.json), [metadados](metadata.json), [partições](splits.json), [congelamentos anteriores à avaliação](freezes.json) e [manifesto](manifest.json). CSV preservados: scores, events, bands, quantiles, point_summary, band_summary, contrasts, reserves e reserve_summary. Previsões e modelos estão arquivados por dobra.
