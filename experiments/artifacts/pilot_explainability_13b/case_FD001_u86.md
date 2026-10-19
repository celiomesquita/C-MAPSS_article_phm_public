# FD001, motor86 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u86.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 247 | 248 | preventive_schedule | 0.291 | indefinido | indefinido | s12:+0.122, s21:+0.107, s7:+0.104 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 247 | 249 | preventive_schedule | 0.291 | indefinido | indefinido | s12:+0.122, s21:+0.107, s7:+0.104 |
| 1 | HI_WAIT_SELECTED_D1 | 233 | 234 | preventive_schedule | 0.455 | indefinido | indefinido | s12:+0.099, s21:+0.077, s7:+0.076 |
| 1 | HI_WAIT_SELECTED_D2 | 233 | 235 | preventive_schedule | 0.455 | indefinido | indefinido | s12:+0.099, s21:+0.077, s7:+0.076 |
| 1 | ISO_POINT_M15_D1 | 250 | 251 | preventive_schedule | 0.257 | 15.41 | 15.41 | s12:+0.120, s21:+0.113, s7:+0.107 |
| 1 | ISO_POINT_M15_D2 | 250 | 252 | preventive_schedule | 0.257 | 15.41 | 15.41 | s12:+0.120, s21:+0.113, s7:+0.107 |
| 1 | ISO_LOWER98_M15_D1 | 223 | 224 | preventive_schedule | 0.491 | 39.63 | 12.00 | s21:+0.087, s12:+0.075, s7:+0.066 |
| 1 | ISO_LOWER98_M15_D2 | 223 | 225 | preventive_schedule | 0.491 | 39.63 | 12.00 | s21:+0.087, s12:+0.075, s7:+0.066 |
| 1 | RF_SLOPE_POINT_M15_D1 | 250 | 251 | preventive_schedule | 0.257 | 12.69 | 12.69 | s12:+0.120, s21:+0.113, s7:+0.107 |
| 1 | RF_SLOPE_POINT_M15_D2 | 249 | 251 | preventive_schedule | 0.267 | 16.60 | 16.60 | s12:+0.119, s7:+0.110, s21:+0.109 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 223 | 224 | preventive_schedule | 0.491 | 60.30 | 4.17 | s21:+0.087, s12:+0.075, s7:+0.066 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 223 | 225 | preventive_schedule | 0.491 | 60.30 | 4.17 | s21:+0.087, s12:+0.075, s7:+0.066 |
| 1 | AGE_D1 | 126 | 127 | preventive_schedule | 0.882 | indefinido | indefinido | s21:+0.028, s20:+0.018, s12:+0.013 |
| 1 | AGE_D2 | 125 | 127 | preventive_schedule | 0.879 | indefinido | indefinido | s21:+0.026, s20:+0.019, s12:+0.016 |
| 1 | HI_MARKER_D1 | 223 | 224 | preventive_schedule | 0.491 | indefinido | indefinido | s21:+0.087, s12:+0.075, s7:+0.066 |
| 1 | HI_MARKER_D2 | 223 | 225 | preventive_schedule | 0.491 | indefinido | indefinido | s21:+0.087, s12:+0.075, s7:+0.066 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 236 | 237 | preventive_schedule | 0.399 | indefinido | indefinido | s7:+0.095, s20:+0.079, s4:+0.077 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 236 | 238 | preventive_schedule | 0.399 | indefinido | indefinido | s7:+0.095, s20:+0.079, s4:+0.077 |
| 2 | HI_WAIT_SELECTED_D1 | 225 | 226 | preventive_schedule | 0.439 | indefinido | indefinido | s2:+0.088, s11:+0.075, s20:+0.070 |
| 2 | HI_WAIT_SELECTED_D2 | 220 | 222 | preventive_schedule | 0.468 | indefinido | indefinido | s2:+0.080, s11:+0.075, s7:+0.071 |
| 2 | ISO_POINT_M15_D1 | 269 | 270 | preventive_schedule | 0.007 | 13.40 | 13.40 | s11:+0.151, s7:+0.137, s4:+0.126 |
| 2 | ISO_POINT_M15_D2 | 262 | 264 | preventive_schedule | 0.101 | 16.66 | 16.66 | s11:+0.137, s4:+0.122, s7:+0.119 |
| 2 | ISO_LOWER98_M15_D1 | 217 | 218 | preventive_schedule | 0.475 | 41.62 | 13.36 | s2:+0.075, s11:+0.073, s4:+0.071 |
| 2 | ISO_LOWER98_M15_D2 | 215 | 217 | preventive_schedule | 0.499 | 45.26 | 17.00 | s7:+0.071, s11:+0.071, s4:+0.067 |
| 2 | RF_SLOPE_POINT_M15_D1 | 270 | 271 | preventive_schedule | 0.000 | 15.70 | 15.70 | s11:+0.149, s7:+0.142, s4:+0.130 |
| 2 | RF_SLOPE_POINT_M15_D2 | 259 | 261 | preventive_schedule | 0.137 | 16.79 | 16.79 | s11:+0.130, s4:+0.121, s7:+0.118 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 216 | 217 | preventive_schedule | 0.483 | 51.00 | 14.54 | s11:+0.074, s7:+0.072, s2:+0.069 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 216 | 218 | preventive_schedule | 0.483 | 51.00 | 14.54 | s11:+0.074, s7:+0.072, s2:+0.069 |
| 2 | AGE_D1 | 133 | 134 | preventive_schedule | 0.916 | indefinido | indefinido | s7:+0.025, s2:-0.022, s11:+0.016 |
| 2 | AGE_D2 | 132 | 134 | preventive_schedule | 0.916 | indefinido | indefinido | s7:+0.024, s2:-0.020, s11:+0.016 |
| 2 | HI_MARKER_D1 | 215 | 216 | preventive_schedule | 0.499 | indefinido | indefinido | s7:+0.071, s11:+0.071, s4:+0.067 |
| 2 | HI_MARKER_D2 | 215 | 217 | preventive_schedule | 0.499 | indefinido | indefinido | s7:+0.071, s11:+0.071, s4:+0.067 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 247 | 248 | preventive_schedule | 0.300 | indefinido | indefinido | s15:+0.145, s7:+0.140, s12:+0.087 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 240 | 242 | preventive_schedule | 0.393 | indefinido | indefinido | s7:+0.127, s15:+0.116, s12:+0.078 |
| 3 | HI_WAIT_SELECTED_D1 | 233 | 234 | preventive_schedule | 0.455 | indefinido | indefinido | s15:+0.112, s7:+0.103, s12:+0.070 |
| 3 | HI_WAIT_SELECTED_D2 | 233 | 235 | preventive_schedule | 0.455 | indefinido | indefinido | s15:+0.112, s7:+0.103, s12:+0.070 |
| 3 | ISO_POINT_M15_D1 | 259 | 260 | preventive_schedule | 0.194 | 14.67 | 14.67 | s15:+0.171, s7:+0.147, s12:+0.094 |
| 3 | ISO_POINT_M15_D2 | 258 | 260 | preventive_schedule | 0.200 | 16.77 | 16.77 | s15:+0.179, s7:+0.142, s12:+0.092 |
| 3 | ISO_LOWER98_M15_D1 | 227 | 228 | preventive_schedule | 0.476 | 33.14 | 15.24 | s15:+0.114, s7:+0.094, s12:+0.060 |
| 3 | ISO_LOWER98_M15_D2 | 227 | 229 | preventive_schedule | 0.476 | 33.14 | 15.24 | s15:+0.114, s7:+0.094, s12:+0.060 |
| 3 | RF_SLOPE_POINT_M15_D1 | 277 | 278 | at_endpoint | 0.014 | 14.95 | 14.95 | s15:+0.194, s7:+0.193, s12:+0.126 |
| 3 | RF_SLOPE_POINT_M15_D2 | 276 | 278 | at_endpoint | 0.023 | 16.67 | 16.67 | s15:+0.196, s7:+0.191, s12:+0.120 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 236 | 237 | preventive_schedule | 0.423 | 50.14 | 15.18 | s7:+0.118, s15:+0.115, s12:+0.077 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 236 | 238 | preventive_schedule | 0.423 | 50.14 | 15.18 | s7:+0.118, s15:+0.115, s12:+0.077 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.893 | indefinido | indefinido | s15:+0.020, s7:+0.018, s20:+0.017 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.891 | indefinido | indefinido | s15:+0.021, s7:+0.020, s20:+0.017 |
| 3 | HI_MARKER_D1 | 223 | 224 | preventive_schedule | 0.493 | indefinido | indefinido | s15:+0.114, s7:+0.088, s2:+0.054 |
| 3 | HI_MARKER_D2 | 223 | 225 | preventive_schedule | 0.493 | indefinido | indefinido | s15:+0.114, s7:+0.088, s2:+0.054 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=223, A=223.
- Repetição2: G=215, A=215.
- Repetição3: G=223, A=223.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.27 | 0.38 | 0.00% | 30.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.27 | 0.38 | 0.00% | 30.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 4.57 | 0.17 | 0.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 4.57 | 0.17 | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.53 | 0.50 | 0.00% | 46.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.50 | 0.50 | 0.00% | 46.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 27.63 | 15 | 4.57 | 2.19 | 0.00% | 30.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 27.63 | 15 | 4.57 | 2.19 | 0.00% | 30.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.13 | 1.00 | 0.00% | 33.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.40 | 0.69 | 0.00% | 46.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 56.13 | 15 | 4.77 | 2.30 | 0.00% | 33.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 56.13 | 15 | 4.53 | 2.30 | 0.00% | 33.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 4.57 | 2.19 | 0.00% | 30.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 4.57 | 2.19 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 3.67 | 1.00 | 0.00% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 3.67 | 1.00 | 0.00% | 36.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.70 | 0.00 | 0.00% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.70 | 0.05 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.63 | 0.57 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.93 | 1.00 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 28.26 | 15 | 3.43 | 0.62 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 28.26 | 15 | 2.70 | 0.32 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.27 | 0.71 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.23 | 2.58 | 0.00% | 60.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 36.46 | 15 | 2.53 | 0.45 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 36.46 | 15 | 1.80 | 0.55 | 0.00% | 33.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.70 | 0.32 | 0.00% | 36.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.70 | 0.32 | 0.00% | 36.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.53 | 0.41 | 0.00% | 43.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.77 | 0.85 | 0.00% | 33.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 4.20 | 0.00 | 0.00% | 6.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 4.20 | 0.00 | 0.00% | 6.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.50 | 1.26 | 0.00% | 36.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.53 | 0.71 | 0.00% | 43.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 17.90 | 15 | 4.70 | 1.17 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 17.90 | 15 | 4.50 | 1.67 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 3.25 | 1.26 | 33.33% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.75 | 2.00 | 33.33% | 43.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 34.96 | 15 | 2.40 | 0.39 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 34.96 | 15 | 4.03 | 2.05 | 0.00% | 30.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 4.20 | 0.75 | 0.00% | 33.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 4.20 | 0.75 | 0.00% | 33.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
