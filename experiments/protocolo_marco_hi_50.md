# P07 — previsão de F a partir de um marco intermediário de HI

Estado em 16/10/2026: especificado, não executado. Proposta do autor após P01–P06. Não é hipótese confirmatória prévia aos resultados anteriores e não define uma fórmula final de índice de saúde (HI).

## Interpretação

Usar a primeira passagem causal do HI estimado por 0,5 como marco para avaliar a previsão do endpoint original F, sem exigir que a curva observada zere exatamente em F. Não substituir F por 0,5 nem chamar esse nível de limite físico, P confirmado, ordem de remoção ou início de inspeções.

    t_i,α = inf{t≥20: Ĥ_i(t)≤α}, α=0,5
    F̂_i(t)=t+r̂_i(t | informações de sensores disponíveis até t).

Ausência de passagem é censura. HI=0,5 não implica 50% da vida restante ou confiabilidade 0,5. Para o alvo convencional de P05/P06, H*=min(1,RUL/ρ)^η, a igualdade corresponde a RUL=ρ·2^(−1/η), dependente da escala. Não usar essa identidade do alvo como validação independente da previsão.

## Primeira análise prevista

Reutilizar as curvas/predições congeladas de P05 e P06, sem novo ajuste. Separar FD001, FD003 reajustado e transferência direta; preservar os namespaces dos motores. α=0,5 é o marco central; 0,4/0,6 são sensibilidades, não níveis a selecionar pelo teste oficial. Os conjuntos já foram examinados em rodadas anteriores e permanecem exploratórios.

Para cada formulação/subconjunto/nível, reportar número de motores que atingem o marco, ciclo de disponibilidade, RUL verdadeira no marco e erro F̂−T (igual a RUL prevista menos verdadeira no mesmo ciclo). Calcular RMSE, MAE e viés condicional à disponibilidade, preservando ausências/censura. Comparações pareadas usam também a interseção de motores com marco disponível em ambas as formulações; não ocultar diferenças de cobertura por uma comparação apenas dos casos favoráveis. No teste truncado, os rótulos finais permitem calcular T, mas não inventar cruzamentos posteriores ao truncamento.

Examinar atualizações subsequentes das previsões nos ciclos observados e contrastar com prognósticos disponíveis antes do marco. A previsão não é retroativamente disponibilizada no início da janela ou de uma suposta mudança física. Avaliar recuperações/recruzamentos e sua influência na utilidade do marco; nenhuma regra de persistência será introduzida após observar seus resultados sem emenda explícita.

O conversor atual usa somente HI corrente; valores semelhantes de HI podem produzir RUL semelhante apesar de histórias diferentes. Uma primeira análise com esse conversor não demonstra individualização temporal suficiente. Uma comparação posterior com informação de trajetória exigirá especificação própria antes de ajustar novos modelos.

## Decisão e limites

Critério para avançar: evidência conjunta de disponibilidade, antecedência e qualidade de previsão do F original, com estabilidade entre motores/formulações/domínios. Um menor erro em poucos motores não demonstra melhor método. Limites aceitáveis de erro, risco e antecedência operacional continuam por fundamentar; a rodada não concede admissibilidade por construção. Se a previsão permanecer inadequada, preservar o resultado e investigar representação/conversor, sem redefinir o endpoint para obter concordância.

A adoção futura do HI deverá apoiar-se em validade da representação e utilidade prognóstica, estabilidade das contribuições dos sensores, limitações e evidência comparativa. Coincidência exata entre zero empírico e T passa a ser diagnóstico, não único requisito de adoção. O HI físico de Saxena continua sendo uma referência conceitual distinta.

Sem inspeções simuladas, sem mudança da periodicidade P–F e sem congelamento do protocolo principal. Saídas previstas: métricas individuais/agregadas de marcos, coberturas e censura, comparações em motores comuns, previsões atualizadas e rastreabilidade dos modelos originais.

## Detalhamento operacional anterior à execução de P07

Autorização de execução recebida em 16/10/2026. Sem consultar as novas métricas, fixam-se os seguintes resumos: ciclos relativos −10, −5, 0, +5, +10 e +20, somente quando observados; todas as previsões após a passagem também serão arquivadas. Para cada deslocamento, contrastar erro no marco e erro atualizado nos mesmos motores disponíveis, além de conservar a cobertura. Antes do marco, a comparação é retrospectiva, não uma regra causal de antecipação de sua ocorrência. O comparador após o marco mantém F̂ fixo no valor inicialmente previsto, cujo erro em relação a T é constante; não mantém RUL fixo.

As comparações entre famílias serão feitas na interseção dos motores: (a) nos respectivos primeiros cruzamentos, com horários potencialmente distintos; (b) num ciclo comum, o máximo dos dois ciclos de cruzamento, com sensores observados até esse ciclo. A segunda comparação controla o instante de informação; a primeira mede a prestação completa de cada marco. Comparar também transferência e reajuste FD003 para a mesma família, mantendo separados motores completos e truncados. Intervalos descritivos de 95% para diferenças de RMSE usam 2.000 reamostragens pareadas por motor, semente 20261016, sem interpretação confirmatória ou ajuste de limiar por resultado.

Reportar mediana e quartis da RUL real e prevista no marco, viés, fração de erros positivos (F previsto tarde) e retornos acima do limiar após a primeira passagem. Ausência até o fim de uma trajetória completa significa não atingimento observado, não censura de tempo de acompanhamento por truncamento; no teste oficial trata-se de ausência até o truncamento. Nenhum dos dois será imputado como passagem no endpoint. Limites de utilidade operacional continuam não estabelecidos. O artigo permanece na versão M17 nesta rodada; a evidência nova será entregue em relatório próprio e no plano.
