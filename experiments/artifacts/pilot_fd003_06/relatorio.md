# P06 — transferência FD001→FD003 e reajuste

Extensão de robustez autorizada pelo autor; sem inspeções. FD003 tem uma condição operacional e dois modos de degradação segundo o readme. A AAKR é adaptação do núcleo terminal, não reprodução integral do artigo de Baraldi.

## Teste oficial FD003 — mesmos 100 motores

Transferência mantém os modelos/conversores FD001 congelados; reajuste aprende apenas em treino FD003 e seleciona antes de avaliar os rótulos oficiais.

| Família | RMSE transferência | RMSE reajuste | MAE transferência | MAE reajuste |
|---|---|---|---|---|
| MARGEM | 38.58 | 32.41 | 26.16 | 23.35 |
| EMPIRICO | 79.56 | 23.40 | 58.91 | 17.29 |
| AAKR | 80.25 | 26.41 | 59.33 | 19.98 |

Unidade dos erros: ciclos de RUL no último ponto disponível; não erro contra HI físico.

## Incerteza descritiva pareada

Contraste refit_minus_transfer: RMSE do reajuste menos transferência, nos mesmos motores. alternative_minus_margin: alternativa menos controle dentro do reajuste. Valores negativos favorecem o primeiro termo.

- refit_minus_transfer, MARGEM: -6.18; percentis 2,5%–97,5% [-9.18; -2.64].
- refit_minus_transfer, EMPIRICO: -56.16; percentis 2,5%–97,5% [-68.56; -43.85].
- refit_minus_transfer, AAKR: -53.84; percentis 2,5%–97,5% [-66.92; -41.52].
- alternative_minus_margin, EMPIRICO: -9.00; percentis 2,5%–97,5% [-14.11; -3.63].
- alternative_minus_margin, AAKR: -6.00; percentis 2,5%–97,5% [-10.97; -0.89].

## Trajetórias completas FD003

cv usa avaliação por motor após reajuste; transfer_complete aplica os modelos FD001 às 100 trajetórias completas FD003, sem reajuste.

| Dados | Família | RMSE cortes | HI terminal mediano | Passagens/100 | Antecipação mediana | Máxima | Recuperações |
|---|---|---|---|---|---|---|---|
| cv | AAKR | 33.74 | 0.0010 | 82 | 18.0 | 51.0 | 52 |
| cv | EMPIRICO | 34.18 | 0.0163 | 46 | 5.0 | 32.0 | 0 |
| cv | MARGEM | 42.20 | 0.1000 | 26 | 5.0 | 15.0 | 3 |
| transfer_complete | AAKR | 70.83 | 0.1416 | 49 | 12.0 | 44.0 | 16 |
| transfer_complete | EMPIRICO | 69.65 | 0.1338 | 38 | 8.0 | 29.0 | 0 |
| transfer_complete | MARGEM | 47.67 | 0.0000 | 82 | 30.5 | 334.0 | 7 |

As antecipações são condicionais a haver passagem por zero. Ausências permanecem censuradas, sem imputar F posterior. As trajetórias completas de cada contraste usam os mesmos motores FD003; seus modelos têm fontes/partições de ajuste diferentes.

## Escolhas internas finais

- MARGEM: q0.95; RMSE de seleção 35.70.
- EMPIRICO: t60_g2_r0; RMSE de seleção 31.17.
- AAKR: top5_L10_h0.5; RMSE de seleção 33.95.

## Distribuição das vidas completas

- FD001: mínimo 128, mediana 199, média 206.31, máximo 362 ciclos.
- FD003: mínimo 145, mediana 220.5, média 247.20, máximo 525 ciclos.

## Limites e consequência científica

Os modos e a distribuição de vidas mudam entre subconjuntos; não atribuir diferenças exclusivamente ao segundo mecanismo. Não há aqui rótulo independente do mecanismo dominante por motor para estratificar resultados. IDs iguais em FD001 e FD003 não identificam o mesmo motor.

RUL verdadeira não identifica univocamente o HI físico. Bons erros de prognóstico não tornam o primeiro zero de HI um limite físico, e âncoras aprendidas podem antecipar ou não atingir zero. Na transferência, a referência inicial própria no ciclo 20 é calculada causalmente conforme a fórmula original; não há reaprendizagem de coeficientes, escala da frota ou conversor em FD003.

As grelhas de P05 permaneceram fixas, inclusive a escala do alvo de RUL do HI empírico. Diferenças de desempenho podem refletir necessidade de calibração, inadequação da representação ou mudança do domínio; esta rodada não separa todas essas causas. Não se escolheu um vencedor ou modificou método pelos resultados oficiais.

O teste FD003 passa a ser dado já examinado para futuras adaptações. Inspeções e protocolo principal continuam adiados/abertos. Artefatos: modelos por fold/finais, seleções, pesos/rankings, curvas por ciclo, métricas por motor, bootstrap, distribuição de vidas, faixas de RUL, auditoria de rótulos, figura, metadados e manifesto.
