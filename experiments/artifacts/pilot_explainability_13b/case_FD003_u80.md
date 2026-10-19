# FD003, motor80 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u80.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 130 | 131 | preventive_schedule | 0.396 | indefinido | indefinido | s4:+0.395, s2:+0.131, s11:+0.055 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 130 | 132 | preventive_schedule | 0.396 | indefinido | indefinido | s4:+0.395, s2:+0.131, s11:+0.055 |
| 1 | HI_WAIT_SELECTED_D1 | 125 | 126 | preventive_schedule | 0.461 | indefinido | indefinido | s4:+0.356, s2:+0.114, s11:+0.050 |
| 1 | HI_WAIT_SELECTED_D2 | 125 | 127 | preventive_schedule | 0.461 | indefinido | indefinido | s4:+0.356, s2:+0.114, s11:+0.050 |
| 1 | ISO_POINT_M15_D1 | 140 | 141 | preventive_schedule | 0.212 | 15.25 | 15.25 | s4:+0.530, s2:+0.157, s11:+0.073 |
| 1 | ISO_POINT_M15_D2 | 138 | 140 | preventive_schedule | 0.269 | 16.61 | 16.61 | s4:+0.489, s2:+0.147, s11:+0.068 |
| 1 | ISO_LOWER98_M15_D1 | 120 | 121 | preventive_schedule | 0.495 | 35.70 | 12.52 | s4:+0.346, s2:+0.099, s11:+0.043 |
| 1 | ISO_LOWER98_M15_D2 | 120 | 122 | preventive_schedule | 0.495 | 35.70 | 12.52 | s4:+0.346, s2:+0.099, s11:+0.043 |
| 1 | RF_SLOPE_POINT_M15_D1 | 138 | 139 | preventive_schedule | 0.269 | 11.90 | 11.90 | s4:+0.489, s2:+0.147, s11:+0.068 |
| 1 | RF_SLOPE_POINT_M15_D2 | 138 | 140 | preventive_schedule | 0.269 | 11.90 | 11.90 | s4:+0.489, s2:+0.147, s11:+0.068 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 120 | 121 | preventive_schedule | 0.495 | 29.19 | 0.00 | s4:+0.346, s2:+0.099, s11:+0.043 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 120 | 122 | preventive_schedule | 0.495 | 29.19 | 0.00 | s4:+0.346, s2:+0.099, s11:+0.043 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.157 | indefinido | indefinido | s4:+0.558, s2:+0.178, s11:+0.076 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.188 | indefinido | indefinido | s4:+0.537, s2:+0.171, s11:+0.075 |
| 1 | HI_MARKER_D1 | 120 | 121 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.346, s2:+0.099, s11:+0.043 |
| 1 | HI_MARKER_D2 | 120 | 122 | preventive_schedule | 0.495 | indefinido | indefinido | s4:+0.346, s2:+0.099, s11:+0.043 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 117 | 118 | preventive_schedule | 0.485 | indefinido | indefinido | s11:+0.294, s15:+0.082, s4:+0.062 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 117 | 119 | preventive_schedule | 0.485 | indefinido | indefinido | s11:+0.294, s15:+0.082, s4:+0.062 |
| 2 | HI_WAIT_SELECTED_D1 | 122 | 123 | preventive_schedule | 0.423 | indefinido | indefinido | s11:+0.331, s15:+0.089, s4:+0.068 |
| 2 | HI_WAIT_SELECTED_D2 | 119 | 121 | preventive_schedule | 0.440 | indefinido | indefinido | s11:+0.325, s15:+0.086, s4:+0.068 |
| 2 | ISO_POINT_M15_D1 | 137 | 138 | preventive_schedule | 0.139 | 15.89 | 15.89 | s11:+0.504, s15:+0.137, s2:+0.092 |
| 2 | ISO_POINT_M15_D2 | 136 | 138 | preventive_schedule | 0.177 | 16.89 | 16.89 | s11:+0.471, s15:+0.140, s2:+0.091 |
| 2 | ISO_LOWER98_M15_D1 | 117 | 118 | preventive_schedule | 0.485 | 43.05 | 13.40 | s11:+0.294, s15:+0.082, s4:+0.062 |
| 2 | ISO_LOWER98_M15_D2 | 117 | 119 | preventive_schedule | 0.485 | 43.05 | 13.40 | s11:+0.294, s15:+0.082, s4:+0.062 |
| 2 | RF_SLOPE_POINT_M15_D1 | 119 | 120 | preventive_schedule | 0.440 | 15.60 | 15.60 | s11:+0.325, s15:+0.086, s4:+0.068 |
| 2 | RF_SLOPE_POINT_M15_D2 | 119 | 121 | preventive_schedule | 0.440 | 15.60 | 15.60 | s11:+0.325, s15:+0.086, s4:+0.068 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 117 | 118 | preventive_schedule | 0.485 | 20.73 | 0.00 | s11:+0.294, s15:+0.082, s4:+0.062 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 117 | 119 | preventive_schedule | 0.485 | 20.73 | 0.00 | s11:+0.294, s15:+0.082, s4:+0.062 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.002 | indefinido | indefinido | s11:+0.561, s15:+0.170, s2:+0.113 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.033 | indefinido | indefinido | s11:+0.553, s15:+0.158, s2:+0.108 |
| 2 | HI_MARKER_D1 | 117 | 118 | preventive_schedule | 0.485 | indefinido | indefinido | s11:+0.294, s15:+0.082, s4:+0.062 |
| 2 | HI_MARKER_D2 | 117 | 119 | preventive_schedule | 0.485 | indefinido | indefinido | s11:+0.294, s15:+0.082, s4:+0.062 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 130 | 131 | preventive_schedule | 0.388 | indefinido | indefinido | s2:+0.231, s4:+0.218, s11:+0.165 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 130 | 132 | preventive_schedule | 0.388 | indefinido | indefinido | s2:+0.231, s4:+0.218, s11:+0.165 |
| 3 | HI_WAIT_SELECTED_D1 | 133 | 134 | preventive_schedule | 0.394 | indefinido | indefinido | s2:+0.227, s4:+0.204, s11:+0.177 |
| 3 | HI_WAIT_SELECTED_D2 | 133 | 135 | preventive_schedule | 0.394 | indefinido | indefinido | s2:+0.227, s4:+0.204, s11:+0.177 |
| 3 | ISO_POINT_M15_D1 | 139 | 140 | preventive_schedule | 0.238 | 13.61 | 13.61 | s4:+0.284, s2:+0.271, s11:+0.209 |
| 3 | ISO_POINT_M15_D2 | 139 | 141 | preventive_schedule | 0.238 | 13.61 | 13.61 | s4:+0.284, s2:+0.271, s11:+0.209 |
| 3 | ISO_LOWER98_M15_D1 | 123 | 124 | preventive_schedule | 0.487 | 32.87 | 9.25 | s4:+0.192, s2:+0.179, s11:+0.144 |
| 3 | ISO_LOWER98_M15_D2 | 123 | 125 | preventive_schedule | 0.487 | 32.87 | 9.25 | s4:+0.192, s2:+0.179, s11:+0.144 |
| 3 | RF_SLOPE_POINT_M15_D1 | 129 | 130 | preventive_schedule | 0.402 | 13.35 | 13.35 | s2:+0.231, s4:+0.208, s11:+0.161 |
| 3 | RF_SLOPE_POINT_M15_D2 | 128 | 130 | preventive_schedule | 0.407 | 16.30 | 16.30 | s2:+0.222, s4:+0.211, s11:+0.163 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 123 | 124 | preventive_schedule | 0.487 | 23.36 | 0.00 | s4:+0.192, s2:+0.179, s11:+0.144 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 123 | 125 | preventive_schedule | 0.487 | 23.36 | 0.00 | s4:+0.192, s2:+0.179, s11:+0.144 |
| 3 | AGE_D1 | indefinido | indefinido | endpoint_without_decision | 0.093 | indefinido | indefinido | s4:+0.344, s2:+0.327, s11:+0.240 |
| 3 | AGE_D2 | indefinido | indefinido | endpoint_without_decision | 0.093 | indefinido | indefinido | s4:+0.344, s2:+0.327, s11:+0.240 |
| 3 | HI_MARKER_D1 | 123 | 124 | preventive_schedule | 0.487 | indefinido | indefinido | s4:+0.192, s2:+0.179, s11:+0.144 |
| 3 | HI_MARKER_D2 | 123 | 125 | preventive_schedule | 0.487 | indefinido | indefinido | s4:+0.192, s2:+0.179, s11:+0.144 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=120, A=120.
- Repetição2: G=117, A=117.
- Repetição3: G=123, A=123.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.50 | 0.29 | 0.00% | 12.50% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.50 | 0.29 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.56 | 0.25 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.56 | 0.25 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.58 | 0.23 | 3.12% | 6.25% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.91 | 0.14 | 0.00% | 9.38% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 23.18 | 15 | 1.56 | 0.36 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 23.18 | 15 | 1.56 | 0.36 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.71 | 0.17 | 3.12% | 6.25% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.03 | 0.17 | 3.12% | 6.25% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 33.23 | 15 | 1.56 | 0.36 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 33.23 | 15 | 1.56 | 0.36 | 0.00% | 12.50% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.56 | 0.36 | 0.00% | 12.50% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.56 | 0.36 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.97 | 0.30 | 0.00% | 15.62% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.97 | 0.30 | 0.00% | 15.62% | 0/32 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 0.97 | 0.21 | 0.00% | 9.38% | 0/32 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 0.97 | 0.21 | 0.00% | 12.50% | 0/32 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.81 | 0.14 | 0.00% | 12.50% | 0/32 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.88 | 0.33 | 0.00% | 15.62% | 0/32 |
| 2 | ISO_LOWER98_M15_D1 | 29.64 | 15 | 0.94 | 0.15 | 0.00% | 18.75% | 0/32 |
| 2 | ISO_LOWER98_M15_D2 | 29.64 | 15 | 0.97 | 0.30 | 0.00% | 15.62% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.44 | 0.30 | 0.00% | 15.62% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.28 | 0.41 | 0.00% | 15.62% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 47.60 | 15 | 0.97 | 0.30 | 0.00% | 15.62% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 47.60 | 15 | 0.97 | 0.30 | 0.00% | 15.62% | 0/32 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 0.97 | 0.30 | 0.00% | 15.62% | 0/32 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 0.97 | 0.30 | 0.00% | 15.62% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.34 | 0.38 | 0.00% | 9.38% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.34 | 0.38 | 0.00% | 9.38% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.25 | 0.30 | 0.00% | 6.25% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.25 | 0.30 | 0.00% | 6.25% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.72 | 0.14 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.72 | 0.17 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 23.62 | 15 | 1.25 | 0.55 | 0.00% | 9.38% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 23.62 | 15 | 1.25 | 0.55 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.56 | 0.04 | 0.00% | 18.75% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.53 | 0.00 | 0.00% | 18.75% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 41.43 | 15 | 1.25 | 0.55 | 0.00% | 9.38% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 41.43 | 15 | 1.25 | 0.55 | 0.00% | 9.38% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.25 | 0.55 | 0.00% | 9.38% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.25 | 0.55 | 0.00% | 9.38% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
