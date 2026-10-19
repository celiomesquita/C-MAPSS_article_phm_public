# FD003, motor71 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u71.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 362 | 363 | preventive_schedule | 0.391 | indefinido | indefinido | s13:+0.579, s15:-0.210, s4:+0.158 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 362 | 364 | preventive_schedule | 0.391 | indefinido | indefinido | s13:+0.579, s15:-0.210, s4:+0.158 |
| 1 | HI_WAIT_SELECTED_D1 | 353 | 354 | preventive_schedule | 0.437 | indefinido | indefinido | s13:+0.536, s15:-0.190, s4:+0.154 |
| 1 | HI_WAIT_SELECTED_D2 | 353 | 355 | preventive_schedule | 0.437 | indefinido | indefinido | s13:+0.536, s15:-0.190, s4:+0.154 |
| 1 | ISO_POINT_M15_D1 | 383 | 384 | preventive_schedule | 0.231 | 14.33 | 14.33 | s13:+0.652, s4:+0.293, s15:-0.269 |
| 1 | ISO_POINT_M15_D2 | 383 | 385 | preventive_schedule | 0.231 | 14.33 | 14.33 | s13:+0.652, s4:+0.293, s15:-0.269 |
| 1 | ISO_LOWER98_M15_D1 | 347 | 348 | preventive_schedule | 0.476 | 35.85 | 15.38 | s13:+0.515, s15:-0.190, s4:+0.139 |
| 1 | ISO_LOWER98_M15_D2 | 343 | 345 | preventive_schedule | 0.498 | 36.60 | 16.13 | s13:+0.503, s15:-0.171, s4:+0.117 |
| 1 | RF_SLOPE_POINT_M15_D1 | 373 | 374 | preventive_schedule | 0.275 | 15.29 | 15.29 | s13:+0.616, s4:+0.237, s15:-0.230 |
| 1 | RF_SLOPE_POINT_M15_D2 | 373 | 375 | preventive_schedule | 0.275 | 15.29 | 15.29 | s13:+0.616, s4:+0.237, s15:-0.230 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 343 | 344 | preventive_schedule | 0.498 | 29.93 | 0.00 | s13:+0.503, s15:-0.171, s4:+0.117 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 343 | 345 | preventive_schedule | 0.498 | 29.93 | 0.00 | s13:+0.503, s15:-0.171, s4:+0.117 |
| 1 | AGE_D1 | 145 | 146 | preventive_schedule | 1.000 | indefinido | indefinido | s13:+0.110, s4:-0.103, s15:-0.033 |
| 1 | AGE_D2 | 144 | 146 | preventive_schedule | 1.000 | indefinido | indefinido | s4:-0.111, s13:+0.107, s15:-0.032 |
| 1 | HI_MARKER_D1 | 343 | 344 | preventive_schedule | 0.498 | indefinido | indefinido | s13:+0.503, s15:-0.171, s4:+0.117 |
| 1 | HI_MARKER_D2 | 343 | 345 | preventive_schedule | 0.498 | indefinido | indefinido | s13:+0.503, s15:-0.171, s4:+0.117 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 173 | 174 | preventive_schedule | 0.398 | indefinido | indefinido | s8:+0.692, s15:-0.103, s14:+0.051 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 173 | 175 | preventive_schedule | 0.398 | indefinido | indefinido | s8:+0.692, s15:-0.103, s14:+0.051 |
| 2 | HI_WAIT_SELECTED_D1 | 173 | 174 | preventive_schedule | 0.398 | indefinido | indefinido | s8:+0.692, s15:-0.103, s14:+0.051 |
| 2 | HI_WAIT_SELECTED_D2 | 173 | 175 | preventive_schedule | 0.398 | indefinido | indefinido | s8:+0.692, s15:-0.103, s14:+0.051 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.000 | 16.02 | 16.02 | s8:+1.776, s15:-0.644, s14:+0.318 |
| 2 | ISO_POINT_M15_D2 | 335 | 337 | preventive_schedule | 0.006 | 16.02 | 16.02 | s8:+1.056, s15:-0.293, s14:+0.139 |
| 2 | ISO_LOWER98_M15_D1 | 163 | 164 | preventive_schedule | 0.497 | 87.77 | 13.72 | s8:+0.537, s15:-0.055, s14:+0.042 |
| 2 | ISO_LOWER98_M15_D2 | 163 | 165 | preventive_schedule | 0.497 | 87.77 | 13.72 | s8:+0.537, s15:-0.055, s14:+0.042 |
| 2 | RF_SLOPE_POINT_M15_D1 | 164 | 165 | preventive_schedule | 0.438 | 6.14 | 6.14 | s8:+0.609, s15:-0.067, s14:+0.046 |
| 2 | RF_SLOPE_POINT_M15_D2 | 164 | 166 | preventive_schedule | 0.438 | 6.14 | 6.14 | s8:+0.609, s15:-0.067, s14:+0.046 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 163 | 164 | preventive_schedule | 0.497 | 91.72 | 0.00 | s8:+0.537, s15:-0.055, s14:+0.042 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 163 | 165 | preventive_schedule | 0.497 | 91.72 | 0.00 | s8:+0.537, s15:-0.055, s14:+0.042 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.734 | indefinido | indefinido | s8:+0.330, s15:-0.071, s14:+0.031 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.812 | indefinido | indefinido | s8:+0.248, s15:-0.065, s14:+0.028 |
| 2 | HI_MARKER_D1 | 163 | 164 | preventive_schedule | 0.497 | indefinido | indefinido | s8:+0.537, s15:-0.055, s14:+0.042 |
| 2 | HI_MARKER_D2 | 163 | 165 | preventive_schedule | 0.497 | indefinido | indefinido | s8:+0.537, s15:-0.055, s14:+0.042 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 367 | 368 | preventive_schedule | 0.296 | indefinido | indefinido | s8:+0.343, s11:+0.275, s12:-0.241 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 367 | 369 | preventive_schedule | 0.296 | indefinido | indefinido | s8:+0.343, s11:+0.275, s12:-0.241 |
| 3 | HI_WAIT_SELECTED_D1 | 358 | 359 | preventive_schedule | 0.392 | indefinido | indefinido | s8:+0.322, s11:+0.239, s12:-0.219 |
| 3 | HI_WAIT_SELECTED_D2 | 358 | 360 | preventive_schedule | 0.392 | indefinido | indefinido | s8:+0.322, s11:+0.239, s12:-0.219 |
| 3 | ISO_POINT_M15_D1 | 387 | 388 | preventive_schedule | 0.071 | 13.82 | 13.82 | s11:+0.420, s8:+0.400, s12:-0.315 |
| 3 | ISO_POINT_M15_D2 | 386 | 388 | preventive_schedule | 0.083 | 16.48 | 16.48 | s11:+0.410, s8:+0.394, s12:-0.313 |
| 3 | ISO_LOWER98_M15_D1 | 348 | 349 | preventive_schedule | 0.497 | 46.49 | 14.13 | s8:+0.309, s12:-0.194, s11:+0.152 |
| 3 | ISO_LOWER98_M15_D2 | 348 | 350 | preventive_schedule | 0.497 | 46.49 | 14.13 | s8:+0.309, s12:-0.194, s11:+0.152 |
| 3 | RF_SLOPE_POINT_M15_D1 | 370 | 371 | preventive_schedule | 0.269 | 13.37 | 13.37 | s8:+0.349, s11:+0.291, s12:-0.246 |
| 3 | RF_SLOPE_POINT_M15_D2 | 370 | 372 | preventive_schedule | 0.269 | 13.37 | 13.37 | s8:+0.349, s11:+0.291, s12:-0.246 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 348 | 349 | preventive_schedule | 0.497 | 41.30 | 2.66 | s8:+0.309, s12:-0.194, s11:+0.152 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 348 | 350 | preventive_schedule | 0.497 | 41.30 | 2.66 | s8:+0.309, s12:-0.194, s11:+0.152 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 1.000 | indefinido | indefinido | s8:+0.065, s11:-0.046, s4:-0.042 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 1.000 | indefinido | indefinido | s8:+0.064, s11:-0.057, s4:-0.046 |
| 3 | HI_MARKER_D1 | 348 | 349 | preventive_schedule | 0.497 | indefinido | indefinido | s8:+0.309, s12:-0.194, s11:+0.152 |
| 3 | HI_MARKER_D2 | 348 | 350 | preventive_schedule | 0.497 | indefinido | indefinido | s8:+0.309, s12:-0.194, s11:+0.152 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=343, A=343.
- Repetição2: G=163, A=163.
- Repetição3: G=348, A=348.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 3.69 | 1.00 | 0.00% | 15.62% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 3.69 | 1.00 | 0.00% | 15.62% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 4.16 | 0.12 | 0.00% | 18.75% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 4.16 | 0.12 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 3.12 | 1.11 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 3.12 | 1.11 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 20.47 | 15 | 3.44 | 0.92 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 20.47 | 15 | 4.16 | 0.88 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.59 | 0.60 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.41 | 0.84 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 52.73 | 15 | 3.44 | 0.88 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 52.73 | 15 | 3.44 | 0.88 | 0.00% | 21.88% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 4.16 | 0.88 | 0.00% | 21.88% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 4.16 | 0.88 | 0.00% | 21.88% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 4.33 | 0.20 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 4.33 | 0.20 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.13 | 0.16 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.13 | 0.16 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 3.50 | 0.65 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 74.05 | 15 | 1.13 | 0.21 | 0.00% | 20.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 74.05 | 15 | 1.13 | 0.21 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 14.27 | 0.08 | 0.00% | 13.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 14.27 | 0.08 | 0.00% | 13.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 136.85 | 15 | 1.13 | 0.20 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 136.85 | 15 | 1.13 | 0.20 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.13 | 0.20 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.13 | 0.20 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.06 | 0.38 | 0.00% | 25.00% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.06 | 0.38 | 0.00% | 25.00% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.16 | 0.14 | 0.00% | 12.50% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.16 | 0.14 | 0.00% | 12.50% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.53 | 0.43 | 0.00% | 12.50% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.56 | 0.61 | 0.00% | 12.50% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 32.36 | 15 | 2.16 | 0.67 | 0.00% | 25.00% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 32.36 | 15 | 2.16 | 0.67 | 0.00% | 25.00% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.75 | 1.04 | 0.00% | 25.00% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.41 | 1.21 | 0.00% | 25.00% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 38.63 | 15 | 1.66 | 0.67 | 0.00% | 25.00% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 38.63 | 15 | 1.75 | 0.67 | 0.00% | 25.00% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.16 | 0.67 | 0.00% | 25.00% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.16 | 0.67 | 0.00% | 25.00% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
