# P07 — previsão do F original a partir de HI=0,5

Análise exploratória retrospectiva das predições congeladas de P05/P06, sem novo treino. HI=0,5 não redefine F, P, remoção ou início de inspeções. Unidades: ciclos. Completo = avaliação externa por motor; truncado = teste oficial já examinado. Não se comparam linhas com coberturas diferentes como se fossem a mesma população.

## Marco principal

| domain | dataset | family | crossed | missing | actual_lead_median | predicted_lead_median | rmse | mae | bias | recovered_engines |
|---|---|---|---|---|---|---|---|---|---|---|
| FD001 | complete | AAKR | 100 | 0 | 56.50 | 65.99 | 22.16 | 17.66 | 0.50 | 14 |
| FD001 | complete | EMPIRICO | 100 | 0 | 39.50 | 40.28 | 17.85 | 14.12 | -0.18 | 7 |
| FD001 | complete | MARGEM | 100 | 0 | 40.50 | 44.08 | 16.87 | 13.51 | 0.26 | 19 |
| FD001 | truncated | AAKR | 32 | 68 | 49.50 | 56.49 | 16.12 | 12.59 | 7.96 | 2 |
| FD001 | truncated | EMPIRICO | 29 | 71 | 42.00 | 42.87 | 13.46 | 10.52 | 3.58 | 1 |
| FD001 | truncated | MARGEM | 29 | 71 | 45.00 | 49.81 | 13.09 | 10.18 | 2.19 | 5 |
| FD003_refit | complete | AAKR | 100 | 0 | 61.00 | 63.60 | 26.43 | 20.20 | -5.82 | 23 |
| FD003_refit | complete | EMPIRICO | 100 | 0 | 33.00 | 30.89 | 14.84 | 11.30 | -3.45 | 10 |
| FD003_refit | complete | MARGEM | 100 | 0 | 30.00 | 27.13 | 25.67 | 13.92 | -7.17 | 26 |
| FD003_refit | truncated | AAKR | 45 | 55 | 80.00 | 64.87 | 34.04 | 25.76 | -19.92 | 13 |
| FD003_refit | truncated | EMPIRICO | 22 | 78 | 37.00 | 30.72 | 15.87 | 11.92 | -6.31 | 1 |
| FD003_refit | truncated | MARGEM | 24 | 76 | 42.50 | 27.94 | 63.59 | 34.61 | -30.72 | 6 |
| FD003_transfer | complete | AAKR | 56 | 44 | 45.00 | 56.49 | 19.75 | 16.88 | 7.50 | 3 |
| FD003_transfer | complete | EMPIRICO | 56 | 44 | 37.50 | 42.87 | 15.59 | 12.97 | 3.42 | 3 |
| FD003_transfer | complete | MARGEM | 100 | 0 | 54.00 | 49.81 | 82.52 | 41.27 | -30.73 | 26 |
| FD003_transfer | truncated | AAKR | 16 | 84 | 50.50 | 56.49 | 16.01 | 14.05 | 3.85 | 1 |
| FD003_transfer | truncated | EMPIRICO | 10 | 90 | 33.50 | 43.87 | 16.01 | 14.05 | 3.96 | 0 |
| FD003_transfer | truncated | MARGEM | 42 | 58 | 84.50 | 44.99 | 110.28 | 70.62 | -65.85 | 16 |

RMSE, MAE e viés são condicionais ao cruzamento. Viés positivo prevê F tarde; é erro de previsão, não uma decisão de remoção. A antecedência real é retrospectiva. Ausências completas e ausências até truncamento estão discriminadas em landmarks.csv.

## Sensibilidade (sem seleção do melhor limiar)

