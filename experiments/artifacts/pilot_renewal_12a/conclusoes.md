# P12.1 — renovação AGAN por exposição simulada

## Resultado e alcance

O simulador de renovação reproduziu a taxa analítica em todas as 96 combinações (domínio × repetição × regra) com erro relativo máximo de 1,7×10⁻⁴ (tolerância predefinida 1%). O custo normalizado por ciclo simulado e as diferenças entre regras confirmam P11/P11.1/P13.1. **Não há cenário calendário validado**: a ponte entre ciclos simulados e ciclos de voo não foi definida pelo autor. Os valores em USD abaixo são aritmética da grade k (ciclos de voo por ciclo simulado) e não previsão. Sem inspeção, sem receita, sem valor de companhia.

## Taxa de restauração por 10.000 ciclos simulados (intervalo entre as três repetições)

| Regra (prazo 1) | FD001 | FD003 | Eventos de endpoint nas 300 vidas* |
|---|---:|---:|---|
| Idade fixa (AGE) | 74,2–76,9 | 67,3–68,9 | 5 ausências em cada domínio |
| Marco HI (HI_MARKER) | 59,5–60,0 | 47,8–48,8 | 0 |
| ISO inferior 98%/reserva 15 | 59,3–59,7 | 47,7–48,6 | 0 |
| RF_SLOPE inferior 98%/reserva 15 | 59,3–59,9 | 47,8–48,7 | 0 |
| Limiar HI selecionado (P13.1) | 54,5–55,3 | 45,3–45,9 | 2 ausências / 3 ausências + 1 exata |
| Espera HI selecionada (P13.1) | 56,2–56,6 | 45,8–47,0 | 0 ausências + 1 exata / 1 ausência |
| ISO central (ponto) reserva 15 | 51,8–52,3 | 42,8–43,0 | 23 ausências + 11 exatas / 37 + 5 |

\* Soma das três repetições (300 vidas por domínio e regra); repetições reutilizam os mesmos 100 motores.

## Economia relativa

Redução da taxa de restauração frente à idade fixa (intervalo entre repetições do ponto e extremos dos bootstrap de motores por repetição):

- ISO inferior 98%/reserva 15: 20,0–22,9% (IC 16,8–26,1%) em FD001 e 29,0–30,3% (23,6–35,3%) em FD003.
- Limiar HI selecionado: 26,6–28,4% (FD001) e 32,6–33,3% (FD003). Espera: 24,3–26,3% e 31,8–32,5%.

Frente ao marco HI: ISO inferior 98% 0,3–0,9% (FD001) e 0–0,4% (FD003), consistente com P11.1; limiar selecionado 7,9–8,4% e 4,2–5,9%; espera 5,4–5,7% e 3,6–4,1%. A economia das regras selecionadas veio com ausências de decisão e chegadas exatas ao endpoint, que o marco HI e as regras inferiores 98% não tiveram nesta amostra. As regras centrais de ponto são as mais baratas e as piores em eventos. Menor custo não classifica admissibilidade. Zero eventos em 300 vidas reutilizadas não comprova risco ≤2%. As quatro escolhas internas inviáveis de P13.1 permanecem como diagnósticos.

## Horizonte parametrizado (H = 32.000/k ciclos simulados)

Restaurações por posição, ISO inferior 98%/reserva 15, prazo 1 (média das réplicas e das três repetições; desvio das réplicas entre parênteses):

| k | Horizonte | FD001: idade → ISO | FD003: idade → ISO |
|---|---:|---|---|
| 1 | 32.000 | 242,1 → 189,8 (2,8) | 217,7 → 153,4 (4,4) |
| 10 | 3.200 | 23,7 → 18,6 (0,9) | 21,3 → 14,9 (1,4) |
| 50 | 640 | 4,04 → 3,31 (0,51) | 4,00 → 2,63 (0,65) |
| 100 | 320 | 2,00 → 1,41 (0,49) | 2,00 → 1,06 (0,50) |
| 150 | 213 | 1,00 → 0,91 (0,29) | 1,00 → 0,66 (0,47) |

- Com k=1, a hipótese direta implica 150–240 restaurações por posição em 20 anos, ou USD 0,9–1,5 bilhão por posição a USD 6 milhões. Isso mostra que a hipótese 1:1 não é plausível como projeção e que a ponte de escala é pendência indispensável, não detalhe.
- A partir de k=50, o horizonte contém poucas vidas. A razão (restaurações simuladas/H)/(taxa analítica) cai a 0,62–0,92: efeito de borda por números inteiros, vida incompleta final e dispersão entre réplicas, não efeito de regra. As diferenças entre regras a k≥100 são pequenas frente ao desvio das réplicas, e a idade fixa tem desvio zero porque a vida é quase constante.
- Resultados por k não podem ser lidos como previsão de 20 anos para a companhia.

## Limitações

- Vidas renovadas por reposição de motores E são hipótese de renovação independente (iid) e não validam comportamento pós-restauração. O custo AGAN é fixo.
- Regras de P13.1 foram selecionadas em desenvolvimento, mas E já foi examinado em P10–P13.5. Esta rodada é exploratória.
- Sem receita, disponibilidade, spares, frota, margem incremental ou braço de inspeção.

## Verificação

Seis testes passaram antes da execução (`experiments/p12a_tests.log`). O verificador independente reconstruiu vidas e eventos das colunas brutas, refez as taxas analíticas (96), conferiu 168 estimativas pontuais de economia, repetiu por laços a renovação de 30 casos (mesmas sequências de motores, 2.000 réplicas) e checou as 96 validações. A primeira chamada falhou por erro de acesso a colunas do pandas (`row.repeat`, método da `Series`) antes de qualquer comparação; log preservado em `experiments/p12a_verification_initial.log`, acesso corrigido, mesma verificação. Manifestos anteriores íntegros. Sem emendas científicas.
