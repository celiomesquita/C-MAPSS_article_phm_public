# P09 — robustez e incerteza de F após o marco HI≤0,5

Índice de saúde (HI) de M18, com a mesma forma funcional e parâmetros reaprendidos em cada partição. Três repetições de cinco folds por motor em FD001 e FD003. F40 ajusta o HI, C20 ajusta a conversão para vida útil remanescente (RUL), U20 calibra exclusivamente a incerteza e E20 avalia. Não há seleção de configurações em U/E. Os testes oficiais truncados usam somente o modelo/calibração do fold 1 de cada repetição, sem ajuste adicional.

ISO = isotônico crescente; RF_HI = floresta aleatória com HI corrente; RF_SLOPE = mesma floresta com HI e inclinação causal de 20 valores. Todos usam ciclos ≥39. Hiperparâmetros da convenção HI e das florestas foram pré-fixados; a separação nesta rodada é nova, mas os dados já informaram escolhas anteriores. São resultados exploratórios.

## Prognóstico no primeiro marco

RMSE = raiz do erro quadrático médio; MAE = erro absoluto médio. Erro = F previsto menos endpoint real, em ciclos; viés positivo prevê F tarde. As métricas são condicionais à disponibilidade do marco. Cada repetição tem os mesmos 100 motores, não uma nova amostra de 100.

| subset | dataset | repeat | method | total | available | rmse | mae | bias | positive_fraction | actual_lead_median |
|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | complete | 1 | ISO | 100 | 100 | 16.426 | 13.198 | 1.341 | 0.640 | 35.000 |
| FD001 | complete | 1 | RF_HI | 100 | 100 | 16.539 | 13.634 | 1.882 | 0.600 | 35.000 |
| FD001 | complete | 1 | RF_SLOPE | 100 | 100 | 15.039 | 12.229 | 3.321 | 0.610 | 35.000 |
| FD001 | complete | 2 | ISO | 100 | 100 | 16.478 | 12.815 | -1.881 | 0.560 | 35.000 |
| FD001 | complete | 2 | RF_HI | 100 | 100 | 16.901 | 13.411 | 0.145 | 0.610 | 35.000 |
| FD001 | complete | 2 | RF_SLOPE | 100 | 100 | 15.801 | 12.117 | -1.146 | 0.480 | 35.000 |
| FD001 | complete | 3 | ISO | 100 | 100 | 16.403 | 12.519 | -1.640 | 0.560 | 34.500 |
| FD001 | complete | 3 | RF_HI | 100 | 100 | 17.387 | 13.366 | -0.804 | 0.570 | 34.500 |
| FD001 | complete | 3 | RF_SLOPE | 100 | 100 | 15.954 | 12.594 | -1.290 | 0.510 | 34.500 |
| FD001 | truncated | 1 | ISO | 100 | 27 | 14.610 | 10.721 | -7.235 | 0.333 | 40.000 |
| FD001 | truncated | 1 | RF_HI | 100 | 27 | 13.703 | 10.117 | -5.709 | 0.407 | 40.000 |
| FD001 | truncated | 1 | RF_SLOPE | 100 | 27 | 14.261 | 11.215 | -7.391 | 0.259 | 40.000 |
| FD001 | truncated | 2 | ISO | 100 | 27 | 13.161 | 10.089 | -2.440 | 0.519 | 38.000 |
| FD001 | truncated | 2 | RF_HI | 100 | 27 | 13.451 | 10.198 | -2.002 | 0.519 | 38.000 |
| FD001 | truncated | 2 | RF_SLOPE | 100 | 27 | 13.056 | 9.955 | -3.666 | 0.333 | 38.000 |
| FD001 | truncated | 3 | ISO | 100 | 27 | 13.149 | 9.995 | -0.988 | 0.519 | 38.000 |
| FD001 | truncated | 3 | RF_HI | 100 | 27 | 12.320 | 9.200 | -1.906 | 0.519 | 38.000 |
| FD001 | truncated | 3 | RF_SLOPE | 100 | 27 | 15.025 | 11.751 | 6.162 | 0.593 | 38.000 |
| FD003 | complete | 1 | ISO | 100 | 100 | 16.405 | 12.867 | -1.635 | 0.510 | 35.000 |
| FD003 | complete | 1 | RF_HI | 100 | 100 | 18.415 | 14.158 | -1.355 | 0.520 | 35.000 |
| FD003 | complete | 1 | RF_SLOPE | 100 | 100 | 16.154 | 12.498 | -0.406 | 0.510 | 35.000 |
| FD003 | complete | 2 | ISO | 100 | 100 | 15.235 | 11.775 | -0.895 | 0.570 | 34.000 |
| FD003 | complete | 2 | RF_HI | 100 | 100 | 17.366 | 13.673 | 0.836 | 0.580 | 34.000 |
| FD003 | complete | 2 | RF_SLOPE | 100 | 100 | 14.546 | 11.336 | 0.651 | 0.550 | 34.000 |
| FD003 | complete | 3 | ISO | 100 | 100 | 15.746 | 12.162 | 0.634 | 0.600 | 36.500 |
| FD003 | complete | 3 | RF_HI | 100 | 100 | 16.887 | 13.213 | 1.092 | 0.590 | 36.500 |
| FD003 | complete | 3 | RF_SLOPE | 100 | 100 | 13.698 | 11.205 | 0.165 | 0.560 | 36.500 |
| FD003 | truncated | 1 | ISO | 100 | 24 | 17.112 | 12.773 | -8.370 | 0.375 | 39.000 |
| FD003 | truncated | 1 | RF_HI | 100 | 24 | 17.916 | 13.582 | -10.228 | 0.250 | 39.000 |
| FD003 | truncated | 1 | RF_SLOPE | 100 | 24 | 14.754 | 11.410 | -5.419 | 0.417 | 39.000 |
| FD003 | truncated | 2 | ISO | 100 | 24 | 13.604 | 10.784 | -2.816 | 0.458 | 37.500 |
| FD003 | truncated | 2 | RF_HI | 100 | 24 | 14.880 | 12.711 | -1.350 | 0.458 | 37.500 |
| FD003 | truncated | 2 | RF_SLOPE | 100 | 24 | 12.614 | 9.273 | -0.524 | 0.542 | 37.500 |
| FD003 | truncated | 3 | ISO | 100 | 25 | 16.286 | 13.079 | -2.968 | 0.480 | 43.000 |
| FD003 | truncated | 3 | RF_HI | 100 | 25 | 19.880 | 16.215 | -3.754 | 0.400 | 43.000 |
| FD003 | truncated | 3 | RF_SLOPE | 100 | 25 | 15.844 | 13.328 | -2.489 | 0.440 | 43.000 |

