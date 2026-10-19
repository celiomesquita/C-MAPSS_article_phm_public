# FD003, motor42 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u42.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 181 | 182 | preventive_schedule | 0.289 | indefinido | indefinido | s11:+0.564, s8:+0.200, s15:-0.175 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 176 | 178 | preventive_schedule | 0.399 | indefinido | indefinido | s11:+0.475, s8:+0.183, s15:-0.156 |
| 1 | HI_WAIT_SELECTED_D1 | 182 | 183 | preventive_schedule | 0.242 | indefinido | indefinido | s11:+0.600, s8:+0.204, s15:-0.176 |
| 1 | HI_WAIT_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.242 | indefinido | indefinido | s11:+0.600, s8:+0.204, s15:-0.176 |
| 1 | ISO_POINT_M15_D1 | 186 | 187 | preventive_schedule | 0.102 | 15.91 | 15.91 | s11:+0.710, s8:+0.225, s15:-0.182 |
| 1 | ISO_POINT_M15_D2 | 186 | 188 | preventive_schedule | 0.102 | 15.91 | 15.91 | s11:+0.710, s8:+0.225, s15:-0.182 |
| 1 | ISO_LOWER98_M15_D1 | 172 | 173 | preventive_schedule | 0.480 | 44.11 | 10.95 | s11:+0.407, s8:+0.171, s15:-0.142 |
| 1 | ISO_LOWER98_M15_D2 | 172 | 174 | preventive_schedule | 0.480 | 44.11 | 10.95 | s11:+0.407, s8:+0.171, s15:-0.142 |
| 1 | RF_SLOPE_POINT_M15_D1 | 179 | 180 | preventive_schedule | 0.337 | 13.73 | 13.73 | s11:+0.522, s8:+0.193, s15:-0.169 |
| 1 | RF_SLOPE_POINT_M15_D2 | 179 | 181 | preventive_schedule | 0.337 | 13.73 | 13.73 | s11:+0.522, s8:+0.193, s15:-0.169 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 172 | 173 | preventive_schedule | 0.480 | 43.40 | 9.31 | s11:+0.407, s8:+0.171, s15:-0.142 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 172 | 174 | preventive_schedule | 0.480 | 43.40 | 9.31 | s11:+0.407, s8:+0.171, s15:-0.142 |
| 1 | AGE_D1 | 145 | 146 | preventive_schedule | 0.833 | indefinido | indefinido | s8:+0.128, s11:+0.100, s15:-0.079 |
| 1 | AGE_D2 | 144 | 146 | preventive_schedule | 0.840 | indefinido | indefinido | s8:+0.125, s11:+0.100, s15:-0.084 |
| 1 | HI_MARKER_D1 | 172 | 173 | preventive_schedule | 0.480 | indefinido | indefinido | s11:+0.407, s8:+0.171, s15:-0.142 |
| 1 | HI_MARKER_D2 | 172 | 174 | preventive_schedule | 0.480 | indefinido | indefinido | s11:+0.407, s8:+0.171, s15:-0.142 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 140 | 141 | preventive_schedule/escolha interna inviável | 0.399 | indefinido | indefinido | s8:+0.706, s15:-0.176, s9:+0.067 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 140 | 142 | preventive_schedule/escolha interna inviável | 0.399 | indefinido | indefinido | s8:+0.706, s15:-0.176, s9:+0.067 |
| 2 | HI_WAIT_SELECTED_D1 | 119 | 120 | preventive_schedule/escolha interna inviável | 0.481 | indefinido | indefinido | s8:+0.595, s15:-0.112, s9:+0.042 |
| 2 | HI_WAIT_SELECTED_D2 | 119 | 121 | preventive_schedule/escolha interna inviável | 0.481 | indefinido | indefinido | s8:+0.595, s15:-0.112, s9:+0.042 |
| 2 | ISO_POINT_M15_D1 | 154 | 155 | preventive_schedule | 0.215 | 15.52 | 15.52 | s8:+0.810, s15:-0.155, s9:+0.097 |
| 2 | ISO_POINT_M15_D2 | 154 | 156 | preventive_schedule | 0.215 | 15.52 | 15.52 | s8:+0.810, s15:-0.155, s9:+0.097 |
| 2 | ISO_LOWER98_M15_D1 | 114 | 115 | preventive_schedule | 0.500 | 38.95 | 13.65 | s8:+0.573, s15:-0.113, s9:+0.041 |
| 2 | ISO_LOWER98_M15_D2 | 114 | 116 | preventive_schedule | 0.500 | 38.95 | 13.65 | s8:+0.573, s15:-0.113, s9:+0.041 |
| 2 | RF_SLOPE_POINT_M15_D1 | 165 | 166 | preventive_schedule | 0.122 | 14.17 | 14.17 | s8:+0.924, s15:-0.234, s9:+0.120 |
| 2 | RF_SLOPE_POINT_M15_D2 | 165 | 167 | preventive_schedule | 0.122 | 14.17 | 14.17 | s8:+0.924, s15:-0.234, s9:+0.120 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 120 | 121 | preventive_schedule | 0.460 | 49.88 | 15.67 | s8:+0.606, s15:-0.110, s9:+0.045 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 120 | 122 | preventive_schedule | 0.460 | 49.88 | 15.67 | s8:+0.606, s15:-0.110, s9:+0.045 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.323 | indefinido | indefinido | s8:+0.745, s15:-0.162, s9:+0.078 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.354 | indefinido | indefinido | s8:+0.726, s15:-0.173, s9:+0.075 |
| 2 | HI_MARKER_D1 | 114 | 115 | preventive_schedule | 0.500 | indefinido | indefinido | s8:+0.573, s15:-0.113, s9:+0.041 |
| 2 | HI_MARKER_D2 | 114 | 116 | preventive_schedule | 0.500 | indefinido | indefinido | s8:+0.573, s15:-0.113, s9:+0.041 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 178 | 179 | preventive_schedule | 0.386 | indefinido | indefinido | s4:+0.250, s2:+0.185, s11:+0.169 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 178 | 180 | preventive_schedule | 0.386 | indefinido | indefinido | s4:+0.250, s2:+0.185, s11:+0.169 |
| 3 | HI_WAIT_SELECTED_D1 | 184 | 185 | preventive_schedule | 0.261 | indefinido | indefinido | s4:+0.306, s11:+0.217, s2:+0.204 |
| 3 | HI_WAIT_SELECTED_D2 | 184 | 186 | preventive_schedule | 0.261 | indefinido | indefinido | s4:+0.306, s11:+0.217, s2:+0.204 |
| 3 | ISO_POINT_M15_D1 | 185 | 186 | preventive_schedule | 0.233 | 12.47 | 12.47 | s4:+0.313, s11:+0.222, s2:+0.219 |
| 3 | ISO_POINT_M15_D2 | 185 | 187 | preventive_schedule | 0.233 | 12.47 | 12.47 | s4:+0.313, s11:+0.222, s2:+0.219 |
| 3 | ISO_LOWER98_M15_D1 | 174 | 175 | preventive_schedule | 0.489 | 32.87 | 9.25 | s4:+0.206, s2:+0.151, s11:+0.143 |
| 3 | ISO_LOWER98_M15_D2 | 174 | 176 | preventive_schedule | 0.489 | 32.87 | 9.25 | s4:+0.206, s2:+0.151, s11:+0.143 |
| 3 | RF_SLOPE_POINT_M15_D1 | 183 | 184 | preventive_schedule | 0.277 | 13.88 | 13.88 | s4:+0.284, s2:+0.216, s11:+0.210 |
| 3 | RF_SLOPE_POINT_M15_D2 | 182 | 184 | preventive_schedule | 0.298 | 16.32 | 16.32 | s4:+0.277, s2:+0.212, s11:+0.201 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 174 | 175 | preventive_schedule | 0.489 | 22.46 | 0.00 | s4:+0.206, s2:+0.151, s11:+0.143 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 174 | 176 | preventive_schedule | 0.489 | 22.46 | 0.00 | s4:+0.206, s2:+0.151, s11:+0.143 |
| 3 | AGE_D1 | 154 | 155 | preventive_schedule | 0.843 | indefinido | indefinido | s4:+0.079, s11:+0.058, s2:+0.013 |
| 3 | AGE_D2 | 153 | 155 | preventive_schedule | 0.842 | indefinido | indefinido | s4:+0.069, s11:+0.062, s2:+0.021 |
| 3 | HI_MARKER_D1 | 174 | 175 | preventive_schedule | 0.489 | indefinido | indefinido | s4:+0.206, s2:+0.151, s11:+0.143 |
| 3 | HI_MARKER_D2 | 174 | 176 | preventive_schedule | 0.489 | indefinido | indefinido | s4:+0.206, s2:+0.151, s11:+0.143 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=172, A=172.
- Repetição2: G=114, A=114.
- Repetição3: G=174, A=174.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.62 | 0.21 | 0.00% | 12.50% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.78 | 0.23 | 0.00% | 18.75% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 0.91 | 0.03 | 0.00% | 3.12% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 0.91 | 0.03 | 0.00% | 3.12% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.39 | 0.07 | 3.12% | 12.50% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.44 | 0.19 | 0.00% | 3.12% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 33.16 | 15 | 0.91 | 0.25 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 33.16 | 15 | 0.91 | 0.25 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.66 | 0.23 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.66 | 0.22 | 0.00% | 15.62% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.09 | 15 | 0.91 | 0.25 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.09 | 15 | 0.91 | 0.25 | 0.00% | 12.50% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 0.91 | 0.25 | 0.00% | 12.50% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 0.91 | 0.25 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 5.07 | 1.32 | 0.00% | 36.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 5.07 | 1.32 | 0.00% | 36.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 4.23 | 0.21 | 0.00% | 36.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 4.23 | 0.21 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.57 | 0.30 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.60 | 0.28 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 25.30 | 15 | 4.23 | 0.42 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 25.30 | 15 | 4.23 | 0.42 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.83 | 0.85 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.97 | 1.96 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 34.21 | 15 | 3.57 | 0.61 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 34.21 | 15 | 3.67 | 0.70 | 0.00% | 10.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 4.23 | 0.42 | 0.00% | 36.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 4.23 | 0.42 | 0.00% | 36.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.75 | 0.17 | 0.00% | 9.38% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.75 | 0.17 | 0.00% | 9.38% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 0.72 | 0.00 | 0.00% | 6.25% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 0.72 | 0.00 | 0.00% | 6.25% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.72 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.72 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 23.62 | 15 | 0.72 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 23.62 | 15 | 0.72 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.69 | 0.17 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.75 | 0.24 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 41.43 | 15 | 0.72 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 41.43 | 15 | 0.72 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 0.72 | 0.21 | 0.00% | 9.38% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 0.72 | 0.21 | 0.00% | 9.38% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
