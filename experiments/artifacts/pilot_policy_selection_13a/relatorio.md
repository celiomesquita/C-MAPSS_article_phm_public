# P13.1 — seleção interna e avaliação externa

240 ajustes internos da mesma fórmula de índice de saúde (HI), 60 seleções externas por domínio/repetição/dobra e 9.600 decisões externas. Cada repetição avalia 100 motores por domínio; repetições reutilizam motores. Escolhas usam apenas D40, sem U50/E10.

## Escolhas congeladas

| Domínio | Família | Prazo | Valor | Dobras |
|---|---|---|---|---|
| FD001 | threshold | 1 | 0.2 | 1 |
| FD001 | threshold | 1 | 0.3 | 20 |
| FD001 | threshold | 1 | 0.4 | 9 |
| FD001 | threshold | 2 | 0.2 | 1 |
| FD001 | threshold | 2 | 0.3 | 14 |
| FD001 | threshold | 2 | 0.4 | 15 |
| FD001 | wait | 1 | 5.0 | 1 |
| FD001 | wait | 1 | 10.0 | 29 |
| FD001 | wait | 2 | 5.0 | 5 |
| FD001 | wait | 2 | 10.0 | 25 |
| FD003 | threshold | 1 | 0.3 | 11 |
| FD003 | threshold | 1 | 0.4 | 13 |
| FD003 | threshold | 1 | 0.5 | 6 |
| FD003 | threshold | 2 | 0.3 | 7 |
| FD003 | threshold | 2 | 0.4 | 17 |
| FD003 | threshold | 2 | 0.5 | 6 |
| FD003 | wait | 1 | 2.0 | 1 |
| FD003 | wait | 1 | 5.0 | 9 |
| FD003 | wait | 1 | 10.0 | 20 |
| FD003 | wait | 2 | 2.0 | 5 |
| FD003 | wait | 2 | 5.0 | 6 |
| FD003 | wait | 2 | 10.0 | 19 |

Seleções sem candidato viável: 4/240.

## Avaliação externa

