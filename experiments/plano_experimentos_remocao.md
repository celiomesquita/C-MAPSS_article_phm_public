# Experimentos para determinar o momento de remoção

Data: 17/10/2026. Detalhamento subordinado ao [plano executivo vigente](../docs/gestao/plano_executivo_de_melhorias.md), que concentra estados e prioridades. P11, P11.1 e P13.1 concluídas; P13 parcialmente concluída; P12 planejada. Protocolo principal não congelado; artefatos anteriores e artigo preservados.

## Pergunta e objetivo da comparação

**RQ1/RQ2/RQ3/RQ5/RQ6:** qual regra causal de remoção aproveita mais vida útil e reduz a frequência de restaurações, dentro dos critérios experimentais de admissibilidade, e como explicar suas decisões? O resultado procurado é a melhor regra entre as alternativas avaliadas, com incerteza e domínio explícitos. Não se alegará ótimo global ou ciclo individual ótimo conhecido a partir de previsão imperfeita.

O índice de saúde (HI) empírico adotado em M18 permanece como referência; manter regressão isotônica (ISO) e floresta aleatória com HI e inclinação causal (RF_SLOPE). O alvo de 98% de cobertura preditiva não equivale a ultrapassagem ≤2% na política. P10 encontrou pouca antecedência no limite inferior, apesar de quantis finitos: agora é preciso avaliar a ação e sua consequência económica.

## Cenários económicos

| Cenário | Objetivo | Parâmetros e alcance |
|---|---|---|
| Base vigente | Minimizar custo de restauração por ciclo efectivamente aproveitado | Restauração perfeita (*as good as new*, AGAN), custo fixo idêntico por evento, sem custos complementares; não depende de preço actual de oficina |
| Extensão de disponibilidade | Estimar ciclos voados e restaurações num horizonte calendário comum | Acrescentar, como hipótese de cenário, utilização e indisponibilidade efectiva; nenhum valor considerado observado no C-MAPSS |
| Extensão de receita | Estimar receita e saldo após restauração por unidade de tempo | Parametrizar receita por ciclo; saldo não é lucro contabilístico, pois outros custos operacionais não estão representados |

O cenário base continua em vigor. As extensões serão análises condicionais, sem converter receita, utilização ou tempo de oficina em fatos do conjunto de dados. A indisponibilidade relevante é a da operação: com motor substituto, não corresponde necessariamente à duração de toda a revisão. Antes da execução económica, registrar valores, unidades, horizonte, origem e faixas de sensibilidade; parâmetros sem fonte serão identificados como hipóteses. O valor histórico candidato de USD 2,25 milhões não passa a custo actual ou calibrado.

**Especificação M21 — horizonte e baseline.** Horizonte de 20 anos definido pelo autor. Adopta-se como cenário de utilização 1.600 ciclos de voo por aeronave/ano, arredondado da estimativa easyJet 2025 de 576.000 setores/354 aeronaves médias ≈1.627; sensibilidade de aproximadamente 1.889 usando a média de aeronaves operadas. A exposição de referência sem parada adicional é 32.000 ciclos em 20 anos. Custo fixo de restauração: USD 6 milhões por motor/evento como hipótese de escala, com sensibilidades USD 5/7 milhões, baseada na faixa de visita completa CFM56-7B divulgada pela AerFin em março de 2026. Fontes, localização e limites: [notas M21](../references/cenario_economico_20anos/notas_fontes.md). Não se identifica o motor do conjunto com esse motor comercial ou com a frota da easyJet.

**Boroscopia — decisão do autor.** Considerar custo incremental C_I=0 e tempo incremental de indisponibilidade D_I=0. Registrar quantidade, instantes e resultados de inspeção; não contabilizar receita perdida ou cobrança por boroscopia. A hipótese não elimina o custo, o prazo de execução ou a eventual indisponibilidade por restauração. O braço com inspeção continua adiado ao congelamento, com periodicidade de cinco ciclos somente em P–F e até a decisão de remoção.

