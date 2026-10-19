# P11 — comparação de regras de remoção sem inspeção

[Protocolo anterior à execução](../../protocolo_remocao_11.md). Previsões P10 congeladas, sem novo ajuste do índice de saúde (HI), modelos ou quantis. FD001 principal; FD003 robustez; três repetições com os mesmos 100 motores por domínio. ISO é isotônico; RF_SLOPE é floresta aleatória com HI e inclinação causal. As 26 regras são 16 primárias, oito sensibilidades 95% e dois controles de idade fixa. São comparações exploratórias, não 300 motores independentes.

## Triagem das regras primárias

Decisão no primeiro ciclo permitido em que a antecedência prevista é ≤reserva+execução; retirada comprometida decisão+d. LOWER98 usa limite inferior calibrado pelo máximo temporal em U; POINT usa previsão central. Reserva 12 é apenas sensibilidade de política, sem adoção. A idade de controle é o menor endpoint dos 40 motores F∪C menos um, definida antes de E. A ausência de decisão preventiva antes do endpoint permanece no denominador e impede completude; não é convertida em programação tardia fictícia.

strict_pass_repeats exige decisão em todos os motores e ultrapassagem estrita ≤2% na repetição. prudent_pass_repeats também exige nenhuma retirada programada exactamente no endpoint, como triagem conservadora, sem alterar o alvo do autor. Nenhum filtro valida risco populacional ou admissibilidade operacional. A tabela mostra amplitudes entre divisões, não intervalos de confiança.

Com execução de um ciclo e decisões apenas antes de T, r=τ+1≤T por construção: a ultrapassagem estrita isolada não detecta todas as falhas. É indispensável conservar chegadas exactas e ausências de decisão. Com dois ciclos, a programação mais tardia ainda observável pode ser T+1; a curta magnitude não valida operação depois do endpoint.

| subset | policy_id | strict_pass_repeats | prudent_pass_repeats | late_min | late_max | exact_max | missing_max | mean_life_min | mean_life_max | unused_min | unused_max |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | AGE_D1 | 0 | 0 | 0 | 0 | 0 | 3 | 130.1200 | 134.7200 | 71.5900 | 76.1900 |
| FD001 | AGE_D2 | 0 | 0 | 0 | 1 | 0 | 2 | 130.1200 | 134.7200 | 71.5900 | 76.1900 |
| FD001 | ISO_LOWER98_M12_D1 | 3 | 3 | 0 | 0 | 0 | 0 | 170.0600 | 170.7900 | 35.5200 | 36.2500 |
| FD001 | ISO_LOWER98_M12_D2 | 3 | 3 | 0 | 0 | 0 | 0 | 169.7300 | 171.1200 | 35.1900 | 36.5800 |
| FD001 | ISO_LOWER98_M15_D1 | 3 | 3 | 0 | 0 | 0 | 0 | 167.4100 | 168.6500 | 37.6600 | 38.9000 |
| FD001 | ISO_LOWER98_M15_D2 | 3 | 3 | 0 | 0 | 0 | 0 | 168.2400 | 169.2300 | 37.0800 | 38.0700 |
| FD001 | ISO_POINT_M12_D1 | 0 | 0 | 0 | 0 | 5 | 20 | 195.6100 | 195.9700 | 10.3400 | 10.7000 |
| FD001 | ISO_POINT_M12_D2 | 0 | 0 | 3 | 6 | 5 | 14 | 194.9000 | 195.3200 | 10.9900 | 11.4100 |
| FD001 | ISO_POINT_M15_D1 | 0 | 0 | 0 | 0 | 5 | 11 | 191.1300 | 193.1600 | 13.1500 | 15.1800 |
| FD001 | ISO_POINT_M15_D2 | 0 | 0 | 1 | 4 | 4 | 8 | 191.3200 | 191.9700 | 14.3400 | 14.9900 |
| FD001 | RF_SLOPE_LOWER98_M12_D1 | 3 | 3 | 0 | 0 | 0 | 0 | 167.7300 | 169.3400 | 36.9700 | 38.5800 |
| FD001 | RF_SLOPE_LOWER98_M12_D2 | 3 | 3 | 0 | 0 | 0 | 0 | 168.6400 | 170.1400 | 36.1700 | 37.6700 |
| FD001 | RF_SLOPE_LOWER98_M15_D1 | 3 | 3 | 0 | 0 | 0 | 0 | 167.0800 | 168.7600 | 37.5500 | 39.2300 |
| FD001 | RF_SLOPE_LOWER98_M15_D2 | 3 | 3 | 0 | 0 | 0 | 0 | 167.9700 | 169.7400 | 36.5700 | 38.3400 |
| FD001 | RF_SLOPE_POINT_M12_D1 | 0 | 0 | 0 | 0 | 3 | 14 | 193.0800 | 194.3200 | 11.9900 | 13.2300 |
| FD001 | RF_SLOPE_POINT_M12_D2 | 0 | 0 | 1 | 4 | 3 | 10 | 193.0500 | 193.9400 | 12.3700 | 13.2600 |
| FD001 | RF_SLOPE_POINT_M15_D1 | 0 | 0 | 0 | 0 | 3 | 7 | 190.8100 | 190.9300 | 15.3800 | 15.5000 |
| FD001 | RF_SLOPE_POINT_M15_D2 | 0 | 0 | 0 | 3 | 4 | 5 | 190.3200 | 190.7500 | 15.5600 | 15.9900 |
| FD003 | AGE_D1 | 0 | 0 | 0 | 0 | 0 | 2 | 145.2400 | 148.6100 | 98.5900 | 101.9600 |
| FD003 | AGE_D2 | 0 | 0 | 0 | 1 | 0 | 1 | 145.2400 | 148.6100 | 98.5900 | 101.9600 |
| FD003 | ISO_LOWER98_M12_D1 | 3 | 3 | 0 | 0 | 0 | 0 | 207.2600 | 210.9800 | 36.2200 | 39.9400 |
| FD003 | ISO_LOWER98_M12_D2 | 3 | 3 | 0 | 0 | 0 | 0 | 207.2700 | 211.1500 | 36.0500 | 39.9300 |
| FD003 | ISO_LOWER98_M15_D1 | 3 | 3 | 0 | 0 | 0 | 0 | 205.7000 | 209.6900 | 37.5100 | 41.5000 |
| FD003 | ISO_LOWER98_M15_D2 | 3 | 3 | 0 | 0 | 0 | 0 | 206.5800 | 210.2100 | 36.9900 | 40.6200 |
| FD003 | ISO_POINT_M12_D1 | 0 | 0 | 0 | 0 | 3 | 23 | 236.1800 | 237.0400 | 10.1600 | 11.0200 |
| FD003 | ISO_POINT_M12_D2 | 0 | 0 | 1 | 2 | 4 | 17 | 235.3300 | 236.7500 | 10.4500 | 11.8700 |
| FD003 | ISO_POINT_M15_D1 | 0 | 0 | 0 | 0 | 2 | 15 | 232.3600 | 233.4700 | 13.7300 | 14.8400 |
| FD003 | ISO_POINT_M15_D2 | 0 | 0 | 0 | 2 | 4 | 10 | 231.3900 | 233.7500 | 13.4500 | 15.8100 |
| FD003 | RF_SLOPE_LOWER98_M12_D1 | 3 | 3 | 0 | 0 | 0 | 0 | 205.7300 | 209.7300 | 37.4700 | 41.4700 |
| FD003 | RF_SLOPE_LOWER98_M12_D2 | 3 | 3 | 0 | 0 | 0 | 0 | 206.5600 | 210.6200 | 36.5800 | 40.6400 |
| FD003 | RF_SLOPE_LOWER98_M15_D1 | 3 | 3 | 0 | 0 | 0 | 0 | 205.4700 | 209.4000 | 37.8000 | 41.7300 |
| FD003 | RF_SLOPE_LOWER98_M15_D2 | 3 | 3 | 0 | 0 | 0 | 0 | 206.4500 | 210.4000 | 36.8000 | 40.7500 |
| FD003 | RF_SLOPE_POINT_M12_D1 | 0 | 0 | 0 | 0 | 4 | 12 | 231.8900 | 234.7900 | 12.4100 | 15.3100 |
| FD003 | RF_SLOPE_POINT_M12_D2 | 0 | 0 | 2 | 4 | 2 | 9 | 231.7200 | 234.2100 | 12.9900 | 15.4800 |
| FD003 | RF_SLOPE_POINT_M15_D1 | 0 | 0 | 0 | 0 | 3 | 6 | 228.5000 | 231.0600 | 16.1400 | 18.7000 |
| FD003 | RF_SLOPE_POINT_M15_D2 | 0 | 0 | 0 | 3 | 2 | 5 | 228.0300 | 231.2000 | 16.0000 | 19.1700 |

![Vida aproveitada e chegadas ao endpoint](removal_tradeoff.png)

A figura inclui chegadas exactas, programações tardias e ausência de decisão; essa frequência composta é distinta do alvo de 2% de ultrapassagem estrita.

## Reserva de referência 15 — comparação por repetição

