# FD003, motor95 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u95.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 154 | 155 | preventive_schedule | 0.298 | indefinido | indefinido | s4:+0.200, s11:+0.159, s2:+0.152 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 154 | 156 | preventive_schedule | 0.298 | indefinido | indefinido | s4:+0.200, s11:+0.159, s2:+0.152 |
| 1 | HI_WAIT_SELECTED_D1 | 153 | 154 | preventive_schedule | 0.320 | indefinido | indefinido | s4:+0.193, s11:+0.153, s2:+0.150 |
| 1 | HI_WAIT_SELECTED_D2 | 153 | 155 | preventive_schedule | 0.320 | indefinido | indefinido | s4:+0.193, s11:+0.153, s2:+0.150 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.119 | 18.24 | 18.24 | s4:+0.240, s11:+0.207, s2:+0.180 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.119 | 18.24 | 18.24 | s4:+0.240, s11:+0.207, s2:+0.180 |
| 1 | ISO_LOWER98_M15_D1 | 146 | 147 | preventive_schedule | 0.441 | 39.52 | 13.62 | s4:+0.153, s2:+0.134, s11:+0.123 |
| 1 | ISO_LOWER98_M15_D2 | 145 | 147 | preventive_schedule | 0.452 | 42.46 | 16.55 | s4:+0.148, s2:+0.135, s11:+0.117 |
| 1 | RF_SLOPE_POINT_M15_D1 | 154 | 155 | preventive_schedule | 0.298 | 14.63 | 14.63 | s4:+0.200, s11:+0.159, s2:+0.152 |
| 1 | RF_SLOPE_POINT_M15_D2 | 153 | 155 | preventive_schedule | 0.320 | 16.95 | 16.95 | s4:+0.193, s11:+0.153, s2:+0.150 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 144 | 145 | preventive_schedule | 0.473 | 40.36 | 10.80 | s4:+0.144, s2:+0.124, s11:+0.113 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 144 | 146 | preventive_schedule | 0.473 | 40.36 | 10.80 | s4:+0.144, s2:+0.124, s11:+0.113 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.493 | indefinido | indefinido | s4:+0.142, s2:+0.117, s11:+0.110 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.525 | indefinido | indefinido | s4:+0.126, s11:+0.110, s2:+0.108 |
| 1 | HI_MARKER_D1 | 143 | 144 | preventive_schedule | 0.493 | indefinido | indefinido | s4:+0.142, s2:+0.117, s11:+0.110 |
| 1 | HI_MARKER_D2 | 143 | 145 | preventive_schedule | 0.493 | indefinido | indefinido | s4:+0.142, s2:+0.117, s11:+0.110 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 161 | 162 | preventive_schedule | 0.293 | indefinido | indefinido | s4:+0.311, s2:+0.145, s11:+0.129 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 161 | 163 | preventive_schedule | 0.293 | indefinido | indefinido | s4:+0.311, s2:+0.145, s11:+0.129 |
| 2 | HI_WAIT_SELECTED_D1 | 154 | 155 | preventive_schedule | 0.398 | indefinido | indefinido | s4:+0.277, s2:+0.135, s11:+0.104 |
| 2 | HI_WAIT_SELECTED_D2 | 154 | 156 | preventive_schedule | 0.398 | indefinido | indefinido | s4:+0.277, s2:+0.135, s11:+0.104 |
| 2 | ISO_POINT_M15_D1 | 162 | 163 | preventive_schedule | 0.276 | 15.84 | 15.84 | s4:+0.317, s2:+0.153, s11:+0.130 |
| 2 | ISO_POINT_M15_D2 | 161 | 163 | preventive_schedule | 0.293 | 16.73 | 16.73 | s4:+0.311, s2:+0.145, s11:+0.129 |
| 2 | ISO_LOWER98_M15_D1 | 149 | 150 | preventive_schedule | 0.494 | 34.68 | 11.48 | s4:+0.219, s2:+0.129, s11:+0.087 |
| 2 | ISO_LOWER98_M15_D2 | 149 | 151 | preventive_schedule | 0.494 | 34.68 | 11.48 | s4:+0.219, s2:+0.129, s11:+0.087 |
| 2 | RF_SLOPE_POINT_M15_D1 | 161 | 162 | preventive_schedule | 0.293 | 15.92 | 15.92 | s4:+0.311, s2:+0.145, s11:+0.129 |
| 2 | RF_SLOPE_POINT_M15_D2 | 160 | 162 | preventive_schedule | 0.312 | 16.22 | 16.22 | s4:+0.301, s2:+0.143, s11:+0.128 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 149 | 150 | preventive_schedule | 0.494 | 38.32 | 0.00 | s4:+0.219, s2:+0.129, s11:+0.087 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 149 | 151 | preventive_schedule | 0.494 | 38.32 | 0.00 | s4:+0.219, s2:+0.129, s11:+0.087 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.528 | indefinido | indefinido | s4:+0.206, s2:+0.120, s11:+0.077 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.543 | indefinido | indefinido | s4:+0.200, s2:+0.110, s11:+0.074 |
| 2 | HI_MARKER_D1 | 149 | 150 | preventive_schedule | 0.494 | indefinido | indefinido | s4:+0.219, s2:+0.129, s11:+0.087 |
| 2 | HI_MARKER_D2 | 149 | 151 | preventive_schedule | 0.494 | indefinido | indefinido | s4:+0.219, s2:+0.129, s11:+0.087 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 158 | 159 | preventive_schedule | 0.273 | indefinido | indefinido | s11:+0.279, s2:+0.118, s15:+0.117 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 153 | 155 | preventive_schedule | 0.391 | indefinido | indefinido | s11:+0.219, s2:+0.110, s15:+0.089 |
| 3 | HI_WAIT_SELECTED_D1 | 157 | 158 | preventive_schedule | 0.302 | indefinido | indefinido | s11:+0.261, s2:+0.122, s15:+0.106 |
| 3 | HI_WAIT_SELECTED_D2 | 157 | 159 | preventive_schedule | 0.302 | indefinido | indefinido | s11:+0.261, s2:+0.122, s15:+0.106 |
| 3 | ISO_POINT_M15_D1 | 165 | 166 | at_endpoint | 0.171 | 13.69 | 13.69 | s11:+0.296, s15:+0.156, s2:+0.131 |
| 3 | ISO_POINT_M15_D2 | 161 | 163 | preventive_schedule | 0.230 | 16.90 | 16.90 | s11:+0.282, s15:+0.137, s2:+0.120 |
| 3 | ISO_LOWER98_M15_D1 | 147 | 148 | preventive_schedule | 0.493 | 40.28 | 16.00 | s11:+0.179, s2:+0.097, s15:+0.084 |
| 3 | ISO_LOWER98_M15_D2 | 147 | 149 | preventive_schedule | 0.493 | 40.28 | 16.00 | s11:+0.179, s2:+0.097, s15:+0.084 |
| 3 | RF_SLOPE_POINT_M15_D1 | 158 | 159 | preventive_schedule | 0.273 | 15.18 | 15.18 | s11:+0.279, s2:+0.118, s15:+0.117 |
| 3 | RF_SLOPE_POINT_M15_D2 | 158 | 160 | preventive_schedule | 0.273 | 15.18 | 15.18 | s11:+0.279, s2:+0.118, s15:+0.117 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 147 | 148 | preventive_schedule | 0.493 | 31.12 | 0.00 | s11:+0.179, s2:+0.097, s15:+0.084 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 147 | 149 | preventive_schedule | 0.493 | 31.12 | 0.00 | s11:+0.179, s2:+0.097, s15:+0.084 |
| 3 | AGE_D1 | 154 | 155 | preventive_schedule | 0.369 | indefinido | indefinido | s11:+0.228, s2:+0.111, s15:+0.090 |
| 3 | AGE_D2 | 153 | 155 | preventive_schedule | 0.391 | indefinido | indefinido | s11:+0.219, s2:+0.110, s15:+0.089 |
| 3 | HI_MARKER_D1 | 147 | 148 | preventive_schedule | 0.493 | indefinido | indefinido | s11:+0.179, s2:+0.097, s15:+0.084 |
| 3 | HI_MARKER_D2 | 147 | 149 | preventive_schedule | 0.493 | indefinido | indefinido | s11:+0.179, s2:+0.097, s15:+0.084 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=143, A=143.
- Repetição2: G=149, A=149.
- Repetição3: G=147, A=147.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.23 | 0.14 | 0.00% | 30.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.23 | 0.14 | 0.00% | 30.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.57 | 0.00 | 0.00% | 10.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.57 | 0.00 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 23.33% | 16.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 25.91 | 15 | 1.47 | 0.48 | 0.00% | 30.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 25.91 | 15 | 1.33 | 0.42 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.27 | 0.48 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.80 | 0.58 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 29.56 | 15 | 1.47 | 0.29 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 29.56 | 15 | 1.43 | 0.29 | 0.00% | 20.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.57 | 0.35 | 0.00% | 23.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.57 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.82 | 0.29 | 6.67% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.82 | 0.29 | 6.67% | 20.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.43 | 0.36 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.43 | 0.36 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.93 | 0.36 | 6.67% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.03 | 0.48 | 3.33% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 23.20 | 15 | 1.43 | 0.62 | 0.00% | 20.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 23.20 | 15 | 1.43 | 0.62 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.62 | 1.04 | 3.33% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.76 | 1.14 | 3.33% | 3.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 40.08 | 15 | 1.43 | 0.62 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 40.08 | 15 | 1.43 | 0.62 | 0.00% | 20.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.43 | 0.62 | 0.00% | 20.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.43 | 0.62 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.27 | 0.42 | 0.00% | 13.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.27 | 0.36 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.00 | 0.31 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.00 | 0.31 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.12 | 0.58 | 16.67% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.93 | 0.48 | 10.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 24.28 | 15 | 2.00 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 24.28 | 15 | 2.00 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.53 | 0.40 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.63 | 0.56 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 54.70 | 15 | 2.00 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 54.70 | 15 | 2.00 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.00 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.00 | 0.68 | 0.00% | 16.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
