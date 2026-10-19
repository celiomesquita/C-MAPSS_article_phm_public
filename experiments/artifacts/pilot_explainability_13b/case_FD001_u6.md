# FD001, motor6 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u6.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 180 | 181 | preventive_schedule | 0.294 | indefinido | indefinido | s7:+0.154, s20:+0.121, s12:+0.114 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 180 | 182 | preventive_schedule | 0.294 | indefinido | indefinido | s7:+0.154, s20:+0.121, s12:+0.114 |
| 1 | HI_WAIT_SELECTED_D1 | 175 | 176 | preventive_schedule | 0.365 | indefinido | indefinido | s7:+0.134, s20:+0.103, s12:+0.099 |
| 1 | HI_WAIT_SELECTED_D2 | 175 | 177 | preventive_schedule | 0.365 | indefinido | indefinido | s7:+0.134, s20:+0.103, s12:+0.099 |
| 1 | ISO_POINT_M15_D1 | 179 | 180 | preventive_schedule | 0.302 | 16.00 | 16.00 | s7:+0.150, s20:+0.119, s12:+0.111 |
| 1 | ISO_POINT_M15_D2 | 178 | 180 | preventive_schedule | 0.324 | 16.42 | 16.42 | s7:+0.145, s20:+0.112, s12:+0.106 |
| 1 | ISO_LOWER98_M15_D1 | 165 | 166 | preventive_schedule | 0.485 | 30.20 | 15.31 | s7:+0.106, s12:+0.089, s20:+0.088 |
| 1 | ISO_LOWER98_M15_D2 | 165 | 167 | preventive_schedule | 0.485 | 30.20 | 15.31 | s7:+0.106, s12:+0.089, s20:+0.088 |
| 1 | RF_SLOPE_POINT_M15_D1 | 178 | 179 | preventive_schedule | 0.324 | 15.34 | 15.34 | s7:+0.145, s20:+0.112, s12:+0.106 |
| 1 | RF_SLOPE_POINT_M15_D2 | 177 | 179 | preventive_schedule | 0.340 | 16.58 | 16.58 | s7:+0.144, s20:+0.106, s12:+0.103 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 165 | 166 | preventive_schedule | 0.485 | 29.17 | 6.63 | s7:+0.106, s12:+0.089, s20:+0.088 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 165 | 167 | preventive_schedule | 0.485 | 29.17 | 6.63 | s7:+0.106, s12:+0.089, s20:+0.088 |
| 1 | AGE_D1 | 126 | 127 | preventive_schedule | 0.753 | indefinido | indefinido | s12:+0.051, s20:+0.051, s7:+0.037 |
| 1 | AGE_D2 | 125 | 127 | preventive_schedule | 0.770 | indefinido | indefinido | s20:+0.049, s12:+0.046, s3:+0.034 |
| 1 | HI_MARKER_D1 | 165 | 166 | preventive_schedule | 0.485 | indefinido | indefinido | s7:+0.106, s12:+0.089, s20:+0.088 |
| 1 | HI_MARKER_D2 | 165 | 167 | preventive_schedule | 0.485 | indefinido | indefinido | s7:+0.106, s12:+0.089, s20:+0.088 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 178 | 179 | preventive_schedule | 0.295 | indefinido | indefinido | s7:+0.159, s2:+0.105, s3:+0.101 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 178 | 180 | preventive_schedule | 0.295 | indefinido | indefinido | s7:+0.159, s2:+0.105, s3:+0.101 |
| 2 | HI_WAIT_SELECTED_D1 | 175 | 176 | preventive_schedule | 0.335 | indefinido | indefinido | s7:+0.147, s2:+0.100, s3:+0.094 |
| 2 | HI_WAIT_SELECTED_D2 | 175 | 177 | preventive_schedule | 0.335 | indefinido | indefinido | s7:+0.147, s2:+0.100, s3:+0.094 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.199 | 19.17 | 19.17 | s7:+0.185, s11:+0.116, s2:+0.112 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.199 | 19.17 | 19.17 | s7:+0.185, s11:+0.116, s2:+0.112 |
| 2 | ISO_LOWER98_M15_D1 | 165 | 166 | preventive_schedule | 0.484 | 35.15 | 7.95 | s7:+0.117, s11:+0.073, s3:+0.072 |
| 2 | ISO_LOWER98_M15_D2 | 165 | 167 | preventive_schedule | 0.484 | 35.15 | 7.95 | s7:+0.117, s11:+0.073, s3:+0.072 |
| 2 | RF_SLOPE_POINT_M15_D1 | 184 | 185 | preventive_schedule | 0.243 | 13.45 | 13.45 | s7:+0.180, s11:+0.107, s2:+0.107 |
| 2 | RF_SLOPE_POINT_M15_D2 | 184 | 186 | preventive_schedule | 0.243 | 13.45 | 13.45 | s7:+0.180, s11:+0.107, s2:+0.107 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 165 | 166 | preventive_schedule | 0.484 | 34.55 | 0.00 | s7:+0.117, s11:+0.073, s3:+0.072 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 165 | 167 | preventive_schedule | 0.484 | 34.55 | 0.00 | s7:+0.117, s11:+0.073, s3:+0.072 |
| 2 | AGE_D1 | 135 | 136 | preventive_schedule | 0.722 | indefinido | indefinido | s7:+0.065, s3:+0.043, s2:+0.040 |
| 2 | AGE_D2 | 134 | 136 | preventive_schedule | 0.728 | indefinido | indefinido | s7:+0.064, s3:+0.043, s11:+0.040 |
| 2 | HI_MARKER_D1 | 165 | 166 | preventive_schedule | 0.484 | indefinido | indefinido | s7:+0.117, s11:+0.073, s3:+0.072 |
| 2 | HI_MARKER_D2 | 165 | 167 | preventive_schedule | 0.484 | indefinido | indefinido | s7:+0.117, s11:+0.073, s3:+0.072 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 172 | 173 | preventive_schedule | 0.296 | indefinido | indefinido | s7:+0.144, s2:+0.124, s12:+0.112 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 172 | 174 | preventive_schedule | 0.296 | indefinido | indefinido | s7:+0.144, s2:+0.124, s12:+0.112 |
| 3 | HI_WAIT_SELECTED_D1 | 166 | 167 | preventive_schedule | 0.385 | indefinido | indefinido | s7:+0.132, s12:+0.107, s2:+0.096 |
| 3 | HI_WAIT_SELECTED_D2 | 166 | 168 | preventive_schedule | 0.385 | indefinido | indefinido | s7:+0.132, s12:+0.107, s2:+0.096 |
| 3 | ISO_POINT_M15_D1 | 179 | 180 | preventive_schedule | 0.194 | 15.05 | 15.05 | s7:+0.176, s12:+0.134, s2:+0.134 |
| 3 | ISO_POINT_M15_D2 | 178 | 180 | preventive_schedule | 0.219 | 16.70 | 16.70 | s7:+0.170, s2:+0.133, s12:+0.128 |
| 3 | ISO_LOWER98_M15_D1 | 156 | 157 | preventive_schedule | 0.494 | 35.42 | 15.00 | s12:+0.102, s7:+0.097, s20:+0.072 |
| 3 | ISO_LOWER98_M15_D2 | 156 | 158 | preventive_schedule | 0.494 | 35.42 | 15.00 | s12:+0.102, s7:+0.097, s20:+0.072 |
| 3 | RF_SLOPE_POINT_M15_D1 | 179 | 180 | preventive_schedule | 0.194 | 14.26 | 14.26 | s7:+0.176, s12:+0.134, s2:+0.134 |
| 3 | RF_SLOPE_POINT_M15_D2 | 179 | 181 | preventive_schedule | 0.194 | 14.26 | 14.26 | s7:+0.176, s12:+0.134, s2:+0.134 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 156 | 157 | preventive_schedule | 0.494 | 40.09 | 14.49 | s12:+0.102, s7:+0.097, s20:+0.072 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 156 | 158 | preventive_schedule | 0.494 | 40.09 | 14.49 | s12:+0.102, s7:+0.097, s20:+0.072 |
| 3 | AGE_D1 | 135 | 136 | preventive_schedule | 0.679 | indefinido | indefinido | s7:+0.069, s12:+0.062, s2:+0.051 |
| 3 | AGE_D2 | 134 | 136 | preventive_schedule | 0.688 | indefinido | indefinido | s7:+0.069, s12:+0.062, s20:+0.050 |
| 3 | HI_MARKER_D1 | 156 | 157 | preventive_schedule | 0.494 | indefinido | indefinido | s12:+0.102, s7:+0.097, s20:+0.072 |
| 3 | HI_MARKER_D2 | 156 | 158 | preventive_schedule | 0.494 | indefinido | indefinido | s12:+0.102, s7:+0.097, s20:+0.072 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=165, A=165.
- Repetição2: G=165, A=165.
- Repetição3: G=156, A=156.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.70 | 0.59 | 0.00% | 26.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.70 | 0.59 | 0.00% | 26.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.90 | 0.03 | 0.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.90 | 0.03 | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.67 | 0.23 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.60 | 0.47 | 0.00% | 36.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 14.89 | 15 | 1.83 | 0.65 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 14.89 | 15 | 1.87 | 0.65 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.80 | 0.79 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.63 | 0.83 | 0.00% | 40.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 22.54 | 15 | 1.90 | 0.70 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 22.54 | 15 | 1.90 | 0.67 | 0.00% | 20.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.90 | 0.75 | 0.00% | 20.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.90 | 0.75 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.03 | 0.57 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.03 | 0.57 | 0.00% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.53 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.53 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 20.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 20.00% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 27.21 | 15 | 1.53 | 0.58 | 0.00% | 20.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 27.21 | 15 | 1.53 | 0.58 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 3.87 | 0.77 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 3.87 | 4.26 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 36.76 | 15 | 1.53 | 0.58 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 36.76 | 15 | 1.53 | 0.58 | 0.00% | 20.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.53 | 0.58 | 0.00% | 20.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.53 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.47 | 0.24 | 0.00% | 30.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.47 | 0.24 | 0.00% | 30.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.90 | 0.00 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.90 | 0.00 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.70 | 0.24 | 0.00% | 30.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.63 | 0.50 | 0.00% | 33.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 20.42 | 15 | 2.87 | 0.76 | 0.00% | 30.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 20.42 | 15 | 2.87 | 0.76 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.27 | 1.37 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.00 | 1.35 | 0.00% | 33.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 25.60 | 15 | 2.90 | 0.86 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 25.60 | 15 | 2.90 | 0.86 | 0.00% | 30.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.90 | 0.86 | 0.00% | 30.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.90 | 0.86 | 0.00% | 30.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