| subset | repeat | policy_id | decisions | without_decision | late_count | exact_count | mean_utilised | mean_unused | initial_insufficient_count | median_real_reserve | restorations_per_10000_cycles | passes_strict_screen | passes_prudent_screen |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | AGE_D1 | 97 | 3 | 0 | 0 | 134.7200 | 71.5900 | 0 | 64.0000 | 74.2280 | False | False |
| FD001 | 1 | AGE_D2 | 98 | 2 | 1 | 0 | 134.7200 | 71.5900 | 0 | 64.0000 | 74.2280 | False | False |
| FD001 | 1 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 168.5000 | 37.8100 | 75 | 35.0000 | 59.3472 | True | True |
| FD001 | 1 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 169.2300 | 37.0800 | 86 | 34.5000 | 59.0912 | True | True |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 168.7600 | 37.5500 | 88 | 34.0000 | 59.2557 | True | True |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 169.7400 | 36.5700 | 88 | 33.0000 | 58.9136 | True | True |
| FD001 | 2 | AGE_D1 | 99 | 1 | 0 | 0 | 131.0200 | 75.2900 | 0 | 68.0000 | 76.3242 | False | False |
| FD001 | 2 | AGE_D2 | 99 | 1 | 0 | 0 | 131.0200 | 75.2900 | 0 | 68.0000 | 76.3242 | False | False |
| FD001 | 2 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 167.4100 | 38.9000 | 63 | 34.5000 | 59.7336 | True | True |
| FD001 | 2 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 168.2400 | 38.0700 | 70 | 33.5000 | 59.4389 | True | True |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 167.0800 | 39.2300 | 87 | 35.0000 | 59.8516 | True | True |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 167.9700 | 38.3400 | 89 | 34.0000 | 59.5344 | True | True |
| FD001 | 3 | AGE_D1 | 99 | 1 | 0 | 0 | 130.1200 | 76.1900 | 0 | 68.0000 | 76.8521 | False | False |
| FD001 | 3 | AGE_D2 | 99 | 1 | 0 | 0 | 130.1200 | 76.1900 | 0 | 68.0000 | 76.8521 | False | False |
| FD001 | 3 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 168.6500 | 37.6600 | 55 | 35.0000 | 59.2944 | True | True |
| FD001 | 3 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 169.2300 | 37.0800 | 65 | 34.0000 | 59.0912 | True | True |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 168.1700 | 38.1400 | 84 | 35.0000 | 59.4636 | True | True |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 169.1300 | 37.1800 | 86 | 34.0000 | 59.1261 | True | True |
| FD003 | 1 | AGE_D1 | 98 | 2 | 0 | 0 | 146.1600 | 101.0400 | 0 | 75.5000 | 68.4182 | False | False |
| FD003 | 1 | AGE_D2 | 99 | 1 | 1 | 0 | 146.1600 | 101.0400 | 0 | 74.0000 | 68.4182 | False | False |
| FD003 | 1 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 209.6900 | 37.5100 | 72 | 34.5000 | 47.6894 | True | True |
| FD003 | 1 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 210.2100 | 36.9900 | 90 | 34.0000 | 47.5715 | True | True |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 209.4000 | 37.8000 | 86 | 35.0000 | 47.7555 | True | True |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 210.2700 | 36.9300 | 87 | 34.0000 | 47.5579 | True | True |
| FD003 | 2 | AGE_D1 | 99 | 1 | 0 | 0 | 145.2400 | 101.9600 | 0 | 76.0000 | 68.8516 | False | False |
| FD003 | 2 | AGE_D2 | 99 | 1 | 0 | 0 | 145.2400 | 101.9600 | 0 | 76.0000 | 68.8516 | False | False |
| FD003 | 2 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 205.7000 | 41.5000 | 74 | 34.0000 | 48.6145 | True | True |
| FD003 | 2 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 206.5800 | 40.6200 | 74 | 33.0000 | 48.4074 | True | True |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 205.4700 | 41.7300 | 91 | 36.0000 | 48.6689 | True | True |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 206.4500 | 40.7500 | 93 | 35.0000 | 48.4379 | True | True |
| FD003 | 3 | AGE_D1 | 98 | 2 | 0 | 0 | 148.6100 | 98.5900 | 0 | 75.0000 | 67.2902 | False | False |
| FD003 | 3 | AGE_D2 | 99 | 1 | 1 | 0 | 148.6100 | 98.5900 | 0 | 74.0000 | 67.2902 | False | False |
| FD003 | 3 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 209.1600 | 38.0400 | 86 | 34.0000 | 47.8103 | True | True |
| FD003 | 3 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 210.1600 | 37.0400 | 100 | 33.0000 | 47.5828 | True | True |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 209.4000 | 37.8000 | 89 | 33.5000 | 47.7555 | True | True |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 210.4000 | 36.8000 | 89 | 32.5000 | 47.5285 | True | True |

## Diferenças pareadas frente ao controle de idade fixa

Vida média em ciclos simulados; custo normalizado n/ΣN. Economia relativa 1−c_PHM/c_idade. Intervalos descritivos de 95% de 2000 reamostragens pareadas por motor, separadamente por repetição, condicionais aos modelos congelados. Não corrigem a escolha entre várias regras e não são projeções de resultado financeiro de companhia. O controle também apresentou eventos não prevenidos; não tratar a comparação como tendo admissibilidade equivalente.

| subset | repeat | policy_id | delay | common | delta_mean_life | life_ci_low | life_ci_high | relative_saving | saving_ci_low | saving_ci_high |
|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | ISO_LOWER98_M15_D1 | 1 | 100 | 33.7800 | 27.6500 | 40.7602 | 0.2005 | 0.1700 | 0.2323 |
| FD001 | 1 | ISO_LOWER98_M15_D2 | 2 | 100 | 34.5100 | 27.9400 | 41.0610 | 0.2039 | 0.1716 | 0.2342 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D1 | 1 | 100 | 34.0400 | 27.4398 | 40.9513 | 0.2017 | 0.1686 | 0.2339 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D2 | 2 | 100 | 35.0200 | 28.4198 | 41.7903 | 0.2063 | 0.1741 | 0.2371 |
| FD001 | 2 | ISO_LOWER98_M15_D1 | 1 | 100 | 36.3900 | 29.9495 | 42.9203 | 0.2174 | 0.1860 | 0.2470 |
| FD001 | 2 | ISO_LOWER98_M15_D2 | 2 | 100 | 37.2200 | 30.6700 | 43.8302 | 0.2212 | 0.1897 | 0.2511 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D1 | 1 | 100 | 36.0600 | 29.9498 | 42.6710 | 0.2158 | 0.1861 | 0.2461 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D2 | 2 | 100 | 36.9500 | 30.2095 | 43.6007 | 0.2200 | 0.1872 | 0.2495 |
| FD001 | 3 | ISO_LOWER98_M15_D1 | 1 | 100 | 38.5300 | 32.1797 | 45.6208 | 0.2285 | 0.1983 | 0.2597 |
| FD001 | 3 | ISO_LOWER98_M15_D2 | 2 | 100 | 39.1100 | 32.5593 | 46.0405 | 0.2311 | 0.2003 | 0.2617 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D1 | 1 | 100 | 38.0500 | 31.0682 | 44.8900 | 0.2263 | 0.1928 | 0.2564 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D2 | 2 | 100 | 39.0100 | 32.2995 | 46.2320 | 0.2307 | 0.1987 | 0.2624 |
| FD003 | 1 | ISO_LOWER98_M15_D1 | 1 | 100 | 63.5300 | 48.8173 | 78.2510 | 0.3030 | 0.2499 | 0.3489 |
| FD003 | 1 | ISO_LOWER98_M15_D2 | 2 | 100 | 64.0500 | 50.5380 | 79.0403 | 0.3047 | 0.2572 | 0.3512 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D1 | 1 | 100 | 63.2400 | 48.8693 | 78.8537 | 0.3020 | 0.2508 | 0.3512 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D2 | 2 | 100 | 64.1100 | 49.4387 | 79.3822 | 0.3049 | 0.2526 | 0.3523 |
| FD003 | 2 | ISO_LOWER98_M15_D1 | 1 | 100 | 60.4600 | 46.4995 | 75.6107 | 0.2939 | 0.2423 | 0.3424 |
| FD003 | 2 | ISO_LOWER98_M15_D2 | 2 | 100 | 61.3400 | 47.5288 | 75.9317 | 0.2969 | 0.2467 | 0.3431 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D1 | 1 | 100 | 60.2300 | 46.4498 | 75.4027 | 0.2931 | 0.2425 | 0.3416 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D2 | 2 | 100 | 61.2100 | 48.1293 | 75.9217 | 0.2965 | 0.2491 | 0.3430 |
| FD003 | 3 | ISO_LOWER98_M15_D1 | 1 | 100 | 60.5500 | 47.0588 | 75.6130 | 0.2895 | 0.2401 | 0.3371 |
| FD003 | 3 | ISO_LOWER98_M15_D2 | 2 | 100 | 61.5500 | 47.3678 | 76.3717 | 0.2929 | 0.2404 | 0.3395 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D1 | 1 | 100 | 60.7900 | 46.7970 | 75.9610 | 0.2903 | 0.2397 | 0.3380 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D2 | 2 | 100 | 61.7900 | 47.8393 | 76.5515 | 0.2937 | 0.2437 | 0.3401 |

## Todas as regras e sensibilidade pré-fixada

