# FD001, motor40 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u40.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 176 | 177 | preventive_schedule | 0.296 | indefinido | indefinido | s2:+0.112, s20:+0.093, s15:+0.087 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 176 | 178 | preventive_schedule | 0.296 | indefinido | indefinido | s2:+0.112, s20:+0.093, s15:+0.087 |
| 1 | HI_WAIT_SELECTED_D1 | 172 | 173 | preventive_schedule | 0.357 | indefinido | indefinido | s2:+0.091, s20:+0.086, s15:+0.084 |
| 1 | HI_WAIT_SELECTED_D2 | 172 | 174 | preventive_schedule | 0.357 | indefinido | indefinido | s2:+0.091, s20:+0.086, s15:+0.084 |
| 1 | ISO_POINT_M15_D1 | 182 | 183 | preventive_schedule | 0.195 | 15.60 | 15.60 | s2:+0.124, s15:+0.101, s20:+0.100 |
| 1 | ISO_POINT_M15_D2 | 180 | 182 | preventive_schedule | 0.226 | 16.07 | 16.07 | s2:+0.125, s15:+0.097, s20:+0.097 |
| 1 | ISO_LOWER98_M15_D1 | 162 | 163 | preventive_schedule | 0.482 | 37.97 | 13.00 | s2:+0.073, s15:+0.065, s7:+0.059 |
| 1 | ISO_LOWER98_M15_D2 | 162 | 164 | preventive_schedule | 0.482 | 37.97 | 13.00 | s2:+0.073, s15:+0.065, s7:+0.059 |
| 1 | RF_SLOPE_POINT_M15_D1 | 177 | 178 | preventive_schedule | 0.287 | 15.71 | 15.71 | s2:+0.118, s20:+0.094, s15:+0.091 |
| 1 | RF_SLOPE_POINT_M15_D2 | 177 | 179 | preventive_schedule | 0.287 | 15.71 | 15.71 | s2:+0.118, s20:+0.094, s15:+0.091 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 162 | 163 | preventive_schedule | 0.482 | 40.34 | 6.14 | s2:+0.073, s15:+0.065, s7:+0.059 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 162 | 164 | preventive_schedule | 0.482 | 40.34 | 6.14 | s2:+0.073, s15:+0.065, s7:+0.059 |
| 1 | AGE_D1 | 145 | 146 | preventive_schedule | 0.652 | indefinido | indefinido | s15:+0.048, s20:+0.043, s7:+0.043 |
| 1 | AGE_D2 | 144 | 146 | preventive_schedule | 0.657 | indefinido | indefinido | s15:+0.046, s20:+0.045, s7:+0.043 |
| 1 | HI_MARKER_D1 | 162 | 163 | preventive_schedule | 0.482 | indefinido | indefinido | s2:+0.073, s15:+0.065, s7:+0.059 |
| 1 | HI_MARKER_D2 | 162 | 164 | preventive_schedule | 0.482 | indefinido | indefinido | s2:+0.073, s15:+0.065, s7:+0.059 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 168 | 169 | preventive_schedule | 0.395 | indefinido | indefinido | s7:+0.134, s2:+0.091, s9:+0.065 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 168 | 170 | preventive_schedule | 0.395 | indefinido | indefinido | s7:+0.134, s2:+0.091, s9:+0.065 |
| 2 | HI_WAIT_SELECTED_D1 | 172 | 173 | preventive_schedule | 0.345 | indefinido | indefinido | s7:+0.141, s2:+0.100, s20:+0.072 |
| 2 | HI_WAIT_SELECTED_D2 | 172 | 174 | preventive_schedule | 0.345 | indefinido | indefinido | s7:+0.141, s2:+0.100, s20:+0.072 |
| 2 | ISO_POINT_M15_D1 | 180 | 181 | preventive_schedule | 0.193 | 13.21 | 13.21 | s7:+0.166, s2:+0.138, s9:+0.085 |
| 2 | ISO_POINT_M15_D2 | 177 | 179 | preventive_schedule | 0.263 | 16.55 | 16.55 | s7:+0.144, s2:+0.130, s9:+0.080 |
| 2 | ISO_LOWER98_M15_D1 | 162 | 163 | preventive_schedule | 0.476 | 34.04 | 11.00 | s7:+0.113, s2:+0.081, s9:+0.054 |
| 2 | ISO_LOWER98_M15_D2 | 162 | 164 | preventive_schedule | 0.476 | 34.04 | 11.00 | s7:+0.113, s2:+0.081, s9:+0.054 |
| 2 | RF_SLOPE_POINT_M15_D1 | 177 | 178 | preventive_schedule | 0.263 | 15.11 | 15.11 | s7:+0.144, s2:+0.130, s9:+0.080 |
| 2 | RF_SLOPE_POINT_M15_D2 | 175 | 177 | preventive_schedule | 0.299 | 16.11 | 16.11 | s7:+0.137, s2:+0.120, s20:+0.078 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 162 | 163 | preventive_schedule | 0.476 | 30.63 | 3.33 | s7:+0.113, s2:+0.081, s9:+0.054 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 162 | 164 | preventive_schedule | 0.476 | 30.63 | 3.33 | s7:+0.113, s2:+0.081, s9:+0.054 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.742 | indefinido | indefinido | s7:+0.062, s2:+0.053, s15:+0.024 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.766 | indefinido | indefinido | s7:+0.057, s2:+0.049, s9:+0.022 |
| 2 | HI_MARKER_D1 | 162 | 163 | preventive_schedule | 0.476 | indefinido | indefinido | s7:+0.113, s2:+0.081, s9:+0.054 |
| 2 | HI_MARKER_D2 | 162 | 164 | preventive_schedule | 0.476 | indefinido | indefinido | s7:+0.113, s2:+0.081, s9:+0.054 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 179 | 180 | preventive_schedule | 0.299 | indefinido | indefinido | s4:+0.108, s20:+0.107, s12:+0.086 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 179 | 181 | preventive_schedule | 0.299 | indefinido | indefinido | s4:+0.108, s20:+0.107, s12:+0.086 |
| 3 | HI_WAIT_SELECTED_D1 | 172 | 173 | preventive_schedule | 0.383 | indefinido | indefinido | s20:+0.095, s4:+0.094, s12:+0.083 |
| 3 | HI_WAIT_SELECTED_D2 | 172 | 174 | preventive_schedule | 0.383 | indefinido | indefinido | s20:+0.095, s4:+0.094, s12:+0.083 |
| 3 | ISO_POINT_M15_D1 | 186 | 187 | preventive_schedule | 0.186 | 13.85 | 13.85 | s4:+0.131, s20:+0.111, s11:+0.105 |
| 3 | ISO_POINT_M15_D2 | 186 | 188 | at_endpoint | 0.186 | 13.85 | 13.85 | s4:+0.131, s20:+0.111, s11:+0.105 |
| 3 | ISO_LOWER98_M15_D1 | 162 | 163 | preventive_schedule | 0.499 | 39.68 | 9.00 | s4:+0.077, s12:+0.069, s11:+0.062 |
| 3 | ISO_LOWER98_M15_D2 | 162 | 164 | preventive_schedule | 0.499 | 39.68 | 9.00 | s4:+0.077, s12:+0.069, s11:+0.062 |
| 3 | RF_SLOPE_POINT_M15_D1 | 186 | 187 | preventive_schedule | 0.186 | 14.83 | 14.83 | s4:+0.131, s20:+0.111, s11:+0.105 |
| 3 | RF_SLOPE_POINT_M15_D2 | 186 | 188 | at_endpoint | 0.186 | 14.83 | 14.83 | s4:+0.131, s20:+0.111, s11:+0.105 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 162 | 163 | preventive_schedule | 0.499 | 38.10 | 1.95 | s4:+0.077, s12:+0.069, s11:+0.062 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 162 | 164 | preventive_schedule | 0.499 | 38.10 | 1.95 | s4:+0.077, s12:+0.069, s11:+0.062 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.794 | indefinido | indefinido | s12:+0.031, s17:+0.026, s15:+0.024 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.810 | indefinido | indefinido | s12:+0.033, s11:+0.026, s17:+0.026 |
| 3 | HI_MARKER_D1 | 162 | 163 | preventive_schedule | 0.499 | indefinido | indefinido | s4:+0.077, s12:+0.069, s11:+0.062 |
| 3 | HI_MARKER_D2 | 162 | 164 | preventive_schedule | 0.499 | indefinido | indefinido | s4:+0.077, s12:+0.069, s11:+0.062 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=162, A=162.
- Repetição2: G=162, A=162.
- Repetição3: G=162, A=162.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.40 | 0.53 | 0.00% | 36.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.40 | 0.53 | 0.00% | 36.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.33 | 0.32 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.33 | 0.55 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 24.97 | 15 | 2.00 | 0.67 | 0.00% | 20.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 24.97 | 15 | 2.00 | 0.67 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.27 | 1.22 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.10 | 1.21 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.20 | 15 | 2.00 | 0.67 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.20 | 15 | 2.00 | 0.67 | 0.00% | 20.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.00 | 0.67 | 0.00% | 20.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.00 | 0.67 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.57 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.57 | 0.41 | 0.00% | 26.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.20 | 0.37 | 0.00% | 0.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.20 | 0.37 | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.23 | 0.22 | 0.00% | 40.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.07 | 0.45 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 23.04 | 15 | 2.20 | 1.04 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 23.04 | 15 | 2.20 | 1.04 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.57 | 0.82 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.87 | 0.42 | 0.00% | 60.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 27.30 | 15 | 2.20 | 1.04 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 27.30 | 15 | 2.20 | 1.04 | 0.00% | 10.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.20 | 1.04 | 0.00% | 10.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.20 | 1.04 | 0.00% | 10.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.30 | 0.42 | 0.00% | 36.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.30 | 0.42 | 0.00% | 36.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.80 | 0.00 | 0.00% | 26.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.80 | 0.00 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.71 | 0.32 | 20.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.71 | 0.32 | 20.00% | 26.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 30.68 | 15 | 1.80 | 0.16 | 0.00% | 36.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 30.68 | 15 | 1.80 | 0.16 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.75 | 0.32 | 20.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.75 | 0.50 | 20.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 36.15 | 15 | 1.80 | 0.16 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 36.15 | 15 | 1.80 | 0.16 | 0.00% | 36.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.80 | 0.16 | 0.00% | 36.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.80 | 0.16 | 0.00% | 36.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
