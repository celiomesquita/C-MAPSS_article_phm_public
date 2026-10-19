# FD001, motor32 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u32.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 179 | 180 | preventive_schedule | 0.289 | indefinido | indefinido | s21:+0.112, s7:+0.112, s12:+0.109 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 179 | 181 | preventive_schedule | 0.289 | indefinido | indefinido | s21:+0.112, s7:+0.112, s12:+0.109 |
| 1 | HI_WAIT_SELECTED_D1 | 175 | 176 | preventive_schedule | 0.360 | indefinido | indefinido | s7:+0.102, s21:+0.097, s12:+0.096 |
| 1 | HI_WAIT_SELECTED_D2 | 175 | 177 | preventive_schedule | 0.360 | indefinido | indefinido | s7:+0.102, s21:+0.097, s12:+0.096 |
| 1 | ISO_POINT_M15_D1 | 185 | 186 | preventive_schedule | 0.253 | 15.41 | 15.41 | s7:+0.117, s12:+0.114, s21:+0.109 |
| 1 | ISO_POINT_M15_D2 | 185 | 187 | preventive_schedule | 0.253 | 15.41 | 15.41 | s7:+0.117, s12:+0.114, s21:+0.109 |
| 1 | ISO_LOWER98_M15_D1 | 165 | 166 | preventive_schedule | 0.482 | 39.63 | 12.00 | s12:+0.085, s21:+0.083, s7:+0.070 |
| 1 | ISO_LOWER98_M15_D2 | 165 | 167 | preventive_schedule | 0.482 | 39.63 | 12.00 | s12:+0.085, s21:+0.083, s7:+0.070 |
| 1 | RF_SLOPE_POINT_M15_D1 | 177 | 178 | preventive_schedule | 0.326 | 11.76 | 11.76 | s21:+0.107, s12:+0.104, s7:+0.104 |
| 1 | RF_SLOPE_POINT_M15_D2 | 177 | 179 | preventive_schedule | 0.326 | 11.76 | 11.76 | s21:+0.107, s12:+0.104, s7:+0.104 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 165 | 166 | preventive_schedule | 0.482 | 30.25 | 0.00 | s12:+0.085, s21:+0.083, s7:+0.070 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 165 | 167 | preventive_schedule | 0.482 | 30.25 | 0.00 | s12:+0.085, s21:+0.083, s7:+0.070 |
| 1 | AGE_D1 | 126 | 127 | preventive_schedule | 0.786 | indefinido | indefinido | s21:+0.041, s12:+0.029, s7:+0.024 |
| 1 | AGE_D2 | 125 | 127 | preventive_schedule | 0.787 | indefinido | indefinido | s21:+0.040, s12:+0.029, s7:+0.028 |
| 1 | HI_MARKER_D1 | 165 | 166 | preventive_schedule | 0.482 | indefinido | indefinido | s12:+0.085, s21:+0.083, s7:+0.070 |
| 1 | HI_MARKER_D2 | 165 | 167 | preventive_schedule | 0.482 | indefinido | indefinido | s12:+0.085, s21:+0.083, s7:+0.070 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 171 | 172 | preventive_schedule | 0.396 | indefinido | indefinido | s12:+0.141, s4:+0.080, s15:+0.070 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 171 | 173 | preventive_schedule | 0.396 | indefinido | indefinido | s12:+0.141, s4:+0.080, s15:+0.070 |
| 2 | HI_WAIT_SELECTED_D1 | 173 | 174 | preventive_schedule | 0.361 | indefinido | indefinido | s12:+0.149, s4:+0.081, s15:+0.073 |
| 2 | HI_WAIT_SELECTED_D2 | 168 | 170 | preventive_schedule | 0.420 | indefinido | indefinido | s12:+0.140, s4:+0.080, s15:+0.064 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.181 | 16.42 | 16.42 | s12:+0.180, s4:+0.120, s15:+0.090 |
| 2 | ISO_POINT_M15_D2 | 190 | 192 | late_schedule | 0.181 | 16.42 | 16.42 | s12:+0.180, s4:+0.120, s15:+0.090 |
| 2 | ISO_LOWER98_M15_D1 | 163 | 164 | preventive_schedule | 0.489 | 37.27 | 14.43 | s12:+0.132, s4:+0.067, s15:+0.054 |
| 2 | ISO_LOWER98_M15_D2 | 163 | 165 | preventive_schedule | 0.489 | 37.27 | 14.43 | s12:+0.132, s4:+0.067, s15:+0.054 |
| 2 | RF_SLOPE_POINT_M15_D1 | 174 | 175 | preventive_schedule | 0.353 | 15.89 | 15.89 | s12:+0.147, s15:+0.079, s4:+0.079 |
| 2 | RF_SLOPE_POINT_M15_D2 | 173 | 175 | preventive_schedule | 0.361 | 16.31 | 16.31 | s12:+0.149, s4:+0.081, s15:+0.073 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 163 | 164 | preventive_schedule | 0.489 | 38.31 | 5.47 | s12:+0.132, s4:+0.067, s15:+0.054 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 163 | 165 | preventive_schedule | 0.489 | 38.31 | 5.47 | s12:+0.132, s4:+0.067, s15:+0.054 |
| 2 | AGE_D1 | 133 | 134 | preventive_schedule | 0.751 | indefinido | indefinido | s12:+0.063, s15:+0.042, s4:+0.030 |
| 2 | AGE_D2 | 132 | 134 | preventive_schedule | 0.751 | indefinido | indefinido | s12:+0.062, s15:+0.044, s4:+0.028 |
| 2 | HI_MARKER_D1 | 163 | 164 | preventive_schedule | 0.489 | indefinido | indefinido | s12:+0.132, s4:+0.067, s15:+0.054 |
| 2 | HI_MARKER_D2 | 163 | 165 | preventive_schedule | 0.489 | indefinido | indefinido | s12:+0.132, s4:+0.067, s15:+0.054 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 172 | 173 | preventive_schedule | 0.390 | indefinido | indefinido | s4:+0.128, s7:+0.086, s2:+0.076 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 172 | 174 | preventive_schedule | 0.390 | indefinido | indefinido | s4:+0.128, s7:+0.086, s2:+0.076 |
| 3 | HI_WAIT_SELECTED_D1 | 176 | 177 | preventive_schedule | 0.344 | indefinido | indefinido | s4:+0.127, s7:+0.101, s2:+0.093 |
| 3 | HI_WAIT_SELECTED_D2 | 171 | 173 | preventive_schedule | 0.407 | indefinido | indefinido | s4:+0.127, s7:+0.084, s2:+0.075 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.176 | 17.52 | 17.52 | s4:+0.191, s7:+0.114, s9:+0.098 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.176 | 17.52 | 17.52 | s4:+0.191, s7:+0.114, s9:+0.098 |
| 3 | ISO_LOWER98_M15_D1 | 166 | 167 | preventive_schedule | 0.477 | 40.59 | 14.83 | s4:+0.118, s7:+0.071, s12:+0.057 |
| 3 | ISO_LOWER98_M15_D2 | 166 | 168 | preventive_schedule | 0.477 | 40.59 | 14.83 | s4:+0.118, s7:+0.071, s12:+0.057 |
| 3 | RF_SLOPE_POINT_M15_D1 | 177 | 178 | preventive_schedule | 0.318 | 15.34 | 15.34 | s4:+0.135, s7:+0.100, s2:+0.096 |
| 3 | RF_SLOPE_POINT_M15_D2 | 176 | 178 | preventive_schedule | 0.344 | 16.88 | 16.88 | s4:+0.127, s7:+0.101, s2:+0.093 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 166 | 167 | preventive_schedule | 0.477 | 48.46 | 9.97 | s4:+0.118, s7:+0.071, s12:+0.057 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 166 | 168 | preventive_schedule | 0.477 | 48.46 | 9.97 | s4:+0.118, s7:+0.071, s12:+0.057 |
| 3 | AGE_D1 | 133 | 134 | preventive_schedule | 0.793 | indefinido | indefinido | s4:+0.048, s12:+0.027, s9:+0.026 |
| 3 | AGE_D2 | 132 | 134 | preventive_schedule | 0.794 | indefinido | indefinido | s4:+0.044, s12:+0.026, s9:+0.025 |
| 3 | HI_MARKER_D1 | 166 | 167 | preventive_schedule | 0.477 | indefinido | indefinido | s4:+0.118, s7:+0.071, s12:+0.057 |
| 3 | HI_MARKER_D2 | 166 | 168 | preventive_schedule | 0.477 | indefinido | indefinido | s4:+0.118, s7:+0.071, s12:+0.057 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=165, A=165.
- Repetição2: G=163, A=163.
- Repetição3: G=166, A=166.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.73 | 0.36 | 0.00% | 26.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.73 | 0.36 | 0.00% | 26.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.53 | 0.33 | 0.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.53 | 0.33 | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.37 | 0.95 | 0.00% | 33.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.37 | 1.05 | 0.00% | 33.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 27.63 | 15 | 1.53 | 0.92 | 0.00% | 16.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 27.63 | 15 | 1.53 | 0.92 | 0.00% | 16.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.43 | 1.36 | 0.00% | 16.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.57 | 1.48 | 0.00% | 16.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 56.13 | 15 | 1.53 | 0.92 | 0.00% | 16.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 56.13 | 15 | 1.53 | 0.92 | 0.00% | 16.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.53 | 0.92 | 0.00% | 16.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.53 | 0.92 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.90 | 0.89 | 0.00% | 40.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.90 | 0.89 | 0.00% | 40.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.40 | 0.03 | 0.00% | 0.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.40 | 0.31 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 13.33% | 3.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.80 | 1.14 | 16.67% | 3.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 22.84 | 15 | 1.40 | 0.57 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 22.84 | 15 | 1.40 | 0.57 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.37 | 2.50 | 36.67% | 46.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.00 | 2.06 | 6.67% | 43.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 32.84 | 15 | 1.40 | 0.57 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 32.84 | 15 | 1.40 | 0.57 | 0.00% | 23.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.40 | 0.57 | 0.00% | 23.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.40 | 0.57 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.40 | 0.52 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.40 | 0.52 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.20 | 0.37 | 0.00% | 0.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.20 | 0.48 | 0.00% | 3.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.33% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 30.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.76 | 15 | 1.20 | 0.63 | 0.00% | 10.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.76 | 15 | 1.20 | 0.63 | 0.00% | 10.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.67 | 0.48 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.73 | 1.06 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 38.50 | 15 | 0.80 | 0.63 | 0.00% | 10.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 38.50 | 15 | 0.93 | 0.63 | 0.00% | 10.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.20 | 0.63 | 0.00% | 10.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.20 | 0.63 | 0.00% | 10.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
