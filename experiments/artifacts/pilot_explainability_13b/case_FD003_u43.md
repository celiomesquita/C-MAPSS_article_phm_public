# FD003, motor43 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u43.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 277 | 278 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.233, s17:+0.119, s11:+0.089 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 277 | 279 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.233, s17:+0.119, s11:+0.089 |
| 1 | HI_WAIT_SELECTED_D1 | 279 | 280 | preventive_schedule | 0.475 | indefinido | indefinido | s4:+0.239, s17:+0.119, s9:+0.092 |
| 1 | HI_WAIT_SELECTED_D2 | 279 | 281 | preventive_schedule | 0.475 | indefinido | indefinido | s4:+0.239, s17:+0.119, s9:+0.092 |
| 1 | ISO_POINT_M15_D1 | 305 | 306 | preventive_schedule | 0.149 | 12.68 | 12.68 | s4:+0.398, s17:+0.201, s15:-0.143 |
| 1 | ISO_POINT_M15_D2 | 303 | 305 | preventive_schedule | 0.192 | 16.32 | 16.32 | s4:+0.376, s17:+0.198, s15:-0.139 |
| 1 | ISO_LOWER98_M15_D1 | 279 | 280 | preventive_schedule | 0.475 | 37.42 | 14.45 | s4:+0.239, s17:+0.119, s9:+0.092 |
| 1 | ISO_LOWER98_M15_D2 | 277 | 279 | preventive_schedule | 0.491 | 39.47 | 16.51 | s4:+0.233, s17:+0.119, s11:+0.089 |
| 1 | RF_SLOPE_POINT_M15_D1 | 288 | 289 | preventive_schedule | 0.351 | 14.86 | 14.86 | s4:+0.322, s17:+0.129, s9:+0.106 |
| 1 | RF_SLOPE_POINT_M15_D2 | 288 | 290 | preventive_schedule | 0.351 | 14.86 | 14.86 | s4:+0.322, s17:+0.129, s9:+0.106 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 277 | 278 | preventive_schedule | 0.491 | 41.46 | 7.21 | s4:+0.233, s17:+0.119, s11:+0.089 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 277 | 279 | preventive_schedule | 0.491 | 41.46 | 7.21 | s4:+0.233, s17:+0.119, s11:+0.089 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.928 | indefinido | indefinido | s4:+0.053, s17:+0.016, s15:-0.015 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.918 | indefinido | indefinido | s4:+0.063, s15:-0.016, s17:+0.016 |
| 1 | HI_MARKER_D1 | 277 | 278 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.233, s17:+0.119, s11:+0.089 |
| 1 | HI_MARKER_D2 | 277 | 279 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.233, s17:+0.119, s11:+0.089 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 286 | 287 | preventive_schedule/escolha interna inviável | 0.377 | indefinido | indefinido | s8:+0.561, s15:-0.217, s9:+0.127 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 286 | 288 | preventive_schedule/escolha interna inviável | 0.377 | indefinido | indefinido | s8:+0.561, s15:-0.217, s9:+0.127 |
| 2 | HI_WAIT_SELECTED_D1 | 284 | 285 | preventive_schedule/escolha interna inviável | 0.419 | indefinido | indefinido | s8:+0.530, s15:-0.213, s9:+0.122 |
| 2 | HI_WAIT_SELECTED_D2 | 284 | 286 | preventive_schedule/escolha interna inviável | 0.419 | indefinido | indefinido | s8:+0.530, s15:-0.213, s9:+0.122 |
| 2 | ISO_POINT_M15_D1 | 303 | 304 | preventive_schedule | 0.215 | 15.52 | 15.52 | s8:+0.737, s15:-0.310, s9:+0.161 |
| 2 | ISO_POINT_M15_D2 | 302 | 304 | preventive_schedule | 0.222 | 16.17 | 16.17 | s8:+0.730, s15:-0.304, s9:+0.159 |
| 2 | ISO_LOWER98_M15_D1 | 279 | 280 | preventive_schedule | 0.487 | 36.50 | 11.20 | s8:+0.476, s15:-0.204, s9:+0.114 |
| 2 | ISO_LOWER98_M15_D2 | 279 | 281 | preventive_schedule | 0.487 | 36.50 | 11.20 | s8:+0.476, s15:-0.204, s9:+0.114 |
| 2 | RF_SLOPE_POINT_M15_D1 | 307 | 308 | preventive_schedule | 0.122 | 14.49 | 14.49 | s8:+0.796, s15:-0.315, s9:+0.174 |
| 2 | RF_SLOPE_POINT_M15_D2 | 294 | 296 | preventive_schedule | 0.303 | 16.63 | 16.63 | s8:+0.657, s15:-0.274, s9:+0.141 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 281 | 282 | preventive_schedule | 0.460 | 47.87 | 13.66 | s8:+0.495, s15:-0.200, s9:+0.118 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 281 | 283 | preventive_schedule | 0.460 | 47.87 | 13.66 | s8:+0.495, s15:-0.200, s9:+0.118 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.919 | indefinido | indefinido | s8:+0.091, s15:-0.036, s4:+0.016 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.912 | indefinido | indefinido | s8:+0.091, s15:-0.031, s4:+0.016 |
| 2 | HI_MARKER_D1 | 279 | 280 | preventive_schedule | 0.487 | indefinido | indefinido | s8:+0.476, s15:-0.204, s9:+0.114 |
| 2 | HI_MARKER_D2 | 279 | 281 | preventive_schedule | 0.487 | indefinido | indefinido | s8:+0.476, s15:-0.204, s9:+0.114 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 277 | 278 | preventive_schedule | 0.500 | indefinido | indefinido | s11:+0.270, s4:+0.149, s20:-0.076 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 277 | 279 | preventive_schedule | 0.500 | indefinido | indefinido | s11:+0.270, s4:+0.149, s20:-0.076 |
| 3 | HI_WAIT_SELECTED_D1 | 282 | 283 | preventive_schedule | 0.440 | indefinido | indefinido | s11:+0.284, s4:+0.162, s8:+0.083 |
| 3 | HI_WAIT_SELECTED_D2 | 279 | 281 | preventive_schedule | 0.482 | indefinido | indefinido | s11:+0.272, s4:+0.153, s8:+0.078 |
| 3 | ISO_POINT_M15_D1 | 305 | 306 | preventive_schedule | 0.162 | 14.99 | 14.99 | s11:+0.397, s4:+0.255, s8:+0.127 |
| 3 | ISO_POINT_M15_D2 | 305 | 307 | preventive_schedule | 0.162 | 14.99 | 14.99 | s11:+0.397, s4:+0.255, s8:+0.127 |
| 3 | ISO_LOWER98_M15_D1 | 277 | 278 | preventive_schedule | 0.500 | 39.67 | 12.00 | s11:+0.270, s4:+0.149, s20:-0.076 |
| 3 | ISO_LOWER98_M15_D2 | 277 | 279 | preventive_schedule | 0.500 | 39.67 | 12.00 | s11:+0.270, s4:+0.149, s20:-0.076 |
| 3 | RF_SLOPE_POINT_M15_D1 | 308 | 309 | preventive_schedule | 0.107 | 11.07 | 11.07 | s11:+0.415, s4:+0.269, s8:+0.133 |
| 3 | RF_SLOPE_POINT_M15_D2 | 308 | 310 | preventive_schedule | 0.107 | 11.07 | 11.07 | s11:+0.415, s4:+0.269, s8:+0.133 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 278 | 279 | preventive_schedule | 0.496 | 39.29 | 6.81 | s11:+0.276, s4:+0.145, s20:-0.078 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 278 | 280 | preventive_schedule | 0.496 | 39.29 | 6.81 | s11:+0.276, s4:+0.145, s20:-0.078 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.958 | indefinido | indefinido | s4:+0.034, s6:-0.024, s8:+0.015 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.953 | indefinido | indefinido | s4:+0.040, s6:-0.024, s8:+0.015 |
| 3 | HI_MARKER_D1 | 277 | 278 | preventive_schedule | 0.500 | indefinido | indefinido | s11:+0.270, s4:+0.149, s20:-0.076 |
| 3 | HI_MARKER_D2 | 277 | 279 | preventive_schedule | 0.500 | indefinido | indefinido | s11:+0.270, s4:+0.149, s20:-0.076 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=277, A=277.
- Repetição2: G=279, A=279.
- Repetição3: G=277, A=277.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.12 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.12 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.12 | 0.35 | 0.00% | 18.75% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.12 | 0.35 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.22 | 0.20 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.81 | 0.63 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 22.97 | 15 | 2.09 | 0.65 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 22.97 | 15 | 2.12 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.88 | 0.60 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.72 | 0.60 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.25 | 15 | 1.53 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.25 | 15 | 1.56 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.12 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.12 | 0.36 | 0.00% | 21.88% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.23 | 0.46 | 0.00% | 6.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.23 | 0.46 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.67 | 0.44 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.67 | 0.44 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.53 | 0.74 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.57 | 0.42 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 25.30 | 15 | 1.67 | 0.59 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 25.30 | 15 | 1.67 | 0.59 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.87 | 0.44 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 5.60 | 0.88 | 0.00% | 46.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 34.21 | 15 | 0.67 | 0.40 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 34.21 | 15 | 0.83 | 0.44 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.67 | 0.59 | 0.00% | 10.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.67 | 0.59 | 0.00% | 10.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.00 | 0.32 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.00 | 0.32 | 0.00% | 26.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.00 | 0.18 | 0.00% | 26.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.00 | 0.23 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.13 | 0.12 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.07 | 0.23 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 27.67 | 15 | 2.00 | 0.32 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 27.67 | 15 | 2.00 | 0.32 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.17 | 0.43 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.27 | 0.50 | 0.00% | 13.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 32.48 | 15 | 1.40 | 0.64 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 32.48 | 15 | 1.40 | 0.64 | 0.00% | 26.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.00 | 0.32 | 0.00% | 26.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.00 | 0.32 | 0.00% | 26.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
