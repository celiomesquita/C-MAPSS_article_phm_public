# P11.1 — controle do marco de condição e ganho incremental do prognóstico

[Protocolo anterior a esta execução](../../protocolo_controle_marco_11a.md). A análise foi motivada por P11 e usa os mesmos motores já examinados. Não é confirmação independente. Índice de saúde (HI) supervisionado P10 congelado, disponibilidade ≥39, mesma passagem causal de 0,5 e mesmos prazos d=1/2. O controle decide no primeiro marco disponível, retira d ciclos depois e não usa conversor de F, quantil, endpoint ou reserva 15/12.

Os 100 motores de cada domínio se repetem nas três divisões; não são 300 unidades independentes. ISO é regressão isotônica; RF_SLOPE é floresta aleatória com HI e inclinação causal. O controle HI utiliza os mesmos parâmetros supervisionados aprendidos em F; retirar o conversor não torna a construção do HI independente da vida remanescente.

## Controle simples nos motores completos

| subset | repeat | policy_id | total | decisions | without_decision | late_count | exact_count | mean_utilised | mean_unused | cost_per_cycle |
|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | HI_MARKER_D1 | 100 | 100 | 0 | 0 | 0 | 168.0200 | 38.2900 | 0.0060 |
| FD001 | 1 | HI_MARKER_D2 | 100 | 100 | 0 | 0 | 0 | 169.0200 | 37.2900 | 0.0059 |
| FD001 | 2 | HI_MARKER_D1 | 100 | 100 | 0 | 0 | 0 | 166.6900 | 39.6200 | 0.0060 |
| FD001 | 2 | HI_MARKER_D2 | 100 | 100 | 0 | 0 | 0 | 167.6900 | 38.6200 | 0.0060 |
| FD001 | 3 | HI_MARKER_D1 | 100 | 100 | 0 | 0 | 0 | 167.0800 | 39.2300 | 0.0060 |
| FD001 | 3 | HI_MARKER_D2 | 100 | 100 | 0 | 0 | 0 | 168.0800 | 38.2300 | 0.0059 |
| FD003 | 1 | HI_MARKER_D1 | 100 | 100 | 0 | 0 | 0 | 208.8600 | 38.3400 | 0.0048 |
| FD003 | 1 | HI_MARKER_D2 | 100 | 100 | 0 | 0 | 0 | 209.8600 | 37.3400 | 0.0048 |
| FD003 | 2 | HI_MARKER_D1 | 100 | 100 | 0 | 0 | 0 | 204.9800 | 42.2200 | 0.0049 |
| FD003 | 2 | HI_MARKER_D2 | 100 | 100 | 0 | 0 | 0 | 205.9800 | 41.2200 | 0.0049 |
| FD003 | 3 | HI_MARKER_D1 | 100 | 100 | 0 | 0 | 0 | 209.1600 | 38.0400 | 0.0048 |
| FD003 | 3 | HI_MARKER_D2 | 100 | 100 | 0 | 0 | 0 | 210.1600 | 37.0400 | 0.0048 |

## Incremento sobre HI: limite inferior 98% e reserva de referência 15

same_date e later_date são contagens nos mesmos 100 motores. Ganho de vida é a diferença média de ciclos simulados aproveitados. Intervalos descritivos de 95%, por 2000 reamostragens pareadas de motores, por repetição e condicionais a modelos congelados. A economia percentual é relativa ao controle HI, não à idade fixa ou a uma companhia.

| subset | repeat | policy_id | same_date | later_date | candidate_without_decision | candidate_reached | reference_reached | delta_mean_life | life_ci_low | life_ci_high | saving_percent | saving_low_percent | saving_high_percent |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | ISO_LOWER98_M15_D1 | 75 | 25 | 0 | 0 | 0 | 0.4800 | 0.3000 | 0.6800 | 0.2849 | 0.1778 | 0.4039 |
| FD001 | 1 | ISO_LOWER98_M15_D2 | 86 | 14 | 0 | 0 | 0 | 0.2100 | 0.1100 | 0.3300 | 0.1241 | 0.0643 | 0.1939 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D1 | 88 | 12 | 0 | 0 | 0 | 0.7400 | 0.3100 | 1.2400 | 0.4385 | 0.1905 | 0.7261 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D2 | 88 | 12 | 0 | 0 | 0 | 0.7200 | 0.3100 | 1.2500 | 0.4242 | 0.1854 | 0.7177 |
| FD001 | 2 | ISO_LOWER98_M15_D1 | 70 | 30 | 0 | 0 | 0 | 0.7200 | 0.4800 | 0.9700 | 0.4301 | 0.2894 | 0.5777 |
| FD001 | 2 | ISO_LOWER98_M15_D2 | 80 | 20 | 0 | 0 | 0 | 0.5500 | 0.3200 | 0.8100 | 0.3269 | 0.1910 | 0.4798 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D1 | 87 | 13 | 0 | 0 | 0 | 0.3900 | 0.1497 | 0.7200 | 0.2334 | 0.0883 | 0.4254 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D2 | 89 | 11 | 0 | 0 | 0 | 0.2800 | 0.1100 | 0.4900 | 0.1667 | 0.0664 | 0.2866 |
| FD001 | 3 | ISO_LOWER98_M15_D1 | 55 | 45 | 0 | 0 | 0 | 1.5700 | 1.1497 | 2.0300 | 0.9309 | 0.6854 | 1.1917 |
| FD001 | 3 | ISO_LOWER98_M15_D2 | 65 | 35 | 0 | 0 | 0 | 1.1500 | 0.7798 | 1.5400 | 0.6795 | 0.4618 | 0.9074 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D1 | 84 | 16 | 0 | 0 | 0 | 1.0900 | 0.5500 | 1.7300 | 0.6482 | 0.3387 | 1.0105 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D2 | 86 | 14 | 0 | 0 | 0 | 1.0500 | 0.5400 | 1.6800 | 0.6208 | 0.3225 | 0.9768 |
| FD003 | 1 | ISO_LOWER98_M15_D1 | 72 | 28 | 0 | 0 | 0 | 0.8300 | 0.5100 | 1.2000 | 0.3958 | 0.2474 | 0.5695 |
| FD003 | 1 | ISO_LOWER98_M15_D2 | 90 | 10 | 0 | 0 | 0 | 0.3500 | 0.1400 | 0.5800 | 0.1665 | 0.0705 | 0.2757 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D1 | 86 | 14 | 0 | 0 | 0 | 0.5400 | 0.1400 | 1.0900 | 0.2579 | 0.0700 | 0.5090 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D2 | 87 | 13 | 0 | 0 | 0 | 0.4100 | 0.1400 | 0.7800 | 0.1950 | 0.0667 | 0.3619 |
| FD003 | 2 | ISO_LOWER98_M15_D1 | 74 | 26 | 0 | 0 | 0 | 0.7200 | 0.4200 | 1.0400 | 0.3500 | 0.2067 | 0.5068 |
| FD003 | 2 | ISO_LOWER98_M15_D2 | 80 | 20 | 0 | 0 | 0 | 0.6000 | 0.3297 | 0.9400 | 0.2904 | 0.1574 | 0.4555 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D1 | 91 | 9 | 0 | 0 | 0 | 0.4900 | 0.1300 | 0.9902 | 0.2385 | 0.0633 | 0.4718 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D2 | 93 | 7 | 0 | 0 | 0 | 0.4700 | 0.1100 | 0.9700 | 0.2277 | 0.0517 | 0.4599 |
| FD003 | 3 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| FD003 | 3 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D1 | 89 | 11 | 0 | 0 | 0 | 0.2400 | 0.0800 | 0.4500 | 0.1146 | 0.0395 | 0.2123 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D2 | 89 | 11 | 0 | 0 | 0 | 0.2400 | 0.0800 | 0.4400 | 0.1141 | 0.0385 | 0.2091 |

