# P10 — calibração de F a 98% e disponibilidade de antecedência

Protocolo definido em 17/10/2026 antes dos ajustes. Autorização: prosseguir com o experimento proposto de calibração exclusiva U50. Questões RQ1/RQ2/RQ7. Não constitui congelamento do protocolo principal nem execução da política de remoção.

## Desenho fixado

FD001 principal e FD003 robustez, analisados separadamente. Três repetições com sementes 20261017, 20261018 e 20261019. Em cada repetição, permutar os 100 motores completos e dividir em dez blocos E10. Em cada dobra, permutar os 90 restantes com semente acrescida de 1000 vezes o número da dobra: F25 para HI, C15 para conversores e U50 exclusivamente para incerteza. Grupos disjuntos; cada motor aparece uma vez em E por repetição. Não agregar repetições como 300 motores independentes. Os mesmos identificadores em FD001/FD003 não constituem pares físicos.

Manter a forma empírica não negativa M18; reaprender orientação, canais, escalas e pesos somente em F. Média móvel causal de 15 ciclos, referência própria no ciclo 20, HI disponível a partir de 20; atributos prognósticos a partir de 39. Alvos fixos: FD001 τ=100, γ=1, penalização 0,1; FD003 τ=60, γ=2, penalização zero. Comparar somente isotônico crescente ISO e floresta aleatória RF_SLOPE com HI atual e inclinação nos últimos 20 HI. Ajustar conversores somente em C, com pesos de mesmo total por motor. RF: 150 árvores, profundidade 12, mínimo de cinco observações por folha, semente da repetição. Nenhuma seleção por U/E ou teste oficial.

Avaliar do primeiro HI≤0,5 causal até o último ciclo observado, com atualizações por ciclo. O marco não é P, F nem gatilho de remoção. Valores antes de 39 e motores sem cruzamento ficam explicitamente indisponíveis. Extensão secundária: modelo da primeira dobra de cada repetição nos testes oficiais, somente até truncamento; rótulos RUL entram depois da previsão para aferir T. Esses testes já foram examinados e não são confirmação intocada.

## Calibração

Para erro e_i(t)=F̂_i(t)−T_i, usar escores por motor: S_abs=max_t |e_i(t)| e S_late=max(0,max_t e_i(t)). Máximo sobre trajetória observada após o marco; alternativa diagnóstica: erro somente no marco. Alvo primário α=0,02 e sensibilidade fixa α=0,05, sem escolher nível após resultados. Para n motores disponíveis, k=ceil((n+1)(1−α)); quantil de ordem k, ou +∞ se k>n. Com U50 e 98%, k=50: o maior escore, sensível a extremos. Com n=49 o quantil ainda é finito; n≤48 não permite quantil finito. Não substituir n por número de ciclos, dobras ou repetições.

Banda bilateral [max(t,F̂−q_abs), F̂+q_abs]; limite unilateral L=max(t,F̂−q_late). Reportar n efetivo, quantis, cobertura por motor no marco e em toda a trajetória, largura mediana, antecedência L−t e colapso em t. O método de ordem corrigida segue Lei et al. (2018), *Distribution-Free Predictive Inference for Regression*, DOI 10.1080/01621459.2017.1307116, seção 2, equações 2–3: [fonte primária](https://www.stat.cmu.edu/~ryantibs/papers/conformal-jasa.pdf). A adaptação de escore máximo por motor pertence a este protocolo. A interpretação marginal requer intercambiabilidade de motores e mesmo domínio de disponibilidade; não equivale a cobertura condicional de cada motor, sensor ou instante.

## Diagnóstico de antecedência, sem política

Para reservas m∈{15,12} e execução d∈{1,2}, definir A_i(t;m,d)=1{L_i(t)−t ≥ m+d}. Esta é uma pergunta sobre informação disponível: o limite inferior ainda deixa espaço para essa reserva e execução? Não adota L como âncora da reserva, não agenda remoção e não implica descontar a incerteza duas vezes. Reportar, por motor, A no marco, fração dos ciclos observados com A=1 e existência de algum ciclo com A=1; resumir sem dar maior peso a trajetórias longas. Disponibilidade do marco e da trajetória permanece no denominador próprio. Critério de incerteza elevada e âncora F̂ versus L continuam pendentes. Não seleccionar m, d ou algoritmo por esses resultados.

## Interpretação e rastreabilidade

98% nominal de cobertura preditiva não demonstra ultrapassagem ≤2% pela futura política. Um resultado de zero eventos em 100 motores tampouco certifica esse risco populacional. E10 tem resolução de 10 pontos percentuais por dobra, 100 motores externos por repetição têm resolução de um ponto; divisões são dependentes. F25/C15/U50/E10 altera também ajuste e avaliação em relação a P09: não atribuir diferenças exclusivamente ao aumento de U. Comparações de conversores dentro de P10 são pareadas por motor; bootstrap de 2000 reamostragens para diferença de RMSE, reportado por repetição, não como intervalo de F individual.

Congelar modelo e quantis antes de avaliar E/teste. Preservar entradas, partições, modelos, previsões, escores, quantis, métricas, parâmetros e hashes. Verificação separada deve reconstruir previsões, quantis, coberturas e diagnóstico de antecedência; testes devem cobrir separação, causalidade, fronteira n=48/49/50 e diferença entre cobertura pontual e temporal. Inspeções, remoções e sensores pós-T não serão simulados. Manter o HI de trabalho e ISO como controle até interpretação conjunta dos resultados; não refinar a fórmula por conveniência visual.
