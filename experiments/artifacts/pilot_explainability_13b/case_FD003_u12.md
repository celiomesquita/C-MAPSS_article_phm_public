# FD003, motor12 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u12.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 151 | 152 | preventive_schedule | 0.389 | indefinido | indefinido | s11:+0.299, s4:+0.147, s2:+0.134 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 151 | 153 | preventive_schedule | 0.389 | indefinido | indefinido | s11:+0.299, s4:+0.147, s2:+0.134 |
| 1 | HI_WAIT_SELECTED_D1 | 158 | 159 | preventive_schedule | 0.262 | indefinido | indefinido | s11:+0.362, s4:+0.170, s2:+0.168 |
| 1 | HI_WAIT_SELECTED_D2 | 153 | 155 | preventive_schedule | 0.366 | indefinido | indefinido | s11:+0.316, s4:+0.146, s2:+0.140 |
| 1 | ISO_POINT_M15_D1 | 163 | 164 | preventive_schedule | 0.180 | 15.40 | 15.40 | s11:+0.391, s4:+0.195, s2:+0.192 |
| 1 | ISO_POINT_M15_D2 | 163 | 165 | preventive_schedule | 0.180 | 15.40 | 15.40 | s11:+0.391, s4:+0.195, s2:+0.192 |
| 1 | ISO_LOWER98_M15_D1 | 148 | 149 | preventive_schedule | 0.470 | 39.46 | 9.00 | s11:+0.258, s4:+0.137, s2:+0.106 |
| 1 | ISO_LOWER98_M15_D2 | 148 | 150 | preventive_schedule | 0.470 | 39.46 | 9.00 | s11:+0.258, s4:+0.137, s2:+0.106 |
| 1 | RF_SLOPE_POINT_M15_D1 | 158 | 159 | preventive_schedule | 0.262 | 15.40 | 15.40 | s11:+0.362, s4:+0.170, s2:+0.168 |
| 1 | RF_SLOPE_POINT_M15_D2 | 158 | 160 | preventive_schedule | 0.262 | 15.40 | 15.40 | s11:+0.362, s4:+0.170, s2:+0.168 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 148 | 149 | preventive_schedule | 0.470 | 41.67 | 8.78 | s11:+0.258, s4:+0.137, s2:+0.106 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 148 | 150 | preventive_schedule | 0.470 | 41.67 | 8.78 | s11:+0.258, s4:+0.137, s2:+0.106 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.550 | indefinido | indefinido | s11:+0.220, s4:+0.110, s2:+0.092 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.566 | indefinido | indefinido | s11:+0.219, s4:+0.104, s2:+0.083 |
| 1 | HI_MARKER_D1 | 148 | 149 | preventive_schedule | 0.470 | indefinido | indefinido | s11:+0.258, s4:+0.137, s2:+0.106 |
| 1 | HI_MARKER_D2 | 148 | 150 | preventive_schedule | 0.470 | indefinido | indefinido | s11:+0.258, s4:+0.137, s2:+0.106 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 153 | 154 | preventive_schedule/escolha interna inviável | 0.396 | indefinido | indefinido | s8:+0.221, s15:+0.155, s4:+0.089 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 153 | 155 | preventive_schedule/escolha interna inviável | 0.396 | indefinido | indefinido | s8:+0.221, s15:+0.155, s4:+0.089 |
| 2 | HI_WAIT_SELECTED_D1 | 149 | 150 | preventive_schedule/escolha interna inviável | 0.446 | indefinido | indefinido | s8:+0.206, s15:+0.146, s4:+0.084 |
| 2 | HI_WAIT_SELECTED_D2 | 149 | 151 | preventive_schedule/escolha interna inviável | 0.446 | indefinido | indefinido | s8:+0.206, s15:+0.146, s4:+0.084 |
| 2 | ISO_POINT_M15_D1 | 160 | 161 | preventive_schedule | 0.216 | 15.52 | 15.52 | s8:+0.287, s15:+0.215, s4:+0.107 |
| 2 | ISO_POINT_M15_D2 | 160 | 162 | preventive_schedule | 0.216 | 15.52 | 15.52 | s8:+0.287, s15:+0.215, s4:+0.107 |
| 2 | ISO_LOWER98_M15_D1 | 144 | 145 | preventive_schedule | 0.486 | 36.50 | 11.20 | s8:+0.187, s15:+0.145, s4:+0.074 |
| 2 | ISO_LOWER98_M15_D2 | 144 | 146 | preventive_schedule | 0.486 | 36.50 | 11.20 | s8:+0.187, s15:+0.145, s4:+0.074 |
| 2 | RF_SLOPE_POINT_M15_D1 | 161 | 162 | preventive_schedule | 0.199 | 9.81 | 9.81 | s8:+0.289, s15:+0.217, s4:+0.111 |
| 2 | RF_SLOPE_POINT_M15_D2 | 160 | 162 | preventive_schedule | 0.216 | 16.18 | 16.18 | s8:+0.287, s15:+0.215, s4:+0.107 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 144 | 145 | preventive_schedule | 0.486 | 27.52 | 0.00 | s8:+0.187, s15:+0.145, s4:+0.074 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 144 | 146 | preventive_schedule | 0.486 | 27.52 | 0.00 | s8:+0.187, s15:+0.145, s4:+0.074 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.493 | indefinido | indefinido | s8:+0.182, s15:+0.146, s4:+0.073 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.486 | indefinido | indefinido | s8:+0.187, s15:+0.145, s4:+0.074 |
| 2 | HI_MARKER_D1 | 144 | 145 | preventive_schedule | 0.486 | indefinido | indefinido | s8:+0.187, s15:+0.145, s4:+0.074 |
| 2 | HI_MARKER_D2 | 144 | 146 | preventive_schedule | 0.486 | indefinido | indefinido | s8:+0.187, s15:+0.145, s4:+0.074 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 148 | 149 | preventive_schedule | 0.493 | indefinido | indefinido | s11:+0.228, s4:+0.151, s20:+0.046 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 148 | 150 | preventive_schedule | 0.493 | indefinido | indefinido | s11:+0.228, s4:+0.151, s20:+0.046 |
| 3 | HI_WAIT_SELECTED_D1 | 153 | 154 | preventive_schedule | 0.395 | indefinido | indefinido | s11:+0.280, s4:+0.162, s20:+0.064 |
| 3 | HI_WAIT_SELECTED_D2 | 150 | 152 | preventive_schedule | 0.451 | indefinido | indefinido | s11:+0.251, s4:+0.158, s20:+0.054 |
| 3 | ISO_POINT_M15_D1 | 166 | 167 | preventive_schedule | 0.162 | 14.99 | 14.99 | s11:+0.368, s4:+0.235, s20:+0.095 |
| 3 | ISO_POINT_M15_D2 | 165 | 167 | preventive_schedule | 0.180 | 16.21 | 16.21 | s11:+0.361, s4:+0.232, s20:+0.087 |
| 3 | ISO_LOWER98_M15_D1 | 148 | 149 | preventive_schedule | 0.493 | 39.67 | 12.00 | s11:+0.228, s4:+0.151, s20:+0.046 |
| 3 | ISO_LOWER98_M15_D2 | 148 | 150 | preventive_schedule | 0.493 | 39.67 | 12.00 | s11:+0.228, s4:+0.151, s20:+0.046 |
| 3 | RF_SLOPE_POINT_M15_D1 | 158 | 159 | preventive_schedule | 0.304 | 15.28 | 15.28 | s11:+0.320, s4:+0.189, s20:+0.069 |
| 3 | RF_SLOPE_POINT_M15_D2 | 158 | 160 | preventive_schedule | 0.304 | 15.28 | 15.28 | s11:+0.320, s4:+0.189, s20:+0.069 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 148 | 149 | preventive_schedule | 0.493 | 42.55 | 10.07 | s11:+0.228, s4:+0.151, s20:+0.046 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 148 | 150 | preventive_schedule | 0.493 | 42.55 | 10.07 | s11:+0.228, s4:+0.151, s20:+0.046 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.570 | indefinido | indefinido | s11:+0.194, s4:+0.121, s20:+0.038 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.580 | indefinido | indefinido | s11:+0.194, s4:+0.115, s20:+0.039 |
| 3 | HI_MARKER_D1 | 148 | 149 | preventive_schedule | 0.493 | indefinido | indefinido | s11:+0.228, s4:+0.151, s20:+0.046 |
| 3 | HI_MARKER_D2 | 148 | 150 | preventive_schedule | 0.493 | indefinido | indefinido | s11:+0.228, s4:+0.151, s20:+0.046 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=148, A=148.
- Repetição2: G=144, A=144.
- Repetição3: G=148, A=148.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.83 | 0.15 | 0.00% | 13.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.83 | 0.15 | 0.00% | 13.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.33 | 0.17 | 0.00% | 0.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.33 | 0.39 | 0.00% | 6.67% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.75 | 0.31 | 6.67% | 13.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.75 | 0.31 | 6.67% | 13.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 30.46 | 15 | 1.33 | 0.52 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 30.46 | 15 | 1.33 | 0.52 | 0.00% | 10.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.00 | 0.35 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.00 | 0.35 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 32.89 | 15 | 1.33 | 0.52 | 0.00% | 10.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 32.89 | 15 | 1.33 | 0.52 | 0.00% | 10.00% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.33 | 0.52 | 0.00% | 10.00% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.33 | 0.52 | 0.00% | 10.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.03 | 0.24 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.03 | 0.24 | 0.00% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.70 | 0.14 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.70 | 0.14 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.73 | 0.09 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.70 | 0.09 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 25.30 | 15 | 1.70 | 0.41 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 25.30 | 15 | 1.70 | 0.41 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.27 | 0.48 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.13 | 0.89 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 34.21 | 15 | 1.70 | 0.41 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 34.21 | 15 | 1.70 | 0.41 | 0.00% | 10.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.70 | 0.41 | 0.00% | 10.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.70 | 0.41 | 0.00% | 10.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.13 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.13 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.13 | 0.04 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.13 | 0.13 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.96 | 0.46 | 10.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.04 | 0.30 | 6.67% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 27.67 | 15 | 1.13 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 27.67 | 15 | 1.13 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.57 | 0.48 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.67 | 0.57 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 32.48 | 15 | 1.23 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 32.48 | 15 | 1.13 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.13 | 0.22 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.13 | 0.22 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
