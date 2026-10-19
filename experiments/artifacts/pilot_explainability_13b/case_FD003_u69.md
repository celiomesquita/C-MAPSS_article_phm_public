# FD003, motor69 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u69.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 158 | 159 | preventive_schedule | 0.399 | indefinido | indefinido | s4:+0.424, s2:+0.113, s11:+0.048 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 158 | 160 | preventive_schedule | 0.399 | indefinido | indefinido | s4:+0.424, s2:+0.113, s11:+0.048 |
| 1 | HI_WAIT_SELECTED_D1 | 154 | 155 | preventive_schedule | 0.425 | indefinido | indefinido | s4:+0.407, s2:+0.106, s11:+0.046 |
| 1 | HI_WAIT_SELECTED_D2 | 154 | 156 | preventive_schedule | 0.425 | indefinido | indefinido | s4:+0.407, s2:+0.106, s11:+0.046 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.252 | 16.61 | 16.61 | s4:+0.508, s2:+0.148, s11:+0.068 |
| 1 | ISO_POINT_M15_D2 | 168 | 170 | at_endpoint | 0.254 | 16.61 | 16.61 | s4:+0.510, s2:+0.146, s11:+0.068 |
| 1 | ISO_LOWER98_M15_D1 | 149 | 150 | preventive_schedule | 0.484 | 34.73 | 11.55 | s4:+0.364, s2:+0.096, s11:+0.043 |
| 1 | ISO_LOWER98_M15_D2 | 149 | 151 | preventive_schedule | 0.484 | 34.73 | 11.55 | s4:+0.364, s2:+0.096, s11:+0.043 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.252 | 18.96 | 18.96 | s4:+0.508, s2:+0.148, s11:+0.068 |
| 1 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.252 | 18.96 | 18.96 | s4:+0.508, s2:+0.148, s11:+0.068 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 149 | 150 | preventive_schedule | 0.484 | 40.66 | 7.43 | s4:+0.364, s2:+0.096, s11:+0.043 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 149 | 151 | preventive_schedule | 0.484 | 40.66 | 7.43 | s4:+0.364, s2:+0.096, s11:+0.043 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.561 | indefinido | indefinido | s4:+0.312, s2:+0.075, s11:+0.042 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.575 | indefinido | indefinido | s4:+0.300, s2:+0.075, s11:+0.039 |
| 1 | HI_MARKER_D1 | 149 | 150 | preventive_schedule | 0.484 | indefinido | indefinido | s4:+0.364, s2:+0.096, s11:+0.043 |
| 1 | HI_MARKER_D2 | 149 | 151 | preventive_schedule | 0.484 | indefinido | indefinido | s4:+0.364, s2:+0.096, s11:+0.043 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 154 | 155 | preventive_schedule | 0.394 | indefinido | indefinido | s4:+0.230, s2:+0.184, s11:+0.180 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 154 | 156 | preventive_schedule | 0.394 | indefinido | indefinido | s4:+0.230, s2:+0.184, s11:+0.180 |
| 2 | HI_WAIT_SELECTED_D1 | 157 | 158 | preventive_schedule | 0.379 | indefinido | indefinido | s4:+0.236, s2:+0.190, s11:+0.182 |
| 2 | HI_WAIT_SELECTED_D2 | 157 | 159 | preventive_schedule | 0.379 | indefinido | indefinido | s4:+0.236, s2:+0.190, s11:+0.182 |
| 2 | ISO_POINT_M15_D1 | 166 | 167 | preventive_schedule | 0.231 | 15.80 | 15.80 | s4:+0.267, s11:+0.253, s2:+0.237 |
| 2 | ISO_POINT_M15_D2 | 166 | 168 | preventive_schedule | 0.231 | 15.80 | 15.80 | s4:+0.267, s11:+0.253, s2:+0.237 |
| 2 | ISO_LOWER98_M15_D1 | 150 | 151 | preventive_schedule | 0.448 | 33.05 | 14.30 | s4:+0.206, s11:+0.174, s2:+0.162 |
| 2 | ISO_LOWER98_M15_D2 | 149 | 151 | preventive_schedule | 0.450 | 34.99 | 16.24 | s4:+0.206, s11:+0.167, s2:+0.167 |
| 2 | RF_SLOPE_POINT_M15_D1 | 167 | 168 | preventive_schedule | 0.207 | 14.54 | 14.54 | s4:+0.270, s11:+0.259, s2:+0.251 |
| 2 | RF_SLOPE_POINT_M15_D2 | 167 | 169 | preventive_schedule | 0.207 | 14.54 | 14.54 | s4:+0.270, s11:+0.259, s2:+0.251 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 147 | 148 | preventive_schedule | 0.486 | 39.42 | 0.00 | s4:+0.189, s11:+0.161, s2:+0.155 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 147 | 149 | preventive_schedule | 0.486 | 39.42 | 0.00 | s4:+0.189, s11:+0.161, s2:+0.155 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.521 | indefinido | indefinido | s4:+0.176, s11:+0.163, s2:+0.130 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.539 | indefinido | indefinido | s4:+0.170, s11:+0.153, s2:+0.130 |
| 2 | HI_MARKER_D1 | 147 | 148 | preventive_schedule | 0.486 | indefinido | indefinido | s4:+0.189, s11:+0.161, s2:+0.155 |
| 2 | HI_MARKER_D2 | 147 | 149 | preventive_schedule | 0.486 | indefinido | indefinido | s4:+0.189, s11:+0.161, s2:+0.155 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 159 | 160 | preventive_schedule | 0.382 | indefinido | indefinido | s4:+0.290, s11:+0.200, s2:+0.128 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 159 | 161 | preventive_schedule | 0.382 | indefinido | indefinido | s4:+0.290, s11:+0.200, s2:+0.128 |
| 3 | HI_WAIT_SELECTED_D1 | 159 | 160 | preventive_schedule | 0.382 | indefinido | indefinido | s4:+0.290, s11:+0.200, s2:+0.128 |
| 3 | HI_WAIT_SELECTED_D2 | 159 | 161 | preventive_schedule | 0.382 | indefinido | indefinido | s4:+0.290, s11:+0.200, s2:+0.128 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.237 | 20.07 | 20.07 | s4:+0.338, s11:+0.270, s2:+0.156 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.237 | 20.07 | 20.07 | s4:+0.338, s11:+0.270, s2:+0.156 |
| 3 | ISO_LOWER98_M15_D1 | 149 | 150 | preventive_schedule | 0.487 | 38.27 | 9.38 | s4:+0.242, s11:+0.170, s2:+0.101 |
| 3 | ISO_LOWER98_M15_D2 | 149 | 151 | preventive_schedule | 0.487 | 38.27 | 9.38 | s4:+0.242, s11:+0.170, s2:+0.101 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.237 | 23.55 | 23.55 | s4:+0.338, s11:+0.270, s2:+0.156 |
| 3 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.237 | 23.55 | 23.55 | s4:+0.338, s11:+0.270, s2:+0.156 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 149 | 150 | preventive_schedule | 0.487 | 32.63 | 0.00 | s4:+0.242, s11:+0.170, s2:+0.101 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 149 | 151 | preventive_schedule | 0.487 | 32.63 | 0.00 | s4:+0.242, s11:+0.170, s2:+0.101 |
| 3 | AGE_D1 | 151 | 152 | preventive_schedule | 0.474 | indefinido | indefinido | s4:+0.250, s11:+0.172, s2:+0.104 |
| 3 | AGE_D2 | 150 | 152 | preventive_schedule | 0.483 | indefinido | indefinido | s4:+0.242, s11:+0.177, s2:+0.098 |
| 3 | HI_MARKER_D1 | 149 | 150 | preventive_schedule | 0.487 | indefinido | indefinido | s4:+0.242, s11:+0.170, s2:+0.101 |
| 3 | HI_MARKER_D2 | 149 | 151 | preventive_schedule | 0.487 | indefinido | indefinido | s4:+0.242, s11:+0.170, s2:+0.101 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=149, A=149.
- Repetição2: G=147, A=147.
- Repetição3: G=149, A=149.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.13 | 0.43 | 3.12% | 12.50% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.13 | 0.43 | 3.12% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.06 | 0.13 | 3.12% | 6.25% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.06 | 0.13 | 3.12% | 6.25% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 12.50% | 6.25% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.80 | 0.30 | 6.25% | 6.25% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 23.18 | 15 | 1.53 | 0.27 | 0.00% | 6.25% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 23.18 | 15 | 1.53 | 0.27 | 0.00% | 6.25% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 18.75% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 18.75% | 18.75% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 33.23 | 15 | 1.53 | 0.27 | 0.00% | 6.25% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 33.23 | 15 | 1.53 | 0.27 | 0.00% | 6.25% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.53 | 0.27 | 0.00% | 6.25% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.53 | 0.27 | 0.00% | 6.25% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.28 | 0.31 | 0.00% | 9.38% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.28 | 0.31 | 0.00% | 9.38% | 0/32 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.47 | 0.10 | 0.00% | 3.12% | 0/32 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.47 | 0.10 | 0.00% | 3.12% | 0/32 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.70 | 0.31 | 6.25% | 9.38% | 0/32 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.70 | 0.31 | 6.25% | 9.38% | 0/32 |
| 2 | ISO_LOWER98_M15_D1 | 18.75 | 15 | 1.41 | 0.32 | 0.00% | 12.50% | 0/32 |
| 2 | ISO_LOWER98_M15_D2 | 18.75 | 15 | 1.41 | 0.18 | 0.00% | 12.50% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.31 | 0.36 | 9.38% | 12.50% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.37 | 0.36 | 6.25% | 12.50% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 42.79 | 15 | 1.47 | 0.48 | 0.00% | 9.38% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 42.79 | 15 | 1.47 | 0.48 | 0.00% | 9.38% | 0/32 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.47 | 0.48 | 0.00% | 9.38% | 0/32 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.47 | 0.48 | 0.00% | 9.38% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.38 | 0.38 | 0.00% | 9.38% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.38 | 0.38 | 0.00% | 9.38% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.53 | 0.06 | 0.00% | 3.12% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.53 | 0.06 | 0.00% | 3.12% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 9.38% | 9.38% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 9.38% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 28.89 | 15 | 1.53 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 28.89 | 15 | 1.53 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 9.38% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 9.38% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 34.95 | 15 | 1.53 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 34.95 | 15 | 1.53 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.53 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.53 | 0.24 | 0.00% | 9.38% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
