# FD001, motor36 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u36.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 142 | 143 | preventive_schedule | 0.396 | indefinido | indefinido | s7:+0.102, s12:+0.089, s15:+0.087 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 142 | 144 | preventive_schedule | 0.396 | indefinido | indefinido | s7:+0.102, s12:+0.089, s15:+0.087 |
| 1 | HI_WAIT_SELECTED_D1 | 143 | 144 | preventive_schedule | 0.390 | indefinido | indefinido | s7:+0.103, s12:+0.089, s15:+0.087 |
| 1 | HI_WAIT_SELECTED_D2 | 143 | 145 | preventive_schedule | 0.390 | indefinido | indefinido | s7:+0.103, s12:+0.089, s15:+0.087 |
| 1 | ISO_POINT_M15_D1 | 156 | 157 | preventive_schedule | 0.194 | 14.37 | 14.37 | s15:+0.139, s7:+0.130, s12:+0.114 |
| 1 | ISO_POINT_M15_D2 | 156 | 158 | at_endpoint | 0.194 | 14.37 | 14.37 | s15:+0.139, s7:+0.130, s12:+0.114 |
| 1 | ISO_LOWER98_M15_D1 | 133 | 134 | preventive_schedule | 0.492 | 37.62 | 9.00 | s7:+0.084, s15:+0.081, s12:+0.077 |
| 1 | ISO_LOWER98_M15_D2 | 133 | 135 | preventive_schedule | 0.492 | 37.62 | 9.00 | s7:+0.084, s15:+0.081, s12:+0.077 |
| 1 | RF_SLOPE_POINT_M15_D1 | 154 | 155 | preventive_schedule | 0.234 | 7.07 | 7.07 | s15:+0.128, s7:+0.127, s12:+0.110 |
| 1 | RF_SLOPE_POINT_M15_D2 | 152 | 154 | preventive_schedule | 0.263 | 16.32 | 16.32 | s7:+0.121, s15:+0.118, s12:+0.107 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 133 | 134 | preventive_schedule | 0.492 | 32.10 | 0.00 | s7:+0.084, s15:+0.081, s12:+0.077 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 133 | 135 | preventive_schedule | 0.492 | 32.10 | 0.00 | s7:+0.084, s15:+0.081, s12:+0.077 |
| 1 | AGE_D1 | 145 | 146 | preventive_schedule | 0.358 | indefinido | indefinido | s7:+0.108, s15:+0.096, s12:+0.091 |
| 1 | AGE_D2 | 144 | 146 | preventive_schedule | 0.377 | indefinido | indefinido | s7:+0.107, s15:+0.090, s12:+0.088 |
| 1 | HI_MARKER_D1 | 133 | 134 | preventive_schedule | 0.492 | indefinido | indefinido | s7:+0.084, s15:+0.081, s12:+0.077 |
| 1 | HI_MARKER_D2 | 133 | 135 | preventive_schedule | 0.492 | indefinido | indefinido | s7:+0.084, s15:+0.081, s12:+0.077 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 135 | 136 | preventive_schedule | 0.387 | indefinido | indefinido | s7:+0.098, s2:+0.097, s11:+0.081 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 135 | 137 | preventive_schedule | 0.387 | indefinido | indefinido | s7:+0.098, s2:+0.097, s11:+0.081 |
| 2 | HI_WAIT_SELECTED_D1 | 139 | 140 | preventive_schedule | 0.335 | indefinido | indefinido | s2:+0.113, s7:+0.101, s11:+0.085 |
| 2 | HI_WAIT_SELECTED_D2 | 134 | 136 | preventive_schedule | 0.413 | indefinido | indefinido | s7:+0.090, s2:+0.089, s11:+0.078 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.060 | 16.66 | 16.66 | s2:+0.171, s7:+0.138, s11:+0.126 |
| 2 | ISO_POINT_M15_D2 | 155 | 157 | preventive_schedule | 0.108 | 16.66 | 16.66 | s2:+0.161, s7:+0.135, s11:+0.117 |
| 2 | ISO_LOWER98_M15_D1 | 130 | 131 | preventive_schedule | 0.475 | 41.62 | 13.36 | s2:+0.086, s7:+0.082, s11:+0.070 |
| 2 | ISO_LOWER98_M15_D2 | 129 | 131 | preventive_schedule | 0.493 | 45.26 | 17.00 | s2:+0.081, s7:+0.079, s11:+0.069 |
| 2 | RF_SLOPE_POINT_M15_D1 | 144 | 145 | preventive_schedule | 0.272 | 15.89 | 15.89 | s2:+0.136, s7:+0.113, s11:+0.095 |
| 2 | RF_SLOPE_POINT_M15_D2 | 144 | 146 | preventive_schedule | 0.272 | 15.89 | 15.89 | s2:+0.136, s7:+0.113, s11:+0.095 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 129 | 130 | preventive_schedule | 0.493 | 41.88 | 5.43 | s2:+0.081, s7:+0.079, s11:+0.069 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 129 | 131 | preventive_schedule | 0.493 | 41.88 | 5.43 | s2:+0.081, s7:+0.079, s11:+0.069 |
| 2 | AGE_D1 | 133 | 134 | preventive_schedule | 0.439 | indefinido | indefinido | s7:+0.089, s2:+0.084, s11:+0.076 |
| 2 | AGE_D2 | 132 | 134 | preventive_schedule | 0.459 | indefinido | indefinido | s7:+0.085, s2:+0.081, s11:+0.072 |
| 2 | HI_MARKER_D1 | 129 | 130 | preventive_schedule | 0.493 | indefinido | indefinido | s2:+0.081, s7:+0.079, s11:+0.069 |
| 2 | HI_MARKER_D2 | 129 | 131 | preventive_schedule | 0.493 | indefinido | indefinido | s2:+0.081, s7:+0.079, s11:+0.069 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 151 | 152 | preventive_schedule | 0.287 | indefinido | indefinido | s4:+0.147, s12:+0.106, s7:+0.103 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 151 | 153 | preventive_schedule | 0.287 | indefinido | indefinido | s4:+0.147, s12:+0.106, s7:+0.103 |
| 3 | HI_WAIT_SELECTED_D1 | 143 | 144 | preventive_schedule | 0.373 | indefinido | indefinido | s4:+0.119, s12:+0.092, s7:+0.089 |
| 3 | HI_WAIT_SELECTED_D2 | 143 | 145 | preventive_schedule | 0.373 | indefinido | indefinido | s4:+0.119, s12:+0.092, s7:+0.089 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.185 | 16.34 | 16.34 | s4:+0.170, s12:+0.121, s7:+0.114 |
| 3 | ISO_POINT_M15_D2 | 155 | 157 | preventive_schedule | 0.220 | 16.93 | 16.93 | s4:+0.158, s12:+0.117, s7:+0.111 |
| 3 | ISO_LOWER98_M15_D1 | 133 | 134 | preventive_schedule | 0.492 | 41.11 | 15.70 | s4:+0.096, s12:+0.079, s7:+0.073 |
| 3 | ISO_LOWER98_M15_D2 | 133 | 135 | preventive_schedule | 0.492 | 41.11 | 15.70 | s4:+0.096, s12:+0.079, s7:+0.073 |
| 3 | RF_SLOPE_POINT_M15_D1 | 157 | 158 | at_endpoint | 0.185 | 12.75 | 12.75 | s4:+0.170, s12:+0.121, s7:+0.114 |
| 3 | RF_SLOPE_POINT_M15_D2 | 157 | 159 | late_schedule | 0.185 | 12.75 | 12.75 | s4:+0.170, s12:+0.121, s7:+0.114 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 133 | 134 | preventive_schedule | 0.492 | 36.59 | 1.70 | s4:+0.096, s12:+0.079, s7:+0.073 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 133 | 135 | preventive_schedule | 0.492 | 36.59 | 1.70 | s4:+0.096, s12:+0.079, s7:+0.073 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.560 | indefinido | indefinido | s4:+0.077, s12:+0.068, s21:+0.066 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.564 | indefinido | indefinido | s4:+0.074, s12:+0.066, s21:+0.065 |
| 3 | HI_MARKER_D1 | 133 | 134 | preventive_schedule | 0.492 | indefinido | indefinido | s4:+0.096, s12:+0.079, s7:+0.073 |
| 3 | HI_MARKER_D2 | 133 | 135 | preventive_schedule | 0.492 | indefinido | indefinido | s4:+0.096, s12:+0.079, s7:+0.073 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=133, A=133.
- Repetição2: G=129, A=129.
- Repetição3: G=133, A=133.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.30 | 0.89 | 0.00% | 36.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.30 | 0.89 | 0.00% | 36.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.57 | 0.24 | 0.00% | 3.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.57 | 0.24 | 0.00% | 3.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.89 | 0.43 | 10.00% | 23.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.96 | 0.50 | 6.67% | 20.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 28.62 | 15 | 1.57 | 0.73 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 28.62 | 15 | 1.57 | 0.73 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.00 | 2.46 | 0.00% | 6.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.53 | 1.78 | 0.00% | 10.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 49.06 | 15 | 1.57 | 0.73 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 49.06 | 15 | 1.57 | 0.73 | 0.00% | 26.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.57 | 0.73 | 0.00% | 26.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.57 | 0.73 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.27 | 0.43 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.27 | 0.43 | 0.00% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.63 | 0.11 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.63 | 1.14 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.14 | 0.45 | 3.33% | 33.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 28.26 | 15 | 2.40 | 0.62 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 28.26 | 15 | 2.63 | 1.57 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.93 | 0.72 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.83 | 0.62 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 36.46 | 15 | 2.63 | 1.05 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 36.46 | 15 | 2.63 | 1.43 | 0.00% | 30.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.63 | 1.57 | 0.00% | 30.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.63 | 1.57 | 0.00% | 30.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.17 | 1.26 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.17 | 1.26 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.27 | 0.03 | 0.00% | 3.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.27 | 0.03 | 0.00% | 3.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 40.00% | 33.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.96 | 0.35 | 10.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.41 | 15 | 1.23 | 0.38 | 0.00% | 30.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.41 | 15 | 1.27 | 0.38 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.33 | 0.55 | 30.00% | 33.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.32 | 0.52 | 26.67% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 34.89 | 15 | 1.37 | 0.39 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 34.89 | 15 | 1.37 | 0.39 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.27 | 0.43 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.27 | 0.43 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
