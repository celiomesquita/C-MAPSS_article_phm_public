# FD003, motor6 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u6.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 227 | 228 | preventive_schedule | 0.498 | indefinido | indefinido | s4:+0.276, s2:+0.079, s11:+0.067 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 227 | 229 | preventive_schedule | 0.498 | indefinido | indefinido | s4:+0.276, s2:+0.079, s11:+0.067 |
| 1 | HI_WAIT_SELECTED_D1 | 232 | 233 | preventive_schedule | 0.461 | indefinido | indefinido | s4:+0.295, s2:+0.085, s11:+0.073 |
| 1 | HI_WAIT_SELECTED_D2 | 232 | 234 | preventive_schedule | 0.461 | indefinido | indefinido | s4:+0.295, s2:+0.085, s11:+0.073 |
| 1 | ISO_POINT_M15_D1 | 263 | 264 | preventive_schedule | 0.211 | 15.24 | 15.24 | s4:+0.451, s11:+0.113, s2:+0.112 |
| 1 | ISO_POINT_M15_D2 | 262 | 264 | preventive_schedule | 0.216 | 16.52 | 16.52 | s4:+0.451, s11:+0.112, s2:+0.107 |
| 1 | ISO_LOWER98_M15_D1 | 227 | 228 | preventive_schedule | 0.498 | 33.05 | 2.80 | s4:+0.276, s2:+0.079, s11:+0.067 |
| 1 | ISO_LOWER98_M15_D2 | 227 | 229 | preventive_schedule | 0.498 | 33.05 | 2.80 | s4:+0.276, s2:+0.079, s11:+0.067 |
| 1 | RF_SLOPE_POINT_M15_D1 | 245 | 246 | preventive_schedule | 0.340 | 15.74 | 15.74 | s4:+0.368, s2:+0.106, s11:+0.092 |
| 1 | RF_SLOPE_POINT_M15_D2 | 245 | 247 | preventive_schedule | 0.340 | 15.74 | 15.74 | s4:+0.368, s2:+0.106, s11:+0.092 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 227 | 228 | preventive_schedule | 0.498 | 34.73 | 0.00 | s4:+0.276, s2:+0.079, s11:+0.067 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 227 | 229 | preventive_schedule | 0.498 | 34.73 | 0.00 | s4:+0.276, s2:+0.079, s11:+0.067 |
| 1 | AGE_D1 | 154 | 155 | preventive_schedule | 0.816 | indefinido | indefinido | s4:+0.098, s11:+0.031, s2:+0.027 |
| 1 | AGE_D2 | 153 | 155 | preventive_schedule | 0.827 | indefinido | indefinido | s4:+0.095, s11:+0.027, s2:+0.022 |
| 1 | HI_MARKER_D1 | 227 | 228 | preventive_schedule | 0.498 | indefinido | indefinido | s4:+0.276, s2:+0.079, s11:+0.067 |
| 1 | HI_MARKER_D2 | 227 | 229 | preventive_schedule | 0.498 | indefinido | indefinido | s4:+0.276, s2:+0.079, s11:+0.067 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 233 | 234 | preventive_schedule | 0.387 | indefinido | indefinido | s8:+0.221, s15:+0.179, s11:+0.109 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 233 | 235 | preventive_schedule | 0.387 | indefinido | indefinido | s8:+0.221, s15:+0.179, s11:+0.109 |
| 2 | HI_WAIT_SELECTED_D1 | 227 | 228 | preventive_schedule | 0.420 | indefinido | indefinido | s8:+0.206, s15:+0.190, s11:+0.098 |
| 2 | HI_WAIT_SELECTED_D2 | 227 | 229 | preventive_schedule | 0.420 | indefinido | indefinido | s8:+0.206, s15:+0.190, s11:+0.098 |
| 2 | ISO_POINT_M15_D1 | indefinido | indefinido | endpoint_without_decision | 0.024 | 22.75 | 22.75 | s15:+0.306, s8:+0.302, s11:+0.214 |
| 2 | ISO_POINT_M15_D2 | indefinido | indefinido | endpoint_without_decision | 0.024 | 22.75 | 22.75 | s15:+0.306, s8:+0.302, s11:+0.214 |
| 2 | ISO_LOWER98_M15_D1 | 217 | 218 | preventive_schedule | 0.498 | 87.77 | 13.72 | s8:+0.183, s15:+0.154, s11:+0.101 |
| 2 | ISO_LOWER98_M15_D2 | 217 | 219 | preventive_schedule | 0.498 | 87.77 | 13.72 | s8:+0.183, s15:+0.154, s11:+0.101 |
| 2 | RF_SLOPE_POINT_M15_D1 | 276 | 277 | preventive_schedule | 0.028 | 12.69 | 12.69 | s15:+0.306, s8:+0.303, s11:+0.210 |
| 2 | RF_SLOPE_POINT_M15_D2 | 274 | 276 | preventive_schedule | 0.059 | 16.06 | 16.06 | s8:+0.300, s15:+0.293, s11:+0.198 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 217 | 218 | preventive_schedule | 0.498 | 41.45 | 0.00 | s8:+0.183, s15:+0.154, s11:+0.101 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 217 | 219 | preventive_schedule | 0.498 | 41.45 | 0.00 | s8:+0.183, s15:+0.154, s11:+0.101 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.847 | indefinido | indefinido | s8:+0.064, s11:+0.034, s15:+0.030 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.836 | indefinido | indefinido | s8:+0.074, s11:+0.035, s15:+0.033 |
| 2 | HI_MARKER_D1 | 217 | 218 | preventive_schedule | 0.498 | indefinido | indefinido | s8:+0.183, s15:+0.154, s11:+0.101 |
| 2 | HI_MARKER_D2 | 217 | 219 | preventive_schedule | 0.498 | indefinido | indefinido | s8:+0.183, s15:+0.154, s11:+0.101 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 225 | 226 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.212, s4:+0.144, s20:+0.059 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 225 | 227 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.212, s4:+0.144, s20:+0.059 |
| 3 | HI_WAIT_SELECTED_D1 | 230 | 231 | preventive_schedule | 0.444 | indefinido | indefinido | s11:+0.223, s4:+0.166, s20:+0.068 |
| 3 | HI_WAIT_SELECTED_D2 | 227 | 229 | preventive_schedule | 0.487 | indefinido | indefinido | s11:+0.203, s4:+0.155, s20:+0.058 |
| 3 | ISO_POINT_M15_D1 | 258 | 259 | preventive_schedule | 0.178 | 15.72 | 15.72 | s11:+0.351, s4:+0.246, s20:+0.099 |
| 3 | ISO_POINT_M15_D2 | 258 | 260 | preventive_schedule | 0.178 | 15.72 | 15.72 | s11:+0.351, s4:+0.246, s20:+0.099 |
| 3 | ISO_LOWER98_M15_D1 | 225 | 226 | preventive_schedule | 0.491 | 39.67 | 12.00 | s11:+0.212, s4:+0.144, s20:+0.059 |
| 3 | ISO_LOWER98_M15_D2 | 225 | 227 | preventive_schedule | 0.491 | 39.67 | 12.00 | s11:+0.212, s4:+0.144, s20:+0.059 |
| 3 | RF_SLOPE_POINT_M15_D1 | 271 | 272 | preventive_schedule | 0.071 | 15.71 | 15.71 | s11:+0.391, s4:+0.286, s20:+0.101 |
| 3 | RF_SLOPE_POINT_M15_D2 | 269 | 271 | preventive_schedule | 0.093 | 16.55 | 16.55 | s11:+0.375, s4:+0.286, s20:+0.099 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 226 | 227 | preventive_schedule | 0.492 | 46.44 | 13.96 | s11:+0.205, s4:+0.148, s20:+0.059 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 226 | 228 | preventive_schedule | 0.492 | 46.44 | 13.96 | s11:+0.205, s4:+0.148, s20:+0.059 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.824 | indefinido | indefinido | s11:+0.071, s4:+0.055, s20:+0.023 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.815 | indefinido | indefinido | s11:+0.072, s4:+0.067, s20:+0.016 |
| 3 | HI_MARKER_D1 | 225 | 226 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.212, s4:+0.144, s20:+0.059 |
| 3 | HI_MARKER_D2 | 225 | 227 | preventive_schedule | 0.491 | indefinido | indefinido | s11:+0.212, s4:+0.144, s20:+0.059 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=227, A=227.
- Repetição2: G=217, A=217.
- Repetição3: G=225, A=225.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.30 | 0.48 | 0.00% | 23.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.30 | 0.48 | 0.00% | 23.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.30 | 0.17 | 0.00% | 23.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.30 | 0.17 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 2.53 | 0.74 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.53 | 0.57 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 30.25 | 15 | 2.30 | 0.48 | 0.00% | 23.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 30.25 | 15 | 2.30 | 0.48 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 3.13 | 0.00 | 0.00% | 33.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 3.17 | 0.04 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 35.95 | 15 | 2.30 | 0.48 | 0.00% | 23.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 35.95 | 15 | 2.30 | 0.48 | 0.00% | 23.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.30 | 0.48 | 0.00% | 23.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.30 | 0.48 | 0.00% | 23.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 3.13 | 1.08 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 3.13 | 1.08 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.07 | 0.08 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.07 | 0.08 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | indefinido | indefinido | 0.00% | 0.00% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | indefinido | indefinido | 16.67% | 13.33% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 74.05 | 15 | 2.10 | 0.46 | 0.00% | 20.00% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 74.05 | 15 | 2.10 | 0.46 | 0.00% | 20.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.08 | 1.07 | 13.33% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.23 | 0.60 | 13.33% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 136.85 | 15 | 2.07 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 136.85 | 15 | 2.07 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 2.07 | 0.52 | 0.00% | 16.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 2.07 | 0.52 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.97 | 0.57 | 0.00% | 23.33% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.97 | 0.57 | 0.00% | 23.33% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.97 | 0.24 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.97 | 0.43 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 3.10 | 0.27 | 0.00% | 26.67% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 2.97 | 0.43 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 27.67 | 15 | 2.97 | 0.57 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 27.67 | 15 | 2.97 | 0.57 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 1.52 | 0.59 | 3.33% | 26.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.80 | 0.32 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 32.48 | 15 | 1.80 | 0.64 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 32.48 | 15 | 1.73 | 0.64 | 0.00% | 26.67% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 2.97 | 0.57 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 2.97 | 0.57 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
