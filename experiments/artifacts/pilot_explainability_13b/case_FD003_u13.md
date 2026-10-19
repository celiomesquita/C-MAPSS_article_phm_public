# FD003, motor13 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u13.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 178 | 179 | preventive_schedule | 0.283 | indefinido | indefinido | s4:+0.220, s11:+0.145, s2:+0.128 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 178 | 180 | preventive_schedule | 0.283 | indefinido | indefinido | s4:+0.220, s11:+0.145, s2:+0.128 |
| 1 | HI_WAIT_SELECTED_D1 | 176 | 177 | preventive_schedule | 0.340 | indefinido | indefinido | s4:+0.201, s11:+0.133, s2:+0.118 |
| 1 | HI_WAIT_SELECTED_D2 | 176 | 178 | preventive_schedule | 0.340 | indefinido | indefinido | s4:+0.201, s11:+0.133, s2:+0.118 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.125 | 18.24 | 18.24 | s4:+0.254, s2:+0.182, s11:+0.172 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.125 | 18.24 | 18.24 | s4:+0.254, s2:+0.182, s11:+0.172 |
| 1 | ISO_LOWER98_M15_D1 | 171 | 172 | preventive_schedule | 0.439 | 39.52 | 13.62 | s4:+0.176, s11:+0.108, s2:+0.089 |
| 1 | ISO_LOWER98_M15_D2 | 168 | 170 | preventive_schedule | 0.464 | 42.61 | 16.71 | s4:+0.172, s11:+0.104, s2:+0.087 |
| 1 | RF_SLOPE_POINT_M15_D1 | 174 | 175 | preventive_schedule | 0.372 | 15.18 | 15.18 | s4:+0.197, s11:+0.123, s2:+0.109 |
| 1 | RF_SLOPE_POINT_M15_D2 | 174 | 176 | preventive_schedule | 0.372 | 15.18 | 15.18 | s4:+0.197, s11:+0.123, s2:+0.109 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 167 | 168 | preventive_schedule | 0.473 | 41.29 | 11.73 | s4:+0.174, s11:+0.106, s2:+0.081 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 167 | 169 | preventive_schedule | 0.473 | 41.29 | 11.73 | s4:+0.174, s11:+0.106, s2:+0.081 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.675 | indefinido | indefinido | s4:+0.084, s11:+0.081, s2:+0.073 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.690 | indefinido | indefinido | s4:+0.083, s11:+0.078, s2:+0.065 |
| 1 | HI_MARKER_D1 | 166 | 167 | preventive_schedule | 0.494 | indefinido | indefinido | s4:+0.162, s11:+0.096, s2:+0.083 |
| 1 | HI_MARKER_D2 | 166 | 168 | preventive_schedule | 0.494 | indefinido | indefinido | s4:+0.162, s11:+0.096, s2:+0.083 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | indefinido | endpoint_without_decision | 0.327 | indefinido | indefinido | s11:+0.429, s4:+0.155, s15:+0.082 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | indefinido | endpoint_without_decision | 0.327 | indefinido | indefinido | s11:+0.429, s4:+0.155, s15:+0.082 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | indefinido | endpoint_without_decision | 0.327 | indefinido | indefinido | s11:+0.429, s4:+0.155, s15:+0.082 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | indefinido | endpoint_without_decision | 0.327 | indefinido | indefinido | s11:+0.429, s4:+0.155, s15:+0.082 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.327 | 18.64 | 18.64 | s11:+0.429, s4:+0.155, s15:+0.082 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.327 | 18.64 | 18.64 | s11:+0.429, s4:+0.155, s15:+0.082 |
| 2 | ISO_LOWER98_M15_D1 | 175 | 176 | preventive_schedule | 0.482 | 28.59 | 9.35 | s11:+0.330, s4:+0.121, s15:+0.064 |
| 2 | ISO_LOWER98_M15_D2 | 175 | 177 | preventive_schedule | 0.482 | 28.59 | 9.35 | s11:+0.330, s4:+0.121, s15:+0.064 |
| 2 | RF_SLOPE_POINT_M15_D1 | 184 | 185 | at_endpoint | 0.327 | 14.26 | 14.26 | s11:+0.429, s4:+0.155, s15:+0.082 |
| 2 | RF_SLOPE_POINT_M15_D2 | 184 | 186 | late_schedule | 0.327 | 14.26 | 14.26 | s11:+0.429, s4:+0.155, s15:+0.082 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 175 | 176 | preventive_schedule | 0.482 | 36.39 | 13.88 | s11:+0.330, s4:+0.121, s15:+0.064 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 175 | 177 | preventive_schedule | 0.482 | 36.39 | 13.88 | s11:+0.330, s4:+0.121, s15:+0.064 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.716 | indefinido | indefinido | s11:+0.191, s4:+0.056, s15:+0.040 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.722 | indefinido | indefinido | s11:+0.190, s4:+0.053, s15:+0.038 |
| 2 | HI_MARKER_D1 | 175 | 176 | preventive_schedule | 0.482 | indefinido | indefinido | s11:+0.330, s4:+0.121, s15:+0.064 |
| 2 | HI_MARKER_D2 | 175 | 177 | preventive_schedule | 0.482 | indefinido | indefinido | s11:+0.330, s4:+0.121, s15:+0.064 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 182 | 183 | preventive_schedule | 0.276 | indefinido | indefinido | s11:+0.215, s15:+0.162, s9:+0.137 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 177 | 179 | preventive_schedule | 0.367 | indefinido | indefinido | s11:+0.202, s15:+0.143, s9:+0.119 |
| 3 | HI_WAIT_SELECTED_D1 | 181 | 182 | preventive_schedule | 0.306 | indefinido | indefinido | s11:+0.215, s15:+0.147, s9:+0.134 |
| 3 | HI_WAIT_SELECTED_D2 | 181 | 183 | preventive_schedule | 0.306 | indefinido | indefinido | s11:+0.215, s15:+0.147, s9:+0.134 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.200 | 16.85 | 16.85 | s11:+0.246, s15:+0.170, s9:+0.145 |
| 3 | ISO_POINT_M15_D2 | 183 | 185 | at_endpoint | 0.233 | 16.90 | 16.90 | s11:+0.232, s15:+0.167, s9:+0.141 |
| 3 | ISO_LOWER98_M15_D1 | 171 | 172 | preventive_schedule | 0.494 | 40.28 | 16.00 | s11:+0.155, s15:+0.119, s9:+0.100 |
| 3 | ISO_LOWER98_M15_D2 | 171 | 173 | preventive_schedule | 0.494 | 40.28 | 16.00 | s11:+0.155, s15:+0.119, s9:+0.100 |
| 3 | RF_SLOPE_POINT_M15_D1 | 181 | 182 | preventive_schedule | 0.306 | 15.83 | 15.83 | s11:+0.215, s15:+0.147, s9:+0.134 |
| 3 | RF_SLOPE_POINT_M15_D2 | 181 | 183 | preventive_schedule | 0.306 | 15.83 | 15.83 | s11:+0.215, s15:+0.147, s9:+0.134 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 171 | 172 | preventive_schedule | 0.494 | 43.49 | 0.00 | s11:+0.155, s15:+0.119, s9:+0.100 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 171 | 173 | preventive_schedule | 0.494 | 43.49 | 0.00 | s11:+0.155, s15:+0.119, s9:+0.100 |
| 3 | AGE_D1 | 154 | 155 | preventive_schedule | 0.670 | indefinido | indefinido | s15:+0.093, s11:+0.083, s9:+0.063 |
| 3 | AGE_D2 | 153 | 155 | preventive_schedule | 0.687 | indefinido | indefinido | s11:+0.084, s15:+0.081, s9:+0.061 |
| 3 | HI_MARKER_D1 | 171 | 172 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.155, s15:+0.119, s9:+0.100 |
| 3 | HI_MARKER_D2 | 171 | 173 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.155, s15:+0.119, s9:+0.100 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=166, A=166.
- Repetição2: G=175, A=175.
- Repetição3: G=171, A=171.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.10 | 0.36 | 0.00% | 16.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.10 | 0.36 | 0.00% | 16.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.17 | 0.00 | 0.00% | 10.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.17 | 0.00 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 20.00% | 10.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 25.91 | 15 | 1.57 | 0.57 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 25.91 | 15 | 1.83 | 0.50 | 0.00% | 33.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.74 | 0.00 | 10.00% | 43.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.03 | 0.00 | 3.33% | 43.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 29.56 | 15 | 1.17 | 0.33 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 29.56 | 15 | 1.13 | 0.33 | 0.00% | 20.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.17 | 0.22 | 0.00% | 23.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.17 | 0.22 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | indefinido | indefinido | 10.00% | 6.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | indefinido | indefinido | 10.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | indefinido | indefinido | 13.33% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | indefinido | indefinido | 13.33% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.67% | 3.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 6.67% | 3.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 19.25 | 15 | 1.03 | 0.22 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 19.25 | 15 | 1.03 | 0.22 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.44 | 0.11 | 10.00% | 6.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.57 | 0.28 | 6.67% | 3.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 22.51 | 15 | 1.03 | 0.22 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 22.51 | 15 | 1.03 | 0.22 | 0.00% | 10.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.03 | 0.22 | 0.00% | 10.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.03 | 0.22 | 0.00% | 10.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.97 | 0.46 | 3.33% | 13.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.30 | 0.58 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.33 | 0.04 | 10.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.33 | 0.04 | 10.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 16.67% | 16.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.46 | 0.16 | 13.33% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 24.28 | 15 | 1.67 | 0.71 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 24.28 | 15 | 1.67 | 0.71 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.66 | 0.62 | 3.33% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.79 | 0.62 | 3.33% | 13.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 54.70 | 15 | 1.60 | 0.71 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 54.70 | 15 | 1.60 | 0.71 | 0.00% | 20.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.67 | 0.71 | 0.00% | 20.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.67 | 0.71 | 0.00% | 20.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
