# Interpretação de P09 — prognóstico estável, incerteza ainda limitante

## Resultado principal

A referência empírica de índice de saúde (HI) foi mantida, com parâmetros reaprendidos nos motores de desenvolvimento de cada nova partição. As três repetições mostraram erros pontuais relativamente estáveis, mas a cobertura das trajetórias e a antecedência fornecida pelos limites inferiores variaram. Menor erro médio não assegurou melhor informação para programar uma remoção. O resultado é misto e não reabre a busca de outra fórmula HI.

Foram usados cinco folds por motor em cada repetição, com F40 para HI, C20 para conversores, U20 exclusivamente para calibração da incerteza e E20 para avaliação. Métodos e hiperparâmetros foram pré-fixados. O isotônico (ISO) é o controle; RF_HI é floresta aleatória com HI corrente; RF_SLOPE usa a mesma floresta com HI e inclinação recente. Não há nova seleção em U/E. Os dados já haviam informado escolhas anteriores, portanto não se trata de confirmação independente.

## Qualidade pontual no marco HI≤0,5

As amplitudes abaixo são mínimos e máximos entre três repetições, cada uma sobre os mesmos 100 motores completos. Não são intervalos de confiança nem resultados de 300 motores independentes. RMSE significa raiz do erro quadrático médio de previsão do F original, em ciclos.

| Subconjunto | ISO | RF_HI | RF_SLOPE |
|---|---:|---:|---:|
| FD001 | 16,40–16,48 | 16,54–17,39 | 15,04–15,95 |
| FD003 | 15,24–16,41 | 16,89–18,41 | 13,70–16,15 |

No FD001, a diferença RF_SLOPE−ISO teve intervalo descritivo incluindo zero nas três repetições. No FD003, isso ocorreu em duas; na terceira a diferença foi −2,05 ciclos, intervalo [−4,10;−0,14]. Frente à RF com HI corrente, o componente temporal reduziu o RMSE pontual nas três repetições FD003, com intervalos excluindo zero, mas esse resultado permanece exploratório. Não se escolheu a melhor semente ou um vencedor universal.

O marco esteve disponível nos 100 motores completos em cada repetição. Nos testes oficiais truncados, esteve disponível em 27/100 FD001 e 24/24/25 de 100 FD003; não se completaram trajetórias ou cruzamentos depois do truncamento. Os erros e coberturas oficiais são condicionais a esses grupos observados.

## Cobertura e largura das bandas

A calibração por motor utilizou o maior erro absoluto de toda a trajetória observada após o marco, com um escore por motor. O alvo nominal de 90% foi investigado, sem interpretá-lo como requisito de segurança aeronáutica. Cobertura bilateral exige que o endpoint verdadeiro esteja dentro da banda em todos os ciclos observados daquele motor.

| Subconjunto/método | Cobertura bilateral da trajetória, alvo 90% | Largura mediana da banda, ciclos |
|---|---:|---:|
| FD001 / ISO | 92–93% | 48,92–51,51 |
| FD001 / RF_SLOPE | 89–97% | 51,99–57,66 |
| FD003 / ISO | 82–94% | 39,57–47,14 |
| FD003 / RF_SLOPE | 86–90% | 48,72–50,64 |

No alvo de 95%, a cobertura bilateral foi 92–96%/93–97% para ISO em FD001/FD003 e 96–97%/89–95% para RF_SLOPE. As larguras medianas da RF temporal foram 55,49–61,91 e 55,72–66,05 ciclos, respectivamente. O número disponível em U foi 20 em todas as calibrações; todos os quantis resultaram finitos. Com essa dimensão, os ranks corrigidos de 90% e 95% são o 19º e o 20º escores, respectivamente, tornando importante a sensibilidade à amostra de calibração.

As coberturas abaixo do alvo em algumas divisões são resultados amostrais preservados. Não refutam isoladamente uma propriedade marginal teórica sob permutabilidade; tampouco demonstram uma garantia operacional para o estado específico de cada motor. O efeito das partições e da amostra pequena de calibração exige tratamento antes de escolher uma política.

## Prever F tarde e antecedência conservadora

Foi calibrado separadamente um limite inferior L(t), usando o maior erro positivo por motor. Sua cobertura exige L(t)≤T em toda a trajetória observada. A antecedência estimada L(t)−t é distinta da antecedência real até F e não constitui ordem de remoção.

No alvo unilateral de 90%, ISO teve cobertura de trajetória 94% nas três repetições FD001 e 90–92% em FD003, com antecedência estimada mediana no marco de 17–20 e 16,15–19 ciclos. RF_SLOPE teve 91–94% e 83–93%, com antecedência mediana 6,10–14,27 e 9,78–12,18 ciclos. O ganho pontual da floresta não se traduziu automaticamente em limite inferior mais estável ou mais informativo.

No nível nominal de 95%, a RF temporal em FD001 teve antecedência estimada mediana entre zero e 12,16 ciclos. Na terceira repetição, L coincidiu com o ciclo corrente em 65% dos motores no marco. Isso fornece proteção conservadora sem antecipação positiva nesses casos; não pode ser apresentado como previsão precisa ou planejamento já viável. A necessidade operacional de antecedência permanece sem limiar fundamentado.

## Por que a trajetória precisa de calibração própria

Usar apenas o erro no primeiro marco de U e depois repetir essa banda ao longo da vida não preservou a mesma cobertura. Para RF_SLOPE em FD003, no alvo de 90%, a calibração pontual teve cobertura no marco de 88–94%, mas cobertura da trajetória inteira de somente 60–82%. Calibrar pelo máximo temporal elevou a cobertura da trajetória para 86–90%, com bandas mais largas. São alvos estatísticos diferentes; cobertura de muitos ciclos ou de um ponto não substitui cobertura simultânea por motor.

Nos motores oficiais, cobrir todos os ciclos observados até o truncamento também não demonstra cobertura depois dele. O endpoint obtido da RUL oficial permite conferir erros, sem revelar os sensores futuros.

## Consequência para a pesquisa

O isotônico permanece uma referência relevante e parcimoniosa; a RF temporal é um comparador promissor para erro pontual, sem adoção automática. A próxima decisão deve ligar o tratamento do erro de prever F tarde à antecedência exigida para manutenção e examinar a estabilidade da calibração. É necessário distinguir uma taxa nominal experimental de uma tolerância operacional fundamentada. Não se deve transformar o limite L em regra de remoção antes dessa especificação.

O domínio prognóstico HI≤0,5 não foi identificado com P físico, e o HI não passou a representar confiabilidade. A fórmula adotada em M18, a restauração perfeita, os custos e o cenário de inspeção não foram modificados. Não houve inspeções, congelamento do protocolo principal ou edição do artigo M17.

## Evidência e verificação

Os 29 testes passaram antes da execução. A verificação reconstruiu 873.984 previsões, com diferença máxima 2,28×10⁻¹³, conferiu 5.400 escores, 360 registros de quantis, 9.048 registros de bandas disponíveis e 120 contrastes pareados. Manifestos anteriores permanecem íntegros.

[Protocolo](../../protocolo_incerteza_f_09.md), [relatório](relatorio.md), [métricas pontuais](point_summary.csv), [coberturas e larguras](band_summary.csv), [quantis](quantiles.csv), [contrastes](contrasts.csv), [verificação](verification.json) e [figura](uncertainty_tradeoff.png). A calibração de ordem estatística segue a fonte primária indicada no protocolo; a adaptação à trajetória por motor e suas limitações estão explicitadas.
