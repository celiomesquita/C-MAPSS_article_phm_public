# P15.2 — idades conservadoras por conjunto de dados

## Resultado e alcance

Quantidade estimada: **idade fixa de retirada A** (decisão em A − d) da política candidata PHM → idade, com estimativa de P(T ≤ A) ≤ 2% (tolerância experimental de M19, não evidência de segurança). Dados: os 100 motores de treino de cada conjunto, todos incluídos; o valor é de nível de conjunto e, portanto, **em amostra** em relação aos motores E dos pilotos anteriores. Descritivo, exploratório, sem inspeção; nenhum valor foi adotado.

| Conjunto | Mínimo de T | 2º menor | p1% | p2,5% | p5% | Mediana | Máximo | Média (CV) |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| FD001 | 128 | 135 | 134,9 | 137,0 | 147,0 | 199 | 362 | 206,3 (0,22) |
| FD003 | 145 | 147 | 147,0 | 152,5 | 157,9 | 220,5 | 525 | 247,2 (0,35) |

## Idades estimadas (ciclos)

| Estimador | FD001 | FD003 | Leitura |
|---|---:|---:|---|
| E0 mínimo − 1 (100 motores) | **127** | **144** | Referência do projeto estendida ao conjunto todo |
| E1 não paramétrico, confiança 80% | 127 (limite de risco 1,60%) | 144 (1,60%) | Atende ≤2% |
| E1 não paramétrico, confiança 90% | inviável (limite 2,28%) | inviável (2,28%) | Com n=100 e nenhuma ocorrência |
| E1 não paramétrico, confiança 95% | inviável (limite 2,95%) | inviável (2,95%) | Idem |
| E2 Weibull, limite inferior 95% do quantil 2% | 80 | 58 | Ajuste rejeitado (KS e AD, p≈0) |
| E2 log-normal, limite inferior 95% do quantil 2% | 121 | 113 | Ajuste duvidoso em FD001 (KS p=0,03; AD p=0,07), rejeitado em FD003 (p<0,01) |
| E3 chegada por min − 1 fora da amostra (LOO) | 1,0% | 1,0% | Só o motor de menor vida chega ao endpoint antes da idade |

**Estimativa conservadora com respaldo nos dados: 127 ciclos (FD001) e 144 ciclos (FD003).** Eles coincidem com o mínimo observado menos um. Nenhum motor de treino chega ao endpoint antes dessas idades, por construção.

## O que os números sustentam e o que não sustentam

- **Limite de tamanho amostral.** Com n=100 e zero ocorrências, o limite superior de risco é 1,60% (confiança 80%), 2,28% (90%) e 2,95% (95%). O alvo de 2% só se afirma com confiança ≤ ~86%. Ampliar a confiança exigiria n ≥ 114 (90%) ou 148 (95%), sem reaproveitar repetições. É restrição de amostra, e não depende do estimador.
- **Estimadores paramétricos não são confiáveis aqui.** Weibull é rejeitado nos dois conjuntos e subestima muito as idades por causa de cauda esquerda mais pesada que a dos dados (80 e 58 ciclos); a log-normal é plausível apenas no FD001. A extrapolação do quantil 2% a partir de um ajuste rejeitado não tem valor. A forma Weibull de FD001 (c≈4,4) é próxima da reportada por Miranda (4,42) para outro quantitativo (cruzamento de THC=0,5), sem implicar equivalência.
- **FD003** reúne dois modos de falha e cauda longa (máximo 525; CV 0,35); a cauda inferior é estreita (p1% 147 contra mínimo 145), o que favorece uma idade fixa, mas não elimina o risco de motores com vida abaixo do mínimo amostral.
- **Em amostra.** Estas idades usam todos os motores de cada conjunto; aplicá-las aos mesmos motores só mostra consistência (nenhuma chegada), nunca validação. Como confirmação, só FD002/FD004 serviriam, com premissa própria que não foi calculada nem lida.

## Custo de ficar na idade

Sob a idade conservadora, a vida média aproveitada é 127 (FD001) e 144 (FD003) ciclos simulados, ciclos não usados médios 79,3 e 103,2, e 78,7 e 69,4 restaurações por 10.000 ciclos. As regras PHM de P12.1 (ISO inferior 98%/reserva 15) ficam em 59,3–59,7 e 47,7–48,6. A idade conservadora custa, portanto, cerca de 32–33% a mais de restaurações por ciclo no FD001 e 43–46% no FD003 frente ao PHM, ordem de grandeza coerente com P15.1 com q=0.

## Verificação

Seis testes passaram antes da execução. O verificador independente refez estatísticas descritivas, a inversão da binomial por bisseção (sem a função beta), E0, E1 e E3 por laços, e a estimação paramétrica com MLE próprio (Weibull por raiz da equação de verossimilhança, log-normal em forma fechada) na mesma sequência aleatória; quantis ajustados concordaram a 10⁻⁵ e limites inferiores bootstrap a 10⁻⁴. Os valores-p de ajuste foram conferidos apenas nos parâmetros ajustados, não reproduzidos. Manifestos anteriores íntegros. Sem emendas.
