# FD003, motor89 — diagnóstico retrospectivo

Critérios de inclusão: median_discordance_d1, median_discordance_d2.

As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.

![Trajetórias e referências](case_FD003_u89.png)

| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | 186 | 187 | preventive_schedule | 0.399 | indefinido | indefinido | s11:+0.313, s2:+0.127, s4:+0.119 |
| 1 | HI_THRESHOLD_SELECTED_D2 | 186 | 188 | preventive_schedule | 0.399 | indefinido | indefinido | s11:+0.313, s2:+0.127, s4:+0.119 |
| 1 | HI_WAIT_SELECTED_D1 | 190 | 191 | preventive_schedule | 0.299 | indefinido | indefinido | s11:+0.364, s2:+0.166, s4:+0.127 |
| 1 | HI_WAIT_SELECTED_D2 | 185 | 187 | preventive_schedule | 0.407 | indefinido | indefinido | s11:+0.302, s2:+0.128, s4:+0.122 |
| 1 | ISO_POINT_M15_D1 | 195 | 196 | preventive_schedule | 0.170 | 15.40 | 15.40 | s11:+0.431, s2:+0.192, s4:+0.159 |
| 1 | ISO_POINT_M15_D2 | 195 | 197 | preventive_schedule | 0.170 | 15.40 | 15.40 | s11:+0.431, s2:+0.192, s4:+0.159 |
| 1 | ISO_LOWER98_M15_D1 | 180 | 181 | preventive_schedule | 0.489 | 40.20 | 9.75 | s11:+0.264, s4:+0.108, s2:+0.103 |
| 1 | ISO_LOWER98_M15_D2 | 180 | 182 | preventive_schedule | 0.489 | 40.20 | 9.75 | s11:+0.264, s4:+0.108, s2:+0.103 |
| 1 | RF_SLOPE_POINT_M15_D1 | 192 | 193 | preventive_schedule | 0.254 | 15.55 | 15.55 | s11:+0.381, s2:+0.176, s4:+0.143 |
| 1 | RF_SLOPE_POINT_M15_D2 | 192 | 194 | preventive_schedule | 0.254 | 15.55 | 15.55 | s11:+0.381, s2:+0.176, s4:+0.143 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 180 | 181 | preventive_schedule | 0.489 | 33.15 | 0.26 | s11:+0.264, s4:+0.108, s2:+0.103 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 180 | 182 | preventive_schedule | 0.489 | 33.15 | 0.26 | s11:+0.264, s4:+0.108, s2:+0.103 |
| 1 | AGE_D1 | 143 | 144 | preventive_schedule | 0.919 | indefinido | indefinido | s11:+0.047, s17:+0.018, s4:+0.017 |
| 1 | AGE_D2 | 142 | 144 | preventive_schedule | 0.946 | indefinido | indefinido | s11:+0.034, s17:+0.016, s4:+0.007 |
| 1 | HI_MARKER_D1 | 180 | 181 | preventive_schedule | 0.489 | indefinido | indefinido | s11:+0.264, s4:+0.108, s2:+0.103 |
| 1 | HI_MARKER_D2 | 180 | 182 | preventive_schedule | 0.489 | indefinido | indefinido | s11:+0.264, s4:+0.108, s2:+0.103 |
| 2 | HI_THRESHOLD_SELECTED_D1 | 189 | 190 | preventive_schedule | 0.390 | indefinido | indefinido | s2:+0.298, s4:+0.206, s11:+0.055 |
| 2 | HI_THRESHOLD_SELECTED_D2 | 189 | 191 | preventive_schedule | 0.390 | indefinido | indefinido | s2:+0.298, s4:+0.206, s11:+0.055 |
| 2 | HI_WAIT_SELECTED_D1 | 189 | 190 | preventive_schedule | 0.390 | indefinido | indefinido | s2:+0.298, s4:+0.206, s11:+0.055 |
| 2 | HI_WAIT_SELECTED_D2 | 189 | 191 | preventive_schedule | 0.390 | indefinido | indefinido | s2:+0.298, s4:+0.206, s11:+0.055 |
| 2 | ISO_POINT_M15_D1 | 196 | 197 | preventive_schedule | 0.219 | 15.12 | 15.12 | s2:+0.353, s4:+0.300, s11:+0.069 |
| 2 | ISO_POINT_M15_D2 | 196 | 198 | preventive_schedule | 0.219 | 15.12 | 15.12 | s2:+0.353, s4:+0.300, s11:+0.069 |
| 2 | ISO_LOWER98_M15_D1 | 184 | 185 | preventive_schedule | 0.482 | 37.40 | 9.93 | s2:+0.218, s4:+0.211, s11:+0.046 |
| 2 | ISO_LOWER98_M15_D2 | 184 | 186 | preventive_schedule | 0.482 | 37.40 | 9.93 | s2:+0.218, s4:+0.211, s11:+0.046 |
| 2 | RF_SLOPE_POINT_M15_D1 | 197 | 198 | preventive_schedule | 0.186 | 15.30 | 15.30 | s2:+0.367, s4:+0.317, s11:+0.071 |
| 2 | RF_SLOPE_POINT_M15_D2 | 196 | 198 | preventive_schedule | 0.219 | 16.18 | 16.18 | s2:+0.353, s4:+0.300, s11:+0.069 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 184 | 185 | preventive_schedule | 0.482 | 32.54 | 0.00 | s2:+0.218, s4:+0.211, s11:+0.046 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 184 | 186 | preventive_schedule | 0.482 | 32.54 | 0.00 | s2:+0.218, s4:+0.211, s11:+0.046 |
| 2 | AGE_D1 | 143 | 144 | preventive_schedule | 0.944 | indefinido | indefinido | s4:+0.030, s17:+0.020, s11:+0.007 |
| 2 | AGE_D2 | 142 | 144 | preventive_schedule | 0.970 | indefinido | indefinido | s17:+0.018, s4:+0.013, s2:-0.006 |
| 2 | HI_MARKER_D1 | 184 | 185 | preventive_schedule | 0.482 | indefinido | indefinido | s2:+0.218, s4:+0.211, s11:+0.046 |
| 2 | HI_MARKER_D2 | 184 | 186 | preventive_schedule | 0.482 | indefinido | indefinido | s2:+0.218, s4:+0.211, s11:+0.046 |
| 3 | HI_THRESHOLD_SELECTED_D1 | 190 | 191 | preventive_schedule | 0.384 | indefinido | indefinido | s11:+0.305, s13:+0.236, s15:-0.221 |
| 3 | HI_THRESHOLD_SELECTED_D2 | 190 | 192 | preventive_schedule | 0.384 | indefinido | indefinido | s11:+0.305, s13:+0.236, s15:-0.221 |
| 3 | HI_WAIT_SELECTED_D1 | 193 | 194 | preventive_schedule | 0.327 | indefinido | indefinido | s11:+0.334, s13:+0.252, s15:-0.239 |
| 3 | HI_WAIT_SELECTED_D2 | 193 | 195 | preventive_schedule | 0.327 | indefinido | indefinido | s11:+0.334, s13:+0.252, s15:-0.239 |
| 3 | ISO_POINT_M15_D1 | 199 | 200 | preventive_schedule | 0.197 | 13.96 | 13.96 | s11:+0.393, s13:+0.283, s15:-0.282 |
| 3 | ISO_POINT_M15_D2 | 198 | 200 | preventive_schedule | 0.214 | 16.80 | 16.80 | s11:+0.385, s13:+0.277, s15:-0.275 |
| 3 | ISO_LOWER98_M15_D1 | 183 | 184 | preventive_schedule | 0.499 | 36.38 | 14.83 | s11:+0.244, s13:+0.206, s15:-0.194 |
| 3 | ISO_LOWER98_M15_D2 | 183 | 185 | preventive_schedule | 0.499 | 36.38 | 14.83 | s11:+0.244, s13:+0.206, s15:-0.194 |
| 3 | RF_SLOPE_POINT_M15_D1 | 193 | 194 | preventive_schedule | 0.327 | 14.96 | 14.96 | s11:+0.334, s13:+0.252, s15:-0.239 |
| 3 | RF_SLOPE_POINT_M15_D2 | 192 | 194 | preventive_schedule | 0.344 | 16.29 | 16.29 | s11:+0.319, s13:+0.247, s15:-0.230 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 183 | 184 | preventive_schedule | 0.499 | 26.54 | 0.00 | s11:+0.244, s13:+0.206, s15:-0.194 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 183 | 185 | preventive_schedule | 0.499 | 26.54 | 0.00 | s11:+0.244, s13:+0.206, s15:-0.194 |
| 3 | AGE_D1 | 143 | 144 | preventive_schedule | 0.895 | indefinido | indefinido | s13:+0.124, s15:-0.110, s11:+0.039 |
| 3 | AGE_D2 | 142 | 144 | preventive_schedule | 0.915 | indefinido | indefinido | s13:+0.121, s15:-0.105, s11:+0.029 |
| 3 | HI_MARKER_D1 | 183 | 184 | preventive_schedule | 0.499 | indefinido | indefinido | s11:+0.244, s13:+0.206, s15:-0.194 |
| 3 | HI_MARKER_D2 | 183 | 185 | preventive_schedule | 0.499 | indefinido | indefinido | s11:+0.244, s13:+0.206, s15:-0.194 |

Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.

