# P09 — robustez e incerteza preditiva do F original

Protocolo anterior ao ajuste/avaliação, 17/10/2026. Autorização do autor para prosseguir após M18. Perguntas RQ1/RQ2/RQ7: quão estáveis são o prognóstico e sua incerteza após o marco empírico HI≤0,5? A representação HI está adotada como referência; esta rodada não busca outra fórmula. Não define P, regra de remoção ou tolerância de segurança.

## Dados, repetições e separação por motor

FD001 é principal e FD003 é robustez, com ajuste no próprio domínio. Três repetições pré-especificadas, sementes 20261017/20261018/20261019. Em cada uma, permutar IDs 1–100, formar cinco blocos externos E20 e, para cada fold, permutar os 80 motores restantes com semente da repetição +1000×fold, separando F40/C20/U20. F ajusta HI; C ajusta conversores; U calibra exclusivamente a incerteza; E avalia. Todos são disjuntos. Cada motor tem uma avaliação externa por repetição, não três novas observações independentes. Não agregar as repetições como 300 motores independentes.

Não haverá seleção de métodos/hiperparâmetros em U. As escolhas ficam fixadas abaixo com base nas rodadas anteriores. Isso permite reservar 20 motores exclusivamente à incerteza e conservar 40/20 para aprendizagem de HI/conversor. A separação é nova nesta rodada; os mesmos dados já informaram decisões passadas. A análise continua exploratória, sem chamar U ou E de dados historicamente intocados.

Como diagnóstico secundário, o modelo e calibração do fold 1 de cada repetição também serão aplicados aos 100 motores oficiais truncados do respectivo subconjunto. Não haverá novo ajuste para esse teste. Os resultados e a cobertura se referem somente aos sensores observados até o truncamento; o endpoint é calculado pelos rótulos RUL oficiais, sem gerar sensores futuros. Não confundir IDs de treino/teste ou FD001/FD003.

## HI e preditores fixados

Manter Ĥ=clip[1−max(0,Σβ_j z_j),0,1], β_j≥0, média causal 15, referência individual no ciclo 20 e direção/escala/canais aprendidos SOMENTE em F. Reaprender esses parâmetros em cada nova partição; não reutilizar modelos HI que viram os motores de avaliação. A convenção supervisionada e regularização já escolhidas anteriormente ficam fixas: FD001 τ=100, γ=1, λ=0,1; FD003 τ=60, γ=2, λ=0. Não selecionar novamente essas convenções pelo desempenho de U/E. Não representam um HI físico observado.

Três conversores, ajustados SOMENTE em C nos ciclos ≥39, com peso total igual por motor e RUL prevista ≥0:

| Método | Entradas e configuração |
|---|---|
| ISO | Isotônico crescente, HI corrente |
| RF_HI | Floresta aleatória, HI corrente; controle de capacidade |
| RF_SLOPE | Mesma floresta, HI corrente + inclinação causal de HI nos últimos 20 valores |

As duas florestas usam 150 árvores, profundidade máxima 12, folha mínima cinco e semente da repetição. Não há nova busca de arquitetura ou seleção em teste. A inclinação é o coeficiente linear local já definido em P08. As três alternativas usam os mesmos ciclos ≥39. O primeiro cruzamento tα=inf{t≥20:Ĥ(t)≤0,5} não é adiado; se anterior a 39, o marco inicial é indisponível para essa comparação, e o monitoramento passa a estar disponível em max(tα,39). Recuperações acima de 0,5 não suspendem as atualizações após a primeira passagem.

## Domínio temporal e calibração da incerteza

O domínio primário é a trajetória observada desde max(tα,39) até o último ciclo disponível, atualizando F̂(t)=t+RUL̂(t) a cada ciclo. Esse intervalo é um domínio prognóstico experimental, não P–F fisicamente validado. Motor sem passagem observada fica sem domínio disponível, conservado no denominador. Os rótulos de E/teste são anexados só depois de congelar os modelos e quantis de U.

Para cada motor i de U com domínio disponível e erro e_i(t)=F̂_i(t)−T_i, calibrar um escore por motor, sem tratar ciclos correlacionados como amostras independentes:

    s_i,abs = max_t |e_i(t)|
    s_i,late = max_t max(e_i(t),0).