![Vida adicional sobre o controle de HI](incremental_life.png)

## De onde veio o ganho frente à idade fixa?

A tabela mostra mínimo/máximo das parcelas entre três repetições; não são intervalos de confiança. prognosis_share é a parcela do ganho MÉDIO DE VIDA frente à idade fixa que ocorre depois do controle HI. marker_share é a parcela já obtida pelo marco. Não são parcelas de poupança monetária e não demonstram decomposição causal externa. As parcelas de vida são aditivas; percentagens de economia não são: os fatores de custo se multiplicam, conforme o protocolo.

| subset | policy_id | life_added_min | life_added_max | prognosis_share_min | prognosis_share_max | marker_share_min | marker_share_max |
|---|---|---|---|---|---|---|---|
| FD001 | ISO_LOWER98_M15_D1 | 0.4800 | 1.5700 | 0.0142 | 0.0407 | 0.9593 | 0.9858 |
| FD001 | ISO_LOWER98_M15_D2 | 0.2100 | 1.1500 | 0.0061 | 0.0294 | 0.9706 | 0.9939 |
| FD001 | RF_SLOPE_LOWER98_M15_D1 | 0.3900 | 1.0900 | 0.0108 | 0.0286 | 0.9714 | 0.9892 |
| FD001 | RF_SLOPE_LOWER98_M15_D2 | 0.2800 | 1.0500 | 0.0076 | 0.0269 | 0.9731 | 0.9924 |
| FD003 | ISO_LOWER98_M15_D1 | 0.0000 | 0.8300 | 0.0000 | 0.0131 | 0.9869 | 1.0000 |
| FD003 | ISO_LOWER98_M15_D2 | 0.0000 | 0.6000 | 0.0000 | 0.0098 | 0.9902 | 1.0000 |
| FD003 | RF_SLOPE_LOWER98_M15_D1 | 0.2400 | 0.5400 | 0.0039 | 0.0085 | 0.9915 | 0.9961 |
| FD003 | RF_SLOPE_LOWER98_M15_D2 | 0.2400 | 0.4700 | 0.0039 | 0.0077 | 0.9923 | 0.9961 |

## HI versus idade fixa

A idade é o controle P11 conservador, definido em F∪C e sujeito aos eventos externos já registrados. Não trocar sua definição para favorecer a narrativa; a comparação não é entre políticas de admissibilidade equivalente ou práticas reais de uma companhia.

