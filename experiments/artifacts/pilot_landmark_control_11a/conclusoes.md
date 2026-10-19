# P11.1 — o ganho do controle de condição e o incremento do conversor

17/10/2026. **O controle simples do primeiro HI≤0,5 reproduziu quase todo o ganho de vida observado em P11 frente à idade fixa. O conversor de F e a calibração acrescentaram pouco nas regras de referência examinadas.** Esse resultado não invalida o HI supervisionado nem demonstra que o prognóstico seja inútil em outros regimes.

## Evidência verificada

Mesmos parâmetros HI, disponibilidade, motores e prazos P11; sem treino novo. O controle usa só o evento causal de passagem do HI e programa retirada em t₀+d, com d=1/2. Os 100 motores completos de cada domínio tiveram decisão e retirada antes do endpoint em todas as três repetições. Não são 300 motores independentes. Nenhuma inspeção foi simulada.

| Indicador, amplitudes entre repetições e prazos d=1/2 | FD001 | FD003 |
|---|---|---|
| Vida média aproveitada pelo controle HI, ciclos simulados | 166,69–169,02 | 204,98–210,16 |
| Ganho adicional ISO/inferior98/reserva15, ciclos médios | 0,21–1,57 | 0,00–0,83 |
| Economia normalizada adicional ISO frente ao HI | 0,12–0,93% | 0,00–0,40% |
| Ganho adicional RF temporal/inferior98/reserva15, ciclos médios | 0,28–1,09 | 0,24–0,54 |
| Economia normalizada adicional RF temporal frente ao HI | 0,17–0,65% | 0,11–0,26% |
| Chegadas, ultrapassagens ou ausência de decisão: HI e essas regras | 0 | 0 |

O isotônico com reserva15/limite98 teve ganho zero e as mesmas 100 datas de retirada na terceira repetição FD003, em ambos os prazos. Nos demais contrastes de referência, os intervalos descritivos pareados do incremento médio foram positivos; a magnitude continua pequena, e significância não estabelece relevância operacional. Todos os resultados e intervalos estão no relatório, sem escolha da melhor semente.

Na decomposição da vida média frente ao controle de idade fixa P11, o controle HI já representava **95,93–100% do ganho** para o isotônico/inferior98/reserva15, considerando os dois domínios, prazos e repetições. O incremento do conversor era a parcela restante, **0–4,07%**. Para RF temporal na mesma configuração, o incremento ficou entre 0,39% e 2,86% do ganho de vida frente à idade. Essas são parcelas de vida, não parcelas aditivas de economia monetária. Os fatores de custo foram verificados multiplicativamente.

## O que a comparação permite concluir

O controle HI deve permanecer como referência decisória competitiva. A grande redução de custo normalizado de P11 frente à idade fixa não pode ser atribuída integralmente à previsão sequencial de F ou ao seu limite inferior. O HI já contém informação supervisionada pela vida remanescente; retirar o conversor da decisão não torna o procedimento não supervisionado ou livre de prognóstico aprendido.

A idade fixa foi conservadora e também apresentou eventos externos, logo o ganho frente a ela não é comparação de admissibilidade equivalente ou prova de vantagem perante programa preventivo real. Nas regras de âncora central, maior vida pode vir acompanhada de falhas não prevenidas; essas diferenças não justificam adoção económica. Uma regra que só pode actuar depois do marco já tem, por construção, vida aproveitada maior ou igual à do controle imediato: a utilidade precisa ser avaliada junto dos eventos, não só pela positividade do incremento.

O ensaio explora o marco 0,5 e reservas congeladas, com dados já examinados. Não determina limiar ótimo, melhor período de espera ou risco populacional ≤2%. Não se modificaram a fórmula HI, a disponibilidade ou a seleção de sensores para favorecer o conversor. Não se adoptou reserva12, nível95 ou política operacional definitiva.

## Consequência para o plano

Manter HI/isotônico e o controle simples na avaliação; qualificar a contribuição incremental do conversor como pequena neste regime. Antes de alegar um momento ótimo, especificar a seleção e validação da decisão sob o mesmo critério de risco, incluindo referências simples competitivas. Ajustar um limiar/espera ou escolher regra pelos mesmos motores avaliados não constituirá confirmação independente. Não acrescentar modelos mais complexos sem hipótese discriminante.

P12 continua condicionado à ponte entre ciclos simulados e de voo; ganho por companhia exige ainda frota elegível, disponibilidade, procura e margem incremental. Estas pequenas economias adicionais não foram convertidas em dólares ou projeção de 20 anos. O braço PHM + inspeção permanece posterior ao congelamento, com custo e duração incrementais de boroscopia zero. O artigo permanece M17.

## Rastreabilidade

Os **49 testes passaram** antes da execução. A verificação independente reconstruiu 2.400 controles completos/truncados, conferiu 312 resumos herdados de P11, 156 contrastes com intervalos e 144 decomposições. Todos os artefatos anteriores permaneceram íntegros; nenhuma emenda de execução ou verificação foi necessária.

[Protocolo](../../protocolo_controle_marco_11a.md), [relatório](relatorio.md), [verificação](verification.json), [contrastes](contrasts.csv), [decomposição](decomposition.csv) e [manifesto](manifest.json).
