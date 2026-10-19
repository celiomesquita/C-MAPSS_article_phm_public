# FD003, motor38 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u38.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 183 | 184 | preventive_schedule | 0.364 | indefinido | indefinido | s4:+0.414, s13:+0.256, s15:-0.133 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 183 | 185 | preventive_schedule | 0.364 | indefinido | indefinido | s4:+0.414, s13:+0.256, s15:-0.133 |
| 1 | HI_WAIT_SELECTED_D1 | 188 | 189 | preventive_schedule | 0.283 | indefinido | indefinido | s4:+0.479, s13:+0.286, s15:-0.158 |
| 1 | HI_WAIT_SELECTED_D2 | 188 | 190 | preventive_schedule | 0.283 | indefinido | indefinido | s4:+0.479, s13:+0.286, s15:-0.158 |
| 1 | ISO_POINT_M15_D1 | 191 | 192 | preventive_schedule | 0.237 | 14.33 | 14.33 | s4:+0.502, s13:+0.307, s15:-0.167 |
| 1 | ISO_POINT_M15_D2 | 191 | 193 | preventive_schedule | 0.237 | 14.33 | 14.33 | s4:+0.502, s13:+0.307, s15:-0.167 |
| 1 | ISO_LOWER98_M15_D1 | 179 | 180 | preventive_schedule | 0.453 | 32.82 | 12.36 | s4:+0.363, s13:+0.224, s15:-0.134 |
| 1 | ISO_LOWER98_M15_D2 | 178 | 180 | preventive_schedule | 0.479 | 36.48 | 16.01 | s4:+0.342, s13:+0.222, s15:-0.132 |
| 1 | RF_SLOPE_POINT_M15_D1 | 186 | 187 | preventive_schedule | 0.304 | 13.23 | 13.23 | s4:+0.462, s13:+0.274, s15:-0.150 |
| 1 | RF_SLOPE_POINT_M15_D2 | 186 | 188 | preventive_schedule | 0.304 | 13.23 | 13.23 | s4:+0.462, s13:+0.274, s15:-0.150 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 178 | 179 | preventive_schedule | 0.479 | 25.25 | 0.00 | s4:+0.342, s13:+0.222, s15:-0.132 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 178 | 180 | preventive_schedule | 0.479 | 25.25 | 0.00 | s4:+0.342, s13:+0.222, s15:-0.132 |
| 1 | AGE_D1 | 145 | 146 | preventive_schedule | 0.781 | indefinido | indefinido | s4:+0.147, s13:+0.099, s15:-0.068 |
| 1 | AGE_D2 | 144 | 146 | preventive_schedule | 0.792 | indefinido | indefinido | s4:+0.151, s13:+0.092, s15:-0.074 |
| 1 | HI_MARKER_D1 | 178 | 179 | preventive_schedule | 0.479 | indefinido | indefinido | s4:+0.342, s13:+0.222, s15:-0.132 |
| 1 | HI_MARKER_D2 | 178 | 180 | preventive_schedule | 0.479 | indefinido | indefinido | s4:+0.342, s13:+0.222, s15:-0.132 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 182 | 183 | preventive_schedule | 0.388 | indefinido | indefinido | s8:+0.518, s15:-0.249, s14:+0.143 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 182 | 184 | preventive_schedule | 0.388 | indefinido | indefinido | s8:+0.518, s15:-0.249, s14:+0.143 |
| 2 | HI_WAIT_SELECTED_D1 | 188 | 189 | preventive_schedule | 0.252 | indefinido | indefinido | s8:+0.641, s15:-0.298, s14:+0.167 |
| 2 | HI_WAIT_SELECTED_D2 | 188 | 190 | preventive_schedule | 0.252 | indefinido | indefinido | s8:+0.641, s15:-0.298, s14:+0.167 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.000 | 16.02 | 16.02 | s8:+0.880, s15:-0.428, s11:+0.236 |
| 2 | ISO_POINT_M15_D2 | 199 | 201 | at_endpoint | 0.000 | 16.02 | 16.02 | s8:+0.857, s15:-0.413, s11:+0.228 |
| 2 | ISO_LOWER98_M15_D1 | 178 | 179 | preventive_schedule | 0.488 | 87.77 | 13.72 | s8:+0.454, s15:-0.249, s14:+0.128 |
| 2 | ISO_LOWER98_M15_D2 | 178 | 180 | preventive_schedule | 0.488 | 87.77 | 13.72 | s8:+0.454, s15:-0.249, s14:+0.128 |
| 2 | RF_SLOPE_POINT_M15_D1 | 183 | 184 | preventive_schedule | 0.353 | 13.65 | 13.65 | s8:+0.539, s15:-0.251, s14:+0.147 |
| 2 | RF_SLOPE_POINT_M15_D2 | 183 | 185 | preventive_schedule | 0.353 | 13.65 | 13.65 | s8:+0.539, s15:-0.251, s14:+0.147 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 178 | 179 | preventive_schedule | 0.488 | 32.67 | 0.00 | s8:+0.454, s15:-0.249, s14:+0.128 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 178 | 180 | preventive_schedule | 0.488 | 32.67 | 0.00 | s8:+0.454, s15:-0.249, s14:+0.128 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.862 | indefinido | indefinido | s8:+0.191, s15:-0.143, s14:+0.048 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.888 | indefinido | indefinido | s8:+0.178, s15:-0.153, s14:+0.046 |
| 2 | HI_MARKER_D1 | 178 | 179 | preventive_schedule | 0.488 | indefinido | indefinido | s8:+0.454, s15:-0.249, s14:+0.128 |
| 2 | HI_MARKER_D2 | 178 | 180 | preventive_schedule | 0.488 | indefinido | indefinido | s8:+0.454, s15:-0.249, s14:+0.128 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 183 | 184 | preventive_schedule | 0.385 | indefinido | indefinido | s4:+0.258, s17:+0.162, s11:+0.143 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 183 | 185 | preventive_schedule | 0.385 | indefinido | indefinido | s4:+0.258, s17:+0.162, s11:+0.143 |
| 3 | HI_WAIT_SELECTED_D1 | 188 | 189 | preventive_schedule | 0.308 | indefinido | indefinido | s4:+0.298, s17:+0.176, s11:+0.163 |
| 3 | HI_WAIT_SELECTED_D2 | 188 | 190 | preventive_schedule | 0.308 | indefinido | indefinido | s4:+0.298, s17:+0.176, s11:+0.163 |
| 3 | ISO_POINT_M15_D1 | 187 | 188 | preventive_schedule | 0.316 | 15.86 | 15.86 | s4:+0.303, s17:+0.172, s11:+0.156 |
| 3 | ISO_POINT_M15_D2 | 187 | 189 | preventive_schedule | 0.316 | 15.86 | 15.86 | s4:+0.303, s17:+0.172, s11:+0.156 |
| 3 | ISO_LOWER98_M15_D1 | 178 | 179 | preventive_schedule | 0.491 | 33.41 | 13.00 | s4:+0.213, s17:+0.136, s11:+0.121 |
| 3 | ISO_LOWER98_M15_D2 | 178 | 180 | preventive_schedule | 0.491 | 33.41 | 13.00 | s4:+0.213, s17:+0.136, s11:+0.121 |
| 3 | RF_SLOPE_POINT_M15_D1 | 189 | 190 | preventive_schedule | 0.292 | 14.55 | 14.55 | s4:+0.302, s17:+0.179, s11:+0.172 |
| 3 | RF_SLOPE_POINT_M15_D2 | 187 | 189 | preventive_schedule | 0.316 | 16.67 | 16.67 | s4:+0.303, s17:+0.172, s11:+0.156 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 178 | 179 | preventive_schedule | 0.491 | 29.68 | 0.00 | s4:+0.213, s17:+0.136, s11:+0.121 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 178 | 180 | preventive_schedule | 0.491 | 29.68 | 0.00 | s4:+0.213, s17:+0.136, s11:+0.121 |
| 3 | AGE_D1 | 154 | 155 | preventive_schedule | 0.754 | indefinido | indefinido | s4:+0.109, s17:+0.083, s15:-0.061 |
| 3 | AGE_D2 | 153 | 155 | preventive_schedule | 0.776 | indefinido | indefinido | s4:+0.098, s17:+0.080, s15:-0.059 |
| 3 | HI_MARKER_D1 | 178 | 179 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.213, s17:+0.136, s11:+0.121 |
| 3 | HI_MARKER_D2 | 178 | 180 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.213, s17:+0.136, s11:+0.121 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=178, A=178.
- Repetição2: G=178, A=178.
- Repetição3: G=178, A=178.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.16 | 0.47 | 0.00% | 6.25% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.16 | 0.47 | 0.00% | 6.25% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.22 | 0.06 | 0.00% | 3.12% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.22 | 0.06 | 0.00% | 3.12% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.59 | 0.40 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.59 | 0.40 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 20.47 | 15 | 1.25 | 0.50 | 0.00% | 12.50% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 20.47 | 15 | 1.22 | 0.43 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.34 | 0.39 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.34 | 0.46 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 52.73 | 15 | 1.22 | 0.43 | 0.00% | 12.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 52.73 | 15 | 1.22 | 0.43 | 0.00% | 12.50% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.22 | 0.43 | 0.00% | 12.50% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.22 | 0.43 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.70 | 0.16 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.70 | 0.16 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.20 | 0.07 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.20 | 0.07 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.56 | 0.28 | 10.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 74.05 | 15 | 1.13 | 0.40 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 74.05 | 15 | 1.13 | 0.40 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.00 | 0.21 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.00 | 0.20 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 136.85 | 15 | 1.20 | 0.40 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 136.85 | 15 | 1.20 | 0.40 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.20 | 0.40 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.20 | 0.40 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.03 | 0.15 | 0.00% | 18.75% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.03 | 0.15 | 0.00% | 18.75% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.16 | 0.00 | 0.00% | 6.25% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.16 | 0.00 | 0.00% | 6.25% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.19 | 0.35 | 0.00% | 18.75% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.19 | 0.35 | 0.00% | 18.75% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 20.41 | 15 | 1.16 | 0.31 | 0.00% | 18.75% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 20.41 | 15 | 1.16 | 0.31 | 0.00% | 18.75% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.19 | 0.42 | 0.00% | 18.75% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.31 | 0.24 | 0.00% | 21.88% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 35.75 | 15 | 1.16 | 0.31 | 0.00% | 18.75% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 35.75 | 15 | 1.16 | 0.31 | 0.00% | 18.75% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.16 | 0.31 | 0.00% | 18.75% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.16 | 0.31 | 0.00% | 18.75% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
