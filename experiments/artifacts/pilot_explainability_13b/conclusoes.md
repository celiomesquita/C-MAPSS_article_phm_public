# P13.2 — mecanismo fiel, estabilidade limitada e suporte insuficiente

17/10/2026. Resultado misto. [Protocolo](../../protocolo_explicabilidade_13b.md), [convenções anteriores à execução](../../protocolo_explicabilidade_13b_implementacao.md), [relatório e66 fichas](relatorio.md), [verificação das trajetórias](verification.json) e [verificação estatística](summary_verification.json). Modelos, quantis e políticas permaneceram congelados; não houve inspeção, nova seleção ou mudança do artigo M17.

## O que foi demonstrado

A cadeia computacional é auditável: reproduzidas9.600 decisões basais, contribuição assinada dos sensores ao índice de saúde (HI), efeito do clipping, alocação radial, inclinação causal e previsões da regressão isotônica (ISO) e da floresta aleatória (RF). O verificador independente usou os preditores públicos e reconstrução própria, inclusive dos replays locais. Nenhuma violação do sentido esperado da resposta do HI foi encontrada; respostas nulas/saturadas permanecem identificadas. Isso demonstra fidelidade ao modelo aprendido, não reconstrução do mecanismo físico ou utilidade humana validada.

Foram avaliadas1.093.760 ações globais e o mesmo número de ações locais, em60 partições. Essas ações são cenários repetidos sobre os mesmos motores, não milhões de unidades independentes. Parâmetros auxiliares da perturbação usaram somente os25 motores F de cada partição; não houve ajuste em C/U/E.

## Por que as regras conservadoras atuam perto do marco

No prazo de um ciclo, o ISO/inferior98/reserva15 decidiu no primeiro marco utilizável em55–75% dos motores FD001 e72–100% FD003, entre repetições. RF na mesma regra:84–88%/86–91%. Em **todas essas decisões conservadoras**, a previsão central ainda não satisfazia o gatilho de16 ciclos; a correção pelo quantil foi necessária para satisfazê-lo naquele instante.

Na ISO, o limite inferior permaneceu positivo nas decisões. Na RF ele já estava em zero em26–49% dos motores FD001 e39–66% FD003. Portanto, o mecanismo não é simplesmente “limite zero em todos”: a combinação previsão−quantil, reserva e disponibilidade do marco explica o acionamento antecipado. A observação não identifica qual alteração manteria o risco nem autoriza reduzir reserva/calibração.

P11.1 mostrou pouco incremento do conversor nessa configuração conservadora. P11.2 localizou a distância ao oráculo após o marco. P13.2 agora mostra como a transformação da previsão em limite/gatilho restringe a expressão dessa informação nas datas de remoção. Isso não equivale a dizer que o prognóstico é inútil em outras regras.

## Estabilidade de sensores, previsões e datas

| Diagnóstico | FD001 | FD003 |
|---|---|---|
| Spearman mediano do ranking de contribuição ao HI entre dobras | 0,728 | 0,560 |
| Menor Spearman nessa comparação | 0,453 | 0,019 |
| Sensores compartilhados nos cinco primeiros, mediana | 3/5 | 3/5 |
| Média absoluta de mudança da remoção ISO/inferior98/reserva15, prazo1, canais, amplitude1 | 2,17–2,19 ciclos | 1,95–2,17 ciclos |
| Fração média de deslocamentos>2 nesse contraste | 34,87–35,07% | 21,41–27,61% |

As frações são médias por motor sobre direções/sinais, separadas por repetição; não são taxas populacionais de falha. Os replays preservam ausência de decisão e distinguem mudança de presença de distância entre datas finitas. O controle por idade permaneceu invariante, como deveria.

As previsões RF foram mais sensíveis que ISO nos contrastes globais pareados, embora as datas das regras conservadoras tenham sensibilidade próxima. Isso é compatível com decisões que ocultam parte da variação preditiva devido ao gatilho e ao acesso comum. Não é superioridade preditiva ou operacional da ISO: a análise mede resposta às intervenções estatísticas especificadas, não erro em novos motores.

**Caso extremo preservado — FD003, motor55.** O marco ocorreu em451/239/396 nas três repetições; a regra ISO conservadora decidiu nesses mesmos ciclos. Na espera selecionada, as decisões foram461/244/406: diferença máxima217 ciclos, dos quais212 já estavam na diferença dos marcos entre as duas primeiras repetições e cinco na espera selecionada. A variabilidade principal desse caso vem da representação aprendida e do evento, não de um novo prazo logístico. Isso não identifica P físico ou prova detecção tardia. [Ficha completa e respostas às perturbações](case_FD003_u55.md).

ISO e RF compartilham HI; concordância dos rankings derivados não é validação independente de importância física. O resultado também não sustenta uma hierarquia universal e estável dos sensores, sobretudo em FD003.

## Limitação de suporte empírico

O envelope foi estimado nos incrementos iniciais F25. A própria trajetória original teve, em média descritiva,15,97% dos incrementos fora dele em FD001 e13,71% em FD003. Nenhum prefixo completo até a decisão satisfez o critério forte de suporte, nem no replay global nem no local. As estatísticas de datas condicionadas a esse suporte são, portanto, indefinidas, não zero.

Isso impede interpretar os resultados como robustez física validada. A saída do envelope pode refletir degradação e limitações da referência inicial; não é, por si só, defeito do sensor, falha do modelo ou prova de perturbação fisicamente impossível. Não ampliamos o envelope depois de observar E para obter aparência de cobertura. Resultados por instante e seus denominadores permanecem publicados.

## Consequência para o plano

P13.2 conclui a rodada exploratória de explicabilidade com mecanismo fiel, rankings moderadamente/fracamente estáveis e decisões sensíveis em casos relevantes. O protocolo principal ainda não está pronto para congelamento. A próxima decisão deve tratar a instabilidade da aprendizagem/marco, começando pelo caso55 e pelos demais extremos, antes de alegar estabilidade ou reduzir reservas. Preservar a fórmula M18 como referência; qualquer novo ajuste/regularização ou análise de influência exigirá especificação prévia e validação por motor, sem usar U/E para escolher e comprovar.

O outro limite é externo: o suporte estatístico inicial não valida a plausibilidade física das perturbações, e a amostra/reutilização não certifica risco populacional≤2%. Não há autorização científica decorrente destes resultados para iniciar inspeções, monetizar ganhos ou declarar ótimo operacional. Hipóteses de inspeção/P e ponte econômica continuam pendentes.

## Rastreabilidade

77 testes passaram antes da execução inicial; um `NameError` de registro das variantes interrompeu a fase de perturbações antes do primeiro resultado dessa etapa. Versões/log preservados; corrigida apenas a definição de V e acrescentado teste de registro/suporte temporal.78 testes passaram antes da retomada, sem refazer a auditoria basal ou alterar modelos. Mais quatro testes de análise passaram, total82 antes da análise estatística. A ampliação prévia do verificador acrescentou checagens de prefixos e respostas locais, com versão intermediária arquivada. `amendments.json` preserva a linhagem dos insumos originais; os arquivos anteriores permanecem íntegros.

66 motores selecionados pelos critérios pré-fixados de casos adversos/extremos/mediano foram apresentados nas três repetições:3.168 linhas motor/política/repetição e respectivas respostas globais/locais. [Inventário](case_inventory.csv), [gatilhos](trigger_explanation.csv), [estatísticas por motor](action_engines.csv), [rankings](rank_comparisons.csv), [contrastes pareados](action_contrasts.csv) e [manifesto](manifest.json).
