# P13.2 — explicabilidade, fidelidade e estabilidade da decisão

**Data:** 17/10/2026. **Estado:** protocolo especificado, antes das novas análises; execução não iniciada. Vinculado a P13/M09 e às perguntas RQ1/RQ2/RQ6/RQ7 do [plano executivo](../docs/gestao/plano_executivo_de_melhorias.md). O aceite do autor sucede a proposta de primeiro fixar este protocolo. Não constitui congelamento do protocolo principal.

## 1. Pergunta e contrato científico

**Dependência atendida antes da execução:** [P11.2](artifacts/pilot_loss_decomposition_11b/conclusoes.md) concluída em17/10/2026. Para retirada T−1, perda por acesso ao sinal zero e descarte adicional localizado na etapa posterior. Orientar as fichas para HI→previsão/incerteza→gatilho, sem interpretar toda a distância ao oráculo como erro preditivo recuperável. O desenho de perturbações permanece preservado; essa orientação foi fixada após P11.2 e antes dos resultados P13.2.

Em que medida conseguimos explicar, reconstruir e avaliar a estabilidade da cadeia sensor → índice de saúde (HI) → previsão do endpoint F → tratamento da incerteza → decisão → remoção? Para regras de condição, a cadeia não exige um conversor explícito para F.

P13.1 mostrou ganho de vida com limiar/espera selecionados, mas quatro escolhas internas inviáveis e chegadas externas ao endpoint. P11.1 mostrou pequeno incremento do conversor explícito frente ao marco HI≤0,5. São evidências já conhecidas; P13.2 é uma análise exploratória motivada por elas, sem alegação confirmatória independente.

Hipóteses concorrentes: (a) a explicação reproduz o mecanismo aprendido e suas mudanças; (b) os rankings parecem estáveis por dominância de sensores correlacionados, mas não explicam mudanças da previsão/decisão; (c) pequenas mudanças compatíveis com a variabilidade dos sensores alteram o evento ou a data de remoção; (d) decisões estáveis escondem previsões/atribuições instáveis devido a saturação, patamares do conversor ou memória do primeiro evento. Resultados nulos e adversos serão preservados.

**Destinatário da explicação:** pesquisador/engenheiro de manutenção que precisa auditar condição de acionamento, antecedência e informação responsável. Não será avaliada compreensão por inspetores ou utilidade humana sem estudo específico. IP-180 e ARP7122 permanecem âncoras para a ficha da tarefa e os limites da evidência, sem afirmar conformidade ou crédito de manutenção.

## 2. Dados, modelos e políticas congelados

- FD001 principal; FD003 robustez. Reutilizar as 60 partições externas de P10, com três repetições e dez dobras por domínio: ajuste HI em F25, conversor em C15, calibração de incerteza em U50 e avaliação em E10.
- Modelos P10, calibração P10 e escolhas P13.1 permanecem congelados. Reutilizar os mesmos 100 motores por domínio/repetição; não contar 300 motores independentes. Identificadores entre FD001/FD003 não formam pares físicos.
- Avaliar as 16 políticas externas de P13.1: limiar selecionado, espera selecionada, marco HI≤0,5, idade fixa, regressão isotônica (ISO) e floresta aleatória com HI/inclinação (RF_SLOPE), estas duas com âncora central ou limite inferior nominal98 e reserva15, sempre com prazo d=1/2 ciclos. A idade é controle de ausência de dependência sensorial.
- Ler sensores somente de `train_FD001.txt`/`train_FD003.txt`. O endpoint real T serve apenas para diagnóstico retrospectivo e encerramento da observação; não entra na explicação disponível em operação. Não usar testes oficiais truncados nesta rodada.
- A estimação auxiliar de variabilidade/associação dos sensores usa somente F25 de cada partição; C/U/E não calibram perturbações. Isso não reaprende HI, preditores, quantis ou políticas. U continua reservado à calibração preditiva original.

