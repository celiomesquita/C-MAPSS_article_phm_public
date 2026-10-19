# P13.1 — resultado misto: mais vida, transferência imperfeita do filtro de risco

17/10/2026. Perguntas RQ1/RQ2/RQ3/RQ7. [Protocolo anterior à execução](../../protocolo_selecao_decisoria_13a.md), [tabelas completas](relatorio.md), [contrastes](contrasts.csv) e [verificação](verification.json).

Mantida a fórmula do índice de saúde (HI), foram ajustados 240 modelos HI internos, com validação por motor, para selecionar limiar ou espera usando somente D40 de cada uma das 60 partições externas. U50/E10 não entraram na escolha. As 240 escolhas foram congeladas antes da avaliação externa. Quatro escolhas não tiveram candidato que passasse pelo filtro interno; foram mantidas apenas como diagnósticos, conforme o protocolo. Não se substituíram regras depois de observar E.

| Resultado externo, intervalo entre repetições e prazos | FD001 | FD003 |
|---|---|---|
| Vida média com limiar selecionado | 180,97–183,51 ciclos | 217,88–220,53 ciclos |
| Vida média com espera selecionada | 176,58–179,01 ciclos | 212,97–218,56 ciclos |
| Ganho do limiar frente ao marco HI≤0,5 | 13,08–15,49 ciclos | 8,29–12,90 ciclos |
| Ganho da espera frente ao marco HI≤0,5 | 8,50–10,00 ciclos | 6,90–9,00 ciclos |
| Chegadas ao endpoint com limiar | 0–2 por 100 motores | 0–2 por 100 motores |
| Chegadas ao endpoint com espera | 0–1 por 100 motores | 0–1 por 100 motores |

Cada repetição contém 100 motores, reutilizados entre repetições; não são 300 motores independentes. Chegada inclui remoção em T, após T ou ausência de decisão. Houve uma ultrapassagem estrita: espera, FD001, repetição1, prazo2. As demais chegadas foram exatas ou ausências. Os controles HI e ISO/inferior98/reserva15 conservaram zero chegadas observadas.

A seleção escolheu limiares 0,2–0,4 em FD001 e 0,3–0,5 em FD003; esperas de 5/10 e 2/5/10 ciclos, respectivamente. A frequência elevada da espera máxima de dez ciclos é um diagnóstico da grelha explorada, não autorização para expandi-la após E. Quatro seleções internas inviáveis em 240 impedem qualificar todo o procedimento como admissível apenas porque a frequência externa agregada ficou baixa.

As reduções aritméticas do custo normalizado frente ao marco foram 7,18–8,44%/3,80–5,92% para limiar e 4,81–5,66%/3,18–4,13% para espera, em FD001/FD003. Esses contrastes incluem configurações com eventos e escolhas internas inviáveis: não demonstram economia admissível nem ganho financeiro de companhia. O bootstrap pareado é condicional às escolhas/modelos e não quantifica a incerteza de reaprendizagem de toda a seleção.

**Conclusão científica.** Regras simples competitivas recuperam mais vida que a retirada imediata no marco; o conversor explícito de F não é a única via para esse ganho. Porém, zero eventos nos 40 motores internos não se transfere uniformemente, e a resolução amostral não demonstra risco populacional ≤2%. O resultado apoia continuar a validação da decisão e sua explicabilidade, sem declarar ótimo global, dispensar o prognóstico ou escolher retrospectivamente a repetição mais favorável.

**Rastreabilidade.** Os 59 testes passaram antes da execução. O verificador teve duas correções documentadas: desconsiderar o índice de linhas recriado pelo CSV ao comparar HI externo e reconhecer separadores Windows ao localizar a cópia original do próprio verificador para conferir seu hash. Versões e logs iniciais foram preservados; protocolo, runner, modelos, escolhas e decisões permaneceram inalterados. A verificação final reconstrói ajustes, ações, seleção, referências, resumos e intervalos. Não houve inspeção, projeção monetária, mudança do HI ou edição do artigo M17.

**Entrega ao plano executivo.** P13.1 concluída com resultado misto; P13 parcialmente concluída. Próxima etapa: especificar uma validação da estabilidade e fidelidade das explicações da decisão, mantendo os controles simples e tratando escolhas inviáveis/ausências explicitamente. Para uma alegação confirmatória de risco baixo, será necessário protocolo prospectivo e evidência independente com resolução amostral adequada. P12 continua dependente da ponte entre ciclos simulados e calendário; inspeções permanecem posteriores ao congelamento.
