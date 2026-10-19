# FD003, motor41 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u41.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 262 | 263 | preventive_schedule | 0.377 | indefinido | indefinido | s4:+0.393, s2:+0.131, s11:+0.060 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 262 | 264 | preventive_schedule | 0.377 | indefinido | indefinido | s4:+0.393, s2:+0.131, s11:+0.060 |
| 1 | HI_WAIT_SELECTED_D1 | 261 | 262 | preventive_schedule | 0.401 | indefinido | indefinido | s4:+0.377, s2:+0.126, s11:+0.058 |
| 1 | HI_WAIT_SELECTED_D2 | 261 | 263 | preventive_schedule | 0.401 | indefinido | indefinido | s4:+0.377, s2:+0.126, s11:+0.058 |
| 1 | ISO_POINT_M15_D1 | 271 | 272 | preventive_schedule | 0.219 | 15.25 | 15.25 | s4:+0.524, s2:+0.145, s11:+0.067 |
| 1 | ISO_POINT_M15_D2 | 268 | 270 | preventive_schedule | 0.252 | 16.61 | 16.61 | s4:+0.492, s2:+0.148, s11:+0.063 |
| 1 | ISO_LOWER98_M15_D1 | 256 | 257 | preventive_schedule | 0.486 | 35.70 | 12.52 | s4:+0.300, s2:+0.121, s11:+0.059 |
| 1 | ISO_LOWER98_M15_D2 | 256 | 258 | preventive_schedule | 0.486 | 35.70 | 12.52 | s4:+0.300, s2:+0.121, s11:+0.059 |
| 1 | RF_SLOPE_POINT_M15_D1 | 277 | 278 | preventive_schedule | 0.154 | 14.46 | 14.46 | s4:+0.565, s2:+0.154, s11:+0.077 |
| 1 | RF_SLOPE_POINT_M15_D2 | 268 | 270 | preventive_schedule | 0.252 | 16.63 | 16.63 | s4:+0.492, s2:+0.148, s11:+0.063 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 256 | 257 | preventive_schedule | 0.486 | 41.63 | 8.40 | s4:+0.300, s2:+0.121, s11:+0.059 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 256 | 258 | preventive_schedule | 0.486 | 41.63 | 8.40 | s4:+0.300, s2:+0.121, s11:+0.059 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.906 | indefinido | indefinido | s2:+0.047, s4:+0.031, s11:+0.012 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.894 | indefinido | indefinido | s2:+0.053, s4:+0.038, s11:+0.011 |
| 1 | HI_MARKER_D1 | 256 | 257 | preventive_schedule | 0.486 | indefinido | indefinido | s4:+0.300, s2:+0.121, s11:+0.059 |
| 1 | HI_MARKER_D2 | 256 | 258 | preventive_schedule | 0.486 | indefinido | indefinido | s4:+0.300, s2:+0.121, s11:+0.059 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 264 | 265 | preventive_schedule/escolha interna inviável | 0.398 | indefinido | indefinido | s8:+0.508, s15:-0.186, s9:+0.123 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 264 | 266 | preventive_schedule/escolha interna inviável | 0.398 | indefinido | indefinido | s8:+0.508, s15:-0.186, s9:+0.123 |
| 2 | HI_WAIT_SELECTED_D1 | 262 | 263 | preventive_schedule/escolha interna inviável | 0.435 | indefinido | indefinido | s8:+0.484, s15:-0.187, s9:+0.113 |
| 2 | HI_WAIT_SELECTED_D2 | 262 | 264 | preventive_schedule/escolha interna inviável | 0.435 | indefinido | indefinido | s8:+0.484, s15:-0.187, s9:+0.113 |
| 2 | ISO_POINT_M15_D1 | 280 | 281 | preventive_schedule | 0.211 | 15.52 | 15.52 | s8:+0.691, s15:-0.284, s9:+0.169 |
| 2 | ISO_POINT_M15_D2 | 280 | 282 | preventive_schedule | 0.211 | 15.52 | 15.52 | s8:+0.691, s15:-0.284, s9:+0.169 |
| 2 | ISO_LOWER98_M15_D1 | 257 | 258 | preventive_schedule | 0.494 | 37.92 | 12.61 | s8:+0.439, s15:-0.177, s9:+0.104 |
| 2 | ISO_LOWER98_M15_D2 | 257 | 259 | preventive_schedule | 0.494 | 37.92 | 12.61 | s8:+0.439, s15:-0.177, s9:+0.104 |
| 2 | RF_SLOPE_POINT_M15_D1 | 287 | 288 | preventive_schedule | 0.128 | 14.95 | 14.95 | s8:+0.779, s15:-0.324, s9:+0.185 |
| 2 | RF_SLOPE_POINT_M15_D2 | 269 | 271 | preventive_schedule | 0.304 | 16.99 | 16.99 | s8:+0.560, s15:-0.181, s9:+0.136 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 257 | 258 | preventive_schedule | 0.494 | 49.11 | 14.89 | s8:+0.439, s15:-0.177, s9:+0.104 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 257 | 259 | preventive_schedule | 0.494 | 49.11 | 14.89 | s8:+0.439, s15:-0.177, s9:+0.104 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.977 | indefinido | indefinido | s15:-0.037, s9:+0.028, s11:+0.014 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.980 | indefinido | indefinido | s15:-0.040, s9:+0.026, s11:+0.013 |
| 2 | HI_MARKER_D1 | 257 | 258 | preventive_schedule | 0.494 | indefinido | indefinido | s8:+0.439, s15:-0.177, s9:+0.104 |
| 2 | HI_MARKER_D2 | 257 | 259 | preventive_schedule | 0.494 | indefinido | indefinido | s8:+0.439, s15:-0.177, s9:+0.104 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 277 | 278 | preventive_schedule | 0.299 | indefinido | indefinido | s8:+0.422, s15:-0.255, s11:+0.221 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 267 | 269 | preventive_schedule | 0.399 | indefinido | indefinido | s8:+0.345, s15:-0.186, s11:+0.175 |
| 3 | HI_WAIT_SELECTED_D1 | 269 | 270 | preventive_schedule | 0.354 | indefinido | indefinido | s8:+0.362, s11:+0.184, s15:-0.183 |
| 3 | HI_WAIT_SELECTED_D2 | 269 | 271 | preventive_schedule | 0.354 | indefinido | indefinido | s8:+0.362, s11:+0.184, s15:-0.183 |
| 3 | ISO_POINT_M15_D1 | 287 | 288 | preventive_schedule | 0.205 | 13.90 | 13.90 | s8:+0.504, s15:-0.329, s11:+0.261 |
| 3 | ISO_POINT_M15_D2 | 287 | 289 | preventive_schedule | 0.205 | 13.90 | 13.90 | s8:+0.504, s15:-0.329, s11:+0.261 |
| 3 | ISO_LOWER98_M15_D1 | 259 | 260 | preventive_schedule | 0.495 | 41.04 | 13.67 | s8:+0.294, s15:-0.177, s11:+0.165 |
| 3 | ISO_LOWER98_M15_D2 | 259 | 261 | preventive_schedule | 0.495 | 41.04 | 13.67 | s8:+0.294, s15:-0.177, s11:+0.165 |
| 3 | RF_SLOPE_POINT_M15_D1 | 276 | 277 | preventive_schedule | 0.308 | 15.92 | 15.92 | s8:+0.411, s15:-0.249, s11:+0.217 |
| 3 | RF_SLOPE_POINT_M15_D2 | 276 | 278 | preventive_schedule | 0.308 | 15.92 | 15.92 | s8:+0.411, s15:-0.249, s11:+0.217 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 259 | 260 | preventive_schedule | 0.495 | 34.22 | 0.00 | s8:+0.294, s15:-0.177, s11:+0.165 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 259 | 261 | preventive_schedule | 0.495 | 34.22 | 0.00 | s8:+0.294, s15:-0.177, s11:+0.165 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.952 | indefinido | indefinido | s15:-0.037, s11:+0.037, s14:+0.021 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.954 | indefinido | indefinido | s15:-0.040, s11:+0.037, s14:+0.021 |
| 3 | HI_MARKER_D1 | 259 | 260 | preventive_schedule | 0.495 | indefinido | indefinido | s8:+0.294, s15:-0.177, s11:+0.165 |
| 3 | HI_MARKER_D2 | 259 | 261 | preventive_schedule | 0.495 | indefinido | indefinido | s8:+0.294, s15:-0.177, s11:+0.165 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=256, A=256.
- Repetição2: G=257, A=257.
- Repetição3: G=259, A=259.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.47 | 0.30 | 0.00% | 6.25% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.47 | 0.30 | 0.00% | 6.25% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 3.06 | 0.97 | 0.00% | 6.25% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 3.06 | 0.97 | 0.00% | 6.25% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.44 | 0.37 | 0.00% | 6.25% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.09 | 0.20 | 0.00% | 6.25% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 23.18 | 15 | 3.06 | 1.20 | 0.00% | 6.25% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 23.18 | 15 | 3.06 | 1.20 | 0.00% | 6.25% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.44 | 1.22 | 0.00% | 0.00% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.75 | 0.32 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 33.23 | 15 | 3.06 | 1.20 | 0.00% | 6.25% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 33.23 | 15 | 3.06 | 1.20 | 0.00% | 6.25% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 3.06 | 1.20 | 0.00% | 6.25% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 3.06 | 1.20 | 0.00% | 6.25% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.17 | 0.35 | 0.00% | 33.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.17 | 0.35 | 0.00% | 33.33% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.87 | 0.16 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.87 | 0.16 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.20 | 0.88 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.20 | 0.92 | 0.00% | 13.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 25.30 | 15 | 1.87 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 25.30 | 15 | 1.87 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.57 | 0.24 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 3.53 | 0.21 | 0.00% | 53.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 34.21 | 15 | 1.87 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 34.21 | 15 | 1.87 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.87 | 0.35 | 0.00% | 23.33% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.87 | 0.35 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.83 | 0.59 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.77 | 0.59 | 0.00% | 26.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.43 | 0.31 | 0.00% | 13.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.43 | 0.31 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.70 | 0.59 | 0.00% | 10.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.70 | 0.59 | 0.00% | 10.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 27.37 | 15 | 2.43 | 0.83 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 27.37 | 15 | 2.43 | 0.83 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 3.87 | 0.24 | 0.00% | 30.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 3.57 | 0.30 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 46.24 | 15 | 2.43 | 0.83 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 46.24 | 15 | 2.43 | 0.83 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.43 | 0.83 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.43 | 0.83 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