## Comparações pareadas no marco

Diferença = RF_SLOPE menos referência, nos mesmos motores e ciclos. Intervalos descritivos de 95% por bootstrap pareado de 2.000 amostras por motor, separadamente em cada repetição. Esses intervalos são distintos das bandas preditivas de F calibradas em U.

| subset | dataset | repeat | event | reference | common | delta_rmse | ci_low | ci_high |
|---|---|---|---|---|---|---|---|---|
| FD001 | complete | 1 | mark | ISO | 100 | -1.387 | -2.860 | 0.151 |
| FD001 | complete | 1 | mark | RF_HI | 100 | -1.501 | -2.947 | -0.091 |
| FD001 | complete | 2 | mark | ISO | 100 | -0.677 | -3.314 | 1.915 |
| FD001 | complete | 2 | mark | RF_HI | 100 | -1.101 | -3.447 | 1.355 |
| FD001 | complete | 3 | mark | ISO | 100 | -0.449 | -2.570 | 1.815 |
| FD001 | complete | 3 | mark | RF_HI | 100 | -1.434 | -3.517 | 0.721 |
| FD001 | truncated | 1 | mark | ISO | 27 | -0.350 | -1.198 | 0.830 |
| FD001 | truncated | 1 | mark | RF_HI | 27 | 0.558 | -0.092 | 1.466 |
| FD001 | truncated | 2 | mark | ISO | 27 | -0.105 | -3.750 | 3.311 |
| FD001 | truncated | 2 | mark | RF_HI | 27 | -0.395 | -3.473 | 2.405 |
| FD001 | truncated | 3 | mark | ISO | 27 | 1.876 | -4.487 | 8.333 |
| FD001 | truncated | 3 | mark | RF_HI | 27 | 2.705 | -3.191 | 8.672 |
| FD003 | complete | 1 | mark | ISO | 100 | -0.251 | -2.101 | 1.638 |
| FD003 | complete | 1 | mark | RF_HI | 100 | -2.260 | -4.437 | -0.082 |
| FD003 | complete | 2 | mark | ISO | 100 | -0.690 | -2.604 | 1.344 |
| FD003 | complete | 2 | mark | RF_HI | 100 | -2.821 | -4.795 | -0.594 |
| FD003 | complete | 3 | mark | ISO | 100 | -2.047 | -4.096 | -0.136 |
| FD003 | complete | 3 | mark | RF_HI | 100 | -3.189 | -5.122 | -1.180 |
| FD003 | truncated | 1 | mark | ISO | 24 | -2.359 | -5.326 | 0.170 |
| FD003 | truncated | 1 | mark | RF_HI | 24 | -3.162 | -7.658 | 0.642 |
| FD003 | truncated | 2 | mark | ISO | 24 | -0.989 | -4.411 | 1.292 |
| FD003 | truncated | 2 | mark | RF_HI | 24 | -2.265 | -6.511 | 1.096 |
| FD003 | truncated | 3 | mark | ISO | 25 | -0.442 | -4.845 | 3.203 |
| FD003 | truncated | 3 | mark | RF_HI | 25 | -4.036 | -8.728 | -0.227 |

