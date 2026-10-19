# FD001, motor91 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u91.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | indefinido | endpoint_without_decision | 0.315 | indefinido | indefinido | s12:+0.170, s2:+0.117, s15:+0.092 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | indefinido | endpoint_without_decision | 0.315 | indefinido | indefinido | s12:+0.170, s2:+0.117, s15:+0.092 |
| 1 | HI_WAIT_SELECTED_D1 | 134 | 135 | at_endpoint | 0.315 | indefinido | indefinido | s12:+0.170, s2:+0.117, s15:+0.092 |
| 1 | HI_WAIT_SELECTED_D2 | 134 | 136 | late_schedule | 0.315 | indefinido | indefinido | s12:+0.170, s2:+0.117, s15:+0.092 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.315 | 23.95 | 23.95 | s12:+0.170, s2:+0.117, s15:+0.092 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.315 | 23.95 | 23.95 | s12:+0.170, s2:+0.117, s15:+0.092 |
| 1 | ISO_LOWER98_M15_D1 | 124 | 125 | preventive_schedule | 0.490 | 39.24 | 13.63 | s12:+0.125, s2:+0.097, s15:+0.067 |
| 1 | ISO_LOWER98_M15_D2 | 124 | 126 | preventive_schedule | 0.490 | 39.24 | 13.63 | s12:+0.125, s2:+0.097, s15:+0.067 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.315 | 18.21 | 18.21 | s12:+0.170, s2:+0.117, s15:+0.092 |
| 1 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.315 | 18.21 | 18.21 | s12:+0.170, s2:+0.117, s15:+0.092 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 124 | 125 | preventive_schedule | 0.490 | 31.09 | 0.00 | s12:+0.125, s2:+0.097, s15:+0.067 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 124 | 126 | preventive_schedule | 0.490 | 31.09 | 0.00 | s12:+0.125, s2:+0.097, s15:+0.067 |
| 1 | AGE_D1 | indefinido | indefinido | endpoint_without_decision | 0.315 | indefinido | indefinido | s12:+0.170, s2:+0.117, s15:+0.092 |
| 1 | AGE_D2 | 134 | 136 | late_schedule | 0.315 | indefinido | indefinido | s12:+0.170, s2:+0.117, s15:+0.092 |
| 1 | HI_MARKER_D1 | 124 | 125 | preventive_schedule | 0.490 | indefinido | indefinido | s12:+0.125, s2:+0.097, s15:+0.067 |
| 1 | HI_MARKER_D2 | 124 | 126 | preventive_schedule | 0.490 | indefinido | indefinido | s12:+0.125, s2:+0.097, s15:+0.067 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | indefinido | endpoint_without_decision | 0.205 | indefinido | indefinido | s2:+0.155, s4:+0.129, s11:+0.113 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | indefinido | endpoint_without_decision | 0.205 | indefinido | indefinido | s2:+0.155, s4:+0.129, s11:+0.113 |
| 2 | HI_WAIT_SELECTED_D1 | 128 | 129 | preventive_schedule | 0.326 | indefinido | indefinido | s2:+0.148, s4:+0.109, s11:+0.098 |
| 2 | HI_WAIT_SELECTED_D2 | 128 | 130 | preventive_schedule | 0.326 | indefinido | indefinido | s2:+0.148, s4:+0.109, s11:+0.098 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.205 | 24.68 | 24.68 | s2:+0.155, s4:+0.129, s11:+0.113 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.205 | 24.68 | 24.68 | s2:+0.155, s4:+0.129, s11:+0.113 |
| 2 | ISO_LOWER98_M15_D1 | 119 | 120 | preventive_schedule | 0.469 | 42.32 | 15.00 | s2:+0.109, s4:+0.090, s11:+0.080 |
| 2 | ISO_LOWER98_M15_D2 | 119 | 121 | preventive_schedule | 0.469 | 42.32 | 15.00 | s2:+0.109, s4:+0.090, s11:+0.080 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.205 | 17.64 | 17.64 | s2:+0.155, s4:+0.129, s11:+0.113 |
| 2 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.205 | 17.64 | 17.64 | s2:+0.155, s4:+0.129, s11:+0.113 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 118 | 119 | preventive_schedule | 0.490 | 44.41 | 5.35 | s2:+0.099, s4:+0.086, s11:+0.076 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 118 | 120 | preventive_schedule | 0.490 | 44.41 | 5.35 | s2:+0.099, s4:+0.086, s11:+0.076 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.367 | indefinido | indefinido | s2:+0.142, s4:+0.106, s11:+0.090 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.391 | indefinido | indefinido | s2:+0.133, s4:+0.102, s11:+0.089 |
| 2 | HI_MARKER_D1 | 118 | 119 | preventive_schedule | 0.490 | indefinido | indefinido | s2:+0.099, s4:+0.086, s11:+0.076 |
| 2 | HI_MARKER_D2 | 118 | 120 | preventive_schedule | 0.490 | indefinido | indefinido | s2:+0.099, s4:+0.086, s11:+0.076 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 133 | 134 | preventive_schedule | 0.278 | indefinido | indefinido | s4:+0.141, s3:+0.113, s20:+0.108 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 133 | 135 | at_endpoint | 0.278 | indefinido | indefinido | s4:+0.141, s3:+0.113, s20:+0.108 |
| 3 | HI_WAIT_SELECTED_D1 | 131 | 132 | preventive_schedule | 0.342 | indefinido | indefinido | s4:+0.128, s3:+0.105, s20:+0.095 |
| 3 | HI_WAIT_SELECTED_D2 | 131 | 133 | preventive_schedule | 0.342 | indefinido | indefinido | s4:+0.128, s3:+0.105, s20:+0.095 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.253 | 21.93 | 21.93 | s4:+0.145, s3:+0.115, s20:+0.113 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.253 | 21.93 | 21.93 | s4:+0.145, s3:+0.115, s20:+0.113 |
| 3 | ISO_LOWER98_M15_D1 | 121 | 122 | preventive_schedule | 0.497 | 41.11 | 15.70 | s4:+0.108, s3:+0.084, s20:+0.065 |
| 3 | ISO_LOWER98_M15_D2 | 121 | 123 | preventive_schedule | 0.497 | 41.11 | 15.70 | s4:+0.108, s3:+0.084, s20:+0.065 |
| 3 | RF_SLOPE_POINT_M15_D1 | 133 | 134 | preventive_schedule | 0.278 | 14.15 | 14.15 | s4:+0.141, s3:+0.113, s20:+0.108 |
| 3 | RF_SLOPE_POINT_M15_D2 | 133 | 135 | at_endpoint | 0.278 | 14.15 | 14.15 | s4:+0.141, s3:+0.113, s20:+0.108 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 121 | 122 | preventive_schedule | 0.497 | 35.59 | 0.70 | s4:+0.108, s3:+0.084, s20:+0.065 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 121 | 123 | preventive_schedule | 0.497 | 35.59 | 0.70 | s4:+0.108, s3:+0.084, s20:+0.065 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.423 | indefinido | indefinido | s4:+0.119, s3:+0.095, s20:+0.076 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.438 | indefinido | indefinido | s4:+0.115, s3:+0.095, s20:+0.076 |
| 3 | HI_MARKER_D1 | 121 | 122 | preventive_schedule | 0.497 | indefinido | indefinido | s4:+0.108, s3:+0.084, s20:+0.065 |
| 3 | HI_MARKER_D2 | 121 | 123 | preventive_schedule | 0.497 | indefinido | indefinido | s4:+0.108, s3:+0.084, s20:+0.065 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=124, A=124.
- Repetição2: G=118, A=118.
- Repetição3: G=121, A=121.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | indefinido | indefinido | 26.67% | 20.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | indefinido | indefinido | 26.67% | 20.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.18 | 0.31 | 26.67% | 3.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.18 | 0.31 | 26.67% | 3.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 25.61 | 15 | 1.30 | 0.45 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 25.61 | 15 | 1.30 | 0.45 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 23.33% | 16.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 38.16 | 15 | 1.37 | 0.73 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 38.16 | 15 | 1.37 | 0.73 | 0.00% | 26.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.37 | 0.73 | 0.00% | 26.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.37 | 0.73 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | indefinido | indefinido | 36.67% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | indefinido | indefinido | 36.67% | 26.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.20 | 0.03 | 0.00% | 3.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.20 | 0.03 | 0.00% | 3.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 27.32 | 15 | 1.80 | 0.26 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 27.32 | 15 | 1.80 | 0.26 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 3.33% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 39.06 | 15 | 2.20 | 0.64 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 39.06 | 15 | 2.20 | 0.64 | 0.00% | 26.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.20 | 0.64 | 0.00% | 26.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.20 | 0.64 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.56 | 0.28 | 10.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.56 | 0.28 | 10.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.30 | 0.00 | 10.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.30 | 0.00 | 10.00% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 20.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.41 | 15 | 1.50 | 0.33 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.41 | 15 | 1.57 | 0.33 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.67 | 0.48 | 10.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.76 | 0.48 | 3.33% | 10.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 34.89 | 15 | 1.63 | 0.35 | 0.00% | 33.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 34.89 | 15 | 1.63 | 0.35 | 0.00% | 33.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.60 | 0.35 | 0.00% | 33.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.60 | 0.35 | 0.00% | 33.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
