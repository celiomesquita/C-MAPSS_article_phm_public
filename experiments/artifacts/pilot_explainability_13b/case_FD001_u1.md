# FD001, motor1 — diagnóstico retrospectivo

Critérios de inclusão: median_discordance_d2.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u1.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 164 | 165 | preventive_schedule | 0.289 | indefinido | indefinido | s12:+0.155, s4:+0.128, s7:+0.078 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 164 | 166 | preventive_schedule | 0.289 | indefinido | indefinido | s12:+0.155, s4:+0.128, s7:+0.078 |
| 1 | HI_WAIT_SELECTED_D1 | 162 | 163 | preventive_schedule | 0.334 | indefinido | indefinido | s12:+0.144, s4:+0.120, s7:+0.074 |
| 1 | HI_WAIT_SELECTED_D2 | 162 | 164 | preventive_schedule | 0.334 | indefinido | indefinido | s12:+0.144, s4:+0.120, s7:+0.074 |
| 1 | ISO_POINT_M15_D1 | 179 | 180 | preventive_schedule | 0.099 | 15.41 | 15.41 | s12:+0.202, s4:+0.153, s15:+0.106 |
| 1 | ISO_POINT_M15_D2 | 177 | 179 | preventive_schedule | 0.111 | 16.62 | 16.62 | s12:+0.199, s4:+0.145, s15:+0.108 |
| 1 | ISO_LOWER98_M15_D1 | 152 | 153 | preventive_schedule | 0.480 | 41.05 | 13.00 | s12:+0.115, s4:+0.085, s7:+0.058 |
| 1 | ISO_LOWER98_M15_D2 | 152 | 154 | preventive_schedule | 0.480 | 41.05 | 13.00 | s12:+0.115, s4:+0.085, s7:+0.058 |
| 1 | RF_SLOPE_POINT_M15_D1 | 173 | 174 | preventive_schedule | 0.154 | 13.70 | 13.70 | s12:+0.187, s4:+0.138, s15:+0.100 |
| 1 | RF_SLOPE_POINT_M15_D2 | 172 | 174 | preventive_schedule | 0.185 | 16.56 | 16.56 | s12:+0.181, s4:+0.130, s15:+0.093 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 152 | 153 | preventive_schedule | 0.480 | 50.77 | 6.65 | s12:+0.115, s4:+0.085, s7:+0.058 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 152 | 154 | preventive_schedule | 0.480 | 50.77 | 6.65 | s12:+0.115, s4:+0.085, s7:+0.058 |
| 1 | AGE_D1 | 126 | 127 | preventive_schedule | 0.699 | indefinido | indefinido | s12:+0.056, s4:+0.055, s2:+0.040 |
| 1 | AGE_D2 | 125 | 127 | preventive_schedule | 0.700 | indefinido | indefinido | s12:+0.054, s4:+0.049, s2:+0.042 |
| 1 | HI_MARKER_D1 | 152 | 153 | preventive_schedule | 0.480 | indefinido | indefinido | s12:+0.115, s4:+0.085, s7:+0.058 |
| 1 | HI_MARKER_D2 | 152 | 154 | preventive_schedule | 0.480 | indefinido | indefinido | s12:+0.115, s4:+0.085, s7:+0.058 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 160 | 161 | preventive_schedule | 0.391 | indefinido | indefinido | s7:+0.105, s11:+0.101, s20:+0.081 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 160 | 162 | preventive_schedule | 0.391 | indefinido | indefinido | s7:+0.105, s11:+0.101, s20:+0.081 |
| 2 | HI_WAIT_SELECTED_D1 | 162 | 163 | preventive_schedule | 0.352 | indefinido | indefinido | s7:+0.106, s11:+0.103, s4:+0.087 |
| 2 | HI_WAIT_SELECTED_D2 | 157 | 159 | preventive_schedule | 0.437 | indefinido | indefinido | s11:+0.091, s7:+0.089, s20:+0.078 |
| 2 | ISO_POINT_M15_D1 | 184 | 185 | preventive_schedule | 0.000 | 9.01 | 9.01 | s11:+0.167, s7:+0.162, s2:+0.147 |
| 2 | ISO_POINT_M15_D2 | 180 | 182 | preventive_schedule | 0.103 | 16.66 | 16.66 | s11:+0.155, s7:+0.145, s2:+0.120 |
| 2 | ISO_LOWER98_M15_D1 | 153 | 154 | preventive_schedule | 0.471 | 41.62 | 13.36 | s11:+0.085, s7:+0.085, s2:+0.069 |
| 2 | ISO_LOWER98_M15_D2 | 152 | 154 | preventive_schedule | 0.495 | 45.26 | 17.00 | s7:+0.083, s11:+0.080, s2:+0.067 |
| 2 | RF_SLOPE_POINT_M15_D1 | 169 | 170 | preventive_schedule | 0.271 | 15.85 | 15.85 | s11:+0.121, s7:+0.119, s4:+0.095 |
| 2 | RF_SLOPE_POINT_M15_D2 | 169 | 171 | preventive_schedule | 0.271 | 15.85 | 15.85 | s11:+0.121, s7:+0.119, s4:+0.095 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 155 | 156 | preventive_schedule | 0.457 | 35.94 | 0.00 | s11:+0.087, s7:+0.084, s20:+0.072 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 155 | 157 | preventive_schedule | 0.457 | 35.94 | 0.00 | s11:+0.087, s7:+0.084, s20:+0.072 |
| 2 | AGE_D1 | 133 | 134 | preventive_schedule | 0.603 | indefinido | indefinido | s11:+0.072, s7:+0.069, s2:+0.066 |
| 2 | AGE_D2 | 132 | 134 | preventive_schedule | 0.610 | indefinido | indefinido | s11:+0.072, s7:+0.066, s2:+0.064 |
| 2 | HI_MARKER_D1 | 152 | 153 | preventive_schedule | 0.495 | indefinido | indefinido | s7:+0.083, s11:+0.080, s2:+0.067 |
| 2 | HI_MARKER_D2 | 152 | 154 | preventive_schedule | 0.495 | indefinido | indefinido | s7:+0.083, s11:+0.080, s2:+0.067 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 170 | 171 | preventive_schedule | 0.297 | indefinido | indefinido | s4:+0.168, s7:+0.135, s13:+0.120 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 170 | 172 | preventive_schedule | 0.297 | indefinido | indefinido | s4:+0.168, s7:+0.135, s13:+0.120 |
| 3 | HI_WAIT_SELECTED_D1 | 166 | 167 | preventive_schedule | 0.328 | indefinido | indefinido | s4:+0.168, s7:+0.128, s13:+0.116 |
| 3 | HI_WAIT_SELECTED_D2 | 166 | 168 | preventive_schedule | 0.328 | indefinido | indefinido | s4:+0.168, s7:+0.128, s13:+0.116 |
| 3 | ISO_POINT_M15_D1 | 173 | 174 | preventive_schedule | 0.234 | 15.98 | 15.98 | s4:+0.174, s7:+0.147, s13:+0.128 |
| 3 | ISO_POINT_M15_D2 | 173 | 175 | preventive_schedule | 0.234 | 15.98 | 15.98 | s4:+0.174, s7:+0.147, s13:+0.128 |
| 3 | ISO_LOWER98_M15_D1 | 158 | 159 | preventive_schedule | 0.473 | 32.54 | 13.55 | s4:+0.122, s7:+0.100, s13:+0.093 |
| 3 | ISO_LOWER98_M15_D2 | 156 | 158 | preventive_schedule | 0.489 | 35.38 | 16.39 | s4:+0.119, s7:+0.093, s13:+0.088 |
| 3 | RF_SLOPE_POINT_M15_D1 | 164 | 165 | preventive_schedule | 0.350 | 14.58 | 14.58 | s4:+0.162, s7:+0.122, s13:+0.114 |
| 3 | RF_SLOPE_POINT_M15_D2 | 163 | 165 | preventive_schedule | 0.368 | 16.92 | 16.92 | s4:+0.158, s7:+0.118, s13:+0.108 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 156 | 157 | preventive_schedule | 0.489 | 35.84 | 0.00 | s4:+0.119, s7:+0.093, s13:+0.088 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 156 | 158 | preventive_schedule | 0.489 | 35.84 | 0.00 | s4:+0.119, s7:+0.093, s13:+0.088 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.715 | indefinido | indefinido | s4:+0.069, s13:+0.048, s2:+0.047 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.714 | indefinido | indefinido | s4:+0.062, s13:+0.051, s2:+0.049 |
| 3 | HI_MARKER_D1 | 156 | 157 | preventive_schedule | 0.489 | indefinido | indefinido | s4:+0.119, s7:+0.093, s13:+0.088 |
| 3 | HI_MARKER_D2 | 156 | 158 | preventive_schedule | 0.489 | indefinido | indefinido | s4:+0.119, s7:+0.093, s13:+0.088 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=152, A=152.
- Repetição2: G=152, A=152.
- Repetição3: G=156, A=156.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.50 | 0.41 | 0.00% | 26.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.50 | 0.41 | 0.00% | 26.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 0.97 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 0.97 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.03 | 0.90 | 0.00% | 33.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.00 | 0.45 | 0.00% | 33.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 28.05 | 15 | 1.00 | 0.29 | 0.00% | 20.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 28.05 | 15 | 0.97 | 0.32 | 0.00% | 16.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.33 | 0.70 | 0.00% | 0.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.03 | 0.59 | 0.00% | 10.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 44.12 | 15 | 0.77 | 0.29 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 44.12 | 15 | 0.77 | 0.29 | 0.00% | 20.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 0.97 | 0.32 | 0.00% | 16.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 0.97 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.40 | 0.48 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.40 | 0.48 | 0.00% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.23 | 0.00 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.23 | 0.14 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.67 | 0.33 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.73 | 1.00 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 28.26 | 15 | 1.57 | 0.43 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 28.26 | 15 | 1.23 | 0.43 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.73 | 1.17 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.03 | 1.33 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 36.46 | 15 | 0.27 | 0.50 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 36.46 | 15 | 0.33 | 0.62 | 0.00% | 20.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.23 | 0.43 | 0.00% | 30.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.23 | 0.43 | 0.00% | 30.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.63 | 0.50 | 0.00% | 33.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.63 | 0.50 | 0.00% | 33.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.80 | 0.17 | 0.00% | 0.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.80 | 0.17 | 0.00% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.23 | 0.35 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.23 | 0.35 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 18.99 | 15 | 1.90 | 1.04 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 18.99 | 15 | 1.80 | 0.88 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.30 | 0.38 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.27 | 0.33 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 40.68 | 15 | 1.60 | 0.88 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 40.68 | 15 | 1.60 | 0.88 | 0.00% | 20.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.80 | 0.88 | 0.00% | 20.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.80 | 0.88 | 0.00% | 20.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
