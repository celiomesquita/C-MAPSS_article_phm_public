# FD003, motor82 — diagnóstico retrospectivo

Critérios de inclusão: adverse_or_infeasible.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u82.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 252 | 253 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.216, s17:+0.116, s11:+0.088 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 252 | 254 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.216, s17:+0.116, s11:+0.088 |
| 1 | HI_WAIT_SELECTED_D1 | 254 | 255 | preventive_schedule | 0.461 | indefinido | indefinido | s4:+0.230, s17:+0.129, s11:+0.095 |
| 1 | HI_WAIT_SELECTED_D2 | 254 | 256 | preventive_schedule | 0.461 | indefinido | indefinido | s4:+0.230, s17:+0.129, s11:+0.095 |
| 1 | ISO_POINT_M15_D1 | 280 | 281 | preventive_schedule | 0.157 | 12.68 | 12.68 | s4:+0.355, s17:+0.188, s11:+0.152 |
| 1 | ISO_POINT_M15_D2 | 278 | 280 | preventive_schedule | 0.188 | 16.32 | 16.32 | s4:+0.342, s17:+0.176, s11:+0.145 |
| 1 | ISO_LOWER98_M15_D1 | 253 | 254 | preventive_schedule | 0.482 | 37.42 | 14.45 | s4:+0.218, s17:+0.122, s11:+0.092 |
| 1 | ISO_LOWER98_M15_D2 | 252 | 254 | preventive_schedule | 0.496 | 39.47 | 16.51 | s4:+0.216, s17:+0.116, s11:+0.088 |
| 1 | RF_SLOPE_POINT_M15_D1 | 271 | 272 | preventive_schedule | 0.305 | 15.45 | 15.45 | s4:+0.302, s17:+0.135, s11:+0.126 |
| 1 | RF_SLOPE_POINT_M15_D2 | 271 | 273 | preventive_schedule | 0.305 | 15.45 | 15.45 | s4:+0.302, s17:+0.135, s11:+0.126 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 252 | 253 | preventive_schedule | 0.496 | 35.42 | 1.17 | s4:+0.216, s17:+0.116, s11:+0.088 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 252 | 254 | preventive_schedule | 0.496 | 35.42 | 1.17 | s4:+0.216, s17:+0.116, s11:+0.088 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.936 | indefinido | indefinido | s11:+0.027, s9:+0.014, s17:+0.009 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.939 | indefinido | indefinido | s11:+0.024, s9:+0.015, s17:+0.006 |
| 1 | HI_MARKER_D1 | 252 | 253 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.216, s17:+0.116, s11:+0.088 |
| 1 | HI_MARKER_D2 | 252 | 254 | preventive_schedule | 0.496 | indefinido | indefinido | s4:+0.216, s17:+0.116, s11:+0.088 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 273 | 274 | preventive_schedule | 0.292 | indefinido | indefinido | s4:+0.321, s11:+0.169, s2:+0.164 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 273 | 275 | preventive_schedule | 0.292 | indefinido | indefinido | s4:+0.321, s11:+0.169, s2:+0.164 |
| 2 | HI_WAIT_SELECTED_D1 | 259 | 260 | preventive_schedule | 0.430 | indefinido | indefinido | s4:+0.270, s11:+0.134, s2:+0.124 |
| 2 | HI_WAIT_SELECTED_D2 | 259 | 261 | preventive_schedule | 0.430 | indefinido | indefinido | s4:+0.270, s11:+0.134, s2:+0.124 |
| 2 | ISO_POINT_M15_D1 | 274 | 275 | preventive_schedule | 0.287 | 15.84 | 15.84 | s4:+0.324, s11:+0.170, s2:+0.164 |
| 2 | ISO_POINT_M15_D2 | 272 | 274 | preventive_schedule | 0.303 | 16.73 | 16.73 | s4:+0.321, s11:+0.163, s2:+0.162 |
| 2 | ISO_LOWER98_M15_D1 | 254 | 255 | preventive_schedule | 0.478 | 34.68 | 11.48 | s4:+0.239, s2:+0.121, s11:+0.119 |
| 2 | ISO_LOWER98_M15_D2 | 254 | 256 | preventive_schedule | 0.478 | 34.68 | 11.48 | s4:+0.239, s2:+0.121, s11:+0.119 |
| 2 | RF_SLOPE_POINT_M15_D1 | 284 | 285 | at_endpoint | 0.155 | 15.30 | 15.30 | s4:+0.396, s11:+0.204, s2:+0.174 |
| 2 | RF_SLOPE_POINT_M15_D2 | 278 | 280 | preventive_schedule | 0.227 | 16.00 | 16.00 | s4:+0.355, s11:+0.182, s2:+0.171 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 254 | 255 | preventive_schedule | 0.478 | 39.37 | 0.00 | s4:+0.239, s2:+0.121, s11:+0.119 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 254 | 256 | preventive_schedule | 0.478 | 39.37 | 0.00 | s4:+0.239, s2:+0.121, s11:+0.119 |
| 2 | AGE_D1 | 145 | 146 | preventive_schedule | 0.938 | indefinido | indefinido | s11:+0.038, s2:+0.017, s8:+0.005 |
| 2 | AGE_D2 | 144 | 146 | preventive_schedule | 0.951 | indefinido | indefinido | s11:+0.036, s2:+0.015, s4:-0.008 |
| 2 | HI_MARKER_D1 | 254 | 255 | preventive_schedule | 0.478 | indefinido | indefinido | s4:+0.239, s2:+0.121, s11:+0.119 |
| 2 | HI_MARKER_D2 | 254 | 256 | preventive_schedule | 0.478 | indefinido | indefinido | s4:+0.239, s2:+0.121, s11:+0.119 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 262 | 263 | preventive_schedule | 0.295 | indefinido | indefinido | s11:+0.389, s12:-0.194, s4:+0.144 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 262 | 264 | preventive_schedule | 0.295 | indefinido | indefinido | s11:+0.389, s12:-0.194, s4:+0.144 |
| 3 | HI_WAIT_SELECTED_D1 | 257 | 258 | preventive_schedule | 0.380 | indefinido | indefinido | s11:+0.352, s12:-0.177, s4:+0.125 |
| 3 | HI_WAIT_SELECTED_D2 | 257 | 259 | preventive_schedule | 0.380 | indefinido | indefinido | s11:+0.352, s12:-0.177, s4:+0.125 |
| 3 | ISO_POINT_M15_D1 | 280 | 281 | preventive_schedule | 0.073 | 13.82 | 13.82 | s11:+0.522, s12:-0.278, s8:+0.205 |
| 3 | ISO_POINT_M15_D2 | 278 | 280 | preventive_schedule | 0.102 | 16.65 | 16.65 | s11:+0.500, s12:-0.268, s8:+0.196 |
| 3 | ISO_LOWER98_M15_D1 | 247 | 248 | preventive_schedule | 0.489 | 46.49 | 14.13 | s11:+0.278, s12:-0.151, s8:+0.109 |
| 3 | ISO_LOWER98_M15_D2 | 247 | 249 | preventive_schedule | 0.489 | 46.49 | 14.13 | s11:+0.278, s12:-0.151, s8:+0.109 |
| 3 | RF_SLOPE_POINT_M15_D1 | 261 | 262 | preventive_schedule | 0.307 | 13.79 | 13.79 | s11:+0.384, s12:-0.191, s4:+0.141 |
| 3 | RF_SLOPE_POINT_M15_D2 | 261 | 263 | preventive_schedule | 0.307 | 13.79 | 13.79 | s11:+0.384, s12:-0.191, s4:+0.141 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 254 | 255 | preventive_schedule | 0.415 | 48.69 | 10.06 | s11:+0.326, s12:-0.168, s4:+0.119 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 254 | 256 | preventive_schedule | 0.415 | 48.69 | 10.06 | s11:+0.326, s12:-0.168, s4:+0.119 |
| 3 | AGE_D1 | 145 | 146 | preventive_schedule | 0.884 | indefinido | indefinido | s11:+0.105, s12:-0.022, s8:+0.015 |
| 3 | AGE_D2 | 144 | 146 | preventive_schedule | 0.896 | indefinido | indefinido | s11:+0.099, s12:-0.021, s8:+0.013 |
| 3 | HI_MARKER_D1 | 247 | 248 | preventive_schedule | 0.489 | indefinido | indefinido | s11:+0.278, s12:-0.151, s8:+0.109 |
| 3 | HI_MARKER_D2 | 247 | 249 | preventive_schedule | 0.489 | indefinido | indefinido | s11:+0.278, s12:-0.151, s8:+0.109 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=252, A=252.
- Repetição2: G=254, A=254.
- Repetição3: G=247, A=247.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 2.25 | 0.76 | 0.00% | 21.88% | 0/32 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 2.25 | 0.76 | 0.00% | 21.88% | 0/32 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 2.25 | 0.56 | 0.00% | 21.88% | 0/32 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 2.25 | 0.56 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.00 | 0.40 | 6.25% | 21.88% | 0/32 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.13 | 0.37 | 3.12% | 15.62% | 0/32 |
| 1 | ISO_LOWER98_M15_D1 | 22.97 | 15 | 2.03 | 0.60 | 0.00% | 21.88% | 0/32 |
| 1 | ISO_LOWER98_M15_D2 | 22.97 | 15 | 2.25 | 0.76 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.25 | 0.50 | 0.00% | 37.50% | 0/32 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.69 | 0.50 | 0.00% | 37.50% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 34.25 | 15 | 2.22 | 0.76 | 0.00% | 21.88% | 0/32 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 34.25 | 15 | 2.25 | 0.76 | 0.00% | 21.88% | 0/32 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 2.25 | 0.76 | 0.00% | 21.88% | 0/32 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 2.25 | 0.76 | 0.00% | 21.88% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.80 | 0.40 | 0.00% | 16.67% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.80 | 0.40 | 0.00% | 16.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.53 | 0.29 | 0.00% | 6.67% | 0/30 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.53 | 0.29 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.87 | 0.52 | 0.00% | 23.33% | 0/30 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.90 | 0.44 | 0.00% | 16.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D1 | 23.20 | 15 | 1.53 | 0.46 | 0.00% | 6.67% | 0/30 |
| 2 | ISO_LOWER98_M15_D2 | 23.20 | 15 | 1.53 | 0.46 | 0.00% | 6.67% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.90 | 2.00 | 3.33% | 10.00% | 0/30 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 2.07 | 0.74 | 0.00% | 10.00% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 40.08 | 15 | 1.53 | 0.46 | 0.00% | 6.67% | 0/30 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 40.08 | 15 | 1.53 | 0.46 | 0.00% | 6.67% | 0/30 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.53 | 0.46 | 0.00% | 6.67% | 0/30 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.53 | 0.46 | 0.00% | 6.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.53 | 0.50 | 0.00% | 25.00% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.53 | 0.50 | 0.00% | 25.00% | 0/32 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 3.41 | 0.13 | 0.00% | 3.12% | 0/32 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 3.41 | 0.13 | 0.00% | 3.12% | 0/32 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 1.23 | 0.48 | 3.12% | 21.88% | 0/32 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 1.26 | 0.25 | 3.12% | 25.00% | 0/32 |
| 3 | ISO_LOWER98_M15_D1 | 32.36 | 15 | 3.41 | 1.11 | 0.00% | 12.50% | 0/32 |
| 3 | ISO_LOWER98_M15_D2 | 32.36 | 15 | 3.41 | 1.11 | 0.00% | 12.50% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 2.58 | 0.32 | 3.12% | 40.62% | 0/32 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 1.28 | 0.50 | 0.00% | 37.50% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 38.63 | 15 | 2.09 | 2.88 | 0.00% | 25.00% | 0/32 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 38.63 | 15 | 2.09 | 2.88 | 0.00% | 25.00% | 0/32 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 3.41 | 1.11 | 0.00% | 12.50% | 0/32 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 3.41 | 1.11 | 0.00% | 12.50% | 0/32 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
