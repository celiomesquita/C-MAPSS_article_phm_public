# P21.1 — custo de equilíbrio dos eventos de fim de vida: conclusões

Execução de 19/10/2026 (emenda E09), exploratória e posterior à confirmação; FD002/FD004 já examinados. Só decisões e expectativas arquivadas (P17.1, P17.2, P13.1); nenhum sensor lido, nenhum modelo reajustado. Cada remoção custa o overhaul-base $c_R$ (US$6 milhões, retorno ao ciclo zero); $\beta$ é o custo **adicional** por evento de fim de vida, em unidades de $c_R$. $\beta^*$ é um limiar de decisão, não um custo estimado; um evento do C-MAPSS é esgotamento de margem, não necessariamente falha catastrófica.

Convenções: taxas por 10.000 ciclos simulados; $\Delta\varpi=\varpi_A-\varpi_B$ (restaurações), $\Delta\eta=\eta_B-\eta_A$ (eventos evitados por A). Valores abaixo: cenário S2_W60_g1, $u=0$, **amplitude entre as três repetições** (que reutilizam os motores; não são amostras independentes). "Limitado" significa que o intervalo de 95% de $\Delta\eta$ (bootstrap sobre motores) exclui zero em todas as três repetições.

## Validação

- P17.1: 1.920 linhas reproduzidas, diferença relativa máxima 1,3e-15 (híbrido) e 1,1e-15 (PHM).
- P20.2: 264 combinações braço/célula; $32\,000\,\varpi$ difere das visitas totais em no máximo 0,74% e das visitas de degradação em 0,55% (tolerância predeclarada 1%); a diferença reflete LLP e horizonte finito.
- PHM independente do cenário de inspeção (diferença máxima 0). 108 contrastes por célula e prazo, 24 células/prazos, 2.592 contrastes, 28.512 pontos de curva de preferência.

## Resultados (prazo 1; prazo 2 em `contrast_summary.csv`, qualitativamente igual)

| Contraste | FD001 | FD002 | FD003 | FD004 |
|---|---|---|---|---|
| C1 margem 98% vs ponto (ISO): $\beta^*$ | 1,03–1,92 | 1,51–2,20 | 0,76–0,97 | 0,28–0,53 |
| C2 idem, RF-slope | 1,50–2,18 | 2,15–2,32 | 1,25–1,72 | 0,42–0,81 |
| C3 inspeção sobre ISO ponto | 0,94–1,72 | 1,51–1,95 | 0,67–0,96 | 0,51–1,27 |
| C4 inspeção sobre RF ponto | 1,31–1,95 | 2,10–2,23 | 1,16–1,72 | 0,90–1,72 |
| C5 inspeção sobre ISO limite inferior | dominado | dominado | dominado | 5,8–11,8, não limitado |
| C6 marco HI vs ISO limite inferior | dominado ou empate | dominado ou empate | dominado ou empate | empate |
| C7 ISO limite inferior vs idade 127 | domina | domina | domina | domina ou preferido se $\beta<59$–$117$ |
| C8 ISO ponto + inspeção vs ISO limite inferior | preferido se $\beta<$ 2–164 | preferido se $\beta<$ 1,5–595 | $<$ 69–1432 ou dominado | 5,3–10,0, não limitado |

Em C1–C4 todas as repetições são limitadas e as curvas de preferência (bootstrap) tornam-se ≥94% a favor de A em $\beta=5$ e ≈100% em $\beta=20$, em todos os subconjuntos.

## Leitura

1. **Com $\beta=0$ (premissa do autor: toda remoção custa um overhaul), as regras de ponto central são as mais baratas** (menos restaurações), apesar de 8–43 motores com evento por repetição (regras de ponto); margem e inspeção só se justificam se um evento custar, além do overhaul, entre cerca de 0,3 e 2,3 $c_R$ (C1–C4). Em unidades monetárias de US$6 milhões, isso equivale a custo adicional por evento da ordem de US$2 a US$14 milhões, condicional ao cenário de inspeção; limiares abaixo de 1 em FD003–FD004 indicam que a margem se paga mesmo com consequência modesta.
2. **A inspeção sobre a regra conservadora (C5) não tem valor econômico em FD001–FD003**: acrescenta 1,5–2,0 restaurações por 10.000 ciclos e evita zero eventos (nenhum motor com evento na regra sem inspeção). Em FD004, evita 0–0,55 eventos por 10.000 ciclos a $\beta^*$ de 5,8–11,8, sem limite estatístico (intervalo de $\Delta\eta$ inclui zero). Não é evidência de inutilidade geral da inspeção.
3. **O marco HI nunca supera a regra ISO conservadora** (C6): é dominado em FD001 e em parte das repetições de FD002/FD003, e empata em FD004. A diferença é pequena (0–0,4 restaurações por 10.000 ciclos, até ≈0,7% da taxa); o ganho incremental da previsão de F é de pequena magnitude, consistente com P11.1 e P20.
4. **ISO limite inferior domina a idade 127 em FD001–FD003** (menos restaurações, zero eventos); em FD004 o conservador tem 2 motores com evento e a idade só é preferível para $\beta$ acima de 59–117, sem limite estatístico.
5. **Inspeção como alternativa à margem (C8) é frágil**: ISO ponto + inspeção faz em média 0,2–1,2 restaurações a menos por 10.000 ciclos que o PHM conservador em FD001–FD003, mas mantém eventos residuais; o limiar varia de 1,5 a 1.432 e depende fortemente de $W$, $\gamma$ e $p_P$ (em vários cenários o PHM conservador domina). Não selecionar vencedora.
6. A sensibilidade a $W$ é a mais forte: em C3/FD001, $\beta^*$ passa de 0,23–0,38 (W=30) a 0,94–1,72 (W=60) e 1,52–2,83 (W=80); entradas S1 (privilegiada) e S2 (observável) diferem pouco em W=60.
7. Fronteira (cenário principal, $u=0$): 61–69% dos braços são dominados em FD001–FD003 e 21% em FD004, por prazo; as regras selecionadas de P13.1 (FD001/FD003) preservam mais vida que o marco mas têm eventos.

## Limites

- Condicional ao gerador de inspeção (ambiente com RUL verdadeiro), sem calibração, e ao modelo de perda de monitoramento ($u$ em grade; $u=0$ aqui). Motores distintos por subconjunto: 100/180/100/169; repetições reutilizam motores.
- Poucos motores com evento (FD001 ≤15, FD002 ≤13, FD003 ≤17 sob regra de ponto; 2 sob regra conservadora em FD004): razões instáveis quando $\Delta\eta$ é pequeno; o campo `beta0_bounded` marca onde há suporte estatístico.
- Não é risco populacional, nem otimização econômica, nem aprovação; custos de indisponibilidade, receita e consequência de falha não foram modelados.
- O cenário de 20 anos fica reduzido a ilustração aritmética de exposição repetida; nenhuma alteração do artigo foi feita nesta rodada.

Artefatos: `rates.csv` (3.288 braços), `contrasts.csv` (2.592), `contrast_summary.csv` (864), `preference_curves.csv` (28.512), `frontier.csv` (288), `validation.json`, `metadata.json`, `manifest.json`, cópias `source_*`. Protocolo `experiments/protocolo_equilibrio_eventos_21a.md`; log `experiments/p21a_execution.log`; verificação `experiments/verify_p21a.log`.
