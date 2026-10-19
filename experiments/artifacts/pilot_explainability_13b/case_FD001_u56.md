# FD001, motor56 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u56.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 258 | 259 | preventive_schedule | 0.295 | indefinido | indefinido | s9:+0.103, s2:+0.098, s21:+0.081 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 248 | 250 | preventive_schedule | 0.391 | indefinido | indefinido | s9:+0.087, s2:+0.083, s21:+0.068 |
| 1 | HI_WAIT_SELECTED_D1 | 243 | 244 | preventive_schedule | 0.415 | indefinido | indefinido | s9:+0.082, s2:+0.074, s21:+0.065 |
| 1 | HI_WAIT_SELECTED_D2 | 243 | 245 | preventive_schedule | 0.415 | indefinido | indefinido | s9:+0.082, s2:+0.074, s21:+0.065 |
| 1 | ISO_POINT_M15_D1 | 268 | 269 | preventive_schedule | 0.180 | 15.33 | 15.33 | s9:+0.122, s2:+0.103, s21:+0.091 |
| 1 | ISO_POINT_M15_D2 | 268 | 270 | preventive_schedule | 0.180 | 15.33 | 15.33 | s9:+0.122, s2:+0.103, s21:+0.091 |
| 1 | ISO_LOWER98_M15_D1 | 236 | 237 | preventive_schedule | 0.469 | 35.56 | 14.00 | s2:+0.075, s9:+0.072, s21:+0.062 |
| 1 | ISO_LOWER98_M15_D2 | 233 | 235 | preventive_schedule | 0.495 | 37.65 | 16.09 | s2:+0.069, s9:+0.069, s21:+0.062 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.106 | 28.10 | 28.10 | s9:+0.139, s2:+0.106, s12:+0.096 |
| 1 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.106 | 28.10 | 28.10 | s9:+0.139, s2:+0.106, s12:+0.096 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 233 | 234 | preventive_schedule | 0.495 | 33.85 | 0.00 | s2:+0.069, s9:+0.069, s21:+0.062 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 233 | 235 | preventive_schedule | 0.495 | 33.85 | 0.00 | s2:+0.069, s9:+0.069, s21:+0.062 |
| 1 | AGE_D1 | 133 | 134 | preventive_schedule | 0.936 | indefinido | indefinido | s8:+0.018, s20:+0.015, s9:+0.014 |
| 1 | AGE_D2 | 132 | 134 | preventive_schedule | 0.942 | indefinido | indefinido | s8:+0.014, s9:+0.014, s20:+0.013 |
| 1 | HI_MARKER_D1 | 233 | 234 | preventive_schedule | 0.495 | indefinido | indefinido | s2:+0.069, s9:+0.069, s21:+0.062 |
| 1 | HI_MARKER_D2 | 233 | 235 | preventive_schedule | 0.495 | indefinido | indefinido | s2:+0.069, s9:+0.069, s21:+0.062 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 254 | 255 | preventive_schedule | 0.299 | indefinido | indefinido | s20:+0.132, s9:+0.120, s15:+0.107 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 254 | 256 | preventive_schedule | 0.299 | indefinido | indefinido | s20:+0.132, s9:+0.120, s15:+0.107 |
| 2 | HI_WAIT_SELECTED_D1 | 241 | 242 | preventive_schedule | 0.386 | indefinido | indefinido | s20:+0.118, s9:+0.096, s15:+0.090 |
| 2 | HI_WAIT_SELECTED_D2 | 241 | 243 | preventive_schedule | 0.386 | indefinido | indefinido | s20:+0.118, s9:+0.096, s15:+0.090 |
| 2 | ISO_POINT_M15_D1 | 257 | 258 | preventive_schedule | 0.263 | 15.84 | 15.84 | s20:+0.136, s9:+0.125, s15:+0.107 |
| 2 | ISO_POINT_M15_D2 | 257 | 259 | preventive_schedule | 0.263 | 15.84 | 15.84 | s20:+0.136, s9:+0.125, s15:+0.107 |
| 2 | ISO_LOWER98_M15_D1 | 233 | 234 | preventive_schedule | 0.460 | 28.27 | 15.42 | s20:+0.107, s9:+0.085, s15:+0.079 |
| 2 | ISO_LOWER98_M15_D2 | 233 | 235 | preventive_schedule | 0.460 | 28.27 | 15.42 | s20:+0.107, s9:+0.085, s15:+0.079 |
| 2 | RF_SLOPE_POINT_M15_D1 | 271 | 272 | preventive_schedule | 0.071 | 15.86 | 15.86 | s20:+0.176, s9:+0.160, s15:+0.131 |
| 2 | RF_SLOPE_POINT_M15_D2 | 271 | 273 | preventive_schedule | 0.071 | 15.86 | 15.86 | s20:+0.176, s9:+0.160, s15:+0.131 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 231 | 232 | preventive_schedule | 0.494 | 24.71 | 1.70 | s20:+0.089, s9:+0.082, s15:+0.081 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 231 | 233 | preventive_schedule | 0.494 | 24.71 | 1.70 | s20:+0.089, s9:+0.082, s15:+0.081 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.929 | indefinido | indefinido | s20:+0.024, s15:+0.017, s9:+0.017 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.937 | indefinido | indefinido | s20:+0.025, s15:+0.017, s9:+0.015 |
| 2 | HI_MARKER_D1 | 231 | 232 | preventive_schedule | 0.494 | indefinido | indefinido | s20:+0.089, s9:+0.082, s15:+0.081 |
| 2 | HI_MARKER_D2 | 231 | 233 | preventive_schedule | 0.494 | indefinido | indefinido | s20:+0.089, s9:+0.082, s15:+0.081 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 236 | 237 | preventive_schedule | 0.398 | indefinido | indefinido | s20:+0.113, s9:+0.109, s4:+0.086 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 236 | 238 | preventive_schedule | 0.398 | indefinido | indefinido | s20:+0.113, s9:+0.109, s4:+0.086 |
| 3 | HI_WAIT_SELECTED_D1 | 237 | 238 | preventive_schedule | 0.392 | indefinido | indefinido | s20:+0.117, s9:+0.111, s4:+0.086 |
| 3 | HI_WAIT_SELECTED_D2 | 232 | 234 | preventive_schedule | 0.448 | indefinido | indefinido | s9:+0.103, s20:+0.101, s21:+0.077 |
| 3 | ISO_POINT_M15_D1 | 261 | 262 | preventive_schedule | 0.160 | 13.41 | 13.41 | s9:+0.163, s20:+0.147, s4:+0.116 |
| 3 | ISO_POINT_M15_D2 | 261 | 263 | preventive_schedule | 0.160 | 13.41 | 13.41 | s9:+0.163, s20:+0.147, s4:+0.116 |
| 3 | ISO_LOWER98_M15_D1 | 233 | 234 | preventive_schedule | 0.423 | 32.78 | 14.86 | s20:+0.110, s9:+0.104, s21:+0.079 |
| 3 | ISO_LOWER98_M15_D2 | 233 | 235 | preventive_schedule | 0.423 | 32.78 | 14.86 | s20:+0.110, s9:+0.104, s21:+0.079 |
| 3 | RF_SLOPE_POINT_M15_D1 | 264 | 265 | preventive_schedule | 0.115 | 8.42 | 8.42 | s9:+0.173, s20:+0.164, s4:+0.124 |
| 3 | RF_SLOPE_POINT_M15_D2 | 264 | 266 | preventive_schedule | 0.115 | 8.42 | 8.42 | s9:+0.173, s20:+0.164, s4:+0.124 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 227 | 228 | preventive_schedule | 0.494 | 35.86 | 9.66 | s20:+0.099, s9:+0.094, s21:+0.067 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 227 | 229 | preventive_schedule | 0.494 | 35.86 | 9.66 | s20:+0.099, s9:+0.094, s21:+0.067 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.922 | indefinido | indefinido | s20:+0.024, s9:+0.020, s4:+0.013 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.936 | indefinido | indefinido | s20:+0.026, s9:+0.018, s15:+0.011 |
| 3 | HI_MARKER_D1 | 227 | 228 | preventive_schedule | 0.494 | indefinido | indefinido | s20:+0.099, s9:+0.094, s21:+0.067 |
| 3 | HI_MARKER_D2 | 227 | 229 | preventive_schedule | 0.494 | indefinido | indefinido | s20:+0.099, s9:+0.094, s21:+0.067 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=233, A=233.
- Repetição2: G=231, A=231.
- Repetição3: G=227, A=227.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.07 | 1.00 | 0.00% | 36.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 3.47 | 1.90 | 0.00% | 30.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.07 | 0.00 | 0.00% | 16.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.07 | 0.00 | 0.00% | 16.67% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.60 | 0.05 | 0.00% | 30.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.57 | 0.05 | 0.00% | 30.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 21.56 | 15 | 2.53 | 1.05 | 0.00% | 30.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 21.56 | 15 | 2.07 | 0.47 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 46.26 | 15 | 2.07 | 0.47 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 46.26 | 15 | 2.07 | 0.47 | 0.00% | 36.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.07 | 0.47 | 0.00% | 36.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.07 | 0.47 | 0.00% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.83 | 1.06 | 0.00% | 40.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.83 | 1.06 | 0.00% | 40.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.50 | 0.30 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.50 | 0.30 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.43 | 0.82 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.43 | 0.82 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 12.84 | 15 | 2.10 | 0.59 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 12.84 | 15 | 2.10 | 0.59 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.47 | 0.83 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.10 | 1.33 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 23.01 | 15 | 2.50 | 1.25 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 23.01 | 15 | 2.50 | 1.25 | 0.00% | 33.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.50 | 1.40 | 0.00% | 33.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.50 | 1.40 | 0.00% | 33.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.47 | 0.94 | 0.00% | 40.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.47 | 0.94 | 0.00% | 40.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.37 | 0.27 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.37 | 0.52 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.60 | 0.54 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.60 | 0.54 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 17.91 | 15 | 1.77 | 0.56 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 17.91 | 15 | 1.77 | 0.56 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.37 | 0.74 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.47 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 26.21 | 15 | 2.10 | 0.90 | 0.00% | 33.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 26.21 | 15 | 2.10 | 0.90 | 0.00% | 33.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.37 | 0.90 | 0.00% | 33.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.37 | 0.90 | 0.00% | 33.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