| subset | repeat | policy_id | decisions | without_decision | late_count | exact_count | mean_utilised | mean_unused | initial_insufficient_count | median_real_reserve | restorations_per_10000_cycles | passes_strict_screen | passes_prudent_screen |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | AGE_D1 | 97 | 3 | 0 | 0 | 134.7200 | 71.5900 | 0 | 64.0000 | 74.2280 | False | False |
| FD001 | 1 | AGE_D2 | 98 | 2 | 1 | 0 | 134.7200 | 71.5900 | 0 | 64.0000 | 74.2280 | False | False |
| FD001 | 1 | ISO_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 172.1900 | 34.1200 | 1 | 30.5000 | 58.0754 | True | True |
| FD001 | 1 | ISO_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 172.6200 | 33.6900 | 27 | 30.0000 | 57.9307 | True | True |
| FD001 | 1 | ISO_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 169.7400 | 36.5700 | 48 | 33.0000 | 58.9136 | True | True |
| FD001 | 1 | ISO_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 170.3900 | 35.9200 | 57 | 33.0000 | 58.6889 | True | True |
| FD001 | 1 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 170.2900 | 36.0200 | 40 | 31.0000 | 58.7234 | True | True |
| FD001 | 1 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 169.7300 | 36.5800 | 59 | 33.0000 | 58.9171 | True | True |
| FD001 | 1 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 168.5000 | 37.8100 | 75 | 35.0000 | 59.3472 | True | True |
| FD001 | 1 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 169.2300 | 37.0800 | 86 | 34.5000 | 59.0912 | True | True |
| FD001 | 1 | ISO_POINT_M12_D1 | 80 | 20 | 0 | 3 | 195.9700 | 10.3400 | 0 | 11.0000 | 51.0282 | False | False |
| FD001 | 1 | ISO_POINT_M12_D2 | 87 | 13 | 5 | 5 | 195.3200 | 10.9900 | 0 | 11.0000 | 51.1980 | False | False |
| FD001 | 1 | ISO_POINT_M15_D1 | 95 | 5 | 0 | 2 | 191.1300 | 15.1800 | 0 | 14.0000 | 52.3204 | False | False |
| FD001 | 1 | ISO_POINT_M15_D2 | 95 | 5 | 1 | 4 | 191.3200 | 14.9900 | 0 | 14.0000 | 52.2685 | False | False |
| FD001 | 1 | RF_SLOPE_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 170.0700 | 36.2400 | 73 | 33.5000 | 58.7993 | True | True |
| FD001 | 1 | RF_SLOPE_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 170.8100 | 35.5000 | 76 | 33.0000 | 58.5446 | True | True |
| FD001 | 1 | RF_SLOPE_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 169.3500 | 36.9600 | 80 | 34.0000 | 59.0493 | True | True |
| FD001 | 1 | RF_SLOPE_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 170.3100 | 36.0000 | 80 | 33.0000 | 58.7165 | True | True |
| FD001 | 1 | RF_SLOPE_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 169.3400 | 36.9700 | 82 | 34.0000 | 59.0528 | True | True |
| FD001 | 1 | RF_SLOPE_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 170.1400 | 36.1700 | 83 | 33.0000 | 58.7751 | True | True |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 168.7600 | 37.5500 | 88 | 34.0000 | 59.2557 | True | True |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 169.7400 | 36.5700 | 88 | 33.0000 | 58.9136 | True | True |
| FD001 | 1 | RF_SLOPE_POINT_M12_D1 | 93 | 7 | 0 | 3 | 193.0800 | 13.2300 | 0 | 14.0000 | 51.7920 | False | False |
| FD001 | 1 | RF_SLOPE_POINT_M12_D2 | 94 | 6 | 3 | 1 | 193.0500 | 13.2600 | 0 | 13.0000 | 51.8001 | False | False |
| FD001 | 1 | RF_SLOPE_POINT_M15_D1 | 94 | 6 | 0 | 0 | 190.8100 | 15.5000 | 0 | 16.0000 | 52.4082 | False | False |
| FD001 | 1 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 0 | 1 | 190.5500 | 15.7600 | 0 | 16.0000 | 52.4797 | False | False |
| FD001 | 2 | AGE_D1 | 99 | 1 | 0 | 0 | 131.0200 | 75.2900 | 0 | 68.0000 | 76.3242 | False | False |
| FD001 | 2 | AGE_D2 | 99 | 1 | 0 | 0 | 131.0200 | 75.2900 | 0 | 68.0000 | 76.3242 | False | False |
| FD001 | 2 | ISO_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 172.6100 | 33.7000 | 8 | 31.0000 | 57.9341 | True | True |
| FD001 | 2 | ISO_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 173.3000 | 33.0100 | 8 | 30.0000 | 57.7034 | True | True |
| FD001 | 2 | ISO_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 169.2200 | 37.0900 | 22 | 33.0000 | 59.0947 | True | True |
| FD001 | 2 | ISO_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 169.2600 | 37.0500 | 31 | 33.0000 | 59.0807 | True | True |
| FD001 | 2 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 170.0600 | 36.2500 | 45 | 32.5000 | 58.8028 | True | True |
| FD001 | 2 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 170.3600 | 35.9500 | 49 | 32.0000 | 58.6992 | True | True |
| FD001 | 2 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 167.4100 | 38.9000 | 63 | 34.5000 | 59.7336 | True | True |
| FD001 | 2 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 168.2400 | 38.0700 | 70 | 33.5000 | 59.4389 | True | True |
| FD001 | 2 | ISO_POINT_M12_D1 | 82 | 18 | 0 | 5 | 195.7500 | 10.5600 | 0 | 10.5000 | 51.0856 | False | False |
| FD001 | 2 | ISO_POINT_M12_D2 | 86 | 14 | 6 | 3 | 195.3100 | 11.0000 | 0 | 10.5000 | 51.2007 | False | False |
| FD001 | 2 | ISO_POINT_M15_D1 | 89 | 11 | 0 | 4 | 193.1600 | 13.1500 | 0 | 12.0000 | 51.7706 | False | False |
| FD001 | 2 | ISO_POINT_M15_D2 | 92 | 8 | 1 | 1 | 191.9700 | 14.3400 | 0 | 13.0000 | 52.0915 | False | False |
| FD001 | 2 | RF_SLOPE_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 168.0500 | 38.2600 | 74 | 34.0000 | 59.5061 | True | True |
| FD001 | 2 | RF_SLOPE_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 168.9300 | 37.3800 | 76 | 33.0000 | 59.1961 | True | True |
| FD001 | 2 | RF_SLOPE_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 167.4700 | 38.8400 | 81 | 34.5000 | 59.7122 | True | True |
| FD001 | 2 | RF_SLOPE_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 168.3500 | 37.9600 | 84 | 34.0000 | 59.4001 | True | True |
| FD001 | 2 | RF_SLOPE_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 167.7300 | 38.5800 | 81 | 35.0000 | 59.6196 | True | True |
| FD001 | 2 | RF_SLOPE_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 168.6400 | 37.6700 | 83 | 34.0000 | 59.2979 | True | True |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 167.0800 | 39.2300 | 87 | 35.0000 | 59.8516 | True | True |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 167.9700 | 38.3400 | 89 | 34.0000 | 59.5344 | True | True |
| FD001 | 2 | RF_SLOPE_POINT_M12_D1 | 87 | 13 | 0 | 0 | 193.1900 | 13.1200 | 0 | 14.0000 | 51.7625 | False | False |
| FD001 | 2 | RF_SLOPE_POINT_M12_D2 | 91 | 9 | 1 | 3 | 193.4000 | 12.9100 | 0 | 13.0000 | 51.7063 | False | False |
| FD001 | 2 | RF_SLOPE_POINT_M15_D1 | 93 | 7 | 0 | 1 | 190.8700 | 15.4400 | 0 | 16.0000 | 52.3917 | False | False |
| FD001 | 2 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 1 | 0 | 190.3200 | 15.9900 | 0 | 16.0000 | 52.5431 | False | False |
| FD001 | 3 | AGE_D1 | 99 | 1 | 0 | 0 | 130.1200 | 76.1900 | 0 | 68.0000 | 76.8521 | False | False |
| FD001 | 3 | AGE_D2 | 99 | 1 | 0 | 0 | 130.1200 | 76.1900 | 0 | 68.0000 | 76.8521 | False | False |
| FD001 | 3 | ISO_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 174.0400 | 32.2700 | 0 | 28.5000 | 57.4581 | True | True |
| FD001 | 3 | ISO_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 173.3700 | 32.9400 | 0 | 30.5000 | 57.6801 | True | True |
| FD001 | 3 | ISO_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 170.4600 | 35.8500 | 10 | 32.5000 | 58.6648 | True | True |
| FD001 | 3 | ISO_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 169.9600 | 36.3500 | 49 | 34.0000 | 58.8374 | True | True |
| FD001 | 3 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 170.7900 | 35.5200 | 21 | 33.0000 | 58.5514 | True | True |
| FD001 | 3 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 171.1200 | 35.1900 | 31 | 32.0000 | 58.4385 | True | True |
| FD001 | 3 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 168.6500 | 37.6600 | 55 | 35.0000 | 59.2944 | True | True |
| FD001 | 3 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 169.2300 | 37.0800 | 65 | 34.0000 | 59.0912 | True | True |
| FD001 | 3 | ISO_POINT_M12_D1 | 83 | 17 | 0 | 1 | 195.6100 | 10.7000 | 0 | 11.0000 | 51.1221 | False | False |
| FD001 | 3 | ISO_POINT_M12_D2 | 88 | 12 | 3 | 2 | 194.9000 | 11.4100 | 0 | 11.0000 | 51.3084 | False | False |
| FD001 | 3 | ISO_POINT_M15_D1 | 93 | 7 | 0 | 5 | 191.9600 | 14.3500 | 0 | 13.0000 | 52.0942 | False | False |
| FD001 | 3 | ISO_POINT_M15_D2 | 96 | 4 | 4 | 2 | 191.6000 | 14.7100 | 0 | 13.5000 | 52.1921 | False | False |
| FD001 | 3 | RF_SLOPE_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 170.4200 | 35.8900 | 62 | 34.0000 | 58.6786 | True | True |
| FD001 | 3 | RF_SLOPE_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 171.1400 | 35.1700 | 63 | 33.5000 | 58.4317 | True | True |
| FD001 | 3 | RF_SLOPE_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 169.6200 | 36.6900 | 69 | 35.0000 | 58.9553 | True | True |
| FD001 | 3 | RF_SLOPE_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 170.2000 | 36.1100 | 71 | 34.0000 | 58.7544 | True | True |
| FD001 | 3 | RF_SLOPE_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 168.8500 | 37.4600 | 75 | 35.0000 | 59.2242 | True | True |
| FD001 | 3 | RF_SLOPE_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 169.7500 | 36.5600 | 78 | 34.0000 | 58.9102 | True | True |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 168.1700 | 38.1400 | 84 | 35.0000 | 59.4636 | True | True |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 169.1300 | 37.1800 | 86 | 34.0000 | 59.1261 | True | True |
| FD001 | 3 | RF_SLOPE_POINT_M12_D1 | 86 | 14 | 0 | 3 | 194.3200 | 11.9900 | 0 | 13.0000 | 51.4615 | False | False |
| FD001 | 3 | RF_SLOPE_POINT_M12_D2 | 90 | 10 | 4 | 2 | 193.9400 | 12.3700 | 0 | 13.0000 | 51.5623 | False | False |
| FD001 | 3 | RF_SLOPE_POINT_M15_D1 | 94 | 6 | 0 | 3 | 190.9300 | 15.3800 | 0 | 16.0000 | 52.3752 | False | False |
| FD001 | 3 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 3 | 4 | 190.7500 | 15.5600 | 1 | 16.0000 | 52.4246 | False | False |
| FD003 | 1 | AGE_D1 | 98 | 2 | 0 | 0 | 146.1600 | 101.0400 | 0 | 75.5000 | 68.4182 | False | False |
| FD003 | 1 | AGE_D2 | 99 | 1 | 1 | 0 | 146.1600 | 101.0400 | 0 | 74.0000 | 68.4182 | False | False |
| FD003 | 1 | ISO_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 212.7600 | 34.4400 | 34 | 32.0000 | 47.0013 | True | True |
| FD003 | 1 | ISO_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 213.5100 | 33.6900 | 40 | 31.0000 | 46.8362 | True | True |
| FD003 | 1 | ISO_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 211.2400 | 35.9600 | 50 | 34.0000 | 47.3395 | True | True |
| FD003 | 1 | ISO_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 211.2400 | 35.9600 | 50 | 33.5000 | 47.3395 | True | True |
| FD003 | 1 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 210.1800 | 37.0200 | 70 | 34.0000 | 47.5783 | True | True |
| FD003 | 1 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 211.0500 | 36.1500 | 70 | 33.0000 | 47.3821 | True | True |
| FD003 | 1 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 209.6900 | 37.5100 | 72 | 34.5000 | 47.6894 | True | True |
| FD003 | 1 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 210.2100 | 36.9900 | 90 | 34.0000 | 47.5715 | True | True |
| FD003 | 1 | ISO_POINT_M12_D1 | 85 | 15 | 0 | 1 | 236.5400 | 10.6600 | 0 | 11.0000 | 42.2761 | False | False |
| FD003 | 1 | ISO_POINT_M12_D2 | 85 | 15 | 1 | 1 | 236.7500 | 10.4500 | 0 | 10.0000 | 42.2386 | False | False |
| FD003 | 1 | ISO_POINT_M15_D1 | 88 | 12 | 0 | 1 | 233.2300 | 13.9700 | 0 | 14.0000 | 42.8761 | False | False |
| FD003 | 1 | ISO_POINT_M15_D2 | 90 | 10 | 2 | 1 | 232.8800 | 14.3200 | 0 | 14.0000 | 42.9406 | False | False |
| FD003 | 1 | RF_SLOPE_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 210.3900 | 36.8100 | 66 | 33.0000 | 47.5308 | True | True |
| FD003 | 1 | RF_SLOPE_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 211.1300 | 36.0700 | 69 | 34.0000 | 47.3642 | True | True |
| FD003 | 1 | RF_SLOPE_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 209.7100 | 37.4900 | 76 | 35.0000 | 47.6849 | True | True |
| FD003 | 1 | RF_SLOPE_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 210.6400 | 36.5600 | 77 | 34.0000 | 47.4744 | True | True |
| FD003 | 1 | RF_SLOPE_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 209.7300 | 37.4700 | 80 | 35.0000 | 47.6804 | True | True |
| FD003 | 1 | RF_SLOPE_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 210.6200 | 36.5800 | 82 | 34.0000 | 47.4789 | True | True |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 209.4000 | 37.8000 | 86 | 35.0000 | 47.7555 | True | True |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 210.2700 | 36.9300 | 87 | 34.0000 | 47.5579 | True | True |
| FD003 | 1 | RF_SLOPE_POINT_M12_D1 | 89 | 11 | 0 | 3 | 234.7900 | 12.4100 | 0 | 12.0000 | 42.5913 | False | False |
| FD003 | 1 | RF_SLOPE_POINT_M12_D2 | 92 | 8 | 2 | 1 | 234.0300 | 13.1700 | 0 | 14.0000 | 42.7296 | False | False |
| FD003 | 1 | RF_SLOPE_POINT_M15_D1 | 95 | 5 | 0 | 1 | 229.4000 | 17.8000 | 0 | 17.0000 | 43.5920 | False | False |
| FD003 | 1 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 0 | 2 | 229.3000 | 17.9000 | 0 | 16.0000 | 43.6110 | False | False |
| FD003 | 2 | AGE_D1 | 99 | 1 | 0 | 0 | 145.2400 | 101.9600 | 0 | 76.0000 | 68.8516 | False | False |
| FD003 | 2 | AGE_D2 | 99 | 1 | 0 | 0 | 145.2400 | 101.9600 | 0 | 76.0000 | 68.8516 | False | False |
| FD003 | 2 | ISO_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 208.5400 | 38.6600 | 17 | 31.0000 | 47.9524 | True | True |
| FD003 | 2 | ISO_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 209.1000 | 38.1000 | 26 | 30.0000 | 47.8240 | True | True |
| FD003 | 2 | ISO_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 206.6500 | 40.5500 | 46 | 33.0000 | 48.3910 | True | True |
| FD003 | 2 | ISO_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 207.0900 | 40.1100 | 46 | 32.5000 | 48.2882 | True | True |
| FD003 | 2 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 207.2600 | 39.9400 | 37 | 32.0000 | 48.2486 | True | True |
| FD003 | 2 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 207.2700 | 39.9300 | 48 | 32.0000 | 48.2462 | True | True |
| FD003 | 2 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 205.7000 | 41.5000 | 74 | 34.0000 | 48.6145 | True | True |
| FD003 | 2 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 206.5800 | 40.6200 | 74 | 33.0000 | 48.4074 | True | True |
| FD003 | 2 | ISO_POINT_M12_D1 | 77 | 23 | 0 | 3 | 237.0400 | 10.1600 | 0 | 10.0000 | 42.1870 | False | False |
| FD003 | 2 | ISO_POINT_M12_D2 | 83 | 17 | 1 | 4 | 236.0100 | 11.1900 | 0 | 11.0000 | 42.3711 | False | False |
| FD003 | 2 | ISO_POINT_M15_D1 | 85 | 15 | 0 | 2 | 232.3600 | 14.8400 | 0 | 14.0000 | 43.0367 | False | False |
| FD003 | 2 | ISO_POINT_M15_D2 | 93 | 7 | 2 | 4 | 231.3900 | 15.8100 | 0 | 13.0000 | 43.2171 | False | False |
| FD003 | 2 | RF_SLOPE_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 205.8600 | 41.3400 | 86 | 36.0000 | 48.5767 | True | True |
| FD003 | 2 | RF_SLOPE_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 206.7800 | 40.4200 | 86 | 35.0000 | 48.3606 | True | True |
| FD003 | 2 | RF_SLOPE_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 205.6500 | 41.5500 | 87 | 36.0000 | 48.6263 | True | True |
| FD003 | 2 | RF_SLOPE_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 206.5700 | 40.6300 | 88 | 35.0000 | 48.4097 | True | True |
| FD003 | 2 | RF_SLOPE_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 205.7300 | 41.4700 | 87 | 36.0000 | 48.6074 | True | True |
| FD003 | 2 | RF_SLOPE_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 206.5600 | 40.6400 | 89 | 35.0000 | 48.4121 | True | True |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 205.4700 | 41.7300 | 91 | 36.0000 | 48.6689 | True | True |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 206.4500 | 40.7500 | 93 | 35.0000 | 48.4379 | True | True |
| FD003 | 2 | RF_SLOPE_POINT_M12_D1 | 88 | 12 | 0 | 4 | 231.8900 | 15.3100 | 0 | 14.5000 | 43.1239 | False | False |
| FD003 | 2 | RF_SLOPE_POINT_M12_D2 | 91 | 9 | 4 | 2 | 231.7200 | 15.4800 | 0 | 14.0000 | 43.1555 | False | False |
| FD003 | 2 | RF_SLOPE_POINT_M15_D1 | 94 | 6 | 0 | 3 | 228.5000 | 18.7000 | 0 | 16.0000 | 43.7637 | False | False |
| FD003 | 2 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 3 | 0 | 228.0300 | 19.1700 | 0 | 16.0000 | 43.8539 | False | False |
| FD003 | 3 | AGE_D1 | 98 | 2 | 0 | 0 | 148.6100 | 98.5900 | 0 | 75.0000 | 67.2902 | False | False |
| FD003 | 3 | AGE_D2 | 99 | 1 | 1 | 0 | 148.6100 | 98.5900 | 0 | 74.0000 | 67.2902 | False | False |
| FD003 | 3 | ISO_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 212.4000 | 34.8000 | 26 | 31.0000 | 47.0810 | True | True |
| FD003 | 3 | ISO_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 212.5500 | 34.6500 | 39 | 30.0000 | 47.0478 | True | True |
| FD003 | 3 | ISO_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 210.1600 | 37.0400 | 66 | 33.0000 | 47.5828 | True | True |
| FD003 | 3 | ISO_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 210.8800 | 36.3200 | 71 | 32.0000 | 47.4203 | True | True |
| FD003 | 3 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 210.9800 | 36.2200 | 38 | 31.5000 | 47.3979 | True | True |
| FD003 | 3 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 211.1500 | 36.0500 | 52 | 32.0000 | 47.3597 | True | True |
| FD003 | 3 | ISO_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 209.1600 | 38.0400 | 86 | 34.0000 | 47.8103 | True | True |
| FD003 | 3 | ISO_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 210.1600 | 37.0400 | 100 | 33.0000 | 47.5828 | True | True |
| FD003 | 3 | ISO_POINT_M12_D1 | 84 | 16 | 0 | 1 | 236.1800 | 11.0200 | 0 | 11.0000 | 42.3406 | False | False |
| FD003 | 3 | ISO_POINT_M12_D2 | 89 | 11 | 2 | 1 | 235.3300 | 11.8700 | 0 | 10.0000 | 42.4935 | False | False |
| FD003 | 3 | ISO_POINT_M15_D1 | 90 | 10 | 0 | 2 | 233.4700 | 13.7300 | 0 | 13.0000 | 42.8321 | False | False |
| FD003 | 3 | ISO_POINT_M15_D2 | 92 | 8 | 0 | 2 | 233.7500 | 13.4500 | 0 | 12.0000 | 42.7807 | False | False |
| FD003 | 3 | RF_SLOPE_LOWER95_M12_D1 | 100 | 0 | 0 | 0 | 209.8500 | 37.3500 | 81 | 33.0000 | 47.6531 | True | True |
| FD003 | 3 | RF_SLOPE_LOWER95_M12_D2 | 100 | 0 | 0 | 0 | 210.7600 | 36.4400 | 82 | 32.0000 | 47.4473 | True | True |
| FD003 | 3 | RF_SLOPE_LOWER95_M15_D1 | 100 | 0 | 0 | 0 | 209.5600 | 37.6400 | 88 | 33.5000 | 47.7190 | True | True |
| FD003 | 3 | RF_SLOPE_LOWER95_M15_D2 | 100 | 0 | 0 | 0 | 210.5600 | 36.6400 | 88 | 32.5000 | 47.4924 | True | True |
| FD003 | 3 | RF_SLOPE_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 209.6100 | 37.5900 | 86 | 33.0000 | 47.7076 | True | True |
| FD003 | 3 | RF_SLOPE_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 210.5600 | 36.6400 | 88 | 32.0000 | 47.4924 | True | True |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D1 | 100 | 0 | 0 | 0 | 209.4000 | 37.8000 | 89 | 33.5000 | 47.7555 | True | True |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D2 | 100 | 0 | 0 | 0 | 210.4000 | 36.8000 | 89 | 32.5000 | 47.5285 | True | True |
| FD003 | 3 | RF_SLOPE_POINT_M12_D1 | 89 | 11 | 0 | 1 | 234.5400 | 12.6600 | 0 | 12.0000 | 42.6367 | False | False |
| FD003 | 3 | RF_SLOPE_POINT_M12_D2 | 93 | 7 | 2 | 0 | 234.2100 | 12.9900 | 0 | 12.0000 | 42.6967 | False | False |
| FD003 | 3 | RF_SLOPE_POINT_M15_D1 | 95 | 5 | 0 | 1 | 231.0600 | 16.1400 | 0 | 16.0000 | 43.2788 | False | False |
| FD003 | 3 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 1 | 0 | 231.2000 | 16.0000 | 0 | 16.0000 | 43.2526 | False | False |

