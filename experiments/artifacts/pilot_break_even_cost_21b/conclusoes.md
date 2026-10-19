# P21.2 — custo de equilíbrio com custo positivo de inspeção: conclusões

Execução de 19/10/2026 (emenda E11/E11.1), exploratória e posterior à confirmação; FD002/FD004 já examinados. Sensibilidade declarada: o cenário principal do artigo mantém custo incremental de inspeção zero. Só decisões e expectativas arquivadas (P17.1/P17.2/P13.1); nenhum sensor lido. Custo da inspeção $c_I=q_I c_R$ com $q_I=0{,}01$ central (cerca de US$60 mil a $c_R$ = US$6 milhões) e grade $\{0;\,0{,}005;\,0{,}01;\,0{,}02\}$. Custo por ciclo em unidades de overhaul: $\varpi+q_I\nu+\beta\eta$, onde $\nu$ é a taxa de inspeções; tempo de oficina da inspeção zero. $\beta^*$ é um limiar de decisão, não um custo estimado.

Convenções como em P21.1: amplitude entre as três repetições (que reutilizam os motores), cenário S2_W60_g1, $u=0$; "limitado" = intervalo de 95% de $\Delta\eta$ exclui zero em todas as repetições.

## Validação

- $q_I=0$ reproduz P21.1 em todas as 2.592 linhas (diferença relativa máxima 7e-13; classes e indicadores de limitação idênticos).
- Contagens de inspeção reproduzem `inspections_per_engine` de P17.1 (1e-9 relativo); braços sem inspeção têm $\nu=0$; o custo equivalente do braço híbrido é monótono em $q_I$.
- 10.368 contrastes (108 por célula, prazo e $q_I$), 114.048 pontos de curva de preferência.
- Primeira execução falhou na validação interna por defeitos da própria função de validação (chave vazia contra NaN; 0/0 com $u=1$); preservada em `pilot_break_even_cost_21b_failed_run1` (E11.1).

## Resultados (prazo 1; prazo 2 em `contrast_summary.csv`)

Inspeções esperadas por vida: 7,7–7,9 (FD001), 7,9–8,1 (FD002), 14,9–15,7 (FD003) e 15,6 (FD004) no híbrido sobre ISO limite inferior; 9,5/9,4/17,3/16,1 sobre ISO ponto. Com $q_I=0{,}01$, isso soma 0,08–0,17 overhauls por vida, comparável ao ganho de restaurações do braço.

| Contraste ($\beta^*$) | $q_I=0$ | 0,005 | 0,01 | 0,02 |
|---|---|---|---|---|
| C3 inspeção sobre ISO ponto, todas as faixas (2 prazos, 4 subconjuntos) | 0,50–2,08 | 0,86–3,13 | 1,22–4,18 | 1,93–6,28 |
| C4 inspeção sobre RF ponto | 0,82–2,99 | 1,37–4,55 | 1,81–6,11 | 2,69–9,23 |
| C5 FD004, inspeção sobre ISO limite inferior (não limitado) | 5,8–11,8 | 12,9–27,0 | 20,0–42,1 | 34,1–72,4 |
| C8 FD001–FD003, ponto + inspeção vs ISO limite inferior | preferido só se $\beta<$ 1,5–1.432 ou dominado | B domina | B domina | B domina |

Em C3 e C4 todos os limiares permanecem limitados em todas as repetições e aumentam de forma aproximadamente linear com $q_I$ (em FD001, C3: 0,94–1,72 → 1,72–3,24 → 2,49–4,75).

## Leitura

1. Um custo de inspeção de 1% do overhaul quase **dobra** o custo de equilíbrio da inspeção sobre as regras de ponto: ela só se paga se um evento de fim de vida custar cerca de 1,2–4,2 overhauls adicionais (ISO) ou 1,8–6,1 (RF-slope), contra 0,5–2,1 e 0,8–3,0 com custo zero. A margem calibrada (C1, C2) não é afetada por $q_I$ e continua mais barata para limiares de 0,3–2,2 (ISO) e 0,4–2,8 (RF).
2. Em FD001–FD003 a inspeção sobre a regra conservadora continua dominada (sem evento evitado) e fica mais cara com $q_I$; em FD004 o limiar sobe para 20–42 e permanece sem suporte estatístico.
3. **Ponto + inspeção deixa de ser alternativa à margem**: para $q_I\ge0{,}005$ o PHM conservador domina em FD001–FD003 (menos restaurações-equivalentes e não mais eventos), eliminando a ambiguidade de C8 observada com custo zero. Em FD004, o limiar é 20–41, não limitado.
4. A ordem qualitativa de P21.1 permanece: margem barata em relação ao custo do evento, inspeção cara em relação a ele; a inspeção só se justifica se o evento for substancialmente mais caro que um overhaul adicional.

## Limites

- $q_I$ é valor de cenário, não estimado; nenhuma inspeção foi precificada com fonte pública. Tempo de oficina, custo por achado e reparo corretivo permanecem zero.
- Condicional ao gerador de inspeção (RUL verdadeiro no ambiente, sem calibração) e a repetições que reutilizam motores; contagens de inspeção são esperanças exatas, sem variância de execução.
- Não é otimização econômica nem aprovação. O cenário principal do artigo continua com custo de inspeção zero; esta análise é uma sensibilidade.

Artefatos: `rates.csv` (13.152), `contrasts.csv` (10.368), `contrast_summary.csv` (3.456), `preference_curves.csv` (114.048), `frontier.csv` (1.152), `validation.json`, `metadata.json`, `manifest.json`, cópias `source_*`. Protocolo `experiments/protocolo_custo_inspecao_21b.md`; log `experiments/p21b_execution.log`; verificação `experiments/verify_p21b.log`.
