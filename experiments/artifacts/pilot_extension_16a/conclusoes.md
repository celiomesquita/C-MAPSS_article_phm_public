# P16.1 — extensão da vida pelo PHM acima do limite de 127 ciclos

## Resultado e alcance

Proposta do autor: sem dados de sensores o limite é 127 ciclos; com dados válidos, o PHM estende a vida de cada motor segundo a condição do HI. Isto é diferente de P15.1 a P15.4: lá a idade era um teto (mínimo entre PHM e idade) e a política colapsava na regra de idade. Aqui a idade é o **limite sem monitoramento** e o PHM governa sem teto enquanto o monitoramento é válido. Com monitoramento sempre válido (u=0) o resultado é a própria regra PHM original; com nenhum dado (u=1), o limite de 127. Exploratório, sobre as regras congeladas de P13.1 e motores E já examinados; sem inspeção, sem crédito, sem validação de segurança. A probabilidade u de monitoramento inválido por ciclo é um eixo de sensibilidade, não um valor adotado.

## Valor da extensão (monitoramento sempre válido; prazo 1; média das três repetições)

| Regra | Motores estendidos além de 127 (FD001 / FD003) | Extensão média (ciclos) | Folga T − 127 recuperada | Vida média (ciclos) | Economia de restauração frente ao limite de 127 [extremos entre repetições, IC bootstrap] |
|---|---|---|---|---|---|
| ISO inferior 98%/reserva 15 | 89% / 98% | 41,2 / 81,2 | 53% / 68% | 168,2 / 208,2 | 24,5% [21,1–27,7] / 39,0% [33,9–43,7] |
| Marco HI | 89% / 98% | 40,3 / 80,7 | 52% / 67% | 167,3 / 207,7 | 24,1% / 38,8% |
| Limiar HI selecionado | 97% / 99% | 55,1 / 91,8 | 70% / 76% | 182,1 / 218,8 | 30,2% / 41,9% |
| ISO ponto central | 99% / 100% | 65,1 / 106,0 | 82% / 88% | 192,1 / 233,0 | 33,9% / 45,5% |

O limite de 127 vale como controle: vida 126,3 (FD001) e 126,9 (FD003). As regras de ponto central e as selecionadas têm eventos próprios de P11/P13.1 (ausências e chegadas exatas), que seguem na amostra.

## A extensão acompanha a condição do HI

Correlação de Spearman entre a extensão de cada motor e o HI no ciclo 127 (saída ISO de P10): **0,95 (FD001) e 0,91 (FD003)** para ISO inferior 98%. Extensão média por terço do HI no ciclo 127: baixo 9,3, médio 39,1, alto 75,4 ciclos (FD001); 22,3, 66,4 e 155,8 (FD003). A correlação com a vida real T também é alta (0,95 e 0,96): o PHM separa motores curtos de longos. Cautelas: o HI de M18 é supervisionado pela vida restante, de modo que a extensão carrega informação prognóstica aprendida, e as instabilidades de M23 permanecem.

## Dependência da disponibilidade do monitoramento (resposta suposta: remoção imediata ao detectar a perda)

Economia de restauração frente ao limite de 127, ISO inferior 98%, prazo 1:

| u (prob. de monitoramento inválido por ciclo) | 0 | 0,001 | 0,005 | 0,01 | 0,02 | 1 |
|---|---:|---:|---:|---:|---:|---:|
| FD001 | 24,5% | 23,9% | 21,6% | 19,2% | 15,5% | −0,5% |
| FD003 | 39,0% | 37,3% | 31,6% | 26,5% | 19,9% | −0,1% |

Com a resposta de remoção imediata, a vida esperada **nunca fica abaixo de 127** (toda perda em t > τ produz retirada em t + d ≥ 127). A queda é moderada para u pequeno porque a exposição fora do limite é de dezenas de ciclos. Uma perda no ciclo t < D gera retirada em t + d, anterior à retirada original (D + d); portanto não cria ultrapassagem para motores cuja retirada original já ocorria antes de T, o caso de todas as regras de limite inferior 98% e do marco HI nesta amostra. Os eventos esperados estão em `summary.csv`.

## Limites desta análise

- **A perda de dados é detectada na hora e leva à retirada.** O risco de dado inválido não detectado (sensor degradado, deriva, dado fora do domínio) não está modelado. É nele que o PHM com extensão fica vulnerável, e a função de detecção de integridade do monitoramento é pressuposto, não resultado.
- Perdas independentes entre ciclos subestimam interrupções longas e correlacionadas. Não há indisponibilidade antes do portão (τ = 127 − d). Os valores de u são uma grade, sem calibração.
- A região acima de 127 contém motores que falham. A afirmação P(T ≤ 127) ≤ 1,49% (n=200, 95%) é em amostra e vale para o limite, não para a extensão. Na extensão, a segurança depende da taxa de eventos tardios do PHM: 0 em 300 vidas para as regras de limite inferior 98%, o que com 100 motores distintos só limita o risco a 2,95% (95%).
- A extensão média (41 a 106 ciclos, 33% a 83% acima de 127) é muito maior que os exemplos de extensão de intervalo da AC 120-113 (25 horas a algumas centenas de horas), que são ilustrativos. Uma justificativa de confiabilidade em serviço e de risco seria necessária; não temos.
- O contexto de 20 anos de P12.2 não foi recomputado para esta política.

## Verificação

Sete testes passaram antes da execução (fórmula igual à enumeração por força bruta em cinco motores construídos, concordância com Monte Carlo de 200.000 realizações, u=0 reproduz o original, u=1 reproduz o limite, vida mínima de 127 sob a resposta de remoção imediata). O verificador independente enumerou por laços 67.200 combinações de motor e u a partir das colunas brutas, refez as 672 linhas de resumo, o HI no ciclo 127 em seis partições e o Spearman de uma linha, e conferiu os manifestos anteriores. Sem emendas.