## Decisão já na primeira oportunidade

A insuficiência inicial refere-se à reserva PREVISTA pelo limite no primeiro marco, não à reserva real retrospectiva. Uma decisão imediata no marco pode ter antecedência real ampla. Essa concentração limita inferir que o prognóstico sequencial individualiza o momento ótimo. at_first_available conta decisões no primeiro marco disponível.

| subset | repeat | policy_id | decisions | at_first_available | initial_insufficient |
|---|---|---|---|---|---|
| FD001 | 1 | ISO_LOWER98_M15_D1 | 100 | 75 | 75 |
| FD001 | 1 | ISO_LOWER98_M15_D2 | 100 | 86 | 86 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D1 | 100 | 88 | 88 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D2 | 100 | 88 | 88 |
| FD001 | 2 | ISO_LOWER98_M15_D1 | 100 | 70 | 63 |
| FD001 | 2 | ISO_LOWER98_M15_D2 | 100 | 80 | 70 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D1 | 100 | 87 | 87 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D2 | 100 | 89 | 89 |
| FD001 | 3 | ISO_LOWER98_M15_D1 | 100 | 55 | 55 |
| FD001 | 3 | ISO_LOWER98_M15_D2 | 100 | 65 | 65 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D1 | 100 | 84 | 84 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D2 | 100 | 86 | 86 |
| FD003 | 1 | ISO_LOWER98_M15_D1 | 100 | 72 | 72 |
| FD003 | 1 | ISO_LOWER98_M15_D2 | 100 | 90 | 90 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D1 | 100 | 86 | 86 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D2 | 100 | 87 | 87 |
| FD003 | 2 | ISO_LOWER98_M15_D1 | 100 | 74 | 74 |
| FD003 | 2 | ISO_LOWER98_M15_D2 | 100 | 80 | 74 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D1 | 100 | 91 | 91 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D2 | 100 | 93 | 93 |
| FD003 | 3 | ISO_LOWER98_M15_D1 | 100 | 100 | 86 |
| FD003 | 3 | ISO_LOWER98_M15_D2 | 100 | 100 | 100 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D1 | 100 | 89 | 89 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D2 | 100 | 89 | 89 |

