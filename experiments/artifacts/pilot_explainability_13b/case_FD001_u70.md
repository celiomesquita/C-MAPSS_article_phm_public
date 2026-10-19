# FD001, motor70 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD001_u70.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 121 | 122 | preventive_schedule | 0.393 | indefinido | indefinido | s15:+0.098, s4:+0.086, s7:+0.084 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 121 | 123 | preventive_schedule | 0.393 | indefinido | indefinido | s15:+0.098, s4:+0.086, s7:+0.084 |
| 1 | HI_WAIT_SELECTED_D1 | 125 | 126 | preventive_schedule | 0.305 | indefinido | indefinido | s15:+0.122, s4:+0.100, s7:+0.100 |
| 1 | HI_WAIT_SELECTED_D2 | 125 | 127 | preventive_schedule | 0.305 | indefinido | indefinido | s15:+0.122, s4:+0.100, s7:+0.100 |
| 1 | ISO_POINT_M15_D1 | 130 | 131 | preventive_schedule | 0.202 | 14.37 | 14.37 | s15:+0.137, s4:+0.112, s7:+0.110 |
| 1 | ISO_POINT_M15_D2 | 130 | 132 | preventive_schedule | 0.202 | 14.37 | 14.37 | s15:+0.137, s4:+0.112, s7:+0.110 |
| 1 | ISO_LOWER98_M15_D1 | 115 | 116 | preventive_schedule | 0.492 | 37.62 | 9.00 | s7:+0.080, s15:+0.069, s4:+0.065 |
| 1 | ISO_LOWER98_M15_D2 | 115 | 117 | preventive_schedule | 0.492 | 37.62 | 9.00 | s7:+0.080, s15:+0.069, s4:+0.065 |
| 1 | RF_SLOPE_POINT_M15_D1 | 130 | 131 | preventive_schedule | 0.202 | 13.88 | 13.88 | s15:+0.137, s4:+0.112, s7:+0.110 |
| 1 | RF_SLOPE_POINT_M15_D2 | 130 | 132 | preventive_schedule | 0.202 | 13.88 | 13.88 | s15:+0.137, s4:+0.112, s7:+0.110 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 115 | 116 | preventive_schedule | 0.492 | 36.75 | 0.00 | s7:+0.080, s15:+0.069, s4:+0.065 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 115 | 117 | preventive_schedule | 0.492 | 36.75 | 0.00 | s7:+0.080, s15:+0.069, s4:+0.065 |
| 1 | AGE_D1 | indefinido | indefinido | endpoint_without_decision | 0.033 | indefinido | indefinido | s15:+0.153, s7:+0.136, s4:+0.121 |
| 1 | AGE_D2 | indefinido | indefinido | endpoint_without_decision | 0.033 | indefinido | indefinido | s15:+0.153, s7:+0.136, s4:+0.121 |
| 1 | HI_MARKER_D1 | 115 | 116 | preventive_schedule | 0.492 | indefinido | indefinido | s7:+0.080, s15:+0.069, s4:+0.065 |
| 1 | HI_MARKER_D2 | 115 | 117 | preventive_schedule | 0.492 | indefinido | indefinido | s7:+0.080, s15:+0.069, s4:+0.065 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 124 | 125 | preventive_schedule | 0.288 | indefinido | indefinido | s4:+0.088, s12:+0.088, s3:+0.076 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 124 | 126 | preventive_schedule | 0.288 | indefinido | indefinido | s4:+0.088, s12:+0.088, s3:+0.076 |
| 2 | HI_WAIT_SELECTED_D1 | 122 | 123 | preventive_schedule | 0.327 | indefinido | indefinido | s12:+0.088, s4:+0.084, s3:+0.068 |
| 2 | HI_WAIT_SELECTED_D2 | 122 | 124 | preventive_schedule | 0.327 | indefinido | indefinido | s12:+0.088, s4:+0.084, s3:+0.068 |
| 2 | ISO_POINT_M15_D1 | 134 | 135 | preventive_schedule | 0.033 | 15.23 | 15.23 | s12:+0.135, s4:+0.110, s21:+0.091 |
| 2 | ISO_POINT_M15_D2 | 134 | 136 | preventive_schedule | 0.033 | 15.23 | 15.23 | s12:+0.135, s4:+0.110, s21:+0.091 |
| 2 | ISO_LOWER98_M15_D1 | 112 | 113 | preventive_schedule | 0.488 | 49.77 | 10.49 | s12:+0.090, s4:+0.057, s21:+0.055 |
| 2 | ISO_LOWER98_M15_D2 | 112 | 114 | preventive_schedule | 0.488 | 49.77 | 10.49 | s12:+0.090, s4:+0.057, s21:+0.055 |
| 2 | RF_SLOPE_POINT_M15_D1 | 124 | 125 | preventive_schedule | 0.288 | 14.69 | 14.69 | s4:+0.088, s12:+0.088, s3:+0.076 |
| 2 | RF_SLOPE_POINT_M15_D2 | 124 | 126 | preventive_schedule | 0.288 | 14.69 | 14.69 | s4:+0.088, s12:+0.088, s3:+0.076 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 112 | 113 | preventive_schedule | 0.488 | 40.73 | 0.00 | s12:+0.090, s4:+0.057, s21:+0.055 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 112 | 114 | preventive_schedule | 0.488 | 40.73 | 0.00 | s12:+0.090, s4:+0.057, s21:+0.055 |
| 2 | AGE_D1 | 126 | 127 | preventive_schedule | 0.243 | indefinido | indefinido | s12:+0.095, s4:+0.094, s3:+0.081 |
| 2 | AGE_D2 | 125 | 127 | preventive_schedule | 0.265 | indefinido | indefinido | s4:+0.092, s12:+0.091, s3:+0.079 |
| 2 | HI_MARKER_D1 | 112 | 113 | preventive_schedule | 0.488 | indefinido | indefinido | s12:+0.090, s4:+0.057, s21:+0.055 |
| 2 | HI_MARKER_D2 | 112 | 114 | preventive_schedule | 0.488 | indefinido | indefinido | s12:+0.090, s4:+0.057, s21:+0.055 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 121 | 122 | preventive_schedule | 0.390 | indefinido | indefinido | s15:+0.089, s21:+0.079, s7:+0.072 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 121 | 123 | preventive_schedule | 0.390 | indefinido | indefinido | s15:+0.089, s21:+0.079, s7:+0.072 |
| 3 | HI_WAIT_SELECTED_D1 | 120 | 121 | preventive_schedule | 0.421 | indefinido | indefinido | s15:+0.081, s21:+0.071, s7:+0.068 |
| 3 | HI_WAIT_SELECTED_D2 | 120 | 122 | preventive_schedule | 0.421 | indefinido | indefinido | s15:+0.081, s21:+0.071, s7:+0.068 |
| 3 | ISO_POINT_M15_D1 | 130 | 131 | preventive_schedule | 0.194 | 13.91 | 13.91 | s15:+0.123, s21:+0.105, s7:+0.094 |
| 3 | ISO_POINT_M15_D2 | 130 | 132 | preventive_schedule | 0.194 | 13.91 | 13.91 | s15:+0.123, s21:+0.105, s7:+0.094 |
| 3 | ISO_LOWER98_M15_D1 | 115 | 116 | preventive_schedule | 0.485 | 34.05 | 13.00 | s21:+0.074, s7:+0.068, s15:+0.062 |
| 3 | ISO_LOWER98_M15_D2 | 115 | 117 | preventive_schedule | 0.485 | 34.05 | 13.00 | s21:+0.074, s7:+0.068, s15:+0.062 |
| 3 | RF_SLOPE_POINT_M15_D1 | 121 | 122 | preventive_schedule | 0.390 | 14.79 | 14.79 | s15:+0.089, s21:+0.079, s7:+0.072 |
| 3 | RF_SLOPE_POINT_M15_D2 | 115 | 117 | preventive_schedule | 0.485 | 16.92 | 16.92 | s21:+0.074, s7:+0.068, s15:+0.062 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 115 | 116 | preventive_schedule | 0.485 | 16.92 | 0.00 | s21:+0.074, s7:+0.068, s15:+0.062 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 115 | 117 | preventive_schedule | 0.485 | 16.92 | 0.00 | s21:+0.074, s7:+0.068, s15:+0.062 |
| 3 | AGE_D1 | 133 | 134 | preventive_schedule | 0.112 | indefinido | indefinido | s15:+0.131, s21:+0.119, s7:+0.104 |
| 3 | AGE_D2 | 132 | 134 | preventive_schedule | 0.147 | indefinido | indefinido | s15:+0.128, s21:+0.114, s7:+0.098 |
| 3 | HI_MARKER_D1 | 115 | 116 | preventive_schedule | 0.485 | indefinido | indefinido | s21:+0.074, s7:+0.068, s15:+0.062 |
| 3 | HI_MARKER_D2 | 115 | 117 | preventive_schedule | 0.485 | indefinido | indefinido | s21:+0.074, s7:+0.068, s15:+0.062 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=115, A=115.
- Repetição2: G=112, A=112.
- Repetição3: G=115, A=115.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.80 | 0.05 | 0.00% | 33.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.80 | 0.05 | 0.00% | 33.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.37 | 0.00 | 0.00% | 3.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.37 | 0.00 | 0.00% | 3.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.83 | 0.16 | 0.00% | 36.67% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.87 | 0.32 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 28.62 | 15 | 1.37 | 0.45 | 0.00% | 26.67% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 28.62 | 15 | 1.37 | 0.45 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.90 | 0.30 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.67 | 1.82 | 0.00% | 6.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 49.06 | 15 | 1.37 | 0.45 | 0.00% | 26.67% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 49.06 | 15 | 1.37 | 0.45 | 0.00% | 26.67% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.37 | 0.45 | 0.00% | 26.67% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.37 | 0.45 | 0.00% | 26.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.10 | 0.43 | 0.00% | 30.00% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.10 | 0.43 | 0.00% | 30.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.80 | 0.30 | 0.00% | 0.00% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.80 | 0.30 | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.70 | 0.05 | 0.00% | 26.67% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.50 | 0.37 | 0.00% | 0.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 39.28 | 15 | 1.80 | 1.10 | 0.00% | 30.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 39.28 | 15 | 1.80 | 1.10 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.40 | 0.00 | 0.00% | 60.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.40 | 0.11 | 0.00% | 36.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 43.83 | 15 | 1.80 | 1.10 | 0.00% | 30.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 43.83 | 15 | 1.80 | 1.10 | 0.00% | 30.00% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.80 | 1.10 | 0.00% | 30.00% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.80 | 1.10 | 0.00% | 30.00% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.87 | 0.09 | 0.00% | 26.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.87 | 0.09 | 0.00% | 26.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.47 | 0.39 | 0.00% | 6.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.47 | 0.39 | 0.00% | 6.67% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.93 | 0.38 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.93 | 0.38 | 0.00% | 13.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 21.05 | 15 | 1.47 | 0.67 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 21.05 | 15 | 1.47 | 0.67 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.87 | 3.76 | 0.00% | 43.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.87 | 0.94 | 0.00% | 43.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 29.95 | 15 | 1.47 | 0.67 | 0.00% | 20.00% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 29.95 | 15 | 1.47 | 0.67 | 0.00% | 20.00% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.47 | 0.67 | 0.00% | 20.00% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.47 | 0.67 | 0.00% | 20.00% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
