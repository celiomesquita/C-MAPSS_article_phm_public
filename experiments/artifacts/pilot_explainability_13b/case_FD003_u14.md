# FD003, motor14 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u14.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 174 | 175 | preventive_schedule | 0.295 | indefinido | indefinido | s4:+0.248, s11:+0.240, s20:+0.074 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 174 | 176 | preventive_schedule | 0.295 | indefinido | indefinido | s4:+0.248, s11:+0.240, s20:+0.074 |
| 1 | HI_WAIT_SELECTED_D1 | 162 | 163 | preventive_schedule | 0.404 | indefinido | indefinido | s11:+0.214, s4:+0.209, s20:+0.064 |
| 1 | HI_WAIT_SELECTED_D2 | 162 | 164 | preventive_schedule | 0.404 | indefinido | indefinido | s11:+0.214, s4:+0.209, s20:+0.064 |
| 1 | ISO_POINT_M15_D1 | 181 | 182 | preventive_schedule | 0.168 | 13.43 | 13.43 | s4:+0.315, s11:+0.271, s20:+0.091 |
| 1 | ISO_POINT_M15_D2 | 179 | 181 | preventive_schedule | 0.212 | 16.28 | 16.28 | s4:+0.295, s11:+0.259, s20:+0.083 |
| 1 | ISO_LOWER98_M15_D1 | 152 | 153 | preventive_schedule | 0.491 | 36.82 | 12.33 | s11:+0.184, s4:+0.179, s20:+0.051 |
| 1 | ISO_LOWER98_M15_D2 | 152 | 154 | preventive_schedule | 0.491 | 36.82 | 12.33 | s11:+0.184, s4:+0.179, s20:+0.051 |
| 1 | RF_SLOPE_POINT_M15_D1 | 177 | 178 | preventive_schedule | 0.244 | 14.56 | 14.56 | s4:+0.276, s11:+0.251, s20:+0.078 |
| 1 | RF_SLOPE_POINT_M15_D2 | 177 | 179 | preventive_schedule | 0.244 | 14.56 | 14.56 | s4:+0.276, s11:+0.251, s20:+0.078 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 152 | 153 | preventive_schedule | 0.491 | 32.30 | 6.04 | s11:+0.184, s4:+0.179, s20:+0.051 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 152 | 154 | preventive_schedule | 0.491 | 32.30 | 6.04 | s11:+0.184, s4:+0.179, s20:+0.051 |
| 1 | AGE_D1 | 150 | 151 | preventive_schedule | 0.507 | indefinido | indefinido | s11:+0.177, s4:+0.175, s20:+0.052 |
| 1 | AGE_D2 | 149 | 151 | preventive_schedule | 0.502 | indefinido | indefinido | s11:+0.178, s4:+0.176, s20:+0.051 |
| 1 | HI_MARKER_D1 | 152 | 153 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.184, s4:+0.179, s20:+0.051 |
| 1 | HI_MARKER_D2 | 152 | 154 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.184, s4:+0.179, s20:+0.051 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 165 | 166 | preventive_schedule/escolha interna inviável | 0.391 | indefinido | indefinido | s8:+0.260, s15:+0.157, s4:+0.096 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 165 | 167 | preventive_schedule/escolha interna inviável | 0.391 | indefinido | indefinido | s8:+0.260, s15:+0.157, s4:+0.096 |
| 2 | HI_WAIT_SELECTED_D1 | 161 | 162 | preventive_schedule/escolha interna inviável | 0.433 | indefinido | indefinido | s8:+0.241, s15:+0.157, s4:+0.087 |
| 2 | HI_WAIT_SELECTED_D2 | 161 | 163 | preventive_schedule/escolha interna inviável | 0.433 | indefinido | indefinido | s8:+0.241, s15:+0.157, s4:+0.087 |
| 2 | ISO_POINT_M15_D1 | 180 | 181 | preventive_schedule | 0.221 | 15.52 | 15.52 | s8:+0.312, s15:+0.220, s4:+0.127 |
| 2 | ISO_POINT_M15_D2 | 180 | 182 | preventive_schedule | 0.221 | 15.52 | 15.52 | s8:+0.312, s15:+0.220, s4:+0.127 |
| 2 | ISO_LOWER98_M15_D1 | 156 | 157 | preventive_schedule | 0.493 | 37.21 | 11.91 | s8:+0.209, s15:+0.137, s4:+0.085 |
| 2 | ISO_LOWER98_M15_D2 | 156 | 158 | preventive_schedule | 0.493 | 37.21 | 11.91 | s8:+0.209, s15:+0.137, s4:+0.085 |
| 2 | RF_SLOPE_POINT_M15_D1 | 184 | 185 | preventive_schedule | 0.141 | 15.42 | 15.42 | s8:+0.350, s15:+0.246, s4:+0.137 |
| 2 | RF_SLOPE_POINT_M15_D2 | 184 | 186 | preventive_schedule | 0.141 | 15.42 | 15.42 | s8:+0.350, s15:+0.246, s4:+0.137 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 156 | 157 | preventive_schedule | 0.493 | 43.83 | 9.62 | s8:+0.209, s15:+0.137, s4:+0.085 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 156 | 158 | preventive_schedule | 0.493 | 43.83 | 9.62 | s8:+0.209, s15:+0.137, s4:+0.085 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.610 | indefinido | indefinido | s8:+0.152, s15:+0.098, s4:+0.064 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.618 | indefinido | indefinido | s8:+0.156, s15:+0.094, s4:+0.062 |
| 2 | HI_MARKER_D1 | 156 | 157 | preventive_schedule | 0.493 | indefinido | indefinido | s8:+0.209, s15:+0.137, s4:+0.085 |
| 2 | HI_MARKER_D2 | 156 | 158 | preventive_schedule | 0.493 | indefinido | indefinido | s8:+0.209, s15:+0.137, s4:+0.085 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 175 | 176 | preventive_schedule | 0.296 | indefinido | indefinido | s11:+0.253, s15:+0.153, s8:+0.134 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 164 | 166 | preventive_schedule | 0.390 | indefinido | indefinido | s11:+0.228, s15:+0.131, s8:+0.127 |
| 3 | HI_WAIT_SELECTED_D1 | 164 | 165 | preventive_schedule | 0.390 | indefinido | indefinido | s11:+0.228, s15:+0.131, s8:+0.127 |
| 3 | HI_WAIT_SELECTED_D2 | 164 | 166 | preventive_schedule | 0.390 | indefinido | indefinido | s11:+0.228, s15:+0.131, s8:+0.127 |
| 3 | ISO_POINT_M15_D1 | 181 | 182 | preventive_schedule | 0.170 | 13.69 | 13.69 | s11:+0.277, s15:+0.190, s8:+0.162 |
| 3 | ISO_POINT_M15_D2 | 178 | 180 | preventive_schedule | 0.240 | 16.90 | 16.90 | s11:+0.258, s15:+0.178, s8:+0.144 |
| 3 | ISO_LOWER98_M15_D1 | 154 | 155 | preventive_schedule | 0.489 | 40.28 | 16.00 | s11:+0.189, s15:+0.110, s8:+0.096 |
| 3 | ISO_LOWER98_M15_D2 | 154 | 156 | preventive_schedule | 0.489 | 40.28 | 16.00 | s11:+0.189, s15:+0.110, s8:+0.096 |
| 3 | RF_SLOPE_POINT_M15_D1 | 183 | 184 | preventive_schedule | 0.138 | 13.11 | 13.11 | s11:+0.294, s15:+0.196, s8:+0.172 |
| 3 | RF_SLOPE_POINT_M15_D2 | 183 | 185 | preventive_schedule | 0.138 | 13.11 | 13.11 | s11:+0.294, s15:+0.196, s8:+0.172 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 154 | 155 | preventive_schedule | 0.489 | 41.48 | 0.00 | s11:+0.189, s15:+0.110, s8:+0.096 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 154 | 156 | preventive_schedule | 0.489 | 41.48 | 0.00 | s11:+0.189, s15:+0.110, s8:+0.096 |
| 3 | AGE_D1 | 154 | 155 | preventive_schedule | 0.489 | indefinido | indefinido | s11:+0.189, s15:+0.110, s8:+0.096 |
| 3 | AGE_D2 | 153 | 155 | preventive_schedule | 0.501 | indefinido | indefinido | s11:+0.184, s15:+0.106, s8:+0.093 |
| 3 | HI_MARKER_D1 | 154 | 155 | preventive_schedule | 0.489 | indefinido | indefinido | s11:+0.189, s15:+0.110, s8:+0.096 |
| 3 | HI_MARKER_D2 | 154 | 156 | preventive_schedule | 0.489 | indefinido | indefinido | s11:+0.189, s15:+0.110, s8:+0.096 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=152, A=152.
- Repetição2: G=156, A=156.
- Repetição3: G=154, A=154.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.25 | 0.67 | 0.00% | 25.00% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.25 | 0.67 | 0.00% | 25.00% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.78 | 0.54 | 0.00% | 12.50% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.78 | 0.54 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.34 | 0.37 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.34 | 0.42 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 24.49 | 15 | 2.78 | 1.27 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 24.49 | 15 | 2.78 | 1.27 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.59 | 0.00 | 0.00% | 37.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.41 | 0.29 | 0.00% | 34.38% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 26.26 | 15 | 2.47 | 1.27 | 0.00% | 18.75% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 26.26 | 15 | 2.56 | 1.27 | 0.00% | 18.75% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.78 | 1.27 | 0.00% | 18.75% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.78 | 1.27 | 0.00% | 18.75% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.27 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.27 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.73 | 0.35 | 0.00% | 13.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.73 | 0.35 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.87 | 0.21 | 0.00% | 36.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.87 | 0.20 | 0.00% | 33.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 25.30 | 15 | 1.73 | 0.57 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 25.30 | 15 | 1.73 | 0.57 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.37 | 0.83 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.33 | 0.80 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 34.21 | 15 | 1.73 | 0.57 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 34.21 | 15 | 1.73 | 0.57 | 0.00% | 23.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.73 | 0.57 | 0.00% | 23.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.73 | 0.57 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.20 | 0.71 | 0.00% | 20.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.60 | 0.84 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.40 | 0.30 | 0.00% | 10.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.40 | 0.30 | 0.00% | 10.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.30 | 0.38 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.43 | 0.35 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 24.28 | 15 | 2.40 | 0.72 | 0.00% | 16.67% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 24.28 | 15 | 2.40 | 0.72 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.23 | 0.40 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.10 | 0.44 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 54.70 | 15 | 2.40 | 0.72 | 0.00% | 16.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 54.70 | 15 | 2.40 | 0.72 | 0.00% | 16.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.40 | 0.72 | 0.00% | 16.67% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.40 | 0.72 | 0.00% | 16.67% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
