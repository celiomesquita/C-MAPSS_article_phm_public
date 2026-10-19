# P13.4 — comparação de estabilização do HI em desenvolvimento

Especificado antes da execução em 17/10/2026, após autorização do autor para prosseguir de P13.3. Estudo exploratório de RQ6/RQ7. Não substitui M18, não congela o protocolo principal e não confirma risco populacional.

## Pergunta e alternativas

A remoção da orientação mediana descontínua e/ou maior regularização melhora a estabilidade da aprendizagem sem perder fidelidade ao alvo supervisionado e utilidade decisória? P13.3 mostrou influência da orientação e dos coeficientes. Não se presume que uma única orientação física descreva os mecanismos de FD003.

Manter média causal15, referência individual no ciclo20, canais com variabilidade inicial>10⁻⁶, escalas do ajuste, tau/gamma M18 por domínio e HI=clip(1−dano,0,1). Comparar cinco alternativas predefinidas:

| ID | Orientação e restrição | Penalização quadrática λ |
|---|---|---|
| M18 | Mediana terminal e coeficientes não negativos | 0,1 FD001; 0 FD003 |
| NNLS_01 | Igual a M18 | 0,1 |
| NNLS_1 | Igual a M18 | 1 |
| SIGNED_01 | Sem orientação terminal, coeficientes assinados | 0,1 |
| SIGNED_1 | Sem orientação terminal, coeficientes assinados | 1 |

NNLS é mínimos quadrados não negativos. SIGNED conserva os canais elegíveis pela variabilidade inicial e escala, sem excluir um canal por mediana terminal zero. Coeficientes assinados não são interpretados como importância física causal. M18 e NNLS_01 são deliberadamente idênticos em FD001: controle de implementação e ablação comum entre domínios. Não incluir mais candidatos depois de observar os resultados.

Objetivo: média, por motor de ajuste, do erro quadrático do dano linear não saturado em relação a 1−min(1,(T−t)/tau)^gamma, mais λ||β||². Preprocessamento completo refeito após cada exclusão; não congelar as escalas ou direções para favorecer uma variante. O cálculo por momentos suficientes poderá acelerar os ajustes se reproduzir as equações e os ajustes originais, com conferência numérica independente.

## Separação e orçamento

Reutilizar as60 partições externas P10: F25/C15/U50/E10, três repetições e dez dobras em cada domínio. D=F∪C tem40 motores. Dentro de cada D, reutilizar exatamente os quatro blocos V10 e F25 (cinco restantes sem uso naquela dobra interna) de P13.1. Assim, cada motor de D é validado uma vez por partição externa. Nenhum U/E entra no ajuste, escolha, cálculo de métricas ou figuras desta rodada. Os dados já examinados não são confirmação independente; a exclusão de U/E nesta etapa não apaga o histórico de uso.

Em cada uma das240 dobras internas, ajustar as cinco variantes em F25 e em cada um dos25 F24 obtidos por exclusão individual:31.200 soluções, incluindo o controle duplicado em FD001. Avaliar todas em V10. São12.000 observações basais de motor/modelo e300.000 respostas de exclusão dependentes, não unidades independentes. Rastrear as identidades e preservar ausências de cruzamento, ausência de decisão e denominadores.

## Métricas e seleção interna predefinida

Medir erro quadrático do HI saturado contra o alvo de HI em V, com peso igual por motor; primeiro HI≤0,5 e primeiro marco utilizável max(39,cruzamento), somente enquanto t<T. Para cada exclusão, medir RMSE da mudança da curva, diferenças de marco finitas e discordância de presença. Para o controle de decisão pelo marco, calcular retirada nos prazos1/2, chegada exata, ultrapassagem estrita, ausência e vida aproveitada min(retirada,T). Isso não aplica conversores antigos ao HI novo e não estima o risco de uma nova política de RUL.

Para cada D40, agregar seus40 motores V, sem usar U/E. Alternativa elegível deve: (i) ter40 decisões basais; (ii) não exceder as chegadas compostas do M18 em nenhum prazo; (iii) ter MSE médio basal≤1,05×M18; (iv) não aumentar o número de discordâncias de presença entre F25/F24 nem o número de decisões ausentes nas exclusões; (v) não aumentar o percentil95 absoluto das diferenças finitas do marco. O limite5% é tolerância metodológica exploratória, não margem física certificada. Publicar todos os candidatos e métricas, inclusive inelegíveis.

Entre elegíveis e M18 (referência de contingência), ordenar por percentil95 da mudança absoluta, média absoluta, MSE e ordem fixa M18/NNLS_01/NNLS_1/SIGNED_01/SIGNED_1. M18 permanece se não houver melhora nesta ordenação; indicar se M18 falhou os requisitos de completude/chegadas. Sem imputar ausência como estabilidade zero: se não houver pares finitos, a estatística é indefinida e o candidato é inelegível. Não exigir redução do máximo como critério oculto; relatá-lo e discutir casos em que a cauda piore apesar da seleção.

Congelar60 indicações internas antes de qualquer uso posterior de U/E. Ajustar apenas o HI indicado em cada F25 externo, salvando60 modelos e a proveniência de seleção D40; não avaliar esses modelos em C/U/E nem chamá-los de operacionais. C participou da escolha, portanto não será anunciado como avaliação independente se depois ajustar conversores. Qualquer comparação posterior de remoção deverá reaprender conversores, recalibrar em U50 e avaliar por motor, com protocolo próprio e consciência do caráter exploratório dos dados existentes.

## Interpretação e parada

Resultado favorável: menor sensibilidade com erro/decisão preservados nas validações internas. Resultado misto: ganho de estabilidade acompanhado de perda de alvo, cobertura, vida ou cauda; não ocultá-lo pela escolha. Resultado nulo/contrário: alternativas não melhoram M18 sob os critérios ou produzem ausência/underfitting; conservar M18 e registrar o limite. A seleção interna é candidata, não prova de generalização nem de risco≤2%. Nenhuma inspeção, redução de reserva, projeção de20anos ou alteração de resultados anteriores. Não expandir a grade até conseguir sucesso.

Salvar fontes pré-execução, versões, hashes de insumos/artefatos anteriores, partições, pesos/estatísticas de todos os ajustes, métricas por motor, seleção, modelos indicados, verificação e relatório em `artifacts/pilot_hi_stabilization_13d`.
