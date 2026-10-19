# FD001, motor69 — diagnóstico retrospectivo

Critérios de inclusão: max_discordance_d1, max_discordance_d2, max_unused_d1, max_unused_d2.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u69.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 313 | 314 | preventive_schedule | 0.296 | indefinido | indefinido | s12:+0.174, s21:+0.111, s2:+0.103 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 313 | 315 | preventive_schedule | 0.296 | indefinido | indefinido | s12:+0.174, s21:+0.111, s2:+0.103 |
| 1 | HI_WAIT_SELECTED_D1 | 294 | 295 | preventive_schedule | 0.427 | indefinido | indefinido | s12:+0.147, s2:+0.093, s21:+0.076 |
| 1 | HI_WAIT_SELECTED_D2 | 294 | 296 | preventive_schedule | 0.427 | indefinido | indefinido | s12:+0.147, s2:+0.093, s21:+0.076 |
| 1 | ISO_POINT_M15_D1 | 326 | 327 | preventive_schedule | 0.161 | 13.18 | 13.18 | s12:+0.203, s2:+0.127, s21:+0.120 |
| 1 | ISO_POINT_M15_D2 | 326 | 328 | preventive_schedule | 0.161 | 13.18 | 13.18 | s12:+0.203, s2:+0.127, s21:+0.120 |
| 1 | ISO_LOWER98_M15_D1 | 284 | 285 | preventive_schedule | 0.493 | 39.24 | 13.63 | s12:+0.141, s2:+0.080, s21:+0.060 |
| 1 | ISO_LOWER98_M15_D2 | 284 | 286 | preventive_schedule | 0.493 | 39.24 | 13.63 | s12:+0.141, s2:+0.080, s21:+0.060 |
| 1 | RF_SLOPE_POINT_M15_D1 | 340 | 341 | preventive_schedule | 0.054 | 15.60 | 15.60 | s12:+0.231, s2:+0.166, s21:+0.132 |
| 1 | RF_SLOPE_POINT_M15_D2 | 340 | 342 | preventive_schedule | 0.054 | 15.60 | 15.60 | s12:+0.231, s2:+0.166, s21:+0.132 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 296 | 297 | preventive_schedule | 0.404 | 53.14 | 14.98 | s12:+0.155, s2:+0.093, s21:+0.078 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 296 | 298 | preventive_schedule | 0.404 | 53.14 | 14.98 | s12:+0.155, s2:+0.093, s21:+0.078 |
| 1 | AGE_D1 | 135 | 136 | preventive_schedule | 0.909 | indefinido | indefinido | s12:+0.037, s21:+0.020, s17:+0.014 |
| 1 | AGE_D2 | 134 | 136 | preventive_schedule | 0.905 | indefinido | indefinido | s12:+0.036, s21:+0.022, s17:+0.014 |
| 1 | HI_MARKER_D1 | 284 | 285 | preventive_schedule | 0.493 | indefinido | indefinido | s12:+0.141, s2:+0.080, s21:+0.060 |
| 1 | HI_MARKER_D2 | 284 | 286 | preventive_schedule | 0.493 | indefinido | indefinido | s12:+0.141, s2:+0.080, s21:+0.060 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 296 | 297 | preventive_schedule | 0.397 | indefinido | indefinido | s15:+0.153, s2:+0.143, s12:+0.065 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 296 | 298 | preventive_schedule | 0.397 | indefinido | indefinido | s15:+0.153, s2:+0.143, s12:+0.065 |
| 2 | HI_WAIT_SELECTED_D1 | 294 | 295 | preventive_schedule | 0.410 | indefinido | indefinido | s15:+0.151, s2:+0.144, s12:+0.062 |
| 2 | HI_WAIT_SELECTED_D2 | 294 | 296 | preventive_schedule | 0.410 | indefinido | indefinido | s15:+0.151, s2:+0.144, s12:+0.062 |
| 2 | ISO_POINT_M15_D1 | 326 | 327 | preventive_schedule | 0.137 | 15.14 | 15.14 | s15:+0.218, s2:+0.196, s8:+0.090 |
| 2 | ISO_POINT_M15_D2 | 323 | 325 | preventive_schedule | 0.182 | 16.57 | 16.57 | s15:+0.203, s2:+0.187, s21:+0.086 |
| 2 | ISO_LOWER98_M15_D1 | 284 | 285 | preventive_schedule | 0.499 | 37.87 | 11.00 | s2:+0.123, s15:+0.110, s12:+0.059 |
| 2 | ISO_LOWER98_M15_D2 | 284 | 286 | preventive_schedule | 0.499 | 37.87 | 11.00 | s2:+0.123, s15:+0.110, s12:+0.059 |
| 2 | RF_SLOPE_POINT_M15_D1 | 343 | 344 | preventive_schedule | 0.007 | 13.69 | 13.69 | s2:+0.259, s15:+0.228, s8:+0.107 |
| 2 | RF_SLOPE_POINT_M15_D2 | 343 | 345 | preventive_schedule | 0.007 | 13.69 | 13.69 | s2:+0.259, s15:+0.228, s8:+0.107 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 284 | 285 | preventive_schedule | 0.499 | 45.37 | 9.47 | s2:+0.123, s15:+0.110, s12:+0.059 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 284 | 286 | preventive_schedule | 0.499 | 45.37 | 9.47 | s2:+0.123, s15:+0.110, s12:+0.059 |
| 2 | AGE_D1 | 135 | 136 | preventive_schedule | 0.928 | indefinido | indefinido | s17:+0.017, s12:+0.016, s21:+0.015 |
| 2 | AGE_D2 | 134 | 136 | preventive_schedule | 0.924 | indefinido | indefinido | s17:+0.017, s21:+0.016, s12:+0.015 |
| 2 | HI_MARKER_D1 | 284 | 285 | preventive_schedule | 0.499 | indefinido | indefinido | s2:+0.123, s15:+0.110, s12:+0.059 |
| 2 | HI_MARKER_D2 | 284 | 286 | preventive_schedule | 0.499 | indefinido | indefinido | s2:+0.123, s15:+0.110, s12:+0.059 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 316 | 317 | preventive_schedule | 0.299 | indefinido | indefinido | s4:+0.143, s12:+0.120, s20:+0.118 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 316 | 318 | preventive_schedule | 0.299 | indefinido | indefinido | s4:+0.143, s12:+0.120, s20:+0.118 |
| 3 | HI_WAIT_SELECTED_D1 | 294 | 295 | preventive_schedule | 0.444 | indefinido | indefinido | s4:+0.124, s12:+0.096, s20:+0.088 |
| 3 | HI_WAIT_SELECTED_D2 | 294 | 296 | preventive_schedule | 0.444 | indefinido | indefinido | s4:+0.124, s12:+0.096, s20:+0.088 |
| 3 | ISO_POINT_M15_D1 | 326 | 327 | preventive_schedule | 0.191 | 13.85 | 13.85 | s4:+0.156, s20:+0.140, s12:+0.133 |
| 3 | ISO_POINT_M15_D2 | 326 | 328 | preventive_schedule | 0.191 | 13.85 | 13.85 | s4:+0.156, s20:+0.140, s12:+0.133 |
| 3 | ISO_LOWER98_M15_D1 | 284 | 285 | preventive_schedule | 0.498 | 39.68 | 9.00 | s4:+0.111, s12:+0.092, s20:+0.083 |
| 3 | ISO_LOWER98_M15_D2 | 284 | 286 | preventive_schedule | 0.498 | 39.68 | 9.00 | s4:+0.111, s12:+0.092, s20:+0.083 |
| 3 | RF_SLOPE_POINT_M15_D1 | 324 | 325 | preventive_schedule | 0.219 | 15.65 | 15.65 | s4:+0.151, s20:+0.135, s12:+0.133 |
| 3 | RF_SLOPE_POINT_M15_D2 | 324 | 326 | preventive_schedule | 0.219 | 15.65 | 15.65 | s4:+0.151, s20:+0.135, s12:+0.133 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 284 | 285 | preventive_schedule | 0.498 | 46.83 | 10.67 | s4:+0.111, s12:+0.092, s20:+0.083 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 284 | 286 | preventive_schedule | 0.498 | 46.83 | 10.67 | s4:+0.111, s12:+0.092, s20:+0.083 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.911 | indefinido | indefinido | s4:+0.024, s12:+0.019, s17:+0.015 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.919 | indefinido | indefinido | s4:+0.021, s12:+0.017, s17:+0.015 |
| 3 | HI_MARKER_D1 | 284 | 285 | preventive_schedule | 0.498 | indefinido | indefinido | s4:+0.111, s12:+0.092, s20:+0.083 |
| 3 | HI_MARKER_D2 | 284 | 286 | preventive_schedule | 0.498 | indefinido | indefinido | s4:+0.111, s12:+0.092, s20:+0.083 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=284, A=284.
- Repetição2: G=284, A=284.
- Repetição3: G=284, A=284.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.90 | 0.52 | 0.00% | 30.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.90 | 0.52 | 0.00% | 30.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 4.40 | 0.30 | 0.00% | 10.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 4.40 | 0.30 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.67 | 0.64 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.67 | 0.64 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 25.61 | 15 | 4.03 | 1.43 | 0.00% | 30.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 25.61 | 15 | 4.07 | 1.43 | 0.00% | 30.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.40 | 0.67 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.53 | 0.67 | 0.00% | 30.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 38.16 | 15 | 2.47 | 2.50 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 38.16 | 15 | 2.53 | 2.84 | 0.00% | 36.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 4.40 | 1.45 | 0.00% | 26.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 4.40 | 1.45 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 3.30 | 1.32 | 0.00% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 3.30 | 1.32 | 0.00% | 36.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 5.03 | 0.00 | 0.00% | 33.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 5.03 | 0.00 | 0.00% | 33.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 3.00 | 0.25 | 0.00% | 20.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.67 | 0.21 | 0.00% | 20.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 26.87 | 15 | 5.03 | 1.71 | 0.00% | 43.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 26.87 | 15 | 5.03 | 1.71 | 0.00% | 43.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.03 | 0.82 | 0.00% | 6.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.07 | 0.93 | 0.00% | 6.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 35.90 | 15 | 5.20 | 1.71 | 0.00% | 43.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 35.90 | 15 | 5.20 | 1.71 | 0.00% | 43.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 5.03 | 1.71 | 0.00% | 43.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 5.03 | 1.71 | 0.00% | 43.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.17 | 0.37 | 0.00% | 36.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.17 | 0.37 | 0.00% | 36.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 3.97 | 0.27 | 0.00% | 26.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 3.97 | 0.27 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.57 | 0.37 | 0.00% | 36.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.53 | 0.37 | 0.00% | 36.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 30.68 | 15 | 3.97 | 1.26 | 0.00% | 36.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 30.68 | 15 | 3.97 | 1.26 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 5.57 | 0.29 | 0.00% | 53.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 3.73 | 1.86 | 0.00% | 3.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 36.15 | 15 | 3.97 | 1.26 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 36.15 | 15 | 3.97 | 1.26 | 0.00% | 36.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 3.97 | 1.26 | 0.00% | 36.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 3.97 | 1.26 | 0.00% | 36.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
