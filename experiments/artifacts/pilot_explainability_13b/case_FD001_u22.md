# FD001, motor22 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u22.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 199 | 200 | preventive_schedule | 0.286 | indefinido | indefinido | s7:+0.154, s20:+0.127, s12:+0.111 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 199 | 201 | preventive_schedule | 0.286 | indefinido | indefinido | s7:+0.154, s20:+0.127, s12:+0.111 |
| 1 | HI_WAIT_SELECTED_D1 | 189 | 190 | preventive_schedule | 0.396 | indefinido | indefinido | s7:+0.143, s20:+0.110, s12:+0.086 |
| 1 | HI_WAIT_SELECTED_D2 | 189 | 191 | preventive_schedule | 0.396 | indefinido | indefinido | s7:+0.143, s20:+0.110, s12:+0.086 |
| 1 | ISO_POINT_M15_D1 | 197 | 198 | preventive_schedule | 0.305 | 16.00 | 16.00 | s7:+0.148, s20:+0.126, s12:+0.106 |
| 1 | ISO_POINT_M15_D2 | 195 | 197 | preventive_schedule | 0.323 | 16.42 | 16.42 | s7:+0.153, s20:+0.118, s12:+0.103 |
| 1 | ISO_LOWER98_M15_D1 | 179 | 180 | preventive_schedule | 0.489 | 30.20 | 15.31 | s7:+0.126, s20:+0.099, s12:+0.064 |
| 1 | ISO_LOWER98_M15_D2 | 179 | 181 | preventive_schedule | 0.489 | 30.20 | 15.31 | s7:+0.126, s20:+0.099, s12:+0.064 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.260 | 17.62 | 17.62 | s7:+0.157, s20:+0.130, s12:+0.119 |
| 1 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.260 | 17.62 | 17.62 | s7:+0.157, s20:+0.130, s12:+0.119 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 181 | 182 | preventive_schedule | 0.473 | 38.21 | 15.67 | s7:+0.134, s20:+0.094, s12:+0.068 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 180 | 182 | preventive_schedule | 0.479 | 38.67 | 16.13 | s7:+0.127, s20:+0.098, s12:+0.068 |
| 1 | AGE_D1 | 126 | 127 | preventive_schedule | 0.838 | indefinido | indefinido | s7:+0.046, s20:+0.031, s15:+0.023 |
| 1 | AGE_D2 | 125 | 127 | preventive_schedule | 0.844 | indefinido | indefinido | s7:+0.052, s20:+0.028, s15:+0.020 |
| 1 | HI_MARKER_D1 | 179 | 180 | preventive_schedule | 0.489 | indefinido | indefinido | s7:+0.126, s20:+0.099, s12:+0.064 |
| 1 | HI_MARKER_D2 | 179 | 181 | preventive_schedule | 0.489 | indefinido | indefinido | s7:+0.126, s20:+0.099, s12:+0.064 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 189 | 190 | preventive_schedule | 0.386 | indefinido | indefinido | s12:+0.152, s8:+0.079, s7:+0.079 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 189 | 191 | preventive_schedule | 0.386 | indefinido | indefinido | s12:+0.152, s8:+0.079, s7:+0.079 |
| 2 | HI_WAIT_SELECTED_D1 | 190 | 191 | preventive_schedule | 0.368 | indefinido | indefinido | s12:+0.159, s7:+0.081, s15:+0.081 |
| 2 | HI_WAIT_SELECTED_D2 | 185 | 187 | preventive_schedule | 0.432 | indefinido | indefinido | s12:+0.131, s15:+0.082, s7:+0.076 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.229 | 19.48 | 19.48 | s12:+0.210, s4:+0.098, s8:+0.091 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.229 | 19.48 | 19.48 | s12:+0.210, s4:+0.098, s8:+0.091 |
| 2 | ISO_LOWER98_M15_D1 | 180 | 181 | preventive_schedule | 0.491 | 37.27 | 14.43 | s12:+0.120, s7:+0.070, s8:+0.069 |
| 2 | ISO_LOWER98_M15_D2 | 180 | 182 | preventive_schedule | 0.491 | 37.27 | 14.43 | s12:+0.120, s7:+0.070, s8:+0.069 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.229 | 22.33 | 22.33 | s12:+0.210, s4:+0.098, s8:+0.091 |
| 2 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.229 | 22.33 | 22.33 | s12:+0.210, s4:+0.098, s8:+0.091 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 180 | 181 | preventive_schedule | 0.491 | 35.70 | 2.87 | s12:+0.120, s7:+0.070, s8:+0.069 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 180 | 182 | preventive_schedule | 0.491 | 35.70 | 2.87 | s12:+0.120, s7:+0.070, s8:+0.069 |
| 2 | AGE_D1 | 133 | 134 | preventive_schedule | 0.806 | indefinido | indefinido | s15:+0.035, s8:+0.027, s12:+0.027 |
| 2 | AGE_D2 | 132 | 134 | preventive_schedule | 0.810 | indefinido | indefinido | s15:+0.032, s7:+0.029, s8:+0.028 |
| 2 | HI_MARKER_D1 | 180 | 181 | preventive_schedule | 0.491 | indefinido | indefinido | s12:+0.120, s7:+0.070, s8:+0.069 |
| 2 | HI_MARKER_D2 | 180 | 182 | preventive_schedule | 0.491 | indefinido | indefinido | s12:+0.120, s7:+0.070, s8:+0.069 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 191 | 192 | preventive_schedule | 0.276 | indefinido | indefinido | s7:+0.174, s12:+0.114, s20:+0.098 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 191 | 193 | preventive_schedule | 0.276 | indefinido | indefinido | s7:+0.174, s12:+0.114, s20:+0.098 |
| 3 | HI_WAIT_SELECTED_D1 | 181 | 182 | preventive_schedule | 0.398 | indefinido | indefinido | s7:+0.157, s12:+0.082, s2:+0.081 |
| 3 | HI_WAIT_SELECTED_D2 | 181 | 183 | preventive_schedule | 0.398 | indefinido | indefinido | s7:+0.157, s12:+0.082, s2:+0.081 |
| 3 | ISO_POINT_M15_D1 | 199 | 200 | preventive_schedule | 0.197 | 15.20 | 15.20 | s7:+0.180, s12:+0.134, s20:+0.107 |
| 3 | ISO_POINT_M15_D2 | 197 | 199 | preventive_schedule | 0.217 | 16.70 | 16.70 | s7:+0.172, s12:+0.128, s20:+0.107 |
| 3 | ISO_LOWER98_M15_D1 | 171 | 172 | preventive_schedule | 0.487 | 35.42 | 15.00 | s7:+0.130, s12:+0.073, s2:+0.073 |
| 3 | ISO_LOWER98_M15_D2 | 171 | 173 | preventive_schedule | 0.487 | 35.42 | 15.00 | s7:+0.130, s12:+0.073, s2:+0.073 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.167 | 18.70 | 18.70 | s7:+0.183, s12:+0.143, s20:+0.110 |
| 3 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.167 | 18.70 | 18.70 | s7:+0.183, s12:+0.143, s20:+0.110 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 171 | 172 | preventive_schedule | 0.487 | 38.60 | 13.00 | s7:+0.130, s12:+0.073, s2:+0.073 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 171 | 173 | preventive_schedule | 0.487 | 38.60 | 13.00 | s7:+0.130, s12:+0.073, s2:+0.073 |
| 3 | AGE_D1 | 135 | 136 | preventive_schedule | 0.745 | indefinido | indefinido | s7:+0.062, s15:+0.044, s2:+0.035 |
| 3 | AGE_D2 | 134 | 136 | preventive_schedule | 0.760 | indefinido | indefinido | s7:+0.062, s15:+0.040, s2:+0.033 |
| 3 | HI_MARKER_D1 | 171 | 172 | preventive_schedule | 0.487 | indefinido | indefinido | s7:+0.130, s12:+0.073, s2:+0.073 |
| 3 | HI_MARKER_D2 | 171 | 173 | preventive_schedule | 0.487 | indefinido | indefinido | s7:+0.130, s12:+0.073, s2:+0.073 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=179, A=179.
- Repetição2: G=180, A=180.
- Repetição3: G=171, A=171.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.68 | 0.88 | 6.67% | 20.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.68 | 0.88 | 6.67% | 20.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.17 | 0.10 | 0.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.17 | 0.10 | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.71 | 0.53 | 6.67% | 36.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.07 | 0.60 | 0.00% | 33.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 14.89 | 15 | 2.17 | 0.43 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 14.89 | 15 | 2.17 | 0.43 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 23.33% | 40.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 23.33% | 40.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 22.54 | 15 | 2.03 | 1.37 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 22.54 | 15 | 2.00 | 1.00 | 0.00% | 36.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.17 | 0.52 | 0.00% | 23.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.17 | 0.52 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.27 | 0.50 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.27 | 0.50 | 0.00% | 20.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.30 | 0.00 | 0.00% | 3.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.30 | 0.16 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 20.00% | 6.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 22.84 | 15 | 1.30 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 22.84 | 15 | 1.30 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 20.00% | 3.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 23.33% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 32.84 | 15 | 1.30 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 32.84 | 15 | 1.30 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.30 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.30 | 0.35 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.53 | 0.60 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.53 | 0.60 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.60 | 0.17 | 0.00% | 0.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.60 | 0.17 | 0.00% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.44 | 0.58 | 16.67% | 36.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.96 | 0.64 | 6.67% | 26.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 20.42 | 15 | 2.63 | 0.65 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 20.42 | 15 | 2.63 | 0.65 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 23.33% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 33.33% | 30.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 25.60 | 15 | 2.60 | 0.74 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 25.60 | 15 | 2.60 | 0.74 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.60 | 0.74 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.60 | 0.74 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
