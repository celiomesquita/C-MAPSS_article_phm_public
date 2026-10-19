# Interpretação de P08 — resultado misto

## O que a comparação permite afirmar

Acrescentar inclinação, curvatura e variabilidade ao índice de saúde (HI) corrente produziu reduções pontuais do erro de previsão do F original com floresta aleatória (RF), mas os intervalos descritivos de 95% incluem zero nos contrastes principais. Com regressão linear penalizada (Ridge), a composição temporal não melhorou a previsão no marco. Portanto, os resultados não demonstram um ganho geral por acrescentar atributos nem justificam escolher automaticamente a representação mais completa.

Todos os valores abaixo correspondem à mesma primeira passagem do HI empírico congelado por 0,5, nos mesmos motores e ciclos. RMSE é a raiz do erro quadrático médio de previsão de F, em ciclos; diferença negativa favorece HI com trajetória.

| Cenário | Motores disponíveis | RF: HI corrente | RF: HI + trajetória | Diferença e intervalo descritivo de 95% |
|---|---:|---:|---:|---:|
| FD001, avaliação externa completa | 100/100 | 18,69 | 16,98 | −1,71 [−3,94;0,63] |
| FD003, avaliação externa completa | 100/100 | 14,85 | 14,05 | −0,80 [−1,79;0,20] |
| FD001, teste oficial truncado | 29/100 | 12,92 | 12,01 | −0,91 [−5,53;3,51] |
| FD003, teste oficial truncado | 22/100 | 16,27 | 15,14 | −1,13 [−4,69;1,56] |

Os 71/78 motores restantes nos testes truncados não tinham cruzamento observado. Não foram imputados ou descartados do denominador. Nenhuma passagem principal ocorreu antes da disponibilidade de atributos no ciclo 39 nesta avaliação. O marco não redefine F, P, remoção ou início das inspeções.

## Controle de capacidade e ablações

Os isotônicos reajustados nos mesmos ciclos de calibração tiveram RMSE 17,82 e 14,87 nos motores completos FD001/FD003. A RF com história teve diferenças −0,84 [−3,07;1,62] e −0,82 [−1,74;0,22] contra esses controles. Assim, a evidência não estabelece superioridade conclusiva frente ao conversor simples anterior. Ridge corrente→completo passou de 25,18 para 25,70 em FD001 e de 20,37 para 20,67 em FD003; não se deve atribuir a uma informação temporal um efeito independente da família preditiva.

As ablações não sustentam que todos os atributos sejam necessários. RF com HI e somente inclinação teve RMSE 16,67/14,00 nos motores completos FD001/FD003, próximos ou inferiores à composição completa. Retirar curvatura resultou em 16,67/13,89. Esses são resultados exploratórios já observados, não critérios novos de seleção ou autorização para substituir o vencedor interno por um modelo escolhido no teste. Os intervalos e todos os candidatos permanecem nos CSVs; nenhum método foi adotado definitivamente.

## Informação direta dos sensores

Com RF em FD003, acrescentar estatísticas aos sensores suavizados reduziu RMSE no marco de 16,44 para 14,40 nos 100 motores completos: diferença −2,04 [−3,63;−0,42]. Nos 22 motores oficiais com marco, passou de 15,69 para 11,21: −4,48 [−8,23;−1,98]. Nesse grupo oficial, sensores completos também ficaram abaixo de HI completo (15,14→11,21; diferença −3,92 [−6,30;−1,18]). É evidência descritiva específica do cenário e dos motores com marco; não superioridade em toda a frota ou confirmação independente após múltiplas comparações.

Em FD001, RF com sensores completos teve RMSE 18,90, contra 16,98 com HI completo nos motores completos, sem diferença conclusiva. A média móvel sozinha também não melhorou universalmente: no FD003 completo, RF com sensores correntes teve 15,27 contra 16,44 com médias. Ridge apresentou pioras com vários grupos de atributos. Portanto, não há evidência de que suavizar ou acrescentar estatísticas aumente sempre o poder prognóstico.

Os controles diretos usam os mesmos canais e parâmetros congelados, mas o HI também incorpora pesos supervisionados previamente em F. Uma vantagem dos sensores sugere possível perda de informação pela compressão; o contraste não isola esse mecanismo causal nem iguala todo o histórico de aprendizagem da representação.

## Estabilidade das contribuições e alcance temporal

A correlação mediana de Spearman entre ranks de importância dos sensores de Ridge e RF nos cinco folds foi 0,442 em FD001 e 0,095 em FD003. Entre folds da mesma família, medianas combinadas foram 0,092/0,321. No teste oficial, a concordância entre famílias foi 0,512/0,095. Esses resultados não sustentam uma importância de sensores estável e consensual, sobretudo em FD003. As correlações combinam partições dependentes e poucos grupos; não são testes confirmatórios. Os ranks são recalculados na interseção de sensores; uma correção documentada de pós-processamento alterou quatro das 104 correlações, sem mudar previsões, erros ou seleção.

No marco, o HI corrente varia pouco entre motores; sua pequena importância por permutação nesse grupo condicionado não demonstra irrelevância do HI ao longo da vida. Inclinação, variabilidade e curvatura podem ser correlacionadas. Variações negativas de erro por permutação foram mantidas e não convertidas em importância positiva. Permutações fora da distribuição, correlações e dependência das partições limitam fidelidade e causalidade; concordância não equivale a validação física.

Os ganhos no marco não se generalizaram automaticamente à última observação oficial. Com RF, HI corrente→história passou de 28,22 para 28,68 ciclos em FD001 e 24,80 para 25,04 em FD003, nos mesmos 97/99 motores com atributos disponíveis. Três motores FD001 e um FD003 terminaram antes do ciclo 39; não comparar esses resultados diretamente aos RMSE de P05/P06 nos 100 motores. Qualidade local perto do marco e qualidade no restante da vida são objetivos diferentes.

## Consequência para a pesquisa

A rodada justifica conservar a fórmula HI e o conversor isotônico como controles, juntamente com candidatos temporais parcimoniosos e sensores diretos, sem adotar a composição completa por conveniência. Antes de selecionar uma solução, é necessário definir o domínio temporal de interesse decisório e verificar robustez das diferenças e contribuições. Uma avaliação com novas partições deve reconstruir a aprendizagem do HI dentro de cada partição: reutilizar modelos HI que viram um novo motor de avaliação introduziria vazamento. Isso requer protocolo próprio e não foi executado nesta rodada.

A localização de P, a incerteza preditiva individual, os limites admissíveis de risco/antecedência e a referência futura de inspeção continuam pendentes. O bootstrap desta rodada quantifica incerteza descritiva das diferenças de desempenho, não fornece intervalos individuais de F. Não houve alteração da fórmula de HI, treinamento de novo detector de P, simulação de inspeções, congelamento principal ou edição do artigo.

Evidências: [protocolo anterior à execução](../../protocolo_trajetoria_hi_08.md), [relatório](relatorio.md), [contrastes](contrasts.csv), [seleção interna](selection.csv), [ranks](importance_ranks.csv), [concordância](rank_concordance.csv), [emenda dos ranks](rank_correction.json), [verificação](verification.json) e [figura](paired_effects.png).
