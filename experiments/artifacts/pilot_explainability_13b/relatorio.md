# P13.2 — explicabilidade e estabilidade após o marco

HI = índice de saúde; ISO = regressão isotônica; RF = floresta aleatória com HI e inclinação. FD001 é o cenário principal; FD003 é extensão de robustez. Três repetições dos mesmos100 motores por domínio, sem300 motores independentes.

Modelos, quantis e políticas congelados. Parâmetros das perturbações aprendidos somente em F25, sem uso de C/U/E. Trata-se de robustez informacional de medições; não valida intervenções físicas, margens operacionais ou risco populacional≤2%.

## Reconstrução e fidelidade

9.600 decisões basais reproduzidas. Atribuições assinadas e alocação radial respeitam clipping/cancelamento. Violações do sinal previsto da resposta do HI às perturbações: 0 em 14154217 comparações de sinal. Identidade algébrica não comprova utilidade humana da explicação.

## Estabilidade de rankings entre ajustes

| Domínio | Ranking | Comparações | Spearman mediano | Mínimo | Top5 compartilhado mediano | Não identificáveis |
|---|---|---|---|---|---|---|
| FD001 | contribution | 135 | 0.73 | 0.45 | 3.0 | 0 |
| FD001 | prediction_ISO | 135 | 0.72 | 0.42 | 3.0 | 0 |
| FD001 | prediction_RF_SLOPE | 135 | 0.72 | 0.42 | 3.0 | 0 |
| FD001 | sensitivity_HI | 135 | 0.72 | 0.42 | 3.0 | 0 |
| FD003 | contribution | 135 | 0.56 | 0.02 | 3.0 | 0 |
| FD003 | prediction_ISO | 135 | 0.55 | -0.02 | 3.0 | 0 |
| FD003 | prediction_RF_SLOPE | 135 | 0.56 | -0.02 | 3.0 | 0 |
| FD003 | sensitivity_HI | 135 | 0.55 | -0.02 | 3.0 | 0 |

Concordância de ranking e fidelidade são critérios distintos. Correlação indefinida não recebe valor1. Empates na fronteira top5 permanecem identificados em `rank_comparisons.csv`. Pesos globais do HI não são apresentados como importância da retirada. ISO e RF recebem o mesmo HI (com inclinação na RF): concordância de sensores após essa representação não é validação independente de importância física.

## Por que a regra conservadora atua cedo?

Auditoria no instante da decisão, sem mudar a regra. A correção q é congelada; o limite inferior é max(0, previsão−q). Quando chega a zero, variações locais da previsão podem não alterar esse limite ou o gatilho. O quadro abaixo é descritivo, não uma identificação causal do ganho recuperável.

| Domínio | Política | Decisões no marco, faixa entre repetições | Limite inferior zero na decisão, faixa | Previsão central já satisfazia o gatilho, faixa |
|---|---|---|---|---|
| FD001 | ISO_LOWER98_M15_D1 | 55–75% | 0–0% | 0–0% |
| FD001 | RF_SLOPE_LOWER98_M15_D1 | 84–88% | 26–49% | 0–0% |
| FD003 | ISO_LOWER98_M15_D1 | 72–100% | 0–0% | 0–0% |
| FD003 | RF_SLOPE_LOWER98_M15_D1 | 86–91% | 39–66% | 0–0% |

## Sensibilidade da data programada

Contraste abaixo: rampa global, amplitude1, canais perturbados individualmente, prazo1. As médias dão peso igual a direções/sinais dentro de cada motor, depois aos motores; mínimo/máximo entre repetições. Ausências permanecem na análise de presença/eventos e ficam fora somente da distância finita, com denominadores publicados.