## Memória do sinal e resposta às perturbações

G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.

- Repetição1: G=180, A=180.
- Repetição2: G=184, A=184.
- Repetição3: G=183, A=183.

Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.

| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |
|---|---|---|---|---|---|---|---|---|
| 1 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.97 | 0.31 | 0.00% | 13.33% | 0/30 |
| 1 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.97 | 0.31 | 0.00% | 13.33% | 0/30 |
| 1 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.23 | 0.11 | 0.00% | 6.67% | 0/30 |
| 1 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.23 | 0.19 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.70 | 0.19 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.70 | 0.22 | 0.00% | 10.00% | 0/30 |
| 1 | ISO_LOWER98_M15_D1 | 30.46 | 15 | 1.23 | 0.46 | 0.00% | 13.33% | 0/30 |
| 1 | ISO_LOWER98_M15_D2 | 30.46 | 15 | 1.23 | 0.46 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.77 | 0.30 | 0.00% | 10.00% | 0/30 |
| 1 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.77 | 0.33 | 0.00% | 10.00% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D1 | 32.89 | 15 | 1.23 | 0.46 | 0.00% | 13.33% | 0/30 |
| 1 | RF_SLOPE_LOWER98_M15_D2 | 32.89 | 15 | 1.23 | 0.46 | 0.00% | 13.33% | 0/30 |
| 1 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 1 | HI_MARKER_D1 | indefinido | 0 | 1.23 | 0.46 | 0.00% | 13.33% | 0/30 |
| 1 | HI_MARKER_D2 | indefinido | 0 | 1.23 | 0.46 | 0.00% | 13.33% | 0/30 |
| 2 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 0.97 | 0.21 | 0.00% | 12.50% | 0/32 |
| 2 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 0.97 | 0.21 | 0.00% | 12.50% | 0/32 |
| 2 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.12 | 0.13 | 0.00% | 6.25% | 0/32 |
| 2 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.12 | 0.13 | 0.00% | 6.25% | 0/32 |
| 2 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.81 | 0.17 | 0.00% | 9.38% | 0/32 |
| 2 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.81 | 0.23 | 0.00% | 6.25% | 0/32 |
| 2 | ISO_LOWER98_M15_D1 | 27.48 | 15 | 1.12 | 0.37 | 0.00% | 6.25% | 0/32 |
| 2 | ISO_LOWER98_M15_D2 | 27.48 | 15 | 1.12 | 0.37 | 0.00% | 6.25% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.91 | 0.18 | 0.00% | 12.50% | 0/32 |
| 2 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.78 | 0.33 | 0.00% | 6.25% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D1 | 45.33 | 15 | 1.12 | 0.37 | 0.00% | 6.25% | 0/32 |
| 2 | RF_SLOPE_LOWER98_M15_D2 | 45.33 | 15 | 1.12 | 0.37 | 0.00% | 6.25% | 0/32 |
| 2 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/32 |
| 2 | HI_MARKER_D1 | indefinido | 0 | 1.12 | 0.37 | 0.00% | 6.25% | 0/32 |
| 2 | HI_MARKER_D2 | indefinido | 0 | 1.12 | 0.37 | 0.00% | 6.25% | 0/32 |
| 3 | HI_THRESHOLD_SELECTED_D1 | indefinido | 0 | 1.00 | 0.40 | 0.00% | 16.67% | 0/30 |
| 3 | HI_THRESHOLD_SELECTED_D2 | indefinido | 0 | 1.00 | 0.40 | 0.00% | 16.67% | 0/30 |
| 3 | HI_WAIT_SELECTED_D1 | indefinido | 0 | 1.60 | 0.00 | 0.00% | 20.00% | 0/30 |
| 3 | HI_WAIT_SELECTED_D2 | indefinido | 0 | 1.60 | 0.00 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D1 | 0.00 | 15 | 0.93 | 0.33 | 0.00% | 20.00% | 0/30 |
| 3 | ISO_POINT_M15_D2 | 0.00 | 15 | 0.90 | 0.26 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D1 | 21.55 | 15 | 1.60 | 0.35 | 0.00% | 23.33% | 0/30 |
| 3 | ISO_LOWER98_M15_D2 | 21.55 | 15 | 1.60 | 0.35 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D1 | 0.00 | 15 | 0.90 | 0.14 | 0.00% | 26.67% | 0/30 |
| 3 | RF_SLOPE_POINT_M15_D2 | 0.00 | 15 | 0.97 | 0.04 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D1 | 52.17 | 15 | 1.60 | 0.35 | 0.00% | 23.33% | 0/30 |
| 3 | RF_SLOPE_LOWER98_M15_D2 | 52.17 | 15 | 1.60 | 0.35 | 0.00% | 23.33% | 0/30 |
| 3 | AGE_D1 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | AGE_D2 | 0.00 | 0 | 0.00 | 0.00 | 0.00% | 0.00% | 0/30 |
| 3 | HI_MARKER_D1 | indefinido | 0 | 1.60 | 0.35 | 0.00% | 23.33% | 0/30 |
| 3 | HI_MARKER_D2 | indefinido | 0 | 1.60 | 0.35 | 0.00% | 23.33% | 0/30 |

Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.