Entradas mínimas: modelos, partições e previsões completas de P10; quantis e decisões P11; controles P11.1; escolhas/decisões/verificação P13.1; dados sensoriais originais. Registrar hashes antes da execução e conferir integridade ao final; resultados anteriores não serão sobrescritos.

## 3. Explicação matemática do HI

Manter a média móvel causal de 15 ciclos, referência individual no ciclo20, canais, orientações d_j, escalas s_j e pesos não negativos β_j do modelo congelado. Para t≥20:

\[
z_{ij}(t)=d_j\frac{\overline{x}_{ij,15}(t)-\overline{x}_{ij,15}(20)}{s_j},\quad
c_{ij}(t)=\beta_jz_{ij}(t),\quad S_i(t)=\sum_jc_{ij}(t),\quad
H_i(t)=1-\operatorname{clip}(S_i(t),0,1).
\]

Guardar contribuições **assinadas** c_j, soma S e região de saturação. c_j negativo compensa contribuição positiva; não eliminar sinais nem renormalizar só os valores positivos. Reconstruir H com erro absoluto≤10⁻⁹ em todos os ciclos disponíveis. Pesos β são parâmetros globais numa escala particular, não importância local nem importância da decisão.

Se for necessário atribuir a queda limitada 1−H aos sensores, usar explicitamente a convenção de caminho radial a partir de z=0:

\[
a_j=\begin{cases}c_j\,\operatorname{clip}(S,0,1)/S,&S>0,\\0,&S\leq0.\end{cases}
\qquad\sum_ja_j=1-H.
\]

Essa alocação é explicação algébrica relativa ao estado de referência, sem identificação causal física. Em S≤0 ela pode ocultar cancelamentos: por isso c_j continua obrigatório. Em S≥1, atribuição acumulada e sensibilidade local diferem: o HI pode não variar apesar de c_j elevado. Registrar também sensibilidade direcional por perturbação, sem substituir c_j por ela.

## 4. Explicação da previsão e da regra

Para cada método, registrar HI, inclinação causal de 20 valores de HI, previsão de vida remanescente \(\widehat\ell(t)\), endpoint previsto \(\widehat F=t+\widehat\ell\), quantil tardio q da partição e \(L=t+\max(0,\widehat\ell-q)\) quando aplicável. A inclinação deriva da trajetória HI; não é uma variável independente que possa ser permutada livremente.

Na ISO, arquivar nós/patamares do mapa monotônico e reconstruir a previsão. Na RF_SLOPE, conferir a média das árvores e obter diferenças de previsão por perturbações das trajetórias, recalculando simultaneamente HI e inclinação. Uma diferença finita do preditor não será apresentada como decomposição aditiva completa nem como efeito físico causal. Não acrescentar um explicador substituto ou escolher a posteriori o que produza os rankings mais convenientes.

Reproduzir exatamente a regra original, inclusive tolerância numérica de P11, disponibilidade≥39, domínio após primeiro HI≤0,5, memória de passagem anterior ao aquecimento, saturação do limite inferior em zero e observação apenas antes de T. Para âncora central/inferior, auditar a desigualdade \(\widehat\ell\leq m+d\) ou \(\max(0,\widehat\ell-q)\leq m+d\), respectivamente, com m=15 e a convenção numérica arquivada. Não reinterpretar m como prazo d nem quantil de erro como probabilidade de segurança.

Para limiar h, informar primeiro evento HI≤h e disponibilidade; para espera k, informar primeiro marco utilizável e término da espera. A recuperação de HI não desfaz o evento. Retirada em \(r=\tau+d\); inexistência de decisão antes de T permanece ausência. A idade fixa deve conservar a data sob todas as perturbações sensoriais, respeitado o mesmo ambiente de observação.

**Auditoria obrigatória:** reproduzir as 9.600 decisões externas arquivadas, incluindo 7.200 referências, sem mudar datas, ausências ou classificação. Falha de reprodução interrompe a rodada para diagnóstico, antes de interpretar explicações.