## Bandas da trajetória completa — variação entre repetições

Valores mínimos/máximos entre três repetições; não intervalos de confiança sobre 300 motores. alpha=0,10 e 0,05 correspondem a alvos nominais de 90% e 95%. A largura é a mediana entre motores de suas larguras medianas ao longo da trajetória. O limite inferior L fornece antecedência estimada L−t no marco; não a antecedência real até F ou uma ordem de remoção.

| subset | method | alpha | coverage_min | coverage_max | lower_coverage_min | lower_coverage_max | width_min | width_max | conservative_lead_min | conservative_lead_max |
|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | ISO | 0.050 | 0.920 | 0.960 | 0.960 | 0.960 | 54.381 | 58.217 | 12.934 | 17.000 |
| FD001 | ISO | 0.100 | 0.920 | 0.930 | 0.940 | 0.940 | 48.920 | 51.515 | 17.000 | 20.000 |
| FD001 | RF_HI | 0.050 | 0.940 | 0.950 | 0.950 | 0.970 | 57.121 | 63.540 | 9.783 | 12.103 |
| FD001 | RF_HI | 0.100 | 0.910 | 0.940 | 0.890 | 0.940 | 54.596 | 58.820 | 10.345 | 15.552 |
| FD001 | RF_SLOPE | 0.050 | 0.960 | 0.970 | 0.950 | 0.980 | 55.495 | 61.912 | 0.000 | 12.158 |
| FD001 | RF_SLOPE | 0.100 | 0.890 | 0.970 | 0.910 | 0.940 | 51.988 | 57.658 | 6.096 | 14.266 |
| FD003 | ISO | 0.050 | 0.930 | 0.970 | 0.930 | 0.950 | 48.333 | 62.378 | 14.576 | 17.000 |
| FD003 | ISO | 0.100 | 0.820 | 0.940 | 0.900 | 0.920 | 39.567 | 47.145 | 16.148 | 19.000 |
| FD003 | RF_HI | 0.050 | 0.920 | 0.980 | 0.920 | 0.950 | 61.577 | 66.890 | 6.025 | 11.102 |
| FD003 | RF_HI | 0.100 | 0.860 | 0.910 | 0.880 | 0.920 | 49.627 | 54.122 | 10.495 | 12.706 |
| FD003 | RF_SLOPE | 0.050 | 0.890 | 0.950 | 0.900 | 0.940 | 55.720 | 66.050 | 6.660 | 7.744 |
| FD003 | RF_SLOPE | 0.100 | 0.860 | 0.900 | 0.830 | 0.930 | 48.716 | 50.639 | 9.784 | 12.182 |

![Cobertura, largura e antecedência estimada](uncertainty_tradeoff.png)

## Cobertura por motor e por repetição

