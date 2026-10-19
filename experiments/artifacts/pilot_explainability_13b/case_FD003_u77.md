# FD003, motor77 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u77.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 222 | 223 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.242, s11:+0.091, s8:+0.086 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 222 | 224 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.242, s11:+0.091, s8:+0.086 |
| 1 | HI_WAIT_SELECTED_D1 | 227 | 228 | preventive_schedule | 0.441 | indefinido | indefinido | s4:+0.266, s11:+0.100, s8:+0.094 |
| 1 | HI_WAIT_SELECTED_D2 | 227 | 229 | preventive_schedule | 0.441 | indefinido | indefinido | s4:+0.266, s11:+0.100, s8:+0.094 |
| 1 | ISO_POINT_M15_D1 | 242 | 243 | preventive_schedule | 0.213 | 15.24 | 15.24 | s4:+0.412, s8:+0.133, s11:+0.111 |
| 1 | ISO_POINT_M15_D2 | 242 | 244 | preventive_schedule | 0.213 | 15.24 | 15.24 | s4:+0.412, s8:+0.133, s11:+0.111 |
| 1 | ISO_LOWER98_M15_D1 | 222 | 223 | preventive_schedule | 0.496 | 33.05 | 2.80 | s4:+0.242, s11:+0.091, s8:+0.086 |
| 1 | ISO_LOWER98_M15_D2 | 222 | 224 | preventive_schedule | 0.496 | 33.05 | 2.80 | s4:+0.242, s11:+0.091, s8:+0.086 |
| 1 | RF_SLOPE_POINT_M15_D1 | 241 | 242 | preventive_schedule | 0.241 | 14.39 | 14.39 | s4:+0.397, s8:+0.129, s11:+0.111 |
| 1 | RF_SLOPE_POINT_M15_D2 | 241 | 243 | preventive_schedule | 0.241 | 14.39 | 14.39 | s4:+0.397, s8:+0.129, s11:+0.111 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 222 | 223 | preventive_schedule | 0.496 | 32.35 | 0.00 | s4:+0.242, s11:+0.091, s8:+0.086 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 222 | 224 | preventive_schedule | 0.496 | 32.35 | 0.00 | s4:+0.242, s11:+0.091, s8:+0.086 |
| 1 | AGE_D1 | 154 | 155 | preventive_schedule | 0.896 | indefinido | indefinido | s4:+0.041, s11:+0.028, s8:+0.016 |
| 1 | AGE_D2 | 153 | 155 | preventive_schedule | 0.907 | indefinido | indefinido | s11:+0.027, s4:+0.026, s2:+0.021 |
| 1 | HI_MARKER_D1 | 222 | 223 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.242, s11:+0.091, s8:+0.086 |
| 1 | HI_MARKER_D2 | 222 | 224 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.242, s11:+0.091, s8:+0.086 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 226 | 227 | preventive_schedule | 0.397 | indefinido | indefinido | s11:+0.217, s4:+0.198, s2:+0.169 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 226 | 228 | preventive_schedule | 0.397 | indefinido | indefinido | s11:+0.217, s4:+0.198, s2:+0.169 |
| 2 | HI_WAIT_SELECTED_D1 | 228 | 229 | preventive_schedule | 0.388 | indefinido | indefinido | s11:+0.227, s4:+0.207, s2:+0.159 |
| 2 | HI_WAIT_SELECTED_D2 | 228 | 230 | preventive_schedule | 0.388 | indefinido | indefinido | s11:+0.227, s4:+0.207, s2:+0.159 |
| 2 | ISO_POINT_M15_D1 | 242 | 243 | preventive_schedule | 0.236 | 15.80 | 15.80 | s4:+0.307, s11:+0.250, s2:+0.185 |
| 2 | ISO_POINT_M15_D2 | 242 | 244 | preventive_schedule | 0.236 | 15.80 | 15.80 | s4:+0.307, s11:+0.250, s2:+0.185 |
| 2 | ISO_LOWER98_M15_D1 | 223 | 224 | preventive_schedule | 0.447 | 33.05 | 14.30 | s11:+0.209, s4:+0.185, s2:+0.144 |
| 2 | ISO_LOWER98_M15_D2 | 223 | 225 | preventive_schedule | 0.447 | 33.05 | 14.30 | s11:+0.209, s4:+0.185, s2:+0.144 |
| 2 | RF_SLOPE_POINT_M15_D1 | 245 | 246 | preventive_schedule | 0.179 | 15.72 | 15.72 | s4:+0.318, s11:+0.273, s2:+0.206 |
| 2 | RF_SLOPE_POINT_M15_D2 | 245 | 247 | preventive_schedule | 0.179 | 15.72 | 15.72 | s4:+0.318, s11:+0.273, s2:+0.206 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 218 | 219 | preventive_schedule | 0.491 | 34.50 | 0.00 | s4:+0.173, s11:+0.170, s2:+0.150 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 218 | 220 | preventive_schedule | 0.491 | 34.50 | 0.00 | s4:+0.173, s11:+0.170, s2:+0.150 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.887 | indefinido | indefinido | s4:+0.040, s11:+0.040, s2:+0.029 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.863 | indefinido | indefinido | s4:+0.048, s2:+0.045, s11:+0.041 |
| 2 | HI_MARKER_D1 | 218 | 219 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.173, s11:+0.170, s2:+0.150 |
| 2 | HI_MARKER_D2 | 218 | 220 | preventive_schedule | 0.491 | indefinido | indefinido | s4:+0.173, s11:+0.170, s2:+0.150 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 242 | 243 | preventive_schedule | 0.391 | indefinido | indefinido | s11:+0.319, s15:-0.223, s4:+0.192 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 242 | 244 | preventive_schedule | 0.391 | indefinido | indefinido | s11:+0.319, s15:-0.223, s4:+0.192 |
| 3 | HI_WAIT_SELECTED_D1 | 239 | 240 | preventive_schedule | 0.440 | indefinido | indefinido | s11:+0.310, s15:-0.216, s4:+0.171 |
| 3 | HI_WAIT_SELECTED_D2 | 239 | 241 | preventive_schedule | 0.440 | indefinido | indefinido | s11:+0.310, s15:-0.216, s4:+0.171 |
| 3 | ISO_POINT_M15_D1 | 254 | 255 | at_endpoint | 0.192 | 13.47 | 13.47 | s11:+0.428, s15:-0.264, s4:+0.218 |
| 3 | ISO_POINT_M15_D2 | 253 | 255 | at_endpoint | 0.212 | 16.80 | 16.80 | s11:+0.418, s15:-0.263, s4:+0.211 |
| 3 | ISO_LOWER98_M15_D1 | 229 | 230 | preventive_schedule | 0.498 | 36.36 | 14.81 | s11:+0.295, s15:-0.173, s4:+0.132 |
| 3 | ISO_LOWER98_M15_D2 | 229 | 231 | preventive_schedule | 0.498 | 36.36 | 14.81 | s11:+0.295, s15:-0.173, s4:+0.132 |
| 3 | RF_SLOPE_POINT_M15_D1 | 248 | 249 | preventive_schedule | 0.295 | 15.62 | 15.62 | s11:+0.373, s15:-0.243, s4:+0.206 |
| 3 | RF_SLOPE_POINT_M15_D2 | 247 | 249 | preventive_schedule | 0.306 | 16.82 | 16.82 | s11:+0.365, s15:-0.235, s4:+0.201 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 229 | 230 | preventive_schedule | 0.498 | 32.48 | 0.00 | s11:+0.295, s15:-0.173, s4:+0.132 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 229 | 231 | preventive_schedule | 0.498 | 32.48 | 0.00 | s11:+0.295, s15:-0.173, s4:+0.132 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.955 | indefinido | indefinido | s15:-0.064, s11:+0.051, s4:+0.025 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.951 | indefinido | indefinido | s15:-0.067, s11:+0.052, s4:+0.030 |
| 3 | HI_MARKER_D1 | 229 | 230 | preventive_schedule | 0.498 | indefinido | indefinido | s11:+0.295, s15:-0.173, s4:+0.132 |
| 3 | HI_MARKER_D2 | 229 | 231 | preventive_schedule | 0.498 | indefinido | indefinido | s11:+0.295, s15:-0.173, s4:+0.132 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=222, A=222.
- Repetição2: G=218, A=218.
- Repetição3: G=229, A=229.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.13 | 0.39 | 0.00% | 23.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.13 | 0.39 | 0.00% | 23.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.13 | 0.13 | 0.00% | 23.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.13 | 0.13 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.20 | 0.13 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.20 | 0.13 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 30.25 | 15 | 2.13 | 0.39 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 30.25 | 15 | 2.13 | 0.39 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.20 | 0.38 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.47 | 0.38 | 0.00% | 20.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 35.95 | 15 | 2.13 | 0.39 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 35.95 | 15 | 2.13 | 0.39 | 0.00% | 23.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.13 | 0.39 | 0.00% | 23.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.13 | 0.39 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.59 | 0.25 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.59 | 0.25 | 0.00% | 12.50% | 0/32 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.91 | 0.14 | 0.00% | 9.38% | 0/32 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.91 | 0.14 | 0.00% | 9.38% | 0/32 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.19 | 0.21 | 0.00% | 12.50% | 0/32 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.19 | 0.21 | 0.00% | 12.50% | 0/32 |
| 2 | ISO_LOWER98_M15_D1 | 18.75 | 15 | 1.69 | 0.36 | 0.00% | 12.50% | 0/32 |
| 2 | ISO_LOWER98_M15_D2 | 18.75 | 15 | 1.69 | 0.36 | 0.00% | 12.50% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.84 | 0.21 | 0.00% | 12.50% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.84 | 0.31 | 0.00% | 9.38% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 42.79 | 15 | 1.84 | 0.45 | 0.00% | 9.38% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 42.79 | 15 | 1.91 | 0.45 | 0.00% | 9.38% | 0/32 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.91 | 0.45 | 0.00% | 9.38% | 0/32 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.91 | 0.45 | 0.00% | 9.38% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.33 | 0.32 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.33 | 0.32 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.47 | 0.00 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.47 | 0.00 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.62 | 0.32 | 20.00% | 16.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.64 | 0.29 | 16.67% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 21.55 | 15 | 2.47 | 0.39 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 21.55 | 15 | 2.47 | 0.39 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.57 | 0.58 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.63 | 0.39 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 52.17 | 15 | 2.47 | 0.39 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 52.17 | 15 | 2.47 | 0.39 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.47 | 0.39 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.47 | 0.39 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