## Teste truncado: diagnóstico condicional

Somente decisões possíveis com os dados observados; ausência até o truncamento é censura, não falha definitiva. A data de uma retirada comprometida pode ser confrontada com o endpoint obtido de RUL, sem observar sua execução e sem criar sensores futuros. Nenhum truncado entra na taxa de renovação. conditional_late_fraction usa apenas decisões disponíveis.

| subset | repeat | policy_id | total | decisions | without_decision | late_count | exact_count | conditional_late_fraction | observed_executions |
|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | AGE_D1 | 100 | 43 | 57 | 0 | 0 | 0.0000 | 42 |
| FD001 | 1 | AGE_D2 | 100 | 44 | 56 | 0 | 0 | 0.0000 | 42 |
| FD001 | 1 | ISO_LOWER95_M12_D1 | 100 | 28 | 72 | 0 | 0 | 0.0000 | 27 |
| FD001 | 1 | ISO_LOWER95_M12_D2 | 100 | 28 | 72 | 0 | 0 | 0.0000 | 26 |
| FD001 | 1 | ISO_LOWER95_M15_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | ISO_LOWER95_M15_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | ISO_LOWER98_M12_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | ISO_LOWER98_M12_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | ISO_LOWER98_M15_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | ISO_LOWER98_M15_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | ISO_POINT_M12_D1 | 100 | 7 | 93 | 0 | 0 | 0.0000 | 6 |
| FD001 | 1 | ISO_POINT_M12_D2 | 100 | 8 | 92 | 0 | 0 | 0.0000 | 7 |
| FD001 | 1 | ISO_POINT_M15_D1 | 100 | 10 | 90 | 0 | 0 | 0.0000 | 10 |
| FD001 | 1 | ISO_POINT_M15_D2 | 100 | 12 | 88 | 0 | 0 | 0.0000 | 10 |
| FD001 | 1 | RF_SLOPE_LOWER95_M12_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | RF_SLOPE_LOWER95_M12_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | RF_SLOPE_LOWER95_M15_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | RF_SLOPE_LOWER95_M15_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | RF_SLOPE_LOWER98_M12_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | RF_SLOPE_LOWER98_M12_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 1 | RF_SLOPE_POINT_M12_D1 | 100 | 13 | 87 | 0 | 0 | 0.0000 | 13 |
| FD001 | 1 | RF_SLOPE_POINT_M12_D2 | 100 | 14 | 86 | 0 | 0 | 0.0000 | 11 |
| FD001 | 1 | RF_SLOPE_POINT_M15_D1 | 100 | 15 | 85 | 0 | 0 | 0.0000 | 14 |
| FD001 | 1 | RF_SLOPE_POINT_M15_D2 | 100 | 18 | 82 | 0 | 0 | 0.0000 | 13 |
| FD001 | 2 | AGE_D1 | 100 | 58 | 42 | 0 | 0 | 0.0000 | 56 |
| FD001 | 2 | AGE_D2 | 100 | 59 | 41 | 0 | 0 | 0.0000 | 56 |
| FD001 | 2 | ISO_LOWER95_M12_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 2 | ISO_LOWER95_M12_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 2 | ISO_LOWER95_M15_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 2 | ISO_LOWER95_M15_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 2 | ISO_LOWER98_M12_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 2 | ISO_LOWER98_M12_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 2 | ISO_LOWER98_M15_D1 | 100 | 30 | 70 | 0 | 0 | 0.0000 | 29 |
| FD001 | 2 | ISO_LOWER98_M15_D2 | 100 | 30 | 70 | 0 | 0 | 0.0000 | 29 |
| FD001 | 2 | ISO_POINT_M12_D1 | 100 | 7 | 93 | 0 | 0 | 0.0000 | 7 |
| FD001 | 2 | ISO_POINT_M12_D2 | 100 | 7 | 93 | 0 | 0 | 0.0000 | 6 |
| FD001 | 2 | ISO_POINT_M15_D1 | 100 | 7 | 93 | 0 | 0 | 0.0000 | 7 |
| FD001 | 2 | ISO_POINT_M15_D2 | 100 | 8 | 92 | 0 | 0 | 0.0000 | 7 |
| FD001 | 2 | RF_SLOPE_LOWER95_M12_D1 | 100 | 30 | 70 | 0 | 0 | 0.0000 | 29 |
| FD001 | 2 | RF_SLOPE_LOWER95_M12_D2 | 100 | 30 | 70 | 0 | 0 | 0.0000 | 29 |
| FD001 | 2 | RF_SLOPE_LOWER95_M15_D1 | 100 | 30 | 70 | 0 | 0 | 0.0000 | 29 |
| FD001 | 2 | RF_SLOPE_LOWER95_M15_D2 | 100 | 30 | 70 | 0 | 0 | 0.0000 | 29 |
| FD001 | 2 | RF_SLOPE_LOWER98_M12_D1 | 100 | 30 | 70 | 0 | 0 | 0.0000 | 29 |
| FD001 | 2 | RF_SLOPE_LOWER98_M12_D2 | 100 | 30 | 70 | 0 | 0 | 0.0000 | 29 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D1 | 100 | 30 | 70 | 0 | 0 | 0.0000 | 29 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D2 | 100 | 30 | 70 | 0 | 0 | 0.0000 | 29 |
| FD001 | 2 | RF_SLOPE_POINT_M12_D1 | 100 | 11 | 89 | 0 | 0 | 0.0000 | 11 |
| FD001 | 2 | RF_SLOPE_POINT_M12_D2 | 100 | 11 | 89 | 0 | 0 | 0.0000 | 10 |
| FD001 | 2 | RF_SLOPE_POINT_M15_D1 | 100 | 12 | 88 | 0 | 0 | 0.0000 | 12 |
| FD001 | 2 | RF_SLOPE_POINT_M15_D2 | 100 | 12 | 88 | 0 | 0 | 0.0000 | 11 |
| FD001 | 3 | AGE_D1 | 100 | 58 | 42 | 0 | 0 | 0.0000 | 56 |
| FD001 | 3 | AGE_D2 | 100 | 59 | 41 | 0 | 0 | 0.0000 | 56 |
| FD001 | 3 | ISO_LOWER95_M12_D1 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 25 |
| FD001 | 3 | ISO_LOWER95_M12_D2 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 23 |
| FD001 | 3 | ISO_LOWER95_M15_D1 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 25 |
| FD001 | 3 | ISO_LOWER95_M15_D2 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 25 |
| FD001 | 3 | ISO_LOWER98_M12_D1 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 25 |
| FD001 | 3 | ISO_LOWER98_M12_D2 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 23 |
| FD001 | 3 | ISO_LOWER98_M15_D1 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 25 |
| FD001 | 3 | ISO_LOWER98_M15_D2 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 25 |
| FD001 | 3 | ISO_POINT_M12_D1 | 100 | 7 | 93 | 0 | 0 | 0.0000 | 7 |
| FD001 | 3 | ISO_POINT_M12_D2 | 100 | 10 | 90 | 0 | 0 | 0.0000 | 7 |
| FD001 | 3 | ISO_POINT_M15_D1 | 100 | 10 | 90 | 0 | 0 | 0.0000 | 10 |
| FD001 | 3 | ISO_POINT_M15_D2 | 100 | 11 | 89 | 0 | 0 | 0.0000 | 10 |
| FD001 | 3 | RF_SLOPE_LOWER95_M12_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 3 | RF_SLOPE_LOWER95_M12_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 27 |
| FD001 | 3 | RF_SLOPE_LOWER95_M15_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 29 |
| FD001 | 3 | RF_SLOPE_LOWER95_M15_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 27 |
| FD001 | 3 | RF_SLOPE_LOWER98_M12_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 29 |
| FD001 | 3 | RF_SLOPE_LOWER98_M12_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D1 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 29 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D2 | 100 | 29 | 71 | 0 | 0 | 0.0000 | 28 |
| FD001 | 3 | RF_SLOPE_POINT_M12_D1 | 100 | 13 | 87 | 0 | 0 | 0.0000 | 12 |
| FD001 | 3 | RF_SLOPE_POINT_M12_D2 | 100 | 13 | 87 | 0 | 0 | 0.0000 | 10 |
| FD001 | 3 | RF_SLOPE_POINT_M15_D1 | 100 | 13 | 87 | 0 | 0 | 0.0000 | 13 |
| FD001 | 3 | RF_SLOPE_POINT_M15_D2 | 100 | 15 | 85 | 0 | 0 | 0.0000 | 13 |
| FD003 | 1 | AGE_D1 | 100 | 53 | 47 | 0 | 0 | 0.0000 | 53 |
| FD003 | 1 | AGE_D2 | 100 | 54 | 46 | 0 | 0 | 0.0000 | 53 |
| FD003 | 1 | ISO_LOWER95_M12_D1 | 100 | 20 | 80 | 0 | 0 | 0.0000 | 20 |
| FD003 | 1 | ISO_LOWER95_M12_D2 | 100 | 20 | 80 | 0 | 0 | 0.0000 | 19 |
| FD003 | 1 | ISO_LOWER95_M15_D1 | 100 | 23 | 77 | 0 | 0 | 0.0000 | 22 |
| FD003 | 1 | ISO_LOWER95_M15_D2 | 100 | 24 | 76 | 0 | 0 | 0.0000 | 20 |
| FD003 | 1 | ISO_LOWER98_M12_D1 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 27 |
| FD003 | 1 | ISO_LOWER98_M12_D2 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 26 |
| FD003 | 1 | ISO_LOWER98_M15_D1 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 27 |
| FD003 | 1 | ISO_LOWER98_M15_D2 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 26 |
| FD003 | 1 | ISO_POINT_M12_D1 | 100 | 4 | 96 | 0 | 0 | 0.0000 | 3 |
| FD003 | 1 | ISO_POINT_M12_D2 | 100 | 8 | 92 | 0 | 0 | 0.0000 | 3 |
| FD003 | 1 | ISO_POINT_M15_D1 | 100 | 8 | 92 | 0 | 0 | 0.0000 | 6 |
| FD003 | 1 | ISO_POINT_M15_D2 | 100 | 9 | 91 | 0 | 0 | 0.0000 | 7 |
| FD003 | 1 | RF_SLOPE_LOWER95_M12_D1 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 24 |
| FD003 | 1 | RF_SLOPE_LOWER95_M12_D2 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 21 |
| FD003 | 1 | RF_SLOPE_LOWER95_M15_D1 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 26 |
| FD003 | 1 | RF_SLOPE_LOWER95_M15_D2 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 23 |
| FD003 | 1 | RF_SLOPE_LOWER98_M12_D1 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 27 |
| FD003 | 1 | RF_SLOPE_LOWER98_M12_D2 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 23 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D1 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 27 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D2 | 100 | 27 | 73 | 0 | 0 | 0.0000 | 23 |
| FD003 | 1 | RF_SLOPE_POINT_M12_D1 | 100 | 9 | 91 | 0 | 0 | 0.0000 | 8 |
| FD003 | 1 | RF_SLOPE_POINT_M12_D2 | 100 | 9 | 91 | 0 | 0 | 0.0000 | 8 |
| FD003 | 1 | RF_SLOPE_POINT_M15_D1 | 100 | 11 | 89 | 0 | 0 | 0.0000 | 10 |
| FD003 | 1 | RF_SLOPE_POINT_M15_D2 | 100 | 11 | 89 | 0 | 0 | 0.0000 | 10 |
| FD003 | 2 | AGE_D1 | 100 | 54 | 46 | 0 | 0 | 0.0000 | 54 |
| FD003 | 2 | AGE_D2 | 100 | 54 | 46 | 0 | 0 | 0.0000 | 54 |
| FD003 | 2 | ISO_LOWER95_M12_D1 | 100 | 24 | 76 | 0 | 0 | 0.0000 | 22 |
| FD003 | 2 | ISO_LOWER95_M12_D2 | 100 | 24 | 76 | 0 | 0 | 0.0000 | 21 |
| FD003 | 2 | ISO_LOWER95_M15_D1 | 100 | 24 | 76 | 0 | 0 | 0.0000 | 22 |
| FD003 | 2 | ISO_LOWER95_M15_D2 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 26 |
| FD003 | 2 | ISO_LOWER98_M12_D1 | 100 | 24 | 76 | 0 | 0 | 0.0000 | 22 |
| FD003 | 2 | ISO_LOWER98_M12_D2 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 26 |
| FD003 | 2 | ISO_LOWER98_M15_D1 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 26 |
| FD003 | 2 | ISO_LOWER98_M15_D2 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 26 |
| FD003 | 2 | ISO_POINT_M12_D1 | 100 | 8 | 92 | 0 | 0 | 0.0000 | 7 |
| FD003 | 2 | ISO_POINT_M12_D2 | 100 | 8 | 92 | 0 | 0 | 0.0000 | 6 |
| FD003 | 2 | ISO_POINT_M15_D1 | 100 | 8 | 92 | 0 | 0 | 0.0000 | 8 |
| FD003 | 2 | ISO_POINT_M15_D2 | 100 | 10 | 90 | 0 | 0 | 0.0000 | 9 |
| FD003 | 2 | RF_SLOPE_LOWER95_M12_D1 | 100 | 25 | 75 | 0 | 0 | 0.0000 | 25 |
| FD003 | 2 | RF_SLOPE_LOWER95_M12_D2 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 24 |
| FD003 | 2 | RF_SLOPE_LOWER95_M15_D1 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 26 |
| FD003 | 2 | RF_SLOPE_LOWER95_M15_D2 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 25 |
| FD003 | 2 | RF_SLOPE_LOWER98_M12_D1 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 26 |
| FD003 | 2 | RF_SLOPE_LOWER98_M12_D2 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 25 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D1 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 26 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D2 | 100 | 26 | 74 | 0 | 0 | 0.0000 | 25 |
| FD003 | 2 | RF_SLOPE_POINT_M12_D1 | 100 | 15 | 85 | 0 | 0 | 0.0000 | 13 |
| FD003 | 2 | RF_SLOPE_POINT_M12_D2 | 100 | 15 | 85 | 0 | 0 | 0.0000 | 12 |
| FD003 | 2 | RF_SLOPE_POINT_M15_D1 | 100 | 15 | 85 | 0 | 0 | 0.0000 | 15 |
| FD003 | 2 | RF_SLOPE_POINT_M15_D2 | 100 | 15 | 85 | 0 | 0 | 0.0000 | 14 |
| FD003 | 3 | AGE_D1 | 100 | 54 | 46 | 0 | 0 | 0.0000 | 54 |
| FD003 | 3 | AGE_D2 | 100 | 54 | 46 | 0 | 0 | 0.0000 | 54 |
| FD003 | 3 | ISO_LOWER95_M12_D1 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 22 |
| FD003 | 3 | ISO_LOWER95_M12_D2 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 22 |
| FD003 | 3 | ISO_LOWER95_M15_D1 | 100 | 23 | 77 | 0 | 0 | 0.0000 | 23 |
| FD003 | 3 | ISO_LOWER95_M15_D2 | 100 | 23 | 77 | 0 | 0 | 0.0000 | 22 |
| FD003 | 3 | ISO_LOWER98_M12_D1 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 22 |
| FD003 | 3 | ISO_LOWER98_M12_D2 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 22 |
| FD003 | 3 | ISO_LOWER98_M15_D1 | 100 | 23 | 77 | 0 | 0 | 0.0000 | 23 |
| FD003 | 3 | ISO_LOWER98_M15_D2 | 100 | 23 | 77 | 0 | 0 | 0.0000 | 22 |
| FD003 | 3 | ISO_POINT_M12_D1 | 100 | 2 | 98 | 0 | 0 | 0.0000 | 2 |
| FD003 | 3 | ISO_POINT_M12_D2 | 100 | 3 | 97 | 0 | 0 | 0.0000 | 3 |
| FD003 | 3 | ISO_POINT_M15_D1 | 100 | 4 | 96 | 0 | 0 | 0.0000 | 3 |
| FD003 | 3 | ISO_POINT_M15_D2 | 100 | 4 | 96 | 0 | 0 | 0.0000 | 3 |
| FD003 | 3 | RF_SLOPE_LOWER95_M12_D1 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 22 |
| FD003 | 3 | RF_SLOPE_LOWER95_M12_D2 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 21 |
| FD003 | 3 | RF_SLOPE_LOWER95_M15_D1 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 22 |
| FD003 | 3 | RF_SLOPE_LOWER95_M15_D2 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 21 |
| FD003 | 3 | RF_SLOPE_LOWER98_M12_D1 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 22 |
| FD003 | 3 | RF_SLOPE_LOWER98_M12_D2 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 21 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D1 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 22 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D2 | 100 | 22 | 78 | 0 | 0 | 0.0000 | 21 |
| FD003 | 3 | RF_SLOPE_POINT_M12_D1 | 100 | 6 | 94 | 0 | 0 | 0.0000 | 5 |
| FD003 | 3 | RF_SLOPE_POINT_M12_D2 | 100 | 7 | 93 | 0 | 0 | 0.0000 | 6 |
| FD003 | 3 | RF_SLOPE_POINT_M15_D1 | 100 | 9 | 91 | 0 | 0 | 0.0000 | 8 |
| FD003 | 3 | RF_SLOPE_POINT_M15_D2 | 100 | 9 | 91 | 0 | 0 | 0.0000 | 8 |

