# FD003, motor59 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u59.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 269 | 270 | preventive_schedule | 0.300 | indefinido | indefinido | s4:+0.218, s11:+0.202, s2:+0.140 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 269 | 271 | preventive_schedule | 0.300 | indefinido | indefinido | s4:+0.218, s11:+0.202, s2:+0.140 |
| 1 | HI_WAIT_SELECTED_D1 | 263 | 264 | preventive_schedule | 0.354 | indefinido | indefinido | s4:+0.199, s11:+0.186, s2:+0.136 |
| 1 | HI_WAIT_SELECTED_D2 | 263 | 265 | preventive_schedule | 0.354 | indefinido | indefinido | s4:+0.199, s11:+0.186, s2:+0.136 |
| 1 | ISO_POINT_M15_D1 | 291 | 292 | preventive_schedule | 0.045 | 15.49 | 15.49 | s11:+0.285, s4:+0.279, s2:+0.184 |
| 1 | ISO_POINT_M15_D2 | 289 | 291 | preventive_schedule | 0.098 | 16.74 | 16.74 | s11:+0.282, s4:+0.253, s2:+0.169 |
| 1 | ISO_LOWER98_M15_D1 | 257 | 258 | preventive_schedule | 0.436 | 38.54 | 12.63 | s4:+0.167, s11:+0.159, s2:+0.133 |
| 1 | ISO_LOWER98_M15_D2 | 255 | 257 | preventive_schedule | 0.459 | 42.46 | 16.55 | s4:+0.161, s11:+0.158, s2:+0.124 |
| 1 | RF_SLOPE_POINT_M15_D1 | 290 | 291 | preventive_schedule | 0.082 | 14.54 | 14.54 | s11:+0.283, s4:+0.261, s2:+0.172 |
| 1 | RF_SLOPE_POINT_M15_D2 | 263 | 265 | preventive_schedule | 0.354 | 16.96 | 16.96 | s4:+0.199, s11:+0.186, s2:+0.136 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 254 | 255 | preventive_schedule | 0.476 | 42.16 | 12.60 | s4:+0.156, s11:+0.148, s2:+0.124 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 253 | 255 | preventive_schedule | 0.492 | 46.00 | 16.44 | s4:+0.147, s11:+0.143, s2:+0.128 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.967 | indefinido | indefinido | s11:+0.033, s15:-0.029, s8:+0.013 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.962 | indefinido | indefinido | s11:+0.030, s15:-0.029, s2:+0.019 |
| 1 | HI_MARKER_D1 | 253 | 254 | preventive_schedule | 0.492 | indefinido | indefinido | s4:+0.147, s11:+0.143, s2:+0.128 |
| 1 | HI_MARKER_D2 | 253 | 255 | preventive_schedule | 0.492 | indefinido | indefinido | s4:+0.147, s11:+0.143, s2:+0.128 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 266 | 267 | preventive_schedule | 0.390 | indefinido | indefinido | s8:+0.551, s15:-0.298, s11:+0.148 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 266 | 268 | preventive_schedule | 0.390 | indefinido | indefinido | s8:+0.551, s15:-0.298, s11:+0.148 |
| 2 | HI_WAIT_SELECTED_D1 | 268 | 269 | preventive_schedule | 0.369 | indefinido | indefinido | s8:+0.562, s15:-0.300, s11:+0.151 |
| 2 | HI_WAIT_SELECTED_D2 | 268 | 270 | preventive_schedule | 0.369 | indefinido | indefinido | s8:+0.562, s15:-0.300, s11:+0.151 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.000 | 16.02 | 16.02 | s8:+0.884, s15:-0.436, s14:+0.241 |
| 2 | ISO_POINT_M15_D2 | 297 | 299 | at_endpoint | 0.000 | 16.02 | 16.02 | s8:+0.867, s15:-0.428, s14:+0.238 |
| 2 | ISO_LOWER98_M15_D1 | 258 | 259 | preventive_schedule | 0.499 | 87.77 | 13.72 | s8:+0.445, s15:-0.257, s14:+0.130 |
| 2 | ISO_LOWER98_M15_D2 | 258 | 260 | preventive_schedule | 0.499 | 87.77 | 13.72 | s8:+0.445, s15:-0.257, s14:+0.130 |
| 2 | RF_SLOPE_POINT_M15_D1 | 291 | 292 | preventive_schedule | 0.077 | 15.50 | 15.50 | s8:+0.797, s15:-0.394, s11:+0.217 |
| 2 | RF_SLOPE_POINT_M15_D2 | 291 | 293 | preventive_schedule | 0.077 | 15.50 | 15.50 | s8:+0.797, s15:-0.394, s11:+0.217 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 258 | 259 | preventive_schedule | 0.499 | 54.23 | 0.00 | s8:+0.445, s15:-0.257, s14:+0.130 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 258 | 260 | preventive_schedule | 0.499 | 54.23 | 0.00 | s8:+0.445, s15:-0.257, s14:+0.130 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.969 | indefinido | indefinido | s15:-0.082, s8:+0.059, s11:+0.025 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.970 | indefinido | indefinido | s15:-0.081, s8:+0.060, s11:+0.023 |
| 2 | HI_MARKER_D1 | 258 | 259 | preventive_schedule | 0.499 | indefinido | indefinido | s8:+0.445, s15:-0.257, s14:+0.130 |
| 2 | HI_MARKER_D2 | 258 | 260 | preventive_schedule | 0.499 | indefinido | indefinido | s8:+0.445, s15:-0.257, s14:+0.130 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 262 | 263 | preventive_schedule | 0.399 | indefinido | indefinido | s4:+0.260, s11:+0.222, s2:+0.119 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 262 | 264 | preventive_schedule | 0.399 | indefinido | indefinido | s4:+0.260, s11:+0.222, s2:+0.119 |
| 3 | HI_WAIT_SELECTED_D1 | 265 | 266 | preventive_schedule | 0.375 | indefinido | indefinido | s4:+0.272, s11:+0.226, s2:+0.127 |
| 3 | HI_WAIT_SELECTED_D2 | 265 | 267 | preventive_schedule | 0.375 | indefinido | indefinido | s4:+0.272, s11:+0.226, s2:+0.127 |
| 3 | ISO_POINT_M15_D1 | 284 | 285 | preventive_schedule | 0.230 | 15.67 | 15.67 | s4:+0.334, s11:+0.300, s2:+0.136 |
| 3 | ISO_POINT_M15_D2 | 284 | 286 | preventive_schedule | 0.230 | 15.67 | 15.67 | s4:+0.334, s11:+0.300, s2:+0.136 |
| 3 | ISO_LOWER98_M15_D1 | 255 | 256 | preventive_schedule | 0.484 | 38.27 | 9.38 | s4:+0.214, s11:+0.188, s2:+0.113 |
| 3 | ISO_LOWER98_M15_D2 | 255 | 257 | preventive_schedule | 0.484 | 38.27 | 9.38 | s4:+0.214, s11:+0.188, s2:+0.113 |
| 3 | RF_SLOPE_POINT_M15_D1 | 291 | 292 | preventive_schedule | 0.122 | 13.56 | 13.56 | s4:+0.370, s11:+0.339, s2:+0.168 |
| 3 | RF_SLOPE_POINT_M15_D2 | 290 | 292 | preventive_schedule | 0.160 | 16.28 | 16.28 | s4:+0.347, s11:+0.336, s2:+0.157 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 255 | 256 | preventive_schedule | 0.484 | 36.52 | 1.57 | s4:+0.214, s11:+0.188, s2:+0.113 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 255 | 257 | preventive_schedule | 0.484 | 36.52 | 1.57 | s4:+0.214, s11:+0.188, s2:+0.113 |
| 3 | AGE_D1 | 151 | 152 | preventive_schedule | 0.945 | indefinido | indefinido | s11:+0.038, s2:+0.018, s4:-0.001 |
| 3 | AGE_D2 | 150 | 152 | preventive_schedule | 0.943 | indefinido | indefinido | s11:+0.032, s2:+0.026, s4:-0.001 |
| 3 | HI_MARKER_D1 | 255 | 256 | preventive_schedule | 0.484 | indefinido | indefinido | s4:+0.214, s11:+0.188, s2:+0.113 |
| 3 | HI_MARKER_D2 | 255 | 257 | preventive_schedule | 0.484 | indefinido | indefinido | s4:+0.214, s11:+0.188, s2:+0.113 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=253, A=253.
- Repetição2: G=258, A=258.
- Repetição3: G=255, A=255.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.77 | 0.75 | 0.00% | 33.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.77 | 0.75 | 0.00% | 33.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.10 | 0.22 | 0.00% | 10.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.10 | 0.22 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.07 | 0.21 | 0.00% | 20.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.53 | 0.74 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 25.91 | 15 | 1.60 | 0.52 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 25.91 | 15 | 1.80 | 0.39 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.93 | 0.92 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 11.40 | 0.36 | 0.00% | 53.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 29.56 | 15 | 1.70 | 0.77 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 29.56 | 15 | 1.80 | 1.00 | 0.00% | 43.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.10 | 0.91 | 0.00% | 23.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.10 | 0.91 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.57 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.57 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.37 | 0.08 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.37 | 0.08 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.81 | 0.40 | 13.33% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 74.05 | 15 | 1.40 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 74.05 | 15 | 1.40 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.50 | 0.92 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.53 | 0.88 | 0.00% | 13.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 136.85 | 15 | 1.37 | 0.33 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 136.85 | 15 | 1.37 | 0.33 | 0.00% | 20.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.37 | 0.33 | 0.00% | 20.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.37 | 0.33 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.72 | 0.34 | 0.00% | 9.38% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.72 | 0.34 | 0.00% | 9.38% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.44 | 0.10 | 0.00% | 3.12% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.44 | 0.10 | 0.00% | 3.12% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.72 | 0.34 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.72 | 0.34 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 28.89 | 15 | 1.44 | 0.45 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 28.89 | 15 | 1.44 | 0.45 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.97 | 0.31 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.19 | 0.41 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 34.95 | 15 | 1.44 | 0.45 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 34.95 | 15 | 1.44 | 0.45 | 0.00% | 9.38% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.44 | 0.45 | 0.00% | 9.38% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.44 | 0.45 | 0.00% | 9.38% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
