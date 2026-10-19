# FD003, motor58 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u58.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 155 | 156 | preventive_schedule | 0.383 | indefinido | indefinido | s4:+0.292, s13:+0.108, s15:+0.093 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 155 | 157 | preventive_schedule | 0.383 | indefinido | indefinido | s4:+0.292, s13:+0.108, s15:+0.093 |
| 1 | HI_WAIT_SELECTED_D1 | 156 | 157 | preventive_schedule | 0.362 | indefinido | indefinido | s4:+0.298, s13:+0.114, s2:+0.104 |
| 1 | HI_WAIT_SELECTED_D2 | 156 | 158 | preventive_schedule | 0.362 | indefinido | indefinido | s4:+0.298, s13:+0.114, s2:+0.104 |
| 1 | ISO_POINT_M15_D1 | 163 | 164 | preventive_schedule | 0.231 | 14.33 | 14.33 | s4:+0.381, s13:+0.132, s15:+0.108 |
| 1 | ISO_POINT_M15_D2 | 163 | 165 | preventive_schedule | 0.231 | 14.33 | 14.33 | s4:+0.381, s13:+0.132, s15:+0.108 |
| 1 | ISO_LOWER98_M15_D1 | 149 | 150 | preventive_schedule | 0.476 | 35.87 | 15.40 | s4:+0.234, s13:+0.107, s2:+0.078 |
| 1 | ISO_LOWER98_M15_D2 | 146 | 148 | preventive_schedule | 0.494 | 36.60 | 16.13 | s4:+0.241, s13:+0.101, s15:+0.069 |
| 1 | RF_SLOPE_POINT_M15_D1 | 159 | 160 | preventive_schedule | 0.315 | 14.64 | 14.64 | s4:+0.323, s13:+0.123, s2:+0.109 |
| 1 | RF_SLOPE_POINT_M15_D2 | 159 | 161 | preventive_schedule | 0.315 | 14.64 | 14.64 | s4:+0.323, s13:+0.123, s2:+0.109 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 146 | 147 | preventive_schedule | 0.494 | 24.88 | 0.00 | s4:+0.241, s13:+0.101, s15:+0.069 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 146 | 148 | preventive_schedule | 0.494 | 24.88 | 0.00 | s4:+0.241, s13:+0.101, s15:+0.069 |
| 1 | AGE_D1 | 145 | 146 | preventive_schedule | 0.521 | indefinido | indefinido | s4:+0.222, s13:+0.099, s15:+0.066 |
| 1 | AGE_D2 | 144 | 146 | preventive_schedule | 0.541 | indefinido | indefinido | s4:+0.215, s13:+0.095, s15:+0.064 |
| 1 | HI_MARKER_D1 | 146 | 147 | preventive_schedule | 0.494 | indefinido | indefinido | s4:+0.241, s13:+0.101, s15:+0.069 |
| 1 | HI_MARKER_D2 | 146 | 148 | preventive_schedule | 0.494 | indefinido | indefinido | s4:+0.241, s13:+0.101, s15:+0.069 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 161 | 162 | preventive_schedule | 0.388 | indefinido | indefinido | s8:+0.274, s15:+0.201, s11:+0.134 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 161 | 163 | preventive_schedule | 0.388 | indefinido | indefinido | s8:+0.274, s15:+0.201, s11:+0.134 |
| 2 | HI_WAIT_SELECTED_D1 | 164 | 165 | preventive_schedule | 0.342 | indefinido | indefinido | s8:+0.298, s15:+0.212, s11:+0.147 |
| 2 | HI_WAIT_SELECTED_D2 | 164 | 166 | preventive_schedule | 0.342 | indefinido | indefinido | s8:+0.298, s15:+0.212, s11:+0.147 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.178 | 44.18 | 44.18 | s8:+0.390, s15:+0.253, s11:+0.190 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.178 | 44.18 | 44.18 | s8:+0.390, s15:+0.253, s11:+0.190 |
| 2 | ISO_LOWER98_M15_D1 | 154 | 155 | preventive_schedule | 0.476 | 84.10 | 10.06 | s8:+0.244, s15:+0.172, s11:+0.115 |
| 2 | ISO_LOWER98_M15_D2 | 154 | 156 | preventive_schedule | 0.476 | 84.10 | 10.06 | s8:+0.244, s15:+0.172, s11:+0.115 |
| 2 | RF_SLOPE_POINT_M15_D1 | 162 | 163 | preventive_schedule | 0.383 | 13.74 | 13.74 | s8:+0.277, s15:+0.200, s11:+0.136 |
| 2 | RF_SLOPE_POINT_M15_D2 | 162 | 164 | preventive_schedule | 0.383 | 13.74 | 13.74 | s8:+0.277, s15:+0.200, s11:+0.136 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 154 | 155 | preventive_schedule | 0.476 | 56.64 | 0.00 | s8:+0.244, s15:+0.172, s11:+0.115 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 154 | 156 | preventive_schedule | 0.476 | 56.64 | 0.00 | s8:+0.244, s15:+0.172, s11:+0.115 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.634 | indefinido | indefinido | s8:+0.184, s15:+0.115, s11:+0.073 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.637 | indefinido | indefinido | s8:+0.182, s15:+0.112, s11:+0.070 |
| 2 | HI_MARKER_D1 | 154 | 155 | preventive_schedule | 0.476 | indefinido | indefinido | s8:+0.244, s15:+0.172, s11:+0.115 |
| 2 | HI_MARKER_D2 | 154 | 156 | preventive_schedule | 0.476 | indefinido | indefinido | s8:+0.244, s15:+0.172, s11:+0.115 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 162 | 163 | preventive_schedule | 0.291 | indefinido | indefinido | s11:+0.321, s4:+0.146, s2:+0.108 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 162 | 164 | preventive_schedule | 0.291 | indefinido | indefinido | s11:+0.321, s4:+0.146, s2:+0.108 |
| 3 | HI_WAIT_SELECTED_D1 | 161 | 162 | preventive_schedule | 0.302 | indefinido | indefinido | s11:+0.315, s4:+0.142, s2:+0.109 |
| 3 | HI_WAIT_SELECTED_D2 | 161 | 163 | preventive_schedule | 0.302 | indefinido | indefinido | s11:+0.315, s4:+0.142, s2:+0.109 |
| 3 | ISO_POINT_M15_D1 | 174 | 175 | preventive_schedule | 0.077 | 13.88 | 13.88 | s11:+0.421, s4:+0.198, s2:+0.134 |
| 3 | ISO_POINT_M15_D2 | 173 | 175 | preventive_schedule | 0.100 | 16.65 | 16.65 | s11:+0.408, s4:+0.194, s2:+0.132 |
| 3 | ISO_LOWER98_M15_D1 | 151 | 152 | preventive_schedule | 0.494 | 46.49 | 14.13 | s11:+0.216, s4:+0.096, s2:+0.084 |
| 3 | ISO_LOWER98_M15_D2 | 151 | 153 | preventive_schedule | 0.494 | 46.49 | 14.13 | s11:+0.216, s4:+0.096, s2:+0.084 |
| 3 | RF_SLOPE_POINT_M15_D1 | 160 | 161 | preventive_schedule | 0.309 | 14.85 | 14.85 | s11:+0.312, s4:+0.141, s2:+0.111 |
| 3 | RF_SLOPE_POINT_M15_D2 | 160 | 162 | preventive_schedule | 0.309 | 14.85 | 14.85 | s11:+0.312, s4:+0.141, s2:+0.111 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 151 | 152 | preventive_schedule | 0.494 | 38.07 | 0.00 | s11:+0.216, s4:+0.096, s2:+0.084 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 151 | 153 | preventive_schedule | 0.494 | 38.07 | 0.00 | s11:+0.216, s4:+0.096, s2:+0.084 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.573 | indefinido | indefinido | s11:+0.180, s4:+0.091, s2:+0.063 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.581 | indefinido | indefinido | s11:+0.181, s4:+0.088, s2:+0.059 |
| 3 | HI_MARKER_D1 | 151 | 152 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.216, s4:+0.096, s2:+0.084 |
| 3 | HI_MARKER_D2 | 151 | 153 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.216, s4:+0.096, s2:+0.084 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=146, A=146.
- Repetição2: G=154, A=154.
- Repetição3: G=151, A=151.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.44 | 0.36 | 0.00% | 12.50% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.44 | 0.36 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.88 | 0.00 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.88 | 0.00 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.16 | 0.30 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.16 | 0.30 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 20.47 | 15 | 2.19 | 0.72 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 20.47 | 15 | 1.88 | 0.28 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.09 | 0.36 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.31 | 0.68 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 52.73 | 15 | 1.81 | 0.28 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 52.73 | 15 | 1.81 | 0.28 | 0.00% | 21.88% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.88 | 0.28 | 0.00% | 21.88% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.88 | 0.28 | 0.00% | 21.88% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.27 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.27 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.17 | 0.07 | 0.00% | 0.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.17 | 0.07 | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 74.05 | 15 | 1.13 | 0.33 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 74.05 | 15 | 1.17 | 0.33 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.10 | 1.00 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.10 | 1.00 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 136.85 | 15 | 1.17 | 0.33 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 136.85 | 15 | 1.17 | 0.33 | 0.00% | 10.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.17 | 0.33 | 0.00% | 10.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.17 | 0.33 | 0.00% | 10.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.47 | 0.63 | 0.00% | 15.62% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.47 | 0.63 | 0.00% | 15.62% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.31 | 0.14 | 0.00% | 12.50% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.31 | 0.14 | 0.00% | 12.50% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.77 | 0.21 | 6.25% | 25.00% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.13 | 0.28 | 3.12% | 21.88% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 32.36 | 15 | 1.31 | 0.58 | 0.00% | 25.00% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 32.36 | 15 | 1.31 | 0.58 | 0.00% | 25.00% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.34 | 0.42 | 0.00% | 25.00% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.34 | 0.60 | 0.00% | 21.88% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 38.63 | 15 | 1.31 | 0.58 | 0.00% | 25.00% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 38.63 | 15 | 1.31 | 0.58 | 0.00% | 25.00% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.31 | 0.58 | 0.00% | 25.00% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.31 | 0.58 | 0.00% | 25.00% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