| Domínio | Política | Média absoluta de Δr (ciclos), faixa entre repetições | Fração de deslocamentos>2, faixa | Mudança de presença, faixa |
|---|---|---|---|---|
| FD001 | AGE_D1 | 0.00–0.00 | 0.00–0.00% | 0.00–0.00% |
| FD001 | HI_MARKER_D1 | 2.17–2.26 | 34.23–35.93% | 0.00–0.00% |
| FD001 | HI_THRESHOLD_SELECTED_D1 | 1.65–1.67 | 25.40–26.74% | 0.30–0.67% |
| FD001 | HI_WAIT_SELECTED_D1 | 2.17–2.25 | 34.16–35.83% | 0.03–0.37% |
| FD001 | ISO_LOWER98_M15_D1 | 2.17–2.19 | 34.87–35.07% | 0.00–0.00% |
| FD001 | ISO_POINT_M15_D1 | 1.29–1.38 | 16.79–19.33% | 1.13–3.47% |
| FD001 | RF_SLOPE_LOWER98_M15_D1 | 2.11–2.24 | 32.17–32.87% | 0.00–0.00% |
| FD001 | RF_SLOPE_POINT_M15_D1 | 1.31–1.49 | 15.65–18.00% | 0.73–2.63% |
| FD003 | AGE_D1 | 0.00–0.00 | 0.00–0.00% | 0.00–0.00% |
| FD003 | HI_MARKER_D1 | 1.96–2.17 | 21.53–27.61% | 0.00–0.00% |
| FD003 | HI_THRESHOLD_SELECTED_D1 | 1.72–1.89 | 19.88–24.31% | 0.22–0.65% |
| FD003 | HI_WAIT_SELECTED_D1 | 1.97–2.16 | 21.54–27.37% | 0.19–0.30% |
| FD003 | ISO_LOWER98_M15_D1 | 1.95–2.17 | 21.41–27.61% | 0.00–0.00% |
| FD003 | ISO_POINT_M15_D1 | 1.32–1.34 | 18.04–20.48% | 1.27–1.84% |
| FD003 | RF_SLOPE_LOWER98_M15_D1 | 1.89–2.11 | 20.56–26.84% | 0.00–0.00% |
| FD003 | RF_SLOPE_POINT_M15_D1 | 1.20–1.49 | 12.42–16.47% | 0.95–1.20% |

Demais amplitudes, direções conjuntas, prazo2 e diagnóstico local estão em [action_summary.csv](action_summary.csv); efeitos extremos por motor também estão publicados. Diagnósticos locais alinham a rampa à decisão original de cada política e não representam a mesma intervenção no mesmo instante entre políticas diferentes.

## Suporte empírico

| Domínio | Tipo | Fração média de incrementos fora do envelope |
|---|---|---|
| FD001 | baseline | 15.97% |
| FD001 | channel | 15.97% |
| FD001 | joint | 16.00% |
| FD003 | baseline | 13.71% |
| FD003 | channel | 13.92% |
| FD003 | joint | 17.10% |

O envelope foi estimado nos incrementos iniciais F25; a própria trajetória original pode sair dele durante a degradação. Quantis0,99 por critério não dão cobertura conjunta garantida99%. Resultados no suporte possuem denominadores próprios e não substituem todos os motores. Exigir todo o prefixo dentro do envelope é diagnóstico restritivo, não filtro de segurança.

## Estabilidade entre repetições

| Domínio | Mediana de diferença absoluta entre datas | Máximo | Presença discordante |
|---|---|---|---|
| FD001 | 3.00 | 31.00 | 82/4800 pares motor/política |
| FD003 | 4.00 | 217.00 | 114/4800 pares motor/política |

Esses pares reutilizam os mesmos motores e modelos com treino parcialmente compartilhado; não são novas unidades independentes. Perfis de contribuição são comparados na interseção de instantes disponíveis em cada par, em `repeat_contributions.csv`.

## Artefatos e limites

[Contrastes pareados de datas/presença](action_contrasts.csv), [contrastes ISO/RF](forecast_contrasts.csv), [verificação](verification.json), [verificação das estatísticas](summary_verification.json), [protocolo](../../protocolo_explicabilidade_13b.md) e [convenções anteriores à execução](../../protocolo_explicabilidade_13b_implementacao.md). Bootstrap descritivo de2.000 amostras por motor/domínio/repetição, condicional aos modelos; sem selecionar o melhor explicador ou regra por intervalos.

