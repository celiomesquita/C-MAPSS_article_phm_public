# P06 — transferência FD001→FD003 e reajuste dentro de FD003

Protocolo definido em 16/10/2026, antes de executar os modelos em FD003, após autorização explícita do autor. Extensão de robustez: FD001 permanece o cenário principal; FD003 acrescenta uma condição operacional com dois modos de degradação (compressor de alta pressão e fan), conforme readme local. Sem inspeções ou alteração do cenário econômico.

## Pergunta e contrastes

RQ1/RQ6: a representação de condição e o prognóstico se transferem a FD003 sem reajuste? O que muda quando a mesma formulação é aprendida nos motores de treino de FD003? Comparar MARGEM, EMPIRICO e a adaptação de regressão kernel autoassociativa terminal (AAKR) de P05. Não é reprodução integral de Baraldi et al. (2018).

1. **Transferência direta:** carregar exatamente os modelos oficiais congelados de P05, incluindo sensores, direções, escalas, pesos, âncoras e conversor HI→RUL. Nenhum ajuste, recalibração ou seleção em FD003. A referência própria de cada motor no ciclo 20 continua calculada de suas observações iniciais, pois já faz parte da formulação causal. Aplicar às 100 trajetórias completas de treino FD003 e às 100 truncadas de teste. Os motores FD003 não participaram do ajuste desses modelos FD001, mesmo quando seus IDs numéricos coincidem.
2. **Reajuste em FD003:** reutilizar sem alteração as funções matemáticas, grelhas e regra de seleção de P05, aprendendo parâmetros somente em FD003. Cinco folds agrupados por motor, 40 ajuste/20 calibração/20 seleção/20 avaliação. Usar os mesmos grupos numéricos de P05 como desenho, sem considerar motores homônimos de subconjuntos diferentes como pares físicos. No ajuste final, 60/20/20 motores de treino FD003 conforme P05. Arquivar escolhas/modelos antes de avaliar RUL_FD003.

As grelhas permanecem 8 configurações de MARGEM, 12 de EMPIRICO e até 18 de AAKR. Sem ampliar τ, largura do kernel ou referências em resposta a FD003. O número de modos e a distribuição de vidas mudam simultaneamente: diferenças entre FD001 e FD003 não isolam causalmente o efeito do segundo mecanismo. O banco distribuído não inclui aqui rótulo independente do mecanismo dominante por motor; não inventar essa classificação.

## Dados, causalidade e seleção

Ler train_FD003/test_FD003/RUL_FD003 com o mesmo esquema de 26 colunas (21 sensores). O readme declara 100 motores completos e 100 truncados. Conferir contagens/alinhamento por ordem. RUL_FD003 informa a vida restante no último ciclo observado: T=t_last+r e RUL(t)=T−t. Não fornece HI físico ou sensores futuros. Não reconstruir a parte não observada.

Pré-processamento de P05: média causal de 15 ciclos, referência no ciclo 20, sem HI antes de 20. O conversor isotônico HI→RUL usa motores C separados; seleção por RMSE em cortes retrospectivos a 50/70/90% da vida dos motores S. O alvo min(1,RUL/τ)^γ é convenção supervisionada apenas para o ajuste empírico. Nenhum endpoint ou rótulo externo entra em transformação, normalização ou seleção.

Preservar os modelos/artefatos P01–P05 e não alterar seus scripts. A reavaliação dos modelos FD001 no próprio teste FD001 deve reproduzir os resultados salvos como teste de integridade do carregamento. As decisões de P06 serão congeladas antes da avaliação oficial FD003; não reajustar após observar seus resultados. FD003 será considerado conjunto já examinado ao fim desta rodada.

## Evidência, incerteza e interpretação

Em trajetórias completas, reportar RMSE nos cortes, RMSE médio por motor na história, HI no endpoint, passagens por zero/ausências, antecipação mediana/máxima, recuperações, saída do patamar assumido 21–40, monotonicidade, tendência e prognosticabilidade. No teste truncado, avaliar RMSE/MAE no último ciclo, faixas de RUL e zeros anteriores ao último ciclo; não chamar o último HI de HI terminal.

Comparar transferência direta e reajuste no MESMO teste FD003, com bootstrap pareado por motor (2.000 amostras, semente 20261016); valores negativos de RMSE_reajuste−RMSE_transferência favorecem reajuste. Comparar alternativas com MARGEM dentro do teste reajustado, separadamente. Intervalos são descritivos condicionais, não validação física ou generalização universal. Não parear motores FD001 e FD003 apenas por número identificador.

Favorável à transferência: desempenho e âncora terminal persistem sem reaprendizagem. Misto: reajuste melhora previsão, mas permanecem zeros antecipados/recuperações ou forte mudança de parâmetros. Contrário: a mesma representação falha mesmo após reajuste, ou o bom RMSE depende de HI inadequado como condição. Encerrar após os contrastes definidos, preservando resultados negativos; melhor RUL não basta para aprovar HI físico/F. Exemplos fixados antes de executar: motores FD003 1/2/3, completos e truncados.

## Validação e artefatos

Testar carregamento/reprodução dos modelos FD001, integridade de seus hashes após transferência, causalidade sob perturbação futura de sensores FD003, isolamento dos rótulos e alinhamento de RUL_FD003. Usar verificações independentes de partições, seleção, conversores e métricas; preservar CSV por motor/ciclo, modelos congelados, seleção, pesos/rankings, diagnóstico de distribuição de vidas, bootstrap, figura, relatório, versões e manifesto. Nenhuma inspeção será executada nem protocolo principal congelado por esta extensão.
