# FD001, motor73 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u73.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 207 | 208 | preventive_schedule | 0.296 | indefinido | indefinido | s7:+0.142, s20:+0.126, s15:+0.099 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 207 | 209 | preventive_schedule | 0.296 | indefinido | indefinido | s7:+0.142, s20:+0.126, s15:+0.099 |
| 1 | HI_WAIT_SELECTED_D1 | 197 | 198 | preventive_schedule | 0.423 | indefinido | indefinido | s7:+0.124, s20:+0.092, s12:+0.090 |
| 1 | HI_WAIT_SELECTED_D2 | 197 | 199 | preventive_schedule | 0.423 | indefinido | indefinido | s7:+0.124, s20:+0.092, s12:+0.090 |
| 1 | ISO_POINT_M15_D1 | 207 | 208 | preventive_schedule | 0.296 | 14.91 | 14.91 | s7:+0.142, s20:+0.126, s15:+0.099 |
| 1 | ISO_POINT_M15_D2 | 206 | 208 | preventive_schedule | 0.308 | 16.42 | 16.42 | s7:+0.139, s20:+0.128, s15:+0.096 |
| 1 | ISO_LOWER98_M15_D1 | 187 | 188 | preventive_schedule | 0.495 | 30.20 | 15.31 | s7:+0.113, s20:+0.091, s15:+0.063 |
| 1 | ISO_LOWER98_M15_D2 | 187 | 189 | preventive_schedule | 0.495 | 30.20 | 15.31 | s7:+0.113, s20:+0.091, s15:+0.063 |
| 1 | RF_SLOPE_POINT_M15_D1 | 210 | 211 | preventive_schedule | 0.263 | 15.10 | 15.10 | s7:+0.148, s20:+0.132, s15:+0.102 |
| 1 | RF_SLOPE_POINT_M15_D2 | 208 | 210 | preventive_schedule | 0.278 | 16.24 | 16.24 | s7:+0.148, s20:+0.130, s15:+0.101 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 187 | 188 | preventive_schedule | 0.495 | 33.55 | 11.01 | s7:+0.113, s20:+0.091, s15:+0.063 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 187 | 189 | preventive_schedule | 0.495 | 33.55 | 11.01 | s7:+0.113, s20:+0.091, s15:+0.063 |
| 1 | AGE_D1 | 126 | 127 | preventive_schedule | 0.843 | indefinido | indefinido | s7:+0.043, s20:+0.033, s15:+0.020 |
| 1 | AGE_D2 | 125 | 127 | preventive_schedule | 0.841 | indefinido | indefinido | s7:+0.042, s20:+0.032, s15:+0.022 |
| 1 | HI_MARKER_D1 | 187 | 188 | preventive_schedule | 0.495 | indefinido | indefinido | s7:+0.113, s20:+0.091, s15:+0.063 |
| 1 | HI_MARKER_D2 | 187 | 189 | preventive_schedule | 0.495 | indefinido | indefinido | s7:+0.113, s20:+0.091, s15:+0.063 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 185 | 186 | preventive_schedule | 0.397 | indefinido | indefinido | s2:+0.182, s15:+0.147, s21:+0.061 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 185 | 187 | preventive_schedule | 0.397 | indefinido | indefinido | s2:+0.182, s15:+0.147, s21:+0.061 |
| 2 | HI_WAIT_SELECTED_D1 | 188 | 189 | preventive_schedule | 0.385 | indefinido | indefinido | s2:+0.193, s15:+0.144, s21:+0.059 |
| 2 | HI_WAIT_SELECTED_D2 | 188 | 190 | preventive_schedule | 0.385 | indefinido | indefinido | s2:+0.193, s15:+0.144, s21:+0.059 |
| 2 | ISO_POINT_M15_D1 | 212 | 213 | at_endpoint | 0.133 | 15.00 | 15.00 | s15:+0.235, s2:+0.228, s21:+0.086 |
| 2 | ISO_POINT_M15_D2 | 208 | 210 | preventive_schedule | 0.178 | 16.57 | 16.57 | s15:+0.233, s2:+0.217, s8:+0.076 |
| 2 | ISO_LOWER98_M15_D1 | 178 | 179 | preventive_schedule | 0.494 | 37.87 | 11.00 | s2:+0.145, s15:+0.124, s21:+0.047 |
| 2 | ISO_LOWER98_M15_D2 | 178 | 180 | preventive_schedule | 0.494 | 37.87 | 11.00 | s2:+0.145, s15:+0.124, s21:+0.047 |
| 2 | RF_SLOPE_POINT_M15_D1 | 212 | 213 | at_endpoint | 0.133 | 13.77 | 13.77 | s15:+0.235, s2:+0.228, s21:+0.086 |
| 2 | RF_SLOPE_POINT_M15_D2 | 212 | 214 | late_schedule | 0.133 | 13.77 | 13.77 | s15:+0.235, s2:+0.228, s21:+0.086 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 178 | 179 | preventive_schedule | 0.494 | 30.72 | 0.00 | s2:+0.145, s15:+0.124, s21:+0.047 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 178 | 180 | preventive_schedule | 0.494 | 30.72 | 0.00 | s2:+0.145, s15:+0.124, s21:+0.047 |
| 2 | AGE_D1 | 135 | 136 | preventive_schedule | 0.768 | indefinido | indefinido | s2:+0.062, s15:+0.050, s17:+0.034 |
| 2 | AGE_D2 | 134 | 136 | preventive_schedule | 0.767 | indefinido | indefinido | s15:+0.060, s2:+0.055, s17:+0.034 |
| 2 | HI_MARKER_D1 | 178 | 179 | preventive_schedule | 0.494 | indefinido | indefinido | s2:+0.145, s15:+0.124, s21:+0.047 |
| 2 | HI_MARKER_D2 | 178 | 180 | preventive_schedule | 0.494 | indefinido | indefinido | s2:+0.145, s15:+0.124, s21:+0.047 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 198 | 199 | preventive_schedule | 0.393 | indefinido | indefinido | s15:+0.089, s21:+0.083, s7:+0.082 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 198 | 200 | preventive_schedule | 0.393 | indefinido | indefinido | s15:+0.089, s21:+0.083, s7:+0.082 |
| 3 | HI_WAIT_SELECTED_D1 | 187 | 188 | preventive_schedule | 0.469 | indefinido | indefinido | s21:+0.080, s15:+0.079, s7:+0.074 |
| 3 | HI_WAIT_SELECTED_D2 | 187 | 189 | preventive_schedule | 0.469 | indefinido | indefinido | s21:+0.080, s15:+0.079, s7:+0.074 |
| 3 | ISO_POINT_M15_D1 | 212 | 213 | at_endpoint | 0.209 | 13.91 | 13.91 | s15:+0.128, s21:+0.121, s7:+0.101 |
| 3 | ISO_POINT_M15_D2 | 212 | 214 | late_schedule | 0.209 | 13.91 | 13.91 | s15:+0.128, s21:+0.121, s7:+0.101 |
| 3 | ISO_LOWER98_M15_D1 | 182 | 183 | preventive_schedule | 0.494 | 34.05 | 13.00 | s21:+0.080, s7:+0.072, s15:+0.072 |
| 3 | ISO_LOWER98_M15_D2 | 182 | 184 | preventive_schedule | 0.494 | 34.05 | 13.00 | s21:+0.080, s7:+0.072, s15:+0.072 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.209 | 24.38 | 24.38 | s15:+0.128, s21:+0.121, s7:+0.101 |
| 3 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.209 | 24.38 | 24.38 | s15:+0.128, s21:+0.121, s7:+0.101 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 182 | 183 | preventive_schedule | 0.494 | 27.65 | 0.00 | s21:+0.080, s7:+0.072, s15:+0.072 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 182 | 184 | preventive_schedule | 0.494 | 27.65 | 0.00 | s21:+0.080, s7:+0.072, s15:+0.072 |
| 3 | AGE_D1 | 133 | 134 | preventive_schedule | 0.812 | indefinido | indefinido | s15:+0.033, s7:+0.026, s21:+0.023 |
| 3 | AGE_D2 | 132 | 134 | preventive_schedule | 0.825 | indefinido | indefinido | s15:+0.032, s7:+0.026, s21:+0.020 |
| 3 | HI_MARKER_D1 | 182 | 183 | preventive_schedule | 0.494 | indefinido | indefinido | s21:+0.080, s7:+0.072, s15:+0.072 |
| 3 | HI_MARKER_D2 | 182 | 184 | preventive_schedule | 0.494 | indefinido | indefinido | s21:+0.080, s7:+0.072, s15:+0.072 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=187, A=187.
- Repetição2: G=178, A=178.
- Repetição3: G=182, A=182.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.53 | 0.45 | 0.00% | 33.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.53 | 0.45 | 0.00% | 33.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 3.53 | 0.16 | 0.00% | 16.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 3.53 | 0.16 | 0.00% | 16.67% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.57 | 0.65 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.63 | 0.88 | 0.00% | 16.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 14.89 | 15 | 3.43 | 1.30 | 0.00% | 33.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 14.89 | 15 | 3.47 | 1.45 | 0.00% | 33.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.07 | 1.24 | 0.00% | 16.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.23 | 0.67 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 22.54 | 15 | 4.47 | 1.58 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 22.54 | 15 | 4.03 | 1.50 | 0.00% | 33.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 3.53 | 1.48 | 0.00% | 30.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 3.53 | 1.48 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.93 | 0.58 | 0.00% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.93 | 0.58 | 0.00% | 36.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.90 | 0.00 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.90 | 0.00 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.12 | 0.67 | 20.00% | 20.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.14 | 0.38 | 6.67% | 13.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 26.87 | 15 | 1.90 | 0.68 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 26.87 | 15 | 1.90 | 0.68 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.00 | 0.68 | 3.33% | 36.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.00 | 0.75 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 35.90 | 15 | 1.90 | 0.68 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 35.90 | 15 | 1.90 | 0.68 | 0.00% | 26.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.90 | 0.68 | 0.00% | 26.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.90 | 0.68 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.77 | 1.30 | 0.00% | 33.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.77 | 1.30 | 0.00% | 33.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.07 | 0.41 | 0.00% | 26.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.07 | 0.41 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.21 | 0.63 | 36.67% | 36.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.26 | 0.68 | 36.67% | 36.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 21.05 | 15 | 2.07 | 0.80 | 0.00% | 33.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 21.05 | 15 | 2.07 | 0.80 | 0.00% | 33.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 6.67% | 26.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 29.95 | 15 | 2.07 | 0.80 | 0.00% | 33.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 29.95 | 15 | 2.07 | 0.80 | 0.00% | 33.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.07 | 0.80 | 0.00% | 33.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.07 | 0.80 | 0.00% | 33.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
