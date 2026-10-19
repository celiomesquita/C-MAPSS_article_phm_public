# FD003, motor15 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible, median_discordance_d1.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u15.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 191 | 192 | preventive_schedule | 0.398 | indefinido | indefinido | s11:+0.262, s2:+0.141, s4:+0.133 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 191 | 193 | preventive_schedule | 0.398 | indefinido | indefinido | s11:+0.262, s2:+0.141, s4:+0.133 |
| 1 | HI_WAIT_SELECTED_D1 | 185 | 186 | preventive_schedule | 0.440 | indefinido | indefinido | s11:+0.253, s4:+0.139, s2:+0.101 |
| 1 | HI_WAIT_SELECTED_D2 | 185 | 187 | preventive_schedule | 0.440 | indefinido | indefinido | s11:+0.253, s4:+0.139, s2:+0.101 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.249 | 22.12 | 22.12 | s11:+0.306, s4:+0.190, s2:+0.173 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.249 | 22.12 | 22.12 | s11:+0.306, s4:+0.190, s2:+0.173 |
| 1 | ISO_LOWER98_M15_D1 | 175 | 176 | preventive_schedule | 0.499 | 38.60 | 9.00 | s11:+0.208, s4:+0.135, s2:+0.098 |
| 1 | ISO_LOWER98_M15_D2 | 175 | 177 | preventive_schedule | 0.499 | 38.60 | 9.00 | s11:+0.208, s4:+0.135, s2:+0.098 |
| 1 | RF_SLOPE_POINT_M15_D1 | 201 | 202 | at_endpoint | 0.249 | 12.84 | 12.84 | s11:+0.306, s4:+0.190, s2:+0.173 |
| 1 | RF_SLOPE_POINT_M15_D2 | 200 | 202 | at_endpoint | 0.261 | 16.90 | 16.90 | s11:+0.311, s4:+0.183, s2:+0.167 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 175 | 176 | preventive_schedule | 0.499 | 23.73 | 0.00 | s11:+0.208, s4:+0.135, s2:+0.098 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 175 | 177 | preventive_schedule | 0.499 | 23.73 | 0.00 | s11:+0.208, s4:+0.135, s2:+0.098 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.684 | indefinido | indefinido | s11:+0.134, s2:+0.078, s4:+0.056 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.696 | indefinido | indefinido | s11:+0.130, s2:+0.082, s4:+0.049 |
| 1 | HI_MARKER_D1 | 175 | 176 | preventive_schedule | 0.499 | indefinido | indefinido | s11:+0.208, s4:+0.135, s2:+0.098 |
| 1 | HI_MARKER_D2 | 175 | 177 | preventive_schedule | 0.499 | indefinido | indefinido | s11:+0.208, s4:+0.135, s2:+0.098 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 182 | 183 | preventive_schedule | 0.386 | indefinido | indefinido | s11:+0.269, s4:+0.132, s15:+0.076 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.386 | indefinido | indefinido | s11:+0.269, s4:+0.132, s15:+0.076 |
| 2 | HI_WAIT_SELECTED_D1 | 181 | 182 | preventive_schedule | 0.408 | indefinido | indefinido | s11:+0.265, s4:+0.128, s15:+0.072 |
| 2 | HI_WAIT_SELECTED_D2 | 181 | 183 | preventive_schedule | 0.408 | indefinido | indefinido | s11:+0.265, s4:+0.128, s15:+0.072 |
| 2 | ISO_POINT_M15_D1 | 195 | 196 | preventive_schedule | 0.258 | 15.51 | 15.51 | s11:+0.316, s4:+0.155, s15:+0.093 |
| 2 | ISO_POINT_M15_D2 | 195 | 197 | preventive_schedule | 0.258 | 15.51 | 15.51 | s11:+0.316, s4:+0.155, s15:+0.093 |
| 2 | ISO_LOWER98_M15_D1 | 173 | 174 | preventive_schedule | 0.477 | 29.28 | 9.94 | s11:+0.232, s4:+0.114, s15:+0.059 |
| 2 | ISO_LOWER98_M15_D2 | 173 | 175 | preventive_schedule | 0.477 | 29.28 | 9.94 | s11:+0.232, s4:+0.114, s15:+0.059 |
| 2 | RF_SLOPE_POINT_M15_D1 | 196 | 197 | preventive_schedule | 0.245 | 15.74 | 15.74 | s11:+0.319, s4:+0.156, s15:+0.098 |
| 2 | RF_SLOPE_POINT_M15_D2 | 195 | 197 | preventive_schedule | 0.258 | 16.05 | 16.05 | s11:+0.316, s4:+0.155, s15:+0.093 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 171 | 172 | preventive_schedule | 0.498 | 29.87 | 0.00 | s11:+0.211, s4:+0.117, s2:+0.057 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 171 | 173 | preventive_schedule | 0.498 | 29.87 | 0.00 | s11:+0.211, s4:+0.117, s2:+0.057 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.688 | indefinido | indefinido | s11:+0.148, s4:+0.054, s2:+0.038 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.695 | indefinido | indefinido | s11:+0.143, s4:+0.047, s2:+0.040 |
| 2 | HI_MARKER_D1 | 171 | 172 | preventive_schedule | 0.498 | indefinido | indefinido | s11:+0.211, s4:+0.117, s2:+0.057 |
| 2 | HI_MARKER_D2 | 171 | 173 | preventive_schedule | 0.498 | indefinido | indefinido | s11:+0.211, s4:+0.117, s2:+0.057 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 192 | 193 | preventive_schedule | 0.287 | indefinido | indefinido | s11:+0.250, s15:+0.156, s2:+0.119 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.392 | indefinido | indefinido | s11:+0.223, s15:+0.133, s2:+0.093 |
| 3 | HI_WAIT_SELECTED_D1 | 182 | 183 | preventive_schedule | 0.392 | indefinido | indefinido | s11:+0.223, s15:+0.133, s2:+0.093 |
| 3 | HI_WAIT_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.392 | indefinido | indefinido | s11:+0.223, s15:+0.133, s2:+0.093 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.191 | 16.85 | 16.85 | s11:+0.280, s15:+0.167, s2:+0.145 |
| 3 | ISO_POINT_M15_D2 | 196 | 198 | preventive_schedule | 0.233 | 16.90 | 16.90 | s11:+0.264, s15:+0.170, s2:+0.128 |
| 3 | ISO_LOWER98_M15_D1 | 172 | 173 | preventive_schedule | 0.491 | 40.28 | 16.00 | s11:+0.178, s15:+0.101, s2:+0.097 |
| 3 | ISO_LOWER98_M15_D2 | 172 | 174 | preventive_schedule | 0.491 | 40.28 | 16.00 | s11:+0.178, s15:+0.101, s2:+0.097 |
| 3 | RF_SLOPE_POINT_M15_D1 | 196 | 197 | preventive_schedule | 0.233 | 15.86 | 15.86 | s11:+0.264, s15:+0.170, s2:+0.128 |
| 3 | RF_SLOPE_POINT_M15_D2 | 196 | 198 | preventive_schedule | 0.233 | 15.86 | 15.86 | s11:+0.264, s15:+0.170, s2:+0.128 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 172 | 173 | preventive_schedule | 0.491 | 41.95 | 0.00 | s11:+0.178, s15:+0.101, s2:+0.097 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 172 | 174 | preventive_schedule | 0.491 | 41.95 | 0.00 | s11:+0.178, s15:+0.101, s2:+0.097 |
| 3 | AGE_D1 | 154 | 155 | preventive_schedule | 0.631 | indefinido | indefinido | s11:+0.116, s15:+0.076, s2:+0.073 |
| 3 | AGE_D2 | 153 | 155 | preventive_schedule | 0.639 | indefinido | indefinido | s11:+0.117, s15:+0.071, s2:+0.068 |
| 3 | HI_MARKER_D1 | 172 | 173 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.178, s15:+0.101, s2:+0.097 |
| 3 | HI_MARKER_D2 | 172 | 174 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.178, s15:+0.101, s2:+0.097 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=175, A=175.
- Repetição2: G=171, A=171.
- Repetição3: G=172, A=172.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.03 | 0.46 | 0.00% | 12.50% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.03 | 0.46 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.53 | 0.07 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.53 | 0.07 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 9.38% | 3.12% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 12.50% | 9.38% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 29.60 | 15 | 2.53 | 0.63 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 29.60 | 15 | 2.53 | 0.63 | 0.00% | 15.62% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.00 | 0.54 | 6.25% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.25 | 0.46 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 63.60 | 15 | 2.53 | 0.63 | 0.00% | 15.62% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 63.60 | 15 | 2.53 | 0.63 | 0.00% | 15.62% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.53 | 0.63 | 0.00% | 15.62% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.53 | 0.63 | 0.00% | 15.62% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.80 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.80 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.00 | 0.00 | 0.00% | 20.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.00 | 0.00 | 0.00% | 20.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.14 | 0.50 | 3.33% | 26.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.14 | 0.50 | 3.33% | 26.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 19.34 | 15 | 2.00 | 0.54 | 0.00% | 20.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 19.34 | 15 | 2.00 | 0.54 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.07 | 0.57 | 3.33% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.41 | 0.55 | 3.33% | 26.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 57.58 | 15 | 2.00 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 57.58 | 15 | 2.00 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.00 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.00 | 0.41 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.62 | 0.44 | 3.33% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.10 | 0.28 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 3.37 | 0.23 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 3.37 | 0.23 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 23.33% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.19 | 0.56 | 13.33% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 24.28 | 15 | 3.37 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 24.28 | 15 | 3.37 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.23 | 0.32 | 26.67% | 26.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.23 | 0.71 | 26.67% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 54.70 | 15 | 3.30 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 54.70 | 15 | 3.30 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 3.37 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 3.37 | 0.68 | 0.00% | 16.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
