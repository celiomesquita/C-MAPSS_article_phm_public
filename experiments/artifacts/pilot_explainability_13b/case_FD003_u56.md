# FD003, motor56 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u56.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 171 | 172 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.227, s17:+0.085, s11:+0.083 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 171 | 173 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.227, s17:+0.085, s11:+0.083 |
| 1 | HI_WAIT_SELECTED_D1 | 173 | 174 | preventive_schedule | 0.461 | indefinido | indefinido | s4:+0.244, s17:+0.091, s11:+0.089 |
| 1 | HI_WAIT_SELECTED_D2 | 173 | 175 | preventive_schedule | 0.461 | indefinido | indefinido | s4:+0.244, s17:+0.091, s11:+0.089 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.242 | 19.32 | 19.32 | s4:+0.339, s17:+0.154, s11:+0.120 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.242 | 19.32 | 19.32 | s4:+0.339, s17:+0.154, s11:+0.120 |
| 1 | ISO_LOWER98_M15_D1 | 172 | 173 | preventive_schedule | 0.474 | 37.42 | 14.45 | s4:+0.238, s17:+0.088, s11:+0.087 |
| 1 | ISO_LOWER98_M15_D2 | 171 | 173 | preventive_schedule | 0.491 | 39.47 | 16.51 | s4:+0.227, s17:+0.085, s11:+0.083 |
| 1 | RF_SLOPE_POINT_M15_D1 | 188 | 189 | preventive_schedule | 0.305 | 15.70 | 15.70 | s4:+0.317, s17:+0.141, s11:+0.113 |
| 1 | RF_SLOPE_POINT_M15_D2 | 187 | 189 | preventive_schedule | 0.320 | 16.47 | 16.47 | s4:+0.312, s17:+0.132, s11:+0.110 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 171 | 172 | preventive_schedule | 0.491 | 33.15 | 0.00 | s4:+0.227, s17:+0.085, s11:+0.083 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 171 | 173 | preventive_schedule | 0.491 | 33.15 | 0.00 | s4:+0.227, s17:+0.085, s11:+0.083 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.668 | indefinido | indefinido | s4:+0.145, s17:+0.082, s11:+0.044 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.663 | indefinido | indefinido | s4:+0.158, s17:+0.075, s11:+0.041 |
| 1 | HI_MARKER_D1 | 171 | 172 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.227, s17:+0.085, s11:+0.083 |
| 1 | HI_MARKER_D2 | 171 | 173 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.227, s17:+0.085, s11:+0.083 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 179 | 180 | preventive_schedule/escolha interna inviável | 0.399 | indefinido | indefinido | s8:+0.257, s15:+0.145, s4:+0.092 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 179 | 181 | preventive_schedule/escolha interna inviável | 0.399 | indefinido | indefinido | s8:+0.257, s15:+0.145, s4:+0.092 |
| 2 | HI_WAIT_SELECTED_D1 | 169 | 170 | preventive_schedule/escolha interna inviável | 0.480 | indefinido | indefinido | s8:+0.213, s15:+0.147, s4:+0.074 |
| 2 | HI_WAIT_SELECTED_D2 | 169 | 171 | preventive_schedule/escolha interna inviável | 0.480 | indefinido | indefinido | s8:+0.213, s15:+0.147, s4:+0.074 |
| 2 | ISO_POINT_M15_D1 | 194 | 195 | at_endpoint | 0.218 | 15.52 | 15.52 | s8:+0.365, s15:+0.182, s4:+0.119 |
| 2 | ISO_POINT_M15_D2 | 194 | 196 | late_schedule | 0.218 | 15.52 | 15.52 | s8:+0.365, s15:+0.182, s4:+0.119 |
| 2 | ISO_LOWER98_M15_D1 | 164 | 165 | preventive_schedule | 0.485 | 36.50 | 11.20 | s8:+0.229, s15:+0.140, s4:+0.073 |
| 2 | ISO_LOWER98_M15_D2 | 164 | 166 | preventive_schedule | 0.485 | 36.50 | 11.20 | s8:+0.229, s15:+0.140, s4:+0.073 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.218 | 23.82 | 23.82 | s8:+0.365, s15:+0.182, s4:+0.119 |
| 2 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.218 | 23.82 | 23.82 | s8:+0.365, s15:+0.182, s4:+0.119 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 164 | 165 | preventive_schedule | 0.485 | 42.82 | 8.61 | s8:+0.229, s15:+0.140, s4:+0.073 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 164 | 166 | preventive_schedule | 0.485 | 42.82 | 8.61 | s8:+0.229, s15:+0.140, s4:+0.073 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.651 | indefinido | indefinido | s8:+0.161, s15:+0.079, s4:+0.054 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.666 | indefinido | indefinido | s8:+0.148, s15:+0.080, s4:+0.053 |
| 2 | HI_MARKER_D1 | 164 | 165 | preventive_schedule | 0.485 | indefinido | indefinido | s8:+0.229, s15:+0.140, s4:+0.073 |
| 2 | HI_MARKER_D2 | 164 | 166 | preventive_schedule | 0.485 | indefinido | indefinido | s8:+0.229, s15:+0.140, s4:+0.073 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 175 | 176 | preventive_schedule | 0.287 | indefinido | indefinido | s11:+0.371, s2:+0.094, s21:+0.092 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 175 | 177 | preventive_schedule | 0.287 | indefinido | indefinido | s11:+0.371, s2:+0.094, s21:+0.092 |
| 3 | HI_WAIT_SELECTED_D1 | 173 | 174 | preventive_schedule | 0.320 | indefinido | indefinido | s11:+0.351, s21:+0.092, s2:+0.086 |
| 3 | HI_WAIT_SELECTED_D2 | 173 | 175 | preventive_schedule | 0.320 | indefinido | indefinido | s11:+0.351, s21:+0.092, s2:+0.086 |
| 3 | ISO_POINT_M15_D1 | 183 | 184 | preventive_schedule | 0.222 | 14.88 | 14.88 | s11:+0.416, s2:+0.107, s21:+0.096 |
| 3 | ISO_POINT_M15_D2 | 183 | 185 | preventive_schedule | 0.222 | 14.88 | 14.88 | s11:+0.416, s2:+0.107, s21:+0.096 |
| 3 | ISO_LOWER98_M15_D1 | 163 | 164 | preventive_schedule | 0.496 | 39.58 | 14.00 | s11:+0.254, s21:+0.072, s2:+0.067 |
| 3 | ISO_LOWER98_M15_D2 | 163 | 165 | preventive_schedule | 0.496 | 39.58 | 14.00 | s11:+0.254, s21:+0.072, s2:+0.067 |
| 3 | RF_SLOPE_POINT_M15_D1 | 175 | 176 | preventive_schedule | 0.287 | 15.90 | 15.90 | s11:+0.371, s2:+0.094, s21:+0.092 |
| 3 | RF_SLOPE_POINT_M15_D2 | 175 | 177 | preventive_schedule | 0.287 | 15.90 | 15.90 | s11:+0.371, s2:+0.094, s21:+0.092 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 165 | 166 | preventive_schedule | 0.472 | 46.49 | 15.20 | s11:+0.268, s21:+0.076, s2:+0.070 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 165 | 167 | preventive_schedule | 0.472 | 46.49 | 15.20 | s11:+0.268, s21:+0.076, s2:+0.070 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.606 | indefinido | indefinido | s11:+0.195, s21:+0.059, s2:+0.046 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.601 | indefinido | indefinido | s11:+0.191, s21:+0.066, s3:+0.049 |
| 3 | HI_MARKER_D1 | 163 | 164 | preventive_schedule | 0.496 | indefinido | indefinido | s11:+0.254, s21:+0.072, s2:+0.067 |
| 3 | HI_MARKER_D2 | 163 | 165 | preventive_schedule | 0.496 | indefinido | indefinido | s11:+0.254, s21:+0.072, s2:+0.067 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=171, A=171.
- Repetição2: G=164, A=164.
- Repetição3: G=163, A=163.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.44 | 1.12 | 0.00% | 21.88% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.44 | 1.12 | 0.00% | 21.88% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.44 | 0.92 | 0.00% | 21.88% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.44 | 0.92 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.12% | 0.00% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 12.50% | 6.25% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 22.97 | 15 | 2.31 | 0.70 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 22.97 | 15 | 2.44 | 1.12 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.22 | 0.16 | 28.12% | 40.62% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.12 | 0.16 | 21.88% | 40.62% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.25 | 15 | 2.06 | 1.12 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.25 | 15 | 2.06 | 1.12 | 0.00% | 21.88% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.44 | 1.12 | 0.00% | 21.88% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.44 | 1.12 | 0.00% | 21.88% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.57 | 1.05 | 0.00% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.57 | 1.05 | 0.00% | 36.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.00 | 0.39 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.00 | 0.39 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.75 | 0.18 | 33.33% | 26.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.71 | 0.22 | 30.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 25.30 | 15 | 2.00 | 0.48 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 25.30 | 15 | 2.00 | 0.48 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 3.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 6.67% | 3.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 34.21 | 15 | 1.73 | 0.48 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 34.21 | 15 | 1.73 | 0.48 | 0.00% | 10.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.00 | 0.48 | 0.00% | 10.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.00 | 0.48 | 0.00% | 10.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.80 | 0.35 | 0.00% | 13.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.80 | 0.35 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.43 | 0.00 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.43 | 0.00 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.86 | 0.58 | 3.33% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.83 | 0.58 | 3.33% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.58 | 15 | 2.43 | 0.48 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.58 | 15 | 2.43 | 0.48 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.60 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.40 | 0.25 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 31.29 | 15 | 1.70 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 31.29 | 15 | 1.80 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.43 | 0.48 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.43 | 0.48 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
