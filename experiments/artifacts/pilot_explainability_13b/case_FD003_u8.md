# FD003, motor8 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u8.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 260 | 261 | preventive_schedule | 0.287 | indefinido | indefinido | s11:+0.248, s4:+0.245, s20:+0.055 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 260 | 262 | preventive_schedule | 0.287 | indefinido | indefinido | s11:+0.248, s4:+0.245, s20:+0.055 |
| 1 | HI_WAIT_SELECTED_D1 | 239 | 240 | preventive_schedule | 0.439 | indefinido | indefinido | s4:+0.206, s11:+0.202, s17:+0.039 |
| 1 | HI_WAIT_SELECTED_D2 | 239 | 241 | preventive_schedule | 0.439 | indefinido | indefinido | s4:+0.206, s11:+0.202, s17:+0.039 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.209 | 16.28 | 16.28 | s4:+0.281, s11:+0.278, s20:+0.057 |
| 1 | ISO_POINT_M15_D2 | 266 | 268 | late_schedule | 0.209 | 16.28 | 16.28 | s4:+0.281, s11:+0.278, s20:+0.057 |
| 1 | ISO_LOWER98_M15_D1 | 229 | 230 | preventive_schedule | 0.488 | 36.82 | 12.33 | s4:+0.201, s11:+0.178, s13:+0.034 |
| 1 | ISO_LOWER98_M15_D2 | 229 | 231 | preventive_schedule | 0.488 | 36.82 | 12.33 | s4:+0.201, s11:+0.178, s13:+0.034 |
| 1 | RF_SLOPE_POINT_M15_D1 | 265 | 266 | preventive_schedule | 0.234 | 15.42 | 15.42 | s11:+0.276, s4:+0.261, s20:+0.060 |
| 1 | RF_SLOPE_POINT_M15_D2 | 265 | 267 | at_endpoint | 0.234 | 15.42 | 15.42 | s11:+0.276, s4:+0.261, s20:+0.060 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 229 | 230 | preventive_schedule | 0.488 | 33.07 | 6.81 | s4:+0.201, s11:+0.178, s13:+0.034 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 229 | 231 | preventive_schedule | 0.488 | 33.07 | 6.81 | s4:+0.201, s11:+0.178, s13:+0.034 |
| 1 | AGE_D1 | 150 | 151 | preventive_schedule | 0.836 | indefinido | indefinido | s11:+0.080, s4:+0.040, s13:+0.015 |
| 1 | AGE_D2 | 149 | 151 | preventive_schedule | 0.823 | indefinido | indefinido | s11:+0.090, s4:+0.042, s13:+0.016 |
| 1 | HI_MARKER_D1 | 229 | 230 | preventive_schedule | 0.488 | indefinido | indefinido | s4:+0.201, s11:+0.178, s13:+0.034 |
| 1 | HI_MARKER_D2 | 229 | 231 | preventive_schedule | 0.488 | indefinido | indefinido | s4:+0.201, s11:+0.178, s13:+0.034 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 261 | 262 | preventive_schedule | 0.293 | indefinido | indefinido | s11:+0.247, s4:+0.244, s15:+0.089 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 246 | 248 | preventive_schedule | 0.395 | indefinido | indefinido | s11:+0.227, s4:+0.212, s15:+0.070 |
| 2 | HI_WAIT_SELECTED_D1 | 239 | 240 | preventive_schedule | 0.449 | indefinido | indefinido | s4:+0.205, s11:+0.197, s15:+0.058 |
| 2 | HI_WAIT_SELECTED_D2 | 239 | 241 | preventive_schedule | 0.449 | indefinido | indefinido | s4:+0.205, s11:+0.197, s15:+0.058 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.221 | 17.85 | 17.85 | s4:+0.279, s11:+0.272, s15:+0.092 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.221 | 17.85 | 17.85 | s4:+0.279, s11:+0.272, s15:+0.092 |
| 2 | ISO_LOWER98_M15_D1 | 229 | 230 | preventive_schedule | 0.498 | 37.90 | 14.00 | s4:+0.200, s11:+0.174, s15:+0.053 |
| 2 | ISO_LOWER98_M15_D2 | 229 | 231 | preventive_schedule | 0.498 | 37.90 | 14.00 | s4:+0.200, s11:+0.174, s15:+0.053 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.221 | 25.21 | 25.21 | s4:+0.279, s11:+0.272, s15:+0.092 |
| 2 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.221 | 25.21 | 25.21 | s4:+0.279, s11:+0.272, s15:+0.092 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 229 | 230 | preventive_schedule | 0.498 | 28.88 | 0.00 | s4:+0.200, s11:+0.174, s15:+0.053 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 229 | 231 | preventive_schedule | 0.498 | 28.88 | 0.00 | s4:+0.200, s11:+0.174, s15:+0.053 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.827 | indefinido | indefinido | s11:+0.089, s4:+0.041, s15:+0.018 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.839 | indefinido | indefinido | s11:+0.080, s4:+0.040, s15:+0.016 |
| 2 | HI_MARKER_D1 | 229 | 230 | preventive_schedule | 0.498 | indefinido | indefinido | s4:+0.200, s11:+0.174, s15:+0.053 |
| 2 | HI_MARKER_D2 | 229 | 231 | preventive_schedule | 0.498 | indefinido | indefinido | s4:+0.200, s11:+0.174, s15:+0.053 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 260 | 261 | preventive_schedule | 0.382 | indefinido | indefinido | s4:+0.292, s11:+0.210, s2:+0.116 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 260 | 262 | preventive_schedule | 0.382 | indefinido | indefinido | s4:+0.292, s11:+0.210, s2:+0.116 |
| 3 | HI_WAIT_SELECTED_D1 | 245 | 246 | preventive_schedule | 0.475 | indefinido | indefinido | s4:+0.243, s11:+0.191, s2:+0.091 |
| 3 | HI_WAIT_SELECTED_D2 | 245 | 247 | preventive_schedule | 0.475 | indefinido | indefinido | s4:+0.243, s11:+0.191, s2:+0.091 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.287 | 20.07 | 20.07 | s4:+0.335, s11:+0.236, s2:+0.142 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.287 | 20.07 | 20.07 | s4:+0.335, s11:+0.236, s2:+0.142 |
| 3 | ISO_LOWER98_M15_D1 | 235 | 236 | preventive_schedule | 0.499 | 38.27 | 9.38 | s4:+0.261, s11:+0.157, s2:+0.083 |
| 3 | ISO_LOWER98_M15_D2 | 235 | 237 | preventive_schedule | 0.499 | 38.27 | 9.38 | s4:+0.261, s11:+0.157, s2:+0.083 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.287 | 28.08 | 28.08 | s4:+0.335, s11:+0.236, s2:+0.142 |
| 3 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.287 | 28.08 | 28.08 | s4:+0.335, s11:+0.236, s2:+0.142 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 235 | 236 | preventive_schedule | 0.499 | 35.49 | 0.55 | s4:+0.261, s11:+0.157, s2:+0.083 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 235 | 237 | preventive_schedule | 0.499 | 35.49 | 0.55 | s4:+0.261, s11:+0.157, s2:+0.083 |
| 3 | AGE_D1 | 151 | 152 | preventive_schedule | 0.884 | indefinido | indefinido | s11:+0.074, s4:+0.047, s2:-0.005 |
| 3 | AGE_D2 | 150 | 152 | preventive_schedule | 0.878 | indefinido | indefinido | s11:+0.067, s4:+0.047, s2:+0.007 |
| 3 | HI_MARKER_D1 | 235 | 236 | preventive_schedule | 0.499 | indefinido | indefinido | s4:+0.261, s11:+0.157, s2:+0.083 |
| 3 | HI_MARKER_D2 | 235 | 237 | preventive_schedule | 0.499 | indefinido | indefinido | s4:+0.261, s11:+0.157, s2:+0.083 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=229, A=229.
- Repetição2: G=229, A=229.
- Repetição3: G=235, A=235.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.48 | 0.88 | 3.12% | 18.75% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.48 | 0.88 | 3.12% | 18.75% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 3.22 | 0.27 | 0.00% | 6.25% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 3.22 | 0.27 | 0.00% | 6.25% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 15.62% | 12.50% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.15 | 0.35 | 18.75% | 18.75% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 24.49 | 15 | 3.22 | 0.69 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 24.49 | 15 | 3.22 | 0.69 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.54 | 0.69 | 12.50% | 18.75% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.64 | 0.78 | 12.50% | 15.62% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 26.26 | 15 | 3.12 | 0.69 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 26.26 | 15 | 3.03 | 0.69 | 0.00% | 18.75% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 3.22 | 0.69 | 0.00% | 18.75% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 3.22 | 0.69 | 0.00% | 18.75% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.40 | 0.21 | 6.25% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.94 | 0.54 | 0.00% | 18.75% | 0/32 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.69 | 0.04 | 0.00% | 12.50% | 0/32 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.69 | 0.04 | 0.00% | 12.50% | 0/32 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/32 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 12.50% | 6.25% | 0/32 |
| 2 | ISO_LOWER98_M15_D1 | 23.90 | 15 | 2.69 | 0.31 | 0.00% | 18.75% | 0/32 |
| 2 | ISO_LOWER98_M15_D2 | 23.90 | 15 | 2.69 | 0.31 | 0.00% | 18.75% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 35.54 | 15 | 3.59 | 0.31 | 0.00% | 18.75% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 35.54 | 15 | 3.53 | 0.31 | 0.00% | 18.75% | 0/32 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.69 | 0.31 | 0.00% | 18.75% | 0/32 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.69 | 0.31 | 0.00% | 18.75% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.32 | 0.45 | 3.12% | 9.38% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.32 | 0.45 | 3.12% | 9.38% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.32 | 0.03 | 3.12% | 9.38% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.32 | 0.03 | 3.12% | 9.38% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 9.38% | 3.12% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 9.38% | 3.12% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 28.89 | 15 | 3.03 | 0.34 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 28.89 | 15 | 3.03 | 0.34 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 3.12% | 3.12% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 34.95 | 15 | 3.03 | 0.34 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 34.95 | 15 | 3.03 | 0.34 | 0.00% | 9.38% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 3.03 | 0.34 | 0.00% | 9.38% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 3.03 | 0.34 | 0.00% | 9.38% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
