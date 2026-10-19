# FD003, motor20 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u20.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 298 | 299 | preventive_schedule | 0.487 | indefinido | indefinido | s4:+0.224, s17:+0.135, s15:-0.109 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 298 | 300 | preventive_schedule | 0.487 | indefinido | indefinido | s4:+0.224, s17:+0.135, s15:-0.109 |
| 1 | HI_WAIT_SELECTED_D1 | 300 | 301 | preventive_schedule | 0.474 | indefinido | indefinido | s4:+0.227, s17:+0.141, s15:-0.112 |
| 1 | HI_WAIT_SELECTED_D2 | 300 | 302 | preventive_schedule | 0.474 | indefinido | indefinido | s4:+0.227, s17:+0.141, s15:-0.112 |
| 1 | ISO_POINT_M15_D1 | 327 | 328 | preventive_schedule | 0.147 | 12.12 | 12.12 | s4:+0.382, s17:+0.198, s11:+0.149 |
| 1 | ISO_POINT_M15_D2 | 322 | 324 | preventive_schedule | 0.200 | 16.32 | 16.32 | s4:+0.360, s17:+0.182, s11:+0.143 |
| 1 | ISO_LOWER98_M15_D1 | 298 | 299 | preventive_schedule | 0.487 | 37.42 | 14.45 | s4:+0.224, s17:+0.135, s15:-0.109 |
| 1 | ISO_LOWER98_M15_D2 | 298 | 300 | preventive_schedule | 0.487 | 37.42 | 14.45 | s4:+0.224, s17:+0.135, s15:-0.109 |
| 1 | RF_SLOPE_POINT_M15_D1 | 319 | 320 | preventive_schedule | 0.229 | 11.44 | 11.44 | s4:+0.348, s17:+0.169, s11:+0.140 |
| 1 | RF_SLOPE_POINT_M15_D2 | 319 | 321 | preventive_schedule | 0.229 | 11.44 | 11.44 | s4:+0.348, s17:+0.169, s11:+0.140 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 298 | 299 | preventive_schedule | 0.487 | 48.79 | 14.54 | s4:+0.224, s17:+0.135, s15:-0.109 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 298 | 300 | preventive_schedule | 0.487 | 48.79 | 14.54 | s4:+0.224, s17:+0.135, s15:-0.109 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.981 | indefinido | indefinido | s11:+0.018, s4:-0.014, s17:+0.013 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.991 | indefinido | indefinido | s11:+0.020, s4:-0.019, s17:+0.009 |
| 1 | HI_MARKER_D1 | 298 | 299 | preventive_schedule | 0.487 | indefinido | indefinido | s4:+0.224, s17:+0.135, s15:-0.109 |
| 1 | HI_MARKER_D2 | 298 | 300 | preventive_schedule | 0.487 | indefinido | indefinido | s4:+0.224, s17:+0.135, s15:-0.109 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 312 | 313 | preventive_schedule/escolha interna inviável | 0.396 | indefinido | indefinido | s8:+0.572, s15:-0.268, s9:+0.130 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 312 | 314 | preventive_schedule/escolha interna inviável | 0.396 | indefinido | indefinido | s8:+0.572, s15:-0.268, s9:+0.130 |
| 2 | HI_WAIT_SELECTED_D1 | 312 | 313 | preventive_schedule/escolha interna inviável | 0.396 | indefinido | indefinido | s8:+0.572, s15:-0.268, s9:+0.130 |
| 2 | HI_WAIT_SELECTED_D2 | 312 | 314 | preventive_schedule/escolha interna inviável | 0.396 | indefinido | indefinido | s8:+0.572, s15:-0.268, s9:+0.130 |
| 2 | ISO_POINT_M15_D1 | 327 | 328 | preventive_schedule | 0.215 | 15.52 | 15.52 | s8:+0.717, s15:-0.327, s9:+0.167 |
| 2 | ISO_POINT_M15_D2 | 327 | 329 | preventive_schedule | 0.215 | 15.52 | 15.52 | s8:+0.717, s15:-0.327, s9:+0.167 |
| 2 | ISO_LOWER98_M15_D1 | 307 | 308 | preventive_schedule | 0.488 | 37.21 | 11.91 | s8:+0.495, s15:-0.269, s9:+0.120 |
| 2 | ISO_LOWER98_M15_D2 | 307 | 309 | preventive_schedule | 0.488 | 37.21 | 11.91 | s8:+0.495, s15:-0.269, s9:+0.120 |
| 2 | RF_SLOPE_POINT_M15_D1 | 317 | 318 | preventive_schedule | 0.306 | 14.60 | 14.60 | s8:+0.627, s15:-0.269, s9:+0.140 |
| 2 | RF_SLOPE_POINT_M15_D2 | 317 | 319 | preventive_schedule | 0.306 | 14.60 | 14.60 | s8:+0.627, s15:-0.269, s9:+0.140 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 308 | 309 | preventive_schedule | 0.469 | 42.45 | 8.23 | s8:+0.504, s15:-0.261, s9:+0.122 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 307 | 309 | preventive_schedule | 0.488 | 50.58 | 16.37 | s8:+0.495, s15:-0.269, s9:+0.120 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.984 | indefinido | indefinido | s8:+0.015, s11:+0.010, s15:-0.008 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.981 | indefinido | indefinido | s8:+0.009, s11:+0.009, s15:-0.004 |
| 2 | HI_MARKER_D1 | 307 | 308 | preventive_schedule | 0.488 | indefinido | indefinido | s8:+0.495, s15:-0.269, s9:+0.120 |
| 2 | HI_MARKER_D2 | 307 | 309 | preventive_schedule | 0.488 | indefinido | indefinido | s8:+0.495, s15:-0.269, s9:+0.120 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 302 | 303 | preventive_schedule | 0.486 | indefinido | indefinido | s4:+0.194, s11:+0.182, s2:+0.102 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 302 | 304 | preventive_schedule | 0.486 | indefinido | indefinido | s4:+0.194, s11:+0.182, s2:+0.102 |
| 3 | HI_WAIT_SELECTED_D1 | 307 | 308 | preventive_schedule | 0.449 | indefinido | indefinido | s4:+0.208, s11:+0.186, s2:+0.106 |
| 3 | HI_WAIT_SELECTED_D2 | 304 | 306 | preventive_schedule | 0.486 | indefinido | indefinido | s4:+0.194, s11:+0.182, s15:-0.099 |
| 3 | ISO_POINT_M15_D1 | 334 | 335 | preventive_schedule | 0.128 | 15.72 | 15.72 | s4:+0.320, s11:+0.270, s2:+0.167 |
| 3 | ISO_POINT_M15_D2 | 334 | 336 | preventive_schedule | 0.128 | 15.72 | 15.72 | s4:+0.320, s11:+0.270, s2:+0.167 |
| 3 | ISO_LOWER98_M15_D1 | 302 | 303 | preventive_schedule | 0.486 | 36.42 | 12.32 | s4:+0.194, s11:+0.182, s2:+0.102 |
| 3 | ISO_LOWER98_M15_D2 | 302 | 304 | preventive_schedule | 0.486 | 36.42 | 12.32 | s4:+0.194, s11:+0.182, s2:+0.102 |
| 3 | RF_SLOPE_POINT_M15_D1 | 318 | 319 | preventive_schedule | 0.292 | 12.59 | 12.59 | s4:+0.257, s11:+0.224, s2:+0.143 |
| 3 | RF_SLOPE_POINT_M15_D2 | 318 | 320 | preventive_schedule | 0.292 | 12.59 | 12.59 | s4:+0.257, s11:+0.224, s2:+0.143 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 302 | 303 | preventive_schedule | 0.486 | 44.78 | 14.27 | s4:+0.194, s11:+0.182, s2:+0.102 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 302 | 304 | preventive_schedule | 0.486 | 44.78 | 14.27 | s4:+0.194, s11:+0.182, s2:+0.102 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.978 | indefinido | indefinido | s11:+0.029, s4:-0.011, s13:+0.004 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.977 | indefinido | indefinido | s11:+0.032, s4:-0.015, s2:+0.006 |
| 3 | HI_MARKER_D1 | 302 | 303 | preventive_schedule | 0.486 | indefinido | indefinido | s4:+0.194, s11:+0.182, s2:+0.102 |
| 3 | HI_MARKER_D2 | 302 | 304 | preventive_schedule | 0.486 | indefinido | indefinido | s4:+0.194, s11:+0.182, s2:+0.102 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=298, A=298.
- Repetição2: G=307, A=307.
- Repetição3: G=302, A=302.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.53 | 0.46 | 0.00% | 18.75% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.53 | 0.46 | 0.00% | 18.75% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.53 | 0.44 | 0.00% | 15.62% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.53 | 0.44 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.81 | 0.54 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.94 | 0.56 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 22.97 | 15 | 2.59 | 0.44 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 22.97 | 15 | 2.53 | 0.46 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.28 | 0.44 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.28 | 0.56 | 0.00% | 15.62% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.25 | 15 | 2.59 | 0.46 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.25 | 15 | 2.59 | 0.46 | 0.00% | 18.75% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.53 | 0.46 | 0.00% | 18.75% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.53 | 0.46 | 0.00% | 18.75% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.23 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.23 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.03 | 0.07 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.03 | 0.07 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.57 | 0.39 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.53 | 0.43 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 25.30 | 15 | 1.03 | 0.19 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 25.30 | 15 | 1.03 | 0.19 | 0.00% | 13.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.24 | 0.43 | 3.33% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.59 | 0.52 | 3.33% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 34.21 | 15 | 0.67 | 0.52 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 34.21 | 15 | 0.63 | 0.21 | 0.00% | 36.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.03 | 0.19 | 0.00% | 13.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.03 | 0.19 | 0.00% | 13.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.50 | 0.56 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.50 | 0.56 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.50 | 0.26 | 0.00% | 10.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.50 | 0.42 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.07 | 0.57 | 6.67% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.11 | 0.58 | 6.67% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 24.10 | 15 | 2.50 | 0.56 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 24.10 | 15 | 2.50 | 0.56 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.40 | 1.70 | 0.00% | 10.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.83 | 1.96 | 0.00% | 6.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 30.51 | 15 | 2.50 | 0.57 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 30.51 | 15 | 2.53 | 0.57 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.50 | 0.56 | 0.00% | 16.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.50 | 0.56 | 0.00% | 16.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