**Comparação de custos em 20 anos.** Para Mπ restaurações efectivamente ocorridas no horizonte, Cπ(20)=C_R Mπ, tanto em PHM como em PHM + inspeção. Economia positiva do híbrido frente a PHM: ΔC=C_R(M_PHM−M_híbrido), e economia relativa ΔC/C_PHM quando o denominador for positivo. Conservar também o controle de idade fixa como baseline de política: custo por evento e política de referência são conceitos distintos. A comparação principal usa dólares de referência de 2026 sem desconto; prever sensibilidades com taxas reais assumidas de 3% e 5% sobre desembolsos nas datas dos eventos, não sobre contagens finais.

**Ponte entre simulação e calendário.** A taxa da companhia não calibra a duração de vida das trajetórias C-MAPSS. Antes de extrapolar financeiramente, explicitar a correspondência entre ciclo simulado e ciclo de voo; um para um será cenário estilizado, não estimativa real de manutenção de companhia. Não reescalar inspeções, reserva ou execução sem nova especificação. A utilização publicada já incorpora indisponibilidades: não acrescentar parada de revisão à mesma base realizada sem explicitar demanda potencial/utilização quando disponível. Sem ponte fundamentada, separar métricas normalizadas por exposição simulada das projeções condicionais de 20 anos. Custos serão por posição de motor; receita de aeronave não será duplicada pelo número de motores.

Seja Nπ o número de ciclos operados desde a condição restaurada até a retirada ou o endpoint, e C_R o custo fixo da restauração. Sob a hipótese adicional de vidas sucessivas independentes e identicamente distribuídas, a taxa de custo no cenário base é

\[
c_\pi=\frac{C_R}{\mathbb{E}[N_\pi]},\qquad
\widehat c_\pi=\frac{n C_R}{\sum_{i=1}^{n}N_{i\pi}}.
\]

