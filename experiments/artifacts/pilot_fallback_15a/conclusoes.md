# P15.1 — política candidata de reserva: PHM quando houver decisão e idade quando não houver

## Resultado e alcance

Exploratório, sem inspeção, sobre as regras congeladas de P13.1 e motores E já examinados. A política é candidata: não é final, não concede crédito de manutenção e não valida segurança. A regra de idade atua se o PHM ainda não decidiu quando a idade de reserva é atingida (decisão em A_q − d, retirada em A_q; empate prevalece o PHM).

**Resultado principal: com a idade congelada do projeto (A_0 = mínimo dos endpoints de desenvolvimento − 1), a política reduz-se, na prática, à própria regra de idade.** A regra de idade atuou em 82–97% dos motores; a vida média aproveitada caiu de 168 para 131 ciclos (FD001, ISO inferior 98%/reserva 15, prazo 1) e de 208 para 145 (FD003), e a economia de restauração frente ao controle de idade foi −1,0% e −1,2%, ou seja, nula. Frente ao marco HI, a perda foi de 28% e 43%. O PHM só decidiu primeiro nos motores em que sua decisão precedeu a idade conservadora.

## Efeito da idade de reserva (prazo 1; média das três repetições; vida em ciclos simulados)

| Regra | q | Idade atua (FD001 / FD003) | Vida média FD001 | Vida média FD003 | Economia vs idade FD001 / FD003 | Economia vs marco HI FD001 / FD003 |
|---|---:|---|---:|---:|---|---|
| ISO inferior 98%/reserva 15 (original) | — | 0 | 168,2 | 208,2 | +21,5% / +29,6% | +0,6% / +0,3% |
| + idade | 0 | 86% / 83% | 130,6 | 144,9 | −1,0% / −1,2% | −28,1% / −43,3% |
| + idade | 0,05 | 75% / 75% | 141,6 | 154,2 | +6,8% / +4,9% | −18,2% / −34,7% |
| + idade | 0,10 | 66% / 67% | 146,9 | 160,2 | +10,1% / +8,4% | −13,9% / −29,7% |
| + idade | 0,25 | 37% / 48% | 156,8 | 171,2 | +15,8% / +14,3% | −6,7% / −21,3% |
| + idade | 0,50 | 18% / 33% | 163,1 | 183,1 | +19,1% / +19,9% | −2,5% / −13,4% |

O mesmo padrão vale para o marco HI e para a espera e o limiar selecionados de P13.1. A idade de reserva em quantis mais altos devolve vida, mas aproxima a regra híbrida da regra PHM original sem nunca recuperar o ganho de vida do PHM. Nenhum valor de q foi selecionado ou adotado; todos estão na grade predeclarada e foram relatados.

## O que a reserva resolve e o que não resolve

- **Regras de limite inferior 98% e marco HI**: não têm ausências nem chegadas ao endpoint (0 eventos em 300 vidas, em todos os q). A reserva apenas custa vida; não há evento a evitar. Passam nas telas estrita e prudente em todas as repetições, com ou sem idade.
- **Regras centrais de ponto (as com ausências de decisão e chegadas exatas)**: a reserva reduz os eventos, mas não os elimina e eles crescem com q, porque a regra de idade também não age em motores com T ≤ A_q − d. Soma das três repetições (300 vidas, prazo 1): ISO ponto FD001 originais 23 ausências + 11 exatas; com q=0: 1 + 1; q=0,05: 6 + 2; q=0,10: 7 + 2; q=0,25: 11 + 5; q=0,50: 15 + 6. FD003 originais 37 + 5; q=0: 4 + 0; q=0,10: 10 + 1; q=0,50: 25 + 5. Não houve ultrapassagem estrita. O controle de idade sozinho teve 5 ausências em 300 vidas em cada domínio.
- **Regras selecionadas de P13.1**: os poucos eventos (2–3 ausências, 0–1 exata) permanecem em quase todos os q.
- **Interpretação**: o compromisso é vida contra eventos. Eliminar os eventos da regra de ponto exige q=0, que devolve a regra de idade.

## Cenário central de 20 anos (P12.2: L_ref=8.425, 1.600 voos/ano, LLP 20.000 EFC, frota madura, prazo 1; visitas por posição)

| Regra | original | q=0 | 0,05 | 0,10 | 0,25 | 0,50 |
|---|---:|---:|---:|---:|---:|---:|
| ISO inferior 98% FD001 | 5,51 | 6,67 | 6,40 | 6,27 | 5,87 | 5,64 |
| ISO inferior 98% FD003 | 5,43 | 7,38 | 6,78 | 6,61 | 6,36 | 5,99 |

A idade fixa de P12.2 tem 6,64 (FD001) e 7,25 (FD003). Os números dependem integralmente de k, utilização e LLP e não são previsão de companhia.

## Limitações

- Um "sem decisão" por **indisponibilidade do monitoramento**, que é o caso descrito no IP 180 e na tese de Miranda, não ocorre em C-MAPSS e não foi simulado. Esta rodada testa a versão mais dura: a idade atua quando o PHM ainda não decidiu quando a idade é atingida, o que mistura "PHM tardio" e "PHM indisponível". Um desenho para o caso de indisponibilidade exigiria um modelo de perda de dados, ainda não especificado.
- A idade conservadora de P11 é do próprio projeto, não uma tarefa MRBR ou intervalo de fabricante. A grade de q usa quantis dos motores de desenvolvimento e não é calibração para segurança.
- A tese de Miranda observa que, se o intervalo tradicional já tiver passado quando o PHM falha, exige-se análise de engenharia; aqui isso é simplificado para retirada na idade.
- Repetições reutilizam os mesmos 100 motores E; zero eventos em 300 vidas não demonstra risco ≤2%. Sem inspeção, sem receita.

## Verificação

Oito testes passaram antes da execução (`experiments/p15a_tests.log`). O verificador independente reconstruiu 42.000 linhas híbridas por laços a partir das colunas brutas (`decision`, `endpoint`, `has_decision`), refez os 300 valores de A_q a partir de `splits.json` e dos arquivos train com interpolação própria, as 420 linhas de resumo e 200 economias amostradas, e confirmou os manifestos anteriores. Sem emendas.
