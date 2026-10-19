# FD003, motor31 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u31.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 168 | 169 | preventive_schedule | 0.294 | indefinido | indefinido | s4:+0.256, s11:+0.240, s20:+0.087 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 168 | 170 | preventive_schedule | 0.294 | indefinido | indefinido | s4:+0.256, s11:+0.240, s20:+0.087 |
| 1 | HI_WAIT_SELECTED_D1 | 154 | 155 | preventive_schedule | 0.387 | indefinido | indefinido | s4:+0.226, s11:+0.210, s20:+0.074 |
| 1 | HI_WAIT_SELECTED_D2 | 154 | 156 | preventive_schedule | 0.387 | indefinido | indefinido | s4:+0.226, s11:+0.210, s20:+0.074 |
| 1 | ISO_POINT_M15_D1 | 175 | 176 | preventive_schedule | 0.175 | 13.43 | 13.43 | s4:+0.303, s11:+0.277, s20:+0.094 |
| 1 | ISO_POINT_M15_D2 | 173 | 175 | preventive_schedule | 0.208 | 16.28 | 16.28 | s4:+0.292, s11:+0.259, s20:+0.098 |
| 1 | ISO_LOWER98_M15_D1 | 144 | 145 | preventive_schedule | 0.494 | 36.82 | 12.33 | s4:+0.208, s11:+0.158, s20:+0.053 |
| 1 | ISO_LOWER98_M15_D2 | 144 | 146 | preventive_schedule | 0.494 | 36.82 | 12.33 | s4:+0.208, s11:+0.158, s20:+0.053 |
| 1 | RF_SLOPE_POINT_M15_D1 | 171 | 172 | preventive_schedule | 0.243 | 15.58 | 15.58 | s4:+0.273, s11:+0.256, s20:+0.089 |
| 1 | RF_SLOPE_POINT_M15_D2 | 171 | 173 | preventive_schedule | 0.243 | 15.58 | 15.58 | s4:+0.273, s11:+0.256, s20:+0.089 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 144 | 145 | preventive_schedule | 0.494 | 39.17 | 12.91 | s4:+0.208, s11:+0.158, s20:+0.053 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 144 | 146 | preventive_schedule | 0.494 | 39.17 | 12.91 | s4:+0.208, s11:+0.158, s20:+0.053 |
| 1 | AGE_D1 | 150 | 151 | preventive_schedule | 0.428 | indefinido | indefinido | s4:+0.209, s11:+0.196, s20:+0.068 |
| 1 | AGE_D2 | 149 | 151 | preventive_schedule | 0.437 | indefinido | indefinido | s4:+0.208, s11:+0.196, s20:+0.065 |
| 1 | HI_MARKER_D1 | 144 | 145 | preventive_schedule | 0.494 | indefinido | indefinido | s4:+0.208, s11:+0.158, s20:+0.053 |
| 1 | HI_MARKER_D2 | 144 | 146 | preventive_schedule | 0.494 | indefinido | indefinido | s4:+0.208, s11:+0.158, s20:+0.053 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 170 | 171 | preventive_schedule | 0.395 | indefinido | indefinido | s8:+0.202, s15:+0.156, s11:+0.136 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 170 | 172 | preventive_schedule | 0.395 | indefinido | indefinido | s8:+0.202, s15:+0.156, s11:+0.136 |
| 2 | HI_WAIT_SELECTED_D1 | 166 | 167 | preventive_schedule | 0.424 | indefinido | indefinido | s8:+0.198, s15:+0.151, s11:+0.128 |
| 2 | HI_WAIT_SELECTED_D2 | 166 | 168 | preventive_schedule | 0.424 | indefinido | indefinido | s8:+0.198, s15:+0.151, s11:+0.128 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.202 | 44.18 | 44.18 | s8:+0.251, s15:+0.218, s11:+0.172 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.202 | 44.18 | 44.18 | s8:+0.251, s15:+0.218, s11:+0.172 |
| 2 | ISO_LOWER98_M15_D1 | 156 | 157 | preventive_schedule | 0.489 | 87.77 | 13.72 | s8:+0.154, s15:+0.149, s11:+0.119 |
| 2 | ISO_LOWER98_M15_D2 | 156 | 158 | preventive_schedule | 0.489 | 87.77 | 13.72 | s8:+0.154, s15:+0.149, s11:+0.119 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.202 | 34.11 | 34.11 | s8:+0.251, s15:+0.218, s11:+0.172 |
| 2 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.202 | 34.11 | 34.11 | s8:+0.251, s15:+0.218, s11:+0.172 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 156 | 157 | preventive_schedule | 0.489 | 114.86 | 0.00 | s8:+0.154, s15:+0.149, s11:+0.119 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 156 | 158 | preventive_schedule | 0.489 | 114.86 | 0.00 | s8:+0.154, s15:+0.149, s11:+0.119 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.593 | indefinido | indefinido | s8:+0.145, s15:+0.101, s11:+0.082 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.594 | indefinido | indefinido | s8:+0.153, s15:+0.094, s11:+0.082 |
| 2 | HI_MARKER_D1 | 156 | 157 | preventive_schedule | 0.489 | indefinido | indefinido | s8:+0.154, s15:+0.149, s11:+0.119 |
| 2 | HI_MARKER_D2 | 156 | 158 | preventive_schedule | 0.489 | indefinido | indefinido | s8:+0.154, s15:+0.149, s11:+0.119 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 152 | 153 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.206, s11:+0.122, s2:+0.069 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 152 | 154 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.206, s11:+0.122, s2:+0.069 |
| 3 | HI_WAIT_SELECTED_D1 | 157 | 158 | preventive_schedule | 0.477 | indefinido | indefinido | s4:+0.193, s11:+0.132, s2:+0.077 |
| 3 | HI_WAIT_SELECTED_D2 | 154 | 156 | preventive_schedule | 0.481 | indefinido | indefinido | s4:+0.206, s11:+0.126, s2:+0.075 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.181 | 18.17 | 18.17 | s4:+0.300, s11:+0.191, s2:+0.138 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.181 | 18.17 | 18.17 | s4:+0.300, s11:+0.191, s2:+0.138 |
| 3 | ISO_LOWER98_M15_D1 | 152 | 153 | preventive_schedule | 0.495 | 40.10 | 16.00 | s4:+0.206, s11:+0.122, s2:+0.069 |
| 3 | ISO_LOWER98_M15_D2 | 152 | 154 | preventive_schedule | 0.495 | 40.10 | 16.00 | s4:+0.206, s11:+0.122, s2:+0.069 |
| 3 | RF_SLOPE_POINT_M15_D1 | 179 | 180 | preventive_schedule | 0.232 | 13.97 | 13.97 | s4:+0.282, s11:+0.182, s2:+0.128 |
| 3 | RF_SLOPE_POINT_M15_D2 | 179 | 181 | preventive_schedule | 0.232 | 13.97 | 13.97 | s4:+0.282, s11:+0.182, s2:+0.128 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 152 | 153 | preventive_schedule | 0.495 | 34.24 | 3.73 | s4:+0.206, s11:+0.122, s2:+0.069 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 152 | 154 | preventive_schedule | 0.495 | 34.24 | 3.73 | s4:+0.206, s11:+0.122, s2:+0.069 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.576 | indefinido | indefinido | s4:+0.184, s11:+0.091, s2:+0.065 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.584 | indefinido | indefinido | s4:+0.181, s11:+0.092, s2:+0.064 |
| 3 | HI_MARKER_D1 | 152 | 153 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.206, s11:+0.122, s2:+0.069 |
| 3 | HI_MARKER_D2 | 152 | 154 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.206, s11:+0.122, s2:+0.069 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=144, A=144.
- Repetição2: G=156, A=156.
- Repetição3: G=152, A=152.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.25 | 0.80 | 0.00% | 21.88% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.25 | 0.80 | 0.00% | 21.88% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.50 | 0.11 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.50 | 0.11 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.59 | 0.42 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.56 | 0.50 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 24.49 | 15 | 2.50 | 0.48 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 24.49 | 15 | 2.50 | 0.48 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.00 | 0.42 | 3.12% | 25.00% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.38 | 0.56 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 26.26 | 15 | 2.28 | 0.50 | 0.00% | 25.00% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 26.26 | 15 | 2.31 | 0.50 | 0.00% | 25.00% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.50 | 0.48 | 0.00% | 21.88% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.50 | 0.48 | 0.00% | 21.88% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.10 | 0.68 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.10 | 0.68 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.33 | 0.14 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.33 | 0.14 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 74.05 | 15 | 2.33 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 74.05 | 15 | 2.33 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 6.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 6.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 136.85 | 15 | 2.33 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 136.85 | 15 | 2.33 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.33 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.33 | 0.52 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.87 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.87 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.87 | 0.33 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.87 | 0.62 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 10.00% | 3.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 10.00% | 3.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 24.10 | 15 | 2.87 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 24.10 | 15 | 2.87 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.40 | 0.62 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.40 | 0.62 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 30.51 | 15 | 2.87 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 30.51 | 15 | 2.87 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.87 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.87 | 0.78 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