Para n motores disponíveis, cobertura nominal 1−α e k=ceil((n+1)(1−α)), usar o k-ésimo escore ordenado se k≤n; caso contrário q=+∞. Primário α=0,10; sensibilidade α=0,05. Com n=20, os ranks são 19 e 20. Se a disponibilidade reduzir n a menos de 19, o nível de 95% pode resultar não finito; não substituir por máximo finito ou quantil interpolado.

Para cada novo ciclo observado, a banda bilateral de F é [max(t,F̂(t)−q_abs), F̂(t)+q_abs]. O limite inferior unilateral é L(t)=max(t,F̂(t)−q_late), relevante ao risco de prever F tarde. A restrição F≥t usa somente a sobrevivência observada; não introduz o endpoint futuro. Esse limite não é uma ordem de remoção nem garante antecedência operacional. Preservar +∞ e reportar proporção de bandas finitas e casos L(t)=t, sem antecipação conservadora positiva.

Como comparação pré-definida, calibrar também escores absolutos/positivos apenas no primeiro marco disponível tα≥39 em U. Avaliar a banda desse ponto tanto no marco quanto nas atualizações; sua cobertura no primeiro ponto não implica cobertura simultânea do restante da trajetória. Os máximos temporais acima são a construção para investigar cobertura da trajetória. Nenhum alvo nominal será convertido em requisito de safety.

## Métricas, comparações e interpretação

Por subconjunto/repetição/método e nível, reportar disponibilidade de marco/domínio, antecedência real, RMSE/MAE/viés, frequência de erro positivo e magnitude de sobrestimação de F. Avaliar marco e +5/+10/+20 ciclos, além das trajetórias observadas inteiras; avaliar também a última observação dentro do domínio, nos completos como diagnóstico retrospectivo do endpoint e nos oficiais até o truncamento. Reportar cobertura bilateral por motor de toda a trajetória, cobertura unilateral, largura mediana por motor, quantis calibrados, finitude e antecedência de L no marco. A largura é do intervalo preditivo de F, não intervalo de confiança de uma média.

Contrastes ISO→RF_SLOPE e RF_HI→RF_SLOPE usam os mesmos motores/ciclos em cada repetição, com 2.000 reamostragens pareadas por motor para intervalos descritivos das diferenças de RMSE. As três repetições serão reportadas separadamente e por amplitude dos resultados, sem escolher a melhor semente, nem atribuir independência às estimativas entre folds/repetições. Cobertura em muitos ciclos de poucos motores não equivale a cobertura em muitos motores.

Favorável: qualidade/viés estáveis e cobertura próxima dos níveis nominais com largura e limite inferior informativos. Misto: cobertura acompanhada de bandas largas/ausência de antecedência; ou ganho dependente da partição. Contrário: subcobertura ou piora preservadas, sem ajustes posteriores do protocolo para eliminá-las. A utilidade operacional permanece aberta sem tolerâncias fundamentadas. Não selecionar um modelo por um melhor resultado isolado.

## Fundamento e limites

A regra de ordem estatística com correção de tamanho amostral e a separação entre ajuste e calibração seguem a construção split conformal descrita por [Lei et al. (2018), seção 2, equações 2–3 e seção 2.2/Algoritmo 2](https://www.stat.cmu.edu/~ryantibs/papers/conformal-jasa.pdf), DOI 10.1080/01621459.2017.1307116. Essa referência sustenta a calibração marginal sob permutabilidade. O escore máximo da trajetória por motor e o domínio após o marco são a adaptação deste experimento, não um resultado aeroespacial atribuído ao artigo. A validade teórica depende de motores/escores permutáveis e modelos fixados fora da calibração; não é cobertura condicional a cada condição/HI ou garantia de safety. Escolhas passadas sobre dados reutilizados, possível mudança de distribuição, poucos motores de calibração e truncamento limitam a inferência. A rodada avalia cobertura empiricamente, sem reivindicar confirmação independente ou novidade teórica.

Saídas em experiments/artifacts/pilot_f_uncertainty_09/: partições, modelos/quantis congelados, previsões por ciclo, escores U/E, métricas individuais e agregadas, comparações pareadas, relatório/figura, fontes/versões/hashes e verificação. Testar separação, causalidade, ausência de informação futura nos parâmetros, quantil com +∞ e distinção entre cobertura pontual/simultânea. Artigo M17, inspeções e economia permanecem sem alteração; protocolo principal não é congelado por esta rodada.
