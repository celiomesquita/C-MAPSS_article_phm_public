# FD003, motor76 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u76.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 142 | 143 | preventive_schedule | 0.388 | indefinido | indefinido | s11:+0.270, s4:+0.139, s2:+0.114 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 142 | 144 | preventive_schedule | 0.388 | indefinido | indefinido | s11:+0.270, s4:+0.139, s2:+0.114 |
| 1 | HI_WAIT_SELECTED_D1 | 144 | 145 | preventive_schedule | 0.366 | indefinido | indefinido | s11:+0.283, s4:+0.143, s2:+0.117 |
| 1 | HI_WAIT_SELECTED_D2 | 144 | 146 | preventive_schedule | 0.366 | indefinido | indefinido | s11:+0.283, s4:+0.143, s2:+0.117 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.260 | 22.12 | 22.12 | s11:+0.340, s4:+0.162, s2:+0.145 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.260 | 22.12 | 22.12 | s11:+0.340, s4:+0.162, s2:+0.145 |
| 1 | ISO_LOWER98_M15_D1 | 134 | 135 | preventive_schedule | 0.487 | 38.60 | 9.00 | s11:+0.210, s4:+0.130, s2:+0.102 |
| 1 | ISO_LOWER98_M15_D2 | 134 | 136 | preventive_schedule | 0.487 | 38.60 | 9.00 | s11:+0.210, s4:+0.130, s2:+0.102 |
| 1 | RF_SLOPE_POINT_M15_D1 | 148 | 149 | preventive_schedule | 0.294 | 13.76 | 13.76 | s11:+0.317, s4:+0.156, s2:+0.140 |
| 1 | RF_SLOPE_POINT_M15_D2 | 145 | 147 | preventive_schedule | 0.339 | 16.87 | 16.87 | s11:+0.303, s4:+0.149, s2:+0.118 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 134 | 135 | preventive_schedule | 0.487 | 24.97 | 0.00 | s11:+0.210, s4:+0.130, s2:+0.102 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 134 | 136 | preventive_schedule | 0.487 | 24.97 | 0.00 | s11:+0.210, s4:+0.130, s2:+0.102 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.373 | indefinido | indefinido | s11:+0.275, s4:+0.141, s2:+0.121 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.388 | indefinido | indefinido | s11:+0.270, s4:+0.139, s2:+0.114 |
| 1 | HI_MARKER_D1 | 134 | 135 | preventive_schedule | 0.487 | indefinido | indefinido | s11:+0.210, s4:+0.130, s2:+0.102 |
| 1 | HI_MARKER_D2 | 134 | 136 | preventive_schedule | 0.487 | indefinido | indefinido | s11:+0.210, s4:+0.130, s2:+0.102 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 149 | 150 | preventive_schedule | 0.300 | indefinido | indefinido | s4:+0.294, s2:+0.146, s11:+0.133 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 149 | 151 | preventive_schedule | 0.300 | indefinido | indefinido | s4:+0.294, s2:+0.146, s11:+0.133 |
| 2 | HI_WAIT_SELECTED_D1 | 134 | 135 | preventive_schedule | 0.466 | indefinido | indefinido | s4:+0.246, s2:+0.105, s11:+0.087 |
| 2 | HI_WAIT_SELECTED_D2 | 134 | 136 | preventive_schedule | 0.466 | indefinido | indefinido | s4:+0.246, s2:+0.105, s11:+0.087 |
| 2 | ISO_POINT_M15_D1 | 151 | 152 | preventive_schedule | 0.285 | 15.84 | 15.84 | s4:+0.298, s2:+0.146, s11:+0.140 |
| 2 | ISO_POINT_M15_D2 | 148 | 150 | preventive_schedule | 0.304 | 16.73 | 16.73 | s4:+0.295, s2:+0.144, s11:+0.132 |
| 2 | ISO_LOWER98_M15_D1 | 129 | 130 | preventive_schedule | 0.500 | 34.68 | 11.48 | s4:+0.239, s2:+0.102, s11:+0.084 |
| 2 | ISO_LOWER98_M15_D2 | 129 | 131 | preventive_schedule | 0.500 | 34.68 | 11.48 | s4:+0.239, s2:+0.102, s11:+0.084 |
| 2 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.272 | 19.54 | 19.54 | s4:+0.307, s2:+0.148, s11:+0.142 |
| 2 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.272 | 19.54 | 19.54 | s4:+0.307, s2:+0.148, s11:+0.142 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 129 | 130 | preventive_schedule | 0.500 | 36.75 | 0.00 | s4:+0.239, s2:+0.102, s11:+0.084 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 129 | 131 | preventive_schedule | 0.500 | 36.75 | 0.00 | s4:+0.239, s2:+0.102, s11:+0.084 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.349 | indefinido | indefinido | s4:+0.282, s11:+0.126, s2:+0.121 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.371 | indefinido | indefinido | s4:+0.271, s2:+0.120, s11:+0.118 |
| 2 | HI_MARKER_D1 | 129 | 130 | preventive_schedule | 0.500 | indefinido | indefinido | s4:+0.239, s2:+0.102, s11:+0.084 |
| 2 | HI_MARKER_D2 | 129 | 131 | preventive_schedule | 0.500 | indefinido | indefinido | s4:+0.239, s2:+0.102, s11:+0.084 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | indefinido | endpoint_without_decision | 0.308 | indefinido | indefinido | s8:+0.205, s15:+0.192, s11:+0.188 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 145 | 147 | preventive_schedule | 0.384 | indefinido | indefinido | s15:+0.183, s11:+0.167, s8:+0.166 |
| 3 | HI_WAIT_SELECTED_D1 | 146 | 147 | preventive_schedule | 0.376 | indefinido | indefinido | s8:+0.178, s15:+0.178, s11:+0.168 |
| 3 | HI_WAIT_SELECTED_D2 | 146 | 148 | preventive_schedule | 0.376 | indefinido | indefinido | s8:+0.178, s15:+0.178, s11:+0.168 |
| 3 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.308 | 22.56 | 22.56 | s8:+0.205, s15:+0.192, s11:+0.188 |
| 3 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.308 | 22.56 | 22.56 | s8:+0.205, s15:+0.192, s11:+0.188 |
| 3 | ISO_LOWER98_M15_D1 | 136 | 137 | preventive_schedule | 0.482 | 40.37 | 13.00 | s15:+0.162, s8:+0.128, s11:+0.126 |
| 3 | ISO_LOWER98_M15_D2 | 136 | 138 | preventive_schedule | 0.482 | 40.37 | 13.00 | s15:+0.162, s8:+0.128, s11:+0.126 |
| 3 | RF_SLOPE_POINT_M15_D1 | 152 | 153 | at_endpoint | 0.308 | 15.92 | 15.92 | s8:+0.205, s15:+0.192, s11:+0.188 |
| 3 | RF_SLOPE_POINT_M15_D2 | 152 | 154 | late_schedule | 0.308 | 15.92 | 15.92 | s8:+0.205, s15:+0.192, s11:+0.188 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 136 | 137 | preventive_schedule | 0.482 | 39.85 | 0.00 | s15:+0.162, s8:+0.128, s11:+0.126 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 136 | 138 | preventive_schedule | 0.482 | 39.85 | 0.00 | s15:+0.162, s8:+0.128, s11:+0.126 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.384 | indefinido | indefinido | s15:+0.183, s11:+0.167, s8:+0.166 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.410 | indefinido | indefinido | s15:+0.178, s8:+0.157, s11:+0.156 |
| 3 | HI_MARKER_D1 | 136 | 137 | preventive_schedule | 0.482 | indefinido | indefinido | s15:+0.162, s8:+0.128, s11:+0.126 |
| 3 | HI_MARKER_D2 | 136 | 138 | preventive_schedule | 0.482 | indefinido | indefinido | s15:+0.162, s8:+0.128, s11:+0.126 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=134, A=134.
- Repetição2: G=129, A=129.
- Repetição3: G=136, A=136.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.38 | 0.54 | 0.00% | 12.50% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.38 | 0.54 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.59 | 0.23 | 0.00% | 3.12% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.59 | 0.23 | 0.00% | 3.12% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.25% | 0.00% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 12.50% | 6.25% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 29.60 | 15 | 1.59 | 0.64 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 29.60 | 15 | 1.59 | 0.64 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.17 | 0.46 | 6.25% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.19 | 0.00 | 3.12% | 25.00% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 63.60 | 15 | 1.59 | 0.64 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 63.60 | 15 | 1.59 | 0.64 | 0.00% | 12.50% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.59 | 0.64 | 0.00% | 12.50% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.59 | 0.64 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.11 | 0.39 | 10.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.11 | 0.39 | 10.00% | 23.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.97 | 0.17 | 0.00% | 23.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.97 | 0.17 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.16 | 0.62 | 16.67% | 20.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.21 | 0.33 | 6.67% | 20.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 23.20 | 15 | 1.97 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 23.20 | 15 | 1.97 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 13.33% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 16.67% | 20.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 40.08 | 15 | 1.97 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 40.08 | 15 | 1.97 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.97 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.97 | 0.35 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | indefinido | indefinido | 23.33% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.87 | 0.48 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.43 | 0.07 | 6.67% | 0.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.43 | 0.07 | 6.67% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 6.67% | 0.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 27.37 | 15 | 1.87 | 0.46 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 27.37 | 15 | 1.87 | 0.46 | 0.00% | 13.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.22 | 0.18 | 23.33% | 26.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.22 | 0.23 | 23.33% | 26.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 46.24 | 15 | 1.87 | 0.46 | 0.00% | 13.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 46.24 | 15 | 1.87 | 0.46 | 0.00% | 13.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.87 | 0.46 | 0.00% | 13.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.87 | 0.46 | 0.00% | 13.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
