# FD001, motor16 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u16.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 207 | 208 | preventive_schedule | 0.285 | indefinido | indefinido | s7:+0.163, s4:+0.132, s21:+0.082 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 195 | 197 | preventive_schedule | 0.398 | indefinido | indefinido | s7:+0.148, s4:+0.114, s21:+0.075 |
| 1 | HI_WAIT_SELECTED_D1 | 198 | 199 | preventive_schedule | 0.370 | indefinido | indefinido | s7:+0.146, s4:+0.121, s21:+0.083 |
| 1 | HI_WAIT_SELECTED_D2 | 198 | 200 | preventive_schedule | 0.370 | indefinido | indefinido | s7:+0.146, s4:+0.121, s21:+0.083 |
| 1 | ISO_POINT_M15_D1 | 208 | 209 | at_endpoint | 0.261 | 15.41 | 15.41 | s7:+0.171, s4:+0.138, s21:+0.085 |
| 1 | ISO_POINT_M15_D2 | 208 | 210 | late_schedule | 0.261 | 15.41 | 15.41 | s7:+0.171, s4:+0.138, s21:+0.085 |
| 1 | ISO_LOWER98_M15_D1 | 188 | 189 | preventive_schedule | 0.487 | 33.00 | 9.32 | s7:+0.124, s4:+0.095, s21:+0.068 |
| 1 | ISO_LOWER98_M15_D2 | 188 | 190 | preventive_schedule | 0.487 | 33.00 | 9.32 | s7:+0.124, s4:+0.095, s21:+0.068 |
| 1 | RF_SLOPE_POINT_M15_D1 | 199 | 200 | preventive_schedule | 0.351 | 14.31 | 14.31 | s7:+0.152, s4:+0.124, s21:+0.086 |
| 1 | RF_SLOPE_POINT_M15_D2 | 199 | 201 | preventive_schedule | 0.351 | 14.31 | 14.31 | s7:+0.152, s4:+0.124, s21:+0.086 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 188 | 189 | preventive_schedule | 0.487 | 39.37 | 0.00 | s7:+0.124, s4:+0.095, s21:+0.068 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 188 | 190 | preventive_schedule | 0.487 | 39.37 | 0.00 | s7:+0.124, s4:+0.095, s21:+0.068 |
| 1 | AGE_D1 | 135 | 136 | preventive_schedule | 0.810 | indefinido | indefinido | s4:+0.049, s7:+0.030, s21:+0.022 |
| 1 | AGE_D2 | 134 | 136 | preventive_schedule | 0.794 | indefinido | indefinido | s4:+0.050, s7:+0.038, s21:+0.026 |
| 1 | HI_MARKER_D1 | 188 | 189 | preventive_schedule | 0.487 | indefinido | indefinido | s7:+0.124, s4:+0.095, s21:+0.068 |
| 1 | HI_MARKER_D2 | 188 | 190 | preventive_schedule | 0.487 | indefinido | indefinido | s7:+0.124, s4:+0.095, s21:+0.068 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 194 | 195 | preventive_schedule | 0.396 | indefinido | indefinido | s7:+0.144, s20:+0.105, s2:+0.092 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 194 | 196 | preventive_schedule | 0.396 | indefinido | indefinido | s7:+0.144, s20:+0.105, s2:+0.092 |
| 2 | HI_WAIT_SELECTED_D1 | 196 | 197 | preventive_schedule | 0.376 | indefinido | indefinido | s7:+0.144, s20:+0.108, s2:+0.097 |
| 2 | HI_WAIT_SELECTED_D2 | 196 | 198 | preventive_schedule | 0.376 | indefinido | indefinido | s7:+0.144, s20:+0.108, s2:+0.097 |
| 2 | ISO_POINT_M15_D1 | 208 | 209 | at_endpoint | 0.191 | 13.21 | 13.21 | s7:+0.170, s2:+0.146, s20:+0.139 |
| 2 | ISO_POINT_M15_D2 | 204 | 206 | preventive_schedule | 0.264 | 16.55 | 16.55 | s7:+0.151, s20:+0.133, s2:+0.127 |
| 2 | ISO_LOWER98_M15_D1 | 186 | 187 | preventive_schedule | 0.482 | 34.84 | 11.80 | s7:+0.121, s20:+0.091, s2:+0.086 |
| 2 | ISO_LOWER98_M15_D2 | 186 | 188 | preventive_schedule | 0.482 | 34.84 | 11.80 | s7:+0.121, s20:+0.091, s2:+0.086 |
| 2 | RF_SLOPE_POINT_M15_D1 | 203 | 204 | preventive_schedule | 0.271 | 13.17 | 13.17 | s7:+0.151, s20:+0.131, s2:+0.125 |
| 2 | RF_SLOPE_POINT_M15_D2 | 203 | 205 | preventive_schedule | 0.271 | 13.17 | 13.17 | s7:+0.151, s20:+0.131, s2:+0.125 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 186 | 187 | preventive_schedule | 0.482 | 35.91 | 8.61 | s7:+0.121, s20:+0.091, s2:+0.086 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 186 | 188 | preventive_schedule | 0.482 | 35.91 | 8.61 | s7:+0.121, s20:+0.091, s2:+0.086 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.813 | indefinido | indefinido | s2:+0.048, s20:+0.042, s7:+0.031 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.813 | indefinido | indefinido | s2:+0.045, s7:+0.038, s20:+0.036 |
| 2 | HI_MARKER_D1 | 186 | 187 | preventive_schedule | 0.482 | indefinido | indefinido | s7:+0.121, s20:+0.091, s2:+0.086 |
| 2 | HI_MARKER_D2 | 186 | 188 | preventive_schedule | 0.482 | indefinido | indefinido | s7:+0.121, s20:+0.091, s2:+0.086 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 199 | 200 | preventive_schedule | 0.296 | indefinido | indefinido | s20:+0.159, s4:+0.134, s12:+0.119 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 199 | 201 | preventive_schedule | 0.296 | indefinido | indefinido | s20:+0.159, s4:+0.134, s12:+0.119 |
| 3 | HI_WAIT_SELECTED_D1 | 192 | 193 | preventive_schedule | 0.397 | indefinido | indefinido | s20:+0.140, s4:+0.111, s12:+0.102 |
| 3 | HI_WAIT_SELECTED_D2 | 192 | 194 | preventive_schedule | 0.397 | indefinido | indefinido | s20:+0.140, s4:+0.111, s12:+0.102 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.193 | 16.82 | 16.82 | s20:+0.184, s4:+0.148, s12:+0.140 |
| 3 | ISO_POINT_M15_D2 | 208 | 210 | late_schedule | 0.193 | 16.82 | 16.82 | s20:+0.184, s4:+0.148, s12:+0.140 |
| 3 | ISO_LOWER98_M15_D1 | 182 | 183 | preventive_schedule | 0.499 | 39.68 | 9.00 | s20:+0.118, s4:+0.099, s12:+0.080 |
| 3 | ISO_LOWER98_M15_D2 | 182 | 184 | preventive_schedule | 0.499 | 39.68 | 9.00 | s20:+0.118, s4:+0.099, s12:+0.080 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.193 | 18.85 | 18.85 | s20:+0.184, s4:+0.148, s12:+0.140 |
| 3 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.193 | 18.85 | 18.85 | s20:+0.184, s4:+0.148, s12:+0.140 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 182 | 183 | preventive_schedule | 0.499 | 41.68 | 5.53 | s20:+0.118, s4:+0.099, s12:+0.080 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 182 | 184 | preventive_schedule | 0.499 | 41.68 | 5.53 | s20:+0.118, s4:+0.099, s12:+0.080 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.804 | indefinido | indefinido | s20:+0.055, s4:+0.038, s12:+0.036 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.809 | indefinido | indefinido | s20:+0.047, s12:+0.034, s4:+0.032 |
| 3 | HI_MARKER_D1 | 182 | 183 | preventive_schedule | 0.499 | indefinido | indefinido | s20:+0.118, s4:+0.099, s12:+0.080 |
| 3 | HI_MARKER_D2 | 182 | 184 | preventive_schedule | 0.499 | indefinido | indefinido | s20:+0.118, s4:+0.099, s12:+0.080 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=188, A=188.
- Repetição2: G=186, A=186.
- Repetição3: G=182, A=182.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.69 | 0.76 | 13.33% | 16.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.80 | 0.32 | 0.00% | 36.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.90 | 0.40 | 0.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.90 | 0.40 | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.00 | 0.40 | 20.00% | 16.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.04 | 0.40 | 20.00% | 16.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 23.68 | 15 | 1.90 | 0.88 | 0.00% | 20.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 23.68 | 15 | 1.90 | 0.88 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.74 | 0.11 | 10.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.17 | 0.09 | 3.33% | 26.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 41.91 | 15 | 1.90 | 0.88 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 41.91 | 15 | 1.90 | 0.88 | 0.00% | 20.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.90 | 0.88 | 0.00% | 20.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.90 | 0.88 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.90 | 0.71 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.90 | 0.71 | 0.00% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.83 | 0.40 | 0.00% | 0.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.83 | 0.40 | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.50 | 0.10 | 40.00% | 30.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.73 | 0.68 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 23.04 | 15 | 1.83 | 0.88 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 23.04 | 15 | 1.83 | 0.88 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.40 | 1.06 | 0.00% | 46.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.40 | 1.33 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 27.30 | 15 | 1.83 | 0.88 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 27.30 | 15 | 1.83 | 0.88 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.83 | 0.88 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.83 | 0.88 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.27 | 0.29 | 0.00% | 30.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.27 | 0.29 | 0.00% | 30.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.23 | 0.14 | 0.00% | 26.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.23 | 0.14 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 36.67% | 36.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.68 | 0.16 | 36.67% | 36.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 30.68 | 15 | 2.23 | 0.53 | 0.00% | 36.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 30.68 | 15 | 2.23 | 0.53 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 36.67% | 36.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 36.67% | 36.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 36.15 | 15 | 2.23 | 0.53 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 36.15 | 15 | 2.23 | 0.53 | 0.00% | 36.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.23 | 0.53 | 0.00% | 36.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.23 | 0.53 | 0.00% | 36.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
