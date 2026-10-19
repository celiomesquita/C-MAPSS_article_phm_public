# FD003, motor45 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible, median_discordance_d2.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u45.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 174 | 175 | preventive_schedule | 0.499 | indefinido | indefinido | s2:+0.178, s11:+0.164, s9:+0.070 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 174 | 176 | preventive_schedule | 0.499 | indefinido | indefinido | s2:+0.178, s11:+0.164, s9:+0.070 |
| 1 | HI_WAIT_SELECTED_D1 | 179 | 180 | preventive_schedule | 0.438 | indefinido | indefinido | s11:+0.188, s2:+0.171, s9:+0.081 |
| 1 | HI_WAIT_SELECTED_D2 | 176 | 178 | preventive_schedule | 0.473 | indefinido | indefinido | s11:+0.177, s2:+0.169, s9:+0.075 |
| 1 | ISO_POINT_M15_D1 | 186 | 187 | preventive_schedule | 0.304 | 14.66 | 14.66 | s11:+0.259, s2:+0.152, s9:+0.099 |
| 1 | ISO_POINT_M15_D2 | 185 | 187 | preventive_schedule | 0.311 | 16.28 | 16.28 | s11:+0.253, s2:+0.161, s9:+0.098 |
| 1 | ISO_LOWER98_M15_D1 | 174 | 175 | preventive_schedule | 0.499 | 28.41 | 5.52 | s2:+0.178, s11:+0.164, s9:+0.070 |
| 1 | ISO_LOWER98_M15_D2 | 174 | 176 | preventive_schedule | 0.499 | 28.41 | 5.52 | s2:+0.178, s11:+0.164, s9:+0.070 |
| 1 | RF_SLOPE_POINT_M15_D1 | 185 | 186 | preventive_schedule | 0.311 | 14.20 | 14.20 | s11:+0.253, s2:+0.161, s9:+0.098 |
| 1 | RF_SLOPE_POINT_M15_D2 | 185 | 187 | preventive_schedule | 0.311 | 14.20 | 14.20 | s11:+0.253, s2:+0.161, s9:+0.098 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 174 | 175 | preventive_schedule | 0.499 | 24.17 | 0.00 | s2:+0.178, s11:+0.164, s9:+0.070 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 174 | 176 | preventive_schedule | 0.499 | 24.17 | 0.00 | s2:+0.178, s11:+0.164, s9:+0.070 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.783 | indefinido | indefinido | s11:+0.075, s2:+0.057, s9:+0.038 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.811 | indefinido | indefinido | s11:+0.070, s2:+0.049, s9:+0.036 |
| 1 | HI_MARKER_D1 | 174 | 175 | preventive_schedule | 0.499 | indefinido | indefinido | s2:+0.178, s11:+0.164, s9:+0.070 |
| 1 | HI_MARKER_D2 | 174 | 176 | preventive_schedule | 0.499 | indefinido | indefinido | s2:+0.178, s11:+0.164, s9:+0.070 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 184 | 185 | preventive_schedule | 0.400 | indefinido | indefinido | s8:+0.525, s15:-0.267, s14:+0.152 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 184 | 186 | preventive_schedule | 0.400 | indefinido | indefinido | s8:+0.525, s15:-0.267, s14:+0.152 |
| 2 | HI_WAIT_SELECTED_D1 | 187 | 188 | preventive_schedule | 0.338 | indefinido | indefinido | s8:+0.572, s15:-0.275, s14:+0.163 |
| 2 | HI_WAIT_SELECTED_D2 | 187 | 189 | preventive_schedule | 0.338 | indefinido | indefinido | s8:+0.572, s15:-0.275, s14:+0.163 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.000 | 16.02 | 16.02 | s8:+0.917, s15:-0.435, s14:+0.249 |
| 2 | ISO_POINT_M15_D2 | 202 | 204 | preventive_schedule | 0.000 | 16.02 | 16.02 | s8:+0.861, s15:-0.406, s14:+0.233 |
| 2 | ISO_LOWER98_M15_D1 | 177 | 178 | preventive_schedule | 0.495 | 87.77 | 13.72 | s8:+0.439, s15:-0.205, s14:+0.124 |
| 2 | ISO_LOWER98_M15_D2 | 177 | 179 | preventive_schedule | 0.495 | 87.77 | 13.72 | s8:+0.439, s15:-0.205, s14:+0.124 |
| 2 | RF_SLOPE_POINT_M15_D1 | 189 | 190 | preventive_schedule | 0.306 | 13.60 | 13.60 | s8:+0.592, s15:-0.279, s14:+0.169 |
| 2 | RF_SLOPE_POINT_M15_D2 | 189 | 191 | preventive_schedule | 0.306 | 13.60 | 13.60 | s8:+0.592, s15:-0.279, s14:+0.169 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 177 | 178 | preventive_schedule | 0.495 | 30.73 | 0.00 | s8:+0.439, s15:-0.205, s14:+0.124 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 177 | 179 | preventive_schedule | 0.495 | 30.73 | 0.00 | s8:+0.439, s15:-0.205, s14:+0.124 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.808 | indefinido | indefinido | s8:+0.170, s15:-0.087, s14:+0.041 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.830 | indefinido | indefinido | s8:+0.151, s15:-0.085, s14:+0.042 |
| 2 | HI_MARKER_D1 | 177 | 178 | preventive_schedule | 0.495 | indefinido | indefinido | s8:+0.439, s15:-0.205, s14:+0.124 |
| 2 | HI_MARKER_D2 | 177 | 179 | preventive_schedule | 0.495 | indefinido | indefinido | s8:+0.439, s15:-0.205, s14:+0.124 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 190 | 191 | preventive_schedule | 0.389 | indefinido | indefinido | s11:+0.295, s15:-0.194, s4:+0.181 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 190 | 192 | preventive_schedule | 0.389 | indefinido | indefinido | s11:+0.295, s15:-0.194, s4:+0.181 |
| 3 | HI_WAIT_SELECTED_D1 | 195 | 196 | preventive_schedule | 0.265 | indefinido | indefinido | s11:+0.355, s15:-0.218, s4:+0.214 |
| 3 | HI_WAIT_SELECTED_D2 | 195 | 197 | preventive_schedule | 0.265 | indefinido | indefinido | s11:+0.355, s15:-0.218, s4:+0.214 |
| 3 | ISO_POINT_M15_D1 | 198 | 199 | preventive_schedule | 0.192 | 13.47 | 13.47 | s11:+0.389, s15:-0.236, s4:+0.233 |
| 3 | ISO_POINT_M15_D2 | 198 | 200 | preventive_schedule | 0.192 | 13.47 | 13.47 | s11:+0.389, s15:-0.236, s4:+0.233 |
| 3 | ISO_LOWER98_M15_D1 | 185 | 186 | preventive_schedule | 0.483 | 35.58 | 14.03 | s11:+0.260, s15:-0.176, s4:+0.145 |
| 3 | ISO_LOWER98_M15_D2 | 185 | 187 | preventive_schedule | 0.483 | 35.58 | 14.03 | s11:+0.260, s15:-0.176, s4:+0.145 |
| 3 | RF_SLOPE_POINT_M15_D1 | 195 | 196 | preventive_schedule | 0.265 | 13.36 | 13.36 | s11:+0.355, s15:-0.218, s4:+0.214 |
| 3 | RF_SLOPE_POINT_M15_D2 | 194 | 196 | preventive_schedule | 0.297 | 16.20 | 16.20 | s11:+0.346, s15:-0.218, s4:+0.203 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 185 | 186 | preventive_schedule | 0.483 | 31.65 | 0.00 | s11:+0.260, s15:-0.176, s4:+0.145 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 185 | 187 | preventive_schedule | 0.483 | 31.65 | 0.00 | s11:+0.260, s15:-0.176, s4:+0.145 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.841 | indefinido | indefinido | s11:+0.077, s15:-0.057, s4:+0.046 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.855 | indefinido | indefinido | s11:+0.072, s15:-0.056, s13:+0.043 |
| 3 | HI_MARKER_D1 | 185 | 186 | preventive_schedule | 0.483 | indefinido | indefinido | s11:+0.260, s15:-0.176, s4:+0.145 |
| 3 | HI_MARKER_D2 | 185 | 187 | preventive_schedule | 0.483 | indefinido | indefinido | s11:+0.260, s15:-0.176, s4:+0.145 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=174, A=174.
- Repetição2: G=177, A=177.
- Repetição3: G=185, A=185.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.41 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.41 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.41 | 0.16 | 0.00% | 21.88% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.41 | 0.24 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.25 | 0.42 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.19 | 0.32 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 22.89 | 15 | 1.41 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 22.89 | 15 | 1.41 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.25 | 0.32 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.34 | 0.59 | 0.00% | 9.38% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 29.47 | 15 | 1.41 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 29.47 | 15 | 1.41 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.41 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.41 | 0.36 | 0.00% | 21.88% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.17 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.17 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.67 | 0.22 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.67 | 0.22 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.55 | 0.19 | 3.33% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 74.05 | 15 | 1.67 | 0.48 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 74.05 | 15 | 1.67 | 0.48 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.00 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.00 | 0.56 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 136.85 | 15 | 1.67 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 136.85 | 15 | 1.67 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.67 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.67 | 0.52 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.97 | 0.36 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.97 | 0.36 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.17 | 0.17 | 0.00% | 0.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.17 | 0.17 | 0.00% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.70 | 0.20 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.80 | 0.28 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 21.55 | 15 | 1.17 | 0.48 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 21.55 | 15 | 1.17 | 0.48 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.77 | 0.50 | 0.00% | 13.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.80 | 0.41 | 0.00% | 3.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 52.17 | 15 | 1.17 | 0.48 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 52.17 | 15 | 1.17 | 0.48 | 0.00% | 16.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.17 | 0.48 | 0.00% | 16.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.17 | 0.48 | 0.00% | 16.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
