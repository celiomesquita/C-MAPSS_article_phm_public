# FD003, motor78 — diagnóstico retrospectivo

Critérios de inclusão: median_discordance_d1, median_discordance_d2.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u78.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 186 | 187 | preventive_schedule | 0.392 | indefinido | indefinido | s11:+0.243, s4:+0.167, s2:+0.142 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 186 | 188 | preventive_schedule | 0.392 | indefinido | indefinido | s11:+0.243, s4:+0.167, s2:+0.142 |
| 1 | HI_WAIT_SELECTED_D1 | 187 | 188 | preventive_schedule | 0.372 | indefinido | indefinido | s11:+0.254, s4:+0.170, s2:+0.150 |
| 1 | HI_WAIT_SELECTED_D2 | 187 | 189 | preventive_schedule | 0.372 | indefinido | indefinido | s11:+0.254, s4:+0.170, s2:+0.150 |
| 1 | ISO_POINT_M15_D1 | 204 | 205 | preventive_schedule | 0.192 | 15.22 | 15.22 | s11:+0.327, s4:+0.208, s2:+0.166 |
| 1 | ISO_POINT_M15_D2 | 201 | 203 | preventive_schedule | 0.215 | 16.25 | 16.25 | s11:+0.317, s4:+0.205, s2:+0.158 |
| 1 | ISO_LOWER98_M15_D1 | 177 | 178 | preventive_schedule | 0.500 | 38.60 | 9.00 | s11:+0.177, s4:+0.146, s2:+0.129 |
| 1 | ISO_LOWER98_M15_D2 | 177 | 179 | preventive_schedule | 0.500 | 38.60 | 9.00 | s11:+0.177, s4:+0.146, s2:+0.129 |
| 1 | RF_SLOPE_POINT_M15_D1 | 190 | 191 | preventive_schedule | 0.307 | 14.87 | 14.87 | s11:+0.285, s4:+0.177, s2:+0.162 |
| 1 | RF_SLOPE_POINT_M15_D2 | 188 | 190 | preventive_schedule | 0.340 | 16.50 | 16.50 | s11:+0.269, s4:+0.175, s2:+0.156 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 177 | 178 | preventive_schedule | 0.500 | 44.88 | 0.00 | s11:+0.177, s4:+0.146, s2:+0.129 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 177 | 179 | preventive_schedule | 0.500 | 44.88 | 0.00 | s11:+0.177, s4:+0.146, s2:+0.129 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.683 | indefinido | indefinido | s11:+0.119, s2:+0.090, s4:+0.081 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.694 | indefinido | indefinido | s11:+0.110, s2:+0.090, s4:+0.080 |
| 1 | HI_MARKER_D1 | 177 | 178 | preventive_schedule | 0.500 | indefinido | indefinido | s11:+0.177, s4:+0.146, s2:+0.129 |
| 1 | HI_MARKER_D2 | 177 | 179 | preventive_schedule | 0.500 | indefinido | indefinido | s11:+0.177, s4:+0.146, s2:+0.129 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 172 | 173 | preventive_schedule | 0.391 | indefinido | indefinido | s2:+0.313, s4:+0.244, s11:+0.029 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 172 | 174 | preventive_schedule | 0.391 | indefinido | indefinido | s2:+0.313, s4:+0.244, s11:+0.029 |
| 2 | HI_WAIT_SELECTED_D1 | 173 | 174 | preventive_schedule | 0.402 | indefinido | indefinido | s2:+0.304, s4:+0.242, s11:+0.028 |
| 2 | HI_WAIT_SELECTED_D2 | 173 | 175 | preventive_schedule | 0.402 | indefinido | indefinido | s2:+0.304, s4:+0.242, s11:+0.028 |
| 2 | ISO_POINT_M15_D1 | 189 | 190 | preventive_schedule | 0.217 | 15.12 | 15.12 | s2:+0.376, s4:+0.328, s11:+0.048 |
| 2 | ISO_POINT_M15_D2 | 188 | 190 | preventive_schedule | 0.232 | 16.08 | 16.08 | s2:+0.372, s4:+0.321, s11:+0.047 |
| 2 | ISO_LOWER98_M15_D1 | 168 | 169 | preventive_schedule | 0.488 | 38.35 | 10.87 | s2:+0.242, s4:+0.220, s11:+0.028 |
| 2 | ISO_LOWER98_M15_D2 | 168 | 170 | preventive_schedule | 0.488 | 38.35 | 10.87 | s2:+0.242, s4:+0.220, s11:+0.028 |
| 2 | RF_SLOPE_POINT_M15_D1 | 188 | 189 | preventive_schedule | 0.232 | 15.87 | 15.87 | s2:+0.372, s4:+0.321, s11:+0.047 |
| 2 | RF_SLOPE_POINT_M15_D2 | 187 | 189 | preventive_schedule | 0.262 | 16.37 | 16.37 | s2:+0.357, s4:+0.311, s11:+0.045 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 168 | 169 | preventive_schedule | 0.488 | 58.85 | 13.52 | s2:+0.242, s4:+0.220, s11:+0.028 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 168 | 170 | preventive_schedule | 0.488 | 58.85 | 13.52 | s2:+0.242, s4:+0.220, s11:+0.028 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.603 | indefinido | indefinido | s2:+0.215, s4:+0.149, s11:+0.021 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.607 | indefinido | indefinido | s2:+0.215, s4:+0.146, s11:+0.019 |
| 2 | HI_MARKER_D1 | 168 | 169 | preventive_schedule | 0.488 | indefinido | indefinido | s2:+0.242, s4:+0.220, s11:+0.028 |
| 2 | HI_MARKER_D2 | 168 | 170 | preventive_schedule | 0.488 | indefinido | indefinido | s2:+0.242, s4:+0.220, s11:+0.028 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 188 | 189 | preventive_schedule | 0.285 | indefinido | indefinido | s11:+0.246, s15:+0.145, s2:+0.132 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.390 | indefinido | indefinido | s11:+0.189, s15:+0.137, s2:+0.114 |
| 3 | HI_WAIT_SELECTED_D1 | 182 | 183 | preventive_schedule | 0.390 | indefinido | indefinido | s11:+0.189, s15:+0.137, s2:+0.114 |
| 3 | HI_WAIT_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.390 | indefinido | indefinido | s11:+0.189, s15:+0.137, s2:+0.114 |
| 3 | ISO_POINT_M15_D1 | 200 | 201 | preventive_schedule | 0.188 | 13.69 | 13.69 | s11:+0.288, s15:+0.159, s8:+0.144 |
| 3 | ISO_POINT_M15_D2 | 192 | 194 | preventive_schedule | 0.230 | 16.90 | 16.90 | s11:+0.268, s15:+0.148, s2:+0.144 |
| 3 | ISO_LOWER98_M15_D1 | 172 | 173 | preventive_schedule | 0.485 | 40.28 | 16.00 | s11:+0.148, s15:+0.112, s2:+0.111 |
| 3 | ISO_LOWER98_M15_D2 | 172 | 174 | preventive_schedule | 0.485 | 40.28 | 16.00 | s11:+0.148, s15:+0.112, s2:+0.111 |
| 3 | RF_SLOPE_POINT_M15_D1 | 195 | 196 | preventive_schedule | 0.225 | 15.51 | 15.51 | s11:+0.276, s15:+0.147, s2:+0.137 |
| 3 | RF_SLOPE_POINT_M15_D2 | 191 | 193 | preventive_schedule | 0.253 | 16.98 | 16.98 | s11:+0.260, s15:+0.143, s2:+0.140 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 172 | 173 | preventive_schedule | 0.485 | 41.71 | 0.00 | s11:+0.148, s15:+0.112, s2:+0.111 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 172 | 174 | preventive_schedule | 0.485 | 41.71 | 0.00 | s11:+0.148, s15:+0.112, s2:+0.111 |
| 3 | AGE_D1 | 154 | 155 | preventive_schedule | 0.607 | indefinido | indefinido | s11:+0.134, s2:+0.090, s15:+0.067 |
| 3 | AGE_D2 | 153 | 155 | preventive_schedule | 0.623 | indefinido | indefinido | s11:+0.131, s2:+0.084, s15:+0.065 |
| 3 | HI_MARKER_D1 | 172 | 173 | preventive_schedule | 0.485 | indefinido | indefinido | s11:+0.148, s15:+0.112, s2:+0.111 |
| 3 | HI_MARKER_D2 | 172 | 174 | preventive_schedule | 0.485 | indefinido | indefinido | s11:+0.148, s15:+0.112, s2:+0.111 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=177, A=177.
- Repetição2: G=168, A=168.
- Repetição3: G=172, A=172.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.19 | 0.43 | 0.00% | 12.50% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.19 | 0.43 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.31 | 0.11 | 0.00% | 15.62% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.31 | 0.11 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.72 | 0.48 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.81 | 0.46 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 29.60 | 15 | 2.31 | 0.65 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 29.60 | 15 | 2.31 | 0.65 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.47 | 0.36 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.25 | 0.31 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 63.60 | 15 | 2.31 | 0.65 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 63.60 | 15 | 2.31 | 0.65 | 0.00% | 18.75% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.31 | 0.65 | 0.00% | 18.75% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.31 | 0.65 | 0.00% | 18.75% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.44 | 0.11 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.44 | 0.11 | 0.00% | 12.50% | 0/32 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 3.81 | 0.37 | 0.00% | 6.25% | 0/32 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 3.81 | 0.37 | 0.00% | 6.25% | 0/32 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.03 | 0.31 | 0.00% | 9.38% | 0/32 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.94 | 0.31 | 0.00% | 9.38% | 0/32 |
| 2 | ISO_LOWER98_M15_D1 | 27.48 | 15 | 3.81 | 0.83 | 0.00% | 9.38% | 0/32 |
| 2 | ISO_LOWER98_M15_D2 | 27.48 | 15 | 3.81 | 0.83 | 0.00% | 9.38% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.97 | 0.31 | 0.00% | 9.38% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.03 | 0.35 | 0.00% | 18.75% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 45.33 | 15 | 3.81 | 0.86 | 0.00% | 12.50% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 45.33 | 15 | 3.81 | 0.83 | 0.00% | 9.38% | 0/32 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 3.81 | 0.83 | 0.00% | 9.38% | 0/32 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 3.81 | 0.83 | 0.00% | 9.38% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.93 | 0.35 | 0.00% | 13.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.90 | 0.68 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.63 | 0.14 | 0.00% | 3.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.63 | 0.14 | 0.00% | 3.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.60 | 0.96 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.47 | 0.52 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 24.28 | 15 | 2.63 | 0.65 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 24.28 | 15 | 2.63 | 0.65 | 0.00% | 13.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 3.67 | 0.91 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 3.57 | 0.33 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 54.70 | 15 | 2.57 | 0.65 | 0.00% | 13.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 54.70 | 15 | 2.57 | 0.65 | 0.00% | 13.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.63 | 0.65 | 0.00% | 13.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.63 | 0.65 | 0.00% | 13.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
