# FD001, motor66 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u66.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 197 | 198 | preventive_schedule | 0.299 | indefinido | indefinido | s12:+0.147, s2:+0.107, s15:+0.094 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 197 | 199 | preventive_schedule | 0.299 | indefinido | indefinido | s12:+0.147, s2:+0.107, s15:+0.094 |
| 1 | HI_WAIT_SELECTED_D1 | 190 | 191 | preventive_schedule | 0.378 | indefinido | indefinido | s12:+0.128, s2:+0.108, s15:+0.079 |
| 1 | HI_WAIT_SELECTED_D2 | 190 | 192 | preventive_schedule | 0.378 | indefinido | indefinido | s12:+0.128, s2:+0.108, s15:+0.079 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.256 | 17.87 | 17.87 | s12:+0.161, s2:+0.102, s21:+0.099 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.256 | 17.87 | 17.87 | s12:+0.161, s2:+0.102, s21:+0.099 |
| 1 | ISO_LOWER98_M15_D1 | 180 | 181 | preventive_schedule | 0.492 | 39.24 | 13.63 | s12:+0.100, s2:+0.081, s15:+0.075 |
| 1 | ISO_LOWER98_M15_D2 | 180 | 182 | preventive_schedule | 0.492 | 39.24 | 13.63 | s12:+0.100, s2:+0.081, s15:+0.075 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.256 | 16.50 | 16.50 | s12:+0.161, s2:+0.102, s21:+0.099 |
| 1 | RF_SLOPE_POINT_M15_D2 | 198 | 200 | preventive_schedule | 0.296 | 16.49 | 16.49 | s12:+0.153, s2:+0.102, s15:+0.092 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 180 | 181 | preventive_schedule | 0.492 | 36.91 | 0.00 | s12:+0.100, s2:+0.081, s15:+0.075 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 180 | 182 | preventive_schedule | 0.492 | 36.91 | 0.00 | s12:+0.100, s2:+0.081, s15:+0.075 |
| 1 | AGE_D1 | 135 | 136 | preventive_schedule | 0.796 | indefinido | indefinido | s12:+0.049, s15:+0.036, s2:+0.024 |
| 1 | AGE_D2 | 134 | 136 | preventive_schedule | 0.794 | indefinido | indefinido | s12:+0.045, s15:+0.038, s7:+0.025 |
| 1 | HI_MARKER_D1 | 180 | 181 | preventive_schedule | 0.492 | indefinido | indefinido | s12:+0.100, s2:+0.081, s15:+0.075 |
| 1 | HI_MARKER_D2 | 180 | 182 | preventive_schedule | 0.492 | indefinido | indefinido | s12:+0.100, s2:+0.081, s15:+0.075 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 194 | 195 | preventive_schedule | 0.199 | indefinido | indefinido | s2:+0.133, s4:+0.129, s11:+0.111 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 194 | 196 | preventive_schedule | 0.199 | indefinido | indefinido | s2:+0.133, s4:+0.129, s11:+0.111 |
| 2 | HI_WAIT_SELECTED_D1 | 178 | 179 | preventive_schedule | 0.413 | indefinido | indefinido | s2:+0.092, s15:+0.089, s4:+0.085 |
| 2 | HI_WAIT_SELECTED_D2 | 178 | 180 | preventive_schedule | 0.413 | indefinido | indefinido | s2:+0.092, s15:+0.089, s4:+0.085 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.119 | 22.00 | 22.00 | s4:+0.135, s2:+0.135, s11:+0.127 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.119 | 22.00 | 22.00 | s4:+0.135, s2:+0.135, s11:+0.127 |
| 2 | ISO_LOWER98_M15_D1 | 170 | 171 | preventive_schedule | 0.468 | 42.32 | 15.00 | s2:+0.085, s4:+0.080, s15:+0.080 |
| 2 | ISO_LOWER98_M15_D2 | 170 | 172 | preventive_schedule | 0.468 | 42.32 | 15.00 | s2:+0.085, s4:+0.080, s15:+0.080 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.119 | 32.13 | 32.13 | s4:+0.135, s2:+0.135, s11:+0.127 |
| 2 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.119 | 32.13 | 32.13 | s4:+0.135, s2:+0.135, s11:+0.127 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 168 | 169 | preventive_schedule | 0.495 | 44.92 | 5.85 | s2:+0.085, s4:+0.077, s15:+0.074 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 168 | 170 | preventive_schedule | 0.495 | 44.92 | 5.85 | s2:+0.085, s4:+0.077, s15:+0.074 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.781 | indefinido | indefinido | s4:+0.048, s2:+0.031, s15:+0.026 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.797 | indefinido | indefinido | s4:+0.044, s15:+0.025, s11:+0.024 |
| 2 | HI_MARKER_D1 | 168 | 169 | preventive_schedule | 0.495 | indefinido | indefinido | s2:+0.085, s4:+0.077, s15:+0.074 |
| 2 | HI_MARKER_D2 | 168 | 170 | preventive_schedule | 0.495 | indefinido | indefinido | s2:+0.085, s4:+0.077, s15:+0.074 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 194 | 195 | preventive_schedule | 0.276 | indefinido | indefinido | s21:+0.131, s20:+0.112, s12:+0.102 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 194 | 196 | preventive_schedule | 0.276 | indefinido | indefinido | s21:+0.131, s20:+0.112, s12:+0.102 |
| 3 | HI_WAIT_SELECTED_D1 | 182 | 183 | preventive_schedule | 0.426 | indefinido | indefinido | s20:+0.104, s21:+0.102, s12:+0.081 |
| 3 | HI_WAIT_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.426 | indefinido | indefinido | s20:+0.104, s21:+0.102, s12:+0.081 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.186 | 18.10 | 18.10 | s21:+0.153, s20:+0.133, s12:+0.116 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.186 | 18.10 | 18.10 | s21:+0.153, s20:+0.133, s12:+0.116 |
| 3 | ISO_LOWER98_M15_D1 | 172 | 173 | preventive_schedule | 0.499 | 42.36 | 10.73 | s21:+0.095, s20:+0.080, s12:+0.065 |
| 3 | ISO_LOWER98_M15_D2 | 172 | 174 | preventive_schedule | 0.499 | 42.36 | 10.73 | s21:+0.095, s20:+0.080, s12:+0.065 |
| 3 | RF_SLOPE_POINT_M15_D1 | 199 | 200 | preventive_schedule | 0.229 | 15.61 | 15.61 | s21:+0.138, s20:+0.124, s12:+0.113 |
| 3 | RF_SLOPE_POINT_M15_D2 | 198 | 200 | preventive_schedule | 0.241 | 16.38 | 16.38 | s21:+0.134, s20:+0.121, s12:+0.111 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 172 | 173 | preventive_schedule | 0.499 | 35.06 | 4.32 | s21:+0.095, s20:+0.080, s12:+0.065 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 172 | 174 | preventive_schedule | 0.499 | 35.06 | 4.32 | s21:+0.095, s20:+0.080, s12:+0.065 |
| 3 | AGE_D1 | 135 | 136 | preventive_schedule | 0.779 | indefinido | indefinido | s20:+0.046, s12:+0.035, s4:+0.033 |
| 3 | AGE_D2 | 134 | 136 | preventive_schedule | 0.779 | indefinido | indefinido | s20:+0.044, s4:+0.036, s12:+0.032 |
| 3 | HI_MARKER_D1 | 172 | 173 | preventive_schedule | 0.499 | indefinido | indefinido | s21:+0.095, s20:+0.080, s12:+0.065 |
| 3 | HI_MARKER_D2 | 172 | 174 | preventive_schedule | 0.499 | indefinido | indefinido | s21:+0.095, s20:+0.080, s12:+0.065 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=180, A=180.
- Repetição2: G=168, A=168.
- Repetição3: G=172, A=172.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.96 | 0.61 | 6.67% | 40.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.96 | 0.61 | 6.67% | 40.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.63 | 0.29 | 0.00% | 6.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.63 | 0.29 | 0.00% | 6.67% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 25.61 | 15 | 2.63 | 0.95 | 0.00% | 30.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 25.61 | 15 | 2.63 | 0.95 | 0.00% | 30.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 30.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.35 | 1.74 | 13.33% | 36.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 38.16 | 15 | 2.63 | 1.00 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 38.16 | 15 | 2.63 | 1.00 | 0.00% | 26.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.63 | 1.00 | 0.00% | 26.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.63 | 1.00 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.83 | 0.47 | 3.33% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.83 | 0.47 | 3.33% | 36.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.50 | 0.16 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.50 | 0.16 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.33% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 26.67% | 26.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 27.32 | 15 | 2.87 | 0.53 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 27.32 | 15 | 2.83 | 0.53 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 39.06 | 15 | 2.50 | 0.90 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 39.06 | 15 | 2.50 | 0.90 | 0.00% | 30.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.50 | 0.90 | 0.00% | 30.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.50 | 0.90 | 0.00% | 30.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.50 | 0.74 | 0.00% | 10.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.50 | 0.74 | 0.00% | 10.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.77 | 0.00 | 0.00% | 40.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.77 | 0.00 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 13.33% | 6.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 31.63 | 15 | 2.77 | 0.53 | 0.00% | 43.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 31.63 | 15 | 2.77 | 0.53 | 0.00% | 43.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.76 | 1.69 | 3.33% | 46.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.93 | 1.00 | 0.00% | 46.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 30.74 | 15 | 2.77 | 0.53 | 0.00% | 43.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 30.74 | 15 | 2.77 | 0.53 | 0.00% | 43.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.77 | 0.53 | 0.00% | 43.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.77 | 0.53 | 0.00% | 43.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