## 5. Instantes e unidade de avaliação

Explicações prospectivamente disponíveis: ciclo39 e depois a cada cinco ciclos até a decisão, inclusive; acrescentar primeira passagem relevante e ciclo de decisão quando não coincidirem com essa grelha. Se a passagem precede39, explicar retrospectivamente o evento e separá-lo da primeira decisão utilizável. Para ausências, seguir até a última observação anterior a T. Não selecionar instantes por proximidade ao endpoint verdadeiro para representar informação operacional.

Para estatísticas globais dos sensores, usar a grelha **comum a todas as políticas** de 39 em passos de cinco, limitada ao menor ciclo de decisão observado entre as políticas sensoriais do motor (ou T−1 se nenhuma decidir). Assim, uma regra tardia não recebe maior peso apenas por fornecer mais instantes. Média por motor primeiro; depois média dos 100 motores, separada por domínio/repetição. Instantes adicionais de evento/decisão servem ao diagnóstico próprio de cada política, sem misturar as duas populações de instantes.

Todas as 9.600 linhas entram na auditoria. Ausências e escolhas internas inviáveis conservam denominador próprio; não recebem artificialmente importância zero, data infinita ou ranking perfeito.

## 6. Perturbações e fronteira de plausibilidade

Dois contrastes pré-fixados, ambos sobre sensores brutos e com todo o pré-processamento recalculado:

1. **Sensibilidade por canal:** pequena alteração assinada em um canal de cada vez. Serve para localizar dependências do modelo; pode quebrar associações entre sensores e não representa uma intervenção física demonstrada.
2. **Sensibilidade conjunta:** alterações correlacionadas entre canais, com direções derivadas da covariância dos incrementos sensoriais iniciais de F25. Serve como controle menos dependente da independência artificial entre canais; continua sendo plausibilidade estatística local.

Em F25, calcular incrementos consecutivos dos sensores nos ciclos6–20, remover a média dos incrementos de cada motor e calcular covariância com igual peso por motor. Canais de variância≤10⁻¹² na unidade original não serão perturbados. Desvios padrão ν_j definem amplitudes; não são limites operacionais. Para o contraste conjunto, usar autovetores em ordem decrescente até explicar≥90% da variância dos incrementos padronizados, com sinal de cada autovetor fixado pelo componente de maior módulo positivo. Guardar autovalores, matriz e canais.

Amplitudes fixas ε∈{0;0,5;1} vezes ν_j, em ambos os sinais; no contraste conjunto, deslocamento \(\pm\varepsilon\,\mathrm{diag}(\nu)\sqrt{\lambda_k}v_k\). Nenhuma amplitude será escolhida usando E. Aplicar cada deslocamento como rampa causal \(g(t)=0\) até20, \(g(t)=(t-20)/20\) de21 a39, e \(g(t)=1\) a partir de40. Isso preserva a referência do ciclo20 e permite replay completo da regra. Em cada instante, a perturbação usa somente ciclo e parâmetros F; não usa T, decisão original ou sensores futuros.

Acrescentar diagnóstico local no instante de decisão (ou último instante disponível em ausência): rampa de zero a um nos últimos20 ciclos, nunca alterando ciclos≤20, seguida de replay somente até esse instante. Esse contraste mede alteração da elegibilidade/decisão já observável, sem prever uma data futura inventada. A intervenção local não substitui o replay completo para medir deslocamento de datas.

Conferir antes da interpretação se cada vetor de incrementos perturbados está no envelope empírico de F: distância de Mahalanobis na sub-base de variância positiva e limite de quantil0,99 obtido em F25, além de amplitudes por canal. Registrar fração fora do envelope, inclusive para a trajetória original; não rejeitar/reescalar silenciosamente perturbações ou excluir motores. Comparar resultados totais e no suporte empírico. A cobertura desse suporte é evidência de extrapolação estatística, não certificação de plausibilidade física.

