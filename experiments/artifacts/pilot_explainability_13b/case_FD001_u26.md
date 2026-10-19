# FD001, motor26 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u26.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 190 | 191 | preventive_schedule | 0.298 | indefinido | indefinido | s9:+0.117, s2:+0.107, s12:+0.087 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.400 | indefinido | indefinido | s9:+0.093, s2:+0.091, s12:+0.073 |
| 1 | HI_WAIT_SELECTED_D1 | 185 | 186 | preventive_schedule | 0.359 | indefinido | indefinido | s9:+0.103, s2:+0.101, s12:+0.080 |
| 1 | HI_WAIT_SELECTED_D2 | 185 | 187 | preventive_schedule | 0.359 | indefinido | indefinido | s9:+0.103, s2:+0.101, s12:+0.080 |
| 1 | ISO_POINT_M15_D1 | 197 | 198 | preventive_schedule | 0.164 | 14.22 | 14.22 | s9:+0.142, s2:+0.128, s12:+0.096 |
| 1 | ISO_POINT_M15_D2 | 197 | 199 | at_endpoint | 0.164 | 14.22 | 14.22 | s9:+0.142, s2:+0.128, s12:+0.096 |
| 1 | ISO_LOWER98_M15_D1 | 177 | 178 | preventive_schedule | 0.472 | 35.56 | 14.00 | s9:+0.083, s2:+0.070, s21:+0.062 |
| 1 | ISO_LOWER98_M15_D2 | 175 | 177 | preventive_schedule | 0.496 | 38.13 | 16.57 | s9:+0.078, s2:+0.068, s12:+0.062 |
| 1 | RF_SLOPE_POINT_M15_D1 | 184 | 185 | preventive_schedule | 0.365 | 15.64 | 15.64 | s9:+0.100, s2:+0.099, s12:+0.078 |
| 1 | RF_SLOPE_POINT_M15_D2 | 184 | 186 | preventive_schedule | 0.365 | 15.64 | 15.64 | s9:+0.100, s2:+0.099, s12:+0.078 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 175 | 176 | preventive_schedule | 0.496 | 35.50 | 0.00 | s9:+0.078, s2:+0.068, s12:+0.062 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 175 | 177 | preventive_schedule | 0.496 | 35.50 | 0.00 | s9:+0.078, s2:+0.068, s12:+0.062 |
| 1 | AGE_D1 | 133 | 134 | preventive_schedule | 0.827 | indefinido | indefinido | s2:+0.033, s9:+0.026, s21:+0.020 |
| 1 | AGE_D2 | 132 | 134 | preventive_schedule | 0.837 | indefinido | indefinido | s2:+0.034, s9:+0.025, s12:+0.019 |
| 1 | HI_MARKER_D1 | 175 | 176 | preventive_schedule | 0.496 | indefinido | indefinido | s9:+0.078, s2:+0.068, s12:+0.062 |
| 1 | HI_MARKER_D2 | 175 | 177 | preventive_schedule | 0.496 | indefinido | indefinido | s9:+0.078, s2:+0.068, s12:+0.062 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 184 | 185 | preventive_schedule | 0.289 | indefinido | indefinido | s2:+0.125, s9:+0.121, s4:+0.105 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 184 | 186 | preventive_schedule | 0.289 | indefinido | indefinido | s2:+0.125, s9:+0.121, s4:+0.105 |
| 2 | HI_WAIT_SELECTED_D1 | 180 | 181 | preventive_schedule | 0.354 | indefinido | indefinido | s9:+0.108, s2:+0.106, s4:+0.101 |
| 2 | HI_WAIT_SELECTED_D2 | 180 | 182 | preventive_schedule | 0.354 | indefinido | indefinido | s9:+0.108, s2:+0.106, s4:+0.101 |
| 2 | ISO_POINT_M15_D1 | 195 | 196 | preventive_schedule | 0.118 | 13.63 | 13.63 | s9:+0.163, s2:+0.152, s4:+0.131 |
| 2 | ISO_POINT_M15_D2 | 195 | 197 | preventive_schedule | 0.118 | 13.63 | 13.63 | s9:+0.163, s2:+0.152, s4:+0.131 |
| 2 | ISO_LOWER98_M15_D1 | 170 | 171 | preventive_schedule | 0.496 | 43.05 | 14.45 | s4:+0.091, s9:+0.081, s2:+0.077 |
| 2 | ISO_LOWER98_M15_D2 | 170 | 172 | preventive_schedule | 0.496 | 43.05 | 14.45 | s4:+0.091, s9:+0.081, s2:+0.077 |
| 2 | RF_SLOPE_POINT_M15_D1 | 188 | 189 | preventive_schedule | 0.228 | 14.92 | 14.92 | s2:+0.137, s9:+0.136, s4:+0.112 |
| 2 | RF_SLOPE_POINT_M15_D2 | 187 | 189 | preventive_schedule | 0.243 | 16.01 | 16.01 | s2:+0.139, s9:+0.133, s15:+0.111 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 170 | 171 | preventive_schedule | 0.496 | 48.82 | 7.45 | s4:+0.091, s9:+0.081, s2:+0.077 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 170 | 172 | preventive_schedule | 0.496 | 48.82 | 7.45 | s4:+0.091, s9:+0.081, s2:+0.077 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.812 | indefinido | indefinido | s2:+0.041, s15:+0.034, s4:+0.028 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.817 | indefinido | indefinido | s2:+0.040, s15:+0.035, s4:+0.026 |
| 2 | HI_MARKER_D1 | 170 | 171 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.091, s9:+0.081, s2:+0.077 |
| 2 | HI_MARKER_D2 | 170 | 172 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.091, s9:+0.081, s2:+0.077 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 181 | 182 | preventive_schedule | 0.390 | indefinido | indefinido | s9:+0.159, s4:+0.117, s2:+0.095 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 181 | 183 | preventive_schedule | 0.390 | indefinido | indefinido | s9:+0.159, s4:+0.117, s2:+0.095 |
| 3 | HI_WAIT_SELECTED_D1 | 184 | 185 | preventive_schedule | 0.344 | indefinido | indefinido | s9:+0.176, s4:+0.123, s2:+0.105 |
| 3 | HI_WAIT_SELECTED_D2 | 179 | 181 | preventive_schedule | 0.412 | indefinido | indefinido | s9:+0.152, s4:+0.119, s2:+0.091 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.124 | 16.83 | 16.83 | s9:+0.255, s4:+0.157, s2:+0.132 |
| 3 | ISO_POINT_M15_D2 | 196 | 198 | preventive_schedule | 0.160 | 16.83 | 16.83 | s9:+0.244, s4:+0.157, s2:+0.126 |
| 3 | ISO_LOWER98_M15_D1 | 174 | 175 | preventive_schedule | 0.495 | 40.76 | 15.00 | s9:+0.131, s4:+0.110, s2:+0.072 |
| 3 | ISO_LOWER98_M15_D2 | 174 | 176 | preventive_schedule | 0.495 | 40.76 | 15.00 | s9:+0.131, s4:+0.110, s2:+0.072 |
| 3 | RF_SLOPE_POINT_M15_D1 | 185 | 186 | preventive_schedule | 0.340 | 15.71 | 15.71 | s9:+0.181, s4:+0.120, s2:+0.107 |
| 3 | RF_SLOPE_POINT_M15_D2 | 183 | 185 | preventive_schedule | 0.354 | 16.61 | 16.61 | s9:+0.169, s4:+0.126, s2:+0.104 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 174 | 175 | preventive_schedule | 0.495 | 48.23 | 9.74 | s9:+0.131, s4:+0.110, s2:+0.072 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 174 | 176 | preventive_schedule | 0.495 | 48.23 | 9.74 | s9:+0.131, s4:+0.110, s2:+0.072 |
| 3 | AGE_D1 | 133 | 134 | preventive_schedule | 0.822 | indefinido | indefinido | s9:+0.046, s4:+0.035, s2:+0.035 |
| 3 | AGE_D2 | 132 | 134 | preventive_schedule | 0.835 | indefinido | indefinido | s9:+0.044, s2:+0.036, s4:+0.029 |
| 3 | HI_MARKER_D1 | 174 | 175 | preventive_schedule | 0.495 | indefinido | indefinido | s9:+0.131, s4:+0.110, s2:+0.072 |
| 3 | HI_MARKER_D2 | 174 | 176 | preventive_schedule | 0.495 | indefinido | indefinido | s9:+0.131, s4:+0.110, s2:+0.072 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=175, A=175.
- Repetição2: G=170, A=170.
- Repetição3: G=174, A=174.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.77 | 1.17 | 0.00% | 40.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.87 | 0.72 | 0.00% | 40.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.63 | 0.00 | 0.00% | 26.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.63 | 0.00 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.00 | 0.46 | 23.33% | 6.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.04 | 0.46 | 20.00% | 6.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 21.56 | 15 | 1.53 | 0.61 | 0.00% | 40.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 21.56 | 15 | 1.63 | 0.56 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.03 | 0.56 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.83 | 1.11 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 46.26 | 15 | 1.63 | 0.56 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 46.26 | 15 | 1.63 | 0.56 | 0.00% | 40.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.63 | 0.56 | 0.00% | 40.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.63 | 0.56 | 0.00% | 40.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.40 | 0.59 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.40 | 0.59 | 0.00% | 26.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.07 | 0.00 | 0.00% | 20.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.07 | 0.00 | 0.00% | 20.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.07 | 0.52 | 3.33% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.10 | 0.56 | 3.33% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 28.60 | 15 | 2.07 | 0.42 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 28.60 | 15 | 2.07 | 0.42 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.97 | 0.44 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.70 | 0.19 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 41.37 | 15 | 2.07 | 0.42 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 41.37 | 15 | 2.07 | 0.42 | 0.00% | 36.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.07 | 0.42 | 0.00% | 36.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.07 | 0.42 | 0.00% | 36.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.57 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.57 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.37 | 0.08 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.37 | 0.27 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 33.33% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.96 | 0.55 | 6.67% | 33.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.76 | 15 | 1.37 | 0.60 | 0.00% | 33.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.76 | 15 | 1.37 | 0.60 | 0.00% | 33.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.90 | 0.76 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.43 | 0.11 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 38.50 | 15 | 1.37 | 0.60 | 0.00% | 33.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 38.50 | 15 | 1.37 | 0.60 | 0.00% | 33.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.37 | 0.60 | 0.00% | 33.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.37 | 0.60 | 0.00% | 33.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
