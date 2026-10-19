# FD003, motor24 — diagnóstico retrospectivo

Critérios de inclusão: max_discordance_d1, max_discordance_d2.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u24.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 435 | 436 | preventive_schedule | 0.287 | indefinido | indefinido | s8:+0.261, s4:+0.150, s13:+0.146 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 435 | 437 | preventive_schedule | 0.287 | indefinido | indefinido | s8:+0.261, s4:+0.150, s13:+0.146 |
| 1 | HI_WAIT_SELECTED_D1 | 416 | 417 | preventive_schedule | 0.445 | indefinido | indefinido | s8:+0.244, s13:+0.127, s15:-0.125 |
| 1 | HI_WAIT_SELECTED_D2 | 416 | 418 | preventive_schedule | 0.445 | indefinido | indefinido | s8:+0.244, s13:+0.127, s15:-0.125 |
| 1 | ISO_POINT_M15_D1 | 459 | 460 | preventive_schedule | 0.046 | 15.49 | 15.49 | s8:+0.310, s4:+0.219, s11:+0.202 |
| 1 | ISO_POINT_M15_D2 | 455 | 457 | preventive_schedule | 0.104 | 16.74 | 16.74 | s8:+0.299, s4:+0.200, s11:+0.182 |
| 1 | ISO_LOWER98_M15_D1 | 416 | 417 | preventive_schedule | 0.445 | 39.52 | 13.62 | s8:+0.244, s13:+0.127, s15:-0.125 |
| 1 | ISO_LOWER98_M15_D2 | 413 | 415 | preventive_schedule | 0.460 | 42.46 | 16.55 | s8:+0.239, s13:+0.127, s15:-0.124 |
| 1 | RF_SLOPE_POINT_M15_D1 | 458 | 459 | preventive_schedule | 0.069 | 15.41 | 15.41 | s8:+0.306, s4:+0.208, s11:+0.198 |
| 1 | RF_SLOPE_POINT_M15_D2 | 453 | 455 | preventive_schedule | 0.127 | 16.85 | 16.85 | s8:+0.295, s4:+0.184, s11:+0.175 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 427 | 428 | preventive_schedule | 0.367 | 44.47 | 14.92 | s8:+0.252, s13:+0.137, s15:-0.129 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 418 | 420 | preventive_schedule | 0.427 | 46.36 | 16.80 | s8:+0.246, s13:+0.129, s15:-0.125 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 1.000 | indefinido | indefinido | s2:-0.031, s8:+0.028, s11:-0.018 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 1.000 | indefinido | indefinido | s2:-0.038, s11:-0.019, s4:-0.016 |
| 1 | HI_MARKER_D1 | 406 | 407 | preventive_schedule | 0.492 | indefinido | indefinido | s8:+0.230, s13:+0.127, s15:-0.114 |
| 1 | HI_MARKER_D2 | 406 | 408 | preventive_schedule | 0.492 | indefinido | indefinido | s8:+0.230, s13:+0.127, s15:-0.114 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 469 | 470 | preventive_schedule | 0.291 | indefinido | indefinido | s11:+0.563, s15:-0.180, s4:+0.177 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 469 | 471 | preventive_schedule | 0.291 | indefinido | indefinido | s11:+0.563, s15:-0.180, s4:+0.177 |
| 2 | HI_WAIT_SELECTED_D1 | 461 | 462 | preventive_schedule | 0.356 | indefinido | indefinido | s11:+0.521, s15:-0.162, s4:+0.143 |
| 2 | HI_WAIT_SELECTED_D2 | 461 | 463 | preventive_schedule | 0.356 | indefinido | indefinido | s11:+0.521, s15:-0.162, s4:+0.143 |
| 2 | ISO_POINT_M15_D1 | 474 | 475 | preventive_schedule | 0.281 | 15.99 | 15.99 | s11:+0.581, s15:-0.192, s4:+0.177 |
| 2 | ISO_POINT_M15_D2 | 474 | 476 | preventive_schedule | 0.281 | 15.99 | 15.99 | s11:+0.581, s15:-0.192, s4:+0.177 |
| 2 | ISO_LOWER98_M15_D1 | 451 | 452 | preventive_schedule | 0.496 | 29.52 | 10.27 | s11:+0.416, s15:-0.153, s8:+0.133 |
| 2 | ISO_LOWER98_M15_D2 | 451 | 453 | preventive_schedule | 0.496 | 29.52 | 10.27 | s11:+0.416, s15:-0.153, s8:+0.133 |
| 2 | RF_SLOPE_POINT_M15_D1 | 461 | 462 | preventive_schedule | 0.356 | 15.47 | 15.47 | s11:+0.521, s15:-0.162, s4:+0.143 |
| 2 | RF_SLOPE_POINT_M15_D2 | 461 | 463 | preventive_schedule | 0.356 | 15.47 | 15.47 | s11:+0.521, s15:-0.162, s4:+0.143 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 451 | 452 | preventive_schedule | 0.496 | 27.57 | 5.06 | s11:+0.416, s15:-0.153, s8:+0.133 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 451 | 453 | preventive_schedule | 0.496 | 27.57 | 5.06 | s11:+0.416, s15:-0.153, s8:+0.133 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 1.000 | indefinido | indefinido | s11:-0.019, s15:-0.008, s8:+0.006 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 1.000 | indefinido | indefinido | s11:-0.041, s8:+0.012, s15:-0.011 |
| 2 | HI_MARKER_D1 | 451 | 452 | preventive_schedule | 0.496 | indefinido | indefinido | s11:+0.416, s15:-0.153, s8:+0.133 |
| 2 | HI_MARKER_D2 | 451 | 453 | preventive_schedule | 0.496 | indefinido | indefinido | s11:+0.416, s15:-0.153, s8:+0.133 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 457 | 458 | preventive_schedule | 0.389 | indefinido | indefinido | s4:+0.237, s2:+0.186, s11:+0.176 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 457 | 459 | preventive_schedule | 0.389 | indefinido | indefinido | s4:+0.237, s2:+0.186, s11:+0.176 |
| 3 | HI_WAIT_SELECTED_D1 | 455 | 456 | preventive_schedule | 0.421 | indefinido | indefinido | s4:+0.221, s2:+0.182, s11:+0.164 |
| 3 | HI_WAIT_SELECTED_D2 | 455 | 457 | preventive_schedule | 0.421 | indefinido | indefinido | s4:+0.221, s2:+0.182, s11:+0.164 |
| 3 | ISO_POINT_M15_D1 | 467 | 468 | preventive_schedule | 0.237 | 12.47 | 12.47 | s4:+0.306, s2:+0.248, s11:+0.195 |
| 3 | ISO_POINT_M15_D2 | 467 | 469 | preventive_schedule | 0.237 | 12.47 | 12.47 | s4:+0.306, s2:+0.248, s11:+0.195 |
| 3 | ISO_LOWER98_M15_D1 | 445 | 446 | preventive_schedule | 0.495 | 32.87 | 9.25 | s2:+0.190, s4:+0.178, s11:+0.126 |
| 3 | ISO_LOWER98_M15_D2 | 445 | 447 | preventive_schedule | 0.495 | 32.87 | 9.25 | s2:+0.190, s4:+0.178, s11:+0.126 |
| 3 | RF_SLOPE_POINT_M15_D1 | 466 | 467 | preventive_schedule | 0.252 | 14.61 | 14.61 | s4:+0.307, s2:+0.238, s11:+0.190 |
| 3 | RF_SLOPE_POINT_M15_D2 | 466 | 468 | preventive_schedule | 0.252 | 14.61 | 14.61 | s4:+0.307, s2:+0.238, s11:+0.190 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 445 | 446 | preventive_schedule | 0.495 | 30.81 | 0.00 | s2:+0.190, s4:+0.178, s11:+0.126 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 445 | 447 | preventive_schedule | 0.495 | 30.81 | 0.00 | s2:+0.190, s4:+0.178, s11:+0.126 |
| 3 | AGE_D1 | 154 | 155 | preventive_schedule | 1.000 | indefinido | indefinido | s2:+0.039, s4:-0.029, s11:-0.022 |
| 3 | AGE_D2 | 153 | 155 | preventive_schedule | 1.000 | indefinido | indefinido | s4:-0.035, s2:+0.026, s11:-0.024 |
| 3 | HI_MARKER_D1 | 445 | 446 | preventive_schedule | 0.495 | indefinido | indefinido | s2:+0.190, s4:+0.178, s11:+0.126 |
| 3 | HI_MARKER_D2 | 445 | 447 | preventive_schedule | 0.495 | indefinido | indefinido | s2:+0.190, s4:+0.178, s11:+0.126 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=406, A=406.
- Repetição2: G=451, A=451.
- Repetição3: G=445, A=445.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.33 | 0.71 | 0.00% | 20.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.33 | 0.71 | 0.00% | 20.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 4.40 | 0.11 | 0.00% | 10.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 4.40 | 0.11 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.40 | 0.67 | 0.00% | 20.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.63 | 0.45 | 0.00% | 33.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 25.91 | 15 | 3.77 | 1.00 | 0.00% | 33.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 25.91 | 15 | 4.27 | 0.86 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.90 | 1.00 | 0.00% | 6.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.33 | 0.15 | 0.00% | 33.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 29.56 | 15 | 2.40 | 0.79 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 29.56 | 15 | 2.40 | 0.76 | 0.00% | 43.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 4.40 | 0.70 | 0.00% | 23.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 4.40 | 0.70 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.17 | 0.38 | 0.00% | 13.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.17 | 0.38 | 0.00% | 13.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.50 | 0.04 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.50 | 0.04 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.07 | 0.85 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.07 | 0.85 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 19.25 | 15 | 1.50 | 0.27 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 19.25 | 15 | 1.50 | 0.27 | 0.00% | 13.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.10 | 0.31 | 0.00% | 13.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.90 | 0.42 | 0.00% | 13.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 22.51 | 15 | 1.50 | 0.27 | 0.00% | 13.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 22.51 | 15 | 1.50 | 0.27 | 0.00% | 13.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.50 | 0.27 | 0.00% | 13.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.50 | 0.27 | 0.00% | 13.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.53 | 0.38 | 0.00% | 9.38% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.53 | 0.38 | 0.00% | 9.38% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.34 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.34 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.34 | 0.31 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.34 | 0.31 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 23.62 | 15 | 2.34 | 0.62 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 23.62 | 15 | 2.34 | 0.62 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.31 | 0.29 | 0.00% | 12.50% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.34 | 0.28 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 41.43 | 15 | 2.34 | 0.62 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 41.43 | 15 | 2.34 | 0.62 | 0.00% | 9.38% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.34 | 0.62 | 0.00% | 9.38% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.34 | 0.62 | 0.00% | 9.38% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
