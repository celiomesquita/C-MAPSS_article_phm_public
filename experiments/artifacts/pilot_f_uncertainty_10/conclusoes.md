# Interpretação científica de P10 — 17/10/2026

**A calibração finita de 98% foi viável, mas ainda não sustenta a regra de remoção nem a redução da reserva para 12 ciclos.** A cobertura unilateral e a antecedência disponível variaram por domínio, modelo e divisão. Mantêm-se a forma HI adotada em M18 e o isotônico como controle. Não houve escolha de política, remoção ou inspeção simulada.

## Evidência primária

Sessenta partições F25/C15/U50/E10, em três repetições de dez dobras por domínio. Cada repetição avalia os mesmos 100 motores completos uma vez; não são 300 motores independentes. Todos os 100 motores de avaliação cruzaram o marco HI≤0,5 com atributos disponíveis em cada repetição. Os valores abaixo são amplitudes entre repetições, não intervalos de confiança.

| Domínio | Conversor | Cobertura bilateral da trajetória | Cobertura unilateral da trajetória | Largura mediana, ciclos | Antecedência mediana L−t no marco, ciclos | Colapso de L em t no marco |
|---|---|---|---|---|---|---|
| FD001 | Isotônico | 99–100% | 98–99% | 63,93–66,36 | 13,00–15,70 | 0% |
| FD001 | RF temporal | 97–99% | 97–100% | 61,74–65,16 | 1,78–7,44 | 26–46% |
| FD003 | Isotônico | 98–100% | 95–99% | 68,46–72,64 | 11,00–14,00 | 0% |
| FD003 | RF temporal | 98–99% | 95–99% | 66,90–77,99 | 0,00–1,92 | 39–65% |

Cobertura unilateral significa L(t)≤T em todos os ciclos observados desde o marco, com L=max(t,F̂−q_late). Não é taxa de remoção antes de T. As coberturas bilateral e unilateral têm escores diferentes; uma cobertura bilateral elevada não assegura cobertura unilateral igualmente elevada. Resultados abaixo de 98% em uma divisão finita não refutam, por si, uma propriedade marginal sob intercambiabilidade, mas impedem alegar estabilidade empírica do alvo em todos os cenários.

## Reserva e execução: informação disponível

Com o diagnóstico L−t≥m+d, reserva de 15 e execução de dois ciclos, a informação no marco permitiu acomodar os 17 ciclos em **14–35% dos motores FD001 com isotônico**, e **0–26% em FD003**. Na RF temporal: 11–14% e 7–13%, respectivamente. Com reserva de 12 e execução de dois ciclos, essas frações foram 41–69%/30–52% no isotônico e 17–22%/11–18% na RF temporal, em FD001/FD003.

Reduzir m torna esse diagnóstico mais frequente por construção; isso não demonstra redução da incerteza ou admissibilidade da mudança. O diagnóstico não agenda retirada, não adopta o limite inferior como âncora da reserva e não escolhe m ou d. A referência F̂ versus L e o critério observável de incerteza elevada permanecem abertos. Exigir reserva adicional ao limite conservador poderá ser excessivo; esse efeito deve ser distinguido da simples possibilidade de executar uma retirada com antecedência de um ou dois ciclos.

## Instabilidade que deve permanecer visível

No marco, o RMSE isotônico variou 15,44–17,54 ciclos em FD001 e 16,75–36,58 em FD003; na RF temporal, 13,25–17,13 e 16,92–33,83. Os seis intervalos descritivos pareados de diferença RF−isotônico incluíram zero. Não há superioridade conclusiva nesses contrastes.

Na segunda repetição FD003, o motor 55 cruzou o marco no ciclo 239, com endpoint 525 e RUL real 286. O isotônico previu 37,21 ciclos restantes (erro −248,79); a RF temporal, 54,96 (erro −231,04). O motor 71 também contribuiu com erros elevados. São observações mantidas, sem exclusão retrospectiva, ajuste da fórmula ou seleção de semente. O valor HI=0,5 não individualiza uniformemente a vida restante. As diferenças para P09 não isolam o tamanho de U: F e C também diminuíram e E mudou.

Em três ajustes FD003, o motor 10 de U não cruzou o marco, ficando n=49 em vez de 50; o quantil corrigido ainda foi finito. Todos os outros ajustes tiveram n=50. Ao nível 98%, o quantil foi sempre o máximo disponível, portanto sensível a observações extremas. Os motores sem marco não foram imputados. Nos testes oficiais truncados, somente 29–30/100 motores FD001 e 23–27/100 FD003 disponibilizaram o marco; seus resultados são condicionais e exploratórios.

## Verificação e emenda numérica

A reconstrução inicial identificou arredondamento em comparações exatamente no limiar m+d. Explicitou-se tolerância de 10⁻⁹ ciclo e recalculou-se somente o diagnóstico a partir de previsões congeladas. Nenhuma classificação no marco ou na trajetória mudou; diferenças nas frações de ciclos foram inferiores a 2×10⁻¹⁶. Versões originais, divergência e fontes executadas foram preservadas; não houve reajuste ou alteração de quantis, bandas e contrastes. [Registro da emenda](amendment_numeric_boundary.json).

## Decisão e limites

P10 respondeu à viabilidade numérica de calibrar 98% com um grupo exclusivo maior e mostrou o custo em antecedência. Não respondeu se uma política satisfaz ultrapassagem ≤2% por motor, nem validou voo além de margens físicas. O conjunto termina no endpoint e nenhum sensor pós-T foi criado. Nenhuma versão da reserva foi escolhida pelos resultados e o protocolo principal continua aberto.

O próximo experimento decisório precisa especificar a âncora da reserva, o tratamento quando a antecedência disponível é insuficiente e um critério observável para incerteza elevada. Deve separar reserva, correção de incerteza e execução, aferir a retirada efectiva por motor e distinguir chegada a T de ultrapassagem. A explicabilidade deve abranger esses componentes e a instabilidade individual, não apenas a importância média das features. Inspeções permanecem posteriores ao congelamento. Não há motivo para retomar uma busca irrestrita de HI perfeito; a instabilidade observada deve ser tratada como limitação da cadeia prognóstica e examinada na sua consequência decisória.

Evidências completas: [relatório](relatorio.md), [verificação](verification.json), [protocolo](../../protocolo_incerteza_f_10.md), [métricas por motor](bands.csv), [antecedência por motor](reserves.csv) e [manifesto](manifest.json). O plano executivo foi atualizado; o artigo permanece na versão M17, sem incorporar esta rodada.
