# FD001, motor76 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u76.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 202 | 203 | preventive_schedule | 0.296 | indefinido | indefinido | s7:+0.171, s4:+0.113, s11:+0.092 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 193 | 195 | preventive_schedule | 0.397 | indefinido | indefinido | s7:+0.136, s4:+0.098, s21:+0.084 |
| 1 | HI_WAIT_SELECTED_D1 | 192 | 193 | preventive_schedule | 0.401 | indefinido | indefinido | s7:+0.135, s4:+0.095, s21:+0.085 |
| 1 | HI_WAIT_SELECTED_D2 | 192 | 194 | preventive_schedule | 0.401 | indefinido | indefinido | s7:+0.135, s4:+0.095, s21:+0.085 |
| 1 | ISO_POINT_M15_D1 | 205 | 206 | preventive_schedule | 0.266 | 15.41 | 15.41 | s7:+0.180, s4:+0.124, s11:+0.098 |
| 1 | ISO_POINT_M15_D2 | 205 | 207 | preventive_schedule | 0.266 | 15.41 | 15.41 | s7:+0.180, s4:+0.124, s11:+0.098 |
| 1 | ISO_LOWER98_M15_D1 | 182 | 183 | preventive_schedule | 0.490 | 33.00 | 9.32 | s7:+0.111, s4:+0.088, s21:+0.076 |
| 1 | ISO_LOWER98_M15_D2 | 182 | 184 | preventive_schedule | 0.490 | 33.00 | 9.32 | s7:+0.111, s4:+0.088, s21:+0.076 |
| 1 | RF_SLOPE_POINT_M15_D1 | 199 | 200 | preventive_schedule | 0.320 | 15.26 | 15.26 | s7:+0.165, s4:+0.105, s21:+0.091 |
| 1 | RF_SLOPE_POINT_M15_D2 | 199 | 201 | preventive_schedule | 0.320 | 15.26 | 15.26 | s7:+0.165, s4:+0.105, s21:+0.091 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 182 | 183 | preventive_schedule | 0.490 | 28.40 | 0.00 | s7:+0.111, s4:+0.088, s21:+0.076 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 182 | 184 | preventive_schedule | 0.490 | 28.40 | 0.00 | s7:+0.111, s4:+0.088, s21:+0.076 |
| 1 | AGE_D1 | 135 | 136 | preventive_schedule | 0.824 | indefinido | indefinido | s21:+0.035, s11:+0.033, s4:+0.022 |
| 1 | AGE_D2 | 134 | 136 | preventive_schedule | 0.826 | indefinido | indefinido | s11:+0.034, s21:+0.031, s4:+0.026 |
| 1 | HI_MARKER_D1 | 182 | 183 | preventive_schedule | 0.490 | indefinido | indefinido | s7:+0.111, s4:+0.088, s21:+0.076 |
| 1 | HI_MARKER_D2 | 182 | 184 | preventive_schedule | 0.490 | indefinido | indefinido | s7:+0.111, s4:+0.088, s21:+0.076 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 192 | 193 | preventive_schedule | 0.399 | indefinido | indefinido | s7:+0.135, s2:+0.093, s20:+0.087 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 192 | 194 | preventive_schedule | 0.399 | indefinido | indefinido | s7:+0.135, s2:+0.093, s20:+0.087 |
| 2 | HI_WAIT_SELECTED_D1 | 192 | 193 | preventive_schedule | 0.399 | indefinido | indefinido | s7:+0.135, s2:+0.093, s20:+0.087 |
| 2 | HI_WAIT_SELECTED_D2 | 192 | 194 | preventive_schedule | 0.399 | indefinido | indefinido | s7:+0.135, s2:+0.093, s20:+0.087 |
| 2 | ISO_POINT_M15_D1 | 208 | 209 | preventive_schedule | 0.174 | 13.21 | 13.21 | s7:+0.196, s2:+0.145, s20:+0.109 |
| 2 | ISO_POINT_M15_D2 | 204 | 206 | preventive_schedule | 0.250 | 16.55 | 16.55 | s7:+0.171, s2:+0.137, s20:+0.100 |
| 2 | ISO_LOWER98_M15_D1 | 182 | 183 | preventive_schedule | 0.488 | 34.84 | 11.80 | s7:+0.110, s2:+0.084, s20:+0.074 |
| 2 | ISO_LOWER98_M15_D2 | 182 | 184 | preventive_schedule | 0.488 | 34.84 | 11.80 | s7:+0.110, s2:+0.084, s20:+0.074 |
| 2 | RF_SLOPE_POINT_M15_D1 | 204 | 205 | preventive_schedule | 0.250 | 15.80 | 15.80 | s7:+0.171, s2:+0.137, s20:+0.100 |
| 2 | RF_SLOPE_POINT_M15_D2 | 204 | 206 | preventive_schedule | 0.250 | 15.80 | 15.80 | s7:+0.171, s2:+0.137, s20:+0.100 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 182 | 183 | preventive_schedule | 0.488 | 42.16 | 14.86 | s7:+0.110, s2:+0.084, s20:+0.074 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 182 | 184 | preventive_schedule | 0.488 | 42.16 | 14.86 | s7:+0.110, s2:+0.084, s20:+0.074 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.845 | indefinido | indefinido | s11:+0.032, s20:+0.024, s7:+0.021 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.831 | indefinido | indefinido | s11:+0.032, s7:+0.031, s2:+0.024 |
| 2 | HI_MARKER_D1 | 182 | 183 | preventive_schedule | 0.488 | indefinido | indefinido | s7:+0.110, s2:+0.084, s20:+0.074 |
| 2 | HI_MARKER_D2 | 182 | 184 | preventive_schedule | 0.488 | indefinido | indefinido | s7:+0.110, s2:+0.084, s20:+0.074 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 193 | 194 | preventive_schedule | 0.299 | indefinido | indefinido | s21:+0.152, s12:+0.119, s20:+0.116 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 193 | 195 | preventive_schedule | 0.299 | indefinido | indefinido | s21:+0.152, s12:+0.119, s20:+0.116 |
| 3 | HI_WAIT_SELECTED_D1 | 184 | 185 | preventive_schedule | 0.401 | indefinido | indefinido | s21:+0.138, s20:+0.098, s12:+0.093 |
| 3 | HI_WAIT_SELECTED_D2 | 184 | 186 | preventive_schedule | 0.401 | indefinido | indefinido | s21:+0.138, s20:+0.098, s12:+0.093 |
| 3 | ISO_POINT_M15_D1 | 209 | 210 | at_endpoint | 0.117 | 15.01 | 15.01 | s21:+0.176, s20:+0.144, s12:+0.136 |
| 3 | ISO_POINT_M15_D2 | 207 | 209 | preventive_schedule | 0.150 | 16.46 | 16.46 | s21:+0.169, s20:+0.142, s12:+0.132 |
| 3 | ISO_LOWER98_M15_D1 | 174 | 175 | preventive_schedule | 0.499 | 42.36 | 10.73 | s21:+0.110, s12:+0.078, s20:+0.075 |
| 3 | ISO_LOWER98_M15_D2 | 174 | 176 | preventive_schedule | 0.499 | 42.36 | 10.73 | s21:+0.110, s12:+0.078, s20:+0.075 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.117 | 22.34 | 22.34 | s21:+0.176, s20:+0.144, s12:+0.136 |
| 3 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.117 | 22.34 | 22.34 | s21:+0.176, s20:+0.144, s12:+0.136 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 174 | 175 | preventive_schedule | 0.499 | 43.07 | 12.32 | s21:+0.110, s12:+0.078, s20:+0.075 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 174 | 176 | preventive_schedule | 0.499 | 43.07 | 12.32 | s21:+0.110, s12:+0.078, s20:+0.075 |
| 3 | AGE_D1 | 135 | 136 | preventive_schedule | 0.762 | indefinido | indefinido | s21:+0.064, s12:+0.044, s20:+0.041 |
| 3 | AGE_D2 | 134 | 136 | preventive_schedule | 0.765 | indefinido | indefinido | s21:+0.056, s20:+0.046, s12:+0.043 |
| 3 | HI_MARKER_D1 | 174 | 175 | preventive_schedule | 0.499 | indefinido | indefinido | s21:+0.110, s12:+0.078, s20:+0.075 |
| 3 | HI_MARKER_D2 | 174 | 176 | preventive_schedule | 0.499 | indefinido | indefinido | s21:+0.110, s12:+0.078, s20:+0.075 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=182, A=182.
- Repetição2: G=182, A=182.
- Repetição3: G=174, A=174.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.93 | 0.68 | 0.00% | 36.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.60 | 1.53 | 0.00% | 36.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.63 | 0.03 | 0.00% | 3.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.63 | 0.03 | 0.00% | 3.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.67 | 0.75 | 0.00% | 20.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.67 | 0.79 | 0.00% | 20.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 23.68 | 15 | 2.63 | 0.83 | 0.00% | 20.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 23.68 | 15 | 2.63 | 0.83 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.30 | 0.29 | 0.00% | 53.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.10 | 0.35 | 0.00% | 43.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 41.91 | 15 | 2.63 | 0.83 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 41.91 | 15 | 2.63 | 0.83 | 0.00% | 20.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.63 | 0.83 | 0.00% | 20.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.63 | 0.83 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.37 | 1.33 | 0.00% | 40.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.37 | 1.33 | 0.00% | 40.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.43 | 0.07 | 0.00% | 0.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.43 | 0.07 | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.93 | 0.48 | 10.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.73 | 0.88 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 23.04 | 15 | 2.43 | 0.78 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 23.04 | 15 | 2.43 | 0.78 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.68 | 0.38 | 6.67% | 56.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.67 | 0.28 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 27.30 | 15 | 2.83 | 1.00 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 27.30 | 15 | 2.73 | 0.90 | 0.00% | 33.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.43 | 0.78 | 0.00% | 23.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.43 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.60 | 1.47 | 0.00% | 43.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.60 | 1.47 | 0.00% | 43.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.67 | 0.06 | 0.00% | 40.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.67 | 0.06 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.10 | 0.52 | 30.00% | 30.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.15 | 0.32 | 10.00% | 36.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 31.63 | 15 | 2.67 | 0.94 | 0.00% | 43.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 31.63 | 15 | 2.67 | 0.94 | 0.00% | 43.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 30.74 | 15 | 2.07 | 0.94 | 0.00% | 43.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 30.74 | 15 | 2.07 | 0.94 | 0.00% | 43.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.67 | 0.94 | 0.00% | 43.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.67 | 0.94 | 0.00% | 43.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