path_coverage exige que T esteja na banda em TODOS os ciclos observados desde a passagem com atributos disponíveis; path_lower_coverage exige L(t)≤T em todos esses ciclos. As duas bandas têm calibrações diferentes, bilateral e unilateral. Um alvo nominal não é um requisito aeronáutico de safety. As coberturas observadas podem ficar abaixo do alvo em uma divisão finita; isso não refuta por si uma propriedade marginal sob permutabilidade.

| subset | repeat | method | alpha | path_available | path_coverage | path_lower_coverage | median_width | conservative_lead_median | collapsed_point_fraction | calibration_n_min | finite_abs_fraction |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | ISO | 0.050 | 100 | 0.920 | 0.960 | 54.381 | 17.000 | 0.000 | 20 | 1.000 |
| FD001 | 1 | ISO | 0.100 | 100 | 0.920 | 0.940 | 51.422 | 19.674 | 0.000 | 20 | 1.000 |
| FD001 | 1 | RF_HI | 0.050 | 100 | 0.940 | 0.970 | 63.540 | 11.959 | 0.180 | 20 | 1.000 |
| FD001 | 1 | RF_HI | 0.100 | 100 | 0.910 | 0.940 | 58.820 | 13.976 | 0.020 | 20 | 1.000 |
| FD001 | 1 | RF_SLOPE | 0.050 | 100 | 0.960 | 0.970 | 61.912 | 12.158 | 0.220 | 20 | 1.000 |
| FD001 | 1 | RF_SLOPE | 0.100 | 100 | 0.900 | 0.910 | 57.360 | 14.266 | 0.130 | 20 | 1.000 |
| FD001 | 2 | ISO | 0.050 | 100 | 0.960 | 0.960 | 54.494 | 17.000 | 0.000 | 20 | 1.000 |
| FD001 | 2 | ISO | 0.100 | 100 | 0.930 | 0.940 | 48.920 | 20.000 | 0.000 | 20 | 1.000 |
| FD001 | 2 | RF_HI | 0.050 | 100 | 0.950 | 0.970 | 57.121 | 12.103 | 0.050 | 20 | 1.000 |
| FD001 | 2 | RF_HI | 0.100 | 100 | 0.940 | 0.890 | 54.596 | 15.552 | 0.000 | 20 | 1.000 |
| FD001 | 2 | RF_SLOPE | 0.050 | 100 | 0.970 | 0.950 | 60.970 | 1.460 | 0.420 | 20 | 1.000 |
| FD001 | 2 | RF_SLOPE | 0.100 | 100 | 0.970 | 0.940 | 57.658 | 11.467 | 0.260 | 20 | 1.000 |
| FD001 | 3 | ISO | 0.050 | 100 | 0.960 | 0.960 | 58.217 | 12.934 | 0.000 | 20 | 1.000 |
| FD001 | 3 | ISO | 0.100 | 100 | 0.930 | 0.940 | 51.515 | 17.000 | 0.000 | 20 | 1.000 |
| FD001 | 3 | RF_HI | 0.050 | 100 | 0.950 | 0.950 | 61.702 | 9.783 | 0.020 | 20 | 1.000 |
| FD001 | 3 | RF_HI | 0.100 | 100 | 0.940 | 0.920 | 56.893 | 10.345 | 0.020 | 20 | 1.000 |
| FD001 | 3 | RF_SLOPE | 0.050 | 100 | 0.960 | 0.980 | 55.495 | 0.000 | 0.650 | 20 | 1.000 |
| FD001 | 3 | RF_SLOPE | 0.100 | 100 | 0.890 | 0.940 | 51.988 | 6.096 | 0.120 | 20 | 1.000 |
| FD003 | 1 | ISO | 0.050 | 100 | 0.970 | 0.950 | 62.378 | 16.000 | 0.000 | 20 | 1.000 |
| FD003 | 1 | ISO | 0.100 | 100 | 0.940 | 0.920 | 47.145 | 18.000 | 0.000 | 20 | 1.000 |
| FD003 | 1 | RF_HI | 0.050 | 100 | 0.980 | 0.920 | 66.890 | 8.828 | 0.150 | 20 | 1.000 |
| FD003 | 1 | RF_HI | 0.100 | 100 | 0.900 | 0.880 | 52.684 | 10.495 | 0.080 | 20 | 1.000 |
| FD003 | 1 | RF_SLOPE | 0.050 | 100 | 0.950 | 0.900 | 61.632 | 7.744 | 0.280 | 20 | 1.000 |
| FD003 | 1 | RF_SLOPE | 0.100 | 100 | 0.900 | 0.830 | 50.639 | 12.182 | 0.120 | 20 | 1.000 |
| FD003 | 2 | ISO | 0.050 | 100 | 0.930 | 0.930 | 48.333 | 14.576 | 0.000 | 20 | 1.000 |
| FD003 | 2 | ISO | 0.100 | 100 | 0.820 | 0.910 | 39.567 | 16.148 | 0.000 | 20 | 1.000 |
| FD003 | 2 | RF_HI | 0.050 | 100 | 0.920 | 0.950 | 61.577 | 6.025 | 0.130 | 20 | 1.000 |
| FD003 | 2 | RF_HI | 0.100 | 100 | 0.860 | 0.920 | 49.627 | 10.969 | 0.040 | 20 | 1.000 |
| FD003 | 2 | RF_SLOPE | 0.050 | 100 | 0.890 | 0.930 | 55.720 | 6.892 | 0.240 | 20 | 1.000 |
| FD003 | 2 | RF_SLOPE | 0.100 | 100 | 0.860 | 0.860 | 48.716 | 11.031 | 0.150 | 20 | 1.000 |
| FD003 | 3 | ISO | 0.050 | 100 | 0.950 | 0.940 | 60.771 | 17.000 | 0.000 | 20 | 1.000 |
| FD003 | 3 | ISO | 0.100 | 100 | 0.870 | 0.900 | 45.696 | 19.000 | 0.000 | 20 | 1.000 |
| FD003 | 3 | RF_HI | 0.050 | 100 | 0.940 | 0.930 | 65.403 | 11.102 | 0.050 | 20 | 1.000 |
| FD003 | 3 | RF_HI | 0.100 | 100 | 0.910 | 0.880 | 54.122 | 12.706 | 0.000 | 20 | 1.000 |
| FD003 | 3 | RF_SLOPE | 0.050 | 100 | 0.930 | 0.940 | 66.050 | 6.660 | 0.180 | 20 | 1.000 |
| FD003 | 3 | RF_SLOPE | 0.100 | 100 | 0.870 | 0.930 | 50.524 | 9.784 | 0.090 | 20 | 1.000 |

