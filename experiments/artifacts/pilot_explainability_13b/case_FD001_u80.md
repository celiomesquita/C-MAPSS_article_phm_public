# FD001, motor80 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u80.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 178 | 179 | preventive_schedule | 0.289 | indefinido | indefinido | s2:+0.115, s14:+0.115, s12:+0.107 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 178 | 180 | preventive_schedule | 0.289 | indefinido | indefinido | s2:+0.115, s14:+0.115, s12:+0.107 |
| 1 | HI_WAIT_SELECTED_D1 | 173 | 174 | preventive_schedule | 0.360 | indefinido | indefinido | s2:+0.119, s14:+0.101, s12:+0.100 |
| 1 | HI_WAIT_SELECTED_D2 | 173 | 175 | preventive_schedule | 0.360 | indefinido | indefinido | s2:+0.119, s14:+0.101, s12:+0.100 |
| 1 | ISO_POINT_M15_D1 | 183 | 184 | preventive_schedule | 0.160 | 13.18 | 13.18 | s2:+0.132, s14:+0.131, s12:+0.128 |
| 1 | ISO_POINT_M15_D2 | 183 | 185 | at_endpoint | 0.160 | 13.18 | 13.18 | s2:+0.132, s14:+0.131, s12:+0.128 |
| 1 | ISO_LOWER98_M15_D1 | 163 | 164 | preventive_schedule | 0.494 | 39.24 | 13.63 | s2:+0.094, s12:+0.084, s14:+0.077 |
| 1 | ISO_LOWER98_M15_D2 | 163 | 165 | preventive_schedule | 0.494 | 39.24 | 13.63 | s2:+0.094, s12:+0.084, s14:+0.077 |
| 1 | RF_SLOPE_POINT_M15_D1 | 179 | 180 | preventive_schedule | 0.267 | 14.29 | 14.29 | s2:+0.119, s14:+0.118, s12:+0.109 |
| 1 | RF_SLOPE_POINT_M15_D2 | 179 | 181 | preventive_schedule | 0.267 | 14.29 | 14.29 | s2:+0.119, s14:+0.118, s12:+0.109 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 163 | 164 | preventive_schedule | 0.494 | 33.42 | 0.00 | s2:+0.094, s12:+0.084, s14:+0.077 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 163 | 165 | preventive_schedule | 0.494 | 33.42 | 0.00 | s2:+0.094, s12:+0.084, s14:+0.077 |
| 1 | AGE_D1 | 135 | 136 | preventive_schedule | 0.780 | indefinido | indefinido | s2:+0.040, s14:+0.034, s12:+0.031 |
| 1 | AGE_D2 | 134 | 136 | preventive_schedule | 0.789 | indefinido | indefinido | s2:+0.038, s14:+0.033, s12:+0.032 |
| 1 | HI_MARKER_D1 | 163 | 164 | preventive_schedule | 0.494 | indefinido | indefinido | s2:+0.094, s12:+0.084, s14:+0.077 |
| 1 | HI_MARKER_D2 | 163 | 165 | preventive_schedule | 0.494 | indefinido | indefinido | s2:+0.094, s12:+0.084, s14:+0.077 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 175 | 176 | preventive_schedule | 0.186 | indefinido | indefinido | s2:+0.153, s9:+0.098, s4:+0.086 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 175 | 177 | preventive_schedule | 0.186 | indefinido | indefinido | s2:+0.153, s9:+0.098, s4:+0.086 |
| 2 | HI_WAIT_SELECTED_D1 | 167 | 168 | preventive_schedule | 0.325 | indefinido | indefinido | s2:+0.151, s9:+0.081, s20:+0.063 |
| 2 | HI_WAIT_SELECTED_D2 | 167 | 169 | preventive_schedule | 0.325 | indefinido | indefinido | s2:+0.151, s9:+0.081, s20:+0.063 |
| 2 | ISO_POINT_M15_D1 | 182 | 183 | preventive_schedule | 0.001 | 8.31 | 8.31 | s2:+0.171, s9:+0.118, s4:+0.112 |
| 2 | ISO_POINT_M15_D2 | 179 | 181 | preventive_schedule | 0.089 | 16.98 | 16.98 | s2:+0.158, s9:+0.109, s4:+0.100 |
| 2 | ISO_LOWER98_M15_D1 | 159 | 160 | preventive_schedule | 0.466 | 42.32 | 15.00 | s2:+0.098, s9:+0.064, s11:+0.056 |
| 2 | ISO_LOWER98_M15_D2 | 159 | 161 | preventive_schedule | 0.466 | 42.32 | 15.00 | s2:+0.098, s9:+0.064, s11:+0.056 |
| 2 | RF_SLOPE_POINT_M15_D1 | 175 | 176 | preventive_schedule | 0.186 | 13.87 | 13.87 | s2:+0.153, s9:+0.098, s4:+0.086 |
| 2 | RF_SLOPE_POINT_M15_D2 | 173 | 175 | preventive_schedule | 0.229 | 16.97 | 16.97 | s2:+0.158, s9:+0.093, s20:+0.079 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 157 | 158 | preventive_schedule | 0.495 | 46.90 | 7.84 | s2:+0.090, s9:+0.060, s11:+0.051 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 157 | 159 | preventive_schedule | 0.495 | 46.90 | 7.84 | s2:+0.090, s9:+0.060, s11:+0.051 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.767 | indefinido | indefinido | s2:+0.054, s7:+0.026, s20:+0.024 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.777 | indefinido | indefinido | s2:+0.048, s20:+0.025, s15:+0.023 |
| 2 | HI_MARKER_D1 | 157 | 158 | preventive_schedule | 0.495 | indefinido | indefinido | s2:+0.090, s9:+0.060, s11:+0.051 |
| 2 | HI_MARKER_D2 | 157 | 159 | preventive_schedule | 0.495 | indefinido | indefinido | s2:+0.090, s9:+0.060, s11:+0.051 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 171 | 172 | preventive_schedule | 0.387 | indefinido | indefinido | s9:+0.104, s15:+0.078, s2:+0.071 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 171 | 173 | preventive_schedule | 0.387 | indefinido | indefinido | s9:+0.104, s15:+0.078, s2:+0.071 |
| 3 | HI_WAIT_SELECTED_D1 | 169 | 170 | preventive_schedule | 0.431 | indefinido | indefinido | s9:+0.099, s2:+0.069, s15:+0.064 |
| 3 | HI_WAIT_SELECTED_D2 | 169 | 171 | preventive_schedule | 0.431 | indefinido | indefinido | s9:+0.099, s2:+0.069, s15:+0.064 |
| 3 | ISO_POINT_M15_D1 | 181 | 182 | preventive_schedule | 0.197 | 13.91 | 13.91 | s9:+0.134, s15:+0.106, s14:+0.083 |
| 3 | ISO_POINT_M15_D2 | 181 | 183 | preventive_schedule | 0.197 | 13.91 | 13.91 | s9:+0.134, s15:+0.106, s14:+0.083 |
| 3 | ISO_LOWER98_M15_D1 | 164 | 165 | preventive_schedule | 0.498 | 34.05 | 13.00 | s9:+0.086, s21:+0.057, s15:+0.053 |
| 3 | ISO_LOWER98_M15_D2 | 164 | 166 | preventive_schedule | 0.498 | 34.05 | 13.00 | s9:+0.086, s21:+0.057, s15:+0.053 |
| 3 | RF_SLOPE_POINT_M15_D1 | 168 | 169 | preventive_schedule | 0.434 | 15.88 | 15.88 | s9:+0.097, s2:+0.068, s21:+0.065 |
| 3 | RF_SLOPE_POINT_M15_D2 | 168 | 170 | preventive_schedule | 0.434 | 15.88 | 15.88 | s9:+0.097, s2:+0.068, s21:+0.065 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 164 | 165 | preventive_schedule | 0.498 | 28.23 | 0.00 | s9:+0.086, s21:+0.057, s15:+0.053 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 164 | 166 | preventive_schedule | 0.498 | 28.23 | 0.00 | s9:+0.086, s21:+0.057, s15:+0.053 |
| 3 | AGE_D1 | 133 | 134 | preventive_schedule | 0.783 | indefinido | indefinido | s9:+0.036, s21:+0.028, s7:+0.024 |
| 3 | AGE_D2 | 132 | 134 | preventive_schedule | 0.788 | indefinido | indefinido | s9:+0.034, s21:+0.028, s2:+0.024 |
| 3 | HI_MARKER_D1 | 164 | 165 | preventive_schedule | 0.498 | indefinido | indefinido | s9:+0.086, s21:+0.057, s15:+0.053 |
| 3 | HI_MARKER_D2 | 164 | 166 | preventive_schedule | 0.498 | indefinido | indefinido | s9:+0.086, s21:+0.057, s15:+0.053 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=163, A=163.
- Repetição2: G=157, A=157.
- Repetição3: G=164, A=164.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.10 | 0.45 | 0.00% | 26.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.10 | 0.45 | 0.00% | 26.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.53 | 0.04 | 0.00% | 13.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.53 | 0.04 | 0.00% | 13.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.39 | 0.09 | 6.67% | 23.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.39 | 0.09 | 6.67% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 25.61 | 15 | 1.63 | 0.47 | 0.00% | 36.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 25.61 | 15 | 1.60 | 0.53 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.27 | 0.14 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.10 | 0.50 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 38.16 | 15 | 1.53 | 0.55 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 38.16 | 15 | 1.53 | 0.55 | 0.00% | 26.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.53 | 0.55 | 0.00% | 26.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.53 | 0.55 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.23 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.23 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.57 | 0.00 | 0.00% | 13.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.57 | 0.00 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.87 | 0.31 | 0.00% | 3.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.90 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 27.32 | 15 | 1.63 | 0.43 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 27.32 | 15 | 1.60 | 0.43 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.20 | 2.00 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.60 | 1.21 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 39.06 | 15 | 1.57 | 0.23 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 39.06 | 15 | 1.57 | 0.23 | 0.00% | 26.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.57 | 0.23 | 0.00% | 26.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.57 | 0.23 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.33 | 0.50 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.33 | 0.50 | 0.00% | 26.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.80 | 0.68 | 0.00% | 36.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.80 | 0.68 | 0.00% | 36.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.83 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.87 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 21.05 | 15 | 1.80 | 1.00 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 21.05 | 15 | 1.80 | 1.00 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.70 | 0.94 | 0.00% | 43.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.43 | 1.05 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 29.95 | 15 | 1.80 | 1.00 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 29.95 | 15 | 1.80 | 1.00 | 0.00% | 40.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.80 | 1.00 | 0.00% | 40.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.80 | 1.00 | 0.00% | 40.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
