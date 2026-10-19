# P05 — HI empírico supervisionado por RUL e comparação com AAKR terminal

Data: 16/10/2026. Protocolo exploratório definido antes de ajustar/avaliar os métodos desta rodada, após sugestão do autor de usar RUL_FD001 e comparar com Baraldi, Bonfanti e Zio (2018). Sem inspeções. RQ1/RQ6: qual representação de condição oferece utilidade prognóstica, comportamento terminal e explicação por sensor sob o mesmo protocolo?

## Dados e verdade de referência

`train_FD001.txt` fornece 100 trajetórias completas, com T_i=max(t) e RUL_i(t)=T_i−t. `RUL_FD001.txt` contém 100 valores associados, por ordem de motor, ao último ciclo de `test_FD001.txt`, não às trajetórias de treino. Para os motores de teste, T_i=t_last,i+r_i e RUL_i(t)=r_i+t_last,i−t. Os identificadores de treino/teste pertencem a populações distintas. O motor 1 de teste termina no ciclo 31, r_1=112 e T_1=143. Nenhum sensor futuro será reconstruído ou inventado.

RUL real fornece supervisão temporal e avaliação do prognóstico; não identifica univocamente o HI físico. Um alvo derivado de RUL é uma convenção supervisionada. Não é permitido comparar métodos atribuindo a esse alvo o estatuto de HI verdadeiro. Rótulos externos nunca entram em normalização, construção do HI, seleção ou conversão HI→RUL.

## Partições e avaliação

Reutilizar os cinco folds de P03: 40 motores de ajuste F, 20 de calibração C para o conversor comum HI→RUL, 20 de seleção S e 20 de avaliação E. Os motores de E foram observados em pilotos anteriores; essa parte permanece desenvolvimento exploratório. A nova família de métodos e sua comparação não serão ajustadas por resultados de E.

Em cada família, selecionar a configuração por RMSE nos ciclos floor(0,50T), floor(0,70T), floor(0,90T) de cada motor de S, com peso igual por motor/corte. Esses cortes são instrumentos retrospectivos de avaliação, não entradas do modelo. Seleção não usa erro contra o alvo de HI que o próprio método escolheu. Reportar também RUL em toda a história observável e no último ciclo; desfechos e cortes são separados.

Avaliação adicional nos 100 motores oficiais de teste: usar a partição do primeiro fold, acrescentando seus 20 motores E aos 40 F, formando 60/20/20 de ajuste/calibração/seleção nos dados de treino. Selecionar cada família somente em S; arquivar essas escolhas antes de calcular métricas com RUL_FD001. Essa avaliação é uma primeira aplicação dessas fórmulas ao teste oficial, não teste intocado em sentido absoluto: a escolha de FD001 e parte do desenvolvimento já refletem conhecimento do benchmark. Não reabrir escolhas após ver métricas oficiais.

## Pré-processamento comum

Média causal de 15 ciclos e referência de cada motor b_ij=x̄_ij(20), com HI disponível apenas em t≥20. Reter canais com desvio dos resíduos iniciais >10⁻⁶ e direção terminal não nula, aprendidos em F. Para as combinações/AAKR, z_ij=d_j(x̄_ij−b_ij)/s_j, com s_j desvio calculado nas observações válidas de F. Não usar identificação, ciclo, RUL, T ou detector P como atributos. O estado inicial é uma referência própria assumida, não as-good-as-new observado.

## Famílias

**MARGEM (controle P04):** mínimo de margens por sensor com tolerância de dois desvios e oito quantis terminais de P04. Nesta rodada o quantil é selecionado pela mesma utilidade prognóstica aplicada às outras famílias, não pela perda convencional de primeira passagem de P04; nomear esse controle como recalibrado por RUL.

