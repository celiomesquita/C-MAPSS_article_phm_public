# P18.1 — normalização por condição operacional: teste sintético em FD001

## Resultado e alcance

O procedimento de normalização por regime (protocolo `protocolo_normalizacao_regimes_18a.md`) ficou especificado e foi testado só em FD001. FD002 e FD004 não foram lidos. O teste é condição necessária e não suficiente: ele mostra que o procedimento remove deslocamentos e escalas de regime injetados, não que funcione nos dados reais de seis condições.

**Procedimento a congelar:** (1) regime por ciclo pelo centro de K-médias (K = 6) mais próximo das configurações operacionais padronizadas, ajustado nos motores F; (2) média e desvio de cada sensor por regime nos ciclos 1 a 20 dos motores F; (3) sensor normalizado x̃ = (x − m)/s por regime; (4) pipeline do M18 inalterado sobre x̃, com parâmetros reaprendidos por domínio e partição.

## T1: equivalência de regime único (FD001 real, dez dobras de P10, repetição 1)

Com K = 1 o HI e as previsões coincidem com o pipeline original em todas as dobras: mesmas linhas, diferença máxima de HI nula, diferença máxima de RUL prevista entre 2×10⁻⁹ e 8,9×10⁻⁸ ciclo, 14 canais retidos nos dois casos (a elegibilidade de canais, dependente da escala, não mudou). A normalização não perturba o M18 quando há um só regime.

## T2: teste sintético multi-regime (FD001 com seis regimes injetados, 100 motores)

| Variante | Disponibilidade do marco | RMSE no marco (ciclos) | Viés | RMSE após o marco | Spearman HI × RUL |
|---|---:|---:|---:|---:|---:|
| V0 FD001 original (referência) | 100% | 16,14 | −0,89 | 10,01 | 0,992 |
| V1 sintético sem normalização | 73% | 26,86 | −3,83 | 16,56 | 0,755 |
| V2 sintético, K-médias | 100% | 16,36 | −1,17 | 10,10 | 0,992 |
| V3 sintético, regimes verdadeiros | 100% | 16,36 | −1,17 | 10,10 | 0,992 |

- **Sem normalização o pipeline degrada** (disponibilidade do marco 73%, RMSE no marco +66%, Spearman 0,755): a normalização é necessária no teste.
- **Com normalização o desempenho volta ao da referência** (RMSE no marco 1,4% acima de V0, dentro da heurística de 10% declarada antes).
- **V2 = V3.** O agrupamento recuperou os regimes sem erro (índice de Rand ajustado 1,00 e silhueta 0,97 em todas as dobras; menor grupo com 777 a 848 ciclos), então o erro de agrupamento não explica diferença alguma.

## Limitações (o que este teste não prova)

- Regimes sintéticos com centros bem separados e iid por ciclo, e efeitos aditivos e multiplicativos por sensor e regime. O agrupamento perfeito é consequência do desenho, não evidência sobre FD002 e FD004, cujas configurações têm ruído e podem não separar tão bem.
- **A interação entre regime e degradação** (a sensibilidade dos sensores à degradação depende da condição) não está representada nem é corrigida pelo procedimento. É o principal risco para a confirmação.
- K = 6 vem da documentação; os diagnósticos de agrupamento serão relatados na confirmação e não autorizam trocar o procedimento depois de ver os resultados.
- O procedimento reaprende parâmetros por domínio e partição; o desempenho de transferência direta de FD001 para os regimes de FD002 e FD004 não foi examinado.
- Os efeitos sintéticos usam apenas FD001. A magnitude do deslocamento (3 desvios totais do sensor) foi escolhida por mim; outros valores não foram varridos.

## Verificação

Oito testes passaram antes da execução (regimes recuperados, linha de base padronizada por regime, remoção dos efeitos injetados, transformação linha a linha e causal, K = 1, reprodutibilidade, sensores constantes intactos e ausência de referências a FD002 e FD004 nos scripts). O verificador independente regenerou o conjunto sintético com a mesma semente (somas de sensores, configurações e regimes iguais, deslocamentos e fatores idênticos), recalculou a normalização por regime de 21 sensores e seis regimes com NumPy, refez as tabelas de resumo e conferiu os manifestos anteriores. Sem emendas.