Usar a razão entre totais; a média de C_R/N_i não estima a mesma taxa de renovação. A independência das vidas é hipótese experimental, não consequência automática de AGAN ou evidência observada de restaurações no C-MAPSS. A formulação de razão de recompensas por duração esperada segue o teorema de renovação-recompensa de [Vlasiou, *Renewal Processes with Costs and Rewards*, teorema 1](https://arxiv.org/html/1404.5601v1). As especializações seguintes são a formulação proposta para este estudo.

Na extensão com utilização constante u em ciclos/dia, parada média efectiva D em dias por evento e receita constante r por ciclo, definir Hπ=E[Nπ]/u+D:

\[
f_\pi=\frac{1}{H_\pi},\quad
v_\pi=\frac{\mathbb{E}[N_\pi]}{H_\pi},\quad
G_\pi=\frac{r\mathbb{E}[N_\pi]-C_R}{H_\pi}.
\]

f é a frequência de restaurações por dia; v, os ciclos voados por dia; G, o saldo diário entre receita e restauração. Para D=0, v=u: retirar antes não reduz a receita nesse cenário, mas aumenta a taxa de restaurações. Para parâmetros comuns C_R>0, u>0, D≥0 e r≥0, maximizar G e minimizar c favorecem a mesma maior E[Nπ]. Portanto, não presumir compromisso económico interior sem custos, indisponibilidades ou consequências que variem com a condição. O objetivo operacional é prolongar a vida **dentro do domínio admissível**. Não acrescentar uma penalização monetária pela vida não aproveitada se o mesmo efeito já está representado pela frequência de revisões.

## P11 — comparar regras causais de remoção, sem inspeção

**Estado: concluída, com resultado misto.** [Protocolo executado](protocolo_remocao_11.md), [interpretação](artifacts/pilot_removal_11/conclusoes.md) e [verificação](artifacts/pilot_removal_11/verification.json). A âncora central deixou ausências de decisão; o limite inferior 98% teve decisões completas e zero chegadas nos completos avaliados, mas muitas retiradas ocorreram já no primeiro marco. O controle de idade também apresentou eventos. Não há ótimo confirmado ou economia empresarial estimada.

**Prioridade indispensável.** Dúvida: a reserva deve referir-se à previsão central ou ao limite inferior, e qual é o efeito real da sua composição com a execução? Comparar as duas interpretações como alternativas experimentais, sem adoptar silenciosamente uma delas como preferência do autor.

**Dados e orçamento.** Reutilizar previsões externas completas, partições, modelos e calibrações congeladas P10: FD001 principal, FD003 robustez, três repetições, dez dobras, F25/C15/U50/E10. Nenhum novo ajuste nesta comparação inicial. Cada repetição contém os mesmos 100 motores por domínio, não 300 motores independentes. Os testes oficiais truncados servem somente para decisões observáveis antes do truncamento; não reconstruir políticas futuras nem incluir vidas incompletas como vidas completas na taxa de renovação.

**Grelha primária fechada antes da execução.** ISO/RF_SLOPE × âncora central/inferior × reserva m∈{15,12} × execução d∈{1,2}: 16 configurações por domínio e repetição. A reserva 15 é a referência do autor; 12 é sensibilidade candidata, sem adoção automática ou interpretação como redução de incerteza. O limite inferior usa calibração de trajetória nominal 98%; sensibilidade 95% somente para a âncora inferior, sem escolher o nível mais favorável. Não há transição adaptativa 15→12 nesta primeira rodada: esse mecanismo depende de critério observável pré-especificado de incerteza elevada.

**Regra candidata para especificação.** Sejam t₀ o primeiro HI≤0,5 com atributos disponíveis, F̂(t) a previsão central e L(t) o limite inferior. Para B(t)∈{F̂(t),L(t)}, propõe-se

\[
\tau_\pi=\inf\{t\ge t_0:B(t)-t\le m+d\},\qquad
r_\pi=\tau_\pi+d.
\]

τ é o instante da decisão, r a retirada programada. Essa convenção interpreta m como reserva que se pretende preservar na retirada, separada do prazo d para executá-la; deve constar explicitamente do protocolo P11. Previsões são actualizadas a cada ciclo até τ; depois, a data fica comprometida, sem adiamento por uma previsão subsequente mais optimista. Rever ou antecipar uma decisão já tomada será extensão identificada, não mudança durante o ensaio.

Se a condição já estiver satisfeita no marco, decidir nesse instante e registrar se B(t₀)−t₀<m+d: a reserva prevista já é insuficiente. Não fingir que a decisão ocorreu antes de o marco ser observado. Se não houver marco ou gatilho antes do fim observado, registrar ausência de decisão; não excluir o motor nem inventar uma retirada. A conduta operacional de contingência permanece por especificar; uma regra incompleta não será proclamada vencedora.

**Controles.** Incluir uma regra de idade fixa, independente de sensores, cuja idade seja definida em desenvolvimento e congelada antes de avaliar E; o protocolo deverá fixar o critério de escolha. Como referência idealizada de vida máxima, usar T conhecido somente na aferição, sem o disponibilizar a uma política. Esse limite de comparação não é tarefa executável ou política admissível. Não seleccionar retrospectivamente a idade fixa que perde para o método proposto.

**Desfechos por motor.** Registrar decisão, retirada programada, endpoint T, execução d, reserva prevista na retirada, ausência de marco/gatilho, insuficiência no primeiro momento de decisão, ultrapassagem estrita r>T, chegada r≥T e atraso programado (r−T)₊. São desfechos distintos. O alvo de até 2% fornecido pelo autor se refere à ultrapassagem estrita; não o redefinir como tolerância de 2% dos ciclos nem assumir que chegar a T é operacionalmente aceitável. O protocolo precisa esclarecer o tratamento da chegada exacta a T e das ausências antes de declarar admissibilidade.

Para a contabilidade observacional, usar Nπ=min(rπ,T); na ausência de decisão, Nπ=T, com falha de cobertura decisória explicitamente assinalada. Esse último caso não se torna economicamente desejável pelo maior N: regras com conduta incompleta ficam sem classificação de admissibilidade. Uma programação posterior a T é contrafactual; não gera receita, sensores, HI ou inspeção depois do endpoint. No modelo económico de base, a renovação no endpoint recebe o mesmo custo fixo, sem acrescentar penalidade de falha não autorizada; o evento continua exposto nas métricas de admissibilidade.

**Entrega e interpretação.** Tabela por configuração/repetição com eventos, cobertura decisória, vida aproveitada e custo normalizado; fronteira entre ultrapassagem e vida aproveitada. Favorável: alguma regra completa preserva o alvo e aproveita mais vida que o controle. Misto: benefício restrito a domínio/divisão ou perda de antecedência. Contrário: nenhuma regra atende aos critérios. Inconclusivo: faltam definições de contingência, amostra ou comparação justa. Não escolher a melhor semente, excluir os motores 55/71 de FD003 ou modificar HI para favorecer a economia.

## P11.1 — isolar o valor incremental do prognóstico

**Concluída com ganho incremental pequeno/variável.** [Protocolo executado](protocolo_controle_marco_11a.md), [interpretação](artifacts/pilot_landmark_control_11a/conclusoes.md) e [verificação](artifacts/pilot_landmark_control_11a/verification.json). O controle retirou no primeiro HI≤0,5 utilizável mais d, com o mesmo HI/aquecimento/motores e sem previsão de F ou quantil na decisão. Todos os completos tiveram decisão sem chegadas. ISO/inferior98/reserva15 acrescentou somente 0,21–1,57/0–0,83 ciclo médio e 0,12–0,93%/0–0,40% de economia normalizada, FD001/FD003. O marco já respondeu por 95,93–100% do ganho de vida dessa regra frente à idade fixa. Não é confirmação independente ou prova de irrelevância do prognóstico noutros regimes.

Resposta neste regime: o ganho frente à idade fixa decorreu sobretudo da representação supervisionada e seu marco; o conversor/calibração ofereceu incremento pequeno, nulo numa divisão FD003. O controle HI torna-se referência decisória competitiva. A construção do HI continua supervisionada por vida remanescente, portanto não se eliminou toda a informação prognóstica aprendida. Não retocar fórmula, limiar ou semente para favorecer o conversor. A qualidade do controle de idade continua limitação antes de alegar vantagem geral sobre manutenção preventiva real.

## P12 — estimar economia e ganho de longo prazo

**Prioridade indispensável para RQ3, após P11.** Primeiro calcular, para todas as alternativas, custo normalizado C_R=1, ciclos médios aproveitados, vida não aproveitada e restaurações por exposição comum; comparar economicamente apenas as classificadas como admissíveis. Ausências e eventos continuam no relatório de todas as regras. Para política candidata π frente ao controle b, estimar economia relativa 1−cπ/c_b. Não somar vidas de repetições como se fossem motores novos.

Validar a taxa analítica com simulação de vidas AGAN amostradas com reposição dos motores de avaliação de cada domínio/repetição, mantendo cada trajetória intacta e aplicando a mesma regra congelada. Usar as mesmas sequências de vidas entre políticas; repetir uma trajetória não cria um novo motor independente para inferência. Não reconstruir sensores de uma vida a partir de fragmentos de diferentes motores. A simulação é uma renovação empírica hipotética, não validação pós-revisão.

O protocolo de execução deverá fixar sementes, exposição, número de replicações, tolerância de erro Monte Carlo e teste de convergência antes dos resultados. Em horizonte finito, definir explicitamente se a restauração inicial é custo incorrido, contabilizar a vida final incompleta e evitar cobrar uma revisão que ainda não ocorreu. Distinguir horizonte operacional comum (ciclos voados) de horizonte calendário comum (dias).

M21 fixa o horizonte principal em 20 anos e a utilização/custo de referência acima; aquisição ou restauração inicial será condição inicial comum, fora dos custos incrementais comparados. Contar apenas restaurações ocorridas dentro do horizonte, registrar a vida residual final e avaliar sensibilidade ao efeito de borda. A boroscopia terá custo e duração incrementais zero em todas as comparações desta especificação; a vantagem económica só decorrerá da mudança das decisões e dos eventos de restauração, respeitada a admissibilidade. Nenhuma inspeção será executada antes do congelamento.

**Tabela principal de resultados.** Comparar baseline de idade fixa, PHM somente por sensores e modelo híbrido PHM + inspeção boroscópica. O baseline é controle experimental a definir em desenvolvimento, não a política real da companhia usada como referência de utilização. Tabela a preencher após os experimentos, por domínio e repetição, com incerteza das diferenças; os traços abaixo não representam resultados nulos.

| Indicador no horizonte de 20 anos | Baseline: idade fixa | PHM sem boroscopia | PHM + boroscopia |
|---|---|---|---|
| Restaurações por posição de motor | — | — | — |
| Custo acumulado de restauração, USD de referência de 2026 | — | — | — |
| Diferença de custo frente ao baseline, absoluta e percentual | — | — | — |
| Ciclos efectivamente aproveitados | — | — | — |
| Vida não aproveitada por restauração, ciclos | — | — | — |
| Ultrapassagens do endpoint, contagem e denominador | — | — | — |
| Chegadas ao endpoint e ausência de decisão, separadamente | — | — | — |
| Inspeções e reprovações que anteciparam a decisão | 0 | 0 | — |
| Indisponibilidade por restauração e receita, se parametrizadas | — | — | — |
| Voos realizados pela frota elegível, se parametrizada | — | — | — |
| Receita e despesas variáveis incrementais, separadamente | — | — | — |
| Saldo económico modelado Receita − Despesa e diferença frente ao baseline | — | — | — |

Além da diferença frente ao baseline, apresentar o contraste pareado PHM + boroscopia versus PHM nos mesmos motores, previsões e sequências de vidas. Classificar a admissibilidade junto dos resultados económicos; não ocultar eventos de uma alternativa por ela ter menor custo. A contagem de inspeções/reprovações não é cobrança financeira.

**Antecipação por achado de inspeção.** No primeiro contraste do braço híbrido, manter a regra PHM congelada e adicionar um gatilho de reprovação nas oportunidades autorizadas em P–F. O resultado binário é amostrado segundo a probabilidade teórica de reprovação, com parâmetros e dependência temporal pré-especificados; não será uma leitura exacta do HI. Seja τ_B a primeira reprovação antes da decisão PHM; se não ocorrer, τ_B=+∞. Então τ_híbrido=min(τ_PHM,τ_B) e r_híbrido=τ_híbrido+d, conservando o mesmo prazo de execução. Reprovação antecipará a decisão quando τ_B<τ_PHM; aprovação não autoriza postergar a retirada PHM. As inspeções terminam na decisão e não ocorrem no endpoint ou após ele. Registrar quantidade e ciclos de antecipação, além da vida e dos eventos que resultarem da retirada.

**Interpretação económica prévia.** Com essa regra apenas aditiva, a retirada híbrida não pode ocorrer depois da PHM na mesma vida. Sob as mesmas sequências emparelhadas, custo fixo AGAN e demais hipóteses comuns, antecipar pode aumentar a frequência e o custo de restauração; custo nulo de inspeção não elimina esse efeito indirecto. Portanto, o benefício a testar é a redução de eventos tardios e o compromisso com vida/custo, sem pressupor economia do híbrido frente ao PHM. Melhorias de custo face ao baseline continuam questão empírica. Uma política que use aprovações para prolongar operação seria outro contraste e exigiria especificação e validação próprias; não será introduzida silenciosamente para tornar o híbrido economicamente superior.

Executar depois as extensões condicionais de disponibilidade e receita. Cenários devem incluir D=0 e D>0; separar utilização e receita para não contar receita perdida duas vezes. Calcular restaurações, ciclos voados, receita, custo e G no mesmo horizonte calendário, com ganho absoluto ΔG=Gπ−G_b. Não usar percentagem de ganho sobre saldo zero ou negativo. Fazer sensibilidade em C_R, r, u e D sem escolher seus valores para inverter a conclusão.

**M22 — resultado financeiro por companhia.** A [avaliação de viabilidade](../references/cenario_economico_20anos/impacto_financeiro_empresa.md) estabelece a ponte: ganho esperado em 20 anos = contribuição dos voos adicionais/perdidos + economia/acréscimo de restaurações. Para ΔQ voos adicionais, receita p por voo e custo variável incremental v, E[ΔB]=(p−v)E[ΔQ]+C_R E[M_b−Mπ]. Contar restaurações nos motores elegíveis e receita uma vez por voo da aeronave; explicitar spares/remanejamento e sobreposição de paradas. Se a programação for integralmente preservada, ΔQ=0 e só as despesas de restauração representadas mudam. Não atribuir toda a receita dos voos adicionais ao ganho, pois também haverá despesas variáveis.

Usar como benchmark a receita média por setor derivada dos dados públicos da easyJet, sem adoptá-la como receita marginal conhecida ou inferir v do custo total médio. Fixar população elegível, procura, disponibilidade e moeda/ano-base antes de somar fluxos. A entrega será saldo económico em caixa modelado; lucro contabilístico requer tratamento próprio de capitalização/depreciação/provisões. Não acrescentar a poupança simulada ao lucro publicado como se fosse efeito demonstrado. Não executar essas extensões antes de fechar suas hipóteses e a ponte de escala; não há valor de ganho estimado nesta atualização.

**Entrega e parada.** Curvas de economia versus exposição, ganho versus indisponibilidade e limiares de parâmetros que mudem a conclusão, quando existirem. Encerrar a expansão do simulador quando reproduzir a taxa analítica dentro da tolerância pré-fixada; mais replicações não corrigem a incerteza sobre os motores ou parâmetros económicos. Se nenhuma política for admissível, registrar o diagnóstico económico, sem recomendar uma regra apenas por custo menor.

## P13 — avaliar estabilidade da escolha e explicar as decisões

**P13.4 concluída, 17/10/2026.** [Protocolo](protocolo_estabilizacao_hi_13d.md) e [comparação em desenvolvimento](artifacts/pilot_hi_stabilization_13d/conclusoes.md): cinco alternativas,31.200 soluções/312.000 respostas e60 indicações congeladas antes dos ajustes F25 finais; sem pontuar U/E. Melhora agregada de estabilidade, mas máximos piores em11/60 partições e uma contingência M18 inelegível em FD003/repetição2/dobra2. Próximo teste: cadeias completas indicadas versus M18 com conversores reaprendidos e U50 recalibrado, avaliação E10 sem nova escolha, prazos1/2 e reserva15. Preservar a contingência e a cauda; não aplicar quantis antigos ao HI novo ou ampliar a grade desta rodada. A transferência para remoção e extremos externos permanece desconhecida.

**P13.5 concluída, 17/10/2026.** [Protocolo](protocolo_cadeia_hi_13e.md) e [comparação das cadeias completas](artifacts/pilot_hi_chain_13e/conclusoes.md): M18 reproduzida de P10 nas 60 partições; SEL com conversores reaprendidos em C15 e quantis em U50; dez regras fixas (P11 primárias com reserva 15 e marco HI, prazos 1/2), 12.000 decisões E10, sem nova escolha em C/U/E. Critério de transferência favorável não satisfeito: p95 da amplitude do marco entre repetições 9,15→12,05 ciclos em FD001 e 27,45→21,60 em FD003, com mais motores acima de 10 ciclos nos dois; ISO inferior 98%/reserva 15 ganhou 1,30–1,96/2,29–4,74 ciclos médios, mas SEL teve chegada exata, ultrapassagem e ausência no FD003 motor 10, ausentes em M18. Caso 55 inalterado (212 ciclos), pois duas das suas partições mantiveram M18. M18 continua referência; não ampliar a grade nem escolher retrospectivamente uma família.

**Decisão M23, 17/10/2026.** O autor encerrou a estabilização do HI e aceitou M18 com as instabilidades documentadas em P13.2–P13.5. Não haverá nova comparação de HI nesta fase; as alternativas de P13.4 ficam como resultado exploratório. O restante de P13 é a confirmação do risco com dados independentes. Os próximos trabalhos são P12, que depende da ponte entre ciclos C-MAPSS e ciclos de voo, e a especificação do braço de inspeção antes do congelamento.

**P13.3 concluída, 17/10/2026.** O [diagnóstico de influência](artifacts/pilot_hi_influence_13c/conclusoes.md), sob [protocolo prévio](protocolo_influencia_hi_13c.md), reproduziu600 marcos e executou300 ajustes F24/3.000 respostas. No caso55 FD003,13 exclusões na repetição2 invertem cinco orientações e deslocam o marco204–213 ciclos; manter pré-processamento não elimina a sensibilidade dos coeficientes (até179 ciclos na repetição3). Próxima etapa: especificar estabilização em desenvolvimento com M18 como controle, preservando fidelidade ao alvo e perda decisória, antes de refazer conversores/calibração. Não adoptar a variante pelo E dos casos, reduzir reservas ou iniciar inspeções. O diagnóstico é exploratório e não confirma risco populacional.

### Prioridade anterior: P11.2 — localizar a perda restante

P11.2 concluída em17/10/2026 com [interpretação](artifacts/pilot_loss_decomposition_11b/conclusoes.md) e [verificação](artifacts/pilot_loss_decomposition_11b/verification.json). Oráculos inicial/após sinal coincidem para retirada T−1: perda básica por acesso zero. ISO/inferior98/reserva15 mantém36,08–37,90/35,99–40,50 ciclos de descarte adicional FD001/FD003 na etapa posterior, sem provar que sejam recuperáveis. Diagnóstico de antecedência15: acesso tardio1–3/100 e2–3/100, sem parcela de aquecimento. Mantidos M18, prazo1/2, risco estrito≤2%, nenhuma escolha em U/E e código próprio. Os69 testes e reconstrução de28.800 decomposições/576 resumos passaram. A dependência de P13.2 foi atendida; a etapa posterior contém modelo, calibração e regra, não apenas erro preditivo.

**Prioridade indispensável antes de recomendar uma regra.** Distinguir seleção exploratória e validação: os dados P10 já foram examinados. A melhor configuração observada entre várias alternativas é uma candidata, não um ótimo confirmado. Apresentar todas as configurações e a sensibilidade da fronteira; não relatar apenas a vencedora.

P11.1 passou a exigir o controle HI entre as referências. P13.1 executou o [protocolo de seleção interna](protocolo_selecao_decisoria_13a.md): D40 com quatro blocos internos V10 e ajustes HI em F25, sem U/E na escolha. Foram congeladas 240 escolhas antes da aplicação externa, comparadas com 12 referências fixas. O [resultado misto](artifacts/pilot_policy_selection_13a/conclusoes.md) mostra ganho de vida, mas quatro escolhas internas inviáveis e 0–2 chegadas/100 com limiar, 0–1 com espera. Zero interno não se transferiu uniformemente; não há nova política operacional adotada. Os 59 testes e a verificação final passaram; emendas do verificador registradas na auditoria.

Se houver ajuste de novos limiares, contingências ou critério adaptativo de incerteza, desenhar seleção interna por motor em desenvolvimento antes da calibração final U e da avaliação externa E. U não será grupo de seleção, nem E será usado para ajustar e comprovar a mesma regra. F25/C15/U50/E10 não contém um grupo S adicional: não introduzir seleção oculta. O protocolo deverá documentar validação interna dentro do desenvolvimento e eventual realocação; cada preditor final de 98% precisa conservar pelo menos 49 motores de calibração disponíveis. Se esse desenho não for viável com 100 motores, limitar a alegação à comparação exploratória de regras pré-fixadas e registrar a necessidade de evidência independente para confirmar a escolha.

Quantificar a incerteza das diferenças de custo/vida por reamostragem pareada por motor e por repetição, distinguindo a análise condicional a modelos congelados da análise com reaprendizagem completa. Reamostrar ciclos isolados ou usar três repetições como 300 motores é inadequado. Uma estimativa de ultrapassagem ≤2%, inclusive zero em 100, não certifica risco populacional ≤2%. Relatar denominador, contagem e incerteza; intervalos binomiais exatos só se aplicam quando a amostra e a regra fixa atenderem às hipóteses, não automaticamente ao conjunto agregado de predições de validação cruzada.

Explicar a cadeia sensor→HI→F̂/L→gatilho→retirada: contribuições dos sensores e atributos temporais, correção de incerteza, reserva, prazo e contingência. Testar fidelidade por perturbações causais plausíveis e estabilidade entre divisões/motores; concordância de rankings não substitui fidelidade. Preservar exemplos de retirada prematura, ultrapassagem, insuficiência de antecedência e decisões discordantes entre regras, incluindo a instabilidade FD003 observada em P10. A decisão deve poder ser representada como tarefa com condição de acionamento, prazo, informação necessária e justificativa, enquadrada pelo IP-180 e pela ARP7122 sem alegar conformidade não demonstrada.

## Condições para o próximo protocolo e para o braço de inspeção

### P13.2 — concluída com resultado misto

O [resultado P13.2](artifacts/pilot_explainability_13b/conclusoes.md) confirmou fidelidade computacional, mas mostrou estabilidade limitada: Spearman mediano das contribuições0,728/0,560 em FD001/FD003; motor55 FD003 com217 ciclos de diferença na espera,212 já no marco. As9.600 decisões e2.187.520 replays passaram por verificação independente;82 testes,66 fichas. Nenhum prefixo completo permaneceu no envelope inicial F25, impedindo alegar robustez física validada. Os diagnósticos explicam o papel do quantil/reserva no acionamento conservador, sem demonstrar que possam ser reduzidos. Modelos, escolhas e [protocolo](protocolo_explicabilidade_13b.md) preservados, com erro de registro corrigido e documentado antes do primeiro resultado perturbado. Nenhuma inspeção ou edição do artigo.

P11/P11.1/P11.2/P13.1/P13.2 estão executadas. Antes do congelamento, especificar diagnóstico dirigido da influência/identificabilidade da aprendizagem do HI e do marco nos casos extremos, sem refazer indiscriminadamente a busca de fórmula perfeita. Qualquer correção exige seleção/validação por motor e nova avaliação explicitamente exploratória enquanto reutilizar estes dados. Uma alegação confirmatória de risco baixo exige evidência prospectiva independente; não ajustar depois de E para obter zero eventos. P12 ainda requer a ponte de escala para20anos. Admissibilidade operacional, critério adaptativo de incerteza e contingências continuam abertos.

P11/P11.1 precedem a contabilização P12; P13 avalia estabilidade, seleção e explicabilidade antes da recomendação. Congelar pré-processamento, prognóstico, calibração, decisão, economia e avaliação, e especificar a referência independente e os parâmetros do futuro braço de inspeção antes de executá-lo. Só então comparar PHM e modelo híbrido PHM + inspeção, com inspeções a cada cinco ciclos exclusivamente em P–F e até a decisão de remoção. Nenhuma inspeção foi executada em P11.
