# FD001, motor19 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u19.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 148 | 149 | preventive_schedule | 0.398 | indefinido | indefinido | s15:+0.109, s12:+0.106, s2:+0.087 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 148 | 150 | preventive_schedule | 0.398 | indefinido | indefinido | s15:+0.109, s12:+0.106, s2:+0.087 |
| 1 | HI_WAIT_SELECTED_D1 | 149 | 150 | preventive_schedule | 0.386 | indefinido | indefinido | s15:+0.111, s12:+0.108, s2:+0.088 |
| 1 | HI_WAIT_SELECTED_D2 | 149 | 151 | preventive_schedule | 0.386 | indefinido | indefinido | s15:+0.111, s12:+0.108, s2:+0.088 |
| 1 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.252 | 23.54 | 23.54 | s15:+0.137, s12:+0.122, s2:+0.111 |
| 1 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.252 | 23.54 | 23.54 | s15:+0.137, s12:+0.122, s2:+0.111 |
| 1 | ISO_LOWER98_M15_D1 | 139 | 140 | preventive_schedule | 0.495 | 42.72 | 10.88 | s15:+0.085, s2:+0.081, s12:+0.079 |
| 1 | ISO_LOWER98_M15_D2 | 139 | 141 | preventive_schedule | 0.495 | 42.72 | 10.88 | s15:+0.085, s2:+0.081, s12:+0.079 |
| 1 | RF_SLOPE_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.252 | 25.91 | 25.91 | s15:+0.137, s12:+0.122, s2:+0.111 |
| 1 | RF_SLOPE_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.252 | 25.91 | 25.91 | s15:+0.137, s12:+0.122, s2:+0.111 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 139 | 140 | preventive_schedule | 0.495 | 42.29 | 4.80 | s15:+0.085, s2:+0.081, s12:+0.079 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 139 | 141 | preventive_schedule | 0.495 | 42.29 | 4.80 | s15:+0.085, s2:+0.081, s12:+0.079 |
| 1 | AGE_D1 | 135 | 136 | preventive_schedule | 0.529 | indefinido | indefinido | s15:+0.079, s2:+0.077, s20:+0.072 |
| 1 | AGE_D2 | 134 | 136 | preventive_schedule | 0.539 | indefinido | indefinido | s2:+0.080, s15:+0.075, s20:+0.072 |
| 1 | HI_MARKER_D1 | 139 | 140 | preventive_schedule | 0.495 | indefinido | indefinido | s15:+0.085, s2:+0.081, s12:+0.079 |
| 1 | HI_MARKER_D2 | 139 | 141 | preventive_schedule | 0.495 | indefinido | indefinido | s15:+0.085, s2:+0.081, s12:+0.079 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 151 | 152 | preventive_schedule | 0.294 | indefinido | indefinido | s4:+0.131, s2:+0.110, s15:+0.106 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 151 | 153 | preventive_schedule | 0.294 | indefinido | indefinido | s4:+0.131, s2:+0.110, s15:+0.106 |
| 2 | HI_WAIT_SELECTED_D1 | 145 | 146 | preventive_schedule | 0.393 | indefinido | indefinido | s4:+0.112, s12:+0.094, s2:+0.092 |
| 2 | HI_WAIT_SELECTED_D2 | 145 | 147 | preventive_schedule | 0.393 | indefinido | indefinido | s4:+0.112, s12:+0.094, s2:+0.092 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.186 | 18.93 | 18.93 | s4:+0.157, s15:+0.134, s2:+0.119 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.186 | 18.93 | 18.93 | s4:+0.157, s15:+0.134, s2:+0.119 |
| 2 | ISO_LOWER98_M15_D1 | 135 | 136 | preventive_schedule | 0.494 | 41.51 | 12.91 | s4:+0.093, s2:+0.082, s15:+0.078 |
| 2 | ISO_LOWER98_M15_D2 | 135 | 137 | preventive_schedule | 0.494 | 41.51 | 12.91 | s4:+0.093, s2:+0.082, s15:+0.078 |
| 2 | RF_SLOPE_POINT_M15_D1 | 156 | 157 | preventive_schedule | 0.208 | 12.38 | 12.38 | s4:+0.151, s15:+0.127, s2:+0.121 |
| 2 | RF_SLOPE_POINT_M15_D2 | 155 | 157 | preventive_schedule | 0.237 | 16.43 | 16.43 | s4:+0.146, s2:+0.119, s15:+0.118 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 135 | 136 | preventive_schedule | 0.494 | 45.01 | 3.64 | s4:+0.093, s2:+0.082, s15:+0.078 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 135 | 137 | preventive_schedule | 0.494 | 45.01 | 3.64 | s4:+0.093, s2:+0.082, s15:+0.078 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.585 | indefinido | indefinido | s15:+0.080, s4:+0.079, s2:+0.067 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.588 | indefinido | indefinido | s4:+0.078, s15:+0.077, s2:+0.069 |
| 2 | HI_MARKER_D1 | 135 | 136 | preventive_schedule | 0.494 | indefinido | indefinido | s4:+0.093, s2:+0.082, s15:+0.078 |
| 2 | HI_MARKER_D2 | 135 | 137 | preventive_schedule | 0.494 | indefinido | indefinido | s4:+0.093, s2:+0.082, s15:+0.078 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 143 | 144 | preventive_schedule | 0.395 | indefinido | indefinido | s20:+0.118, s7:+0.096, s4:+0.087 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 143 | 145 | preventive_schedule | 0.395 | indefinido | indefinido | s20:+0.118, s7:+0.096, s4:+0.087 |
| 3 | HI_WAIT_SELECTED_D1 | 143 | 144 | preventive_schedule | 0.395 | indefinido | indefinido | s20:+0.118, s7:+0.096, s4:+0.087 |
| 3 | HI_WAIT_SELECTED_D2 | 138 | 140 | preventive_schedule | 0.446 | indefinido | indefinido | s20:+0.122, s4:+0.083, s7:+0.079 |
| 3 | ISO_POINT_M15_D1 | 157 | 158 | at_endpoint | 0.158 | 13.30 | 13.30 | s20:+0.150, s4:+0.126, s7:+0.119 |
| 3 | ISO_POINT_M15_D2 | 157 | 159 | late_schedule | 0.158 | 13.30 | 13.30 | s20:+0.150, s4:+0.126, s7:+0.119 |
| 3 | ISO_LOWER98_M15_D1 | 138 | 139 | preventive_schedule | 0.446 | 32.78 | 14.86 | s20:+0.122, s4:+0.083, s7:+0.079 |
| 3 | ISO_LOWER98_M15_D2 | 138 | 140 | preventive_schedule | 0.446 | 32.78 | 14.86 | s20:+0.122, s4:+0.083, s7:+0.079 |
| 3 | RF_SLOPE_POINT_M15_D1 | 156 | 157 | preventive_schedule | 0.193 | 15.07 | 15.07 | s20:+0.137, s4:+0.121, s7:+0.118 |
| 3 | RF_SLOPE_POINT_M15_D2 | 156 | 158 | at_endpoint | 0.193 | 15.07 | 15.07 | s20:+0.137, s4:+0.121, s7:+0.118 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 133 | 134 | preventive_schedule | 0.495 | 38.69 | 12.49 | s20:+0.117, s7:+0.080, s4:+0.072 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 133 | 135 | preventive_schedule | 0.495 | 38.69 | 12.49 | s20:+0.117, s7:+0.080, s4:+0.072 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.554 | indefinido | indefinido | s20:+0.088, s7:+0.068, s4:+0.063 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.564 | indefinido | indefinido | s20:+0.081, s7:+0.066, s4:+0.063 |
| 3 | HI_MARKER_D1 | 133 | 134 | preventive_schedule | 0.495 | indefinido | indefinido | s20:+0.117, s7:+0.080, s4:+0.072 |
| 3 | HI_MARKER_D2 | 133 | 135 | preventive_schedule | 0.495 | indefinido | indefinido | s20:+0.117, s7:+0.080, s4:+0.072 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=139, A=139.
- Repetição2: G=135, A=135.
- Repetição3: G=133, A=133.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.63 | 0.56 | 0.00% | 40.00% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.63 | 0.56 | 0.00% | 40.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.27 | 0.00 | 0.00% | 16.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.27 | 0.00 | 0.00% | 16.67% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 31.84 | 15 | 2.27 | 0.50 | 0.00% | 33.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 31.84 | 15 | 2.27 | 0.50 | 0.00% | 33.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 37.49 | 15 | 2.27 | 0.50 | 0.00% | 33.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 37.49 | 15 | 2.27 | 0.50 | 0.00% | 33.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.27 | 0.50 | 0.00% | 33.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.27 | 0.50 | 0.00% | 33.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.40 | 0.19 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.40 | 0.19 | 0.00% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.97 | 0.04 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.97 | 0.04 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 10.00% | 3.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 10.00% | 3.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 28.60 | 15 | 1.97 | 0.60 | 0.00% | 33.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 28.60 | 15 | 1.97 | 0.60 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.31 | 1.05 | 3.33% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.28 | 0.67 | 3.33% | 40.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 41.37 | 15 | 1.97 | 0.60 | 0.00% | 33.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 41.37 | 15 | 1.97 | 0.60 | 0.00% | 33.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.97 | 0.60 | 0.00% | 33.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.97 | 0.60 | 0.00% | 33.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.20 | 1.25 | 0.00% | 33.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.20 | 1.25 | 0.00% | 33.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.97 | 0.21 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.97 | 0.36 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.48 | 0.25 | 23.33% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.48 | 0.25 | 23.33% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 17.91 | 15 | 2.20 | 0.72 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 17.91 | 15 | 2.20 | 0.72 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.35 | 0.29 | 23.33% | 43.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.41 | 0.29 | 10.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 26.21 | 15 | 1.97 | 0.55 | 0.00% | 33.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 26.21 | 15 | 1.97 | 0.55 | 0.00% | 33.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.97 | 0.55 | 0.00% | 33.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.97 | 0.55 | 0.00% | 33.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
