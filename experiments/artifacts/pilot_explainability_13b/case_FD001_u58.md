# FD001, motor58 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u58.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 132 | 133 | preventive_schedule | 0.389 | indefinido | indefinido | s2:+0.112, s12:+0.101, s15:+0.098 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 132 | 134 | preventive_schedule | 0.389 | indefinido | indefinido | s2:+0.112, s12:+0.101, s15:+0.098 |
| 1 | HI_WAIT_SELECTED_D1 | 135 | 136 | preventive_schedule | 0.335 | indefinido | indefinido | s2:+0.131, s12:+0.107, s15:+0.103 |
| 1 | HI_WAIT_SELECTED_D2 | 135 | 137 | preventive_schedule | 0.335 | indefinido | indefinido | s2:+0.131, s12:+0.107, s15:+0.103 |
| 1 | ISO_POINT_M15_D1 | 146 | 147 | at_endpoint | 0.079 | 15.34 | 15.34 | s2:+0.179, s12:+0.134, s15:+0.134 |
| 1 | ISO_POINT_M15_D2 | 145 | 147 | at_endpoint | 0.101 | 16.10 | 16.10 | s2:+0.171, s21:+0.134, s15:+0.130 |
| 1 | ISO_LOWER98_M15_D1 | 125 | 126 | preventive_schedule | 0.493 | 42.72 | 10.88 | s2:+0.095, s15:+0.089, s12:+0.075 |
| 1 | ISO_LOWER98_M15_D2 | 125 | 127 | preventive_schedule | 0.493 | 42.72 | 10.88 | s2:+0.095, s15:+0.089, s12:+0.075 |
| 1 | RF_SLOPE_POINT_M15_D1 | 143 | 144 | preventive_schedule | 0.171 | 14.95 | 14.95 | s2:+0.152, s12:+0.128, s21:+0.121 |
| 1 | RF_SLOPE_POINT_M15_D2 | 142 | 144 | preventive_schedule | 0.187 | 16.24 | 16.24 | s2:+0.150, s12:+0.127, s21:+0.122 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 125 | 126 | preventive_schedule | 0.493 | 48.65 | 11.17 | s2:+0.095, s15:+0.089, s12:+0.075 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 125 | 127 | preventive_schedule | 0.493 | 48.65 | 11.17 | s2:+0.095, s15:+0.089, s12:+0.075 |
| 1 | AGE_D1 | 135 | 136 | preventive_schedule | 0.335 | indefinido | indefinido | s2:+0.131, s12:+0.107, s15:+0.103 |
| 1 | AGE_D2 | 134 | 136 | preventive_schedule | 0.361 | indefinido | indefinido | s2:+0.122, s12:+0.106, s15:+0.096 |
| 1 | HI_MARKER_D1 | 125 | 126 | preventive_schedule | 0.493 | indefinido | indefinido | s2:+0.095, s15:+0.089, s12:+0.075 |
| 1 | HI_MARKER_D2 | 125 | 127 | preventive_schedule | 0.493 | indefinido | indefinido | s2:+0.095, s15:+0.089, s12:+0.075 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 138 | 139 | preventive_schedule | 0.283 | indefinido | indefinido | s7:+0.157, s11:+0.107, s2:+0.097 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 138 | 140 | preventive_schedule | 0.283 | indefinido | indefinido | s7:+0.157, s11:+0.107, s2:+0.097 |
| 2 | HI_WAIT_SELECTED_D1 | 135 | 136 | preventive_schedule | 0.371 | indefinido | indefinido | s7:+0.130, s11:+0.097, s2:+0.086 |
| 2 | HI_WAIT_SELECTED_D2 | 135 | 137 | preventive_schedule | 0.371 | indefinido | indefinido | s7:+0.130, s11:+0.097, s2:+0.086 |
| 2 | ISO_POINT_M15_D1 | 144 | 145 | preventive_schedule | 0.139 | 15.18 | 15.18 | s7:+0.208, s11:+0.130, s4:+0.107 |
| 2 | ISO_POINT_M15_D2 | 144 | 146 | preventive_schedule | 0.139 | 15.18 | 15.18 | s7:+0.208, s11:+0.130, s4:+0.107 |
| 2 | ISO_LOWER98_M15_D1 | 125 | 126 | preventive_schedule | 0.487 | 35.15 | 7.95 | s7:+0.119, s11:+0.078, s4:+0.065 |
| 2 | ISO_LOWER98_M15_D2 | 125 | 127 | preventive_schedule | 0.487 | 35.15 | 7.95 | s7:+0.119, s11:+0.078, s4:+0.065 |
| 2 | RF_SLOPE_POINT_M15_D1 | 137 | 138 | preventive_schedule | 0.307 | 14.98 | 14.98 | s7:+0.150, s11:+0.105, s2:+0.095 |
| 2 | RF_SLOPE_POINT_M15_D2 | 137 | 139 | preventive_schedule | 0.307 | 14.98 | 14.98 | s7:+0.150, s11:+0.105, s2:+0.095 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 125 | 126 | preventive_schedule | 0.487 | 21.93 | 0.00 | s7:+0.119, s11:+0.078, s4:+0.065 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 125 | 127 | preventive_schedule | 0.487 | 21.93 | 0.00 | s7:+0.119, s11:+0.078, s4:+0.065 |
| 2 | AGE_D1 | 135 | 136 | preventive_schedule | 0.371 | indefinido | indefinido | s7:+0.130, s11:+0.097, s2:+0.086 |
| 2 | AGE_D2 | 134 | 136 | preventive_schedule | 0.391 | indefinido | indefinido | s7:+0.127, s11:+0.097, s4:+0.084 |
| 2 | HI_MARKER_D1 | 125 | 126 | preventive_schedule | 0.487 | indefinido | indefinido | s7:+0.119, s11:+0.078, s4:+0.065 |
| 2 | HI_MARKER_D2 | 125 | 127 | preventive_schedule | 0.487 | indefinido | indefinido | s7:+0.119, s11:+0.078, s4:+0.065 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 136 | 137 | preventive_schedule | 0.273 | indefinido | indefinido | s4:+0.146, s20:+0.105, s12:+0.097 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 136 | 138 | preventive_schedule | 0.273 | indefinido | indefinido | s4:+0.146, s20:+0.105, s12:+0.097 |
| 3 | HI_WAIT_SELECTED_D1 | 133 | 134 | preventive_schedule | 0.342 | indefinido | indefinido | s4:+0.135, s20:+0.096, s12:+0.093 |
| 3 | HI_WAIT_SELECTED_D2 | 133 | 135 | preventive_schedule | 0.342 | indefinido | indefinido | s4:+0.135, s20:+0.096, s12:+0.093 |
| 3 | ISO_POINT_M15_D1 | 140 | 141 | preventive_schedule | 0.172 | 14.48 | 14.48 | s4:+0.162, s20:+0.122, s12:+0.107 |
| 3 | ISO_POINT_M15_D2 | 138 | 140 | preventive_schedule | 0.223 | 16.93 | 16.93 | s4:+0.159, s20:+0.113, s12:+0.099 |
| 3 | ISO_LOWER98_M15_D1 | 123 | 124 | preventive_schedule | 0.497 | 41.11 | 15.70 | s4:+0.104, s7:+0.071, s20:+0.064 |
| 3 | ISO_LOWER98_M15_D2 | 123 | 125 | preventive_schedule | 0.497 | 41.11 | 15.70 | s4:+0.104, s7:+0.071, s20:+0.064 |
| 3 | RF_SLOPE_POINT_M15_D1 | 136 | 137 | preventive_schedule | 0.273 | 12.51 | 12.51 | s4:+0.146, s20:+0.105, s12:+0.097 |
| 3 | RF_SLOPE_POINT_M15_D2 | 136 | 138 | preventive_schedule | 0.273 | 12.51 | 12.51 | s4:+0.146, s20:+0.105, s12:+0.097 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 123 | 124 | preventive_schedule | 0.497 | 42.99 | 8.10 | s4:+0.104, s7:+0.071, s20:+0.064 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 123 | 125 | preventive_schedule | 0.497 | 42.99 | 8.10 | s4:+0.104, s7:+0.071, s20:+0.064 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.455 | indefinido | indefinido | s4:+0.113, s7:+0.070, s12:+0.069 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.464 | indefinido | indefinido | s4:+0.110, s7:+0.073, s20:+0.068 |
| 3 | HI_MARKER_D1 | 123 | 124 | preventive_schedule | 0.497 | indefinido | indefinido | s4:+0.104, s7:+0.071, s20:+0.064 |
| 3 | HI_MARKER_D2 | 123 | 125 | preventive_schedule | 0.497 | indefinido | indefinido | s4:+0.104, s7:+0.071, s20:+0.064 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=125, A=125.
- Repetição2: G=125, A=125.
- Repetição3: G=123, A=123.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.50 | 0.83 | 0.00% | 23.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.50 | 0.83 | 0.00% | 23.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.13 | 0.37 | 0.00% | 10.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.13 | 0.37 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.72 | 0.54 | 16.67% | 13.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.57 | 0.22 | 6.67% | 10.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 31.84 | 15 | 2.13 | 0.67 | 0.00% | 30.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 31.84 | 15 | 2.13 | 0.67 | 0.00% | 30.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.13 | 2.64 | 0.00% | 6.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.23 | 3.37 | 0.00% | 0.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 37.49 | 15 | 2.13 | 0.67 | 0.00% | 30.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 37.49 | 15 | 2.13 | 0.67 | 0.00% | 30.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.13 | 0.67 | 0.00% | 30.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.13 | 0.67 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.80 | 0.33 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.80 | 0.33 | 0.00% | 20.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.90 | 0.27 | 0.00% | 0.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.90 | 0.27 | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.77 | 0.43 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.73 | 0.45 | 0.00% | 3.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 27.21 | 15 | 1.90 | 0.61 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 27.21 | 15 | 1.90 | 0.61 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.40 | 0.36 | 0.00% | 63.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.40 | 0.70 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 36.76 | 15 | 1.90 | 0.61 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 36.76 | 15 | 1.90 | 0.61 | 0.00% | 23.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.90 | 0.61 | 0.00% | 23.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.90 | 0.61 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.83 | 0.26 | 0.00% | 10.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.83 | 0.26 | 0.00% | 10.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.13 | 0.25 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.13 | 0.25 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.83 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.87 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.41 | 15 | 2.10 | 0.89 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.41 | 15 | 2.10 | 0.89 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.20 | 0.43 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.17 | 0.45 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 34.89 | 15 | 2.63 | 0.37 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 34.89 | 15 | 2.50 | 0.35 | 0.00% | 33.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.13 | 0.95 | 0.00% | 33.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.13 | 0.95 | 0.00% | 33.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
