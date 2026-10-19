# FD003, motor67 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u67.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 222 | 223 | preventive_schedule | 0.291 | indefinido | indefinido | s11:+0.520, s15:+0.059, s2:+0.049 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 214 | 216 | preventive_schedule | 0.386 | indefinido | indefinido | s11:+0.453, s15:+0.050, s2:+0.043 |
| 1 | HI_WAIT_SELECTED_D1 | 204 | 205 | preventive_schedule | 0.404 | indefinido | indefinido | s11:+0.444, s15:+0.053, s2:+0.042 |
| 1 | HI_WAIT_SELECTED_D2 | 204 | 206 | preventive_schedule | 0.404 | indefinido | indefinido | s11:+0.444, s15:+0.053, s2:+0.042 |
| 1 | ISO_POINT_M15_D1 | 238 | 239 | preventive_schedule | 0.121 | 15.94 | 15.94 | s11:+0.631, s15:+0.097, s2:+0.051 |
| 1 | ISO_POINT_M15_D2 | 238 | 240 | preventive_schedule | 0.121 | 15.94 | 15.94 | s11:+0.631, s15:+0.097, s2:+0.051 |
| 1 | ISO_LOWER98_M15_D1 | 194 | 195 | preventive_schedule | 0.493 | 44.16 | 11.00 | s11:+0.372, s15:+0.057, s2:+0.029 |
| 1 | ISO_LOWER98_M15_D2 | 194 | 196 | preventive_schedule | 0.493 | 44.16 | 11.00 | s11:+0.372, s15:+0.057, s2:+0.029 |
| 1 | RF_SLOPE_POINT_M15_D1 | 221 | 222 | preventive_schedule | 0.306 | 13.35 | 13.35 | s11:+0.509, s15:+0.058, s2:+0.049 |
| 1 | RF_SLOPE_POINT_M15_D2 | 221 | 223 | preventive_schedule | 0.306 | 13.35 | 13.35 | s11:+0.509, s15:+0.058, s2:+0.049 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 197 | 198 | preventive_schedule | 0.459 | 45.31 | 11.22 | s11:+0.395, s15:+0.053, s2:+0.040 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 197 | 199 | preventive_schedule | 0.459 | 45.31 | 11.22 | s11:+0.395, s15:+0.053, s2:+0.040 |
| 1 | AGE_D1 | 145 | 146 | preventive_schedule | 0.721 | indefinido | indefinido | s11:+0.229, s15:+0.017, s8:+0.013 |
| 1 | AGE_D2 | 144 | 146 | preventive_schedule | 0.705 | indefinido | indefinido | s11:+0.247, s15:+0.017, s8:+0.011 |
| 1 | HI_MARKER_D1 | 194 | 195 | preventive_schedule | 0.493 | indefinido | indefinido | s11:+0.372, s15:+0.057, s2:+0.029 |
| 1 | HI_MARKER_D2 | 194 | 196 | preventive_schedule | 0.493 | indefinido | indefinido | s11:+0.372, s15:+0.057, s2:+0.029 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 225 | 226 | preventive_schedule/escolha interna inviável | 0.385 | indefinido | indefinido | s8:+0.239, s15:+0.142, s4:+0.105 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 225 | 227 | preventive_schedule/escolha interna inviável | 0.385 | indefinido | indefinido | s8:+0.239, s15:+0.142, s4:+0.105 |
| 2 | HI_WAIT_SELECTED_D1 | 222 | 223 | preventive_schedule/escolha interna inviável | 0.433 | indefinido | indefinido | s8:+0.214, s15:+0.120, s4:+0.097 |
| 2 | HI_WAIT_SELECTED_D2 | 222 | 224 | preventive_schedule/escolha interna inviável | 0.433 | indefinido | indefinido | s8:+0.214, s15:+0.120, s4:+0.097 |
| 2 | ISO_POINT_M15_D1 | 241 | 242 | preventive_schedule | 0.221 | 15.52 | 15.52 | s8:+0.305, s15:+0.191, s4:+0.116 |
| 2 | ISO_POINT_M15_D2 | 241 | 243 | preventive_schedule | 0.221 | 15.52 | 15.52 | s8:+0.305, s15:+0.191, s4:+0.116 |
| 2 | ISO_LOWER98_M15_D1 | 217 | 218 | preventive_schedule | 0.490 | 37.21 | 11.91 | s8:+0.187, s15:+0.103, s4:+0.097 |
| 2 | ISO_LOWER98_M15_D2 | 217 | 219 | preventive_schedule | 0.490 | 37.21 | 11.91 | s8:+0.187, s15:+0.103, s4:+0.097 |
| 2 | RF_SLOPE_POINT_M15_D1 | 252 | 253 | preventive_schedule | 0.160 | 14.42 | 14.42 | s8:+0.321, s15:+0.195, s4:+0.139 |
| 2 | RF_SLOPE_POINT_M15_D2 | 251 | 253 | preventive_schedule | 0.161 | 16.86 | 16.86 | s8:+0.325, s15:+0.194, s4:+0.138 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 222 | 223 | preventive_schedule | 0.433 | 47.85 | 13.64 | s8:+0.214, s15:+0.120, s4:+0.097 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 222 | 224 | preventive_schedule | 0.433 | 47.85 | 13.64 | s8:+0.214, s15:+0.120, s4:+0.097 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.811 | indefinido | indefinido | s8:+0.073, s15:+0.035, s4:+0.033 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.817 | indefinido | indefinido | s8:+0.066, s15:+0.034, s4:+0.033 |
| 2 | HI_MARKER_D1 | 217 | 218 | preventive_schedule | 0.490 | indefinido | indefinido | s8:+0.187, s15:+0.103, s4:+0.097 |
| 2 | HI_MARKER_D2 | 217 | 219 | preventive_schedule | 0.490 | indefinido | indefinido | s8:+0.187, s15:+0.103, s4:+0.097 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 222 | 223 | preventive_schedule | 0.291 | indefinido | indefinido | s11:+0.397, s21:+0.093, s3:+0.069 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 222 | 224 | preventive_schedule | 0.291 | indefinido | indefinido | s11:+0.397, s21:+0.093, s3:+0.069 |
| 3 | HI_WAIT_SELECTED_D1 | 206 | 207 | preventive_schedule | 0.419 | indefinido | indefinido | s11:+0.334, s21:+0.069, s3:+0.059 |
| 3 | HI_WAIT_SELECTED_D2 | 206 | 208 | preventive_schedule | 0.419 | indefinido | indefinido | s11:+0.334, s21:+0.069, s3:+0.059 |
| 3 | ISO_POINT_M15_D1 | 235 | 236 | preventive_schedule | 0.225 | 14.88 | 14.88 | s11:+0.461, s21:+0.098, s3:+0.064 |
| 3 | ISO_POINT_M15_D2 | 235 | 237 | preventive_schedule | 0.225 | 14.88 | 14.88 | s11:+0.461, s21:+0.098, s3:+0.064 |
| 3 | ISO_LOWER98_M15_D1 | 196 | 197 | preventive_schedule | 0.491 | 39.58 | 14.00 | s11:+0.306, s21:+0.055, s3:+0.049 |
| 3 | ISO_LOWER98_M15_D2 | 196 | 198 | preventive_schedule | 0.491 | 39.58 | 14.00 | s11:+0.306, s21:+0.055, s3:+0.049 |
| 3 | RF_SLOPE_POINT_M15_D1 | 236 | 237 | preventive_schedule | 0.215 | 12.16 | 12.16 | s11:+0.466, s21:+0.100, s3:+0.063 |
| 3 | RF_SLOPE_POINT_M15_D2 | 236 | 238 | preventive_schedule | 0.215 | 12.16 | 12.16 | s11:+0.466, s21:+0.100, s3:+0.063 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 201 | 202 | preventive_schedule | 0.452 | 46.09 | 14.80 | s11:+0.315, s21:+0.062, s2:+0.058 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 201 | 203 | preventive_schedule | 0.452 | 46.09 | 14.80 | s11:+0.315, s21:+0.062, s2:+0.058 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.752 | indefinido | indefinido | s11:+0.175, s21:+0.029, s4:+0.015 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.741 | indefinido | indefinido | s11:+0.188, s21:+0.028, s4:+0.014 |
| 3 | HI_MARKER_D1 | 196 | 197 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.306, s21:+0.055, s3:+0.049 |
| 3 | HI_MARKER_D2 | 196 | 198 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.306, s21:+0.055, s3:+0.049 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=194, A=194.
- Repetição2: G=217, A=217.
- Repetição3: G=196, A=196.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.31 | 0.29 | 0.00% | 12.50% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 3.81 | 1.43 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.94 | 0.06 | 0.00% | 3.12% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.94 | 0.06 | 0.00% | 3.12% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.22 | 0.16 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.47 | 0.46 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 33.16 | 15 | 2.94 | 0.54 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 33.16 | 15 | 2.94 | 0.54 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 3.84 | 0.43 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 3.22 | 0.50 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.09 | 15 | 2.88 | 0.64 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.09 | 15 | 2.88 | 0.64 | 0.00% | 12.50% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.94 | 0.54 | 0.00% | 12.50% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.94 | 0.54 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.37 | 0.30 | 0.00% | 10.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.37 | 0.30 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.13 | 0.19 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.13 | 0.19 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 3.37 | 1.26 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 3.23 | 1.20 | 0.00% | 33.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 25.30 | 15 | 2.13 | 0.36 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 25.30 | 15 | 2.13 | 0.36 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.57 | 1.09 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.17 | 0.79 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 34.21 | 15 | 1.20 | 0.70 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 34.21 | 15 | 1.53 | 0.92 | 0.00% | 13.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.13 | 0.36 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.13 | 0.36 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 3.07 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 3.07 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 4.10 | 0.00 | 0.00% | 3.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 4.10 | 0.00 | 0.00% | 3.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.33 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.33 | 0.74 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.58 | 15 | 4.10 | 0.29 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.58 | 15 | 4.10 | 0.29 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.37 | 0.72 | 0.00% | 3.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.87 | 1.03 | 0.00% | 3.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 31.29 | 15 | 4.00 | 0.92 | 0.00% | 13.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 31.29 | 15 | 4.03 | 0.92 | 0.00% | 13.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 4.10 | 0.29 | 0.00% | 20.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 4.10 | 0.29 | 0.00% | 20.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
