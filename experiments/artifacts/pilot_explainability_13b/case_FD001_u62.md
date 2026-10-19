# FD001, motor62 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible, median_discordance_d1.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u62.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 171 | 172 | preventive_schedule | 0.286 | indefinido | indefinido | s12:+0.172, s4:+0.110, s2:+0.088 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 171 | 173 | preventive_schedule | 0.286 | indefinido | indefinido | s12:+0.172, s4:+0.110, s2:+0.088 |
| 1 | HI_WAIT_SELECTED_D1 | 165 | 166 | preventive_schedule | 0.374 | indefinido | indefinido | s12:+0.152, s4:+0.101, s2:+0.082 |
| 1 | HI_WAIT_SELECTED_D2 | 165 | 167 | preventive_schedule | 0.374 | indefinido | indefinido | s12:+0.152, s4:+0.101, s2:+0.082 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.191 | 18.01 | 18.01 | s12:+0.187, s4:+0.126, s15:+0.103 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.191 | 18.01 | 18.01 | s12:+0.187, s4:+0.126, s15:+0.103 |
| 1 | ISO_LOWER98_M15_D1 | 155 | 156 | preventive_schedule | 0.492 | 42.40 | 14.35 | s12:+0.112, s4:+0.082, s15:+0.069 |
| 1 | ISO_LOWER98_M15_D2 | 155 | 157 | preventive_schedule | 0.492 | 42.40 | 14.35 | s12:+0.112, s4:+0.082, s15:+0.069 |
| 1 | RF_SLOPE_POINT_M15_D1 | 174 | 175 | preventive_schedule | 0.235 | 14.92 | 14.92 | s12:+0.180, s4:+0.121, s2:+0.096 |
| 1 | RF_SLOPE_POINT_M15_D2 | 174 | 176 | preventive_schedule | 0.235 | 14.92 | 14.92 | s12:+0.180, s4:+0.121, s2:+0.096 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 155 | 156 | preventive_schedule | 0.492 | 44.86 | 0.74 | s12:+0.112, s4:+0.082, s15:+0.069 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 155 | 157 | preventive_schedule | 0.492 | 44.86 | 0.74 | s12:+0.112, s4:+0.082, s15:+0.069 |
| 1 | AGE_D1 | 126 | 127 | preventive_schedule | 0.724 | indefinido | indefinido | s12:+0.064, s4:+0.052, s2:+0.043 |
| 1 | AGE_D2 | 125 | 127 | preventive_schedule | 0.742 | indefinido | indefinido | s12:+0.062, s4:+0.050, s2:+0.042 |
| 1 | HI_MARKER_D1 | 155 | 156 | preventive_schedule | 0.492 | indefinido | indefinido | s12:+0.112, s4:+0.082, s15:+0.069 |
| 1 | HI_MARKER_D2 | 155 | 157 | preventive_schedule | 0.492 | indefinido | indefinido | s12:+0.112, s4:+0.082, s15:+0.069 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 177 | 178 | preventive_schedule | 0.295 | indefinido | indefinido | s7:+0.167, s11:+0.095, s3:+0.088 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 177 | 179 | preventive_schedule | 0.295 | indefinido | indefinido | s7:+0.167, s11:+0.095, s3:+0.088 |
| 2 | HI_WAIT_SELECTED_D1 | 171 | 172 | preventive_schedule | 0.374 | indefinido | indefinido | s7:+0.156, s3:+0.084, s11:+0.080 |
| 2 | HI_WAIT_SELECTED_D2 | 171 | 173 | preventive_schedule | 0.374 | indefinido | indefinido | s7:+0.156, s3:+0.084, s11:+0.080 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.283 | 23.92 | 23.92 | s7:+0.176, s11:+0.098, s3:+0.091 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.283 | 23.92 | 23.92 | s7:+0.176, s11:+0.098, s3:+0.091 |
| 2 | ISO_LOWER98_M15_D1 | 161 | 162 | preventive_schedule | 0.495 | 35.15 | 7.95 | s7:+0.128, s3:+0.071, s2:+0.067 |
| 2 | ISO_LOWER98_M15_D2 | 161 | 163 | preventive_schedule | 0.495 | 35.15 | 7.95 | s7:+0.128, s3:+0.071, s2:+0.067 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.283 | 20.57 | 20.57 | s7:+0.176, s11:+0.098, s3:+0.091 |
| 2 | RF_SLOPE_POINT_M15_D2 | 175 | 177 | preventive_schedule | 0.316 | 16.89 | 16.89 | s7:+0.165, s3:+0.091, s11:+0.090 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 161 | 162 | preventive_schedule | 0.495 | 29.55 | 0.00 | s7:+0.128, s3:+0.071, s2:+0.067 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 161 | 163 | preventive_schedule | 0.495 | 29.55 | 0.00 | s7:+0.128, s3:+0.071, s2:+0.067 |
| 2 | AGE_D1 | 135 | 136 | preventive_schedule | 0.694 | indefinido | indefinido | s7:+0.083, s2:+0.047, s4:+0.037 |
| 2 | AGE_D2 | 134 | 136 | preventive_schedule | 0.698 | indefinido | indefinido | s7:+0.079, s2:+0.048, s4:+0.037 |
| 2 | HI_MARKER_D1 | 161 | 162 | preventive_schedule | 0.495 | indefinido | indefinido | s7:+0.128, s3:+0.071, s2:+0.067 |
| 2 | HI_MARKER_D2 | 161 | 163 | preventive_schedule | 0.495 | indefinido | indefinido | s7:+0.128, s3:+0.071, s2:+0.067 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 167 | 168 | preventive_schedule | 0.383 | indefinido | indefinido | s20:+0.101, s7:+0.100, s4:+0.095 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 167 | 169 | preventive_schedule | 0.383 | indefinido | indefinido | s20:+0.101, s7:+0.100, s4:+0.095 |
| 3 | HI_WAIT_SELECTED_D1 | 167 | 168 | preventive_schedule | 0.383 | indefinido | indefinido | s20:+0.101, s7:+0.100, s4:+0.095 |
| 3 | HI_WAIT_SELECTED_D2 | 162 | 164 | preventive_schedule | 0.449 | indefinido | indefinido | s20:+0.105, s7:+0.087, s4:+0.084 |
| 3 | ISO_POINT_M15_D1 | 179 | 180 | at_endpoint | 0.177 | 15.45 | 15.45 | s20:+0.144, s21:+0.127, s7:+0.118 |
| 3 | ISO_POINT_M15_D2 | 179 | 181 | late_schedule | 0.177 | 15.45 | 15.45 | s20:+0.144, s21:+0.127, s7:+0.118 |
| 3 | ISO_LOWER98_M15_D1 | 164 | 165 | preventive_schedule | 0.421 | 32.78 | 14.86 | s20:+0.107, s4:+0.092, s7:+0.087 |
| 3 | ISO_LOWER98_M15_D2 | 164 | 166 | preventive_schedule | 0.421 | 32.78 | 14.86 | s20:+0.107, s4:+0.092, s7:+0.087 |
| 3 | RF_SLOPE_POINT_M15_D1 | 176 | 177 | preventive_schedule | 0.197 | 15.48 | 15.48 | s20:+0.152, s21:+0.116, s4:+0.114 |
| 3 | RF_SLOPE_POINT_M15_D2 | 176 | 178 | preventive_schedule | 0.197 | 15.48 | 15.48 | s20:+0.152, s21:+0.116, s4:+0.114 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 157 | 158 | preventive_schedule | 0.492 | 35.39 | 9.19 | s20:+0.085, s4:+0.078, s7:+0.077 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 157 | 159 | preventive_schedule | 0.492 | 35.39 | 9.19 | s20:+0.085, s4:+0.078, s7:+0.077 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.746 | indefinido | indefinido | s20:+0.057, s4:+0.046, s7:+0.044 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.758 | indefinido | indefinido | s20:+0.052, s4:+0.045, s7:+0.043 |
| 3 | HI_MARKER_D1 | 157 | 158 | preventive_schedule | 0.492 | indefinido | indefinido | s20:+0.085, s4:+0.078, s7:+0.077 |
| 3 | HI_MARKER_D2 | 157 | 159 | preventive_schedule | 0.492 | indefinido | indefinido | s20:+0.085, s4:+0.078, s7:+0.077 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=155, A=155.
- Repetição2: G=161, A=161.
- Repetição3: G=157, A=157.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.33 | 0.38 | 0.00% | 20.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.33 | 0.38 | 0.00% | 20.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.93 | 0.04 | 0.00% | 6.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.93 | 0.04 | 0.00% | 6.67% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 28.05 | 15 | 2.10 | 0.71 | 0.00% | 30.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 28.05 | 15 | 1.93 | 1.00 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.27 | 0.50 | 13.33% | 40.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.62 | 0.63 | 3.33% | 36.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 44.12 | 15 | 1.83 | 1.00 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 44.12 | 15 | 1.87 | 1.00 | 0.00% | 26.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.93 | 1.00 | 0.00% | 26.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.93 | 1.00 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.27 | 0.71 | 26.67% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.27 | 0.71 | 26.67% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.43 | 0.12 | 0.00% | 13.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.43 | 0.12 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 27.21 | 15 | 2.43 | 0.57 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 27.21 | 15 | 2.43 | 0.57 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 50.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.24 | 0.56 | 3.33% | 40.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 36.76 | 15 | 2.43 | 0.57 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 36.76 | 15 | 2.43 | 0.57 | 0.00% | 30.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.43 | 0.57 | 0.00% | 30.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.43 | 0.57 | 0.00% | 30.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.73 | 1.04 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.73 | 1.04 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 3.30 | 0.11 | 0.00% | 6.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 3.30 | 1.00 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.94 | 1.17 | 40.00% | 40.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.00 | 1.17 | 40.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 17.91 | 15 | 2.23 | 1.35 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 17.91 | 15 | 2.23 | 1.35 | 0.00% | 13.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.10 | 0.42 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.93 | 0.81 | 0.00% | 10.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 26.21 | 15 | 3.27 | 1.50 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 26.21 | 15 | 3.30 | 1.50 | 0.00% | 26.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 3.30 | 1.50 | 0.00% | 26.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 3.30 | 1.50 | 0.00% | 26.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
