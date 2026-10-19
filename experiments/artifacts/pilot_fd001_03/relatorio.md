# P03 — robustez de P e diagnóstico empírico HI/F

Rodada exploratória, sem inspeções. Cinco folds por motor, grupos 40/20/20/20 de P02. Foram examinadas 18 configurações com previsões e margem comuns por modelo/fold. Não se escolheu configuração vencedora com dados externos. O conjunto de treino agora começa no ciclo 21; diferenças P02/P03 também reflectem essa mudança e não isolam o detector.

## Robustez da detecção

| config | b0 | window | persistence | engines | detected | median_P | early_40 | early_b0 | median_lead |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B0_30_w_10_d_3 | 30 | 10 | 3 | 100 | 100 | 44.500 | 39 | 11 | 148.500 |
| B0_30_w_10_d_5 | 30 | 10 | 5 | 100 | 100 | 43.000 | 44 | 8 | 152.000 |
| B0_30_w_15_d_3 | 30 | 15 | 3 | 100 | 100 | 41.000 | 49 | 8 | 159.000 |
| B0_30_w_15_d_5 | 30 | 15 | 5 | 100 | 100 | 38.000 | 63 | 4 | 160.000 |
| B0_30_w_5_d_3 | 30 | 5 | 3 | 100 | 100 | 66.000 | 16 | 8 | 133.500 |
| B0_30_w_5_d_5 | 30 | 5 | 5 | 100 | 100 | 62.000 | 16 | 6 | 137.500 |
| B0_40_w_10_d_3 | 40 | 10 | 3 | 100 | 100 | 67.000 | 8 | 8 | 131.500 |
| B0_40_w_10_d_5 | 40 | 10 | 5 | 100 | 100 | 68.000 | 8 | 8 | 131.000 |
| B0_40_w_15_d_3 | 40 | 15 | 3 | 100 | 100 | 69.500 | 6 | 6 | 128.000 |
| B0_40_w_15_d_5 | 40 | 15 | 5 | 100 | 100 | 69.000 | 5 | 5 | 129.000 |
| B0_40_w_5_d_3 | 40 | 5 | 3 | 100 | 100 | 74.500 | 6 | 6 | 124.500 |
| B0_40_w_5_d_5 | 40 | 5 | 5 | 100 | 100 | 72.000 | 10 | 10 | 126.500 |
| B0_50_w_10_d_3 | 50 | 10 | 3 | 100 | 100 | 79.500 | 6 | 10 | 118.000 |
| B0_50_w_10_d_5 | 50 | 10 | 5 | 100 | 100 | 79.000 | 5 | 7 | 119.500 |
| B0_50_w_15_d_3 | 50 | 15 | 3 | 100 | 100 | 79.000 | 2 | 5 | 116.000 |
| B0_50_w_15_d_5 | 50 | 15 | 5 | 100 | 100 | 80.500 | 4 | 7 | 116.500 |
| B0_50_w_5_d_3 | 50 | 5 | 3 | 100 | 100 | 82.000 | 4 | 6 | 117.000 |
| B0_50_w_5_d_5 | 50 | 5 | 5 | 100 | 100 | 81.500 | 3 | 5 | 115.500 |

100/100 motores tiveram alerta nas 18 configurações. A amplitude mediana de P no mesmo motor foi 51.0 ciclos; a maior foi 122.0. Amplitudes usam os alertas disponíveis; ausência em alguma configuração não é convertida em P=0. Alertas até 40 usam um horizonte comum; alertas até B0 usam a hipótese própria de cada configuração. Nenhum desses indicadores constitui acurácia de P físico. A configuração B0=40/w=15/d=3 reproduz os alertas de P02, verificação de continuidade do detector.

![Robustez do ciclo de alerta](P_robustness.png)

## Efeito nas decisões com previsão controlada

