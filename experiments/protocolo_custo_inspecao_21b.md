# P21.2 — sensibilidade do custo de equilíbrio ao custo da inspeção

Especificado e autorizado em 19/10/2026 ("Pode especificar e executar com custo da inspeção cerca de 1% do custo do overhaul"), na sequência da sugestão de sensibilidade ao custo da inspeção. Análise exploratória posterior ao congelamento e à confirmação; FD002/FD004 já examinados. Exige a emenda E11 em `congelamento_2026-10-18/emendas.md`, com o SHA-256 deste protocolo e dos scripts, registrada antes da execução. Não altera o protocolo congelado, as políticas, o gerador de inspeção, o cenário principal (custo incremental de inspeção zero, M21) nem as saídas P17.1, P17.2, P20.x e P21.1.

## 1. Motivação

P21.1 supôs custo incremental de inspeção igual a zero (M21). Com custo positivo, a comparação PHM contra PHM + inspeção muda: cada inspeção é paga, mesmo quando não evita evento. Esta análise reutiliza as contagens esperadas de inspeção já arquivadas e mede quanto o custo da inspeção desloca o custo de equilíbrio $\beta^*$.

## 2. Definições

- Custo da inspeção $c_I = q_I\,c_R$, com $c_R$ = custo médio do overhaul (US$6 milhões). Valor central $q_I=0{,}01$ (autor: "cerca de 1% do custo do overhaul", isto é, cerca de US$60 mil por inspeção). Grade de sensibilidade $q_I\in\{0;\ 0{,}005;\ 0{,}01;\ 0{,}02\}$, que delimita "cerca de 1%" por metade e dobro; $q_I=0$ reproduz P21.1.
- Taxa de inspeções por ciclo simulado $\nu^\pi=\sum_i N_i^\pi/\sum_i \ell_i^\pi$, onde $N_i^\pi$ é o número esperado de inspeções do motor $i$ (coluna `inspections` das expectativas arquivadas) e $\ell_i^\pi$ a vida utilizada esperada. Arms sem inspeção (PHM, idade, regras selecionadas): $\nu=0$.
- Custo por ciclo, em unidades de $c_R$: $\varpi^\pi+q_I\nu^\pi+\beta\eta^\pi$. Com $\varpi^\pi_{\mathrm{ef}}=\varpi^\pi+q_I\nu^\pi$ (restaurações-equivalentes por ciclo), toda a álgebra de P21.1 se mantém com $\varpi_{\mathrm{ef}}$ no lugar de $\varpi$: $\Delta\varpi_{\mathrm{ef}}=\Delta\varpi+q_I\Delta\nu$, $\Delta\nu=\nu^A-\nu^B$, e
  $$\beta^*=\frac{\Delta\varpi+q_I\Delta\nu}{\Delta\eta},\quad\Delta\eta=\eta^B-\eta^A.$$
  As mesmas classes (A domina, B domina, limiar acima, limiar abaixo, empate) e a mesma tolerância relativa $10^{-9}\varpi_{\mathrm{ef}}^B$ são usadas.
- Indisponibilidade/tempo de oficina da inspeção permanece zero; apenas o custo direto de execução é considerado. Sem desconto, sem custo adicional de inspeção por achado, sem reparo corretivo.

## 3. Dados, contrastes e incerteza

- Mesmas entradas e hashes de P21.1 (`pilot_inspection_17b/expectations.csv.gz` f7ce6b0647deddf1cf2241cb3cf63e2d6fb17c4d7dc553a32891dcde917ecd60; `pilot_inspection_latent_17c/expectations.csv.gz` 3bfdf83cc0b797eeeb03a531af81e9f1cafedf1063e9cfc2a48c21a1ba21114c), regras selecionadas P13.1 como braços PHM com $\nu=0$, contrastes C1–C8, cenários de inspeção e grade de $\beta$ de P21.1.
- Bootstrap pareado sobre motores, B=4000, semente 20261021 e a mesma construção das contagens multinomiais por (origem, subconjunto, repetição) de P21.1; o bootstrap re-amostra conjuntamente $\ell_i$, eventos e $N_i$. Repetições reportadas separadamente, como amplitudes.
- $\beta^*$ é delimitado só se o intervalo de 95% de $\Delta\eta$ exclui zero (inalterado: o custo da inspeção não afeta $\Delta\eta$).

## 4. Verificações antes de relatar

1. Para $q_I=0$, taxas, $\Delta\varpi$, $\Delta\eta$, classes, $\beta^*$ e intervalos coincidem com `pilot_break_even_21a/contrasts.csv` (diferença relativa ≤ 1e-9).
2. A média de inspeções por motor dos braços híbridos coincide com `inspections_per_engine` de `pilot_inspection_17b/summary.csv` (1e-9 relativo).
3. Testes sintéticos com $\beta^*$ conhecido com e sem custo de inspeção; verificação de que $\nu=0$ para braços sem inspeção; monotonicidade: para os contrastes C3, C4, C5, C8 com $\Delta\nu>0$, a restauração-equivalente de A não diminui com $q_I$.
4. Verificador independente reconstrói das fontes brutas contrastes, curvas de preferência e a frontier para todos os $q_I$.

## 5. Interpretação predeclarada

- $q_I$ é um valor de cenário, não estimado; nenhuma inspeção boroscópica foi precificada com fonte pública (M21). O resultado é condicional ao gerador de inspeção, sem calibração.
- Previsão (não critério de sucesso): C5 permanece dominado em FD001–FD003 para todo $q_I$; os limiares de C3 e C4 aumentam com $q_I$ em proporção a $\Delta\nu/\Delta\eta$; C8 passa a favorecer o PHM conservador onde a inspeção acrescenta restaurações-equivalentes. Resultados contrários são relatados.
- Não é otimização econômica, risco populacional nem aprovação. O cenário principal do artigo mantém custo de inspeção zero; esta análise é uma sensibilidade declarada.

## 6. Artefatos previstos

`experiments/break_even_cost_21b.py`, `test_break_even_cost_21b.py`, `verify_break_even_cost_21b.py`; saídas em `experiments/artifacts/pilot_break_even_cost_21b/`: `rates.csv`, `contrasts.csv`, `contrast_summary.csv`, `preference_curves.csv`, `frontier.csv`, `validation.json`, `metadata.json`, `manifest.json`, `conclusoes.md`.
