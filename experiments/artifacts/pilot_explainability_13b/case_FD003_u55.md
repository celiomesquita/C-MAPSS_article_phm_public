# FD003, motor55 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible, max_discordance_d1, max_discordance_d2, max_unused_d1, max_unused_d2.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u55.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 457 | 458 | preventive_schedule | 0.400 | indefinido | indefinido | s11:+0.250, s4:+0.126, s17:+0.115 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 457 | 459 | preventive_schedule | 0.400 | indefinido | indefinido | s11:+0.250, s4:+0.126, s17:+0.115 |
| 1 | HI_WAIT_SELECTED_D1 | 461 | 462 | preventive_schedule | 0.391 | indefinido | indefinido | s11:+0.269, s4:+0.122, s17:+0.113 |
| 1 | HI_WAIT_SELECTED_D2 | 461 | 463 | preventive_schedule | 0.391 | indefinido | indefinido | s11:+0.269, s4:+0.122, s17:+0.113 |
| 1 | ISO_POINT_M15_D1 | 485 | 486 | preventive_schedule | 0.184 | 14.28 | 14.28 | s11:+0.346, s4:+0.171, s17:+0.141 |
| 1 | ISO_POINT_M15_D2 | 484 | 486 | preventive_schedule | 0.201 | 16.25 | 16.25 | s11:+0.339, s4:+0.168, s17:+0.141 |
| 1 | ISO_LOWER98_M15_D1 | 451 | 452 | preventive_schedule | 0.496 | 38.60 | 9.00 | s11:+0.208, s17:+0.104, s4:+0.099 |
| 1 | ISO_LOWER98_M15_D2 | 451 | 453 | preventive_schedule | 0.496 | 38.60 | 9.00 | s11:+0.208, s17:+0.104, s4:+0.099 |
| 1 | RF_SLOPE_POINT_M15_D1 | 491 | 492 | preventive_schedule | 0.112 | 14.79 | 14.79 | s11:+0.379, s4:+0.170, s17:+0.163 |
| 1 | RF_SLOPE_POINT_M15_D2 | 491 | 493 | preventive_schedule | 0.112 | 14.79 | 14.79 | s11:+0.379, s4:+0.170, s17:+0.163 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 451 | 452 | preventive_schedule | 0.496 | 50.89 | 0.00 | s11:+0.208, s17:+0.104, s4:+0.099 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 451 | 453 | preventive_schedule | 0.496 | 50.89 | 0.00 | s11:+0.208, s17:+0.104, s4:+0.099 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.940 | indefinido | indefinido | s11:+0.049, s4:+0.017, s17:-0.005 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.930 | indefinido | indefinido | s11:+0.057, s4:+0.023, s17:-0.007 |
| 1 | HI_MARKER_D1 | 451 | 452 | preventive_schedule | 0.496 | indefinido | indefinido | s11:+0.208, s17:+0.104, s4:+0.099 |
| 1 | HI_MARKER_D2 | 451 | 453 | preventive_schedule | 0.496 | indefinido | indefinido | s11:+0.208, s17:+0.104, s4:+0.099 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 326 | 327 | preventive_schedule/escolha interna inviável | 0.399 | indefinido | indefinido | s8:+0.648, s15:-0.092, s9:+0.061 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 326 | 328 | preventive_schedule/escolha interna inviável | 0.399 | indefinido | indefinido | s8:+0.648, s15:-0.092, s9:+0.061 |
| 2 | HI_WAIT_SELECTED_D1 | 244 | 245 | preventive_schedule/escolha interna inviável | 0.498 | indefinido | indefinido | s8:+0.562, s15:-0.050, s9:+0.042 |
| 2 | HI_WAIT_SELECTED_D2 | 244 | 246 | preventive_schedule/escolha interna inviável | 0.498 | indefinido | indefinido | s8:+0.562, s15:-0.050, s9:+0.042 |
| 2 | ISO_POINT_M15_D1 | 399 | 400 | preventive_schedule | 0.218 | 15.52 | 15.52 | s8:+0.817, s15:-0.157, s9:+0.093 |
| 2 | ISO_POINT_M15_D2 | 399 | 401 | preventive_schedule | 0.218 | 15.52 | 15.52 | s8:+0.817, s15:-0.157, s9:+0.093 |
| 2 | ISO_LOWER98_M15_D1 | 239 | 240 | preventive_schedule | 0.493 | 37.21 | 11.91 | s8:+0.571, s15:-0.047, s9:+0.041 |
| 2 | ISO_LOWER98_M15_D2 | 239 | 241 | preventive_schedule | 0.493 | 37.21 | 11.91 | s8:+0.571, s15:-0.047, s9:+0.041 |
| 2 | RF_SLOPE_POINT_M15_D1 | 431 | 432 | preventive_schedule | 0.129 | 15.24 | 15.24 | s8:+0.912, s15:-0.233, s9:+0.131 |
| 2 | RF_SLOPE_POINT_M15_D2 | 431 | 433 | preventive_schedule | 0.129 | 15.24 | 15.24 | s8:+0.912, s15:-0.233, s9:+0.131 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 244 | 245 | preventive_schedule | 0.498 | 48.11 | 13.90 | s8:+0.562, s15:-0.050, s9:+0.042 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 244 | 246 | preventive_schedule | 0.498 | 48.11 | 13.90 | s8:+0.562, s15:-0.050, s9:+0.042 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 1.000 | indefinido | indefinido | s8:-0.382, s15:+0.014, s11:+0.009 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 1.000 | indefinido | indefinido | s8:-0.400, s15:+0.018, s4:+0.012 |
| 2 | HI_MARKER_D1 | 239 | 240 | preventive_schedule | 0.493 | indefinido | indefinido | s8:+0.571, s15:-0.047, s9:+0.041 |
| 2 | HI_MARKER_D2 | 239 | 241 | preventive_schedule | 0.493 | indefinido | indefinido | s8:+0.571, s15:-0.047, s9:+0.041 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 450 | 451 | preventive_schedule | 0.296 | indefinido | indefinido | s8:+0.667, s15:-0.277, s14:+0.150 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 433 | 435 | preventive_schedule | 0.392 | indefinido | indefinido | s8:+0.598, s15:-0.238, s14:+0.128 |
| 3 | HI_WAIT_SELECTED_D1 | 406 | 407 | preventive_schedule | 0.461 | indefinido | indefinido | s8:+0.538, s15:-0.189, s14:+0.114 |
| 3 | HI_WAIT_SELECTED_D2 | 406 | 408 | preventive_schedule | 0.461 | indefinido | indefinido | s8:+0.538, s15:-0.189, s14:+0.114 |
| 3 | ISO_POINT_M15_D1 | 457 | 458 | preventive_schedule | 0.231 | 13.90 | 13.90 | s8:+0.684, s15:-0.278, s14:+0.155 |
| 3 | ISO_POINT_M15_D2 | 457 | 459 | preventive_schedule | 0.231 | 13.90 | 13.90 | s8:+0.684, s15:-0.278, s14:+0.155 |
| 3 | ISO_LOWER98_M15_D1 | 396 | 397 | preventive_schedule | 0.498 | 41.04 | 13.67 | s8:+0.518, s15:-0.175, s14:+0.096 |
| 3 | ISO_LOWER98_M15_D2 | 396 | 398 | preventive_schedule | 0.498 | 41.04 | 13.67 | s8:+0.518, s15:-0.175, s14:+0.096 |
| 3 | RF_SLOPE_POINT_M15_D1 | 466 | 467 | preventive_schedule | 0.189 | 14.19 | 14.19 | s8:+0.726, s15:-0.321, s14:+0.176 |
| 3 | RF_SLOPE_POINT_M15_D2 | 466 | 468 | preventive_schedule | 0.189 | 14.19 | 14.19 | s8:+0.726, s15:-0.321, s14:+0.176 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 397 | 398 | preventive_schedule | 0.486 | 52.15 | 5.91 | s8:+0.524, s15:-0.172, s14:+0.098 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 397 | 399 | preventive_schedule | 0.486 | 52.15 | 5.91 | s8:+0.524, s15:-0.172, s14:+0.098 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 1.000 | indefinido | indefinido | s8:-0.247, s11:+0.023, s15:+0.014 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 1.000 | indefinido | indefinido | s8:-0.259, s11:+0.024, s15:+0.018 |
| 3 | HI_MARKER_D1 | 396 | 397 | preventive_schedule | 0.498 | indefinido | indefinido | s8:+0.518, s15:-0.175, s14:+0.096 |
| 3 | HI_MARKER_D2 | 396 | 398 | preventive_schedule | 0.498 | indefinido | indefinido | s8:+0.518, s15:-0.175, s14:+0.096 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=451, A=451.
- Repetição2: G=239, A=239.
- Repetição3: G=396, A=396.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.50 | 0.31 | 0.00% | 18.75% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.50 | 0.31 | 0.00% | 18.75% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.97 | 0.04 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.97 | 0.04 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.59 | 0.36 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.59 | 0.57 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 29.60 | 15 | 1.97 | 0.50 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 29.60 | 15 | 1.97 | 0.50 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.28 | 0.62 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.16 | 0.64 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 63.60 | 15 | 1.97 | 0.50 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 63.60 | 15 | 1.97 | 0.50 | 0.00% | 12.50% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.97 | 0.50 | 0.00% | 12.50% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.97 | 0.50 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 11.03 | 0.58 | 0.00% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 11.03 | 0.58 | 0.00% | 36.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 10.10 | 0.00 | 0.00% | 13.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 10.10 | 0.00 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 5.80 | 0.32 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 5.63 | 0.30 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 25.30 | 15 | 10.10 | 0.00 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 25.30 | 15 | 10.10 | 0.00 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 3.47 | 0.75 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 3.50 | 0.95 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 34.21 | 15 | 10.13 | 0.37 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 34.21 | 15 | 9.87 | 0.95 | 0.00% | 36.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 10.10 | 0.00 | 0.00% | 23.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 10.10 | 0.00 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 3.53 | 1.61 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 5.40 | 1.08 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 5.53 | 0.08 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 5.53 | 0.08 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 3.70 | 0.61 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 3.70 | 0.61 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 27.37 | 15 | 5.53 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 27.37 | 15 | 5.53 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 4.13 | 0.87 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 4.03 | 0.96 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 46.24 | 15 | 5.60 | 0.83 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 46.24 | 15 | 5.70 | 0.92 | 0.00% | 20.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 5.53 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 5.53 | 0.70 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
