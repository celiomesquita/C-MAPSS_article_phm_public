# FD003, motor84 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u84.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 197 | 198 | preventive_schedule | 0.490 | indefinido | indefinido | s4:+0.238, s17:+0.110, s15:-0.094 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 197 | 199 | preventive_schedule | 0.490 | indefinido | indefinido | s4:+0.238, s17:+0.110, s15:-0.094 |
| 1 | HI_WAIT_SELECTED_D1 | 199 | 200 | preventive_schedule | 0.462 | indefinido | indefinido | s4:+0.257, s17:+0.113, s15:-0.104 |
| 1 | HI_WAIT_SELECTED_D2 | 199 | 201 | preventive_schedule | 0.462 | indefinido | indefinido | s4:+0.257, s17:+0.113, s15:-0.104 |
| 1 | ISO_POINT_M15_D1 | 220 | 221 | preventive_schedule | 0.131 | 12.12 | 12.12 | s4:+0.411, s15:-0.163, s11:+0.162 |
| 1 | ISO_POINT_M15_D2 | 218 | 220 | preventive_schedule | 0.190 | 16.32 | 16.32 | s4:+0.374, s11:+0.154, s15:-0.154 |
| 1 | ISO_LOWER98_M15_D1 | 198 | 199 | preventive_schedule | 0.474 | 37.42 | 14.45 | s4:+0.247, s17:+0.113, s15:-0.099 |
| 1 | ISO_LOWER98_M15_D2 | 197 | 199 | preventive_schedule | 0.490 | 39.47 | 16.51 | s4:+0.238, s17:+0.110, s15:-0.094 |
| 1 | RF_SLOPE_POINT_M15_D1 | 208 | 209 | preventive_schedule | 0.362 | 15.90 | 15.90 | s4:+0.297, s11:+0.122, s17:+0.119 |
| 1 | RF_SLOPE_POINT_M15_D2 | 208 | 210 | preventive_schedule | 0.362 | 15.90 | 15.90 | s4:+0.297, s11:+0.122, s17:+0.119 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 197 | 198 | preventive_schedule | 0.490 | 31.88 | 0.00 | s4:+0.238, s17:+0.110, s15:-0.094 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 197 | 199 | preventive_schedule | 0.490 | 31.88 | 0.00 | s4:+0.238, s17:+0.110, s15:-0.094 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.890 | indefinido | indefinido | s11:+0.036, s4:+0.029, s15:-0.028 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.906 | indefinido | indefinido | s11:+0.033, s15:-0.031, s9:+0.026 |
| 1 | HI_MARKER_D1 | 197 | 198 | preventive_schedule | 0.490 | indefinido | indefinido | s4:+0.238, s17:+0.110, s15:-0.094 |
| 1 | HI_MARKER_D2 | 197 | 199 | preventive_schedule | 0.490 | indefinido | indefinido | s4:+0.238, s17:+0.110, s15:-0.094 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 202 | 203 | preventive_schedule | 0.398 | indefinido | indefinido | s8:+0.520, s15:-0.276, s11:+0.154 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 202 | 204 | preventive_schedule | 0.398 | indefinido | indefinido | s8:+0.520, s15:-0.276, s11:+0.154 |
| 2 | HI_WAIT_SELECTED_D1 | 206 | 207 | preventive_schedule | 0.339 | indefinido | indefinido | s8:+0.575, s15:-0.299, s11:+0.168 |
| 2 | HI_WAIT_SELECTED_D2 | 206 | 208 | preventive_schedule | 0.339 | indefinido | indefinido | s8:+0.575, s15:-0.299, s11:+0.168 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.000 | 16.02 | 16.02 | s8:+0.922, s15:-0.454, s11:+0.264 |
| 2 | ISO_POINT_M15_D2 | 224 | 226 | at_endpoint | 0.000 | 16.02 | 16.02 | s8:+0.896, s15:-0.458, s11:+0.260 |
| 2 | ISO_LOWER98_M15_D1 | 196 | 197 | preventive_schedule | 0.478 | 84.10 | 10.06 | s8:+0.453, s15:-0.236, s14:+0.131 |
| 2 | ISO_LOWER98_M15_D2 | 196 | 198 | preventive_schedule | 0.478 | 84.10 | 10.06 | s8:+0.453, s15:-0.236, s14:+0.131 |
| 2 | RF_SLOPE_POINT_M15_D1 | 199 | 200 | preventive_schedule | 0.440 | 13.54 | 13.54 | s8:+0.495, s15:-0.271, s11:+0.141 |
| 2 | RF_SLOPE_POINT_M15_D2 | 199 | 201 | preventive_schedule | 0.440 | 13.54 | 13.54 | s8:+0.495, s15:-0.271, s11:+0.141 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 196 | 197 | preventive_schedule | 0.478 | 60.57 | 0.00 | s8:+0.453, s15:-0.236, s14:+0.131 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 196 | 198 | preventive_schedule | 0.478 | 60.57 | 0.00 | s8:+0.453, s15:-0.236, s14:+0.131 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.837 | indefinido | indefinido | s8:+0.133, s15:-0.073, s11:+0.053 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.857 | indefinido | indefinido | s8:+0.131, s15:-0.081, s11:+0.048 |
| 2 | HI_MARKER_D1 | 196 | 197 | preventive_schedule | 0.478 | indefinido | indefinido | s8:+0.453, s15:-0.236, s14:+0.131 |
| 2 | HI_MARKER_D2 | 196 | 198 | preventive_schedule | 0.478 | indefinido | indefinido | s8:+0.453, s15:-0.236, s14:+0.131 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 215 | 216 | preventive_schedule | 0.300 | indefinido | indefinido | s8:+0.476, s15:-0.333, s11:+0.234 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 208 | 210 | preventive_schedule | 0.397 | indefinido | indefinido | s8:+0.405, s15:-0.266, s11:+0.203 |
| 3 | HI_WAIT_SELECTED_D1 | 212 | 213 | preventive_schedule | 0.362 | indefinido | indefinido | s8:+0.446, s15:-0.318, s11:+0.218 |
| 3 | HI_WAIT_SELECTED_D2 | 212 | 214 | preventive_schedule | 0.362 | indefinido | indefinido | s8:+0.446, s15:-0.318, s11:+0.218 |
| 3 | ISO_POINT_M15_D1 | 219 | 220 | preventive_schedule | 0.213 | 13.90 | 13.90 | s8:+0.537, s15:-0.359, s11:+0.259 |
| 3 | ISO_POINT_M15_D2 | 219 | 221 | preventive_schedule | 0.213 | 13.90 | 13.90 | s8:+0.537, s15:-0.359, s11:+0.259 |
| 3 | ISO_LOWER98_M15_D1 | 202 | 203 | preventive_schedule | 0.488 | 41.04 | 13.67 | s8:+0.349, s15:-0.240, s11:+0.175 |
| 3 | ISO_LOWER98_M15_D2 | 202 | 204 | preventive_schedule | 0.488 | 41.04 | 13.67 | s8:+0.349, s15:-0.240, s11:+0.175 |
| 3 | RF_SLOPE_POINT_M15_D1 | 216 | 217 | preventive_schedule | 0.269 | 15.89 | 15.89 | s8:+0.497, s15:-0.331, s11:+0.237 |
| 3 | RF_SLOPE_POINT_M15_D2 | 216 | 218 | preventive_schedule | 0.269 | 15.89 | 15.89 | s8:+0.497, s15:-0.331, s11:+0.237 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 202 | 203 | preventive_schedule | 0.488 | 28.72 | 0.00 | s8:+0.349, s15:-0.240, s11:+0.175 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 202 | 204 | preventive_schedule | 0.488 | 28.72 | 0.00 | s8:+0.349, s15:-0.240, s11:+0.175 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.832 | indefinido | indefinido | s8:+0.098, s11:+0.068, s15:-0.054 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.850 | indefinido | indefinido | s8:+0.096, s11:+0.062, s15:-0.060 |
| 3 | HI_MARKER_D1 | 202 | 203 | preventive_schedule | 0.488 | indefinido | indefinido | s8:+0.349, s15:-0.240, s11:+0.175 |
| 3 | HI_MARKER_D2 | 202 | 204 | preventive_schedule | 0.488 | indefinido | indefinido | s8:+0.349, s15:-0.240, s11:+0.175 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=197, A=197.
- Repetição2: G=196, A=196.
- Repetição3: G=202, A=202.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.31 | 0.28 | 0.00% | 21.88% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.31 | 0.28 | 0.00% | 21.88% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.31 | 0.23 | 0.00% | 18.75% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.31 | 0.23 | 0.00% | 18.75% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.78 | 0.27 | 0.00% | 6.25% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.97 | 0.33 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 22.97 | 15 | 1.38 | 0.37 | 0.00% | 15.62% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 22.97 | 15 | 1.31 | 0.28 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.41 | 0.09 | 0.00% | 31.25% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.38 | 0.22 | 0.00% | 28.12% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.25 | 15 | 1.31 | 0.28 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.25 | 15 | 1.31 | 0.28 | 0.00% | 21.88% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.31 | 0.28 | 0.00% | 21.88% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.31 | 0.28 | 0.00% | 21.88% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.27 | 0.21 | 0.00% | 20.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.27 | 0.21 | 0.00% | 20.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.10 | 0.13 | 0.00% | 0.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.10 | 0.13 | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.61 | 0.32 | 6.67% | 6.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 74.05 | 15 | 1.07 | 0.33 | 0.00% | 10.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 74.05 | 15 | 1.07 | 0.33 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.70 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.70 | 0.32 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 136.85 | 15 | 1.10 | 0.37 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 136.85 | 15 | 1.10 | 0.37 | 0.00% | 10.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.10 | 0.37 | 0.00% | 10.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.10 | 0.37 | 0.00% | 10.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.97 | 0.14 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.57 | 0.26 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.70 | 0.07 | 0.00% | 6.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.70 | 0.07 | 0.00% | 6.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.10 | 0.54 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.10 | 0.54 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 27.37 | 15 | 1.70 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 27.37 | 15 | 1.70 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.93 | 0.09 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.87 | 0.17 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 46.24 | 15 | 1.70 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 46.24 | 15 | 1.70 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.70 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.70 | 0.58 | 0.00% | 20.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
