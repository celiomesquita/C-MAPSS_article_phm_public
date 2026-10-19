# P12.2 — ponte de escala k, cenário operacional de 20 anos e estabilidade da ordenação

Especificado em 18/10/2026 antes da execução, por solicitação do autor: adotar a alternativa (a) (fator k calibrado, com calibração documentada e análise de sensibilidade). Exploratório, RQ3. Sem inspeção, receita, disponibilidade ou valor financeiro de companhia. Não congela o protocolo principal.

## Princípio

Os resultados por **ciclo simulado** (P12.1, taxas e contrastes sobre motores E) continuam sendo os resultados científicos principais e não são alterados. O horizonte de 20 anos é um **cenário operacional condicionado** aos parâmetros k, utilização anual, limite de LLP, condições iniciais e eficiência de restauração. Nada aqui valida equivalência física entre C-MAPSS e um motor comercial.

## Calibração de k (documentada)

[Ficha de calibração](../references/cenario_economico_20anos/calibracao_k.md) e [intervalos de referência](../references/cenario_economico_20anos/intervalos_referencia_k.csv). Fontes: Aircraft Commerce (2003, 2005, 2019) para intervalos de remoção por EGT/desempenho; FAA AC 33.70-1 e Change 1 para o tratamento de LLP; Saxena et al. (2008) para a definição de ciclo (um voo) e do endpoint (menor margem normalizada). Apenas os intervalos regidos por EGT/desempenho (R1-R10) entram. k = L_ref/T̄, com T̄ a vida média até o endpoint dos 100 motores de treino do domínio. L_ref ∈ {4.000, 5.000, 6.000, 7.000, 8.425 (mediana dos pontos médios), 10.000, 12.000, 14.000, 16.500, 19.000} EFC. Esta grade vem da tabela, não de resultados; o valor central não foi ajustado.

## Cenário

- **Unidade de tempo**: ciclos de voo (FC). Horizonte = 20 × u FC, com u ∈ {1.400, 1.600, 1.900} FC/ano (AC 2019: "most aircraft achieve 1,400-1,900FC per year"; M21: 1.600).
- **Vida de degradação**: uma vida de motor E com `utilised` = vida simulada u_i dura ρ_j · k · u_i FC. ρ_0 = 1 na primeira vida; para vidas posteriores ρ ∈ {1,0 (AGAN), 0,8 (restauração parcial; AC 2003: segunda corrida ≈80% da primeira)}.
- **LLP**: contador de FC próprio, preservado nas restaurações por degradação e zerado somente na visita forçada por LLP (todas as LLPs substituídas, hipótese). Visita forçada ao atingir L_LLP ∈ {sem LLP, 20.000, 25.000, 30.000} EFC (valores de módulos CFM56/V2500 nas fontes; sensibilidade, não identificação de motor). A visita forçada também renova o estado de degradação e precede a remoção por degradação se ocorrer antes ou no mesmo ciclo; o evento de endpoint da vida interrompida não ocorre. Visitas por degradação e por LLP têm o mesmo custo fixo (hipótese); são contadas separadamente. Não se funde uma visita por degradação com a substituição de LLP próxima (limitação declarada).
- **Condições iniciais**: IC0 = motor novo (idade de degradação 0, LLP 0); IC1 = frota madura (idade de degradação do estado estacionário da renovação: vida escolhida com probabilidade proporcional ao seu comprimento e fração decorrida uniforme; idade de LLP uniforme em [0, L_LLP]). Em IC1 a vida inicial usa ρ (frota madura). A restauração inicial não é contada.
- **Aposentadoria do motor**: não há limite de restaurações; aposentadoria técnica ou econômica não é modelada. Contagem só de eventos no horizonte; vida residual registrada.
- **Custo**: US$ 6 milhões por visita, sensibilidade 5/7 pós-simulação (linear). Com custo fixo comum, o custo não altera a ordenação das regras, apenas a magnitude. Sem desconto nem inflação.
- **Regras**: as 16 regras congeladas de P13.1 (fonte `pilot_policy_selection_13a/decisions.csv`, 100 motores completos por domínio e repetição); repetições separadas.

## Simulação