| subset | repeat | policy_id | delay | reference | common | same_date | later_date | earlier_date | candidate_without_decision | candidate_reached | reference_reached | delta_mean_life | life_ci_low | life_ci_high | relative_saving | saving_ci_low | saving_ci_high |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | HI_MARKER_D1 | 1 | AGE_D1 | 100 | 0 | 83 | 14 | 0 | 0 | 3 | 33.3000 | 26.6693 | 39.9305 | 0.1982 | 0.1650 | 0.2292 |
| FD001 | 1 | HI_MARKER_D2 | 2 | AGE_D2 | 100 | 1 | 83 | 14 | 0 | 0 | 3 | 34.3000 | 27.9292 | 41.3702 | 0.2029 | 0.1713 | 0.2348 |
| FD001 | 2 | HI_MARKER_D1 | 1 | AGE_D1 | 100 | 1 | 86 | 12 | 0 | 0 | 1 | 35.6700 | 29.4085 | 42.6600 | 0.2140 | 0.1831 | 0.2457 |
| FD001 | 2 | HI_MARKER_D2 | 2 | AGE_D2 | 100 | 0 | 87 | 12 | 0 | 0 | 1 | 36.6700 | 30.5287 | 43.5300 | 0.2187 | 0.1889 | 0.2491 |
| FD001 | 3 | HI_MARKER_D1 | 1 | AGE_D1 | 100 | 1 | 87 | 11 | 0 | 0 | 1 | 36.9600 | 30.5600 | 43.7200 | 0.2212 | 0.1902 | 0.2516 |
| FD001 | 3 | HI_MARKER_D2 | 2 | AGE_D2 | 100 | 0 | 88 | 11 | 0 | 0 | 1 | 37.9600 | 31.6698 | 44.6610 | 0.2258 | 0.1957 | 0.2559 |
| FD003 | 1 | HI_MARKER_D1 | 1 | AGE_D1 | 100 | 3 | 83 | 12 | 0 | 0 | 2 | 62.7000 | 48.9975 | 78.0242 | 0.3002 | 0.2510 | 0.3480 |
| FD003 | 1 | HI_MARKER_D2 | 2 | AGE_D2 | 100 | 1 | 86 | 12 | 0 | 0 | 2 | 63.7000 | 49.8545 | 79.6907 | 0.3035 | 0.2539 | 0.3528 |
| FD003 | 2 | HI_MARKER_D1 | 1 | AGE_D1 | 100 | 0 | 83 | 16 | 0 | 0 | 1 | 59.7400 | 46.0195 | 73.8342 | 0.2914 | 0.2404 | 0.3372 |
| FD003 | 2 | HI_MARKER_D2 | 2 | AGE_D2 | 100 | 4 | 83 | 12 | 0 | 0 | 1 | 60.7400 | 47.5278 | 75.4917 | 0.2949 | 0.2466 | 0.3418 |
| FD003 | 3 | HI_MARKER_D1 | 1 | AGE_D1 | 100 | 2 | 81 | 15 | 0 | 0 | 2 | 60.5500 | 46.8155 | 75.0435 | 0.2895 | 0.2392 | 0.3360 |
| FD003 | 3 | HI_MARKER_D2 | 2 | AGE_D2 | 100 | 0 | 83 | 16 | 0 | 0 | 2 | 61.5500 | 47.5180 | 76.1315 | 0.2929 | 0.2425 | 0.3384 |

## Todas as regras: vida e eventos permanecem associados

A previsão central pode prolongar mais a vida enquanto deixa falhas sem prevenção. Esse ganho não será tratado como vantagem económica admissível. As sensibilidades 95% e reserva12 permanecem comparações, sem adoção. A maior vida frente ao primeiro marco é estrutural para regras que só podem actuar depois dele; portanto, um intervalo positivo por si só não demonstra utilidade de informação prognóstica ou segurança.