| domain | dataset | family | alpha | crossed | actual_lead_median | rmse | bias |
|---|---|---|---|---|---|---|---|
| FD001 | complete | AAKR | 0.40 | 100 | 47.00 | 19.64 | -0.77 |
| FD001 | complete | AAKR | 0.50 | 100 | 56.50 | 22.16 | 0.50 |
| FD001 | complete | AAKR | 0.60 | 100 | 68.00 | 23.66 | 0.91 |
| FD001 | complete | EMPIRICO | 0.40 | 100 | 31.00 | 16.96 | 1.13 |
| FD001 | complete | EMPIRICO | 0.50 | 100 | 39.50 | 17.85 | -0.18 |
| FD001 | complete | EMPIRICO | 0.60 | 100 | 49.50 | 20.22 | 1.35 |
| FD001 | complete | MARGEM | 0.40 | 99 | 30.00 | 15.41 | -1.37 |
| FD001 | complete | MARGEM | 0.50 | 100 | 40.50 | 16.87 | 0.26 |
| FD001 | complete | MARGEM | 0.60 | 100 | 54.00 | 21.91 | -0.84 |
| FD001 | truncated | AAKR | 0.40 | 28 | 38.00 | 13.50 | 1.81 |
| FD001 | truncated | AAKR | 0.50 | 32 | 49.50 | 16.12 | 7.96 |
| FD001 | truncated | AAKR | 0.60 | 41 | 62.00 | 18.71 | 1.16 |
| FD001 | truncated | EMPIRICO | 0.40 | 23 | 34.00 | 11.95 | -1.47 |
| FD001 | truncated | EMPIRICO | 0.50 | 29 | 42.00 | 13.46 | 3.58 |
| FD001 | truncated | EMPIRICO | 0.60 | 33 | 54.00 | 16.62 | 2.69 |
| FD001 | truncated | MARGEM | 0.40 | 21 | 35.00 | 14.66 | -6.85 |
| FD001 | truncated | MARGEM | 0.50 | 29 | 45.00 | 13.09 | 2.19 |
| FD001 | truncated | MARGEM | 0.60 | 33 | 58.00 | 15.16 | 4.73 |
| FD003_refit | complete | AAKR | 0.40 | 100 | 54.00 | 23.29 | -3.14 |
| FD003_refit | complete | AAKR | 0.50 | 100 | 61.00 | 26.43 | -5.82 |
| FD003_refit | complete | AAKR | 0.60 | 100 | 74.00 | 29.23 | -6.46 |
| FD003_refit | complete | EMPIRICO | 0.40 | 99 | 25.00 | 13.61 | -3.84 |
| FD003_refit | complete | EMPIRICO | 0.50 | 100 | 33.00 | 14.84 | -3.45 |
| FD003_refit | complete | EMPIRICO | 0.60 | 100 | 44.50 | 18.40 | -4.24 |
| FD003_refit | complete | MARGEM | 0.40 | 98 | 19.00 | 16.59 | -5.12 |
| FD003_refit | complete | MARGEM | 0.50 | 100 | 30.00 | 25.67 | -7.17 |
| FD003_refit | complete | MARGEM | 0.60 | 100 | 41.50 | 37.42 | -9.81 |
| FD003_refit | truncated | AAKR | 0.40 | 43 | 75.00 | 28.01 | -15.99 |
| FD003_refit | truncated | AAKR | 0.50 | 45 | 80.00 | 34.04 | -19.92 |
| FD003_refit | truncated | AAKR | 0.60 | 52 | 90.00 | 38.43 | -20.61 |
| FD003_refit | truncated | EMPIRICO | 0.40 | 15 | 28.00 | 11.15 | -6.81 |
| FD003_refit | truncated | EMPIRICO | 0.50 | 22 | 37.00 | 15.87 | -6.31 |
| FD003_refit | truncated | EMPIRICO | 0.60 | 30 | 49.00 | 18.47 | -9.54 |
| FD003_refit | truncated | MARGEM | 0.40 | 16 | 29.50 | 33.85 | -19.14 |
| FD003_refit | truncated | MARGEM | 0.50 | 24 | 42.50 | 63.59 | -30.72 |
| FD003_refit | truncated | MARGEM | 0.60 | 36 | 57.00 | 79.81 | -41.36 |
| FD003_transfer | complete | AAKR | 0.40 | 56 | 35.50 | 16.06 | 1.89 |
| FD003_transfer | complete | AAKR | 0.50 | 56 | 45.00 | 19.75 | 7.50 |
| FD003_transfer | complete | AAKR | 0.60 | 56 | 54.00 | 21.61 | 3.98 |
| FD003_transfer | complete | EMPIRICO | 0.40 | 56 | 28.00 | 14.19 | 2.57 |
| FD003_transfer | complete | EMPIRICO | 0.50 | 56 | 37.50 | 15.59 | 3.42 |
| FD003_transfer | complete | EMPIRICO | 0.60 | 56 | 46.50 | 18.40 | 4.36 |
| FD003_transfer | complete | MARGEM | 0.40 | 100 | 45.00 | 75.15 | -33.75 |
| FD003_transfer | complete | MARGEM | 0.50 | 100 | 54.00 | 82.52 | -30.73 |
| FD003_transfer | complete | MARGEM | 0.60 | 100 | 71.00 | 82.19 | -30.01 |
| FD003_transfer | truncated | AAKR | 0.40 | 11 | 33.00 | 16.09 | -0.22 |
| FD003_transfer | truncated | AAKR | 0.50 | 16 | 50.50 | 16.01 | 3.85 |
| FD003_transfer | truncated | AAKR | 0.60 | 18 | 68.00 | 17.07 | -0.30 |
| FD003_transfer | truncated | EMPIRICO | 0.40 | 9 | 25.00 | 13.40 | 3.50 |
| FD003_transfer | truncated | EMPIRICO | 0.50 | 10 | 33.50 | 16.01 | 3.96 |
| FD003_transfer | truncated | EMPIRICO | 0.60 | 16 | 51.50 | 15.70 | 1.11 |
| FD003_transfer | truncated | MARGEM | 0.40 | 35 | 80.00 | 122.81 | -81.78 |
| FD003_transfer | truncated | MARGEM | 0.50 | 42 | 84.50 | 110.28 | -65.85 |
| FD003_transfer | truncated | MARGEM | 0.60 | 47 | 86.00 | 100.80 | -55.71 |

