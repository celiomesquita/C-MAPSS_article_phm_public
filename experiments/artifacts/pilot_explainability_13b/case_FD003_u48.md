# FD003, motor48 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u48.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 164 | 165 | preventive_schedule | 0.391 | indefinido | indefinido | s11:+0.285, s2:+0.150, s4:+0.135 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 164 | 166 | preventive_schedule | 0.391 | indefinido | indefinido | s11:+0.285, s2:+0.150, s4:+0.135 |
| 1 | HI_WAIT_SELECTED_D1 | 169 | 170 | preventive_schedule | 0.268 | indefinido | indefinido | s11:+0.334, s2:+0.178, s4:+0.172 |
| 1 | HI_WAIT_SELECTED_D2 | 164 | 166 | preventive_schedule | 0.391 | indefinido | indefinido | s11:+0.285, s2:+0.150, s4:+0.135 |
| 1 | ISO_POINT_M15_D1 | 173 | 174 | at_endpoint | 0.169 | 15.40 | 15.40 | s11:+0.372, s4:+0.204, s2:+0.203 |
| 1 | ISO_POINT_M15_D2 | 173 | 175 | late_schedule | 0.169 | 15.40 | 15.40 | s11:+0.372, s4:+0.204, s2:+0.203 |
| 1 | ISO_LOWER98_M15_D1 | 159 | 160 | preventive_schedule | 0.491 | 40.20 | 9.75 | s11:+0.246, s4:+0.118, s2:+0.113 |
| 1 | ISO_LOWER98_M15_D2 | 159 | 161 | preventive_schedule | 0.491 | 40.20 | 9.75 | s11:+0.246, s4:+0.118, s2:+0.113 |
| 1 | RF_SLOPE_POINT_M15_D1 | 169 | 170 | preventive_schedule | 0.268 | 15.39 | 15.39 | s11:+0.334, s2:+0.178, s4:+0.172 |
| 1 | RF_SLOPE_POINT_M15_D2 | 169 | 171 | preventive_schedule | 0.268 | 15.39 | 15.39 | s11:+0.334, s2:+0.178, s4:+0.172 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 159 | 160 | preventive_schedule | 0.491 | 48.06 | 15.16 | s11:+0.246, s4:+0.118, s2:+0.113 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 159 | 161 | preventive_schedule | 0.491 | 48.06 | 15.16 | s11:+0.246, s4:+0.118, s2:+0.113 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.588 | indefinido | indefinido | s11:+0.196, s4:+0.113, s2:+0.082 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.606 | indefinido | indefinido | s11:+0.185, s4:+0.103, s2:+0.084 |
| 1 | HI_MARKER_D1 | 159 | 160 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.246, s4:+0.118, s2:+0.113 |
| 1 | HI_MARKER_D2 | 159 | 161 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.246, s4:+0.118, s2:+0.113 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 166 | 167 | preventive_schedule | 0.290 | indefinido | indefinido | s11:+0.240, s4:+0.220, s9:+0.114 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 163 | 165 | preventive_schedule | 0.388 | indefinido | indefinido | s11:+0.208, s4:+0.189, s9:+0.104 |
| 2 | HI_WAIT_SELECTED_D1 | 157 | 158 | preventive_schedule | 0.457 | indefinido | indefinido | s11:+0.184, s4:+0.172, s9:+0.087 |
| 2 | HI_WAIT_SELECTED_D2 | 157 | 159 | preventive_schedule | 0.457 | indefinido | indefinido | s11:+0.184, s4:+0.172, s9:+0.087 |
| 2 | ISO_POINT_M15_D1 | 173 | 174 | at_endpoint | 0.101 | 12.05 | 12.05 | s4:+0.293, s11:+0.286, s9:+0.143 |
| 2 | ISO_POINT_M15_D2 | 170 | 172 | preventive_schedule | 0.186 | 16.08 | 16.08 | s11:+0.264, s4:+0.260, s9:+0.130 |
| 2 | ISO_LOWER98_M15_D1 | 147 | 148 | preventive_schedule | 0.496 | 37.90 | 14.00 | s4:+0.181, s11:+0.155, s15:+0.065 |
| 2 | ISO_LOWER98_M15_D2 | 147 | 149 | preventive_schedule | 0.496 | 37.90 | 14.00 | s4:+0.181, s11:+0.155, s15:+0.065 |
| 2 | RF_SLOPE_POINT_M15_D1 | 167 | 168 | preventive_schedule | 0.266 | 11.67 | 11.67 | s11:+0.243, s4:+0.232, s9:+0.118 |
| 2 | RF_SLOPE_POINT_M15_D2 | 167 | 169 | preventive_schedule | 0.266 | 11.67 | 11.67 | s11:+0.243, s4:+0.232, s9:+0.118 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 147 | 148 | preventive_schedule | 0.496 | 35.69 | 0.15 | s4:+0.181, s11:+0.155, s15:+0.065 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 147 | 149 | preventive_schedule | 0.496 | 35.69 | 0.15 | s4:+0.181, s11:+0.155, s15:+0.065 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.543 | indefinido | indefinido | s4:+0.162, s11:+0.150, s15:+0.058 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.567 | indefinido | indefinido | s4:+0.147, s11:+0.143, s15:+0.057 |
| 2 | HI_MARKER_D1 | 147 | 148 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.181, s11:+0.155, s15:+0.065 |
| 2 | HI_MARKER_D2 | 147 | 149 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.181, s11:+0.155, s15:+0.065 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 147 | 148 | preventive_schedule | 0.488 | indefinido | indefinido | s4:+0.166, s9:+0.116, s11:+0.095 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 147 | 149 | preventive_schedule | 0.488 | indefinido | indefinido | s4:+0.166, s9:+0.116, s11:+0.095 |
| 3 | HI_WAIT_SELECTED_D1 | 152 | 153 | preventive_schedule | 0.461 | indefinido | indefinido | s4:+0.156, s9:+0.140, s11:+0.105 |
| 3 | HI_WAIT_SELECTED_D2 | 149 | 151 | preventive_schedule | 0.485 | indefinido | indefinido | s4:+0.157, s9:+0.125, s11:+0.102 |
| 3 | ISO_POINT_M15_D1 | 170 | 171 | preventive_schedule | 0.113 | 13.45 | 13.45 | s9:+0.242, s4:+0.239, s11:+0.163 |
| 3 | ISO_POINT_M15_D2 | 170 | 172 | preventive_schedule | 0.113 | 13.45 | 13.45 | s9:+0.242, s4:+0.239, s11:+0.163 |
| 3 | ISO_LOWER98_M15_D1 | 147 | 148 | preventive_schedule | 0.488 | 36.42 | 12.32 | s4:+0.166, s9:+0.116, s11:+0.095 |
| 3 | ISO_LOWER98_M15_D2 | 147 | 149 | preventive_schedule | 0.488 | 36.42 | 12.32 | s4:+0.166, s9:+0.116, s11:+0.095 |
| 3 | RF_SLOPE_POINT_M15_D1 | 166 | 167 | preventive_schedule | 0.227 | 14.66 | 14.66 | s9:+0.213, s4:+0.202, s11:+0.148 |
| 3 | RF_SLOPE_POINT_M15_D2 | 166 | 168 | preventive_schedule | 0.227 | 14.66 | 14.66 | s9:+0.213, s4:+0.202, s11:+0.148 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 147 | 148 | preventive_schedule | 0.488 | 43.88 | 13.37 | s4:+0.166, s9:+0.116, s11:+0.095 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 147 | 149 | preventive_schedule | 0.488 | 43.88 | 13.37 | s4:+0.166, s9:+0.116, s11:+0.095 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.540 | indefinido | indefinido | s4:+0.149, s9:+0.102, s11:+0.093 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.561 | indefinido | indefinido | s4:+0.136, s9:+0.099, s11:+0.088 |
| 3 | HI_MARKER_D1 | 147 | 148 | preventive_schedule | 0.488 | indefinido | indefinido | s4:+0.166, s9:+0.116, s11:+0.095 |
| 3 | HI_MARKER_D2 | 147 | 149 | preventive_schedule | 0.488 | indefinido | indefinido | s4:+0.166, s9:+0.116, s11:+0.095 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=159, A=159.
- Repetição2: G=147, A=147.
- Repetição3: G=147, A=147.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.83 | 0.19 | 0.00% | 13.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.83 | 0.19 | 0.00% | 13.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.89 | 0.19 | 6.67% | 10.00% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.10 | 0.33 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.46 | 0.22 | 13.33% | 10.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.46 | 0.22 | 13.33% | 10.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 30.46 | 15 | 2.10 | 0.58 | 0.00% | 13.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 30.46 | 15 | 2.10 | 0.58 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.38 | 0.19 | 3.33% | 13.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.41 | 0.19 | 3.33% | 13.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 32.89 | 15 | 2.27 | 0.58 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 32.89 | 15 | 2.10 | 0.58 | 0.00% | 13.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.10 | 0.58 | 0.00% | 13.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.10 | 0.58 | 0.00% | 13.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.59 | 0.07 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.06 | 0.25 | 0.00% | 12.50% | 0/32 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.28 | 0.00 | 0.00% | 12.50% | 0/32 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.28 | 0.00 | 0.00% | 12.50% | 0/32 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.39 | 0.20 | 12.50% | 6.25% | 0/32 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.55 | 0.08 | 3.12% | 18.75% | 0/32 |
| 2 | ISO_LOWER98_M15_D1 | 23.90 | 15 | 2.28 | 0.31 | 0.00% | 18.75% | 0/32 |
| 2 | ISO_LOWER98_M15_D2 | 23.90 | 15 | 2.28 | 0.31 | 0.00% | 18.75% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.25 | 0.08 | 0.00% | 18.75% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.25 | 0.08 | 0.00% | 18.75% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 35.54 | 15 | 2.44 | 0.31 | 0.00% | 18.75% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 35.54 | 15 | 2.44 | 0.31 | 0.00% | 18.75% | 0/32 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.28 | 0.31 | 0.00% | 18.75% | 0/32 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.28 | 0.31 | 0.00% | 18.75% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.00 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.00 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.00 | 0.26 | 0.00% | 10.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.00 | 0.40 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.60 | 0.12 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.60 | 0.11 | 0.00% | 10.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 24.10 | 15 | 2.00 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 24.10 | 15 | 2.00 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.93 | 0.86 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.17 | 0.86 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 30.51 | 15 | 2.00 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 30.51 | 15 | 2.00 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.00 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.00 | 0.44 | 0.00% | 16.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
