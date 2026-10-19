# FD003, motor100 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u100.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 137 | 138 | preventive_schedule | 0.471 | indefinido | indefinido | s4:+0.313, s11:+0.076, s2:+0.058 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 137 | 139 | preventive_schedule | 0.471 | indefinido | indefinido | s4:+0.313, s11:+0.076, s2:+0.058 |
| 1 | HI_WAIT_SELECTED_D1 | 142 | 143 | preventive_schedule | 0.407 | indefinido | indefinido | s4:+0.346, s11:+0.093, s2:+0.065 |
| 1 | HI_WAIT_SELECTED_D2 | 142 | 144 | preventive_schedule | 0.407 | indefinido | indefinido | s4:+0.346, s11:+0.093, s2:+0.065 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.285 | 20.24 | 20.24 | s4:+0.374, s11:+0.125, s2:+0.103 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.285 | 20.24 | 20.24 | s4:+0.374, s11:+0.125, s2:+0.103 |
| 1 | ISO_LOWER98_M15_D1 | 137 | 138 | preventive_schedule | 0.471 | 33.05 | 2.80 | s4:+0.313, s11:+0.076, s2:+0.058 |
| 1 | ISO_LOWER98_M15_D2 | 137 | 139 | preventive_schedule | 0.471 | 33.05 | 2.80 | s4:+0.313, s11:+0.076, s2:+0.058 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.285 | 17.69 | 17.69 | s4:+0.374, s11:+0.125, s2:+0.103 |
| 1 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.285 | 17.69 | 17.69 | s4:+0.374, s11:+0.125, s2:+0.103 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 137 | 138 | preventive_schedule | 0.471 | 27.54 | 0.00 | s4:+0.313, s11:+0.076, s2:+0.058 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 137 | 139 | preventive_schedule | 0.471 | 27.54 | 0.00 | s4:+0.313, s11:+0.076, s2:+0.058 |
| 1 | AGE_D1 | indefinido | indefinido | endpoint_without_decision | 0.285 | indefinido | indefinido | s4:+0.374, s11:+0.125, s2:+0.103 |
| 1 | AGE_D2 | indefinido | indefinido | endpoint_without_decision | 0.285 | indefinido | indefinido | s4:+0.374, s11:+0.125, s2:+0.103 |
| 1 | HI_MARKER_D1 | 137 | 138 | preventive_schedule | 0.471 | indefinido | indefinido | s4:+0.313, s11:+0.076, s2:+0.058 |
| 1 | HI_MARKER_D2 | 137 | 139 | preventive_schedule | 0.471 | indefinido | indefinido | s4:+0.313, s11:+0.076, s2:+0.058 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 145 | 146 | preventive_schedule | 0.281 | indefinido | indefinido | s4:+0.338, s11:+0.134, s2:+0.115 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 145 | 147 | preventive_schedule | 0.281 | indefinido | indefinido | s4:+0.338, s11:+0.134, s2:+0.115 |
| 2 | HI_WAIT_SELECTED_D1 | 140 | 141 | preventive_schedule | 0.376 | indefinido | indefinido | s4:+0.308, s11:+0.105, s2:+0.095 |
| 2 | HI_WAIT_SELECTED_D2 | 140 | 142 | preventive_schedule | 0.376 | indefinido | indefinido | s4:+0.308, s11:+0.105, s2:+0.095 |
| 2 | ISO_POINT_M15_D1 | 145 | 146 | preventive_schedule | 0.281 | 15.84 | 15.84 | s4:+0.338, s11:+0.134, s2:+0.115 |
| 2 | ISO_POINT_M15_D2 | 144 | 146 | preventive_schedule | 0.302 | 16.73 | 16.73 | s4:+0.332, s11:+0.131, s2:+0.109 |
| 2 | ISO_LOWER98_M15_D1 | 135 | 136 | preventive_schedule | 0.490 | 34.68 | 11.48 | s4:+0.255, s11:+0.089, s2:+0.068 |
| 2 | ISO_LOWER98_M15_D2 | 135 | 137 | preventive_schedule | 0.490 | 34.68 | 11.48 | s4:+0.255, s11:+0.089, s2:+0.068 |
| 2 | RF_SLOPE_POINT_M15_D1 | 144 | 145 | preventive_schedule | 0.302 | 13.18 | 13.18 | s4:+0.332, s11:+0.131, s2:+0.109 |
| 2 | RF_SLOPE_POINT_M15_D2 | 144 | 146 | preventive_schedule | 0.302 | 13.18 | 13.18 | s4:+0.332, s11:+0.131, s2:+0.109 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 135 | 136 | preventive_schedule | 0.490 | 29.13 | 0.00 | s4:+0.255, s11:+0.089, s2:+0.068 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 135 | 137 | preventive_schedule | 0.490 | 29.13 | 0.00 | s4:+0.255, s11:+0.089, s2:+0.068 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.281 | indefinido | indefinido | s4:+0.338, s11:+0.134, s2:+0.115 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.302 | indefinido | indefinido | s4:+0.332, s11:+0.131, s2:+0.109 |
| 2 | HI_MARKER_D1 | 135 | 136 | preventive_schedule | 0.490 | indefinido | indefinido | s4:+0.255, s11:+0.089, s2:+0.068 |
| 2 | HI_MARKER_D2 | 135 | 137 | preventive_schedule | 0.490 | indefinido | indefinido | s4:+0.255, s11:+0.089, s2:+0.068 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 143 | 144 | preventive_schedule | 0.293 | indefinido | indefinido | s11:+0.381, s21:+0.100, s3:+0.074 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 143 | 145 | preventive_schedule | 0.293 | indefinido | indefinido | s11:+0.381, s21:+0.100, s3:+0.074 |
| 3 | HI_WAIT_SELECTED_D1 | 138 | 139 | preventive_schedule | 0.386 | indefinido | indefinido | s11:+0.310, s21:+0.099, s3:+0.072 |
| 3 | HI_WAIT_SELECTED_D2 | 138 | 140 | preventive_schedule | 0.386 | indefinido | indefinido | s11:+0.310, s21:+0.099, s3:+0.072 |
| 3 | ISO_POINT_M15_D1 | 146 | 147 | preventive_schedule | 0.218 | 14.84 | 14.84 | s11:+0.431, s21:+0.101, s3:+0.082 |
| 3 | ISO_POINT_M15_D2 | 146 | 148 | preventive_schedule | 0.218 | 14.84 | 14.84 | s11:+0.431, s21:+0.101, s3:+0.082 |
| 3 | ISO_LOWER98_M15_D1 | 128 | 129 | preventive_schedule | 0.496 | 39.58 | 14.00 | s11:+0.262, s21:+0.083, s3:+0.069 |
| 3 | ISO_LOWER98_M15_D2 | 128 | 130 | preventive_schedule | 0.496 | 39.58 | 14.00 | s11:+0.262, s21:+0.083, s3:+0.069 |
| 3 | RF_SLOPE_POINT_M15_D1 | 144 | 145 | preventive_schedule | 0.256 | 13.29 | 13.29 | s11:+0.414, s21:+0.101, s2:+0.071 |
| 3 | RF_SLOPE_POINT_M15_D2 | 144 | 146 | preventive_schedule | 0.256 | 13.29 | 13.29 | s11:+0.414, s21:+0.101, s2:+0.071 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 128 | 129 | preventive_schedule | 0.496 | 22.65 | 0.00 | s11:+0.262, s21:+0.083, s3:+0.069 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 128 | 130 | preventive_schedule | 0.496 | 22.65 | 0.00 | s11:+0.262, s21:+0.083, s3:+0.069 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.236 | indefinido | indefinido | s11:+0.424, s21:+0.100, s2:+0.075 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.256 | indefinido | indefinido | s11:+0.414, s21:+0.101, s2:+0.071 |
| 3 | HI_MARKER_D1 | 128 | 129 | preventive_schedule | 0.496 | indefinido | indefinido | s11:+0.262, s21:+0.083, s3:+0.069 |
| 3 | HI_MARKER_D2 | 128 | 130 | preventive_schedule | 0.496 | indefinido | indefinido | s11:+0.262, s21:+0.083, s3:+0.069 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=137, A=137.
- Repetição2: G=135, A=135.
- Repetição3: G=128, A=128.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.10 | 0.36 | 0.00% | 6.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.10 | 0.36 | 0.00% | 6.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.10 | 0.28 | 0.00% | 3.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.10 | 0.28 | 0.00% | 3.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.33% | 3.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 3.33% | 3.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 30.25 | 15 | 1.10 | 0.36 | 0.00% | 6.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 30.25 | 15 | 1.10 | 0.36 | 0.00% | 6.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 3.33% | 3.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 10.00% | 10.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 35.95 | 15 | 1.10 | 0.36 | 0.00% | 6.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 35.95 | 15 | 1.10 | 0.36 | 0.00% | 6.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.10 | 0.36 | 0.00% | 6.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.10 | 0.36 | 0.00% | 6.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.86 | 0.33 | 3.33% | 10.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.86 | 0.33 | 3.33% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 0.97 | 0.19 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 0.97 | 0.19 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.90 | 0.20 | 3.33% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.83 | 0.16 | 3.33% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 23.20 | 15 | 0.97 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 23.20 | 15 | 0.97 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.70 | 0.42 | 0.00% | 13.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.87 | 0.52 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 40.08 | 15 | 0.97 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 40.08 | 15 | 0.97 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 0.97 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 0.97 | 0.32 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.93 | 0.25 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.93 | 0.25 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.80 | 0.00 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.80 | 0.00 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.87 | 0.32 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.83 | 0.36 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.58 | 15 | 1.80 | 0.43 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.58 | 15 | 1.80 | 0.43 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.27 | 0.25 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.27 | 0.38 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 31.29 | 15 | 1.77 | 0.43 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 31.29 | 15 | 1.77 | 0.43 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.80 | 0.43 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.80 | 0.43 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
