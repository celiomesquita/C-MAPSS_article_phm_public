# FD001, motor100 — diagnóstico retrospectivo

Critérios de inclusão: median_discordance_d1, median_discordance_d2.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u100.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 178 | 179 | preventive_schedule | 0.290 | indefinido | indefinido | s7:+0.146, s20:+0.125, s12:+0.107 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 178 | 180 | preventive_schedule | 0.290 | indefinido | indefinido | s7:+0.146, s20:+0.125, s12:+0.107 |
| 1 | HI_WAIT_SELECTED_D1 | 173 | 174 | preventive_schedule | 0.351 | indefinido | indefinido | s7:+0.125, s20:+0.123, s12:+0.101 |
| 1 | HI_WAIT_SELECTED_D2 | 173 | 175 | preventive_schedule | 0.351 | indefinido | indefinido | s7:+0.125, s20:+0.123, s12:+0.101 |
| 1 | ISO_POINT_M15_D1 | 177 | 178 | preventive_schedule | 0.301 | 16.00 | 16.00 | s7:+0.143, s20:+0.128, s12:+0.100 |
| 1 | ISO_POINT_M15_D2 | 176 | 178 | preventive_schedule | 0.320 | 16.42 | 16.42 | s7:+0.139, s20:+0.122, s12:+0.101 |
| 1 | ISO_LOWER98_M15_D1 | 163 | 164 | preventive_schedule | 0.487 | 30.20 | 15.31 | s20:+0.100, s7:+0.094, s12:+0.075 |
| 1 | ISO_LOWER98_M15_D2 | 163 | 165 | preventive_schedule | 0.487 | 30.20 | 15.31 | s20:+0.100, s7:+0.094, s12:+0.075 |
| 1 | RF_SLOPE_POINT_M15_D1 | 176 | 177 | preventive_schedule | 0.320 | 15.85 | 15.85 | s7:+0.139, s20:+0.122, s12:+0.101 |
| 1 | RF_SLOPE_POINT_M15_D2 | 176 | 178 | preventive_schedule | 0.320 | 15.85 | 15.85 | s7:+0.139, s20:+0.122, s12:+0.101 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 163 | 164 | preventive_schedule | 0.487 | 33.26 | 10.72 | s20:+0.100, s7:+0.094, s12:+0.075 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 163 | 165 | preventive_schedule | 0.487 | 33.26 | 10.72 | s20:+0.100, s7:+0.094, s12:+0.075 |
| 1 | AGE_D1 | 126 | 127 | preventive_schedule | 0.757 | indefinido | indefinido | s12:+0.045, s7:+0.044, s20:+0.044 |
| 1 | AGE_D2 | 125 | 127 | preventive_schedule | 0.772 | indefinido | indefinido | s20:+0.043, s12:+0.043, s7:+0.036 |
| 1 | HI_MARKER_D1 | 163 | 164 | preventive_schedule | 0.487 | indefinido | indefinido | s20:+0.100, s7:+0.094, s12:+0.075 |
| 1 | HI_MARKER_D2 | 163 | 165 | preventive_schedule | 0.487 | indefinido | indefinido | s20:+0.100, s7:+0.094, s12:+0.075 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 168 | 169 | preventive_schedule | 0.386 | indefinido | indefinido | s7:+0.132, s2:+0.118, s20:+0.091 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 168 | 170 | preventive_schedule | 0.386 | indefinido | indefinido | s7:+0.132, s2:+0.118, s20:+0.091 |
| 2 | HI_WAIT_SELECTED_D1 | 168 | 169 | preventive_schedule | 0.386 | indefinido | indefinido | s7:+0.132, s2:+0.118, s20:+0.091 |
| 2 | HI_WAIT_SELECTED_D2 | 168 | 170 | preventive_schedule | 0.386 | indefinido | indefinido | s7:+0.132, s2:+0.118, s20:+0.091 |
| 2 | ISO_POINT_M15_D1 | 185 | 186 | preventive_schedule | 0.192 | 13.21 | 13.21 | s7:+0.186, s2:+0.134, s20:+0.121 |
| 2 | ISO_POINT_M15_D2 | 179 | 181 | preventive_schedule | 0.258 | 16.55 | 16.55 | s7:+0.170, s2:+0.113, s20:+0.106 |
| 2 | ISO_LOWER98_M15_D1 | 158 | 159 | preventive_schedule | 0.493 | 34.84 | 11.80 | s7:+0.113, s2:+0.091, s20:+0.065 |
| 2 | ISO_LOWER98_M15_D2 | 158 | 160 | preventive_schedule | 0.493 | 34.84 | 11.80 | s7:+0.113, s2:+0.091, s20:+0.065 |
| 2 | RF_SLOPE_POINT_M15_D1 | 179 | 180 | preventive_schedule | 0.258 | 12.54 | 12.54 | s7:+0.170, s2:+0.113, s20:+0.106 |
| 2 | RF_SLOPE_POINT_M15_D2 | 179 | 181 | preventive_schedule | 0.258 | 12.54 | 12.54 | s7:+0.170, s2:+0.113, s20:+0.106 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 159 | 160 | preventive_schedule | 0.484 | 41.91 | 14.61 | s7:+0.113, s2:+0.097, s20:+0.067 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 158 | 160 | preventive_schedule | 0.493 | 43.91 | 16.61 | s7:+0.113, s2:+0.091, s20:+0.065 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.742 | indefinido | indefinido | s2:+0.059, s7:+0.051, s20:+0.036 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.753 | indefinido | indefinido | s2:+0.062, s7:+0.042, s20:+0.036 |
| 2 | HI_MARKER_D1 | 158 | 159 | preventive_schedule | 0.493 | indefinido | indefinido | s7:+0.113, s2:+0.091, s20:+0.065 |
| 2 | HI_MARKER_D2 | 158 | 160 | preventive_schedule | 0.493 | indefinido | indefinido | s7:+0.113, s2:+0.091, s20:+0.065 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 165 | 166 | preventive_schedule | 0.387 | indefinido | indefinido | s20:+0.118, s21:+0.098, s4:+0.087 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 165 | 167 | preventive_schedule | 0.387 | indefinido | indefinido | s20:+0.118, s21:+0.098, s4:+0.087 |
| 3 | HI_WAIT_SELECTED_D1 | 164 | 165 | preventive_schedule | 0.409 | indefinido | indefinido | s20:+0.111, s21:+0.092, s4:+0.084 |
| 3 | HI_WAIT_SELECTED_D2 | 159 | 161 | preventive_schedule | 0.446 | indefinido | indefinido | s20:+0.096, s4:+0.084, s21:+0.079 |
| 3 | ISO_POINT_M15_D1 | 179 | 180 | preventive_schedule | 0.175 | 14.44 | 14.44 | s20:+0.152, s4:+0.127, s21:+0.118 |
| 3 | ISO_POINT_M15_D2 | 179 | 181 | preventive_schedule | 0.175 | 14.44 | 14.44 | s20:+0.152, s4:+0.127, s21:+0.118 |
| 3 | ISO_LOWER98_M15_D1 | 159 | 160 | preventive_schedule | 0.446 | 32.78 | 14.86 | s20:+0.096, s4:+0.084, s21:+0.079 |
| 3 | ISO_LOWER98_M15_D2 | 159 | 161 | preventive_schedule | 0.446 | 32.78 | 14.86 | s20:+0.096, s4:+0.084, s21:+0.079 |
| 3 | RF_SLOPE_POINT_M15_D1 | 177 | 178 | preventive_schedule | 0.192 | 13.96 | 13.96 | s20:+0.152, s4:+0.124, s21:+0.123 |
| 3 | RF_SLOPE_POINT_M15_D2 | 177 | 179 | preventive_schedule | 0.192 | 13.96 | 13.96 | s20:+0.152, s4:+0.124, s21:+0.123 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 155 | 156 | preventive_schedule | 0.486 | 41.11 | 14.90 | s20:+0.097, s4:+0.076, s21:+0.075 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 154 | 156 | preventive_schedule | 0.493 | 42.51 | 16.30 | s20:+0.100, s21:+0.076, s4:+0.073 |
| 3 | AGE_D1 | 126 | 127 | preventive_schedule | 0.734 | indefinido | indefinido | s20:+0.052, s21:+0.043, s4:+0.035 |
| 3 | AGE_D2 | 125 | 127 | preventive_schedule | 0.752 | indefinido | indefinido | s20:+0.051, s21:+0.038, s4:+0.034 |
| 3 | HI_MARKER_D1 | 154 | 155 | preventive_schedule | 0.493 | indefinido | indefinido | s20:+0.100, s21:+0.076, s4:+0.073 |
| 3 | HI_MARKER_D2 | 154 | 156 | preventive_schedule | 0.493 | indefinido | indefinido | s20:+0.100, s21:+0.076, s4:+0.073 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=163, A=163.
- Repetição2: G=158, A=158.
- Repetição3: G=154, A=154.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.67 | 0.61 | 0.00% | 23.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.67 | 0.61 | 0.00% | 23.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.37 | 0.17 | 0.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.37 | 0.17 | 0.00% | 0.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.43 | 0.36 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.47 | 0.68 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 14.89 | 15 | 2.37 | 1.00 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 14.89 | 15 | 2.37 | 1.00 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.70 | 0.65 | 0.00% | 33.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.43 | 1.00 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 22.54 | 15 | 1.73 | 1.26 | 0.00% | 36.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 22.54 | 15 | 1.90 | 1.04 | 0.00% | 23.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.37 | 1.04 | 0.00% | 23.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.37 | 1.04 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.67 | 0.58 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.67 | 0.58 | 0.00% | 20.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.40 | 0.26 | 0.00% | 10.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.40 | 0.26 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.77 | 0.52 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.93 | 0.74 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 23.04 | 15 | 2.40 | 0.86 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 23.04 | 15 | 2.40 | 0.86 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.13 | 1.06 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.27 | 1.17 | 0.00% | 40.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 27.30 | 15 | 2.13 | 0.91 | 0.00% | 26.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 27.30 | 15 | 2.20 | 0.56 | 0.00% | 40.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.40 | 0.86 | 0.00% | 26.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.40 | 0.86 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.03 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.03 | 0.70 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.97 | 0.00 | 0.00% | 10.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.97 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.23 | 0.72 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.23 | 0.72 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 17.91 | 15 | 2.67 | 1.11 | 0.00% | 40.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 17.91 | 15 | 2.67 | 1.11 | 0.00% | 40.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.80 | 0.24 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.33 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 26.21 | 15 | 0.83 | 1.05 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 26.21 | 15 | 0.93 | 0.67 | 0.00% | 40.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.97 | 0.57 | 0.00% | 30.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.97 | 0.57 | 0.00% | 30.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
