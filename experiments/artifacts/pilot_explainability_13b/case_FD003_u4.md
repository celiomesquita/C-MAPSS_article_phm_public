# FD003, motor4 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u4.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 253 | 254 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.241, s2:+0.184, s17:+0.043 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 253 | 255 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.241, s2:+0.184, s17:+0.043 |
| 1 | HI_WAIT_SELECTED_D1 | 258 | 259 | preventive_schedule | 0.461 | indefinido | indefinido | s11:+0.268, s2:+0.182, s17:+0.050 |
| 1 | HI_WAIT_SELECTED_D2 | 255 | 257 | preventive_schedule | 0.467 | indefinido | indefinido | s11:+0.252, s2:+0.194, s17:+0.048 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.342 | 18.97 | 18.97 | s11:+0.314, s2:+0.248, s17:+0.050 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.342 | 18.97 | 18.97 | s11:+0.314, s2:+0.248, s17:+0.050 |
| 1 | ISO_LOWER98_M15_D1 | 253 | 254 | preventive_schedule | 0.494 | 28.41 | 5.52 | s11:+0.241, s2:+0.184, s17:+0.043 |
| 1 | ISO_LOWER98_M15_D2 | 253 | 255 | preventive_schedule | 0.494 | 28.41 | 5.52 | s11:+0.241, s2:+0.184, s17:+0.043 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.342 | 32.55 | 32.55 | s11:+0.314, s2:+0.248, s17:+0.050 |
| 1 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.342 | 32.55 | 32.55 | s11:+0.314, s2:+0.248, s17:+0.050 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 253 | 254 | preventive_schedule | 0.494 | 32.91 | 3.45 | s11:+0.241, s2:+0.184, s17:+0.043 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 253 | 255 | preventive_schedule | 0.494 | 32.91 | 3.45 | s11:+0.241, s2:+0.184, s17:+0.043 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.917 | indefinido | indefinido | s11:+0.063, s17:+0.017, s3:+0.006 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.934 | indefinido | indefinido | s11:+0.062, s2:-0.015, s17:+0.014 |
| 1 | HI_MARKER_D1 | 253 | 254 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.241, s2:+0.184, s17:+0.043 |
| 1 | HI_MARKER_D2 | 253 | 255 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.241, s2:+0.184, s17:+0.043 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 260 | 261 | preventive_schedule | 0.291 | indefinido | indefinido | s11:+0.267, s4:+0.245, s8:+0.098 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 249 | 251 | preventive_schedule | 0.388 | indefinido | indefinido | s4:+0.228, s11:+0.214, s8:+0.083 |
| 2 | HI_WAIT_SELECTED_D1 | 248 | 249 | preventive_schedule | 0.407 | indefinido | indefinido | s4:+0.224, s11:+0.205, s8:+0.080 |
| 2 | HI_WAIT_SELECTED_D2 | 248 | 250 | preventive_schedule | 0.407 | indefinido | indefinido | s4:+0.224, s11:+0.205, s8:+0.080 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.184 | 16.08 | 16.08 | s11:+0.296, s4:+0.291, s8:+0.114 |
| 2 | ISO_POINT_M15_D2 | 271 | 273 | late_schedule | 0.184 | 16.08 | 16.08 | s11:+0.296, s4:+0.291, s8:+0.114 |
| 2 | ISO_LOWER98_M15_D1 | 238 | 239 | preventive_schedule | 0.495 | 37.90 | 14.00 | s4:+0.196, s11:+0.171, s8:+0.067 |
| 2 | ISO_LOWER98_M15_D2 | 238 | 240 | preventive_schedule | 0.495 | 37.90 | 14.00 | s4:+0.196, s11:+0.171, s8:+0.067 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.184 | 27.09 | 27.09 | s11:+0.296, s4:+0.291, s8:+0.114 |
| 2 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.184 | 27.09 | 27.09 | s11:+0.296, s4:+0.291, s8:+0.114 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 246 | 247 | preventive_schedule | 0.429 | 51.38 | 15.84 | s4:+0.220, s11:+0.189, s8:+0.080 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 246 | 248 | preventive_schedule | 0.429 | 51.38 | 15.84 | s4:+0.220, s11:+0.189, s8:+0.080 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.868 | indefinido | indefinido | s11:+0.060, s4:+0.046, s8:+0.015 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.875 | indefinido | indefinido | s11:+0.058, s4:+0.041, s8:+0.016 |
| 2 | HI_MARKER_D1 | 238 | 239 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.196, s11:+0.171, s8:+0.067 |
| 2 | HI_MARKER_D2 | 238 | 240 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.196, s11:+0.171, s8:+0.067 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 244 | 245 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.200, s11:+0.119, s2:+0.092 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 244 | 246 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.200, s11:+0.119, s2:+0.092 |
| 3 | HI_WAIT_SELECTED_D1 | 249 | 250 | preventive_schedule | 0.450 | indefinido | indefinido | s4:+0.209, s11:+0.132, s2:+0.097 |
| 3 | HI_WAIT_SELECTED_D2 | 246 | 248 | preventive_schedule | 0.480 | indefinido | indefinido | s4:+0.202, s11:+0.117, s2:+0.097 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.278 | 23.37 | 23.37 | s4:+0.268, s11:+0.183, s2:+0.132 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.278 | 23.37 | 23.37 | s4:+0.268, s11:+0.183, s2:+0.132 |
| 3 | ISO_LOWER98_M15_D1 | 244 | 245 | preventive_schedule | 0.491 | 36.42 | 12.32 | s4:+0.200, s11:+0.119, s2:+0.092 |
| 3 | ISO_LOWER98_M15_D2 | 244 | 246 | preventive_schedule | 0.491 | 36.42 | 12.32 | s4:+0.200, s11:+0.119, s2:+0.092 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.278 | 25.31 | 25.31 | s4:+0.268, s11:+0.183, s2:+0.132 |
| 3 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.278 | 25.31 | 25.31 | s4:+0.268, s11:+0.183, s2:+0.132 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 244 | 245 | preventive_schedule | 0.491 | 38.25 | 7.73 | s4:+0.200, s11:+0.119, s2:+0.092 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 244 | 246 | preventive_schedule | 0.491 | 38.25 | 7.73 | s4:+0.200, s11:+0.119, s2:+0.092 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.902 | indefinido | indefinido | s4:+0.042, s11:+0.037, s15:+0.010 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.914 | indefinido | indefinido | s4:+0.038, s11:+0.036, s15:+0.009 |
| 3 | HI_MARKER_D1 | 244 | 245 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.200, s11:+0.119, s2:+0.092 |
| 3 | HI_MARKER_D2 | 244 | 246 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.200, s11:+0.119, s2:+0.092 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=253, A=253.
- Repetição2: G=238, A=238.
- Repetição3: G=244, A=244.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.69 | 0.81 | 0.00% | 18.75% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.69 | 0.81 | 0.00% | 18.75% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.29 | 0.48 | 3.12% | 15.62% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.69 | 0.65 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 9.38% | 9.38% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 15.62% | 9.38% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 22.89 | 15 | 2.69 | 0.81 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 22.89 | 15 | 2.69 | 0.81 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 3.12% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 3.12% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 29.47 | 15 | 2.69 | 0.81 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 29.47 | 15 | 2.69 | 0.81 | 0.00% | 18.75% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.69 | 0.81 | 0.00% | 18.75% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.69 | 0.81 | 0.00% | 18.75% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.62 | 0.43 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.81 | 0.36 | 0.00% | 12.50% | 0/32 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.47 | 0.29 | 0.00% | 12.50% | 0/32 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.47 | 0.29 | 0.00% | 12.50% | 0/32 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.25% | 3.12% | 0/32 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.23 | 0.56 | 18.75% | 15.62% | 0/32 |
| 2 | ISO_LOWER98_M15_D1 | 23.90 | 15 | 2.47 | 0.77 | 0.00% | 18.75% | 0/32 |
| 2 | ISO_LOWER98_M15_D2 | 23.90 | 15 | 2.47 | 0.77 | 0.00% | 18.75% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 12.50% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 12.50% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 35.54 | 15 | 1.59 | 0.50 | 0.00% | 18.75% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 35.54 | 15 | 1.59 | 0.62 | 0.00% | 18.75% | 0/32 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.47 | 0.77 | 0.00% | 18.75% | 0/32 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.47 | 0.77 | 0.00% | 18.75% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.17 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.17 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.17 | 0.35 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.17 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 24.10 | 15 | 2.17 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 24.10 | 15 | 2.17 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 30.51 | 15 | 2.03 | 0.42 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 30.51 | 15 | 2.10 | 0.42 | 0.00% | 20.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.17 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.17 | 0.50 | 0.00% | 20.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