| model | variant | min_endpoints | max_endpoints | min_unused | max_unused |
| --- | --- | --- | --- | --- | --- |
| GBR | local_gate30 | 0 | 0 | 25.940 | 25.940 |
| GBR | raw | 13 | 13 | 8.990 | 8.990 |
| LGBM | local_gate30 | 0 | 0 | 24.770 | 24.770 |
| LGBM | raw | 1 | 1 | 10.250 | 10.250 |
| RF | local_gate30 | 0 | 0 | 24.170 | 24.170 |
| RF | raw | 1 | 1 | 9.380 | 9.380 |
| XGB | local_gate30 | 0 | 0 | 24.590 | 24.590 |
| XGB | raw | 0 | 0 | 9.660 | 9.660 |

As amplitudes da tabela são entre as 18 configurações, não intervalos de confiança nem escolha de configuração. `raw` não tem margem; `local_gate30` usa margem local e região prevista ≤30. Ambas têm gatilho 10 e acção imediata como cenário. Detecção variável com desfechos estáveis significa apenas que as alterações antecedem a região decisória na maioria dos casos; não valida P. O máximo de ciclos de remoção distintos por motor/modelo/política entre configurações foi 1; nesta rodada, a invariância verificou-se também por motor, não apenas nas médias agregadas.

## Proxy HI/F

| quantile | engines | zero_crossings | median_endpoint_HI | zero_at_endpoint | median_lead_HI | min_lead_HI | max_lead_HI | before_earliest_P | recovers_after_zero |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.500 | 100 | 94 | 0.000 | 94 | 42.500 | 0.000 | 270.000 | 1 | 30 |
| 0.900 | 100 | 41 | 0.032 | 41 | 5.000 | 0.000 | 22.000 | 0 | 5 |

Direcções e referências terminais foram aprendidas somente nos motores de ajuste. O HI é 1 no ciclo 20; não foi forçado a zero no endpoint externo nem a decrescer após P. `median_lead_HI` é endpoint menos primeira passagem do HI por zero; positivo indica antecipação. Motores sem passagem por zero até o endpoint ficam censurados, não recebem F inventado. Recuperação após zero indica instabilidade da interpretação de primeira passagem; não é restauração física. A proxy não foi usada para agir, calibrar RUL ou simular inspeções.

![HI nos motores 1, 2 e 3, escolhidos antes da execução](HI_examples.png)

## Limitações e condições para avançar

As medianas de P variaram de 38 a 82 ciclos entre configurações, apesar das decisões invariantes. Isso não justifica escolher a configuração mais tardia como fisicamente mais correcta. A referência terminal mediana produziu 94 passagens por zero, seis ausências, antecipação mediana de 42,5 ciclos entre as passagens e máxima de 270, com recuperação após zero em 30 motores. Com quantil 0,90 houve 41 passagens, 59 ausências e antecipação mediana de cinco ciclos entre as passagens; a mediana de HI no endpoint foi aproximadamente 0,032. Essa proximidade de zero não demonstra margem física nem define automaticamente a tolerância de F. Preservar os casos de ausência e recuperação; não escolher normalização por endpoint externo para removê-los.

O intervalo inicial estável é assumido; não há rótulo independente de P ou margens físicas FD001. A proxy mínima entre sensores pode antecipar o zero por variabilidade ou por um canal fraco; um terminal aprendido da frota não garante zero em cada motor. Não congelar a referência somente porque ela se correlaciona com o endpoint. Verificar mecanismo, canais e robustez sem normalização pelo endpoint externo. Segurança e antecedência ainda não estão validadas. Inspeções continuam adiadas até congelamento do protocolo principal.

## Verificações e artefactos

[Protocolo](../../protocolo_piloto_fd001_03.md). Partições disjuntas, escolhas de limiares reproduzidas das tabelas internas, margens recalculadas da calibração, todas as decisões recalculadas das mesmas previsões, referência de P02 reproduzida e hashes de dados/fontes verificados. CSVs preservam os resultados completos por motor, configurações e curvas HI. Nenhum resultado externo foi usado para substituir a escolha interna de limiar.
