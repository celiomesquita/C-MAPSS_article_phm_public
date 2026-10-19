# FD001, motor77 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u77.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 146 | 147 | preventive_schedule | 0.294 | indefinido | indefinido | s7:+0.146, s20:+0.105, s12:+0.103 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 146 | 148 | preventive_schedule | 0.294 | indefinido | indefinido | s7:+0.146, s20:+0.105, s12:+0.103 |
| 1 | HI_WAIT_SELECTED_D1 | 144 | 145 | preventive_schedule | 0.343 | indefinido | indefinido | s7:+0.139, s12:+0.096, s20:+0.095 |
| 1 | HI_WAIT_SELECTED_D2 | 144 | 146 | preventive_schedule | 0.343 | indefinido | indefinido | s7:+0.139, s12:+0.096, s20:+0.095 |
| 1 | ISO_POINT_M15_D1 | 146 | 147 | preventive_schedule | 0.294 | 14.91 | 14.91 | s7:+0.146, s20:+0.105, s12:+0.103 |
| 1 | ISO_POINT_M15_D2 | 145 | 147 | preventive_schedule | 0.318 | 16.42 | 16.42 | s7:+0.146, s20:+0.099, s12:+0.097 |
| 1 | ISO_LOWER98_M15_D1 | 134 | 135 | preventive_schedule | 0.496 | 30.20 | 15.31 | s7:+0.101, s12:+0.082, s20:+0.070 |
| 1 | ISO_LOWER98_M15_D2 | 134 | 136 | preventive_schedule | 0.496 | 30.20 | 15.31 | s7:+0.101, s12:+0.082, s20:+0.070 |
| 1 | RF_SLOPE_POINT_M15_D1 | 146 | 147 | preventive_schedule | 0.294 | 15.64 | 15.64 | s7:+0.146, s20:+0.105, s12:+0.103 |
| 1 | RF_SLOPE_POINT_M15_D2 | 146 | 148 | preventive_schedule | 0.294 | 15.64 | 15.64 | s7:+0.146, s20:+0.105, s12:+0.103 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 134 | 135 | preventive_schedule | 0.496 | 31.24 | 8.70 | s7:+0.101, s12:+0.082, s20:+0.070 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 134 | 136 | preventive_schedule | 0.496 | 31.24 | 8.70 | s7:+0.101, s12:+0.082, s20:+0.070 |
| 1 | AGE_D1 | 126 | 127 | preventive_schedule | 0.585 | indefinido | indefinido | s7:+0.080, s12:+0.070, s20:+0.069 |
| 1 | AGE_D2 | 125 | 127 | preventive_schedule | 0.581 | indefinido | indefinido | s7:+0.081, s20:+0.071, s12:+0.069 |
| 1 | HI_MARKER_D1 | 134 | 135 | preventive_schedule | 0.496 | indefinido | indefinido | s7:+0.101, s12:+0.082, s20:+0.070 |
| 1 | HI_MARKER_D2 | 134 | 136 | preventive_schedule | 0.496 | indefinido | indefinido | s7:+0.101, s12:+0.082, s20:+0.070 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 137 | 138 | preventive_schedule | 0.389 | indefinido | indefinido | s2:+0.157, s15:+0.141, s17:+0.059 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 137 | 139 | preventive_schedule | 0.389 | indefinido | indefinido | s2:+0.157, s15:+0.141, s17:+0.059 |
| 2 | HI_WAIT_SELECTED_D1 | 140 | 141 | preventive_schedule | 0.329 | indefinido | indefinido | s2:+0.168, s15:+0.165, s17:+0.068 |
| 2 | HI_WAIT_SELECTED_D2 | 140 | 142 | preventive_schedule | 0.329 | indefinido | indefinido | s2:+0.168, s15:+0.165, s17:+0.068 |
| 2 | ISO_POINT_M15_D1 | 153 | 154 | at_endpoint | 0.135 | 15.14 | 15.14 | s15:+0.205, s2:+0.190, s21:+0.090 |
| 2 | ISO_POINT_M15_D2 | 150 | 152 | preventive_schedule | 0.188 | 16.57 | 16.57 | s15:+0.193, s2:+0.176, s21:+0.085 |
| 2 | ISO_LOWER98_M15_D1 | 130 | 131 | preventive_schedule | 0.495 | 37.87 | 11.00 | s2:+0.129, s15:+0.104, s12:+0.053 |
| 2 | ISO_LOWER98_M15_D2 | 130 | 132 | preventive_schedule | 0.495 | 37.87 | 11.00 | s2:+0.129, s15:+0.104, s12:+0.053 |
| 2 | RF_SLOPE_POINT_M15_D1 | 148 | 149 | preventive_schedule | 0.236 | 12.40 | 12.40 | s15:+0.184, s2:+0.170, s21:+0.078 |
| 2 | RF_SLOPE_POINT_M15_D2 | 148 | 150 | preventive_schedule | 0.236 | 12.40 | 12.40 | s15:+0.184, s2:+0.170, s21:+0.078 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 130 | 131 | preventive_schedule | 0.495 | 29.87 | 0.00 | s2:+0.129, s15:+0.104, s12:+0.053 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 130 | 132 | preventive_schedule | 0.495 | 29.87 | 0.00 | s2:+0.129, s15:+0.104, s12:+0.053 |
| 2 | AGE_D1 | 135 | 136 | preventive_schedule | 0.434 | indefinido | indefinido | s2:+0.142, s15:+0.127, s12:+0.058 |
| 2 | AGE_D2 | 134 | 136 | preventive_schedule | 0.457 | indefinido | indefinido | s2:+0.136, s15:+0.117, s12:+0.055 |
| 2 | HI_MARKER_D1 | 130 | 131 | preventive_schedule | 0.495 | indefinido | indefinido | s2:+0.129, s15:+0.104, s12:+0.053 |
| 2 | HI_MARKER_D2 | 130 | 132 | preventive_schedule | 0.495 | indefinido | indefinido | s2:+0.129, s15:+0.104, s12:+0.053 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 137 | 138 | preventive_schedule | 0.388 | indefinido | indefinido | s4:+0.121, s2:+0.096, s7:+0.078 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 137 | 139 | preventive_schedule | 0.388 | indefinido | indefinido | s4:+0.121, s2:+0.096, s7:+0.078 |
| 3 | HI_WAIT_SELECTED_D1 | 139 | 140 | preventive_schedule | 0.359 | indefinido | indefinido | s4:+0.124, s2:+0.101, s7:+0.085 |
| 3 | HI_WAIT_SELECTED_D2 | 134 | 136 | preventive_schedule | 0.438 | indefinido | indefinido | s4:+0.118, s2:+0.083, s7:+0.073 |
| 3 | ISO_POINT_M15_D1 | 153 | 154 | at_endpoint | 0.113 | 15.64 | 15.64 | s4:+0.185, s7:+0.126, s2:+0.116 |
| 3 | ISO_POINT_M15_D2 | 152 | 154 | at_endpoint | 0.147 | 16.83 | 16.83 | s4:+0.180, s7:+0.119, s2:+0.110 |
| 3 | ISO_LOWER98_M15_D1 | 129 | 130 | preventive_schedule | 0.490 | 40.76 | 15.00 | s4:+0.111, s2:+0.074, s7:+0.065 |
| 3 | ISO_LOWER98_M15_D2 | 129 | 131 | preventive_schedule | 0.490 | 40.76 | 15.00 | s4:+0.111, s2:+0.074, s7:+0.065 |
| 3 | RF_SLOPE_POINT_M15_D1 | 141 | 142 | preventive_schedule | 0.333 | 15.33 | 15.33 | s4:+0.127, s2:+0.104, s7:+0.089 |
| 3 | RF_SLOPE_POINT_M15_D2 | 141 | 143 | preventive_schedule | 0.333 | 15.33 | 15.33 | s4:+0.127, s2:+0.104, s7:+0.089 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 129 | 130 | preventive_schedule | 0.490 | 32.92 | 0.00 | s4:+0.111, s2:+0.074, s7:+0.065 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 129 | 131 | preventive_schedule | 0.490 | 32.92 | 0.00 | s4:+0.111, s2:+0.074, s7:+0.065 |
| 3 | AGE_D1 | 133 | 134 | preventive_schedule | 0.450 | indefinido | indefinido | s4:+0.119, s2:+0.077, s7:+0.072 |
| 3 | AGE_D2 | 132 | 134 | preventive_schedule | 0.457 | indefinido | indefinido | s4:+0.114, s2:+0.080, s7:+0.071 |
| 3 | HI_MARKER_D1 | 129 | 130 | preventive_schedule | 0.490 | indefinido | indefinido | s4:+0.111, s2:+0.074, s7:+0.065 |
| 3 | HI_MARKER_D2 | 129 | 131 | preventive_schedule | 0.490 | indefinido | indefinido | s4:+0.111, s2:+0.074, s7:+0.065 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=134, A=134.
- Repetição2: G=130, A=130.
- Repetição3: G=129, A=129.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.03 | 0.23 | 0.00% | 26.67% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.03 | 0.23 | 0.00% | 26.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.83 | 0.08 | 0.00% | 16.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.83 | 0.08 | 0.00% | 16.67% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.00 | 0.29 | 0.00% | 20.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.07 | 0.23 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 14.89 | 15 | 1.77 | 0.58 | 0.00% | 36.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 14.89 | 15 | 1.77 | 0.58 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.97 | 0.76 | 0.00% | 30.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 3.13 | 1.72 | 0.00% | 16.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 22.54 | 15 | 1.60 | 0.65 | 0.00% | 33.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 22.54 | 15 | 1.73 | 0.65 | 0.00% | 33.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.83 | 0.65 | 0.00% | 33.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.83 | 0.65 | 0.00% | 33.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.30 | 0.58 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.30 | 0.58 | 0.00% | 20.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.87 | 0.00 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.87 | 0.00 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.57 | 0.21 | 23.33% | 20.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.07 | 0.25 | 6.67% | 20.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 26.87 | 15 | 1.87 | 0.30 | 0.00% | 33.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 26.87 | 15 | 1.87 | 0.30 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.67 | 0.90 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.77 | 2.00 | 0.00% | 0.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 35.90 | 15 | 1.87 | 0.30 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 35.90 | 15 | 1.87 | 0.30 | 0.00% | 33.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.87 | 0.30 | 0.00% | 33.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.87 | 0.30 | 0.00% | 33.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.37 | 0.67 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.37 | 0.67 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.57 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.57 | 0.15 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.39 | 0.06 | 40.00% | 40.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.93 | 0.54 | 6.67% | 13.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 25.76 | 15 | 1.57 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 25.76 | 15 | 1.57 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 3.83 | 0.89 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.30 | 1.16 | 0.00% | 36.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 38.50 | 15 | 1.57 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 38.50 | 15 | 1.57 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.57 | 0.50 | 0.00% | 20.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.57 | 0.50 | 0.00% | 20.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
