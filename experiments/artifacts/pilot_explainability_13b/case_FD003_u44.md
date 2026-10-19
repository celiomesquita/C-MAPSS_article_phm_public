# FD003, motor44 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u44.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 165 | 166 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.315, s11:+0.084, s2:+0.064 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 165 | 167 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.315, s11:+0.084, s2:+0.064 |
| 1 | HI_WAIT_SELECTED_D1 | 170 | 171 | preventive_schedule | 0.444 | indefinido | indefinido | s4:+0.339, s11:+0.090, s2:+0.080 |
| 1 | HI_WAIT_SELECTED_D2 | 170 | 172 | preventive_schedule | 0.444 | indefinido | indefinido | s4:+0.339, s11:+0.090, s2:+0.080 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.340 | 25.98 | 25.98 | s4:+0.390, s11:+0.112, s2:+0.101 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.340 | 25.98 | 25.98 | s4:+0.390, s11:+0.112, s2:+0.101 |
| 1 | ISO_LOWER98_M15_D1 | 165 | 166 | preventive_schedule | 0.495 | 33.05 | 2.80 | s4:+0.315, s11:+0.084, s2:+0.064 |
| 1 | ISO_LOWER98_M15_D2 | 165 | 167 | preventive_schedule | 0.495 | 33.05 | 2.80 | s4:+0.315, s11:+0.084, s2:+0.064 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.340 | 32.92 | 32.92 | s4:+0.390, s11:+0.112, s2:+0.101 |
| 1 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.340 | 32.92 | 32.92 | s4:+0.390, s11:+0.112, s2:+0.101 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 165 | 166 | preventive_schedule | 0.495 | 31.21 | 0.00 | s4:+0.315, s11:+0.084, s2:+0.064 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 165 | 167 | preventive_schedule | 0.495 | 31.21 | 0.00 | s4:+0.315, s11:+0.084, s2:+0.064 |
| 1 | AGE_D1 | 154 | 155 | preventive_schedule | 0.606 | indefinido | indefinido | s4:+0.236, s11:+0.067, s2:+0.059 |
| 1 | AGE_D2 | 153 | 155 | preventive_schedule | 0.614 | indefinido | indefinido | s4:+0.230, s11:+0.069, s2:+0.056 |
| 1 | HI_MARKER_D1 | 165 | 166 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.315, s11:+0.084, s2:+0.064 |
| 1 | HI_MARKER_D2 | 165 | 167 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.315, s11:+0.084, s2:+0.064 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 177 | 178 | preventive_schedule | 0.297 | indefinido | indefinido | s11:+0.424, s15:+0.121, s8:+0.065 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 177 | 179 | preventive_schedule | 0.297 | indefinido | indefinido | s11:+0.424, s15:+0.121, s8:+0.065 |
| 2 | HI_WAIT_SELECTED_D1 | 166 | 167 | preventive_schedule | 0.424 | indefinido | indefinido | s11:+0.332, s15:+0.119, s8:+0.055 |
| 2 | HI_WAIT_SELECTED_D2 | 166 | 168 | preventive_schedule | 0.424 | indefinido | indefinido | s11:+0.332, s15:+0.119, s8:+0.055 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.268 | 21.14 | 21.14 | s11:+0.444, s15:+0.121, s8:+0.067 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.268 | 21.14 | 21.14 | s11:+0.444, s15:+0.121, s8:+0.067 |
| 2 | ISO_LOWER98_M15_D1 | 156 | 157 | preventive_schedule | 0.497 | 36.05 | 15.64 | s11:+0.279, s15:+0.116, s8:+0.045 |
| 2 | ISO_LOWER98_M15_D2 | 156 | 158 | preventive_schedule | 0.497 | 36.05 | 15.64 | s11:+0.279, s15:+0.116, s8:+0.045 |
| 2 | RF_SLOPE_POINT_M15_D1 | 179 | 180 | at_endpoint | 0.268 | 9.84 | 9.84 | s11:+0.444, s15:+0.121, s8:+0.067 |
| 2 | RF_SLOPE_POINT_M15_D2 | 179 | 181 | late_schedule | 0.268 | 9.84 | 9.84 | s11:+0.444, s15:+0.121, s8:+0.067 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 156 | 157 | preventive_schedule | 0.497 | 29.10 | 0.00 | s11:+0.279, s15:+0.116, s8:+0.045 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 156 | 158 | preventive_schedule | 0.497 | 29.10 | 0.00 | s11:+0.279, s15:+0.116, s8:+0.045 |
| 2 | AGE_D1 | 150 | 151 | preventive_schedule | 0.555 | indefinido | indefinido | s11:+0.246, s15:+0.107, s8:+0.036 |
| 2 | AGE_D2 | 149 | 151 | preventive_schedule | 0.559 | indefinido | indefinido | s11:+0.247, s15:+0.107, s8:+0.034 |
| 2 | HI_MARKER_D1 | 156 | 157 | preventive_schedule | 0.497 | indefinido | indefinido | s11:+0.279, s15:+0.116, s8:+0.045 |
| 2 | HI_MARKER_D2 | 156 | 158 | preventive_schedule | 0.497 | indefinido | indefinido | s11:+0.279, s15:+0.116, s8:+0.045 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 159 | 160 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.227, s4:+0.153, s20:+0.052 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 159 | 161 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.227, s4:+0.153, s20:+0.052 |
| 3 | HI_WAIT_SELECTED_D1 | 164 | 165 | preventive_schedule | 0.452 | indefinido | indefinido | s11:+0.240, s4:+0.176, s20:+0.053 |
| 3 | HI_WAIT_SELECTED_D2 | 161 | 163 | preventive_schedule | 0.487 | indefinido | indefinido | s11:+0.224, s4:+0.161, s20:+0.049 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.247 | 20.22 | 20.22 | s11:+0.340, s4:+0.220, s20:+0.083 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.247 | 20.22 | 20.22 | s11:+0.340, s4:+0.220, s20:+0.083 |
| 3 | ISO_LOWER98_M15_D1 | 159 | 160 | preventive_schedule | 0.494 | 39.67 | 12.00 | s11:+0.227, s4:+0.153, s20:+0.052 |
| 3 | ISO_LOWER98_M15_D2 | 159 | 161 | preventive_schedule | 0.494 | 39.67 | 12.00 | s11:+0.227, s4:+0.153, s20:+0.052 |
| 3 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.247 | 24.04 | 24.04 | s11:+0.340, s4:+0.220, s20:+0.083 |
| 3 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.247 | 24.04 | 24.04 | s11:+0.340, s4:+0.220, s20:+0.083 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 159 | 160 | preventive_schedule | 0.494 | 41.75 | 9.27 | s11:+0.227, s4:+0.153, s20:+0.052 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 159 | 161 | preventive_schedule | 0.494 | 41.75 | 9.27 | s11:+0.227, s4:+0.153, s20:+0.052 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.639 | indefinido | indefinido | s11:+0.157, s4:+0.114, s20:+0.041 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.646 | indefinido | indefinido | s11:+0.156, s4:+0.109, s20:+0.039 |
| 3 | HI_MARKER_D1 | 159 | 160 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.227, s4:+0.153, s20:+0.052 |
| 3 | HI_MARKER_D2 | 159 | 161 | preventive_schedule | 0.494 | indefinido | indefinido | s11:+0.227, s4:+0.153, s20:+0.052 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=165, A=165.
- Repetição2: G=156, A=156.
- Repetição3: G=159, A=159.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.03 | 0.52 | 0.00% | 23.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.03 | 0.52 | 0.00% | 23.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.66 | 0.38 | 3.33% | 20.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.66 | 0.38 | 3.33% | 20.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.33% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 3.33% | 0.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 30.25 | 15 | 2.03 | 0.52 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 30.25 | 15 | 2.03 | 0.52 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 35.95 | 15 | 2.03 | 0.52 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 35.95 | 15 | 2.03 | 0.52 | 0.00% | 23.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.03 | 0.52 | 0.00% | 23.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.03 | 0.52 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.13 | 0.26 | 6.25% | 28.12% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.13 | 0.26 | 6.25% | 28.12% | 0/32 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.16 | 0.36 | 3.12% | 12.50% | 0/32 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.16 | 0.36 | 3.12% | 12.50% | 0/32 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.25% | 3.12% | 0/32 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 6.25% | 6.25% | 0/32 |
| 2 | ISO_LOWER98_M15_D1 | 20.41 | 15 | 2.56 | 1.26 | 0.00% | 28.12% | 0/32 |
| 2 | ISO_LOWER98_M15_D2 | 20.41 | 15 | 2.56 | 1.26 | 0.00% | 28.12% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.00 | 0.78 | 3.12% | 28.12% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.03 | 0.78 | 0.00% | 28.12% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 52.53 | 15 | 2.56 | 1.26 | 0.00% | 28.12% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 52.53 | 15 | 2.56 | 1.26 | 0.00% | 28.12% | 0/32 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.56 | 1.26 | 0.00% | 28.12% | 0/32 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.56 | 1.26 | 0.00% | 28.12% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.30 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.30 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.30 | 0.52 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.30 | 0.61 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 27.67 | 15 | 2.30 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 27.67 | 15 | 2.30 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 6.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 6.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 32.48 | 15 | 2.30 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 32.48 | 15 | 2.30 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.30 | 0.78 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.30 | 0.78 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