P11.2 localizou a distância ao oráculo após o marco; P13.2 testa se essa cadeia é auditável e estável. Nenhuma resposta de sensibilidade prova que a distância possa ser recuperada com segurança. Não houve inspeção, mudança do HI ou artigo, nova política ou projeção monetária.

## Fichas retrospectivas de todos os casos especificados

- [FD001, motor1](case_FD001_u1.md)
- [FD001, motor6](case_FD001_u6.md)
- [FD001, motor8](case_FD001_u8.md)
- [FD001, motor16](case_FD001_u16.md)
- [FD001, motor19](case_FD001_u19.md)
- [FD001, motor22](case_FD001_u22.md)
- [FD001, motor23](case_FD001_u23.md)
- [FD001, motor26](case_FD001_u26.md)
- [FD001, motor32](case_FD001_u32.md)
- [FD001, motor36](case_FD001_u36.md)
- [FD001, motor39](case_FD001_u39.md)
- [FD001, motor40](case_FD001_u40.md)
- [FD001, motor56](case_FD001_u56.md)
- [FD001, motor58](case_FD001_u58.md)
- [FD001, motor62](case_FD001_u62.md)
- [FD001, motor66](case_FD001_u66.md)
- [FD001, motor68](case_FD001_u68.md)
- [FD001, motor69](case_FD001_u69.md)
- [FD001, motor70](case_FD001_u70.md)
- [FD001, motor73](case_FD001_u73.md)
- [FD001, motor75](case_FD001_u75.md)
- [FD001, motor76](case_FD001_u76.md)
- [FD001, motor77](case_FD001_u77.md)
- [FD001, motor80](case_FD001_u80.md)
- [FD001, motor84](case_FD001_u84.md)
- [FD001, motor86](case_FD001_u86.md)
- [FD001, motor91](case_FD001_u91.md)
- [FD001, motor100](case_FD001_u100.md)
- [FD003, motor4](case_FD003_u4.md)
- [FD003, motor6](case_FD003_u6.md)
- [FD003, motor8](case_FD003_u8.md)
- [FD003, motor12](case_FD003_u12.md)
- [FD003, motor13](case_FD003_u13.md)
- [FD003, motor14](case_FD003_u14.md)
- [FD003, motor15](case_FD003_u15.md)
- [FD003, motor20](case_FD003_u20.md)
- [FD003, motor24](case_FD003_u24.md)
- [FD003, motor31](case_FD003_u31.md)
- [FD003, motor38](case_FD003_u38.md)
- [FD003, motor41](case_FD003_u41.md)
- [FD003, motor42](case_FD003_u42.md)
- [FD003, motor43](case_FD003_u43.md)
- [FD003, motor44](case_FD003_u44.md)
- [FD003, motor45](case_FD003_u45.md)
- [FD003, motor48](case_FD003_u48.md)
- [FD003, motor55](case_FD003_u55.md)
- [FD003, motor56](case_FD003_u56.md)
- [FD003, motor57](case_FD003_u57.md)
- [FD003, motor58](case_FD003_u58.md)
- [FD003, motor59](case_FD003_u59.md)
- [FD003, motor62](case_FD003_u62.md)
- [FD003, motor67](case_FD003_u67.md)
- [FD003, motor68](case_FD003_u68.md)
- [FD003, motor69](case_FD003_u69.md)
- [FD003, motor71](case_FD003_u71.md)
- [FD003, motor76](case_FD003_u76.md)
- [FD003, motor77](case_FD003_u77.md)
- [FD003, motor78](case_FD003_u78.md)
- [FD003, motor80](case_FD003_u80.md)
- [FD003, motor82](case_FD003_u82.md)
- [FD003, motor84](case_FD003_u84.md)
- [FD003, motor89](case_FD003_u89.md)
- [FD003, motor92](case_FD003_u92.md)
- [FD003, motor95](case_FD003_u95.md)
- [FD003, motor99](case_FD003_u99.md)
- [FD003, motor100](case_FD003_u100.md)
