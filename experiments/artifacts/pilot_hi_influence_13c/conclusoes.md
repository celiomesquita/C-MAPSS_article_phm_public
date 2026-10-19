# P13.3 — influência da aprendizagem do HI

## Resposta atual

A instabilidade de FD003 tem um mecanismo verificável na aprendizagem da representação. Não decorre apenas do conversor RUL ou da proximidade de um limiar. Na repetição 2 do caso55, a exclusão de13 dos25 motores F inverte simultaneamente a orientação aprendida dos sensores s7, s12, s15, s20 e s21. O marco passa de239 para443–452 (deslocamento204–213). Reaprender somente os coeficientes, mantendo o pré-processamento basal, leva esse marco a223–325. A orientação é estimada pelo sinal da mediana do desvio terminal: nesses cinco canais, F25 contém sinais divididos em12/13 motores. A retirada de uma observação pode inverter essa mediana e, com coeficientes não negativos, alterar o conjunto de combinações admissíveis dos sensores.

Essa inversão não demonstra que um sensor físico tenha mudado de mecanismo ou que os grupos de sinais sejam rótulos observados de falha de fan/HPC. A heterogeneidade de FD003 é explicação plausível, ainda não demonstrada causalmente. Não escolhemos a orientação que produz a curva mais favorável no motor55.

## Desenho executado

[Protocolo](../../protocolo_influencia_hi_13c.md) escrito antes da execução. Reproduzidos600 marcos,60 geometrias de ajuste,150 exclusões de motores F e300 ajustes diagnósticos (coeficientes com estatísticas fixas versus reaprendizagem completa). Avaliados os dez motores E de cada uma das seis partições dos casos, totalizando3.000 respostas pareadas dependentes. Nenhum arquivo RUL ou teste oficial foi lido por esta rodada. Alvos T−t vieram exclusivamente dos motores F para os ajustes. As trajetórias E são usadas para diagnóstico exploratório, nunca para escolher/adoptar uma variante.

Seleção de extremos previamente especificada: maior amplitude do primeiro HI≤0,5 entre três repetições, com ausências separadas. FD001: motor83, marcos228/204/222, amplitude24. FD003: motor55,451/239/396, amplitude212. O extremo FD001 aqui é do marco, não necessariamente o mesmo extremo de uma política com RUL. Todos os600 marcos estavam presentes; nenhuma exclusão gerou ausência nas3.000 respostas.

## Magnitude e alcance

| Domínio | Reajuste | Mediana absoluta, ciclos | Percentil95, ciclos | Máximo, ciclos |
|---|---|---:|---:|---:|
| FD001 | coefficients | 0 | 2.55 | 10 |
| FD001 | full | 0 | 3.00 | 10 |
| FD003 | coefficients | 0 | 8.00 | 179 |
| FD003 | full | 1 | 21.00 | 213 |

Cada linha resume750 respostas dependentes:25 exclusões × dez motores externos × três partições do caso. Não é uma estimativa populacional de estabilidade. Em FD001, no próprio motor83, os maiores deslocamentos absolutos foram4/5/10 ciclos nas repetições. No motor55 FD003, foram2/86/179 com coeficientes e2/213/179 com ajuste completo. Na repetição3, o deslocamento179 aparece mesmo mantendo o pré-processamento: estabilizar apenas a orientação não resolveria toda a sensibilidade observada.

As médias descritivas do RMSE entre curvas HI basais/reajustadas foram0,00413/0,00429 em FD001 e0,00934/0,02665 em FD003 (coeficientes/completo). Essas médias não substituem os extremos: no motor55/repetição2, os reajustes completos com inversão de orientação alteram substancialmente a curva, não apenas um cruzamento quase tangente.

## Geometria e solução numérica

As60 matrizes ponderadas têm posto de coluna completo segundo tolerância relativa1e−12. Condição espectral:48,84–76,03 em FD001 e73,22–108,45 em FD003. Com a penalização M18, FD001 passa a13,68–14,35; FD003 mantém a condição, pois ridge=0. Nas colunas ativas, as condições variam24,78–68,02 e11,66–51,49, respectivamente. Esses resultados não sustentam atribuir o caso a deficiência exata de posto ou falha de convergência. A unicidade do minimizador para uma matriz fixa não implica estabilidade perante mudança da amostra, canais ou orientação.

A verificação independente reconstruiu600 marcos via caminho público original e3.000 respostas diretamente dos sensores e pesos efetivos salvos; conferiu perdas e penalizações dos300 ajustes e as condições de Karush–Kuhn–Tucker (KKT), com violação máxima5,39×10⁻¹⁵. As cinco provas automatizadas passaram antes da execução. Todos os objetivos com estatísticas fixas melhoraram ou conservaram o objetivo basal no mesmo F24. Objetivos de variantes com escalas/orientações diferentes não foram tratados como um único problema de optimização.

## Consequência e próxima decisão

P13.3 está concluída como diagnóstico exploratório com resultado misto: estabilidade local muito maior em FD001; em FD003, influência de composição e descontinuidade da orientação mediana demonstradas nestes casos. M18 permanece a referência e todos os modelos/políticas P10–P13.2 permanecem intactos. Não há nova fórmula, redução de reserva, validação do risco≤2%, inspeção ou ganho financeiro resultante desta rodada.

O próximo experimento deverá pré-especificar alternativas para estabilizar a orientação e os coeficientes exclusivamente em desenvolvimento, com reamostragem por motor e controle M18, antes de recalibrar conversores e incerteza. A análise deve confrontar estabilidade do marco, fidelidade ao alvo e perda decisória, sem adoptar simplesmente a curva mais estável. A hipótese de mistura de trajetórias exige diagnóstico próprio; não usar rótulos físicos não distribuídos. U/E já examinados não podem confirmar a alternativa escolhida. Confirmar risco populacional permanece uma necessidade de evidência independente.

## Artefatos e limites

`baseline_markers.csv`, `marker_ranges.csv`, `cases.csv`, `spectra.csv`, `refits.csv`, `weights.csv`, `effects.csv`, `summary.csv`, `case_responses.csv`, `preprocessing_changes.csv`, `terminal_direction_evidence.csv`, `verification.json`, `deep_verification.json`, duas figuras e fontes arquivadas. O verificador aprofundado e este relatório foram acrescentados depois da execução para conferir e interpretar os resultados; não alteraram o protocolo ou ajustaram modelos. Hashes iniciais e manifesto final preservam essa precedência.

![Caso55 FD003](case_FD003_55.png)

![Caso83 FD001](case_FD001_83.png)
