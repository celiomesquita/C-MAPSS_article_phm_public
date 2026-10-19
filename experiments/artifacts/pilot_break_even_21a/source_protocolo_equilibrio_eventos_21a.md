# P21.1 — custo de equilíbrio dos eventos de fim de vida, sem dependência de escala

Especificado em 19/10/2026 a pedido do autor. **Não executado.** Análise exploratória posterior ao congelamento e à confirmação: FD002/FD004 já são dados examinados. A execução exige emenda E09 em `congelamento_2026-10-18/emendas.md`, com o SHA-256 deste protocolo e dos scripts, registrada antes de rodar. Não altera o protocolo congelado, as políticas, o gerador de inspeção nem as saídas P17.1, P20.1 e P20.2.

## 1. Motivação

O cenário de 20 anos (P20.1/P20.2) reescala a taxa de restauração por ciclo para um horizonte fixo e depende de uma correspondência ciclo simulado → voo que nenhuma das duas convenções examinadas valida (ξ=1 implica uma visita a cada 127 voos na regra de idade; ξ≈34–41 usa motores de outra classe). Além disso, a despesa conta apenas visitas: eventos de fim de vida não têm custo próprio, o que torna a regra de ponto central a mais barata apesar de 10–25 eventos por posição.

P21.1 substitui a pergunta "quanto custa em 20 anos" por "a partir de que custo adicional por evento cada braço mais conservador se torna preferível", uma razão invariante a ξ e ao horizonte.

## 2. Premissa de renovação (autor, 19/10/2026)

Na simulação C-MAPSS todos os motores atingem o fim da trajetória. No paralelo operacional, toda remoção — preventiva ou após atingir o fim de vida — é seguida de overhaul ao custo médio de US$6 milhões, e o motor retorna ao ciclo zero (AGAN, vidas renovadas iid, como em P12–P20). Portanto:

- custo base por remoção $c_R$ = US$6 milhões, **igual para as duas causas**; esse é o caso β = 0;
- β ≥ 0 é o custo **adicional** de consequência por evento, em unidades de $c_R$ (remoção não programada, dano secundário, indisponibilidade, desligamento em voo); não é estimado nem adotado aqui;
- LLP: contador independente, igual entre braços; cancela-se nas diferenças e fica fora desta análise.

## 3. Grandezas

Para um braço π e um conjunto de motores de avaliação $i$, com vida utilizada esperada $\ell_i^\pi$ e probabilidade de evento $e_i^\pi$ = P(chegada sem decisão) + P(chegada exata) + P(programação tardia):

- taxa de restauração $\varpi^\pi = n / \sum_i \ell_i^\pi$ por ciclo simulado;
- taxa de eventos $\eta^\pi = \sum_i e_i^\pi / \sum_i \ell_i^\pi$ por ciclo simulado;
- custo por ciclo $c_R(\varpi^\pi + \beta\,\eta^\pi)$; por voo, dividir por ξ, que se cancela em toda comparação.

Para um par (A mais conservador, B), A é preferível sse $\varpi^A + \beta\eta^A < \varpi^B + \beta\eta^B$, ou seja, para β > β* com

$$\beta^* = \frac{\varpi^A - \varpi^B}{\eta^B - \eta^A}.$$

Casos: $\Delta\varpi \le 0$ e $\Delta\eta \le 0$ (com uma desigualdade estrita) → A domina; $\Delta\varpi > 0$ e $\Delta\eta = 0$ → B domina (A só custa); ambos > 0 sem eventos evitados → idem. As três componentes do evento são relatadas separadamente, além da soma.

## 4. Dados

- Principal: `artifacts/pilot_inspection_17b/expectations.csv.gz` (SHA-256 `f7ce6b0647deddf1cf2241cb3cf63e2d6fb17c4d7dc553a32891dcde917ecd60`), expectativas exatas por motor para PHM (`*_p`) e híbrido (`*_h`). Conferir o hash antes e depois.
- AGE127: $\ell_i = \min(127, T_i)$, evento se $T_i \le 127$ (nenhum observado), calculado a partir de `T` do mesmo arquivo.
- Secundário, apenas FD001/FD003 e só PHM: regras de limiar/espera selecionadas em P13.1 (`pilot_policy_selection_13a/decisions.csv`), como pontos adicionais da fronteira, rotulados fora do conjunto M38.
- Não se leem sensores, não se reajustam HI, conversores, margens ou políticas.

## 5. Braços e contrastes predeclarados

Braços: AGE127; HI_MARKER, ISO_LOWER98_M15, RF_SLOPE_LOWER98_M15, ISO_POINT_M15, RF_SLOPE_POINT_M15, cada um sozinho e com inspeção. Prazos d = 1 e 2; três repetições; quatro subconjuntos.