Nenhuma trajetória será extrapolada depois de T ou completada artificialmente. Perturbar a medição mantendo T fixo é um teste de robustez informacional, não uma simulação de alteração da degradação física ou da vida real do motor.

## 7. Fidelidade e estabilidade: medidas pré-especificadas

| Camada | Medida | Interpretação permitida |
|---|---|---|
| Reconstrução HI/previsão/regra | Erro máximo e número de divergências | Identidade algébrica e reprodutibilidade; não é validação física |
| Sensores → HI | c_j/a_j assinados, variação finita ΔH, concordância de sinal na região não saturada | Dependência aprendida e saturação; contribuições podem cancelar |
| HI/trajectória → previsão | Δvida prevista e comparação ISO/RF nos mesmos sensores perturbados | Sensibilidade preditiva; nenhuma decomposição causal aditiva presumida |
| Previsão/condição → decisão | Δτ e Δr, proporção de datas iguais e de alterações>1/>2 ciclos | Efeito decisório confrontado com prazo1/2; cortes descritivos, sem selo de segurança |
| Eventos | Decisão→ausência, ausência→decisão; mudança entre antes/em/após T | Robustez informacional, não novo risco físico estimado |
| Rankings | Spearman com empates e sobreposição dos cinco primeiros sensores | Concordância, separada da fidelidade e do efeito sobre decisões |

Ranking primário: média por motor de |c_j| na grelha comum; secundário: média por motor de |ΔH|/ε e |Δvida prevista|/ε em ε=0,5. Guardar também sinais, efeito para ε=1 e todos os canais. Para uma previsão sem alteração em todas as direções, declarar ranking não identificável por esse contraste, não atribuir Spearman=1.

Comparar rankings entre partições usando todos os21 sensores: canal excluído pelo modelo recebe contribuição zero, identificado como excluído; falta de observação não recebe zero. Desempatar a seleção top5 pelo identificador do sensor apenas para reprodutibilidade e publicar os empates de fronteira. Spearman usa postos médios; vetores constantes têm correlação indefinida. FD001/FD003 serão comparados por perfil agregado, sem pareamento de motores.

Comparar as três previsões externas do mesmo motor entre repetições: distância absoluta entre datas, ausência discordante e estabilidade das contribuições na interseção de instantes disponíveis. É estabilidade entre ajustes/seleções reutilizando dados, não incerteza de uma frota independente. Não executar bootstrap de reaprendizagem nem mudar parâmetros nesta rodada.

Resumir por motor/domínio/repetição: medianas, quartis, quantis0,05/0,95, extremos, contagens e denominadores; preservar distribuições. Estimandos dos contrastes: diferença média pareada de |Δvida prevista| entre ISO/RF nos instantes comuns; diferença média de |Δr| entre cada regra selecionada e marco/ISO inferior98 do mesmo prazo, condicionada a decisão nos dois replays, junto da diferença de proporção de presença de decisão em todos os motores. Ausências ficam fora somente do estimando de distância finita, com seu denominador publicado, e permanecem no estimando de presença/eventos. Antes da média por motor, dar peso igual às direções, sinais, amplitudes não nulas e instantes elegíveis de cada contraste; publicar por amplitude e tipo de perturbação, sem misturar sensores individuais com direções conjuntas.

Bootstrap pareado descritivo de2.000 reamostragens de motores, semente20261017, separado por repetição e domínio. Reutilizar os mesmos índices nos contrastes de uma repetição/domínio; não reamostrar ciclos como unidades independentes. Não usar intervalos de95% para selecionar o melhor ranking ou certificar risco≤2%.

## 8. Casos adversos e fichas de tarefa

Inventariar todos os casos com ausência, retirada em T, após T ou escolha interna inviável. Para aprofundamento gráfico, manter todos os casos únicos desse inventário; se um motor repetir, mostrar as repetições lado a lado. Acrescentar, por domínio/repetição/prazo, o motor com maior vida não aproveitada, o de maior discordância de datas entre regras e o motor mediano dessa discordância; empates pelo menor ID. A escolha desses exemplos é retrospectiva e serve para diagnóstico, não para avaliação independente.