R=2.000 réplicas por célula; sequências de motores e sorteios iniciais comuns a todas as regras dentro da célula (sementes por domínio, repetição, L_ref, u, cenário). Grade completa: 2 domínios × 3 repetições × 10 L_ref × 3 u × 4 LLP × 2 IC × 2 ρ = 2.880 células. Cenário operacional central (sem otimizar): L_ref=8.425, u=1.600, LLP=20.000, IC1, ρ=1,0; ele e os demais permanecem na grade. Registrar por regra e célula: visitas por degradação, por LLP e totais; eventos de endpoint (ausência de decisão, chegada exata, ultrapassagem estrita) nas vidas por degradação; razão de efeito de borda frente à taxa analítica.

## Contrastes e estabilidade da ordenação

Pares pré-declarados, d ∈ {1,2}: ISO_LOWER98_M15 vs AGE; HI_MARKER vs AGE; ISO_LOWER98_M15 vs HI_MARKER; RF_SLOPE_LOWER98_M15 vs ISO_LOWER98_M15; HI_THRESHOLD_SELECTED vs HI_MARKER; HI_WAIT_SELECTED vs HI_MARKER; ISO_POINT_M15 vs ISO_LOWER98_M15. Diferença de visitas totais (a−b) pareada por réplica; média, erro padrão das réplicas (variabilidade do processo para os 100 motores, não incerteza de população). Sinal analítico de referência: sinal de (taxa_a − taxa_b) de P12.1 no mesmo domínio e repetição.

- **Estável**: sinal da média igual ao analítico e |média| ≥ 2 EP.
- **Indistinguível**: |média| < 2 EP.
- **Invertido**: sinal oposto e |média| ≥ 2 EP.
Relatar as frações por par e nível de cada fator (L_ref/k, u, LLP, IC, ρ, domínio) e as condições em que cada par deixa de ser estável. Também Kendall τ entre a ordenação das 16 regras na célula e a ordenação analítica. Não declarar vencedor global; a ordenação é estável ou não sob as condições, nunca validada para uma companhia. O contraste ISO_LOWER98 vs HI_MARKER tem efeito analítico de 0-0,9% e é esperado indistinguível em muitas células: isso é resultado, não falha.

## Validação do simulador

(1) Estado estacionário: sem LLP, ρ=1, IC1, a média de visitas por posição deve igualar H·taxa analítica dentro de |z| < 4 em todos os horizontes da grade e dentro de 1% em horizonte longo (2×10⁶ FC). (2) IC0 sem LLP, horizonte longo: taxa por FC igual a taxa_analítica/k dentro de 1%. (3) Com LLP, o número de visitas por LLP é igual em todas as regras na mesma réplica e igual ao valor determinístico. Falha interrompe o relato.

## Interpretação prévia

- Para k na faixa calibrada, o horizonte contém poucas vidas (quando H_sim = H/k fica em poucas vidas de ~170-210 ciclos) e o efeito de borda é grande em IC0; registrar, não corrigir.
- Visitas forçadas por LLP são iguais entre regras e podem diluir as diferenças por degradação; relatar a ordenação das visitas totais e das visitas por degradação.
- Nenhum resultado selecionará k, u ou L_LLP. Uma ordenação estável em uma região da grade não torna essa região correta.

## Verificação e artefatos

Testes antes da execução: construção determinística de uma réplica com LLP; ausência de leitura de test/RUL/FD002/FD004; estado estacionário sem LLP; contagem LLP igual entre regras; ρ aplicado só às vidas posteriores; reprodutibilidade das sementes. Verificador independente: reimplementação por laços para subconjunto de células (todos os níveis de cada fator representados), comparação exata de médias e desvios, invariantes e sinais analíticos refeitos de colunas brutas, manifestos anteriores íntegros. Saídas em `artifacts/pilot_scale_bridge_12b`: fontes, hashes, tabelas de células, contrastes, estabilidade, validação, figura, verificação, `conclusoes.md`.

## Pendências (autor)

Frota elegível, procura, disponibilidade efetiva e margem incremental (M22); parâmetros do braço de inspeção; uma justificativa externa mais forte para L_ref de um motor da classe C-MAPSS; critério de aposentadoria do motor, se houver.
