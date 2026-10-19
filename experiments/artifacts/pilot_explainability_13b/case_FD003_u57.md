# FD003, motor57 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u57.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 198 | 199 | preventive_schedule | 0.300 | indefinido | indefinido | s11:+0.220, s4:+0.191, s8:+0.121 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 198 | 200 | preventive_schedule | 0.300 | indefinido | indefinido | s11:+0.220, s4:+0.191, s8:+0.121 |
| 1 | HI_WAIT_SELECTED_D1 | 193 | 194 | preventive_schedule | 0.333 | indefinido | indefinido | s11:+0.200, s4:+0.192, s2:+0.112 |
| 1 | HI_WAIT_SELECTED_D2 | 193 | 195 | preventive_schedule | 0.333 | indefinido | indefinido | s11:+0.200, s4:+0.192, s2:+0.112 |
| 1 | ISO_POINT_M15_D1 | 211 | 212 | preventive_schedule | 0.040 | 15.08 | 15.08 | s11:+0.297, s4:+0.266, s2:+0.174 |
| 1 | ISO_POINT_M15_D2 | 209 | 211 | preventive_schedule | 0.089 | 16.74 | 16.74 | s11:+0.285, s4:+0.246, s2:+0.164 |
| 1 | ISO_LOWER98_M15_D1 | 186 | 187 | preventive_schedule | 0.441 | 39.52 | 13.62 | s11:+0.178, s4:+0.147, s2:+0.104 |
| 1 | ISO_LOWER98_M15_D2 | 185 | 187 | preventive_schedule | 0.458 | 42.46 | 16.55 | s11:+0.173, s4:+0.139, s2:+0.106 |
| 1 | RF_SLOPE_POINT_M15_D1 | 190 | 191 | preventive_schedule | 0.370 | 14.64 | 14.64 | s11:+0.193, s4:+0.173, s2:+0.115 |
| 1 | RF_SLOPE_POINT_M15_D2 | 190 | 192 | preventive_schedule | 0.370 | 14.64 | 14.64 | s11:+0.193, s4:+0.173, s2:+0.115 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 184 | 185 | preventive_schedule | 0.481 | 41.71 | 12.16 | s11:+0.163, s4:+0.139, s2:+0.096 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 184 | 186 | preventive_schedule | 0.481 | 41.71 | 12.16 | s11:+0.163, s4:+0.139, s2:+0.096 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.781 | indefinido | indefinido | s11:+0.093, s2:+0.040, s4:+0.034 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.800 | indefinido | indefinido | s11:+0.086, s4:+0.033, s2:+0.032 |
| 1 | HI_MARKER_D1 | 183 | 184 | preventive_schedule | 0.495 | indefinido | indefinido | s11:+0.158, s4:+0.140, s2:+0.093 |
| 1 | HI_MARKER_D2 | 183 | 185 | preventive_schedule | 0.495 | indefinido | indefinido | s11:+0.158, s4:+0.140, s2:+0.093 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 190 | 191 | preventive_schedule | 0.376 | indefinido | indefinido | s8:+0.475, s15:-0.191, s11:+0.147 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 190 | 192 | preventive_schedule | 0.376 | indefinido | indefinido | s8:+0.475, s15:-0.191, s11:+0.147 |
| 2 | HI_WAIT_SELECTED_D1 | 194 | 195 | preventive_schedule | 0.342 | indefinido | indefinido | s8:+0.508, s15:-0.217, s11:+0.157 |
| 2 | HI_WAIT_SELECTED_D2 | 194 | 196 | preventive_schedule | 0.342 | indefinido | indefinido | s8:+0.508, s15:-0.217, s11:+0.157 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.000 | 16.02 | 16.02 | s8:+0.833, s15:-0.364, s11:+0.241 |
| 2 | ISO_POINT_M15_D2 | 213 | 215 | at_endpoint | 0.002 | 16.02 | 16.02 | s8:+0.814, s15:-0.361, s11:+0.232 |
| 2 | ISO_LOWER98_M15_D1 | 184 | 185 | preventive_schedule | 0.497 | 87.77 | 13.72 | s8:+0.390, s15:-0.174, s11:+0.124 |
| 2 | ISO_LOWER98_M15_D2 | 184 | 186 | preventive_schedule | 0.497 | 87.77 | 13.72 | s8:+0.390, s15:-0.174, s11:+0.124 |
| 2 | RF_SLOPE_POINT_M15_D1 | 187 | 188 | preventive_schedule | 0.437 | 14.63 | 14.63 | s8:+0.435, s15:-0.191, s11:+0.138 |
| 2 | RF_SLOPE_POINT_M15_D2 | 187 | 189 | preventive_schedule | 0.437 | 14.63 | 14.63 | s8:+0.435, s15:-0.191, s11:+0.138 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 184 | 185 | preventive_schedule | 0.497 | 31.81 | 0.00 | s8:+0.390, s15:-0.174, s11:+0.124 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 184 | 186 | preventive_schedule | 0.497 | 31.81 | 0.00 | s8:+0.390, s15:-0.174, s11:+0.124 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.817 | indefinido | indefinido | s8:+0.103, s11:+0.071, s15:-0.058 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.826 | indefinido | indefinido | s8:+0.106, s11:+0.066, s15:-0.062 |
| 2 | HI_MARKER_D1 | 184 | 185 | preventive_schedule | 0.497 | indefinido | indefinido | s8:+0.390, s15:-0.174, s11:+0.124 |
| 2 | HI_MARKER_D2 | 184 | 186 | preventive_schedule | 0.497 | indefinido | indefinido | s8:+0.390, s15:-0.174, s11:+0.124 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 195 | 196 | preventive_schedule | 0.381 | indefinido | indefinido | s4:+0.262, s11:+0.251, s2:+0.105 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 195 | 197 | preventive_schedule | 0.381 | indefinido | indefinido | s4:+0.262, s11:+0.251, s2:+0.105 |
| 3 | HI_WAIT_SELECTED_D1 | 196 | 197 | preventive_schedule | 0.377 | indefinido | indefinido | s4:+0.264, s11:+0.254, s2:+0.105 |
| 3 | HI_WAIT_SELECTED_D2 | 196 | 198 | preventive_schedule | 0.377 | indefinido | indefinido | s4:+0.264, s11:+0.254, s2:+0.105 |
| 3 | ISO_POINT_M15_D1 | 208 | 209 | preventive_schedule | 0.210 | 15.67 | 15.67 | s11:+0.334, s4:+0.313, s2:+0.142 |
| 3 | ISO_POINT_M15_D2 | 208 | 210 | preventive_schedule | 0.210 | 15.67 | 15.67 | s11:+0.334, s4:+0.313, s2:+0.142 |
| 3 | ISO_LOWER98_M15_D1 | 186 | 187 | preventive_schedule | 0.499 | 38.27 | 9.38 | s11:+0.211, s4:+0.195, s2:+0.095 |
| 3 | ISO_LOWER98_M15_D2 | 186 | 188 | preventive_schedule | 0.499 | 38.27 | 9.38 | s11:+0.211, s4:+0.195, s2:+0.095 |
| 3 | RF_SLOPE_POINT_M15_D1 | 210 | 211 | preventive_schedule | 0.169 | 13.03 | 13.03 | s11:+0.343, s4:+0.336, s2:+0.152 |
| 3 | RF_SLOPE_POINT_M15_D2 | 210 | 212 | preventive_schedule | 0.169 | 13.03 | 13.03 | s11:+0.343, s4:+0.336, s2:+0.152 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 186 | 187 | preventive_schedule | 0.499 | 46.78 | 11.83 | s11:+0.211, s4:+0.195, s2:+0.095 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 186 | 188 | preventive_schedule | 0.499 | 46.78 | 11.83 | s11:+0.211, s4:+0.195, s2:+0.095 |
| 3 | AGE_D1 | 151 | 152 | preventive_schedule | 0.776 | indefinido | indefinido | s11:+0.114, s4:+0.071, s2:+0.039 |
| 3 | AGE_D2 | 150 | 152 | preventive_schedule | 0.766 | indefinido | indefinido | s11:+0.122, s4:+0.070, s2:+0.043 |
| 3 | HI_MARKER_D1 | 186 | 187 | preventive_schedule | 0.499 | indefinido | indefinido | s11:+0.211, s4:+0.195, s2:+0.095 |
| 3 | HI_MARKER_D2 | 186 | 188 | preventive_schedule | 0.499 | indefinido | indefinido | s11:+0.211, s4:+0.195, s2:+0.095 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=183, A=183.
- Repetição2: G=184, A=184.
- Repetição3: G=186, A=186.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.30 | 1.10 | 0.00% | 33.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.30 | 1.10 | 0.00% | 33.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.10 | 0.00 | 0.00% | 13.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.10 | 0.00 | 0.00% | 13.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.80 | 0.28 | 0.00% | 16.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.77 | 0.12 | 0.00% | 16.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 25.91 | 15 | 1.20 | 0.30 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 25.91 | 15 | 1.20 | 0.30 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.17 | 0.33 | 0.00% | 30.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.03 | 0.33 | 0.00% | 30.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 29.56 | 15 | 0.60 | 0.52 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 29.56 | 15 | 0.53 | 0.62 | 0.00% | 20.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.10 | 0.26 | 0.00% | 23.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.10 | 0.26 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.97 | 0.33 | 0.00% | 10.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.97 | 0.33 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.13 | 0.00 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.13 | 0.00 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.41 | 0.08 | 10.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 74.05 | 15 | 1.10 | 0.33 | 0.00% | 20.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 74.05 | 15 | 1.10 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.47 | 0.25 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.47 | 0.25 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 136.85 | 15 | 1.13 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 136.85 | 15 | 1.13 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.13 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.13 | 0.32 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.62 | 0.41 | 0.00% | 9.38% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.62 | 0.41 | 0.00% | 9.38% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.12 | 0.03 | 0.00% | 9.38% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.12 | 0.03 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.81 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.81 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 28.89 | 15 | 1.12 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 28.89 | 15 | 1.12 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.44 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.53 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 34.95 | 15 | 1.12 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 34.95 | 15 | 1.12 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.12 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.12 | 0.24 | 0.00% | 9.38% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