## Comparações nos mesmos motores e no mesmo ciclo

A = primeira família/domínio do rótulo; B = segunda. Diferenças B−A. Ciclo comum = máximo dos dois primeiros cruzamentos. Intervalos de bootstrap pareado com 2.000 reamostragens são descritivos e não corrigem reutilização dos dados.

| comparison | dataset | common | rmse_a | rmse_b | delta_rmse_b_minus_a | ci_low | ci_high |
|---|---|---|---|---|---|---|---|
| FD001:MARGEM->EMPIRICO | complete | 100 | 16.72 | 15.59 | -1.13 | -2.74 | 0.43 |
| FD001:MARGEM->AAKR | complete | 100 | 17.15 | 17.43 | 0.29 | -1.86 | 2.54 |
| FD001:EMPIRICO->AAKR | complete | 100 | 17.94 | 18.27 | 0.33 | -0.31 | 1.01 |
| FD003_refit:MARGEM->EMPIRICO | complete | 100 | 14.62 | 13.57 | -1.05 | -2.96 | 0.69 |
| FD003_refit:MARGEM->AAKR | complete | 100 | 17.96 | 16.97 | -0.99 | -4.96 | 2.51 |
| FD003_refit:EMPIRICO->AAKR | complete | 100 | 14.84 | 16.00 | 1.16 | -0.41 | 2.84 |
| FD003_transfer:MARGEM->EMPIRICO | complete | 56 | 15.36 | 15.57 | 0.21 | -1.74 | 2.22 |
| FD003_transfer:MARGEM->AAKR | complete | 56 | 16.13 | 17.95 | 1.82 | -0.53 | 4.24 |
| FD003_transfer:EMPIRICO->AAKR | complete | 56 | 15.53 | 17.66 | 2.13 | 0.73 | 3.44 |
| FD003_transfer->refit:MARGEM | complete | 100 | 32.63 | 25.67 | -6.96 | -9.18 | -5.45 |
| FD003_transfer->refit:EMPIRICO | complete | 56 | 14.75 | 15.41 | 0.66 | -1.54 | 2.73 |
| FD003_transfer->refit:AAKR | complete | 56 | 19.75 | 19.22 | -0.53 | -2.07 | 1.16 |
| FD001:MARGEM->EMPIRICO | truncated | 27 | 14.35 | 13.36 | -0.98 | -3.50 | 1.65 |
| FD001:MARGEM->AAKR | truncated | 28 | 14.00 | 13.82 | -0.18 | -2.10 | 2.06 |
| FD001:EMPIRICO->AAKR | truncated | 29 | 13.46 | 14.02 | 0.56 | -1.06 | 2.65 |
| FD003_refit:MARGEM->EMPIRICO | truncated | 20 | 17.83 | 14.30 | -3.53 | -6.85 | -1.18 |
| FD003_refit:MARGEM->AAKR | truncated | 22 | 31.18 | 24.75 | -6.43 | -15.88 | 2.81 |
| FD003_refit:EMPIRICO->AAKR | truncated | 22 | 15.87 | 21.93 | 6.06 | 1.66 | 10.35 |
| FD003_transfer:MARGEM->EMPIRICO | truncated | 10 | 14.02 | 15.44 | 1.41 | -2.43 | 5.82 |
| FD003_transfer:MARGEM->AAKR | truncated | 12 | 12.94 | 15.68 | 2.74 | -2.20 | 7.47 |
| FD003_transfer:EMPIRICO->AAKR | truncated | 10 | 16.01 | 17.09 | 1.08 | -1.56 | 3.50 |
| FD003_transfer->refit:MARGEM | truncated | 24 | 73.40 | 63.59 | -9.82 | -13.53 | -7.28 |
| FD003_transfer->refit:EMPIRICO | truncated | 10 | 16.54 | 17.29 | 0.75 | -8.06 | 5.93 |
| FD003_transfer->refit:AAKR | truncated | 16 | 16.01 | 20.08 | 4.07 | -2.22 | 9.79 |