| subset | repeat | policy_id | delay | reference | common | same_date | later_date | earlier_date | candidate_without_decision | candidate_reached | reference_reached | delta_mean_life | life_ci_low | life_ci_high | relative_saving | saving_ci_low | saving_ci_high |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | ISO_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 11 | 89 | 0 | 0 | 0 | 0 | 4.1700 | 3.4398 | 4.9600 | 0.0242 | 0.0201 | 0.0285 |
| FD001 | 1 | ISO_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 27 | 73 | 0 | 0 | 0 | 0 | 3.6000 | 2.9000 | 4.3802 | 0.0209 | 0.0169 | 0.0250 |
| FD001 | 1 | ISO_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 49 | 51 | 0 | 0 | 0 | 0 | 1.7200 | 1.2197 | 2.2702 | 0.0101 | 0.0072 | 0.0135 |
| FD001 | 1 | ISO_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 66 | 34 | 0 | 0 | 0 | 0 | 1.3700 | 0.8800 | 1.9500 | 0.0080 | 0.0051 | 0.0115 |
| FD001 | 1 | ISO_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 53 | 47 | 0 | 0 | 0 | 0 | 2.2700 | 1.5597 | 2.9500 | 0.0133 | 0.0092 | 0.0172 |
| FD001 | 1 | ISO_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 61 | 39 | 0 | 0 | 0 | 0 | 0.7100 | 0.5100 | 0.9202 | 0.0042 | 0.0030 | 0.0054 |
| FD001 | 1 | ISO_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 75 | 25 | 0 | 0 | 0 | 0 | 0.4800 | 0.3000 | 0.6800 | 0.0028 | 0.0018 | 0.0040 |
| FD001 | 1 | ISO_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 86 | 14 | 0 | 0 | 0 | 0 | 0.2100 | 0.1100 | 0.3300 | 0.0012 | 0.0006 | 0.0019 |
| FD001 | 1 | ISO_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 80 | 0 | 20 | 23 | 0 | 27.9500 | 26.2000 | 29.7600 | 0.1426 | 0.1369 | 0.1481 |
| FD001 | 1 | ISO_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 87 | 0 | 13 | 23 | 0 | 26.3000 | 24.6097 | 27.9602 | 0.1347 | 0.1291 | 0.1399 |
| FD001 | 1 | ISO_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 95 | 0 | 5 | 7 | 0 | 23.1100 | 21.6998 | 24.5102 | 0.1209 | 0.1162 | 0.1259 |
| FD001 | 1 | ISO_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 95 | 0 | 5 | 10 | 0 | 22.3000 | 20.9997 | 23.7200 | 0.1166 | 0.1117 | 0.1215 |
| FD001 | 1 | RF_SLOPE_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 73 | 27 | 0 | 0 | 0 | 0 | 2.0500 | 1.1500 | 3.0000 | 0.0121 | 0.0071 | 0.0171 |
| FD001 | 1 | RF_SLOPE_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 76 | 24 | 0 | 0 | 0 | 0 | 1.7900 | 1.0000 | 2.7400 | 0.0105 | 0.0060 | 0.0155 |
| FD001 | 1 | RF_SLOPE_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 80 | 20 | 0 | 0 | 0 | 0 | 1.3300 | 0.6500 | 2.1202 | 0.0079 | 0.0040 | 0.0122 |
| FD001 | 1 | RF_SLOPE_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 80 | 20 | 0 | 0 | 0 | 0 | 1.2900 | 0.6100 | 2.0800 | 0.0076 | 0.0038 | 0.0118 |
| FD001 | 1 | RF_SLOPE_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 82 | 18 | 0 | 0 | 0 | 0 | 1.3200 | 0.6400 | 2.1500 | 0.0078 | 0.0039 | 0.0123 |
| FD001 | 1 | RF_SLOPE_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 83 | 17 | 0 | 0 | 0 | 0 | 1.1200 | 0.5100 | 1.9000 | 0.0066 | 0.0031 | 0.0109 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 88 | 12 | 0 | 0 | 0 | 0 | 0.7400 | 0.3100 | 1.2400 | 0.0044 | 0.0019 | 0.0073 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 88 | 12 | 0 | 0 | 0 | 0 | 0.7200 | 0.3100 | 1.2500 | 0.0042 | 0.0019 | 0.0072 |
| FD001 | 1 | RF_SLOPE_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 93 | 0 | 7 | 10 | 0 | 25.0600 | 22.8700 | 27.5005 | 0.1298 | 0.1223 | 0.1376 |
| FD001 | 1 | RF_SLOPE_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 94 | 0 | 6 | 10 | 0 | 24.0300 | 21.7697 | 26.5703 | 0.1245 | 0.1160 | 0.1327 |
| FD001 | 1 | RF_SLOPE_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 94 | 0 | 6 | 6 | 0 | 22.7900 | 20.5095 | 25.2003 | 0.1194 | 0.1107 | 0.1279 |
| FD001 | 1 | RF_SLOPE_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 95 | 0 | 5 | 6 | 0 | 21.5300 | 19.1500 | 23.9503 | 0.1130 | 0.1040 | 0.1218 |
| FD001 | 2 | ISO_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 8 | 92 | 0 | 0 | 0 | 0 | 5.9200 | 4.8998 | 6.9905 | 0.0343 | 0.0289 | 0.0398 |
| FD001 | 2 | ISO_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 8 | 92 | 0 | 0 | 0 | 0 | 5.6100 | 4.6600 | 6.6002 | 0.0324 | 0.0274 | 0.0377 |
| FD001 | 2 | ISO_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 26 | 74 | 0 | 0 | 0 | 0 | 2.5300 | 2.0900 | 3.0000 | 0.0150 | 0.0125 | 0.0175 |
| FD001 | 2 | ISO_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 41 | 59 | 0 | 0 | 0 | 0 | 1.5700 | 1.1900 | 1.9502 | 0.0093 | 0.0071 | 0.0114 |
| FD001 | 2 | ISO_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 48 | 52 | 0 | 0 | 0 | 0 | 3.3700 | 2.4100 | 4.4102 | 0.0198 | 0.0144 | 0.0257 |
| FD001 | 2 | ISO_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 49 | 51 | 0 | 0 | 0 | 0 | 2.6700 | 1.7700 | 3.7100 | 0.0157 | 0.0104 | 0.0214 |
| FD001 | 2 | ISO_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 70 | 30 | 0 | 0 | 0 | 0 | 0.7200 | 0.4800 | 0.9700 | 0.0043 | 0.0029 | 0.0058 |
| FD001 | 2 | ISO_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 80 | 20 | 0 | 0 | 0 | 0 | 0.5500 | 0.3200 | 0.8100 | 0.0033 | 0.0019 | 0.0048 |
| FD001 | 2 | ISO_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 82 | 0 | 18 | 23 | 0 | 29.0600 | 27.1998 | 31.0600 | 0.1485 | 0.1423 | 0.1548 |
| FD001 | 2 | ISO_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 86 | 0 | 14 | 23 | 0 | 27.6200 | 25.7500 | 29.5003 | 0.1414 | 0.1349 | 0.1481 |
| FD001 | 2 | ISO_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 89 | 0 | 11 | 15 | 0 | 26.4700 | 24.7395 | 28.4402 | 0.1370 | 0.1306 | 0.1441 |
| FD001 | 2 | ISO_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 92 | 0 | 8 | 10 | 0 | 24.2800 | 22.6898 | 26.0508 | 0.1265 | 0.1206 | 0.1324 |
| FD001 | 2 | RF_SLOPE_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 74 | 26 | 0 | 0 | 0 | 0 | 1.3600 | 0.6700 | 2.1502 | 0.0081 | 0.0041 | 0.0128 |
| FD001 | 2 | RF_SLOPE_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 76 | 24 | 0 | 0 | 0 | 0 | 1.2400 | 0.6100 | 2.1100 | 0.0073 | 0.0037 | 0.0122 |
| FD001 | 2 | RF_SLOPE_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 81 | 19 | 0 | 0 | 0 | 0 | 0.7800 | 0.3900 | 1.3000 | 0.0047 | 0.0024 | 0.0075 |
| FD001 | 2 | RF_SLOPE_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 84 | 16 | 0 | 0 | 0 | 0 | 0.6600 | 0.2900 | 1.1200 | 0.0039 | 0.0018 | 0.0066 |
| FD001 | 2 | RF_SLOPE_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 81 | 19 | 0 | 0 | 0 | 0 | 1.0400 | 0.4298 | 1.8700 | 0.0062 | 0.0026 | 0.0109 |
| FD001 | 2 | RF_SLOPE_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 83 | 17 | 0 | 0 | 0 | 0 | 0.9500 | 0.3598 | 1.7600 | 0.0056 | 0.0021 | 0.0102 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 87 | 13 | 0 | 0 | 0 | 0 | 0.3900 | 0.1497 | 0.7200 | 0.0023 | 0.0009 | 0.0043 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 89 | 11 | 0 | 0 | 0 | 0 | 0.2800 | 0.1100 | 0.4900 | 0.0017 | 0.0007 | 0.0029 |
| FD001 | 2 | RF_SLOPE_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 87 | 0 | 13 | 13 | 0 | 26.5000 | 24.1797 | 28.9902 | 0.1372 | 0.1287 | 0.1456 |
| FD001 | 2 | RF_SLOPE_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 91 | 0 | 9 | 13 | 0 | 25.7100 | 23.2300 | 28.1805 | 0.1329 | 0.1243 | 0.1416 |
| FD001 | 2 | RF_SLOPE_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 93 | 0 | 7 | 8 | 0 | 24.1800 | 21.9698 | 26.6715 | 0.1267 | 0.1185 | 0.1356 |
| FD001 | 2 | RF_SLOPE_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 95 | 0 | 5 | 6 | 0 | 22.6300 | 20.3395 | 25.0805 | 0.1189 | 0.1102 | 0.1283 |
| FD001 | 3 | ISO_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 100 | 0 | 0 | 0 | 0 | 6.9600 | 6.1898 | 7.7502 | 0.0400 | 0.0361 | 0.0440 |
| FD001 | 3 | ISO_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 10 | 90 | 0 | 0 | 0 | 0 | 5.2900 | 4.5997 | 6.0100 | 0.0305 | 0.0269 | 0.0344 |
| FD001 | 3 | ISO_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 20 | 80 | 0 | 0 | 0 | 0 | 3.3800 | 2.8400 | 3.9100 | 0.0198 | 0.0168 | 0.0228 |
| FD001 | 3 | ISO_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 49 | 51 | 0 | 0 | 0 | 0 | 1.8800 | 1.4400 | 2.3400 | 0.0111 | 0.0085 | 0.0137 |
| FD001 | 3 | ISO_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 31 | 69 | 0 | 0 | 0 | 0 | 3.7100 | 3.0400 | 4.4002 | 0.0217 | 0.0179 | 0.0256 |
| FD001 | 3 | ISO_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 31 | 69 | 0 | 0 | 0 | 0 | 3.0400 | 2.4498 | 3.6900 | 0.0178 | 0.0144 | 0.0213 |
| FD001 | 3 | ISO_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 55 | 45 | 0 | 0 | 0 | 0 | 1.5700 | 1.1497 | 2.0300 | 0.0093 | 0.0069 | 0.0119 |
| FD001 | 3 | ISO_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 65 | 35 | 0 | 0 | 0 | 0 | 1.1500 | 0.7798 | 1.5400 | 0.0068 | 0.0046 | 0.0091 |
| FD001 | 3 | ISO_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 83 | 0 | 17 | 18 | 0 | 28.5300 | 27.0200 | 30.2200 | 0.1459 | 0.1419 | 0.1500 |
| FD001 | 3 | ISO_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 88 | 0 | 12 | 17 | 0 | 26.8200 | 25.2797 | 28.3900 | 0.1376 | 0.1333 | 0.1421 |
| FD001 | 3 | ISO_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 93 | 0 | 7 | 12 | 0 | 24.8800 | 23.4400 | 26.3502 | 0.1296 | 0.1258 | 0.1336 |
| FD001 | 3 | ISO_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 96 | 0 | 4 | 10 | 0 | 23.5200 | 22.1100 | 24.9300 | 0.1228 | 0.1188 | 0.1267 |
| FD001 | 3 | RF_SLOPE_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 62 | 38 | 0 | 0 | 0 | 0 | 3.3400 | 2.0798 | 4.8002 | 0.0196 | 0.0125 | 0.0273 |
| FD001 | 3 | RF_SLOPE_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 63 | 37 | 0 | 0 | 0 | 0 | 3.0600 | 1.8900 | 4.4102 | 0.0179 | 0.0112 | 0.0252 |
| FD001 | 3 | RF_SLOPE_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 69 | 31 | 0 | 0 | 0 | 0 | 2.5400 | 1.4600 | 3.8400 | 0.0150 | 0.0087 | 0.0223 |
| FD001 | 3 | RF_SLOPE_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 71 | 29 | 0 | 0 | 0 | 0 | 2.1200 | 1.1400 | 3.3802 | 0.0125 | 0.0068 | 0.0193 |
| FD001 | 3 | RF_SLOPE_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 75 | 25 | 0 | 0 | 0 | 0 | 1.7700 | 0.9000 | 2.8602 | 0.0105 | 0.0055 | 0.0164 |
| FD001 | 3 | RF_SLOPE_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 78 | 22 | 0 | 0 | 0 | 0 | 1.6700 | 0.8598 | 2.7302 | 0.0098 | 0.0052 | 0.0156 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 84 | 16 | 0 | 0 | 0 | 0 | 1.0900 | 0.5500 | 1.7300 | 0.0065 | 0.0034 | 0.0101 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 86 | 14 | 0 | 0 | 0 | 0 | 1.0500 | 0.5400 | 1.6800 | 0.0062 | 0.0032 | 0.0098 |
| FD001 | 3 | RF_SLOPE_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 86 | 0 | 14 | 17 | 0 | 27.2400 | 24.9995 | 29.5300 | 0.1402 | 0.1331 | 0.1470 |
| FD001 | 3 | RF_SLOPE_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 90 | 0 | 10 | 16 | 0 | 25.8600 | 23.5098 | 28.0900 | 0.1333 | 0.1256 | 0.1404 |
| FD001 | 3 | RF_SLOPE_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 94 | 0 | 6 | 9 | 0 | 23.8500 | 21.6000 | 26.1600 | 0.1249 | 0.1169 | 0.1329 |
| FD001 | 3 | RF_SLOPE_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 1 | 94 | 0 | 5 | 12 | 0 | 22.6700 | 20.3495 | 25.1705 | 0.1188 | 0.1100 | 0.1273 |
| FD003 | 1 | ISO_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 34 | 66 | 0 | 0 | 0 | 0 | 3.9000 | 3.1200 | 4.7000 | 0.0183 | 0.0148 | 0.0221 |
| FD003 | 1 | ISO_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 40 | 60 | 0 | 0 | 0 | 0 | 3.6500 | 2.8600 | 4.4600 | 0.0171 | 0.0134 | 0.0208 |
| FD003 | 1 | ISO_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 50 | 50 | 0 | 0 | 0 | 0 | 2.3800 | 1.7400 | 3.0600 | 0.0113 | 0.0083 | 0.0145 |
| FD003 | 1 | ISO_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 55 | 45 | 0 | 0 | 0 | 0 | 1.3800 | 0.9700 | 1.8800 | 0.0065 | 0.0046 | 0.0088 |
| FD003 | 1 | ISO_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 70 | 30 | 0 | 0 | 0 | 0 | 1.3200 | 0.8700 | 1.8300 | 0.0063 | 0.0042 | 0.0086 |
| FD003 | 1 | ISO_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 70 | 30 | 0 | 0 | 0 | 0 | 1.1900 | 0.8000 | 1.6300 | 0.0056 | 0.0038 | 0.0076 |
| FD003 | 1 | ISO_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 72 | 28 | 0 | 0 | 0 | 0 | 0.8300 | 0.5100 | 1.2000 | 0.0040 | 0.0025 | 0.0057 |
| FD003 | 1 | ISO_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 90 | 10 | 0 | 0 | 0 | 0 | 0.3500 | 0.1400 | 0.5800 | 0.0017 | 0.0007 | 0.0028 |
| FD003 | 1 | ISO_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 85 | 0 | 15 | 16 | 0 | 27.6800 | 25.7697 | 29.6502 | 0.1170 | 0.1102 | 0.1240 |
| FD003 | 1 | ISO_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 85 | 0 | 15 | 17 | 0 | 26.8900 | 25.0500 | 28.9805 | 0.1136 | 0.1068 | 0.1213 |
| FD003 | 1 | ISO_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 88 | 0 | 12 | 13 | 0 | 24.3700 | 22.5300 | 26.2100 | 0.1045 | 0.0976 | 0.1119 |
| FD003 | 1 | ISO_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 90 | 0 | 10 | 13 | 0 | 23.0200 | 21.3498 | 24.6803 | 0.0988 | 0.0924 | 0.1058 |
| FD003 | 1 | RF_SLOPE_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 66 | 34 | 0 | 0 | 0 | 0 | 1.5300 | 0.8397 | 2.3600 | 0.0073 | 0.0040 | 0.0111 |
| FD003 | 1 | RF_SLOPE_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 69 | 31 | 0 | 0 | 0 | 0 | 1.2700 | 0.6900 | 2.0500 | 0.0060 | 0.0033 | 0.0095 |
| FD003 | 1 | RF_SLOPE_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 76 | 24 | 0 | 0 | 0 | 0 | 0.8500 | 0.4000 | 1.4102 | 0.0041 | 0.0019 | 0.0067 |
| FD003 | 1 | RF_SLOPE_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 77 | 23 | 0 | 0 | 0 | 0 | 0.7800 | 0.3400 | 1.3700 | 0.0037 | 0.0017 | 0.0063 |
| FD003 | 1 | RF_SLOPE_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 80 | 20 | 0 | 0 | 0 | 0 | 0.8700 | 0.3500 | 1.5700 | 0.0041 | 0.0017 | 0.0074 |
| FD003 | 1 | RF_SLOPE_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 82 | 18 | 0 | 0 | 0 | 0 | 0.7600 | 0.2700 | 1.4400 | 0.0036 | 0.0013 | 0.0066 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 86 | 14 | 0 | 0 | 0 | 0 | 0.5400 | 0.1400 | 1.0900 | 0.0026 | 0.0007 | 0.0051 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 87 | 13 | 0 | 0 | 0 | 0 | 0.4100 | 0.1400 | 0.7800 | 0.0019 | 0.0007 | 0.0036 |
| FD003 | 1 | RF_SLOPE_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 89 | 0 | 11 | 14 | 0 | 25.9300 | 23.6300 | 28.2500 | 0.1104 | 0.1028 | 0.1180 |
| FD003 | 1 | RF_SLOPE_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 92 | 0 | 8 | 11 | 0 | 24.1700 | 21.7398 | 26.4103 | 0.1033 | 0.0953 | 0.1113 |
| FD003 | 1 | RF_SLOPE_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 95 | 0 | 5 | 6 | 0 | 20.5400 | 18.4498 | 22.7800 | 0.0895 | 0.0819 | 0.0975 |
| FD003 | 1 | RF_SLOPE_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 95 | 0 | 5 | 7 | 0 | 19.4400 | 17.3888 | 21.4300 | 0.0848 | 0.0772 | 0.0928 |
| FD003 | 2 | ISO_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 19 | 81 | 0 | 0 | 0 | 0 | 3.5600 | 2.8600 | 4.3300 | 0.0171 | 0.0138 | 0.0206 |
| FD003 | 2 | ISO_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 26 | 74 | 0 | 0 | 0 | 0 | 3.1200 | 2.3900 | 3.8800 | 0.0149 | 0.0115 | 0.0185 |
| FD003 | 2 | ISO_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 46 | 54 | 0 | 0 | 0 | 0 | 1.6700 | 1.2497 | 2.1500 | 0.0081 | 0.0061 | 0.0103 |
| FD003 | 2 | ISO_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 56 | 44 | 0 | 0 | 0 | 0 | 1.1100 | 0.8000 | 1.4600 | 0.0054 | 0.0039 | 0.0071 |
| FD003 | 2 | ISO_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 37 | 63 | 0 | 0 | 0 | 0 | 2.2800 | 1.7000 | 2.9100 | 0.0110 | 0.0082 | 0.0141 |
| FD003 | 2 | ISO_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 64 | 36 | 0 | 0 | 0 | 0 | 1.2900 | 0.8400 | 1.7900 | 0.0062 | 0.0041 | 0.0087 |
| FD003 | 2 | ISO_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 74 | 26 | 0 | 0 | 0 | 0 | 0.7200 | 0.4200 | 1.0400 | 0.0035 | 0.0021 | 0.0051 |
| FD003 | 2 | ISO_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 80 | 20 | 0 | 0 | 0 | 0 | 0.6000 | 0.3297 | 0.9400 | 0.0029 | 0.0016 | 0.0046 |
| FD003 | 2 | ISO_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 77 | 0 | 23 | 26 | 0 | 32.0600 | 27.3500 | 38.4802 | 0.1353 | 0.1180 | 0.1590 |
| FD003 | 2 | ISO_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 83 | 0 | 17 | 22 | 0 | 30.0300 | 25.2495 | 36.0705 | 0.1272 | 0.1096 | 0.1496 |
| FD003 | 2 | ISO_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 85 | 0 | 15 | 17 | 0 | 27.3800 | 22.9898 | 33.2810 | 0.1178 | 0.1003 | 0.1403 |
| FD003 | 2 | ISO_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 93 | 0 | 7 | 13 | 0 | 25.4100 | 21.8400 | 30.0500 | 0.1098 | 0.0957 | 0.1284 |
| FD003 | 2 | RF_SLOPE_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 86 | 14 | 0 | 0 | 0 | 0 | 0.8800 | 0.3200 | 1.6300 | 0.0043 | 0.0016 | 0.0078 |
| FD003 | 2 | RF_SLOPE_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 86 | 14 | 0 | 0 | 0 | 0 | 0.8000 | 0.2800 | 1.4500 | 0.0039 | 0.0014 | 0.0068 |
| FD003 | 2 | RF_SLOPE_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 87 | 13 | 0 | 0 | 0 | 0 | 0.6700 | 0.2500 | 1.1900 | 0.0033 | 0.0013 | 0.0057 |
| FD003 | 2 | RF_SLOPE_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 88 | 12 | 0 | 0 | 0 | 0 | 0.5900 | 0.1900 | 1.1200 | 0.0029 | 0.0009 | 0.0054 |
| FD003 | 2 | RF_SLOPE_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 87 | 13 | 0 | 0 | 0 | 0 | 0.7500 | 0.2300 | 1.4500 | 0.0036 | 0.0012 | 0.0068 |
| FD003 | 2 | RF_SLOPE_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 89 | 11 | 0 | 0 | 0 | 0 | 0.5800 | 0.1998 | 1.1300 | 0.0028 | 0.0009 | 0.0053 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 91 | 9 | 0 | 0 | 0 | 0 | 0.4900 | 0.1300 | 0.9902 | 0.0024 | 0.0006 | 0.0047 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 93 | 7 | 0 | 0 | 0 | 0 | 0.4700 | 0.1100 | 0.9700 | 0.0023 | 0.0005 | 0.0046 |
| FD003 | 2 | RF_SLOPE_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 88 | 0 | 12 | 16 | 0 | 26.9100 | 23.2900 | 31.0210 | 0.1160 | 0.1031 | 0.1315 |
| FD003 | 2 | RF_SLOPE_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 91 | 0 | 9 | 15 | 0 | 25.7400 | 22.1397 | 30.4920 | 0.1111 | 0.0983 | 0.1283 |
| FD003 | 2 | RF_SLOPE_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 94 | 0 | 6 | 9 | 0 | 23.5200 | 19.7500 | 27.9608 | 0.1029 | 0.0889 | 0.1196 |
| FD003 | 2 | RF_SLOPE_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 95 | 0 | 5 | 8 | 0 | 22.0500 | 18.5697 | 26.5700 | 0.0967 | 0.0833 | 0.1138 |
| FD003 | 3 | ISO_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 27 | 73 | 0 | 0 | 0 | 0 | 3.2400 | 2.5900 | 3.9500 | 0.0153 | 0.0122 | 0.0187 |
| FD003 | 3 | ISO_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 39 | 61 | 0 | 0 | 0 | 0 | 2.3900 | 1.8800 | 2.9000 | 0.0112 | 0.0088 | 0.0138 |
| FD003 | 3 | ISO_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 71 | 29 | 0 | 0 | 0 | 0 | 1.0000 | 0.6600 | 1.3402 | 0.0048 | 0.0032 | 0.0065 |
| FD003 | 3 | ISO_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 80 | 20 | 0 | 0 | 0 | 0 | 0.7200 | 0.4400 | 1.0300 | 0.0034 | 0.0021 | 0.0048 |
| FD003 | 3 | ISO_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 40 | 60 | 0 | 0 | 0 | 0 | 1.8200 | 1.4500 | 2.2200 | 0.0086 | 0.0069 | 0.0105 |
| FD003 | 3 | ISO_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 64 | 36 | 0 | 0 | 0 | 0 | 0.9900 | 0.6600 | 1.3500 | 0.0047 | 0.0031 | 0.0064 |
| FD003 | 3 | ISO_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 100 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| FD003 | 3 | ISO_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 100 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |
| FD003 | 3 | ISO_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 84 | 0 | 16 | 17 | 0 | 27.0200 | 24.8697 | 29.4200 | 0.1144 | 0.1072 | 0.1215 |
| FD003 | 3 | ISO_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 89 | 0 | 11 | 14 | 0 | 25.1700 | 23.2598 | 27.2100 | 0.1070 | 0.1008 | 0.1133 |
| FD003 | 3 | ISO_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 90 | 0 | 10 | 12 | 0 | 24.3100 | 22.3397 | 26.3600 | 0.1041 | 0.0979 | 0.1105 |
| FD003 | 3 | ISO_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 92 | 0 | 8 | 10 | 0 | 23.5900 | 21.7697 | 25.4608 | 0.1009 | 0.0951 | 0.1068 |
| FD003 | 3 | RF_SLOPE_LOWER95_M12_D1 | 1 | HI_MARKER_D1 | 100 | 81 | 19 | 0 | 0 | 0 | 0 | 0.6900 | 0.3400 | 1.1000 | 0.0033 | 0.0017 | 0.0052 |
| FD003 | 3 | RF_SLOPE_LOWER95_M12_D2 | 2 | HI_MARKER_D2 | 100 | 82 | 18 | 0 | 0 | 0 | 0 | 0.6000 | 0.2900 | 0.9500 | 0.0028 | 0.0014 | 0.0045 |
| FD003 | 3 | RF_SLOPE_LOWER95_M15_D1 | 1 | HI_MARKER_D1 | 100 | 88 | 12 | 0 | 0 | 0 | 0 | 0.4000 | 0.1500 | 0.7100 | 0.0019 | 0.0007 | 0.0034 |
| FD003 | 3 | RF_SLOPE_LOWER95_M15_D2 | 2 | HI_MARKER_D2 | 100 | 88 | 12 | 0 | 0 | 0 | 0 | 0.4000 | 0.1500 | 0.7100 | 0.0019 | 0.0007 | 0.0033 |
| FD003 | 3 | RF_SLOPE_LOWER98_M12_D1 | 1 | HI_MARKER_D1 | 100 | 86 | 14 | 0 | 0 | 0 | 0 | 0.4500 | 0.2000 | 0.7600 | 0.0021 | 0.0010 | 0.0036 |
| FD003 | 3 | RF_SLOPE_LOWER98_M12_D2 | 2 | HI_MARKER_D2 | 100 | 88 | 12 | 0 | 0 | 0 | 0 | 0.4000 | 0.1300 | 0.7100 | 0.0019 | 0.0006 | 0.0033 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D1 | 1 | HI_MARKER_D1 | 100 | 89 | 11 | 0 | 0 | 0 | 0 | 0.2400 | 0.0800 | 0.4500 | 0.0011 | 0.0004 | 0.0021 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D2 | 2 | HI_MARKER_D2 | 100 | 89 | 11 | 0 | 0 | 0 | 0 | 0.2400 | 0.0800 | 0.4400 | 0.0011 | 0.0004 | 0.0021 |
| FD003 | 3 | RF_SLOPE_POINT_M12_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 89 | 0 | 11 | 12 | 0 | 25.3800 | 22.6900 | 28.2100 | 0.1082 | 0.1003 | 0.1167 |
| FD003 | 3 | RF_SLOPE_POINT_M12_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 93 | 0 | 7 | 9 | 0 | 24.0500 | 21.5000 | 26.8302 | 0.1027 | 0.0942 | 0.1113 |
| FD003 | 3 | RF_SLOPE_POINT_M15_D1 | 1 | HI_MARKER_D1 | 100 | 0 | 95 | 0 | 5 | 6 | 0 | 21.9000 | 19.4300 | 24.5600 | 0.0948 | 0.0866 | 0.1034 |
| FD003 | 3 | RF_SLOPE_POINT_M15_D2 | 2 | HI_MARKER_D2 | 100 | 0 | 95 | 0 | 5 | 6 | 0 | 21.0400 | 18.4997 | 23.7903 | 0.0910 | 0.0826 | 0.0998 |