Cada ficha deve separar: sensores/HI observados; previsão e correção de incerteza; evento memorizado; condição e ciclo de acionamento; prazo/data programada; informação ausente; escolha interna viável/inviável; diagnóstico posterior baseado em T; resposta às perturbações e limite de interpretação. Mostrar o que levou à decisão e o que os dados não permitem concluir sobre o mecanismo físico. Não atribuir o evento FD003 ao fan ou HPC individualmente sem rótulos físicos que o sustentem.

Representação da tarefa: condição de monitoramento, fonte somente sensorial, requisito de disponibilidade, gatilho, prazo e condição de encerramento. Campos de aplicabilidade operacional, criticidade e evidência normativa permanecem por validar à luz do IP-180/ARP7122. Inspeção não será adicionada à ficha como informação já disponível.

## 9. Critérios de interpretação e parada

- **Favorável:** identidades reproduzidas, efeitos previstos pelo mecanismo coincidem com os observados, perfis/rankings e datas mostram estabilidade nas amplitudes especificadas com suporte empírico documentado. Qualificar alcance e magnitude; não existe limiar universal de explicabilidade aprovado.
- **Misto:** reconstrução fiel, mas rankings instáveis, saturação/patamares ocultam alterações ou mudanças>1/2 ciclos/ausências ocorrem; declarar qual camada é estável e em quais condições.
- **Contrário:** a explicação proposta erra o sinal/saída na condição em que deveria ser válida, ou não reproduz o mecanismo. Corrigir o explicador com versão/emenda, preservando o resultado inicial; não retocar modelo/política para melhorar a explicação.
- **Inconclusivo:** suporte empírico insuficiente, quase nenhuma variação identificável ou forte dependência entre dados impede a inferência proposta. Não tratar ausência de resposta como prova de robustez física.

Identidades numéricas devem passar≤10⁻⁹ para HI/previsões; datas/eventos devem ser idênticos. Esse critério testa implementação. Não há regra binária de aprovação operacional baseada em Spearman ou estabilidade de datas. Encerrar após os contrastes e instantes fixados, incluindo os resultados negativos. Antes de novos parâmetros ou novos explicadores, registrar hipótese, benefício discriminante e emenda anterior à nova execução.

## 10. Artefatos, verificação e próxima decisão

Saída prevista: `experiments/artifacts/pilot_explainability_13b/`, exclusiva da rodada. Guardar protocolo e configuração com hashes; parâmetros auxiliares F; contribuições por sensor; auditoria de reprodução; previsões/decisões sob perturbação; suporte empírico; rankings/empates; comparações entre repetições; inventário/fichas de casos; tabelas/figuras; metadados de ambiente; log e manifesto. Não se prevê novo ajuste HI/conversor ou simulação de inspeção.

Antes da execução: testes significativos de soma/clipping/cancelamento, referência preservada, causalidade por prefixo, correspondência ISO/RF, memória do primeiro evento, espera interrompida pelo endpoint, controle idade invariante e tratamento de ausências. Verificador separado deve reconstruir contribuições e uma implementação independente das datas/eventos, conferir todos os insumos e contagens e auditar resultados de perturbação. Não declarar a rodada concluída apenas por produzir gráficos.

**Estado desta entrega:** planejamento de P13.2 concluído; análise/implementação não iniciadas. Dependência P11.2 concluída com decisões reproduzidas e perda básica localizada após o marco. Executar agora este protocolo, reutilizando a auditoria das decisões e mantendo seus testes de identidade/causalidade. P13 permanece parcialmente concluída; validação prospectiva de risco≤2%, ponte econômica P12 e definição operacional de P/inspeções permanecem separadas. O artigo continua M17, sem novos resultados ou detalhes de implementação incorporados nesta entrega.
