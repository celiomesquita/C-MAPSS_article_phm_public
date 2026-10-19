# P18.1 — normalização por condição operacional, especificada e testada sem abrir FD002 e FD004

Especificado em 18/10/2026 antes da execução, por escolha do autor de tratar a normalização por condição operacional como o primeiro ponto pendente do congelamento. Exploratório. FD002 e FD004 continuam intocados: o procedimento é fixado agora e executado neles só na confirmação.

## Problema

FD002 e FD004 têm seis condições de voo (altitude 0–42 mil pés, Mach 0–0,84, TRA 20–100; Saxena et al., 2008, seção V), que mudam de ciclo para ciclo e deslocam os sensores muito mais que a degradação. O HI do M18 usa a média causal de 15 ciclos e a referência de cada motor no ciclo 20; com regimes aleatórios por ciclo, essa referência e a escala dos sensores misturam regime e degradação. FD001 e FD003 têm uma só condição e não permitem testar o procedimento nos dados reais.

## Procedimento a congelar

Etapa que precede o pré-processamento de M18, sem alterá-lo:

1. **Regime por ciclo, só com as configurações operacionais.** Padronizar (op1, op2, op3) com média e desvio dos motores de ajuste F e ajustar K-médias com K = 6 (o número de condições documentado), 20 inicializações e semente fixa, somente nos motores F de cada partição. O regime c(t) de um ciclo é o centro mais próximo da configuração observada nesse ciclo; é causal e não usa sensores nem vida.
2. **Linha de base saudável por regime e sensor.** Para cada sensor j e regime c, média m_{j,c} e desvio s_{j,c} dos valores brutos dos ciclos 1 a 20 dos motores F cujo regime nesse ciclo é c. Se s_{j,c} < 10⁻⁹, usar 1.
3. **Sensor normalizado.** x̃_{ij}(t) = (x_{ij}(t) − m_{j,c(t)})/s_{j,c(t)}.
4. O pipeline de M18 (média causal de 15 ciclos, referência no ciclo 20, canais, direções, pesos não negativos, conversores, margem de 98%) roda **sem mudança** sobre x̃, com parâmetros reaprendidos por domínio e partição como em P05 e P06.

K-médias, centros, médias e desvios são ajustados em F, aplicados a C, U e E sem reajuste. Os diagnósticos do agrupamento (coeficiente de silhueta nas configurações de F, tamanho dos grupos, estabilidade entre sementes) são relatados na confirmação e **não** autorizam troca do procedimento depois de ver os resultados.

Limitação conhecida: o procedimento remove deslocamentos e escalas de regime por sensor, mas não a **interação regime × degradação** (a sensibilidade dos sensores à degradação varia com a condição). Uma normalização residual por regime não a corrige.

## Verificação antes do congelamento (somente FD001)

- **T1, equivalência de regime único.** Com K = 1 o procedimento é um deslocamento e uma escala por sensor, e o HI do M18 é invariante a isso, salvo os limiares absolutos de elegibilidade de canais (σ > 10⁻⁶ e limite > 3σ + 10⁻⁶), que dependem da escala. Aplicar K = 1 a FD001 nas dez dobras de P10 (repetição 1) e comparar HI e previsões com os originais. Divergências, se houver, serão atribuídas à elegibilidade.
- **T2, teste sintético multi-regime em FD001.** Construir regimes sintéticos sobre as trajetórias reais de FD001: seis centros de configuração operacional sorteados (semente fixa) dentro das faixas de Saxena, regime iid uniforme por ciclo e, por sensor e regime, um deslocamento aditivo b_{j,c} ~ N(0, (3·σ_j)²) e um fator multiplicativo a_{j,c} ~ U(0,9; 1,1), em que σ_j é o desvio do sensor sobre todas as linhas de FD001. Variantes sobre as mesmas partições: **V0** FD001 original (referência); **V1** sintético sem normalização; **V2** sintético com o procedimento (K-médias); **V3** sintético com rótulos verdadeiros de regime (isola erro de agrupamento). Os efeitos são afins e iid por ciclo; o teste não representa a interação regime × degradação nem o acoplamento real entre condições e sensores do C-MAPSS.
- **Medidas** em E10 por dobra, agregadas nos 100 motores da repetição: disponibilidade do marco (cruzamento do HI por 0,5), RMSE da RUL prevista no marco, RMSE por motor nos ciclos após o marco, correlação de Spearman entre HI e RUL verdadeira. Os resultados são descritivos; a única regra pré-declarada é a heurística de que V2 "restaura" a referência quando seu RMSE no marco fica a até 10% do de V0.

## Interpretação prévia

- Se V1 ficar muito pior que V0, a normalização é necessária no teste sintético; se V2 ≈ V0 e V3 ≈ V2, o procedimento remove os efeitos afins de regime que o teste injetou. Isso é condição necessária e não suficiente para o desempenho em FD002 e FD004.
- O resultado não valida o procedimento nos dados reais. Ele só cria uma regra fixa e testada nos limites do que FD001 permite, antes de abrir FD002 e FD004.

## Artefatos e verificação

Módulo `regime_normalisation.py`; runner `pilot_regime_synthetic_18a.py`; testes antes da execução (K = 1 invariante em dados sintéticos de regime único, K-médias recupera regimes bem separados, normalização remove deslocamentos afins conhecidos, causalidade, uso apenas de F no ajuste, sem leitura de FD002/FD004); verificador independente por reimplementação em NumPy das médias e desvios por regime e do deslocamento sintético. Saídas em `artifacts/pilot_regime_synthetic_18a`.