## Calibrar no marco não equivale a calibrar a trajetória

scope=point usa somente o erro no primeiro marco de cada motor U. scope=path usa o maior erro da trajetória, um escore por motor. A tabela compara ambos os usos no alvo nominal de 90%; aplicar a banda pontual em todos os ciclos não lhe concede cobertura simultânea.

| subset | repeat | method | scope | point_coverage | path_coverage | point_lower_coverage | path_lower_coverage |
|---|---|---|---|---|---|---|---|
| FD001 | 1 | ISO | path | 0.920 | 0.920 | 0.950 | 0.940 |
| FD001 | 1 | ISO | point | 0.890 | 0.860 | 0.940 | 0.870 |
| FD001 | 1 | RF_HI | path | 0.980 | 0.910 | 0.990 | 0.940 |
| FD001 | 1 | RF_HI | point | 0.900 | 0.770 | 0.920 | 0.720 |
| FD001 | 1 | RF_SLOPE | path | 0.970 | 0.900 | 0.990 | 0.910 |
| FD001 | 1 | RF_SLOPE | point | 0.940 | 0.780 | 0.930 | 0.700 |
| FD001 | 2 | ISO | path | 0.930 | 0.930 | 0.940 | 0.940 |
| FD001 | 2 | ISO | point | 0.930 | 0.930 | 0.910 | 0.870 |
| FD001 | 2 | RF_HI | path | 0.950 | 0.940 | 0.990 | 0.890 |
| FD001 | 2 | RF_HI | point | 0.920 | 0.860 | 0.930 | 0.720 |
| FD001 | 2 | RF_SLOPE | path | 0.980 | 0.970 | 0.980 | 0.940 |
| FD001 | 2 | RF_SLOPE | point | 0.950 | 0.890 | 0.920 | 0.690 |
| FD001 | 3 | ISO | path | 0.940 | 0.930 | 0.960 | 0.940 |
| FD001 | 3 | ISO | point | 0.930 | 0.930 | 0.950 | 0.890 |
| FD001 | 3 | RF_HI | path | 0.960 | 0.940 | 0.980 | 0.920 |
| FD001 | 3 | RF_HI | point | 0.910 | 0.840 | 0.970 | 0.800 |
| FD001 | 3 | RF_SLOPE | path | 0.960 | 0.890 | 0.970 | 0.940 |
| FD001 | 3 | RF_SLOPE | point | 0.880 | 0.750 | 0.910 | 0.750 |
| FD003 | 1 | ISO | path | 0.940 | 0.940 | 0.930 | 0.920 |
| FD003 | 1 | ISO | point | 0.940 | 0.920 | 0.880 | 0.820 |
| FD003 | 1 | RF_HI | path | 0.930 | 0.900 | 0.970 | 0.880 |
| FD003 | 1 | RF_HI | point | 0.890 | 0.780 | 0.850 | 0.620 |
| FD003 | 1 | RF_SLOPE | path | 0.970 | 0.900 | 0.990 | 0.830 |
| FD003 | 1 | RF_SLOPE | point | 0.910 | 0.820 | 0.950 | 0.760 |
| FD003 | 2 | ISO | path | 0.860 | 0.820 | 0.950 | 0.910 |
| FD003 | 2 | ISO | point | 0.840 | 0.790 | 0.920 | 0.860 |
| FD003 | 2 | RF_HI | path | 0.930 | 0.860 | 0.990 | 0.920 |
| FD003 | 2 | RF_HI | point | 0.840 | 0.720 | 0.910 | 0.720 |
| FD003 | 2 | RF_SLOPE | path | 0.960 | 0.860 | 0.980 | 0.860 |
| FD003 | 2 | RF_SLOPE | point | 0.880 | 0.600 | 0.880 | 0.580 |
| FD003 | 3 | ISO | path | 0.890 | 0.870 | 0.950 | 0.900 |
| FD003 | 3 | ISO | point | 0.880 | 0.840 | 0.930 | 0.880 |
| FD003 | 3 | RF_HI | path | 0.940 | 0.910 | 0.970 | 0.880 |
| FD003 | 3 | RF_HI | point | 0.880 | 0.760 | 0.930 | 0.830 |
| FD003 | 3 | RF_SLOPE | path | 0.960 | 0.870 | 1.000 | 0.930 |
| FD003 | 3 | RF_SLOPE | point | 0.940 | 0.750 | 0.970 | 0.820 |

