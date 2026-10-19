# P04 — resultados exploratórios do HI

Sem inspeção e sem alteração das políticas de remoção.

## Curvas seleccionadas internamente

λ é a penalização convencional de ausência de zero; k multiplica σ na tolerância inicial.

| λ | k | Passagens/100 | Sem zero | Antecipação mediana | Máxima | HI terminal mediano | Saída inicial média | Recuperações |
|---|---|---|---|---|---|---|---|---|
| 0.25 | 0 | 65 | 35 | 11.0 | 34.0 | 0.0000 | 1.000 | 6 |
| 0.25 | 2 | 65 | 35 | 11.0 | 34.0 | 0.0000 | 0.812 | 6 |
| 0.25 | 3 | 65 | 35 | 11.0 | 34.0 | 0.0000 | 0.593 | 6 |
| 0.5 | 0 | 74 | 26 | 16.5 | 42.0 | 0.0000 | 1.000 | 7 |
| 0.5 | 2 | 74 | 26 | 16.5 | 42.0 | 0.0000 | 0.812 | 7 |
| 0.5 | 3 | 74 | 26 | 16.5 | 42.0 | 0.0000 | 0.593 | 7 |
| 1 | 0 | 81 | 19 | 21.0 | 171.0 | 0.0000 | 1.000 | 15 |
| 1 | 2 | 81 | 19 | 21.0 | 171.0 | 0.0000 | 0.812 | 15 |
| 1 | 3 | 81 | 19 | 21.0 | 171.0 | 0.0000 | 0.593 | 15 |
| 2 | 0 | 88 | 12 | 45.0 | 270.0 | 0.0000 | 1.000 | 28 |
| 2 | 2 | 88 | 12 | 45.0 | 270.0 | 0.0000 | 0.812 | 28 |
| 2 | 3 | 88 | 12 | 45.0 | 270.0 | 0.0000 | 0.593 | 28 |

## Escolhas por fold

- λ=0.25: quantis [0.75, 0.75, 0.75, 0.9, 0.75].
- λ=0.5: quantis [0.75, 0.65, 0.75, 0.5, 0.75].
- λ=1: quantis [0.65, 0.5, 0.65, 0.5, 0.75].
- λ=2: quantis [0.65, 0.5, 0.5, 0.5, 0.5].

## Resultado e decisão

Resultado misto. Na configuração principal, 81/100 motores chegaram a zero, com antecipação mediana 21 ciclos e máxima 171, entre passagens. Houve 19 ausências e 15 recuperações posteriores a zero. A saída do patamar inicial ocorreu em média em 81.2% dos ciclos 21–40 por motor, apesar da tolerância de dois desvios.

A tolerância reduz a resposta à variabilidade inicial, mas não sustenta o patamar pretendido nesta amostra; a interpretação pressupõe que o intervalo 21–40 seja estável, hipótese ainda não confirmada. A referência terminal mantém compromisso forte entre antecipação e ausência, dependente da penalização convencional. Não adoptar ainda o primeiro zero como F nem esta curva como gerador de inspeções. Investigar calibração conjunta da variabilidade entre sensores e heterogeneidade terminal, sem impor monotonicidade para encobrir as recuperações.

## Limites da interpretação

A tolerância muda o patamar e a amplitude do HI, mas não o primeiro zero para canais e referências fixos. As três tolerâncias não constituem três evidências independentes de F.

A referência terminal é supervisionada pelos endpoints dos motores de ajuste. Não representa limites operacionais certificados. Não há observações posteriores ao endpoint: ausência de zero é censura, não atraso medido.

O primeiro zero pode ser seguido de recuperação; monotonicidade não foi imposta. O período inicial assumido estável não tem rótulo físico independente. Se o endpoint cair dentro da região de tolerância, a própria interpretação de saúde precisa de revisão.

A perda de selecção e λ são convenções exploratórias, não custos de manutenção ou critérios de segurança. A sensibilidade a λ limita qualquer adopção definitiva. As cinco avaliações externas reutilizam dados já examinados em P01–P03.

A lista de sensores elegíveis está em reference.csv (inclui excluídos). Os empates do mínimo têm um representante por ordem de coluna, não uma causa exclusiva.

Artefatos: candidate_metrics.csv/candidate_summary.csv (todos os candidatos), selection.csv e selection_engines_fold*.csv (selecção interna), selected_metrics.csv/selected_summary.csv (avaliação das escolhas), selected_trajectories.csv, HI_examples.png, splits.json, metadata.json e manifest.json.
