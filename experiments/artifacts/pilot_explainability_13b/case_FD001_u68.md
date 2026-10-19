# FD001, motor68 — diagnóstico retrospectivo

Critérios de inclusão: median_discordance_d1, median_discordance_d2.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u68.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 182 | 183 | preventive_schedule | 0.298 | indefinido | indefinido | s12:+0.128, s21:+0.094, s2:+0.090 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.298 | indefinido | indefinido | s12:+0.128, s21:+0.094, s2:+0.090 |
| 1 | HI_WAIT_SELECTED_D1 | 175 | 176 | preventive_schedule | 0.392 | indefinido | indefinido | s12:+0.118, s2:+0.088, s21:+0.075 |
| 1 | HI_WAIT_SELECTED_D2 | 175 | 177 | preventive_schedule | 0.392 | indefinido | indefinido | s12:+0.118, s2:+0.088, s21:+0.075 |
| 1 | ISO_POINT_M15_D1 | 188 | 189 | preventive_schedule | 0.169 | 13.18 | 13.18 | s12:+0.151, s2:+0.126, s21:+0.104 |
| 1 | ISO_POINT_M15_D2 | 188 | 190 | preventive_schedule | 0.169 | 13.18 | 13.18 | s12:+0.151, s2:+0.126, s21:+0.104 |
| 1 | ISO_LOWER98_M15_D1 | 166 | 167 | preventive_schedule | 0.488 | 39.24 | 13.63 | s12:+0.112, s2:+0.095, s21:+0.060 |
| 1 | ISO_LOWER98_M15_D2 | 166 | 168 | preventive_schedule | 0.488 | 39.24 | 13.63 | s12:+0.112, s2:+0.095, s21:+0.060 |
| 1 | RF_SLOPE_POINT_M15_D1 | 181 | 182 | preventive_schedule | 0.301 | 15.65 | 15.65 | s12:+0.126, s2:+0.094, s21:+0.091 |
| 1 | RF_SLOPE_POINT_M15_D2 | 180 | 182 | preventive_schedule | 0.317 | 16.78 | 16.78 | s12:+0.121, s2:+0.096, s21:+0.088 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 165 | 166 | preventive_schedule | 0.498 | 43.27 | 5.12 | s12:+0.111, s2:+0.090, s21:+0.059 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 165 | 167 | preventive_schedule | 0.498 | 43.27 | 5.12 | s12:+0.111, s2:+0.090, s21:+0.059 |
| 1 | AGE_D1 | 135 | 136 | preventive_schedule | 0.721 | indefinido | indefinido | s12:+0.060, s2:+0.044, s21:+0.034 |
| 1 | AGE_D2 | 134 | 136 | preventive_schedule | 0.732 | indefinido | indefinido | s12:+0.060, s2:+0.033, s7:+0.033 |
| 1 | HI_MARKER_D1 | 165 | 166 | preventive_schedule | 0.498 | indefinido | indefinido | s12:+0.111, s2:+0.090, s21:+0.059 |
| 1 | HI_MARKER_D2 | 165 | 167 | preventive_schedule | 0.498 | indefinido | indefinido | s12:+0.111, s2:+0.090, s21:+0.059 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 178 | 179 | preventive_schedule | 0.300 | indefinido | indefinido | s20:+0.124, s9:+0.100, s7:+0.093 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 178 | 180 | preventive_schedule | 0.300 | indefinido | indefinido | s20:+0.124, s9:+0.100, s7:+0.093 |
| 2 | HI_WAIT_SELECTED_D1 | 173 | 174 | preventive_schedule | 0.380 | indefinido | indefinido | s20:+0.102, s9:+0.088, s7:+0.076 |
| 2 | HI_WAIT_SELECTED_D2 | 173 | 175 | preventive_schedule | 0.380 | indefinido | indefinido | s20:+0.102, s9:+0.088, s7:+0.076 |
| 2 | ISO_POINT_M15_D1 | 180 | 181 | preventive_schedule | 0.273 | 15.84 | 15.84 | s20:+0.120, s9:+0.104, s7:+0.101 |
| 2 | ISO_POINT_M15_D2 | 180 | 182 | preventive_schedule | 0.273 | 15.84 | 15.84 | s20:+0.120, s9:+0.104, s7:+0.101 |
| 2 | ISO_LOWER98_M15_D1 | 166 | 167 | preventive_schedule | 0.465 | 28.27 | 15.42 | s20:+0.086, s9:+0.071, s12:+0.062 |
| 2 | ISO_LOWER98_M15_D2 | 166 | 168 | preventive_schedule | 0.465 | 28.27 | 15.42 | s20:+0.086, s9:+0.071, s12:+0.062 |
| 2 | RF_SLOPE_POINT_M15_D1 | 182 | 183 | preventive_schedule | 0.247 | 10.40 | 10.40 | s20:+0.127, s9:+0.109, s7:+0.106 |
| 2 | RF_SLOPE_POINT_M15_D2 | 180 | 182 | preventive_schedule | 0.273 | 16.79 | 16.79 | s20:+0.120, s9:+0.104, s7:+0.101 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 163 | 164 | preventive_schedule | 0.495 | 28.15 | 5.14 | s20:+0.075, s9:+0.067, s15:+0.059 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 163 | 165 | preventive_schedule | 0.495 | 28.15 | 5.14 | s20:+0.075, s9:+0.067, s15:+0.059 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.746 | indefinido | indefinido | s20:+0.051, s7:+0.044, s15:+0.035 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.740 | indefinido | indefinido | s20:+0.051, s7:+0.046, s15:+0.037 |
| 2 | HI_MARKER_D1 | 163 | 164 | preventive_schedule | 0.495 | indefinido | indefinido | s20:+0.075, s9:+0.067, s15:+0.059 |
| 2 | HI_MARKER_D2 | 163 | 165 | preventive_schedule | 0.495 | indefinido | indefinido | s20:+0.075, s9:+0.067, s15:+0.059 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 182 | 183 | preventive_schedule | 0.292 | indefinido | indefinido | s4:+0.116, s3:+0.106, s20:+0.099 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.292 | indefinido | indefinido | s4:+0.116, s3:+0.106, s20:+0.099 |
| 3 | HI_WAIT_SELECTED_D1 | 174 | 175 | preventive_schedule | 0.397 | indefinido | indefinido | s4:+0.101, s3:+0.090, s20:+0.084 |
| 3 | HI_WAIT_SELECTED_D2 | 174 | 176 | preventive_schedule | 0.397 | indefinido | indefinido | s4:+0.101, s3:+0.090, s20:+0.084 |
| 3 | ISO_POINT_M15_D1 | 189 | 190 | preventive_schedule | 0.175 | 15.80 | 15.80 | s4:+0.136, s3:+0.129, s20:+0.115 |
| 3 | ISO_POINT_M15_D2 | 187 | 189 | preventive_schedule | 0.218 | 16.93 | 16.93 | s4:+0.127, s3:+0.117, s20:+0.105 |
| 3 | ISO_LOWER98_M15_D1 | 164 | 165 | preventive_schedule | 0.497 | 41.11 | 15.70 | s3:+0.100, s4:+0.083, s20:+0.059 |
| 3 | ISO_LOWER98_M15_D2 | 164 | 166 | preventive_schedule | 0.497 | 41.11 | 15.70 | s3:+0.100, s4:+0.083, s20:+0.059 |
| 3 | RF_SLOPE_POINT_M15_D1 | 188 | 189 | preventive_schedule | 0.187 | 13.54 | 13.54 | s4:+0.136, s3:+0.124, s20:+0.111 |
| 3 | RF_SLOPE_POINT_M15_D2 | 187 | 189 | preventive_schedule | 0.218 | 16.94 | 16.94 | s4:+0.127, s3:+0.117, s20:+0.105 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 164 | 165 | preventive_schedule | 0.497 | 43.99 | 9.10 | s3:+0.100, s4:+0.083, s20:+0.059 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 164 | 166 | preventive_schedule | 0.497 | 43.99 | 9.10 | s3:+0.100, s4:+0.083, s20:+0.059 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.779 | indefinido | indefinido | s20:+0.040, s7:+0.037, s21:+0.034 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.775 | indefinido | indefinido | s20:+0.040, s7:+0.039, s21:+0.034 |
| 3 | HI_MARKER_D1 | 164 | 165 | preventive_schedule | 0.497 | indefinido | indefinido | s3:+0.100, s4:+0.083, s20:+0.059 |
| 3 | HI_MARKER_D2 | 164 | 166 | preventive_schedule | 0.497 | indefinido | indefinido | s3:+0.100, s4:+0.083, s20:+0.059 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=165, A=165.
- Repetição2: G=163, A=163.
- Repetição3: G=164, A=164.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.47 | 0.84 | 0.00% | 36.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.47 | 0.84 | 0.00% | 36.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.77 | 0.05 | 0.00% | 26.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.77 | 0.05 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.17 | 0.21 | 0.00% | 36.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.20 | 0.19 | 0.00% | 30.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 25.61 | 15 | 1.70 | 0.82 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 25.61 | 15 | 1.70 | 0.82 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.23 | 0.07 | 0.00% | 53.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.40 | 0.10 | 0.00% | 66.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 38.16 | 15 | 1.77 | 0.58 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 38.16 | 15 | 1.77 | 0.58 | 0.00% | 36.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.77 | 0.58 | 0.00% | 36.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.77 | 0.58 | 0.00% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.63 | 0.39 | 0.00% | 40.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.63 | 0.39 | 0.00% | 40.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.90 | 0.15 | 0.00% | 13.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.90 | 0.15 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.57 | 0.50 | 0.00% | 40.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.57 | 0.50 | 0.00% | 40.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 12.84 | 15 | 1.90 | 0.90 | 0.00% | 33.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 12.84 | 15 | 1.87 | 0.95 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.53 | 2.61 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.17 | 1.67 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 23.01 | 15 | 2.00 | 0.60 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 23.01 | 15 | 2.00 | 0.60 | 0.00% | 33.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.90 | 0.60 | 0.00% | 33.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.90 | 0.60 | 0.00% | 33.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.77 | 0.73 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.77 | 0.73 | 0.00% | 26.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.13 | 0.00 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.13 | 0.00 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.43 | 0.41 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.10 | 0.38 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.41 | 15 | 2.23 | 0.61 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.41 | 15 | 2.20 | 0.61 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.50 | 0.77 | 0.00% | 13.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.63 | 0.89 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 34.89 | 15 | 2.40 | 0.35 | 0.00% | 33.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 34.89 | 15 | 2.23 | 0.35 | 0.00% | 33.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.13 | 0.60 | 0.00% | 33.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.13 | 0.60 | 0.00% | 33.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
