# FD001, motor84 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u84.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 252 | 253 | preventive_schedule | 0.299 | indefinido | indefinido | s12:+0.082, s2:+0.082, s21:+0.079 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 243 | 245 | preventive_schedule | 0.391 | indefinido | indefinido | s12:+0.084, s2:+0.068, s7:+0.064 |
| 1 | HI_WAIT_SELECTED_D1 | 240 | 241 | preventive_schedule | 0.422 | indefinido | indefinido | s12:+0.083, s2:+0.063, s7:+0.059 |
| 1 | HI_WAIT_SELECTED_D2 | 240 | 242 | preventive_schedule | 0.422 | indefinido | indefinido | s12:+0.083, s2:+0.063, s7:+0.059 |
| 1 | ISO_POINT_M15_D1 | 261 | 262 | preventive_schedule | 0.184 | 15.33 | 15.33 | s2:+0.108, s12:+0.098, s21:+0.088 |
| 1 | ISO_POINT_M15_D2 | 261 | 263 | preventive_schedule | 0.184 | 15.33 | 15.33 | s2:+0.108, s12:+0.098, s21:+0.088 |
| 1 | ISO_LOWER98_M15_D1 | 232 | 233 | preventive_schedule | 0.472 | 35.56 | 14.00 | s12:+0.075, s2:+0.057, s7:+0.055 |
| 1 | ISO_LOWER98_M15_D2 | 230 | 232 | preventive_schedule | 0.495 | 37.64 | 16.08 | s12:+0.073, s7:+0.051, s8:+0.048 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.140 | 28.89 | 28.89 | s12:+0.108, s2:+0.104, s21:+0.097 |
| 1 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.140 | 28.89 | 28.89 | s12:+0.108, s2:+0.104, s21:+0.097 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 244 | 245 | preventive_schedule | 0.372 | 48.15 | 1.89 | s12:+0.085, s2:+0.070, s21:+0.066 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 243 | 245 | preventive_schedule | 0.391 | 63.18 | 16.92 | s12:+0.084, s2:+0.068, s7:+0.064 |
| 1 | AGE_D1 | 133 | 134 | preventive_schedule | 0.902 | indefinido | indefinido | s8:+0.025, s2:-0.021, s20:+0.019 |
| 1 | AGE_D2 | 132 | 134 | preventive_schedule | 0.902 | indefinido | indefinido | s8:+0.025, s2:-0.021, s20:+0.018 |
| 1 | HI_MARKER_D1 | 230 | 231 | preventive_schedule | 0.495 | indefinido | indefinido | s12:+0.073, s7:+0.051, s8:+0.048 |
| 1 | HI_MARKER_D2 | 230 | 232 | preventive_schedule | 0.495 | indefinido | indefinido | s12:+0.073, s7:+0.051, s8:+0.048 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 255 | 256 | preventive_schedule | 0.298 | indefinido | indefinido | s7:+0.146, s3:+0.100, s11:+0.090 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 255 | 257 | preventive_schedule | 0.298 | indefinido | indefinido | s7:+0.146, s3:+0.100, s11:+0.090 |
| 2 | HI_WAIT_SELECTED_D1 | 244 | 245 | preventive_schedule | 0.413 | indefinido | indefinido | s7:+0.114, s3:+0.088, s11:+0.069 |
| 2 | HI_WAIT_SELECTED_D2 | 244 | 246 | preventive_schedule | 0.413 | indefinido | indefinido | s7:+0.114, s3:+0.088, s11:+0.069 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.196 | 19.17 | 19.17 | s7:+0.154, s11:+0.100, s3:+0.100 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.196 | 19.17 | 19.17 | s7:+0.154, s11:+0.100, s3:+0.100 |
| 2 | ISO_LOWER98_M15_D1 | 234 | 235 | preventive_schedule | 0.499 | 40.21 | 13.00 | s7:+0.107, s4:+0.069, s15:+0.061 |
| 2 | ISO_LOWER98_M15_D2 | 234 | 236 | preventive_schedule | 0.499 | 40.21 | 13.00 | s7:+0.107, s4:+0.069, s15:+0.061 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.196 | 28.00 | 28.00 | s7:+0.154, s11:+0.100, s3:+0.100 |
| 2 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.196 | 28.00 | 28.00 | s7:+0.154, s11:+0.100, s3:+0.100 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 238 | 239 | preventive_schedule | 0.470 | 48.85 | 12.09 | s7:+0.109, s4:+0.069, s3:+0.069 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 238 | 240 | preventive_schedule | 0.470 | 48.85 | 12.09 | s7:+0.109, s4:+0.069, s3:+0.069 |
| 2 | AGE_D1 | 135 | 136 | preventive_schedule | 0.906 | indefinido | indefinido | s7:+0.024, s8:+0.019, s11:+0.016 |
| 2 | AGE_D2 | 134 | 136 | preventive_schedule | 0.914 | indefinido | indefinido | s7:+0.025, s8:+0.018, s2:-0.016 |
| 2 | HI_MARKER_D1 | 234 | 235 | preventive_schedule | 0.499 | indefinido | indefinido | s7:+0.107, s4:+0.069, s15:+0.061 |
| 2 | HI_MARKER_D2 | 234 | 236 | preventive_schedule | 0.499 | indefinido | indefinido | s7:+0.107, s4:+0.069, s15:+0.061 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 250 | 251 | preventive_schedule | 0.296 | indefinido | indefinido | s21:+0.140, s20:+0.115, s12:+0.096 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 250 | 252 | preventive_schedule | 0.296 | indefinido | indefinido | s21:+0.140, s20:+0.115, s12:+0.096 |
| 3 | HI_WAIT_SELECTED_D1 | 236 | 237 | preventive_schedule | 0.434 | indefinido | indefinido | s20:+0.093, s21:+0.093, s12:+0.091 |
| 3 | HI_WAIT_SELECTED_D2 | 236 | 238 | preventive_schedule | 0.434 | indefinido | indefinido | s20:+0.093, s21:+0.093, s12:+0.091 |
| 3 | ISO_POINT_M15_D1 | 264 | 265 | preventive_schedule | 0.125 | 15.01 | 15.01 | s20:+0.167, s21:+0.159, s12:+0.117 |
| 3 | ISO_POINT_M15_D2 | 262 | 264 | preventive_schedule | 0.153 | 16.46 | 16.46 | s20:+0.158, s21:+0.150, s12:+0.117 |
| 3 | ISO_LOWER98_M15_D1 | 226 | 227 | preventive_schedule | 0.497 | 42.20 | 10.57 | s20:+0.107, s12:+0.077, s4:+0.065 |
| 3 | ISO_LOWER98_M15_D2 | 226 | 228 | preventive_schedule | 0.497 | 42.20 | 10.57 | s20:+0.107, s12:+0.077, s4:+0.065 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.103 | 16.30 | 16.30 | s21:+0.168, s20:+0.164, s12:+0.122 |
| 3 | RF_SLOPE_POINT_M15_D2 | 266 | 268 | late_schedule | 0.103 | 16.30 | 16.30 | s21:+0.168, s20:+0.164, s12:+0.122 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 238 | 239 | preventive_schedule | 0.413 | 45.36 | 14.62 | s12:+0.095, s21:+0.095, s20:+0.094 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 238 | 240 | preventive_schedule | 0.413 | 45.36 | 14.62 | s12:+0.095, s21:+0.095, s20:+0.094 |
| 3 | AGE_D1 | 135 | 136 | preventive_schedule | 0.875 | indefinido | indefinido | s20:+0.040, s21:+0.025, s4:+0.017 |
| 3 | AGE_D2 | 134 | 136 | preventive_schedule | 0.886 | indefinido | indefinido | s20:+0.039, s21:+0.024, s4:+0.015 |
| 3 | HI_MARKER_D1 | 226 | 227 | preventive_schedule | 0.497 | indefinido | indefinido | s20:+0.107, s12:+0.077, s4:+0.065 |
| 3 | HI_MARKER_D2 | 226 | 228 | preventive_schedule | 0.497 | indefinido | indefinido | s20:+0.107, s12:+0.077, s4:+0.065 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=230, A=230.
- Repetição2: G=234, A=234.
- Repetição3: G=226, A=226.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.00 | 1.17 | 0.00% | 40.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.37 | 0.81 | 0.00% | 30.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 3.63 | 0.92 | 0.00% | 13.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 3.63 | 0.92 | 0.00% | 13.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.38 | 0.11 | 3.33% | 40.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.38 | 0.11 | 3.33% | 40.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 21.56 | 15 | 3.47 | 0.72 | 0.00% | 40.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 21.56 | 15 | 3.63 | 2.00 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 46.26 | 15 | 4.73 | 1.43 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 46.26 | 15 | 4.57 | 1.76 | 0.00% | 43.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 3.63 | 2.00 | 0.00% | 36.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 3.63 | 2.00 | 0.00% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.23 | 0.35 | 0.00% | 33.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.23 | 0.35 | 0.00% | 33.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.63 | 0.00 | 0.00% | 33.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.63 | 0.00 | 0.00% | 33.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 20.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 23.33% | 13.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 27.21 | 15 | 2.63 | 0.63 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 27.21 | 15 | 2.63 | 0.63 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 20.00% | 0.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 36.76 | 15 | 0.50 | 0.52 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 36.76 | 15 | 0.50 | 0.52 | 0.00% | 30.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.63 | 0.63 | 0.00% | 36.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.63 | 0.63 | 0.00% | 36.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.00 | 0.15 | 0.00% | 33.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.00 | 0.15 | 0.00% | 33.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 4.53 | 0.00 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 4.53 | 0.00 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.36 | 0.61 | 16.67% | 40.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.21 | 0.59 | 6.67% | 43.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 31.63 | 15 | 4.53 | 0.78 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 31.63 | 15 | 4.53 | 0.78 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 26.67% | 46.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.34 | 1.76 | 3.33% | 43.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 30.74 | 15 | 7.23 | 0.53 | 0.00% | 43.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 30.74 | 15 | 7.17 | 0.56 | 0.00% | 40.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 4.53 | 0.78 | 0.00% | 40.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 4.53 | 0.78 | 0.00% | 40.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
