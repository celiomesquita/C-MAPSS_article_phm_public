# FD003, motor99 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u99.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 143 | 144 | preventive_schedule | 0.295 | indefinido | indefinido | s11:+0.445, s15:+0.103, s2:+0.066 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 136 | 138 | preventive_schedule | 0.394 | indefinido | indefinido | s11:+0.387, s15:+0.087, s2:+0.058 |
| 1 | HI_WAIT_SELECTED_D1 | 137 | 138 | preventive_schedule | 0.383 | indefinido | indefinido | s11:+0.394, s15:+0.090, s2:+0.058 |
| 1 | HI_WAIT_SELECTED_D2 | 137 | 139 | preventive_schedule | 0.383 | indefinido | indefinido | s11:+0.394, s15:+0.090, s2:+0.058 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.279 | 24.40 | 24.40 | s11:+0.457, s15:+0.109, s2:+0.064 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.279 | 24.40 | 24.40 | s11:+0.457, s15:+0.109, s2:+0.064 |
| 1 | ISO_LOWER98_M15_D1 | 127 | 128 | preventive_schedule | 0.500 | 44.16 | 11.00 | s11:+0.326, s15:+0.068, s2:+0.050 |
| 1 | ISO_LOWER98_M15_D2 | 127 | 129 | preventive_schedule | 0.500 | 44.16 | 11.00 | s11:+0.326, s15:+0.068, s2:+0.050 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.279 | 26.20 | 26.20 | s11:+0.457, s15:+0.109, s2:+0.064 |
| 1 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.279 | 26.20 | 26.20 | s11:+0.457, s15:+0.109, s2:+0.064 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 127 | 128 | preventive_schedule | 0.500 | 47.18 | 13.08 | s11:+0.326, s15:+0.068, s2:+0.050 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 127 | 129 | preventive_schedule | 0.500 | 47.18 | 13.08 | s11:+0.326, s15:+0.068, s2:+0.050 |
| 1 | AGE_D1 | indefinido | indefinido | endpoint_without_decision | 0.279 | indefinido | indefinido | s11:+0.457, s15:+0.109, s2:+0.064 |
| 1 | AGE_D2 | 144 | 146 | late_schedule | 0.279 | indefinido | indefinido | s11:+0.457, s15:+0.109, s2:+0.064 |
| 1 | HI_MARKER_D1 | 127 | 128 | preventive_schedule | 0.500 | indefinido | indefinido | s11:+0.326, s15:+0.068, s2:+0.050 |
| 1 | HI_MARKER_D2 | 127 | 129 | preventive_schedule | 0.500 | indefinido | indefinido | s11:+0.326, s15:+0.068, s2:+0.050 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | indefinido | endpoint_without_decision | 0.315 | indefinido | indefinido | s11:+0.349, s15:+0.153, s8:+0.055 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | indefinido | endpoint_without_decision | 0.315 | indefinido | indefinido | s11:+0.349, s15:+0.153, s8:+0.055 |
| 2 | HI_WAIT_SELECTED_D1 | 141 | 142 | preventive_schedule | 0.345 | indefinido | indefinido | s11:+0.339, s15:+0.139, s8:+0.051 |
| 2 | HI_WAIT_SELECTED_D2 | 141 | 143 | preventive_schedule | 0.345 | indefinido | indefinido | s11:+0.339, s15:+0.139, s8:+0.051 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.315 | 23.48 | 23.48 | s11:+0.349, s15:+0.153, s8:+0.055 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.315 | 23.48 | 23.48 | s11:+0.349, s15:+0.153, s8:+0.055 |
| 2 | ISO_LOWER98_M15_D1 | 131 | 132 | preventive_schedule | 0.495 | 36.05 | 15.64 | s11:+0.276, s15:+0.100, s8:+0.037 |
| 2 | ISO_LOWER98_M15_D2 | 131 | 133 | preventive_schedule | 0.495 | 36.05 | 15.64 | s11:+0.276, s15:+0.100, s8:+0.037 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.315 | 16.05 | 16.05 | s11:+0.349, s15:+0.153, s8:+0.055 |
| 2 | RF_SLOPE_POINT_M15_D2 | 144 | 146 | late_schedule | 0.315 | 16.05 | 16.05 | s11:+0.349, s15:+0.153, s8:+0.055 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 131 | 132 | preventive_schedule | 0.495 | 31.21 | 0.00 | s11:+0.276, s15:+0.100, s8:+0.037 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 131 | 133 | preventive_schedule | 0.495 | 31.21 | 0.00 | s11:+0.276, s15:+0.100, s8:+0.037 |
| 2 | AGE_D1 | indefinido | indefinido | endpoint_without_decision | 0.315 | indefinido | indefinido | s11:+0.349, s15:+0.153, s8:+0.055 |
| 2 | AGE_D2 | indefinido | indefinido | endpoint_without_decision | 0.315 | indefinido | indefinido | s11:+0.349, s15:+0.153, s8:+0.055 |
| 2 | HI_MARKER_D1 | 131 | 132 | preventive_schedule | 0.495 | indefinido | indefinido | s11:+0.276, s15:+0.100, s8:+0.037 |
| 2 | HI_MARKER_D2 | 131 | 133 | preventive_schedule | 0.495 | indefinido | indefinido | s11:+0.276, s15:+0.100, s8:+0.037 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 144 | 145 | at_endpoint | 0.298 | indefinido | indefinido | s15:+0.226, s8:+0.165, s11:+0.147 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 138 | 140 | preventive_schedule | 0.381 | indefinido | indefinido | s15:+0.196, s8:+0.139, s11:+0.132 |
| 3 | HI_WAIT_SELECTED_D1 | 142 | 143 | preventive_schedule | 0.329 | indefinido | indefinido | s15:+0.207, s8:+0.161, s11:+0.140 |
| 3 | HI_WAIT_SELECTED_D2 | 142 | 144 | preventive_schedule | 0.329 | indefinido | indefinido | s15:+0.207, s8:+0.161, s11:+0.140 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.298 | 22.56 | 22.56 | s15:+0.226, s8:+0.165, s11:+0.147 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.298 | 22.56 | 22.56 | s15:+0.226, s8:+0.165, s11:+0.147 |
| 3 | ISO_LOWER98_M15_D1 | 132 | 133 | preventive_schedule | 0.484 | 41.04 | 13.67 | s15:+0.153, s11:+0.117, s8:+0.116 |
| 3 | ISO_LOWER98_M15_D2 | 132 | 134 | preventive_schedule | 0.484 | 41.04 | 13.67 | s15:+0.153, s11:+0.117, s8:+0.116 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.298 | 18.34 | 18.34 | s15:+0.226, s8:+0.165, s11:+0.147 |
| 3 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.298 | 18.34 | 18.34 | s15:+0.226, s8:+0.165, s11:+0.147 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 132 | 133 | preventive_schedule | 0.484 | 33.93 | 0.00 | s15:+0.153, s11:+0.117, s8:+0.116 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 132 | 134 | preventive_schedule | 0.484 | 33.93 | 0.00 | s15:+0.153, s11:+0.117, s8:+0.116 |
| 3 | AGE_D1 | indefinido | indefinido | endpoint_without_decision | 0.298 | indefinido | indefinido | s15:+0.226, s8:+0.165, s11:+0.147 |
| 3 | AGE_D2 | 144 | 146 | late_schedule | 0.298 | indefinido | indefinido | s15:+0.226, s8:+0.165, s11:+0.147 |
| 3 | HI_MARKER_D1 | 132 | 133 | preventive_schedule | 0.484 | indefinido | indefinido | s15:+0.153, s11:+0.117, s8:+0.116 |
| 3 | HI_MARKER_D2 | 132 | 134 | preventive_schedule | 0.484 | indefinido | indefinido | s15:+0.153, s11:+0.117, s8:+0.116 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=127, A=127.
- Repetição2: G=131, A=131.
- Repetição3: G=132, A=132.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.96 | 0.50 | 12.50% | 18.75% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.16 | 0.42 | 3.12% | 18.75% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.48 | 0.00 | 3.12% | 18.75% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.48 | 0.00 | 3.12% | 18.75% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.12% | 0.00% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 3.12% | 0.00% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 33.16 | 15 | 1.84 | 0.24 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 33.16 | 15 | 1.84 | 0.24 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.12% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 3.12% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.09 | 15 | 1.84 | 0.24 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.09 | 15 | 1.84 | 0.24 | 0.00% | 21.88% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.84 | 0.24 | 0.00% | 21.88% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.84 | 0.24 | 0.00% | 21.88% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | indefinido | indefinido | 15.62% | 9.38% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | indefinido | indefinido | 15.62% | 9.38% | 0/32 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.03 | 0.03 | 6.25% | 6.25% | 0/32 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.03 | 0.03 | 6.25% | 6.25% | 0/32 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.12% | 0.00% | 0/32 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 3.12% | 0.00% | 0/32 |
| 2 | ISO_LOWER98_M15_D1 | 20.41 | 15 | 1.34 | 0.48 | 0.00% | 28.12% | 0/32 |
| 2 | ISO_LOWER98_M15_D2 | 20.41 | 15 | 1.34 | 0.48 | 0.00% | 28.12% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 31.25% | 31.25% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.04 | 1.05 | 25.00% | 31.25% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 52.53 | 15 | 1.34 | 0.48 | 0.00% | 28.12% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 52.53 | 15 | 1.34 | 0.48 | 0.00% | 28.12% | 0/32 |
| 2 | AGE_D1 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/32 |
| 2 | AGE_D2 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/32 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.34 | 0.48 | 0.00% | 28.12% | 0/32 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.34 | 0.48 | 0.00% | 28.12% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.95 | 0.43 | 26.67% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.27 | 0.42 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.33 | 0.20 | 10.00% | 0.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.33 | 0.20 | 10.00% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 27.37 | 15 | 1.63 | 0.52 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 27.37 | 15 | 1.63 | 0.52 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 13.33% | 13.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 13.33% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 46.24 | 15 | 1.63 | 0.52 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 46.24 | 15 | 1.63 | 0.52 | 0.00% | 16.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.63 | 0.52 | 0.00% | 16.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.63 | 0.52 | 0.00% | 16.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