## Teste truncado

Sem marco utilizável até o truncamento, status censurado. Não criar decisões ou vidas futuras a partir de RUL verdadeiro. Aferição de uma retirada comprometida não significa que sua execução foi observada. Nenhum truncado entra em custo de renovação.

| subset | repeat | policy_id | total | decisions | without_decision | late_count | exact_count | observed_executions |
|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | HI_MARKER_D1 | 100 | 29 | 71 | 0 | 0 | 28 |
| FD001 | 1 | HI_MARKER_D2 | 100 | 29 | 71 | 0 | 0 | 28 |
| FD001 | 2 | HI_MARKER_D1 | 100 | 30 | 70 | 0 | 0 | 29 |
| FD001 | 2 | HI_MARKER_D2 | 100 | 30 | 70 | 0 | 0 | 29 |
| FD001 | 3 | HI_MARKER_D1 | 100 | 29 | 71 | 0 | 0 | 29 |
| FD001 | 3 | HI_MARKER_D2 | 100 | 29 | 71 | 0 | 0 | 28 |
| FD003 | 1 | HI_MARKER_D1 | 100 | 27 | 73 | 0 | 0 | 27 |
| FD003 | 1 | HI_MARKER_D2 | 100 | 27 | 73 | 0 | 0 | 26 |
| FD003 | 2 | HI_MARKER_D1 | 100 | 26 | 74 | 0 | 0 | 26 |
| FD003 | 2 | HI_MARKER_D2 | 100 | 26 | 74 | 0 | 0 | 26 |
| FD003 | 3 | HI_MARKER_D1 | 100 | 23 | 77 | 0 | 0 | 23 |
| FD003 | 3 | HI_MARKER_D2 | 100 | 23 | 77 | 0 | 0 | 22 |

## Limites e decisão científica

Distinguir ganho de condição supervisionada e ganho incremental do conversor/calibração. Ausência de eventos não certifica risco populacional ≤2%, e as divisões são dependentes. Não escolher a melhor semente, alterar o HI ou o marco após estes resultados. O controle simples deve permanecer como referência decisória competitiva. Qualquer otimização de limiar, espera após marco ou regra futura exige seleção interna e protocolo próprio; não acrescentar complexidade apenas para obter uma melhoria.

Sem ajuste, inspeção, projeção de 20 anos ou edição do artigo. Custos são normalizados por exposição simulada; a ponte de escala e os parâmetros empresariais continuam abertos.

[Verificação](verification.json), [controles](controls.csv), [contrastes](contrasts.csv), [decomposição](decomposition.csv), [metadados](metadata.json) e [manifesto](manifest.json).
