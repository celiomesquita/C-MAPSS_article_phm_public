# P13.5 — transferência decisória das indicações de HI de P13.4

## Resultado e alcance

Resultado misto, que **não satisfaz o critério predefinido de transferência favorável**. As indicações SEL acrescentaram vida aproveitada e reduziram o erro no marco, mas a estabilidade externa entre repetições piorou em FD001 e, em FD003, surgiram eventos de endpoint ausentes da cadeia M18. M18 continua sendo a referência de trabalho. Nenhuma alternativa foi adoptada, e nenhuma escolha foi feita em C, U ou E.

O critério do [protocolo](../../protocolo_cadeia_hi_13e.md) exigia, nos dois domínios, p95 da amplitude do marco entre repetições não maior e nenhum evento adicional de endpoint para ISO inferior 98%/reserva 15. Falhou em ambas as partes: o p95 subiu em FD001, e FD003 teve uma chegada exata (prazo 1), uma ultrapassagem estrita (prazo 2) e uma ausência de decisão.

## Estabilidade entre repetições (pergunta principal)

Amplitude do primeiro marco utilizável max(39, HI≤0,5) de cada motor E entre as três repetições; 100 motores por domínio.

| Domínio | Cadeia | Mediana | p95 | Máximo | Motores >10 ciclos | Indefinidos |
|---|---|---:|---:|---:|---:|---:|
| FD001 | M18 | 4,5 | 9,15 | 24 | 5 | 0 |
| FD001 | SEL | 4,0 | 12,05 | 27 | 13 | 0 |
| FD003 | M18 | 6,5 | 27,45 | 212 | 29 | 0 |
| FD003 | SEL | 8,0 | 21,60 | 212 | 40 | 1 |

Diferenças pareadas SEL−M18 da amplitude média: FD001 +0,31 [−0,25; 0,90]; FD003 −0,49 [−3,33; 1,61] nos 99 motores comuns. A redução do p95 em FD003 (−6,3 [−24,7; 5,6]) é incerta e convive com mais motores acima de 10 ciclos (29→40). Para a data de decisão ISO inferior 98% prazo 1, o p95 passou de 9,05 para 13,00 em FD001 (+3,95 [1,05; 6,20]) e de 27,40 para 21,60 em FD003.

A estabilização interna de P13.4 não se transferiu de modo uniforme aos motores externos. Houve melhoras pontuais grandes: no FD003 motor 71, a amplitude caiu de 185 para 82 ciclos (decisão na repetição 2 passou de 163 para 279, numa partição cujo máximo interno tinha piorado), motor 24 de 45 para 18, motor 96 de 27 para 4. Houve também pioras: FD001 motor 17 de 12 para 23, FD003 motor 37 de 16 para 29.

**Caso 55 (FD003).** A amplitude de 212 ciclos não mudou. Nas repetições 1 e 2, o motor 55 está em partições cuja indicação foi M18, incluindo a contingência inelegível FD003/repetição 2/dobra 2 (marco 239). Na repetição 3, NNLS_01 deslocou o marco de 396 para 432. Esse caso foi identificado com E em rodadas anteriores; sua descrição não valida nem invalida a alternativa. **Caso 83 (FD001):** 228/204/222 → 231/204/230, amplitude 24→27.

## Decisões de remoção

| Regra | Domínio | Eventos de endpoint M18 | Eventos de endpoint SEL | Δ vida média SEL−M18, ciclos |
|---|---|---|---|---|
| ISO inferior 98%, prazo 1 | FD001 | 0 em todas | 0 em todas | +1,62 a +1,82 |
| ISO inferior 98%, prazo 1 | FD003 | 0 em todas | rep. 2: 1 chegada exata; rep. 3: 1 ausência | +2,29 a +4,74 |
| ISO inferior 98%, prazo 2 | FD003 | 0 em todas | rep. 2: 1 ultrapassagem estrita; rep. 3: 1 ausência | +2,59 a +4,73 |
| Marco HI, prazo 1 | FD003 | 0 em todas | rep. 2: 1 chegada exata; rep. 3: 1 ausência | +2,25 a +4,74 |

