# FD001, motor39 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u39.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 125 | 126 | preventive_schedule | 0.276 | indefinido | indefinido | s7:+0.169, s4:+0.160, s11:+0.089 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 120 | 122 | preventive_schedule | 0.383 | indefinido | indefinido | s4:+0.137, s7:+0.126, s21:+0.084 |
| 1 | HI_WAIT_SELECTED_D1 | 125 | 126 | preventive_schedule | 0.276 | indefinido | indefinido | s7:+0.169, s4:+0.160, s11:+0.089 |
| 1 | HI_WAIT_SELECTED_D2 | 125 | 127 | preventive_schedule | 0.276 | indefinido | indefinido | s7:+0.169, s4:+0.160, s11:+0.089 |
| 1 | ISO_POINT_M15_D1 | 125 | 126 | preventive_schedule | 0.276 | 15.41 | 15.41 | s7:+0.169, s4:+0.160, s11:+0.089 |
| 1 | ISO_POINT_M15_D2 | 125 | 127 | preventive_schedule | 0.276 | 15.41 | 15.41 | s7:+0.169, s4:+0.160, s11:+0.089 |
| 1 | ISO_LOWER98_M15_D1 | 115 | 116 | preventive_schedule | 0.489 | 33.00 | 9.32 | s4:+0.116, s7:+0.109, s21:+0.070 |
| 1 | ISO_LOWER98_M15_D2 | 115 | 117 | preventive_schedule | 0.489 | 33.00 | 9.32 | s4:+0.116, s7:+0.109, s21:+0.070 |
| 1 | RF_SLOPE_POINT_M15_D1 | 125 | 126 | preventive_schedule | 0.276 | 14.83 | 14.83 | s7:+0.169, s4:+0.160, s11:+0.089 |
| 1 | RF_SLOPE_POINT_M15_D2 | 125 | 127 | preventive_schedule | 0.276 | 14.83 | 14.83 | s7:+0.169, s4:+0.160, s11:+0.089 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 115 | 116 | preventive_schedule | 0.489 | 33.18 | 0.00 | s4:+0.116, s7:+0.109, s21:+0.070 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 115 | 117 | preventive_schedule | 0.489 | 33.18 | 0.00 | s4:+0.116, s7:+0.109, s21:+0.070 |
| 1 | AGE_D1 | indefinido | indefinido | endpoint_without_decision | 0.252 | indefinido | indefinido | s7:+0.184, s4:+0.159, s11:+0.094 |
| 1 | AGE_D2 | indefinido | indefinido | endpoint_without_decision | 0.252 | indefinido | indefinido | s7:+0.184, s4:+0.159, s11:+0.094 |
| 1 | HI_MARKER_D1 | 115 | 116 | preventive_schedule | 0.489 | indefinido | indefinido | s4:+0.116, s7:+0.109, s21:+0.070 |
| 1 | HI_MARKER_D2 | 115 | 117 | preventive_schedule | 0.489 | indefinido | indefinido | s4:+0.116, s7:+0.109, s21:+0.070 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 118 | 119 | preventive_schedule | 0.376 | indefinido | indefinido | s15:+0.170, s2:+0.138, s8:+0.068 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 118 | 120 | preventive_schedule | 0.376 | indefinido | indefinido | s15:+0.170, s2:+0.138, s8:+0.068 |
| 2 | HI_WAIT_SELECTED_D1 | 124 | 125 | preventive_schedule | 0.209 | indefinido | indefinido | s15:+0.216, s2:+0.191, s8:+0.084 |
| 2 | HI_WAIT_SELECTED_D2 | 124 | 126 | preventive_schedule | 0.209 | indefinido | indefinido | s15:+0.216, s2:+0.191, s8:+0.084 |
| 2 | ISO_POINT_M15_D1 | 127 | 128 | at_endpoint | 0.106 | 13.08 | 13.08 | s15:+0.240, s2:+0.237, s8:+0.097 |
| 2 | ISO_POINT_M15_D2 | 125 | 127 | preventive_schedule | 0.182 | 16.57 | 16.57 | s15:+0.224, s2:+0.194, s8:+0.088 |
| 2 | ISO_LOWER98_M15_D1 | 114 | 115 | preventive_schedule | 0.498 | 37.87 | 11.00 | s15:+0.140, s2:+0.085, s8:+0.063 |
| 2 | ISO_LOWER98_M15_D2 | 114 | 116 | preventive_schedule | 0.498 | 37.87 | 11.00 | s15:+0.140, s2:+0.085, s8:+0.063 |
| 2 | RF_SLOPE_POINT_M15_D1 | 123 | 124 | preventive_schedule | 0.221 | 13.74 | 13.74 | s15:+0.215, s2:+0.190, s8:+0.080 |
| 2 | RF_SLOPE_POINT_M15_D2 | 123 | 125 | preventive_schedule | 0.221 | 13.74 | 13.74 | s15:+0.215, s2:+0.190, s8:+0.080 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 114 | 115 | preventive_schedule | 0.498 | 35.07 | 0.00 | s15:+0.140, s2:+0.085, s8:+0.063 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 114 | 116 | preventive_schedule | 0.498 | 35.07 | 0.00 | s15:+0.140, s2:+0.085, s8:+0.063 |
| 2 | AGE_D1 | indefinido | indefinido | endpoint_without_decision | 0.106 | indefinido | indefinido | s15:+0.240, s2:+0.237, s8:+0.097 |
| 2 | AGE_D2 | indefinido | indefinido | endpoint_without_decision | 0.106 | indefinido | indefinido | s15:+0.240, s2:+0.237, s8:+0.097 |
| 2 | HI_MARKER_D1 | 114 | 115 | preventive_schedule | 0.498 | indefinido | indefinido | s15:+0.140, s2:+0.085, s8:+0.063 |
| 2 | HI_MARKER_D2 | 114 | 116 | preventive_schedule | 0.498 | indefinido | indefinido | s15:+0.140, s2:+0.085, s8:+0.063 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 120 | 121 | preventive_schedule | 0.284 | indefinido | indefinido | s12:+0.128, s7:+0.127, s15:+0.103 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 120 | 122 | preventive_schedule | 0.284 | indefinido | indefinido | s12:+0.128, s7:+0.127, s15:+0.103 |
| 3 | HI_WAIT_SELECTED_D1 | 122 | 123 | preventive_schedule | 0.222 | indefinido | indefinido | s7:+0.145, s12:+0.135, s15:+0.110 |
| 3 | HI_WAIT_SELECTED_D2 | 122 | 124 | preventive_schedule | 0.222 | indefinido | indefinido | s7:+0.145, s12:+0.135, s15:+0.110 |
| 3 | ISO_POINT_M15_D1 | 123 | 124 | preventive_schedule | 0.193 | 15.05 | 15.05 | s7:+0.152, s12:+0.141, s15:+0.113 |
| 3 | ISO_POINT_M15_D2 | 122 | 124 | preventive_schedule | 0.222 | 16.70 | 16.70 | s7:+0.145, s12:+0.135, s15:+0.110 |
| 3 | ISO_LOWER98_M15_D1 | 112 | 113 | preventive_schedule | 0.486 | 35.42 | 15.00 | s7:+0.096, s20:+0.090, s12:+0.086 |
| 3 | ISO_LOWER98_M15_D2 | 112 | 114 | preventive_schedule | 0.486 | 35.42 | 15.00 | s7:+0.096, s20:+0.090, s12:+0.086 |
| 3 | RF_SLOPE_POINT_M15_D1 | 122 | 123 | preventive_schedule | 0.222 | 11.92 | 11.92 | s7:+0.145, s12:+0.135, s15:+0.110 |
| 3 | RF_SLOPE_POINT_M15_D2 | 121 | 123 | preventive_schedule | 0.251 | 16.95 | 16.95 | s7:+0.139, s12:+0.130, s15:+0.108 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 112 | 113 | preventive_schedule | 0.486 | 39.34 | 13.74 | s7:+0.096, s20:+0.090, s12:+0.086 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 112 | 114 | preventive_schedule | 0.486 | 39.34 | 13.74 | s7:+0.096, s20:+0.090, s12:+0.086 |
| 3 | AGE_D1 | indefinido | indefinido | endpoint_without_decision | 0.085 | indefinido | indefinido | s7:+0.186, s12:+0.162, s2:+0.134 |
| 3 | AGE_D2 | indefinido | indefinido | endpoint_without_decision | 0.085 | indefinido | indefinido | s7:+0.186, s12:+0.162, s2:+0.134 |
| 3 | HI_MARKER_D1 | 112 | 113 | preventive_schedule | 0.486 | indefinido | indefinido | s7:+0.096, s20:+0.090, s12:+0.086 |
| 3 | HI_MARKER_D2 | 112 | 114 | preventive_schedule | 0.486 | indefinido | indefinido | s7:+0.096, s20:+0.090, s12:+0.086 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=115, A=115.
- Repetição2: G=114, A=114.
- Repetição3: G=112, A=112.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.90 | 0.46 | 3.33% | 13.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.93 | 0.32 | 0.00% | 16.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 0.93 | 0.00 | 10.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 0.93 | 0.00 | 10.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.56 | 0.05 | 16.67% | 36.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.56 | 0.05 | 16.67% | 36.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 23.68 | 15 | 1.13 | 0.38 | 0.00% | 20.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 23.68 | 15 | 1.13 | 0.38 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.38 | 0.32 | 3.33% | 36.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.50 | 0.35 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 41.91 | 15 | 1.13 | 0.38 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 41.91 | 15 | 1.13 | 0.38 | 0.00% | 20.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.13 | 0.38 | 0.00% | 20.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.13 | 0.38 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.77 | 0.29 | 0.00% | 6.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.77 | 0.29 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 0.72 | 0.00 | 3.33% | 20.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 0.72 | 0.00 | 3.33% | 20.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.64 | 0.43 | 6.67% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.72 | 0.29 | 3.33% | 20.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 26.87 | 15 | 0.83 | 0.16 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 26.87 | 15 | 0.83 | 0.16 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.97 | 0.43 | 0.00% | 6.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.03 | 0.54 | 0.00% | 6.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 35.90 | 15 | 0.83 | 0.16 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 35.90 | 15 | 0.83 | 0.16 | 0.00% | 36.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 0.83 | 0.16 | 0.00% | 36.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 0.83 | 0.16 | 0.00% | 36.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.70 | 0.25 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.70 | 0.25 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.33 | 0.17 | 0.00% | 0.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.33 | 0.17 | 0.00% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.90 | 0.23 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.83 | 0.11 | 0.00% | 36.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 20.42 | 15 | 1.30 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 20.42 | 15 | 1.30 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.83 | 0.28 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.87 | 0.11 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 25.60 | 15 | 1.10 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 25.60 | 15 | 1.17 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.33 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.33 | 0.70 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
