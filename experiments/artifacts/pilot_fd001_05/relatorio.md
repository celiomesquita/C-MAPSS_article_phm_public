# P05 — HI empírico e AAKR terminal

Rodada exploratória sem inspeções. AAKR é adaptação do núcleo terminal, não reprodução integral de Baraldi et al. (2018).

RUL_FD001 rotula o último ciclo de cada motor de teste. Não fornece HI físico nem sensores futuros. As configurações foram selecionadas antes da avaliação oficial, com registro em official_freeze.json.

## Utilidade prognóstica

Conversor isotônico HI→RUL idêntico entre famílias, aprendido em motores separados.

| Dados | Família | RMSE nos cortes | RMSE último ciclo | MAE último ciclo | RMSE médio por motor na história |
|---|---|---|---|---|---|
| cv | AAKR | 24.71 | 21.17 | 19.00 | 27.45 |
| cv | EMPIRICO | 25.17 | 11.19 | 10.54 | 27.85 |
| cv | MARGEM | 24.67 | 12.41 | 11.17 | 28.60 |
| official | AAKR | — | 27.57 | 20.42 | 31.29 |
| official | EMPIRICO | — | 27.66 | 20.00 | 30.65 |
| official | MARGEM | — | 28.85 | 22.35 | 32.49 |

No último ciclo das trajetórias CV a RUL verdadeira é zero; no teste oficial ela varia de 7 a 145. Não comparar essas colunas entre conjuntos como dificuldade equivalente.

## Diagnóstico de condição

| Dados | Família | HI mediano no último ciclo | Motores com zero | Antecipação mediana do zero | Máxima | Recuperações | Saída inicial média |
|---|---|---|---|---|---|---|---|
| cv | AAKR | 0.0000 | 92 | 18.5 | 64.0 | 43 | 0.591 |
| cv | EMPIRICO | 0.0000 | 71 | 14.0 | 49.0 | 0 | 0.591 |
| cv | MARGEM | 0.0000 | 63 | 14.0 | 42.0 | 6 | 0.812 |
| official | AAKR | 0.6978 | 9 | 19.0 | 34.0 | 1 | 0.626 |
| official | EMPIRICO | 0.7524 | 6 | 16.0 | 26.0 | 0 | 0.692 |
| official | MARGEM | 0.7271 | 6 | 21.0 | 33.0 | 0 | 0.829 |

No teste oficial, o último HI é anterior a F: não equivale a HI terminal. Ausências de zero permanecem censuradas; sensores posteriores ao truncamento não foram simulados. Saída inicial é proporção de ciclos 21–40 por motor, sob hipótese de estabilidade não confirmada.

## Escolhas no ajuste final

- MARGEM: q0.75; RMSE interno 24.96 ciclos.
- EMPIRICO: t100_g1_r0.1; RMSE interno 21.56 ciclos.
- AAKR: top10_L5_h8; RMSE interno 22.60 ciclos.

## Incerteza descritiva no teste oficial

Diferença de RMSE relativamente ao controle; valores negativos favorecem a alternativa.

- EMPIRICO: -1.19 ciclos; percentis 2,5%–97,5% do bootstrap pareado [-4.05; 1.65].
- AAKR: -1.28 ciclos; percentis 2,5%–97,5% do bootstrap pareado [-3.90; 1.43].

## Limites e decisão

O alvo de treino do HI empírico é uma função convencional de RUL. A avaliação externa mede utilidade prognóstica e comportamento da curva, sem observar o HI verdadeiro. Boa previsão por um conversor não demonstra recuperação de margens físicas nem fidelidade causal dos pesos.

AAKR emprega atributos causais e seleção de subconjuntos determinística, substituindo componentes do artigo original. A comparação identifica desempenho destas implementações sob este orçamento, não superioridade sobre a reprodução integral de Baraldi. O número de configurações por família é diferente e está preservado em selection.csv.

O conversor e as referências usam 40/20/20/20 em CV e 60/20/20 no ajuste oficial, sem reajuste depois da seleção. Não há escolha retrospectiva por menor RMSE oficial. A ausência ou antecipação excessiva de zeros limita o uso do HI para F e para inspeções, mesmo quando os erros de RUL forem menores.

Artefatos: predições por ciclo, métricas por motor, todas as escolhas internas, coeficientes, rankings, modelos completos e conversores, auditoria de rótulos, bootstrap, figura, partições e metadados. Inspeções e protocolo principal permanecem suspensos/abertos.