## Fronteira descritiva

Não dominadas por menor/igual número de ausências, ultrapassagens e chegadas exactas, e menor/igual vida não aproveitada, com melhoria estrita em pelo menos um indicador. Comparar somente primárias/controle com o mesmo prazo d; não seleccionar a melhor semente.

| subset | repeat | policy_id | decisions | without_decision | late_count | exact_count | mean_utilised | mean_unused | initial_insufficient_count | median_real_reserve | restorations_per_10000_cycles | passes_strict_screen | passes_prudent_screen |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | 1 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 170.2900 | 36.0200 | 40 | 31.0000 | 58.7234 | True | True |
| FD001 | 1 | ISO_POINT_M12_D1 | 80 | 20 | 0 | 3 | 195.9700 | 10.3400 | 0 | 11.0000 | 51.0282 | False | False |
| FD001 | 1 | ISO_POINT_M12_D2 | 87 | 13 | 5 | 5 | 195.3200 | 10.9900 | 0 | 11.0000 | 51.1980 | False | False |
| FD001 | 1 | ISO_POINT_M15_D1 | 95 | 5 | 0 | 2 | 191.1300 | 15.1800 | 0 | 14.0000 | 52.3204 | False | False |
| FD001 | 1 | ISO_POINT_M15_D2 | 95 | 5 | 1 | 4 | 191.3200 | 14.9900 | 0 | 14.0000 | 52.2685 | False | False |
| FD001 | 1 | RF_SLOPE_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 170.1400 | 36.1700 | 83 | 33.0000 | 58.7751 | True | True |
| FD001 | 1 | RF_SLOPE_POINT_M12_D1 | 93 | 7 | 0 | 3 | 193.0800 | 13.2300 | 0 | 14.0000 | 51.7920 | False | False |
| FD001 | 1 | RF_SLOPE_POINT_M12_D2 | 94 | 6 | 3 | 1 | 193.0500 | 13.2600 | 0 | 13.0000 | 51.8001 | False | False |
| FD001 | 1 | RF_SLOPE_POINT_M15_D1 | 94 | 6 | 0 | 0 | 190.8100 | 15.5000 | 0 | 16.0000 | 52.4082 | False | False |
| FD001 | 1 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 0 | 1 | 190.5500 | 15.7600 | 0 | 16.0000 | 52.4797 | False | False |
| FD001 | 2 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 170.0600 | 36.2500 | 45 | 32.5000 | 58.8028 | True | True |
| FD001 | 2 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 170.3600 | 35.9500 | 49 | 32.0000 | 58.6992 | True | True |
| FD001 | 2 | ISO_POINT_M12_D1 | 82 | 18 | 0 | 5 | 195.7500 | 10.5600 | 0 | 10.5000 | 51.0856 | False | False |
| FD001 | 2 | ISO_POINT_M12_D2 | 86 | 14 | 6 | 3 | 195.3100 | 11.0000 | 0 | 10.5000 | 51.2007 | False | False |
| FD001 | 2 | ISO_POINT_M15_D1 | 89 | 11 | 0 | 4 | 193.1600 | 13.1500 | 0 | 12.0000 | 51.7706 | False | False |
| FD001 | 2 | ISO_POINT_M15_D2 | 92 | 8 | 1 | 1 | 191.9700 | 14.3400 | 0 | 13.0000 | 52.0915 | False | False |
| FD001 | 2 | RF_SLOPE_POINT_M12_D1 | 87 | 13 | 0 | 0 | 193.1900 | 13.1200 | 0 | 14.0000 | 51.7625 | False | False |
| FD001 | 2 | RF_SLOPE_POINT_M12_D2 | 91 | 9 | 1 | 3 | 193.4000 | 12.9100 | 0 | 13.0000 | 51.7063 | False | False |
| FD001 | 2 | RF_SLOPE_POINT_M15_D1 | 93 | 7 | 0 | 1 | 190.8700 | 15.4400 | 0 | 16.0000 | 52.3917 | False | False |
| FD001 | 2 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 1 | 0 | 190.3200 | 15.9900 | 0 | 16.0000 | 52.5431 | False | False |
| FD001 | 3 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 170.7900 | 35.5200 | 21 | 33.0000 | 58.5514 | True | True |
| FD001 | 3 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 171.1200 | 35.1900 | 31 | 32.0000 | 58.4385 | True | True |
| FD001 | 3 | ISO_POINT_M12_D1 | 83 | 17 | 0 | 1 | 195.6100 | 10.7000 | 0 | 11.0000 | 51.1221 | False | False |
| FD001 | 3 | ISO_POINT_M12_D2 | 88 | 12 | 3 | 2 | 194.9000 | 11.4100 | 0 | 11.0000 | 51.3084 | False | False |
| FD001 | 3 | ISO_POINT_M15_D1 | 93 | 7 | 0 | 5 | 191.9600 | 14.3500 | 0 | 13.0000 | 52.0942 | False | False |
| FD001 | 3 | ISO_POINT_M15_D2 | 96 | 4 | 4 | 2 | 191.6000 | 14.7100 | 0 | 13.5000 | 52.1921 | False | False |
| FD001 | 3 | RF_SLOPE_POINT_M12_D1 | 86 | 14 | 0 | 3 | 194.3200 | 11.9900 | 0 | 13.0000 | 51.4615 | False | False |
| FD001 | 3 | RF_SLOPE_POINT_M12_D2 | 90 | 10 | 4 | 2 | 193.9400 | 12.3700 | 0 | 13.0000 | 51.5623 | False | False |
| FD001 | 3 | RF_SLOPE_POINT_M15_D1 | 94 | 6 | 0 | 3 | 190.9300 | 15.3800 | 0 | 16.0000 | 52.3752 | False | False |
| FD001 | 3 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 3 | 4 | 190.7500 | 15.5600 | 1 | 16.0000 | 52.4246 | False | False |
| FD003 | 1 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 210.1800 | 37.0200 | 70 | 34.0000 | 47.5783 | True | True |
| FD003 | 1 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 211.0500 | 36.1500 | 70 | 33.0000 | 47.3821 | True | True |
| FD003 | 1 | ISO_POINT_M12_D1 | 85 | 15 | 0 | 1 | 236.5400 | 10.6600 | 0 | 11.0000 | 42.2761 | False | False |
| FD003 | 1 | ISO_POINT_M12_D2 | 85 | 15 | 1 | 1 | 236.7500 | 10.4500 | 0 | 10.0000 | 42.2386 | False | False |
| FD003 | 1 | ISO_POINT_M15_D1 | 88 | 12 | 0 | 1 | 233.2300 | 13.9700 | 0 | 14.0000 | 42.8761 | False | False |
| FD003 | 1 | RF_SLOPE_POINT_M12_D1 | 89 | 11 | 0 | 3 | 234.7900 | 12.4100 | 0 | 12.0000 | 42.5913 | False | False |
| FD003 | 1 | RF_SLOPE_POINT_M12_D2 | 92 | 8 | 2 | 1 | 234.0300 | 13.1700 | 0 | 14.0000 | 42.7296 | False | False |
| FD003 | 1 | RF_SLOPE_POINT_M15_D1 | 95 | 5 | 0 | 1 | 229.4000 | 17.8000 | 0 | 17.0000 | 43.5920 | False | False |
| FD003 | 1 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 0 | 2 | 229.3000 | 17.9000 | 0 | 16.0000 | 43.6110 | False | False |
| FD003 | 2 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 207.2600 | 39.9400 | 37 | 32.0000 | 48.2486 | True | True |
| FD003 | 2 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 207.2700 | 39.9300 | 48 | 32.0000 | 48.2462 | True | True |
| FD003 | 2 | ISO_POINT_M12_D1 | 77 | 23 | 0 | 3 | 237.0400 | 10.1600 | 0 | 10.0000 | 42.1870 | False | False |
| FD003 | 2 | ISO_POINT_M12_D2 | 83 | 17 | 1 | 4 | 236.0100 | 11.1900 | 0 | 11.0000 | 42.3711 | False | False |
| FD003 | 2 | ISO_POINT_M15_D1 | 85 | 15 | 0 | 2 | 232.3600 | 14.8400 | 0 | 14.0000 | 43.0367 | False | False |
| FD003 | 2 | ISO_POINT_M15_D2 | 93 | 7 | 2 | 4 | 231.3900 | 15.8100 | 0 | 13.0000 | 43.2171 | False | False |
| FD003 | 2 | RF_SLOPE_POINT_M12_D1 | 88 | 12 | 0 | 4 | 231.8900 | 15.3100 | 0 | 14.5000 | 43.1239 | False | False |
| FD003 | 2 | RF_SLOPE_POINT_M12_D2 | 91 | 9 | 4 | 2 | 231.7200 | 15.4800 | 0 | 14.0000 | 43.1555 | False | False |
| FD003 | 2 | RF_SLOPE_POINT_M15_D1 | 94 | 6 | 0 | 3 | 228.5000 | 18.7000 | 0 | 16.0000 | 43.7637 | False | False |
| FD003 | 2 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 3 | 0 | 228.0300 | 19.1700 | 0 | 16.0000 | 43.8539 | False | False |
| FD003 | 3 | ISO_LOWER98_M12_D1 | 100 | 0 | 0 | 0 | 210.9800 | 36.2200 | 38 | 31.5000 | 47.3979 | True | True |
| FD003 | 3 | ISO_LOWER98_M12_D2 | 100 | 0 | 0 | 0 | 211.1500 | 36.0500 | 52 | 32.0000 | 47.3597 | True | True |
| FD003 | 3 | ISO_POINT_M12_D1 | 84 | 16 | 0 | 1 | 236.1800 | 11.0200 | 0 | 11.0000 | 42.3406 | False | False |
| FD003 | 3 | ISO_POINT_M12_D2 | 89 | 11 | 2 | 1 | 235.3300 | 11.8700 | 0 | 10.0000 | 42.4935 | False | False |
| FD003 | 3 | ISO_POINT_M15_D1 | 90 | 10 | 0 | 2 | 233.4700 | 13.7300 | 0 | 13.0000 | 42.8321 | False | False |
| FD003 | 3 | ISO_POINT_M15_D2 | 92 | 8 | 0 | 2 | 233.7500 | 13.4500 | 0 | 12.0000 | 42.7807 | False | False |
| FD003 | 3 | RF_SLOPE_POINT_M12_D1 | 89 | 11 | 0 | 1 | 234.5400 | 12.6600 | 0 | 12.0000 | 42.6367 | False | False |
| FD003 | 3 | RF_SLOPE_POINT_M12_D2 | 93 | 7 | 2 | 0 | 234.2100 | 12.9900 | 0 | 12.0000 | 42.6967 | False | False |
| FD003 | 3 | RF_SLOPE_POINT_M15_D1 | 95 | 5 | 0 | 1 | 231.0600 | 16.1400 | 0 | 16.0000 | 43.2788 | False | False |
| FD003 | 3 | RF_SLOPE_POINT_M15_D2 | 95 | 5 | 1 | 0 | 231.2000 | 16.0000 | 0 | 16.0000 | 43.2526 | False | False |

## Limites e rastreabilidade

Não houve simulação de 20 anos, monetização, inspeção ou edição do artigo. As métricas por 10.000 ciclos referem-se à exposição simulada, sem afirmar equivalência com voo real. P12 ainda exige ponte de escala; ganho empresarial exige margem incremental, demanda, disponibilidade e harmonização monetária. O marco não identifica P e o endpoint não valida margens físicas de sensores. Zero eventos em uma amostra exploratória não certifica risco ≤2%.

O primeiro verificador encontrou motores truncados sem qualquer previsão após aquecimento; a correção trata esse grupo como trajetória vazia, preservando decisões e resultados. Houve ainda correção de separador Windows no mapeamento de fonte arquivada. Código original e logs foram preservados. [Correção do verificador](verifier_correction.json).

[Verificação independente](verification.json); [metadados](metadata.json); [controle congelado por dobra](controls.json); [decisões](decisions.csv); [contrastes](contrasts.csv); [manifesto](manifest.json).