| ID | A (conservador) | B | Pergunta |
|---|---|---|---|
| C1 | ISO lower98 | ISO ponto | custo do conservadorismo da margem |
| C2 | RF lower98 | RF ponto | idem, outro conversor |
| C3 | ISO ponto + inspeção | ISO ponto | valor da inspeção sobre regra com eventos |
| C4 | RF ponto + inspeção | RF ponto | idem |
| C5 | ISO lower98 + inspeção | ISO lower98 | valor da inspeção sobre regra conservadora |
| C6 | HI marker | ISO lower98 | valor incremental da previsão de F; com Δη = 0, decide-se só por ϖ |
| C7 | ISO lower98 | AGE127 | ganho do PHM sobre a idade |
| C8 | ISO ponto + inspeção | ISO lower98 | inspeção como alternativa à margem |

Cenário principal de inspeção: S2_W60_g1, u = 0. Sensibilidades, todas relatadas: W ∈ {30, 80}, γ ∈ {0,26; 2}, pP = 0,02, S1 (entrada privilegiada), u ∈ {0,0005; …; 0,02; 1}. Efeito latente P17.2: `artifacts/pilot_inspection_latent_17c/expectations.csv.gz` (SHA-256 `3bfdf83cc0b797eeeb03a531af81e9f1cafedf1063e9cfc2a48c21a1ba21114c`), cenários L1 de janela e forma, como sensibilidade.

## 6. Incerteza

- *Bootstrap* não paramétrico sobre **motores**, pareado (os mesmos motores reamostrados em todos os braços), dentro de subconjunto × repetição × prazo; B = 4.000; semente 20261021.
- Não se agregam repetições como amostras independentes; relatam-se por repetição e a amplitude entre repetições.
- Como β* é uma razão com denominador que pode cruzar zero, o resultado principal é a **curva de preferência** P*(A mais barato | β) sobre a grade β ∈ {0; 0,1; 0,25; 0,5; 1; 2; 5; 10; 20; 50; 100}, além de β* pontual. Intervalos percentis de β* só são relatados quando o intervalo de 95% de Δη exclui zero; caso contrário, β* é declarado não limitado.
- Para cada subconjunto, o número de motores distintos com evento em B é relatado ao lado de β*: poucos eventos implicam razões instáveis.

## 7. Fronteira

Para cada subconjunto × repetição × prazo, tabular ϖ e η (por 10.000 ciclos simulados) de todos os braços, com intervalos de *bootstrap* de 95%, e identificar braços dominados nas estimativas pontuais (outro braço com ϖ e η não maiores e um estritamente menor). A figura é opcional. Não escolher vencedor; a fronteira mostra trocas, não ótimo.

## 8. Verificações antes de relatar

1. Recalcular ϖ do PHM e do híbrido e conferir com `summary.csv` de P17.1 (`rate_p_per_10000`, `rate_h_per_10000`) até 1e-9 relativo.
2. Conferir consistência com P20.2: 32.000·ϖ + visitas LLP ≈ visitas por posição da tabela literal, com tolerância declarada para efeitos de horizonte finito e início maduro (diferença relativa ≤ 1%); divergência maior é investigada, não ajustada.
3. Testes sintéticos com β* conhecido, casos de dominância, Δη = 0 e motores sem evento.
4. Verificador independente (implementação separada, sem importar o módulo principal) reconstrói taxas, β*, curvas de preferência em 200 réplicas *bootstrap* com a mesma semente e a classificação de dominância.
5. Falha impede relato até diagnóstico documentado; logs de falha preservados.

## 9. Interpretação predeclarada

- β* é um **limiar de decisão**, não um custo estimado. Um evento de fim de vida no C-MAPSS é esgotamento de margem operacional, não necessariamente falha catastrófica; o significado operacional de β depende da categoria de efeito de falha, ainda indeterminada (ver IP-180 em `sec:task-implications`).
- β* < 1: o braço conservador é preferível se um evento custar mais que um overhaul adicional. Valores altos indicam que o braço conservador só se justifica por critérios de segurança, não pela despesa de restauração.
- Δη = 0 com Δϖ > 0 (por exemplo, C5 em FD001–FD003): a inspeção não tem valor econômico nesse cenário, qualquer que seja β; não é evidência de inutilidade da inspeção em geral.
- Resultados condicionados ao gerador de inspeção, ao modelo de perda de monitoramento e às decisões arquivadas; não constituem risco populacional nem aprovação.
- O cenário de 20 anos passa a ilustração aritmética de exposição repetida (eventos acumulados por posição), fora do resultado principal; a mudança no manuscrito depende de aprovação do autor após a execução.

## 10. Artefatos previstos

Nota (E09): a figura da fronteira não é produzida porque matplotlib não está instalado no ambiente; `frontier.csv` contém os dados para composição posterior.

`experiments/break_even_21a.py`, `experiments/test_break_even_21a.py`, `experiments/verify_break_even_21a.py`; saídas em `experiments/artifacts/pilot_break_even_21a/`: `rates.csv`, `contrasts.csv`, `contrast_summary.csv`, `preference_curves.csv`, `frontier.csv`, `validation.json`, `metadata.json`, `manifest.json` e `conclusoes.md`.
