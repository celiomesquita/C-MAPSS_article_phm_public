# FD003, motor62 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u62.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 214 | 215 | preventive_schedule | 0.396 | indefinido | indefinido | s11:+0.312, s2:+0.132, s4:+0.122 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 214 | 216 | preventive_schedule | 0.396 | indefinido | indefinido | s11:+0.312, s2:+0.132, s4:+0.122 |
| 1 | HI_WAIT_SELECTED_D1 | 213 | 214 | preventive_schedule | 0.409 | indefinido | indefinido | s11:+0.300, s2:+0.132, s4:+0.122 |
| 1 | HI_WAIT_SELECTED_D2 | 208 | 210 | preventive_schedule | 0.459 | indefinido | indefinido | s11:+0.265, s2:+0.129, s4:+0.113 |
| 1 | ISO_POINT_M15_D1 | 226 | 227 | preventive_schedule | 0.181 | 15.40 | 15.40 | s11:+0.422, s4:+0.202, s2:+0.140 |
| 1 | ISO_POINT_M15_D2 | 226 | 228 | preventive_schedule | 0.181 | 15.40 | 15.40 | s11:+0.422, s4:+0.202, s2:+0.140 |
| 1 | ISO_LOWER98_M15_D1 | 203 | 204 | preventive_schedule | 0.498 | 40.20 | 9.75 | s11:+0.231, s4:+0.120, s2:+0.118 |
| 1 | ISO_LOWER98_M15_D2 | 203 | 205 | preventive_schedule | 0.498 | 40.20 | 9.75 | s11:+0.231, s4:+0.120, s2:+0.118 |
| 1 | RF_SLOPE_POINT_M15_D1 | 224 | 225 | preventive_schedule | 0.241 | 13.93 | 13.93 | s11:+0.397, s4:+0.180, s2:+0.133 |
| 1 | RF_SLOPE_POINT_M15_D2 | 224 | 226 | preventive_schedule | 0.241 | 13.93 | 13.93 | s11:+0.397, s4:+0.180, s2:+0.133 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 203 | 204 | preventive_schedule | 0.498 | 38.71 | 5.82 | s11:+0.231, s4:+0.120, s2:+0.118 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 203 | 205 | preventive_schedule | 0.498 | 38.71 | 5.82 | s11:+0.231, s4:+0.120, s2:+0.118 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.889 | indefinido | indefinido | s11:+0.051, s2:+0.030, s4:+0.023 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.882 | indefinido | indefinido | s11:+0.051, s2:+0.034, s4:+0.024 |
| 1 | HI_MARKER_D1 | 203 | 204 | preventive_schedule | 0.498 | indefinido | indefinido | s11:+0.231, s4:+0.120, s2:+0.118 |
| 1 | HI_MARKER_D2 | 203 | 205 | preventive_schedule | 0.498 | indefinido | indefinido | s11:+0.231, s4:+0.120, s2:+0.118 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 201 | 202 | preventive_schedule | 0.393 | indefinido | indefinido | s8:+0.541, s15:-0.187, s14:+0.109 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 201 | 203 | preventive_schedule | 0.393 | indefinido | indefinido | s8:+0.541, s15:-0.187, s14:+0.109 |
| 2 | HI_WAIT_SELECTED_D1 | 201 | 202 | preventive_schedule | 0.393 | indefinido | indefinido | s8:+0.541, s15:-0.187, s14:+0.109 |
| 2 | HI_WAIT_SELECTED_D2 | 201 | 203 | preventive_schedule | 0.393 | indefinido | indefinido | s8:+0.541, s15:-0.187, s14:+0.109 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.000 | 16.02 | 16.02 | s8:+1.170, s15:-0.433, s14:+0.283 |
| 2 | ISO_POINT_M15_D2 | 230 | 232 | preventive_schedule | 0.000 | 16.02 | 16.02 | s8:+0.878, s15:-0.365, s14:+0.201 |
| 2 | ISO_LOWER98_M15_D1 | 191 | 192 | preventive_schedule | 0.493 | 87.77 | 13.72 | s8:+0.460, s15:-0.149, s14:+0.091 |
| 2 | ISO_LOWER98_M15_D2 | 191 | 193 | preventive_schedule | 0.493 | 87.77 | 13.72 | s8:+0.460, s15:-0.149, s14:+0.091 |
| 2 | RF_SLOPE_POINT_M15_D1 | 223 | 224 | preventive_schedule | 0.108 | 12.54 | 12.54 | s8:+0.777, s15:-0.297, s14:+0.171 |
| 2 | RF_SLOPE_POINT_M15_D2 | 223 | 225 | preventive_schedule | 0.108 | 12.54 | 12.54 | s8:+0.777, s15:-0.297, s14:+0.171 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 191 | 192 | preventive_schedule | 0.493 | 100.58 | 0.00 | s8:+0.460, s15:-0.149, s14:+0.091 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 191 | 193 | preventive_schedule | 0.493 | 100.58 | 0.00 | s8:+0.460, s15:-0.149, s14:+0.091 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.707 | indefinido | indefinido | s8:+0.264, s15:-0.037, s14:+0.035 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.715 | indefinido | indefinido | s8:+0.257, s15:-0.039, s14:+0.033 |
| 2 | HI_MARKER_D1 | 191 | 192 | preventive_schedule | 0.493 | indefinido | indefinido | s8:+0.460, s15:-0.149, s14:+0.091 |
| 2 | HI_MARKER_D2 | 191 | 193 | preventive_schedule | 0.493 | indefinido | indefinido | s8:+0.460, s15:-0.149, s14:+0.091 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 226 | 227 | preventive_schedule | 0.268 | indefinido | indefinido | s11:+0.488, s21:-0.143, s3:+0.118 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 226 | 228 | preventive_schedule | 0.268 | indefinido | indefinido | s11:+0.488, s21:-0.143, s3:+0.118 |
| 3 | HI_WAIT_SELECTED_D1 | 220 | 221 | preventive_schedule | 0.373 | indefinido | indefinido | s11:+0.413, s21:-0.124, s3:+0.097 |
| 3 | HI_WAIT_SELECTED_D2 | 220 | 222 | preventive_schedule | 0.373 | indefinido | indefinido | s11:+0.413, s21:-0.124, s3:+0.097 |
| 3 | ISO_POINT_M15_D1 | 230 | 231 | preventive_schedule | 0.213 | 14.84 | 14.84 | s11:+0.534, s21:-0.160, s3:+0.117 |
| 3 | ISO_POINT_M15_D2 | 230 | 232 | preventive_schedule | 0.213 | 14.84 | 14.84 | s11:+0.534, s21:-0.160, s3:+0.117 |
| 3 | ISO_LOWER98_M15_D1 | 210 | 211 | preventive_schedule | 0.492 | 39.58 | 14.00 | s11:+0.327, s21:-0.101, s3:+0.073 |
| 3 | ISO_LOWER98_M15_D2 | 210 | 212 | preventive_schedule | 0.492 | 39.58 | 14.00 | s11:+0.327, s21:-0.101, s3:+0.073 |
| 3 | RF_SLOPE_POINT_M15_D1 | 227 | 228 | preventive_schedule | 0.259 | 14.09 | 14.09 | s11:+0.495, s21:-0.145, s3:+0.117 |
| 3 | RF_SLOPE_POINT_M15_D2 | 227 | 229 | preventive_schedule | 0.259 | 14.09 | 14.09 | s11:+0.495, s21:-0.145, s3:+0.117 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 210 | 211 | preventive_schedule | 0.492 | 36.43 | 5.14 | s11:+0.327, s21:-0.101, s3:+0.073 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 210 | 212 | preventive_schedule | 0.492 | 36.43 | 5.14 | s11:+0.327, s21:-0.101, s3:+0.073 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.860 | indefinido | indefinido | s11:+0.072, s8:+0.031, s3:+0.024 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.862 | indefinido | indefinido | s11:+0.063, s8:+0.031, s3:+0.027 |
| 3 | HI_MARKER_D1 | 210 | 211 | preventive_schedule | 0.492 | indefinido | indefinido | s11:+0.327, s21:-0.101, s3:+0.073 |
| 3 | HI_MARKER_D2 | 210 | 212 | preventive_schedule | 0.492 | indefinido | indefinido | s11:+0.327, s21:-0.101, s3:+0.073 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=203, A=203.
- Repetição2: G=191, A=191.
- Repetição3: G=210, A=210.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.70 | 0.50 | 0.00% | 13.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.70 | 0.50 | 0.00% | 13.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.77 | 0.23 | 0.00% | 13.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.77 | 0.38 | 0.00% | 13.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.90 | 0.08 | 0.00% | 13.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.90 | 0.08 | 0.00% | 13.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 30.46 | 15 | 1.77 | 0.50 | 0.00% | 13.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 30.46 | 15 | 1.77 | 0.50 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.40 | 0.50 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.33 | 0.50 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 32.89 | 15 | 1.77 | 0.50 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 32.89 | 15 | 1.77 | 0.50 | 0.00% | 13.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.77 | 0.50 | 0.00% | 13.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.77 | 0.50 | 0.00% | 13.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.10 | 0.56 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.10 | 0.56 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.40 | 0.11 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.40 | 0.11 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.07 | 0.40 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 74.05 | 15 | 2.43 | 0.48 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 74.05 | 15 | 2.43 | 0.48 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.20 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.20 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 136.85 | 15 | 2.40 | 0.48 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 136.85 | 15 | 2.40 | 0.48 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.40 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.40 | 0.52 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.23 | 0.43 | 0.00% | 6.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.23 | 0.43 | 0.00% | 6.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.00 | 0.15 | 0.00% | 10.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.00 | 0.15 | 0.00% | 10.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.23 | 0.46 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.27 | 0.46 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.58 | 15 | 2.00 | 0.54 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.58 | 15 | 2.00 | 0.54 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.73 | 0.35 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.67 | 0.54 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 31.29 | 15 | 1.97 | 0.54 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 31.29 | 15 | 2.00 | 0.54 | 0.00% | 20.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.00 | 0.54 | 0.00% | 20.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.00 | 0.54 | 0.00% | 20.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