Os intervalos bootstrap dos ganhos de vida excluem zero em todas as repetições, com 61–87 motores alterados por repetição. Os ganhos são descritivos e acompanham marcos mais tardios: a antecedência real mediana no marco caiu de 36–37 para 32–36 ciclos. Os três eventos adversos são do mesmo motor, FD003 motor 10, o de vida mais longa (481 ciclos), que já não cruzava HI=0,5 em calibrações de P10. Com coeficientes assinados, o HI cruzou apenas no ciclo 480 (SIGNED_1, repetição 2) ou não cruzou (SIGNED_01, repetição 3); M18 decidira nos ciclos 430–434. Em análise descritiva não predefinida, excluir esse motor reduz o ganho FD003 em até 0,43 ciclo médio na regra ISO e 0,53 no marco HI: o ganho não depende só do evento adverso, mas o evento continua a impedir a triagem.

A triagem experimental (decisão em todos os motores e ultrapassagem ≤2%) passou para M18 em todas as repetições e para SEL em FD003 só nas repetições 1 e 2; a repetição 3 falhou por ausência de decisão. As regras de âncora central mantiveram 3–15 ausências por 100 motores nas duas cadeias. Zero eventos em amostras de 100 motores não comprova risco populacional ≤2%.

## Prognóstico e incerteza

O RMSE no marco caiu com SEL em 11 dos 12 contrastes (ISO: FD001 −0,59 a −1,06; FD003 −1,62 a −6,05), com intervalos excluindo zero em nove; RF_SLOPE em FD001, repetição 3, piorou +1,02 [−0,60; 2,62]. A comparação não é no mesmo ciclo: o marco SEL ocorre mais tarde, e prever restos de vida menores tende a reduzir o erro absoluto. No FD003, repetição 1, a cobertura inferior ISO caiu de 0,99 para 0,95, e 8% dos motores tiveram antecedência conservadora colapsada no marco (0% em M18). A antecedência conservadora mediana ISO caiu de 13,98 para 9,37 ciclos na repetição 3. Todos os quantis foram finitos, com n=49–50.

## Caudas pré-especificadas

Nas 11 partições com máximo interno agravado em P13.4, o p95 da mudança da decisão ISO prazo 1 entre cadeias foi 10,05 ciclos em FD001 (máximo 14) e 9,75 em FD003 (máximo 116, motor 71). Nas demais, foi 5,00 (máximo 10) e 14,00 (máximo 46). O agravamento interno do máximo não previu o comportamento externo nesta amostra; a categoria é pequena (8 e 3 partições).

## Verificação e rastreabilidade

Antes de executar, 7 de 8 testes passaram. O teste de equivalência do reajuste do conversor exigia igualdade bit a bit e falhou por diferenças de até 8,5×10⁻¹⁴ ciclo na média paralela das árvores RF. A tolerância do teste passou a 10⁻⁹, a mesma do protocolo; log inicial preservado em `experiments/p13e_tests_initial.log`. Os 8 testes passaram antes da execução. Nenhuma regra, modelo ou critério mudou.

Durante a execução, as 60 cadeias M18 reproduziram previsões E e quantis arquivados de P10 (tolerância 10⁻⁹). O verificador independente reconstruiu HI e inclinação a partir dos sensores brutos com implementação própria (diferença máxima 1,33×10⁻¹⁰), repetiu as previsões dos modelos salvos (9,93×10⁻¹¹), refez os quantis a partir das trajetórias U (2,84×10⁻¹⁴) e as 12.000 decisões. Confirmou ainda 6.000 linhas M18 iguais a P11/P11.1/P11.2, cinco partições SEL idênticas a M18, 120 resumos e 2.000 amplitudes. A primeira chamada do verificador falhou depois de todas essas reconstruções, por não filtrar linhas truncadas no arquivo de controles P11.1. O filtro foi corrigido e a fonte original e o log inicial foram preservados (`source_verify_hi_chain_13e.py`, `verification_initial.log`). Somente arquivos train foram lidos. Manifestos anteriores permaneceram íntegros.

## Consequência para o plano

A estabilização em desenvolvimento não deve ser adoptada como substituta de M18 com base nesta evidência. O padrão sugere que coeficientes assinados podem atrasar ou eliminar o cruzamento em motores de vida longa, mas isso é observação descritiva de três eventos de um motor, não nova regra de escolha. Não reformular a grade nem selecionar retrospectivamente NNLS por esse resultado; E já foi examinado. Próximos passos possíveis, todos dependentes de decisão do autor: aceitar M18 como representação de trabalho para encerrar P13 sem nova alternativa; ou especificar evidência independente (novos dados ou simulação com estados físicos) antes de qualquer outra comparação de HI. Sem inspeção, redução de reserva, projeção monetária ou alteração do artigo nesta rodada.

![Amplitude do marco e mudança da vida aproveitada](chain_comparison.png)
