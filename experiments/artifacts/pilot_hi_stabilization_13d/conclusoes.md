# P13.4 — estabilização do HI em desenvolvimento

## Resultado e alcance

A comparação produziu indicações internas mais estáveis segundo o critério previamente fixado, sobretudo em FD003. É um resultado misto: a seleção não protegeu todos os máximos individuais, depende da partição e manteve um caso de referência incompleta. M18 continua sendo o controle de trabalho; nenhuma alternativa foi declarada superior em U/E ou adoptada como política operacional.

| Domínio | Mediana entre partições do p95 absoluto, ciclos | Mediana da média absoluta, ciclos | Maior máximo observado, ciclos | Partições com máximo pior |
|---|---:|---:|---:|---:|
| FD001 | 2.00 → 2.00 | 0.542 → 0.418 | 15 → 15 | 8 |
| FD003 | 5.00 → 3.00 | 1.229 → 0.627 | 223 → 45 | 3 |

Os deslocamentos são do primeiro HI≤0,5 após excluir um motor do ajuste, avaliados em motores V internos. As medianas referem-se às30 partições D40 de cada domínio; o maior máximo é o extremo sobre essas partições. Cada D contém40 motores repetidamente utilizados em diferentes divisões. Não são30 populações independentes ou uma estimativa de risco de falha. O máximo223 de FD003 nesta comparação interna é diferente do213 observado no caso externo de P13.3; não se comparam os dois como antes/depois no mesmo motor.

## Protocolo executado

[Protocolo prévio](../../protocolo_estabilizacao_hi_13d.md): cinco alternativas (M18; não negativa com λ0,1/1; assinada com λ0,1/1),240 dobras internas e31.200 soluções, incluindo o controle duplicado de FD001. Cada dobra interna usaF25/V10, com cinco motores D restantes não usados. Cada exclusão reaprendeu canais, escalas e, quando aplicável, orientação. Calcularam-se12.000 respostas basais e300.000 respostas de exclusão; nenhuma representa um novo motor independente. Leram-se somente os arquivos train; nenhum arquivo RUL/test oficial foi utilizado. Os alvos supervisionados vieram de T−t.

Somente D=F∪C participou da aprendizagem/seleção. U/E não foram pontuados, usados para escolher, ou incluídos nas figuras. Isso não elimina o uso exploratório anterior dos dados do projeto. Após congelar as60 indicações, foram ajustados60 HIs em F25 externo, sem lhes aplicar conversores/quantis antigos. C participou da seleção; seu eventual uso posterior para ajustar conversores será explicitado, sem apresentá-lo como avaliação independente.

## Escolhas internas e compromissos

Elegibilidade exigiu completude basal, chegadas compostas não superiores a M18 em ambos os prazos, MSE basal≤1,05×M18, sem aumento de discordâncias de presença ou ausências após exclusão e p95 não superior. Entre elegíveis e a referência de contingência, minimizaram-se p95, média absoluta, MSE e ordem fixa. Não se acrescentou proteção do máximo depois de observar os resultados.

| Domínio | Variante indicada | Partições, de30 |
|---|---|---:|
| FD001 | M18 | 2 |
| FD001 | NNLS_1 | 3 |
| FD001 | SIGNED_01 | 2 |
| FD001 | SIGNED_1 | 23 |
| FD003 | M18 | 3 |
| FD003 | NNLS_01 | 9 |
| FD003 | NNLS_1 | 1 |
| FD003 | SIGNED_01 | 7 |
| FD003 | SIGNED_1 | 10 |

FD001: a razão MSE indicado/M18 variou0,905–1,049 (mediana0,994). FD003:0,710–1,048 (mediana1,000). Portanto, parte da estabilidade foi aceita com até cerca de5% de perda no alvo de HI, conforme tolerância exploratória prévia; não se trata de margem de engenharia validada. O controle M18/NNLS_01 foi exatamente idêntico em FD001.

A vida média aproveitada pelo controle de remoção no marco, prazo1, mudou−0,375 a+3,375 ciclos em FD001 (mediana+2,425) e−0,850 a+11,275 em FD003 (mediana+1,338), entre D40. São diferenças internas no controle simples de marco, não resultados do conversor RUL, custo de renovação, lucro empresarial ou efeito em20anos.

**Resultado adverso preservado:** o máximo de deslocamento piorou em8/30 partições FD001 e3/30 FD003, mesmo com melhora/empate do p95. Logo, reduzir uma medida agregada não demonstra estabilidade uniforme. O relatório mantém todas as variantes, inclusive as inelegíveis, e o máximo não será usado retrospectivamente para trocar as escolhas já congeladas.

**Contingência não elegível:** FD003/repetição2/dobra2 manteve M18: apenas39/40 decisões basais e uma ausência contabilizada como chegada composta em ambos os prazos. Nenhuma alternativa satisfez os filtros. Essa indicação é diagnóstico/contingência, não um ajuste aprovado. Nas30 partições indicadas FD003 houve1.199/1.200 decisões internas e26 ausências de decisão nas exclusões, com denominadores dependentes. As escolhas FD001 tiveram1.200/1.200 e nenhuma ausência nas exclusões. Não houve ultrapassagem estrita basal nas escolhas, mas isso não certifica o limite populacional≤2%.

## Verificação e rastreabilidade

Sete testes passaram antes da execução: reprodução M18 em ambos os domínios, equivalência ridge com todas as linhas, pesos iguais por motor, separação interna, barreira de erro na escolha, ausência sem imputação e controle duplicado. Os240 ajustes M18 internos foram ainda confrontados com os modelos originais P13.1 durante a execução.

A conferência independente reconstruiu312,000 respostas a partir das linhas originais, estatísticas e pesos, refez as300 métricas e60 escolhas e verificou optimalidade das31,200 soluções (violação KKT máxima6.731e-15). Outra conferência verificou os60 ajustes finais somente em F25, com máximo3.574e-16, e a integridade dos artefatos anteriores.

O verificador sequencial pré-especificado foi interrompido para substituir a repetição de operações tabulares por uma reconstrução vetorizada independente de mesmo escopo. O código inicial e o log parcial foram preservados; não houve mudança dos critérios científicos, modelos, seleções ou resultados. A versão vetorizada e a conferência adicional dos modelos finais foram acrescentadas depois da execução, antes deste relatório. Manifestos e fontes preservam essa ordem.

## Consequência para o plano

P13.4 conclui esta grade exploratória, com59 indicações elegíveis e uma contingência inelegível. Não expandir a grade até obter estabilidade perfeita. O próximo teste deve avaliar a consequência decisória da seleção interna: reconstruir conversores compatíveis com cada HI indicado, recalibrar em U50 e comparar com M18 sob os mesmos prazos1/2, reserva15 e tolerância experimental de ultrapassagem≤2%, sem escolher novamente em U/E. Definir antes da execução como preservar a contingência inelegível e reportar a cauda agravada. Reserva12 permanece sensibilidade condicionada, não redução autorizada pela estabilidade.

Essa avaliação poderá indicar se a estabilidade interna se transfere para marcos, previsões, remoção e exposição. Não sabemos ainda se o extremo externo do motor55 foi corrigido. Os dados existentes continuam exploratórios; evidência independente de risco e plausibilidade física permanece distinta. Sem inspeções, alteração do artigo ou projeção monetária nesta rodada.

![Comparação de estabilidade e caudas](stability_comparison.png)