## Teste truncado — apenas a trajetória observada

Motores sem passagem não recebem sensores ou cruzamentos futuros inventados. A RUL oficial permite avaliar T, mas não observar a qualidade das previsões depois do truncamento. Assim, cobertura de toda a trajetória observada no teste não é cobertura de toda a vida.

| subset | repeat | method | alpha | total | path_available | point_available | path_coverage | path_lower_coverage | median_width | conservative_lead_median |
|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | ISO | 0.050 | 100 | 27 | 27 | 1.000 | 0.963 | 76.278 | 19.652 |
| FD001 | 1 | ISO | 0.100 | 100 | 27 | 27 | 1.000 | 0.963 | 75.278 | 20.434 |
| FD001 | 1 | RF_HI | 0.050 | 100 | 27 | 27 | 1.000 | 0.963 | 79.834 | 15.280 |
| FD001 | 1 | RF_HI | 0.100 | 100 | 27 | 27 | 1.000 | 0.963 | 79.351 | 16.757 |
| FD001 | 1 | RF_SLOPE | 0.050 | 100 | 27 | 27 | 1.000 | 0.963 | 73.254 | 14.050 |
| FD001 | 1 | RF_SLOPE | 0.100 | 100 | 27 | 27 | 1.000 | 0.963 | 72.283 | 17.564 |
| FD001 | 2 | ISO | 0.050 | 100 | 27 | 27 | 0.963 | 0.889 | 65.504 | 21.876 |
| FD001 | 2 | ISO | 0.100 | 100 | 27 | 27 | 0.926 | 0.889 | 49.944 | 21.876 |
| FD001 | 2 | RF_HI | 0.050 | 100 | 27 | 27 | 0.963 | 1.000 | 67.986 | 11.317 |
| FD001 | 2 | RF_HI | 0.100 | 100 | 27 | 27 | 0.926 | 0.889 | 55.733 | 15.295 |
| FD001 | 2 | RF_SLOPE | 0.050 | 100 | 27 | 27 | 0.926 | 1.000 | 56.623 | 2.114 |
| FD001 | 2 | RF_SLOPE | 0.100 | 100 | 27 | 27 | 0.926 | 0.926 | 56.292 | 13.598 |
| FD001 | 3 | ISO | 0.050 | 100 | 27 | 27 | 0.963 | 1.000 | 64.897 | 15.000 |
| FD001 | 3 | ISO | 0.100 | 100 | 27 | 27 | 0.926 | 1.000 | 62.026 | 16.000 |
| FD001 | 3 | RF_HI | 0.050 | 100 | 27 | 27 | 0.963 | 1.000 | 69.967 | 4.687 |
| FD001 | 3 | RF_HI | 0.100 | 100 | 27 | 27 | 0.963 | 1.000 | 69.038 | 6.321 |
| FD001 | 3 | RF_SLOPE | 0.050 | 100 | 27 | 27 | 1.000 | 1.000 | 71.747 | 0.000 |
| FD001 | 3 | RF_SLOPE | 0.100 | 100 | 27 | 27 | 0.815 | 0.852 | 58.648 | 9.077 |
| FD003 | 1 | ISO | 0.050 | 100 | 24 | 24 | 0.917 | 1.000 | 65.351 | 16.000 |
| FD003 | 1 | ISO | 0.100 | 100 | 24 | 24 | 0.917 | 0.958 | 59.351 | 18.000 |
| FD003 | 1 | RF_HI | 0.050 | 100 | 24 | 24 | 0.917 | 1.000 | 71.209 | 7.979 |
| FD003 | 1 | RF_HI | 0.100 | 100 | 24 | 24 | 0.917 | 1.000 | 63.446 | 8.901 |
| FD003 | 1 | RF_SLOPE | 0.050 | 100 | 24 | 24 | 0.958 | 1.000 | 68.912 | 11.278 |
| FD003 | 1 | RF_SLOPE | 0.100 | 100 | 24 | 24 | 0.958 | 0.958 | 56.818 | 14.953 |
| FD003 | 2 | ISO | 0.050 | 100 | 24 | 24 | 0.917 | 1.000 | 54.606 | 10.744 |
| FD003 | 2 | ISO | 0.100 | 100 | 24 | 24 | 0.917 | 1.000 | 49.721 | 15.000 |
| FD003 | 2 | RF_HI | 0.050 | 100 | 24 | 24 | 0.958 | 1.000 | 63.315 | 1.465 |
| FD003 | 2 | RF_HI | 0.100 | 100 | 24 | 24 | 0.917 | 1.000 | 58.345 | 8.637 |
| FD003 | 2 | RF_SLOPE | 0.050 | 100 | 24 | 24 | 0.958 | 1.000 | 61.300 | 13.727 |
| FD003 | 2 | RF_SLOPE | 0.100 | 100 | 24 | 24 | 0.958 | 1.000 | 58.100 | 15.990 |
| FD003 | 3 | ISO | 0.050 | 100 | 25 | 25 | 0.960 | 1.000 | 70.746 | 17.000 |
| FD003 | 3 | ISO | 0.100 | 100 | 25 | 25 | 0.920 | 0.920 | 44.939 | 19.628 |
| FD003 | 3 | RF_HI | 0.050 | 100 | 25 | 25 | 0.960 | 0.960 | 78.393 | 7.819 |
| FD003 | 3 | RF_HI | 0.100 | 100 | 25 | 25 | 0.880 | 0.880 | 58.960 | 9.423 |
| FD003 | 3 | RF_SLOPE | 0.050 | 100 | 25 | 25 | 1.000 | 1.000 | 80.718 | 7.368 |
| FD003 | 3 | RF_SLOPE | 0.100 | 100 | 25 | 25 | 0.920 | 1.000 | 62.390 | 11.169 |

