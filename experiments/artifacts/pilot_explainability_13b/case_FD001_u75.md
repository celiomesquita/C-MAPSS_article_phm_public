# FD001, motor75 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u75.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 208 | 209 | preventive_schedule | 0.298 | indefinido | indefinido | s2:+0.129, s20:+0.117, s7:+0.082 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 208 | 210 | preventive_schedule | 0.298 | indefinido | indefinido | s2:+0.129, s20:+0.117, s7:+0.082 |
| 1 | HI_WAIT_SELECTED_D1 | 197 | 198 | preventive_schedule | 0.428 | indefinido | indefinido | s2:+0.099, s20:+0.093, s7:+0.073 |
| 1 | HI_WAIT_SELECTED_D2 | 197 | 199 | preventive_schedule | 0.428 | indefinido | indefinido | s2:+0.099, s20:+0.093, s7:+0.073 |
| 1 | ISO_POINT_M15_D1 | 217 | 218 | preventive_schedule | 0.202 | 15.60 | 15.60 | s20:+0.134, s2:+0.121, s15:+0.106 |
| 1 | ISO_POINT_M15_D2 | 213 | 215 | preventive_schedule | 0.232 | 16.07 | 16.07 | s20:+0.130, s2:+0.122, s15:+0.100 |
| 1 | ISO_LOWER98_M15_D1 | 187 | 188 | preventive_schedule | 0.497 | 37.97 | 13.00 | s20:+0.082, s2:+0.081, s7:+0.071 |
| 1 | ISO_LOWER98_M15_D2 | 187 | 189 | preventive_schedule | 0.497 | 37.97 | 13.00 | s20:+0.082, s2:+0.081, s7:+0.071 |
| 1 | RF_SLOPE_POINT_M15_D1 | 215 | 216 | preventive_schedule | 0.208 | 14.55 | 14.55 | s20:+0.130, s2:+0.125, s15:+0.106 |
| 1 | RF_SLOPE_POINT_M15_D2 | 211 | 213 | preventive_schedule | 0.244 | 16.84 | 16.84 | s20:+0.130, s2:+0.128, s7:+0.090 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 187 | 188 | preventive_schedule | 0.497 | 38.05 | 3.85 | s20:+0.082, s2:+0.081, s7:+0.071 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 187 | 189 | preventive_schedule | 0.497 | 38.05 | 3.85 | s20:+0.082, s2:+0.081, s7:+0.071 |
| 1 | AGE_D1 | 145 | 146 | preventive_schedule | 0.759 | indefinido | indefinido | s2:+0.055, s7:+0.035, s12:+0.033 |
| 1 | AGE_D2 | 144 | 146 | preventive_schedule | 0.752 | indefinido | indefinido | s2:+0.057, s7:+0.037, s12:+0.031 |
| 1 | HI_MARKER_D1 | 187 | 188 | preventive_schedule | 0.497 | indefinido | indefinido | s20:+0.082, s2:+0.081, s7:+0.071 |
| 1 | HI_MARKER_D2 | 187 | 189 | preventive_schedule | 0.497 | indefinido | indefinido | s20:+0.082, s2:+0.081, s7:+0.071 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 196 | 197 | preventive_schedule | 0.394 | indefinido | indefinido | s2:+0.100, s7:+0.096, s11:+0.095 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 196 | 198 | preventive_schedule | 0.394 | indefinido | indefinido | s2:+0.100, s7:+0.096, s11:+0.095 |
| 2 | HI_WAIT_SELECTED_D1 | 194 | 195 | preventive_schedule | 0.416 | indefinido | indefinido | s7:+0.095, s11:+0.094, s2:+0.091 |
| 2 | HI_WAIT_SELECTED_D2 | 189 | 191 | preventive_schedule | 0.459 | indefinido | indefinido | s7:+0.096, s11:+0.088, s2:+0.082 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.024 | 16.66 | 16.66 | s7:+0.168, s2:+0.167, s11:+0.149 |
| 2 | ISO_POINT_M15_D2 | 222 | 224 | preventive_schedule | 0.104 | 16.66 | 16.66 | s7:+0.155, s2:+0.140, s11:+0.134 |
| 2 | ISO_LOWER98_M15_D1 | 185 | 186 | preventive_schedule | 0.469 | 41.62 | 13.36 | s11:+0.090, s7:+0.089, s2:+0.086 |
| 2 | ISO_LOWER98_M15_D2 | 184 | 186 | preventive_schedule | 0.488 | 45.26 | 17.00 | s7:+0.088, s11:+0.087, s2:+0.082 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.024 | 26.63 | 26.63 | s7:+0.168, s2:+0.167, s11:+0.149 |
| 2 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.024 | 26.63 | 26.63 | s7:+0.168, s2:+0.167, s11:+0.149 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 184 | 185 | preventive_schedule | 0.488 | 41.29 | 4.83 | s7:+0.088, s11:+0.087, s2:+0.082 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 184 | 186 | preventive_schedule | 0.488 | 41.29 | 4.83 | s7:+0.088, s11:+0.087, s2:+0.082 |
| 2 | AGE_D1 | 133 | 134 | preventive_schedule | 0.807 | indefinido | indefinido | s2:+0.045, s11:+0.044, s7:+0.040 |
| 2 | AGE_D2 | 132 | 134 | preventive_schedule | 0.809 | indefinido | indefinido | s2:+0.043, s11:+0.040, s7:+0.040 |
| 2 | HI_MARKER_D1 | 184 | 185 | preventive_schedule | 0.488 | indefinido | indefinido | s7:+0.088, s11:+0.087, s2:+0.082 |
| 2 | HI_MARKER_D2 | 184 | 186 | preventive_schedule | 0.488 | indefinido | indefinido | s7:+0.088, s11:+0.087, s2:+0.082 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 194 | 195 | preventive_schedule | 0.391 | indefinido | indefinido | s4:+0.153, s8:+0.098, s2:+0.089 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 194 | 196 | preventive_schedule | 0.391 | indefinido | indefinido | s4:+0.153, s8:+0.098, s2:+0.089 |
| 3 | HI_WAIT_SELECTED_D1 | 194 | 195 | preventive_schedule | 0.391 | indefinido | indefinido | s4:+0.153, s8:+0.098, s2:+0.089 |
| 3 | HI_WAIT_SELECTED_D2 | 189 | 191 | preventive_schedule | 0.435 | indefinido | indefinido | s4:+0.142, s8:+0.094, s7:+0.085 |
| 3 | ISO_POINT_M15_D1 | 221 | 222 | preventive_schedule | 0.106 | 15.64 | 15.64 | s4:+0.217, s8:+0.140, s7:+0.135 |
| 3 | ISO_POINT_M15_D2 | 216 | 218 | preventive_schedule | 0.160 | 16.83 | 16.83 | s4:+0.205, s8:+0.137, s2:+0.122 |
| 3 | ISO_LOWER98_M15_D1 | 184 | 185 | preventive_schedule | 0.488 | 40.76 | 15.00 | s4:+0.134, s2:+0.080, s7:+0.078 |
| 3 | ISO_LOWER98_M15_D2 | 184 | 186 | preventive_schedule | 0.488 | 40.76 | 15.00 | s4:+0.134, s2:+0.080, s7:+0.078 |
| 3 | RF_SLOPE_POINT_M15_D1 | 228 | 229 | at_endpoint | 0.003 | 9.13 | 9.13 | s4:+0.240, s2:+0.163, s8:+0.154 |
| 3 | RF_SLOPE_POINT_M15_D2 | 228 | 230 | late_schedule | 0.003 | 9.13 | 9.13 | s4:+0.240, s2:+0.163, s8:+0.154 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 184 | 185 | preventive_schedule | 0.488 | 51.24 | 12.74 | s4:+0.134, s2:+0.080, s7:+0.078 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 184 | 186 | preventive_schedule | 0.488 | 51.24 | 12.74 | s4:+0.134, s2:+0.080, s7:+0.078 |
| 3 | AGE_D1 | 133 | 134 | preventive_schedule | 0.780 | indefinido | indefinido | s4:+0.056, s2:+0.043, s8:+0.041 |
| 3 | AGE_D2 | 132 | 134 | preventive_schedule | 0.778 | indefinido | indefinido | s4:+0.060, s2:+0.042, s8:+0.041 |
| 3 | HI_MARKER_D1 | 184 | 185 | preventive_schedule | 0.488 | indefinido | indefinido | s4:+0.134, s2:+0.080, s7:+0.078 |
| 3 | HI_MARKER_D2 | 184 | 186 | preventive_schedule | 0.488 | indefinido | indefinido | s4:+0.134, s2:+0.080, s7:+0.078 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=187, A=187.
- Repetição2: G=184, A=184.
- Repetição3: G=184, A=184.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.57 | 0.58 | 0.00% | 36.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.57 | 0.58 | 0.00% | 36.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.93 | 0.00 | 0.00% | 26.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.93 | 0.00 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 3.50 | 1.61 | 0.00% | 40.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.73 | 0.95 | 0.00% | 36.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 24.97 | 15 | 2.93 | 0.84 | 0.00% | 36.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 24.97 | 15 | 2.93 | 0.84 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.07 | 1.28 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.97 | 0.74 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.20 | 15 | 2.93 | 0.84 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.20 | 15 | 2.93 | 0.84 | 0.00% | 36.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.93 | 0.84 | 0.00% | 36.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.93 | 0.84 | 0.00% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.93 | 0.81 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.93 | 0.81 | 0.00% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.43 | 0.30 | 0.00% | 0.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.43 | 0.40 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 30.00% | 30.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.03 | 0.48 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 28.26 | 15 | 2.87 | 0.57 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 28.26 | 15 | 2.43 | 0.81 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 30.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 30.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 36.46 | 15 | 2.43 | 0.71 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 36.46 | 15 | 2.43 | 0.71 | 0.00% | 30.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.43 | 0.81 | 0.00% | 30.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.43 | 0.81 | 0.00% | 30.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.07 | 0.67 | 0.00% | 30.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.07 | 0.67 | 0.00% | 30.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.83 | 0.20 | 0.00% | 0.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.83 | 0.62 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.77 | 0.67 | 0.00% | 30.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.10 | 1.05 | 0.00% | 33.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.76 | 15 | 2.83 | 0.92 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.76 | 15 | 2.83 | 0.92 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.90 | 0.08 | 33.33% | 13.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.96 | 0.07 | 20.00% | 6.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 38.50 | 15 | 2.93 | 0.92 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 38.50 | 15 | 2.83 | 0.92 | 0.00% | 20.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.83 | 0.92 | 0.00% | 20.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.83 | 0.92 | 0.00% | 20.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