| Domínio | Repetição | Regra | Vida média | Chegadas/100 | Tardias | Exatas | Sem decisão |
|---|---|---|---|---|---|---|---|
| FD001 | 1 | AGE_D1 | 134.72 | 3 | 0 | 0 | 3 |
| FD001 | 1 | AGE_D2 | 134.72 | 3 | 1 | 0 | 2 |
| FD001 | 1 | HI_MARKER_D1 | 168.02 | 0 | 0 | 0 | 0 |
| FD001 | 1 | HI_MARKER_D2 | 169.02 | 0 | 0 | 0 | 0 |
| FD001 | 1 | HI_THRESHOLD_SELECTED_D1 | 183.51 | 1 | 0 | 0 | 1 |
| FD001 | 1 | HI_THRESHOLD_SELECTED_D2 | 182.10 | 1 | 0 | 0 | 1 |
| FD001 | 1 | HI_WAIT_SELECTED_D1 | 178.02 | 1 | 0 | 1 | 0 |
| FD001 | 1 | HI_WAIT_SELECTED_D2 | 179.01 | 1 | 1 | 0 | 0 |
| FD001 | 1 | ISO_LOWER98_M15_D1 | 168.50 | 0 | 0 | 0 | 0 |
| FD001 | 1 | ISO_LOWER98_M15_D2 | 169.23 | 0 | 0 | 0 | 0 |
| FD001 | 1 | ISO_POINT_M15_D1 | 191.13 | 7 | 0 | 2 | 5 |
| FD001 | 1 | ISO_POINT_M15_D2 | 191.32 | 10 | 1 | 4 | 5 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D1 | 168.76 | 0 | 0 | 0 | 0 |
| FD001 | 1 | RF_SLOPE_LOWER98_M15_D2 | 169.74 | 0 | 0 | 0 | 0 |
| FD001 | 1 | RF_SLOPE_POINT_M15_D1 | 190.81 | 6 | 0 | 0 | 6 |
| FD001 | 1 | RF_SLOPE_POINT_M15_D2 | 190.55 | 6 | 0 | 1 | 5 |
| FD001 | 2 | AGE_D1 | 131.02 | 1 | 0 | 0 | 1 |
| FD001 | 2 | AGE_D2 | 131.02 | 1 | 0 | 0 | 1 |
| FD001 | 2 | HI_MARKER_D1 | 166.69 | 0 | 0 | 0 | 0 |
| FD001 | 2 | HI_MARKER_D2 | 167.69 | 0 | 0 | 0 | 0 |
| FD001 | 2 | HI_THRESHOLD_SELECTED_D1 | 180.97 | 1 | 0 | 0 | 1 |
| FD001 | 2 | HI_THRESHOLD_SELECTED_D2 | 181.17 | 1 | 0 | 0 | 1 |
| FD001 | 2 | HI_WAIT_SELECTED_D1 | 176.69 | 0 | 0 | 0 | 0 |
| FD001 | 2 | HI_WAIT_SELECTED_D2 | 176.69 | 0 | 0 | 0 | 0 |
| FD001 | 2 | ISO_LOWER98_M15_D1 | 167.41 | 0 | 0 | 0 | 0 |
| FD001 | 2 | ISO_LOWER98_M15_D2 | 168.24 | 0 | 0 | 0 | 0 |
| FD001 | 2 | ISO_POINT_M15_D1 | 193.16 | 15 | 0 | 4 | 11 |
| FD001 | 2 | ISO_POINT_M15_D2 | 191.97 | 10 | 1 | 1 | 8 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D1 | 167.08 | 0 | 0 | 0 | 0 |
| FD001 | 2 | RF_SLOPE_LOWER98_M15_D2 | 167.97 | 0 | 0 | 0 | 0 |
| FD001 | 2 | RF_SLOPE_POINT_M15_D1 | 190.87 | 8 | 0 | 1 | 7 |
| FD001 | 2 | RF_SLOPE_POINT_M15_D2 | 190.32 | 6 | 1 | 0 | 5 |
| FD001 | 3 | AGE_D1 | 130.12 | 1 | 0 | 0 | 1 |
| FD001 | 3 | AGE_D2 | 130.12 | 1 | 0 | 0 | 1 |
| FD001 | 3 | HI_MARKER_D1 | 167.08 | 0 | 0 | 0 | 0 |
| FD001 | 3 | HI_MARKER_D2 | 168.08 | 0 | 0 | 0 | 0 |
| FD001 | 3 | HI_THRESHOLD_SELECTED_D1 | 181.70 | 0 | 0 | 0 | 0 |
| FD001 | 3 | HI_THRESHOLD_SELECTED_D2 | 181.27 | 2 | 0 | 2 | 0 |
| FD001 | 3 | HI_WAIT_SELECTED_D1 | 176.58 | 0 | 0 | 0 | 0 |
| FD001 | 3 | HI_WAIT_SELECTED_D2 | 176.58 | 0 | 0 | 0 | 0 |
| FD001 | 3 | ISO_LOWER98_M15_D1 | 168.65 | 0 | 0 | 0 | 0 |
| FD001 | 3 | ISO_LOWER98_M15_D2 | 169.23 | 0 | 0 | 0 | 0 |
| FD001 | 3 | ISO_POINT_M15_D1 | 191.96 | 12 | 0 | 5 | 7 |
| FD001 | 3 | ISO_POINT_M15_D2 | 191.60 | 10 | 4 | 2 | 4 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D1 | 168.17 | 0 | 0 | 0 | 0 |
| FD001 | 3 | RF_SLOPE_LOWER98_M15_D2 | 169.13 | 0 | 0 | 0 | 0 |
| FD001 | 3 | RF_SLOPE_POINT_M15_D1 | 190.93 | 9 | 0 | 3 | 6 |
| FD001 | 3 | RF_SLOPE_POINT_M15_D2 | 190.75 | 12 | 3 | 4 | 5 |
| FD003 | 1 | AGE_D1 | 146.16 | 2 | 0 | 0 | 2 |
| FD003 | 1 | AGE_D2 | 146.16 | 2 | 1 | 0 | 1 |
| FD003 | 1 | HI_MARKER_D1 | 208.86 | 0 | 0 | 0 | 0 |
| FD003 | 1 | HI_MARKER_D2 | 209.86 | 0 | 0 | 0 | 0 |
| FD003 | 1 | HI_THRESHOLD_SELECTED_D1 | 217.94 | 0 | 0 | 0 | 0 |
| FD003 | 1 | HI_THRESHOLD_SELECTED_D2 | 218.15 | 0 | 0 | 0 | 0 |
| FD003 | 1 | HI_WAIT_SELECTED_D1 | 216.56 | 0 | 0 | 0 | 0 |
| FD003 | 1 | HI_WAIT_SELECTED_D2 | 216.76 | 0 | 0 | 0 | 0 |
| FD003 | 1 | ISO_LOWER98_M15_D1 | 209.69 | 0 | 0 | 0 | 0 |
| FD003 | 1 | ISO_LOWER98_M15_D2 | 210.21 | 0 | 0 | 0 | 0 |
| FD003 | 1 | ISO_POINT_M15_D1 | 233.23 | 13 | 0 | 1 | 12 |
| FD003 | 1 | ISO_POINT_M15_D2 | 232.88 | 13 | 2 | 1 | 10 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D1 | 209.40 | 0 | 0 | 0 | 0 |
| FD003 | 1 | RF_SLOPE_LOWER98_M15_D2 | 210.27 | 0 | 0 | 0 | 0 |
| FD003 | 1 | RF_SLOPE_POINT_M15_D1 | 229.40 | 6 | 0 | 1 | 5 |
| FD003 | 1 | RF_SLOPE_POINT_M15_D2 | 229.30 | 7 | 0 | 2 | 5 |
| FD003 | 2 | AGE_D1 | 145.24 | 1 | 0 | 0 | 1 |
| FD003 | 2 | AGE_D2 | 145.24 | 1 | 0 | 0 | 1 |
| FD003 | 2 | HI_MARKER_D1 | 204.98 | 0 | 0 | 0 | 0 |
| FD003 | 2 | HI_MARKER_D2 | 205.98 | 0 | 0 | 0 | 0 |
| FD003 | 2 | HI_THRESHOLD_SELECTED_D1 | 217.88 | 2 | 0 | 0 | 2 |
| FD003 | 2 | HI_THRESHOLD_SELECTED_D2 | 218.03 | 2 | 0 | 0 | 2 |
| FD003 | 2 | HI_WAIT_SELECTED_D1 | 212.97 | 1 | 0 | 0 | 1 |
| FD003 | 2 | HI_WAIT_SELECTED_D2 | 213.66 | 1 | 0 | 0 | 1 |
| FD003 | 2 | ISO_LOWER98_M15_D1 | 205.70 | 0 | 0 | 0 | 0 |
| FD003 | 2 | ISO_LOWER98_M15_D2 | 206.58 | 0 | 0 | 0 | 0 |
| FD003 | 2 | ISO_POINT_M15_D1 | 232.36 | 17 | 0 | 2 | 15 |
| FD003 | 2 | ISO_POINT_M15_D2 | 231.39 | 13 | 2 | 4 | 7 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D1 | 205.47 | 0 | 0 | 0 | 0 |
| FD003 | 2 | RF_SLOPE_LOWER98_M15_D2 | 206.45 | 0 | 0 | 0 | 0 |
| FD003 | 2 | RF_SLOPE_POINT_M15_D1 | 228.50 | 9 | 0 | 3 | 6 |
| FD003 | 2 | RF_SLOPE_POINT_M15_D2 | 228.03 | 8 | 3 | 0 | 5 |
| FD003 | 3 | AGE_D1 | 148.61 | 2 | 0 | 0 | 2 |
| FD003 | 3 | AGE_D2 | 148.61 | 2 | 1 | 0 | 1 |
| FD003 | 3 | HI_MARKER_D1 | 209.16 | 0 | 0 | 0 | 0 |
| FD003 | 3 | HI_MARKER_D2 | 210.16 | 0 | 0 | 0 | 0 |
| FD003 | 3 | HI_THRESHOLD_SELECTED_D1 | 220.53 | 2 | 0 | 1 | 1 |
| FD003 | 3 | HI_THRESHOLD_SELECTED_D2 | 219.57 | 0 | 0 | 0 | 0 |
| FD003 | 3 | HI_WAIT_SELECTED_D1 | 218.16 | 0 | 0 | 0 | 0 |
| FD003 | 3 | HI_WAIT_SELECTED_D2 | 218.56 | 0 | 0 | 0 | 0 |
| FD003 | 3 | ISO_LOWER98_M15_D1 | 209.16 | 0 | 0 | 0 | 0 |
| FD003 | 3 | ISO_LOWER98_M15_D2 | 210.16 | 0 | 0 | 0 | 0 |
| FD003 | 3 | ISO_POINT_M15_D1 | 233.47 | 12 | 0 | 2 | 10 |
| FD003 | 3 | ISO_POINT_M15_D2 | 233.75 | 10 | 0 | 2 | 8 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D1 | 209.40 | 0 | 0 | 0 | 0 |
| FD003 | 3 | RF_SLOPE_LOWER98_M15_D2 | 210.40 | 0 | 0 | 0 | 0 |
| FD003 | 3 | RF_SLOPE_POINT_M15_D1 | 231.06 | 6 | 0 | 1 | 5 |
| FD003 | 3 | RF_SLOPE_POINT_M15_D2 | 231.20 | 6 | 1 | 0 | 5 |

As chegadas incluem retirada em T, após T ou ausência de decisão. O filtro interno composto ≤2% em 40 motores exige zero eventos observados; difere da tolerância estrita de ultrapassagem >T do autor. Não constitui garantia populacional. Ganhos de vida acompanhados de eventos não são economia admissível demonstrada.

[Contrastes pareados e intervalos bootstrap](contrasts.csv): 2.000 reamostragens por motor/repetição, condicionais aos modelos e escolhas; não reaprendem todo o procedimento. Dados já explorados, sem confirmação externa intocada. Nenhuma inspeção ou projeção monetária nesta rodada.