**EMPIRICO (formulação nossa):** Ĥ=clip[1−max(0,Σ_j w_j z_j),0,1], w_j≥0. Ajustar w por mínimos quadrados não negativos regularizados, com peso total igual por motor, para representar 1−H*. Alvo de treino H*=min(1,RUL/τ)^γ, τ∈{60;100;140} ciclos, γ∈{1;2}, regularização λ∈{0;0,1} (zero ou um décimo). São 12 configurações. O alvo não usa P; patamar de vida restante é convenção e não evidência de início físico de dano. Pesos e contribuições ficam arquivados por sensor.

**AAKR (adaptação do núcleo de Baraldi):** regressão kernel autoassociativa terminal, reconstrução como média ponderada de padrões dos últimos L∈{5,10} ciclos dos motores F, kernel gaussiano com distância padronizada pela dispersão desses padrões e largura h∈{0,5;2;8}. O resíduo euclidiano no espaço z orienta HI decrescente. Normalizar usando resíduo na referência inicial e mediana de resíduos no endpoint de F, calculados excluindo os padrões do próprio motor (leave-one-engine-out). Não usar resíduos de auto-reconstrução terminal para fixar zero. Candidatos a sensores: todos, cinco e dez melhores segundo média de monotonicidade, tendência comum e prognosticabilidade univariadas em F; remover subconjuntos duplicados. São até 18 configurações. Arquivar ranking/subconjuntos e parâmetros.

Esse contraste implementa o núcleo terminal AAKR, não a reprodução integral do artigo: usa FD001, atributos causais comuns e subconjuntos determinísticos em lugar de decomposição modal empírica e busca por evolução diferencial binária. Não atribuir diferenças à totalidade do método publicado. Monotonicidade, tendência e prognosticabilidade são diagnósticos auxiliares; não substituir avaliação prognóstica independente por otimização da aparência da curva. Uma reprodução integral exige uma rodada própria, incluindo orçamento e controles para esses componentes.

## Conversor comum e métricas

Para cada configuração, ajustar regressão isotônica crescente HI→RUL somente em C, com pesos de motor iguais e extrapolação constante fora do intervalo. A relação pode saturar na fase saudável; reportar esse limite. Essa etapa usa os mesmos dados e algoritmo em todas as famílias, sem receber sensores extras. Comparar erro quadrático médio (RMSE) e erro absoluto médio (MAE) em ciclos e calibração descritiva em faixas de RUL; identidade da configuração selecionada fica separada dos resultados externos.

Nos motores completos externos, reportar HI terminal, primeira passagem por zero/ausência e antecipação, recuperações, patamar inicial assumido, monotonicidade, prognosticabilidade e tendência interpolada apenas para avaliação. No teste oficial truncado, reportar HI no último ciclo e zeros antes de F conhecido; não avaliar HI terminal onde faltam sensores. Nenhum método terá HI forçado a zero com seu próprio T externo. Guardar curvas de motores 1/2/3 previamente fixados. No teste oficial, comparar RMSE pareado por reamostragem de motores (2.000 bootstrap, semente 20261016), interpretando intervalos como descritivos condicionais, sem alegação confirmatória de superioridade.

## Interpretação, fronteiras e parada

Favorável: utilidade prognóstica e referência terminal mais consistentes em motores não usados no ajuste. Misto: bom prognóstico mas zeros inadequados ou seleção instável. Contrário: nova fórmula não melhora controles ou apenas reproduz o alvo por construção. A utilidade de um conversor HI→RUL não valida o HI físico, a detectabilidade de P ou o ganho de inspeção. Encerrar após os cinco folds e uma avaliação oficial, preservando resultados negativos e todas as configurações; não ampliar a grelha em resposta ao teste.

Testes: alinhamento e isolamento dos rótulos oficiais, perturbação dos sensores futuros, impossibilidade de usar o endpoint externo na transformação, exclusão do próprio motor nas referências terminais e comportamento numérico do kernel em distâncias grandes. Artefatos: auditoria de rótulos, seleções, coeficientes/ranking, parâmetros, predições/HI, métricas individuais e agregadas, bootstrap, gráficos, relatório, versões e hashes. Dados, artefatos P01–P04 e manuscrito permanecem preservados.