## Calibração e fontes

Quantil = escore ordenado de rank ceil((n+1)(1−alpha)), com +infinito quando esse rank excede n. Os quantis individuais de cada partição estão em quantiles.csv; não se substitui o caso não finito por um máximo amostral. Parâmetros HI, modelos e quantis foram congelados antes da avaliação, com rastreabilidade em execution_start.json, freezes.json e metadata.json.

| subset | method | scope | alpha | n_min | n_max | q_abs_min | q_abs_max | q_late_min | q_late_max |
|---|---|---|---|---|---|---|---|---|---|
| FD001 | ISO | path | 0.050 | 20 | 20 | 24.959 | 51.167 | 12.769 | 32.384 |
| FD001 | ISO | path | 0.100 | 20 | 20 | 21.705 | 50.167 | 11.987 | 27.384 |
| FD001 | ISO | point | 0.050 | 20 | 20 | 23.959 | 51.167 | 8.833 | 31.384 |
| FD001 | ISO | point | 0.100 | 20 | 20 | 19.041 | 49.578 | 8.833 | 24.384 |
| FD001 | RF_HI | path | 0.050 | 20 | 20 | 28.949 | 54.074 | 18.889 | 45.892 |
| FD001 | RF_HI | path | 0.100 | 20 | 20 | 27.867 | 52.554 | 17.412 | 36.010 |
| FD001 | RF_HI | point | 0.050 | 20 | 20 | 25.761 | 53.037 | 9.339 | 31.552 |
| FD001 | RF_HI | point | 0.100 | 20 | 20 | 20.817 | 47.553 | 9.325 | 29.571 |
| FD001 | RF_SLOPE | path | 0.050 | 20 | 20 | 32.566 | 49.644 | 20.779 | 48.215 |
| FD001 | RF_SLOPE | path | 0.100 | 20 | 20 | 27.752 | 48.673 | 17.266 | 42.592 |
| FD001 | RF_SLOPE | point | 0.050 | 20 | 20 | 23.380 | 49.644 | 9.234 | 41.735 |
| FD001 | RF_SLOPE | point | 0.100 | 20 | 20 | 19.470 | 46.841 | 6.129 | 40.434 |
| FD003 | ISO | path | 0.050 | 20 | 20 | 22.833 | 57.060 | 14.406 | 28.139 |
| FD003 | ISO | path | 0.100 | 20 | 20 | 16.018 | 36.961 | 12.406 | 26.139 |
| FD003 | ISO | point | 0.050 | 20 | 20 | 22.833 | 54.800 | 12.406 | 26.689 |
| FD003 | ISO | point | 0.100 | 20 | 20 | 15.200 | 35.901 | 10.996 | 23.355 |
| FD003 | RF_HI | path | 0.050 | 20 | 20 | 28.250 | 60.801 | 18.810 | 41.938 |
| FD003 | RF_HI | path | 0.100 | 20 | 20 | 25.091 | 41.938 | 17.888 | 38.336 |
| FD003 | RF_HI | point | 0.050 | 20 | 20 | 24.165 | 53.779 | 13.227 | 39.355 |
| FD003 | RF_HI | point | 0.100 | 20 | 20 | 17.746 | 40.598 | 6.526 | 34.986 |
| FD003 | RF_SLOPE | path | 0.050 | 20 | 20 | 24.716 | 60.017 | 19.073 | 40.780 |
| FD003 | RF_SLOPE | path | 0.100 | 20 | 20 | 22.849 | 37.354 | 16.874 | 34.703 |
| FD003 | RF_SLOPE | point | 0.050 | 20 | 20 | 24.473 | 60.017 | 14.047 | 37.260 |
| FD003 | RF_SLOPE | point | 0.100 | 20 | 20 | 18.507 | 32.292 | 10.503 | 29.675 |

A ordem estatística corrigida e a separação ajuste/calibração seguem [Lei et al. (2018), seção 2 e seção 2.2/Algoritmo 2](https://www.stat.cmu.edu/~ryantibs/papers/conformal-jasa.pdf), DOI 10.1080/01621459.2017.1307116. O escore máximo temporal por motor e o domínio após o marco são nossa adaptação experimental. Permutabilidade, reutilização histórica, pequena calibração e mudança de distribuição limitam a interpretação; não há garantia condicional por estado, validação física do HI ou admissibilidade operacional demonstrada.

Não foram escolhidas políticas de remoção, tolerâncias operacionais ou custos adicionais. Não houve inspeções, alteração da forma HI, busca de outra fórmula ou edição do artigo M17. Todos os resultados, repetições, casos ausentes e diferenças desfavoráveis permanecem arquivados.
