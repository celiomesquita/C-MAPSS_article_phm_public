# FD003, motor68 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u68.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 182 | 183 | preventive_schedule | 0.392 | indefinido | indefinido | s4:+0.434, s2:+0.118, s11:+0.048 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.392 | indefinido | indefinido | s4:+0.434, s2:+0.118, s11:+0.048 |
| 1 | HI_WAIT_SELECTED_D1 | 181 | 182 | preventive_schedule | 0.410 | indefinido | indefinido | s4:+0.423, s2:+0.113, s11:+0.047 |
| 1 | HI_WAIT_SELECTED_D2 | 181 | 183 | preventive_schedule | 0.410 | indefinido | indefinido | s4:+0.423, s2:+0.113, s11:+0.047 |
| 1 | ISO_POINT_M15_D1 | 188 | 189 | preventive_schedule | 0.214 | 15.25 | 15.25 | s4:+0.573, s2:+0.145, s11:+0.058 |
| 1 | ISO_POINT_M15_D2 | 186 | 188 | preventive_schedule | 0.278 | 16.61 | 16.61 | s4:+0.520, s2:+0.139, s11:+0.054 |
| 1 | ISO_LOWER98_M15_D1 | 176 | 177 | preventive_schedule | 0.481 | 32.18 | 9.00 | s4:+0.392, s2:+0.077, s11:+0.042 |
| 1 | ISO_LOWER98_M15_D2 | 176 | 178 | preventive_schedule | 0.481 | 32.18 | 9.00 | s4:+0.392, s2:+0.077, s11:+0.042 |
| 1 | RF_SLOPE_POINT_M15_D1 | 190 | 191 | preventive_schedule | 0.167 | 15.86 | 15.86 | s4:+0.611, s2:+0.146, s11:+0.063 |
| 1 | RF_SLOPE_POINT_M15_D2 | 186 | 188 | preventive_schedule | 0.278 | 16.26 | 16.26 | s4:+0.520, s2:+0.139, s11:+0.054 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 176 | 177 | preventive_schedule | 0.481 | 35.08 | 1.85 | s4:+0.392, s2:+0.077, s11:+0.042 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 176 | 178 | preventive_schedule | 0.481 | 35.08 | 1.85 | s4:+0.392, s2:+0.077, s11:+0.042 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.717 | indefinido | indefinido | s4:+0.202, s2:+0.057, s11:+0.024 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.735 | indefinido | indefinido | s4:+0.188, s2:+0.054, s11:+0.023 |
| 1 | HI_MARKER_D1 | 176 | 177 | preventive_schedule | 0.481 | indefinido | indefinido | s4:+0.392, s2:+0.077, s11:+0.042 |
| 1 | HI_MARKER_D2 | 176 | 178 | preventive_schedule | 0.481 | indefinido | indefinido | s4:+0.392, s2:+0.077, s11:+0.042 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 172 | 173 | preventive_schedule/escolha interna inviável | 0.386 | indefinido | indefinido | s9:+0.208, s15:+0.093, s8:+0.085 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 172 | 174 | preventive_schedule/escolha interna inviável | 0.386 | indefinido | indefinido | s9:+0.208, s15:+0.093, s8:+0.085 |
| 2 | HI_WAIT_SELECTED_D1 | 167 | 168 | preventive_schedule/escolha interna inviável | 0.462 | indefinido | indefinido | s9:+0.175, s4:+0.081, s15:+0.079 |
| 2 | HI_WAIT_SELECTED_D2 | 167 | 169 | preventive_schedule/escolha interna inviável | 0.462 | indefinido | indefinido | s9:+0.175, s4:+0.081, s15:+0.079 |
| 2 | ISO_POINT_M15_D1 | 181 | 182 | preventive_schedule | 0.200 | 15.52 | 15.52 | s9:+0.264, s15:+0.120, s8:+0.119 |
| 2 | ISO_POINT_M15_D2 | 181 | 183 | preventive_schedule | 0.200 | 15.52 | 15.52 | s9:+0.264, s15:+0.120, s8:+0.119 |
| 2 | ISO_LOWER98_M15_D1 | 162 | 163 | preventive_schedule | 0.491 | 37.21 | 11.91 | s9:+0.153, s15:+0.084, s8:+0.073 |
| 2 | ISO_LOWER98_M15_D2 | 162 | 164 | preventive_schedule | 0.491 | 37.21 | 11.91 | s9:+0.153, s15:+0.084, s8:+0.073 |
| 2 | RF_SLOPE_POINT_M15_D1 | 182 | 183 | preventive_schedule | 0.163 | 8.58 | 8.58 | s9:+0.270, s15:+0.131, s8:+0.129 |
| 2 | RF_SLOPE_POINT_M15_D2 | 178 | 180 | preventive_schedule | 0.278 | 16.93 | 16.93 | s9:+0.244, s15:+0.110, s8:+0.100 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 162 | 163 | preventive_schedule | 0.491 | 29.20 | 0.00 | s9:+0.153, s15:+0.084, s8:+0.073 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 162 | 164 | preventive_schedule | 0.491 | 29.20 | 0.00 | s9:+0.153, s15:+0.084, s8:+0.073 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.699 | indefinido | indefinido | s9:+0.096, s15:+0.054, s4:+0.045 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.696 | indefinido | indefinido | s9:+0.094, s15:+0.056, s4:+0.046 |
| 2 | HI_MARKER_D1 | 162 | 163 | preventive_schedule | 0.491 | indefinido | indefinido | s9:+0.153, s15:+0.084, s8:+0.073 |
| 2 | HI_MARKER_D2 | 162 | 164 | preventive_schedule | 0.491 | indefinido | indefinido | s9:+0.153, s15:+0.084, s8:+0.073 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 178 | 179 | preventive_schedule | 0.300 | indefinido | indefinido | s11:+0.266, s9:+0.157, s4:+0.132 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 178 | 180 | preventive_schedule | 0.300 | indefinido | indefinido | s11:+0.266, s9:+0.157, s4:+0.132 |
| 3 | HI_WAIT_SELECTED_D1 | 172 | 173 | preventive_schedule | 0.412 | indefinido | indefinido | s11:+0.222, s9:+0.134, s4:+0.121 |
| 3 | HI_WAIT_SELECTED_D2 | 172 | 174 | preventive_schedule | 0.412 | indefinido | indefinido | s11:+0.222, s9:+0.134, s4:+0.121 |
| 3 | ISO_POINT_M15_D1 | 187 | 188 | preventive_schedule | 0.053 | 13.77 | 13.77 | s11:+0.334, s9:+0.198, s4:+0.190 |
| 3 | ISO_POINT_M15_D2 | 186 | 188 | preventive_schedule | 0.089 | 16.65 | 16.65 | s11:+0.323, s9:+0.193, s4:+0.180 |
| 3 | ISO_LOWER98_M15_D1 | 162 | 163 | preventive_schedule | 0.483 | 46.36 | 14.00 | s11:+0.196, s4:+0.107, s9:+0.098 |
| 3 | ISO_LOWER98_M15_D2 | 162 | 164 | preventive_schedule | 0.483 | 46.36 | 14.00 | s11:+0.196, s4:+0.107, s9:+0.098 |
| 3 | RF_SLOPE_POINT_M15_D1 | 177 | 178 | preventive_schedule | 0.315 | 15.95 | 15.95 | s11:+0.263, s9:+0.151, s4:+0.134 |
| 3 | RF_SLOPE_POINT_M15_D2 | 177 | 179 | preventive_schedule | 0.315 | 15.95 | 15.95 | s11:+0.263, s9:+0.151, s4:+0.134 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 162 | 163 | preventive_schedule | 0.483 | 38.80 | 0.17 | s11:+0.196, s4:+0.107, s9:+0.098 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 162 | 164 | preventive_schedule | 0.483 | 38.80 | 0.17 | s11:+0.196, s4:+0.107, s9:+0.098 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.665 | indefinido | indefinido | s11:+0.129, s4:+0.066, s9:+0.062 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.657 | indefinido | indefinido | s11:+0.142, s4:+0.068, s9:+0.060 |
| 3 | HI_MARKER_D1 | 162 | 163 | preventive_schedule | 0.483 | indefinido | indefinido | s11:+0.196, s4:+0.107, s9:+0.098 |
| 3 | HI_MARKER_D2 | 162 | 164 | preventive_schedule | 0.483 | indefinido | indefinido | s11:+0.196, s4:+0.107, s9:+0.098 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=176, A=176.
- Repetição2: G=162, A=162.
- Repetição3: G=162, A=162.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.09 | 0.25 | 0.00% | 12.50% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.09 | 0.25 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.69 | 0.13 | 0.00% | 6.25% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.69 | 0.13 | 0.00% | 6.25% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.72 | 0.17 | 0.00% | 6.25% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.72 | 0.11 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 23.18 | 15 | 1.69 | 0.33 | 0.00% | 6.25% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 23.18 | 15 | 1.69 | 0.33 | 0.00% | 6.25% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.28 | 0.28 | 0.00% | 9.38% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.97 | 0.12 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 33.23 | 15 | 1.69 | 0.33 | 0.00% | 6.25% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 33.23 | 15 | 1.69 | 0.33 | 0.00% | 6.25% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.69 | 0.33 | 0.00% | 6.25% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.69 | 0.33 | 0.00% | 6.25% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.20 | 0.52 | 0.00% | 10.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.20 | 0.52 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.43 | 0.00 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.43 | 0.00 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.70 | 0.48 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.73 | 0.46 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 25.30 | 15 | 1.43 | 0.12 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 25.30 | 15 | 1.43 | 0.12 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.47 | 0.54 | 0.00% | 6.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.00 | 0.48 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 34.21 | 15 | 1.43 | 0.12 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 34.21 | 15 | 1.43 | 0.12 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.43 | 0.12 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.43 | 0.12 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.94 | 0.21 | 0.00% | 25.00% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.94 | 0.21 | 0.00% | 25.00% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.75 | 0.13 | 0.00% | 3.12% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.75 | 0.13 | 0.00% | 3.12% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.66 | 0.25 | 0.00% | 12.50% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.66 | 0.18 | 0.00% | 12.50% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 32.36 | 15 | 1.75 | 0.46 | 0.00% | 12.50% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 32.36 | 15 | 1.75 | 0.46 | 0.00% | 12.50% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.03 | 0.00 | 0.00% | 50.00% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.25 | 0.11 | 0.00% | 43.75% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 38.63 | 15 | 1.75 | 0.46 | 0.00% | 12.50% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 38.63 | 15 | 1.75 | 0.46 | 0.00% | 12.50% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.75 | 0.46 | 0.00% | 12.50% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.75 | 0.46 | 0.00% | 12.50% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