## Atualização após cinco ciclos

| domain | dataset | family | available | crossed | initial_rmse_same_engines | rmse | delta_rmse_from_initial |
|---|---|---|---|---|---|---|---|
| FD001 | complete | AAKR | 100 | 100 | 22.16 | 20.58 | -1.59 |
| FD001 | complete | EMPIRICO | 100 | 100 | 17.85 | 17.11 | -0.74 |
| FD001 | complete | MARGEM | 99 | 100 | 16.85 | 15.87 | -0.98 |
| FD001 | truncated | AAKR | 29 | 32 | 16.14 | 15.02 | -1.12 |
| FD001 | truncated | EMPIRICO | 25 | 29 | 13.02 | 12.76 | -0.26 |
| FD001 | truncated | MARGEM | 24 | 29 | 13.83 | 14.55 | 0.72 |
| FD003_refit | complete | AAKR | 100 | 100 | 26.43 | 25.41 | -1.02 |
| FD003_refit | complete | EMPIRICO | 100 | 100 | 14.84 | 14.31 | -0.53 |
| FD003_refit | complete | MARGEM | 100 | 100 | 25.67 | 24.70 | -0.97 |
| FD003_refit | truncated | AAKR | 44 | 45 | 34.16 | 32.27 | -1.89 |
| FD003_refit | truncated | EMPIRICO | 20 | 22 | 16.34 | 15.22 | -1.13 |
| FD003_refit | truncated | MARGEM | 19 | 24 | 69.09 | 66.15 | -2.94 |
| FD003_transfer | complete | AAKR | 56 | 56 | 19.75 | 17.36 | -2.38 |
| FD003_transfer | complete | EMPIRICO | 56 | 56 | 15.59 | 15.76 | 0.17 |
| FD003_transfer | complete | MARGEM | 100 | 100 | 82.52 | 73.32 | -9.20 |
| FD003_transfer | truncated | AAKR | 12 | 16 | 17.51 | 16.43 | -1.08 |
| FD003_transfer | truncated | EMPIRICO | 10 | 10 | 16.01 | 15.18 | -0.83 |
| FD003_transfer | truncated | MARGEM | 38 | 42 | 115.43 | 114.99 | -0.45 |

O comparador conserva F previsto no marco. Os CSVs incluem todos os ciclos subsequentes e deslocamentos −10/−5/0/+5/+10/+20, com coberturas próprias. Comparações anteriores ao marco são retrospectivas; não permitem antecipar causalmente seu instante. Recuperações são retornos de HI acima do limiar depois da primeira passagem.

## Limites de interpretação

O conversor usa HI corrente. A concentração das previsões no limiar deve ser examinada junto da dispersão das vidas reais: cruzar o mesmo nível não demonstra prognóstico individualizado. As famílias podem cruzar em instantes diferentes; por isso estão arquivadas comparações em ciclos comuns e em marcos próprios. Não há tolerância operacional validada, adoção definitiva do HI, inspeção simulada ou protocolo principal congelado. Modelos FD001 transferidos foram ajustados nas trajetórias completas FD001, mas não nas trajetórias FD003 avaliadas nesse braço. Os domínios não são motores pareados.
