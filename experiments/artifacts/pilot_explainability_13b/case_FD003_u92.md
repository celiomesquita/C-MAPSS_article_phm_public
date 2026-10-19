# FD003, motor92 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u92.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 147 | 148 | preventive_schedule | 0.287 | indefinido | indefinido | s11:+0.520, s15:+0.074, s2:+0.037 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 139 | 141 | preventive_schedule | 0.390 | indefinido | indefinido | s11:+0.448, s15:+0.064, s8:+0.033 |
| 1 | HI_WAIT_SELECTED_D1 | 143 | 144 | preventive_schedule | 0.341 | indefinido | indefinido | s11:+0.485, s15:+0.070, s8:+0.036 |
| 1 | HI_WAIT_SELECTED_D2 | 143 | 145 | preventive_schedule | 0.341 | indefinido | indefinido | s11:+0.485, s15:+0.070, s8:+0.036 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.173 | 19.01 | 19.01 | s11:+0.593, s15:+0.082, s2:+0.055 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.173 | 19.01 | 19.01 | s11:+0.593, s15:+0.082, s2:+0.055 |
| 1 | ISO_LOWER98_M15_D1 | 133 | 134 | preventive_schedule | 0.497 | 44.16 | 11.00 | s11:+0.374, s15:+0.051, s8:+0.028 |
| 1 | ISO_LOWER98_M15_D2 | 133 | 135 | preventive_schedule | 0.497 | 44.16 | 11.00 | s11:+0.374, s15:+0.051, s8:+0.028 |
| 1 | RF_SLOPE_POINT_M15_D1 | 144 | 145 | preventive_schedule | 0.335 | 15.92 | 15.92 | s11:+0.484, s15:+0.072, s8:+0.036 |
| 1 | RF_SLOPE_POINT_M15_D2 | 142 | 144 | preventive_schedule | 0.334 | 16.05 | 16.05 | s11:+0.495, s15:+0.068, s8:+0.037 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 133 | 134 | preventive_schedule | 0.497 | 44.55 | 10.46 | s11:+0.374, s15:+0.051, s8:+0.028 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 133 | 135 | preventive_schedule | 0.497 | 44.55 | 10.46 | s11:+0.374, s15:+0.051, s8:+0.028 |
| 1 | AGE_D1 | 145 | 146 | preventive_schedule | 0.327 | indefinido | indefinido | s11:+0.491, s15:+0.073, s8:+0.036 |
| 1 | AGE_D2 | 144 | 146 | preventive_schedule | 0.335 | indefinido | indefinido | s11:+0.484, s15:+0.072, s8:+0.036 |
| 1 | HI_MARKER_D1 | 133 | 134 | preventive_schedule | 0.497 | indefinido | indefinido | s11:+0.374, s15:+0.051, s8:+0.028 |
| 1 | HI_MARKER_D2 | 133 | 135 | preventive_schedule | 0.497 | indefinido | indefinido | s11:+0.374, s15:+0.051, s8:+0.028 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 154 | 155 | preventive_schedule | 0.290 | indefinido | indefinido | s4:+0.359, s11:+0.139, s2:+0.097 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 154 | 156 | preventive_schedule | 0.290 | indefinido | indefinido | s4:+0.359, s11:+0.139, s2:+0.097 |
| 2 | HI_WAIT_SELECTED_D1 | 143 | 144 | preventive_schedule | 0.432 | indefinido | indefinido | s4:+0.296, s11:+0.117, s2:+0.062 |
| 2 | HI_WAIT_SELECTED_D2 | 143 | 145 | preventive_schedule | 0.432 | indefinido | indefinido | s4:+0.296, s11:+0.117, s2:+0.062 |
| 2 | ISO_POINT_M15_D1 | 155 | 156 | preventive_schedule | 0.272 | 15.84 | 15.84 | s4:+0.366, s11:+0.140, s2:+0.103 |
| 2 | ISO_POINT_M15_D2 | 154 | 156 | preventive_schedule | 0.290 | 16.73 | 16.73 | s4:+0.359, s11:+0.139, s2:+0.097 |
| 2 | ISO_LOWER98_M15_D1 | 138 | 139 | preventive_schedule | 0.490 | 34.68 | 11.48 | s4:+0.272, s11:+0.101, s2:+0.050 |
| 2 | ISO_LOWER98_M15_D2 | 138 | 140 | preventive_schedule | 0.490 | 34.68 | 11.48 | s4:+0.272, s11:+0.101, s2:+0.050 |
| 2 | RF_SLOPE_POINT_M15_D1 | 149 | 150 | preventive_schedule | 0.357 | 15.73 | 15.73 | s4:+0.327, s11:+0.131, s2:+0.080 |
| 2 | RF_SLOPE_POINT_M15_D2 | 149 | 151 | preventive_schedule | 0.357 | 15.73 | 15.73 | s4:+0.327, s11:+0.131, s2:+0.080 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 138 | 139 | preventive_schedule | 0.490 | 27.28 | 0.00 | s4:+0.272, s11:+0.101, s2:+0.050 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 138 | 140 | preventive_schedule | 0.490 | 27.28 | 0.00 | s4:+0.272, s11:+0.101, s2:+0.050 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.412 | indefinido | indefinido | s4:+0.308, s11:+0.119, s2:+0.062 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.415 | indefinido | indefinido | s4:+0.305, s11:+0.117, s2:+0.069 |
| 2 | HI_MARKER_D1 | 138 | 139 | preventive_schedule | 0.490 | indefinido | indefinido | s4:+0.272, s11:+0.101, s2:+0.050 |
| 2 | HI_MARKER_D2 | 138 | 140 | preventive_schedule | 0.490 | indefinido | indefinido | s4:+0.272, s11:+0.101, s2:+0.050 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 149 | 150 | preventive_schedule | 0.296 | indefinido | indefinido | s11:+0.360, s4:+0.163, s8:+0.057 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 149 | 151 | preventive_schedule | 0.296 | indefinido | indefinido | s11:+0.360, s4:+0.163, s8:+0.057 |
| 3 | HI_WAIT_SELECTED_D1 | 144 | 145 | preventive_schedule | 0.360 | indefinido | indefinido | s11:+0.322, s4:+0.152, s8:+0.054 |
| 3 | HI_WAIT_SELECTED_D2 | 144 | 146 | preventive_schedule | 0.360 | indefinido | indefinido | s11:+0.322, s4:+0.152, s8:+0.054 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.187 | 18.44 | 18.44 | s11:+0.394, s4:+0.189, s2:+0.081 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.187 | 18.44 | 18.44 | s11:+0.394, s4:+0.189, s2:+0.081 |
| 3 | ISO_LOWER98_M15_D1 | 134 | 135 | preventive_schedule | 0.498 | 46.49 | 14.13 | s11:+0.247, s4:+0.127, s8:+0.043 |
| 3 | ISO_LOWER98_M15_D2 | 134 | 136 | preventive_schedule | 0.498 | 46.49 | 14.13 | s11:+0.247, s4:+0.127, s8:+0.043 |
| 3 | RF_SLOPE_POINT_M15_D1 | 154 | 155 | preventive_schedule | 0.231 | 13.81 | 13.81 | s11:+0.382, s4:+0.179, s2:+0.068 |
| 3 | RF_SLOPE_POINT_M15_D2 | 154 | 156 | preventive_schedule | 0.231 | 13.81 | 13.81 | s11:+0.382, s4:+0.179, s2:+0.068 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 134 | 135 | preventive_schedule | 0.498 | 49.09 | 10.45 | s11:+0.247, s4:+0.127, s8:+0.043 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 134 | 136 | preventive_schedule | 0.498 | 49.09 | 10.45 | s11:+0.247, s4:+0.127, s8:+0.043 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.356 | indefinido | indefinido | s11:+0.326, s4:+0.154, s8:+0.054 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.360 | indefinido | indefinido | s11:+0.322, s4:+0.152, s8:+0.054 |
| 3 | HI_MARKER_D1 | 134 | 135 | preventive_schedule | 0.498 | indefinido | indefinido | s11:+0.247, s4:+0.127, s8:+0.043 |
| 3 | HI_MARKER_D2 | 134 | 136 | preventive_schedule | 0.498 | indefinido | indefinido | s11:+0.247, s4:+0.127, s8:+0.043 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=133, A=133.
- Repetição2: G=138, A=138.
- Repetição3: G=134, A=134.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.19 | 0.36 | 3.12% | 12.50% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.19 | 0.11 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.38 | 0.00 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.38 | 0.00 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.12% | 3.12% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 12.50% | 3.12% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 33.16 | 15 | 1.38 | 0.15 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 33.16 | 15 | 1.38 | 0.15 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.74 | 0.52 | 3.12% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.71 | 0.12 | 3.12% | 18.75% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.09 | 15 | 1.25 | 0.15 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.09 | 15 | 1.28 | 0.15 | 0.00% | 18.75% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.38 | 0.15 | 0.00% | 18.75% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.38 | 0.15 | 0.00% | 18.75% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.96 | 0.36 | 6.67% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.96 | 0.36 | 6.67% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.37 | 0.15 | 0.00% | 13.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.37 | 0.15 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.86 | 0.46 | 6.67% | 13.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.28 | 0.63 | 3.33% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 23.20 | 15 | 1.37 | 0.36 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 23.20 | 15 | 1.37 | 0.36 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.60 | 0.18 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.43 | 0.24 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 40.08 | 15 | 1.37 | 0.36 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 40.08 | 15 | 1.37 | 0.36 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.37 | 0.36 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.37 | 0.36 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.29 | 0.38 | 3.12% | 25.00% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.29 | 0.38 | 3.12% | 25.00% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.69 | 0.12 | 0.00% | 21.88% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.69 | 0.12 | 0.00% | 21.88% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.12% | 0.00% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 3.12% | 0.00% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 32.36 | 15 | 1.69 | 0.54 | 0.00% | 25.00% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 32.36 | 15 | 1.69 | 0.54 | 0.00% | 25.00% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.84 | 0.32 | 3.12% | 31.25% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.87 | 0.58 | 3.12% | 18.75% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 38.63 | 15 | 1.59 | 0.54 | 0.00% | 25.00% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 38.63 | 15 | 1.59 | 0.54 | 0.00% | 25.00% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.69 | 0.54 | 0.00% | 25.00% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.69 | 0.54 | 0.00% | 25.00% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
