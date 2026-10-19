# FD001, motor8 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u8.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 140 | 141 | preventive_schedule | 0.396 | indefinido | indefinido | s7:+0.105, s15:+0.097, s12:+0.070 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 140 | 142 | preventive_schedule | 0.396 | indefinido | indefinido | s7:+0.105, s15:+0.097, s12:+0.070 |
| 1 | HI_WAIT_SELECTED_D1 | 143 | 144 | preventive_schedule | 0.342 | indefinido | indefinido | s7:+0.112, s15:+0.105, s12:+0.079 |
| 1 | HI_WAIT_SELECTED_D2 | 143 | 145 | preventive_schedule | 0.342 | indefinido | indefinido | s7:+0.112, s15:+0.105, s12:+0.079 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.254 | 19.23 | 19.23 | s7:+0.128, s15:+0.106, s12:+0.095 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.254 | 19.23 | 19.23 | s7:+0.128, s15:+0.106, s12:+0.095 |
| 1 | ISO_LOWER98_M15_D1 | 133 | 134 | preventive_schedule | 0.490 | 37.62 | 9.00 | s7:+0.087, s15:+0.080, s12:+0.061 |
| 1 | ISO_LOWER98_M15_D2 | 133 | 135 | preventive_schedule | 0.490 | 37.62 | 9.00 | s7:+0.087, s15:+0.080, s12:+0.061 |
| 1 | RF_SLOPE_POINT_M15_D1 | 148 | 149 | preventive_schedule | 0.284 | 15.45 | 15.45 | s7:+0.121, s15:+0.098, s12:+0.090 |
| 1 | RF_SLOPE_POINT_M15_D2 | 148 | 150 | at_endpoint | 0.284 | 15.45 | 15.45 | s7:+0.121, s15:+0.098, s12:+0.090 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 133 | 134 | preventive_schedule | 0.490 | 37.40 | 0.00 | s7:+0.087, s15:+0.080, s12:+0.061 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 133 | 135 | preventive_schedule | 0.490 | 37.40 | 0.00 | s7:+0.087, s15:+0.080, s12:+0.061 |
| 1 | AGE_D1 | 145 | 146 | preventive_schedule | 0.319 | indefinido | indefinido | s7:+0.116, s15:+0.102, s12:+0.086 |
| 1 | AGE_D2 | 144 | 146 | preventive_schedule | 0.331 | indefinido | indefinido | s7:+0.115, s15:+0.105, s12:+0.082 |
| 1 | HI_MARKER_D1 | 133 | 134 | preventive_schedule | 0.490 | indefinido | indefinido | s7:+0.087, s15:+0.080, s12:+0.061 |
| 1 | HI_MARKER_D2 | 133 | 135 | preventive_schedule | 0.490 | indefinido | indefinido | s7:+0.087, s15:+0.080, s12:+0.061 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 143 | 144 | preventive_schedule | 0.284 | indefinido | indefinido | s12:+0.117, s20:+0.074, s7:+0.069 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 143 | 145 | preventive_schedule | 0.284 | indefinido | indefinido | s12:+0.117, s20:+0.074, s7:+0.069 |
| 2 | HI_WAIT_SELECTED_D1 | 140 | 141 | preventive_schedule | 0.345 | indefinido | indefinido | s12:+0.104, s20:+0.066, s7:+0.064 |
| 2 | HI_WAIT_SELECTED_D2 | 140 | 142 | preventive_schedule | 0.345 | indefinido | indefinido | s12:+0.104, s20:+0.066, s7:+0.064 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.179 | 23.61 | 23.61 | s12:+0.140, s20:+0.086, s3:+0.083 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.179 | 23.61 | 23.61 | s12:+0.140, s20:+0.086, s3:+0.083 |
| 2 | ISO_LOWER98_M15_D1 | 130 | 131 | preventive_schedule | 0.497 | 55.28 | 16.00 | s12:+0.080, s20:+0.056, s4:+0.048 |
| 2 | ISO_LOWER98_M15_D2 | 130 | 132 | preventive_schedule | 0.497 | 55.28 | 16.00 | s12:+0.080, s20:+0.056, s4:+0.048 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.179 | 16.35 | 16.35 | s12:+0.140, s20:+0.086, s3:+0.083 |
| 2 | RF_SLOPE_POINT_M15_D2 | 143 | 145 | preventive_schedule | 0.284 | 16.05 | 16.05 | s12:+0.117, s20:+0.074, s7:+0.069 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 130 | 131 | preventive_schedule | 0.497 | 42.01 | 0.00 | s12:+0.080, s20:+0.056, s4:+0.048 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 130 | 132 | preventive_schedule | 0.497 | 42.01 | 0.00 | s12:+0.080, s20:+0.056, s4:+0.048 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.548 | indefinido | indefinido | s12:+0.078, s20:+0.052, s11:+0.042 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.565 | indefinido | indefinido | s12:+0.075, s20:+0.051, s11:+0.041 |
| 2 | HI_MARKER_D1 | 130 | 131 | preventive_schedule | 0.497 | indefinido | indefinido | s12:+0.080, s20:+0.056, s4:+0.048 |
| 2 | HI_MARKER_D2 | 130 | 132 | preventive_schedule | 0.497 | indefinido | indefinido | s12:+0.080, s20:+0.056, s4:+0.048 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 148 | 149 | preventive_schedule | 0.299 | indefinido | indefinido | s20:+0.135, s4:+0.124, s12:+0.113 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 148 | 150 | at_endpoint | 0.299 | indefinido | indefinido | s20:+0.135, s4:+0.124, s12:+0.113 |
| 3 | HI_WAIT_SELECTED_D1 | 144 | 145 | preventive_schedule | 0.355 | indefinido | indefinido | s20:+0.123, s4:+0.110, s12:+0.104 |
| 3 | HI_WAIT_SELECTED_D2 | 144 | 146 | preventive_schedule | 0.355 | indefinido | indefinido | s20:+0.123, s4:+0.110, s12:+0.104 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.273 | 19.71 | 19.71 | s20:+0.142, s4:+0.125, s12:+0.120 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.273 | 19.71 | 19.71 | s20:+0.142, s4:+0.125, s12:+0.120 |
| 3 | ISO_LOWER98_M15_D1 | 134 | 135 | preventive_schedule | 0.492 | 39.68 | 9.00 | s20:+0.093, s4:+0.091, s11:+0.085 |
| 3 | ISO_LOWER98_M15_D2 | 134 | 136 | preventive_schedule | 0.492 | 39.68 | 9.00 | s20:+0.093, s4:+0.091, s11:+0.085 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.273 | 18.33 | 18.33 | s20:+0.142, s4:+0.125, s12:+0.120 |
| 3 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.273 | 18.33 | 18.33 | s20:+0.142, s4:+0.125, s12:+0.120 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 134 | 135 | preventive_schedule | 0.492 | 31.67 | 0.00 | s20:+0.093, s4:+0.091, s11:+0.085 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 134 | 136 | preventive_schedule | 0.492 | 31.67 | 0.00 | s20:+0.093, s4:+0.091, s11:+0.085 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.590 | indefinido | indefinido | s20:+0.086, s4:+0.069, s11:+0.068 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.605 | indefinido | indefinido | s20:+0.085, s4:+0.067, s11:+0.066 |
| 3 | HI_MARKER_D1 | 134 | 135 | preventive_schedule | 0.492 | indefinido | indefinido | s20:+0.093, s4:+0.091, s11:+0.085 |
| 3 | HI_MARKER_D2 | 134 | 136 | preventive_schedule | 0.492 | indefinido | indefinido | s20:+0.093, s4:+0.091, s11:+0.085 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=133, A=133.
- Repetição2: G=130, A=130.
- Repetição3: G=134, A=134.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.73 | 0.95 | 0.00% | 36.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.73 | 0.95 | 0.00% | 36.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.30 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.30 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.33% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 3.33% | 0.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 28.62 | 15 | 1.30 | 0.55 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 28.62 | 15 | 1.30 | 0.55 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.36 | 0.17 | 16.67% | 80.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.03 | 1.06 | 0.00% | 43.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 49.06 | 15 | 1.30 | 0.55 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 49.06 | 15 | 1.30 | 0.55 | 0.00% | 26.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.30 | 0.55 | 0.00% | 26.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.30 | 0.55 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.97 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.97 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.30 | 0.00 | 0.00% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.30 | 0.00 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 39.28 | 15 | 1.30 | 0.37 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 39.28 | 15 | 1.30 | 0.37 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 86.67% | 86.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.07 | 0.11 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 43.83 | 15 | 1.30 | 0.37 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 43.83 | 15 | 1.30 | 0.37 | 0.00% | 36.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.30 | 0.37 | 0.00% | 36.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.30 | 0.37 | 0.00% | 36.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.04 | 0.63 | 20.00% | 36.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.04 | 0.63 | 20.00% | 36.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.47 | 0.03 | 0.00% | 3.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.47 | 0.03 | 0.00% | 3.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 30.68 | 15 | 1.47 | 0.55 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 30.68 | 15 | 1.47 | 0.55 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 6.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 10.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 36.15 | 15 | 1.47 | 0.55 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 36.15 | 15 | 1.47 | 0.55 | 0.00% | 26.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.47 | 0.55 | 0.00% | 26.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.47 | 0.55 | 0.00% | 26.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
