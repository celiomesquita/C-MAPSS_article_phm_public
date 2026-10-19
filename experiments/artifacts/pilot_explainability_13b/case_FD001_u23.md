# FD001, motor23 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u23.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 160 | 161 | preventive_schedule | 0.295 | indefinido | indefinido | s7:+0.178, s4:+0.140, s11:+0.085 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 152 | 154 | preventive_schedule | 0.396 | indefinido | indefinido | s7:+0.166, s4:+0.103, s11:+0.074 |
| 1 | HI_WAIT_SELECTED_D1 | 156 | 157 | preventive_schedule | 0.356 | indefinido | indefinido | s7:+0.171, s4:+0.125, s11:+0.080 |
| 1 | HI_WAIT_SELECTED_D2 | 156 | 158 | preventive_schedule | 0.356 | indefinido | indefinido | s7:+0.171, s4:+0.125, s11:+0.080 |
| 1 | ISO_POINT_M15_D1 | 162 | 163 | preventive_schedule | 0.262 | 15.41 | 15.41 | s7:+0.185, s4:+0.142, s3:+0.089 |
| 1 | ISO_POINT_M15_D2 | 161 | 163 | preventive_schedule | 0.279 | 16.70 | 16.70 | s7:+0.186, s4:+0.140, s11:+0.087 |
| 1 | ISO_LOWER98_M15_D1 | 146 | 147 | preventive_schedule | 0.500 | 35.34 | 11.66 | s7:+0.129, s4:+0.078, s3:+0.065 |
| 1 | ISO_LOWER98_M15_D2 | 146 | 148 | preventive_schedule | 0.500 | 35.34 | 11.66 | s7:+0.129, s4:+0.078, s3:+0.065 |
| 1 | RF_SLOPE_POINT_M15_D1 | 157 | 158 | preventive_schedule | 0.344 | 13.51 | 13.51 | s7:+0.170, s4:+0.129, s11:+0.080 |
| 1 | RF_SLOPE_POINT_M15_D2 | 157 | 159 | preventive_schedule | 0.344 | 13.51 | 13.51 | s7:+0.170, s4:+0.129, s11:+0.080 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 146 | 147 | preventive_schedule | 0.500 | 34.02 | 0.00 | s7:+0.129, s4:+0.078, s3:+0.065 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 146 | 148 | preventive_schedule | 0.500 | 34.02 | 0.00 | s7:+0.129, s4:+0.078, s3:+0.065 |
| 1 | AGE_D1 | 135 | 136 | preventive_schedule | 0.611 | indefinido | indefinido | s7:+0.097, s4:+0.075, s3:+0.052 |
| 1 | AGE_D2 | 134 | 136 | preventive_schedule | 0.620 | indefinido | indefinido | s7:+0.093, s4:+0.079, s3:+0.049 |
| 1 | HI_MARKER_D1 | 146 | 147 | preventive_schedule | 0.500 | indefinido | indefinido | s7:+0.129, s4:+0.078, s3:+0.065 |
| 1 | HI_MARKER_D2 | 146 | 148 | preventive_schedule | 0.500 | indefinido | indefinido | s7:+0.129, s4:+0.078, s3:+0.065 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 157 | 158 | preventive_schedule | 0.285 | indefinido | indefinido | s4:+0.140, s2:+0.132, s12:+0.092 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 157 | 159 | preventive_schedule | 0.285 | indefinido | indefinido | s4:+0.140, s2:+0.132, s12:+0.092 |
| 2 | HI_WAIT_SELECTED_D1 | 150 | 151 | preventive_schedule | 0.384 | indefinido | indefinido | s2:+0.128, s4:+0.104, s12:+0.076 |
| 2 | HI_WAIT_SELECTED_D2 | 150 | 152 | preventive_schedule | 0.384 | indefinido | indefinido | s2:+0.128, s4:+0.104, s12:+0.076 |
| 2 | ISO_POINT_M15_D1 | 166 | 167 | preventive_schedule | 0.134 | 14.57 | 14.57 | s2:+0.165, s4:+0.163, s15:+0.106 |
| 2 | ISO_POINT_M15_D2 | 166 | 168 | at_endpoint | 0.134 | 14.57 | 14.57 | s2:+0.165, s4:+0.163, s15:+0.106 |
| 2 | ISO_LOWER98_M15_D1 | 140 | 141 | preventive_schedule | 0.493 | 41.24 | 12.64 | s2:+0.103, s4:+0.080, s12:+0.069 |
| 2 | ISO_LOWER98_M15_D2 | 140 | 142 | preventive_schedule | 0.493 | 41.24 | 12.64 | s2:+0.103, s4:+0.080, s12:+0.069 |
| 2 | RF_SLOPE_POINT_M15_D1 | 160 | 161 | preventive_schedule | 0.229 | 13.61 | 13.61 | s4:+0.153, s2:+0.146, s12:+0.093 |
| 2 | RF_SLOPE_POINT_M15_D2 | 160 | 162 | preventive_schedule | 0.229 | 13.61 | 13.61 | s4:+0.153, s2:+0.146, s12:+0.093 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 140 | 141 | preventive_schedule | 0.493 | 45.06 | 3.69 | s2:+0.103, s4:+0.080, s12:+0.069 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 140 | 142 | preventive_schedule | 0.493 | 45.06 | 3.69 | s2:+0.103, s4:+0.080, s12:+0.069 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.616 | indefinido | indefinido | s2:+0.104, s4:+0.064, s12:+0.054 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.623 | indefinido | indefinido | s2:+0.105, s4:+0.064, s12:+0.052 |
| 2 | HI_MARKER_D1 | 140 | 141 | preventive_schedule | 0.493 | indefinido | indefinido | s2:+0.103, s4:+0.080, s12:+0.069 |
| 2 | HI_MARKER_D2 | 140 | 142 | preventive_schedule | 0.493 | indefinido | indefinido | s2:+0.103, s4:+0.080, s12:+0.069 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 157 | 158 | preventive_schedule | 0.293 | indefinido | indefinido | s7:+0.143, s4:+0.109, s15:+0.097 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 149 | 151 | preventive_schedule | 0.397 | indefinido | indefinido | s7:+0.124, s20:+0.091, s15:+0.087 |
| 3 | HI_WAIT_SELECTED_D1 | 150 | 151 | preventive_schedule | 0.384 | indefinido | indefinido | s7:+0.130, s20:+0.093, s15:+0.081 |
| 3 | HI_WAIT_SELECTED_D2 | 150 | 152 | preventive_schedule | 0.384 | indefinido | indefinido | s7:+0.130, s20:+0.093, s15:+0.081 |
| 3 | ISO_POINT_M15_D1 | 164 | 165 | preventive_schedule | 0.170 | 15.86 | 15.86 | s7:+0.160, s4:+0.123, s15:+0.120 |
| 3 | ISO_POINT_M15_D2 | 160 | 162 | preventive_schedule | 0.236 | 16.05 | 16.05 | s7:+0.150, s4:+0.119, s20:+0.109 |
| 3 | ISO_LOWER98_M15_D1 | 146 | 147 | preventive_schedule | 0.439 | 29.61 | 12.69 | s7:+0.109, s20:+0.091, s15:+0.084 |
| 3 | ISO_LOWER98_M15_D2 | 143 | 145 | preventive_schedule | 0.447 | 33.75 | 16.83 | s7:+0.116, s20:+0.090, s15:+0.077 |
| 3 | RF_SLOPE_POINT_M15_D1 | 162 | 163 | preventive_schedule | 0.197 | 13.34 | 13.34 | s7:+0.156, s4:+0.121, s15:+0.116 |
| 3 | RF_SLOPE_POINT_M15_D2 | 162 | 164 | preventive_schedule | 0.197 | 13.34 | 13.34 | s7:+0.156, s4:+0.121, s15:+0.116 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 140 | 141 | preventive_schedule | 0.481 | 34.44 | 3.04 | s7:+0.109, s20:+0.083, s15:+0.076 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 140 | 142 | preventive_schedule | 0.481 | 34.44 | 3.04 | s7:+0.109, s20:+0.083, s15:+0.076 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.656 | indefinido | indefinido | s20:+0.064, s7:+0.050, s4:+0.050 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.665 | indefinido | indefinido | s20:+0.064, s7:+0.051, s4:+0.050 |
| 3 | HI_MARKER_D1 | 140 | 141 | preventive_schedule | 0.481 | indefinido | indefinido | s7:+0.109, s20:+0.083, s15:+0.076 |
| 3 | HI_MARKER_D2 | 140 | 142 | preventive_schedule | 0.481 | indefinido | indefinido | s7:+0.109, s20:+0.083, s15:+0.076 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=146, A=146.
- Repetição2: G=140, A=140.
- Repetição3: G=140, A=140.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.37 | 0.37 | 0.00% | 36.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.37 | 0.26 | 0.00% | 36.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.73 | 1.89 | 0.00% | 40.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.73 | 1.89 | 0.00% | 40.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.37 | 0.64 | 0.00% | 16.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.37 | 0.33 | 0.00% | 40.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 23.68 | 15 | 2.73 | 2.22 | 0.00% | 40.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 23.68 | 15 | 2.73 | 2.22 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.20 | 0.25 | 0.00% | 46.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.07 | 0.27 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 41.91 | 15 | 2.73 | 2.22 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 41.91 | 15 | 2.73 | 2.22 | 0.00% | 40.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.73 | 2.22 | 0.00% | 40.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.73 | 2.22 | 0.00% | 40.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.40 | 0.54 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.40 | 0.54 | 0.00% | 20.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.20 | 0.11 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.20 | 0.11 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.93 | 0.37 | 10.00% | 36.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.93 | 0.35 | 10.00% | 33.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 28.60 | 15 | 2.20 | 0.59 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 28.60 | 15 | 2.20 | 0.59 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.43 | 0.67 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.20 | 0.70 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 41.37 | 15 | 2.20 | 0.59 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 41.37 | 15 | 2.20 | 0.59 | 0.00% | 26.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.20 | 0.59 | 0.00% | 26.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.20 | 0.59 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.80 | 0.86 | 0.00% | 30.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.77 | 0.25 | 0.00% | 33.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.50 | 0.10 | 0.00% | 0.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.50 | 0.10 | 0.00% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.41 | 0.64 | 3.33% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.17 | 0.36 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 16.92 | 15 | 2.73 | 1.44 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 16.92 | 15 | 2.40 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.17 | 0.70 | 0.00% | 10.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.17 | 1.07 | 0.00% | 10.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 31.40 | 15 | 1.40 | 0.48 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 31.40 | 15 | 1.40 | 0.48 | 0.00% | 16.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.50 | 0.48 | 0.00% | 16.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.50 | 0.48 | 0.00% | 16.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
