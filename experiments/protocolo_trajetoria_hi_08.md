# P08 — informação temporal do HI e controle direto por sensores

Especificação anterior ao ajuste/avaliação de P08, 16/10/2026. Autorizada pelo autor após P07. Rodada exploratória: os motores e testes oficiais já foram examinados. Perguntas RQ1/RQ7: a trajetória recente acrescenta informação prognóstica ao HI corrente? RQ6: quais grupos de atributos sustentam a previsão, com que estabilidade? Não é um novo teste de localização física de P.

## Representação fixa e informação disponível

Usar somente a combinação empírica de HI já congelada em P05 (FD001) e P06 (FD003), com os mesmos modelos por fold e modelo final. Não reaprender pesos, referências, canais, escala, direção ou alvo do HI. O estudo não seleciona uma fórmula nova nem afirma reconstruir o HI físico. Cada transformação recebe sensores, unidade e ciclo, sem endpoint/RUL; rótulos são anexados depois, para ajuste do prognóstico ou avaliação.

Para uma sequência causal y, usar os últimos 20 valores, sem extrapolar ou completar janelas. Com u=−9,5,…,9,5 e v=u²−média(u²): inclinação b=Σuy/Σu²; curvatura c=2Σvy/Σv²; variabilidade s=desvio padrão amostral. São coeficientes de ajuste polinomial local, não derivadas físicas observadas. O HI existe desde o ciclo 20; sua primeira janela completa termina no ciclo 39. Nenhum atributo usa idade absoluta, identidade do motor, endpoint, fração da vida, RUL verdadeira ou sensores futuros como entrada preditiva.

Representações e ablações:

| ID | Entradas |
|---|---|
| HI | HI corrente |
| HI_SLOPE | HI + inclinação |
| HI_CURV | HI + curvatura |
| HI_STD | HI + variabilidade |
| HI_FULL | HI + inclinação + curvatura + variabilidade |
| HI_NO_SLOPE | HI + curvatura + variabilidade |
| HI_NO_CURV | HI + inclinação + variabilidade |
| HI_NO_STD | HI + inclinação + curvatura |
| SENSOR_RAW | Valor corrente dos canais retidos, centralizado na referência individual e orientado/escalado pelos parâmetros congelados |
| SENSOR_MEAN | Média causal de 15 ciclos desses sensores, com a mesma centralização/orientação/escala do HI |
| SENSOR_FULL | SENSOR_MEAN + desvio padrão, raiz da média quadrática e assimetria dos afastamentos normalizados em 20 ciclos + inclinação e curvatura da média causal nos últimos 20 ciclos |

Todas as representações serão ajustadas/avaliadas somente em ciclos ≥39, para controlar disponibilidade. HI original e seus cruzamentos continuam sendo calculados desde 20: passagem anterior a 39 será explicitamente indisponível para a comparação no marco, sem deslocar a passagem. Manter motores sem passagem e testes com último ciclo <39 nos denominadores de cobertura. SENSOR_RAW é controle sem estatísticas móveis como atributos, mas ainda usa a referência individual no ciclo 20; não equivale a sensores sem pré-processamento.

## Separação, famílias e orçamento

Reusar os cinco folds por motor P05/P06: F40/C20/S20/E20. F e os rótulos de desenvolvimento anteriores produziram a construção congelada de HI; os novos preditores RUL serão ajustados SOMENTE em C20, com peso total igual por motor, sem usar seus identificadores como atributos. S20 seleciona regularização; E20 avalia. Isso iguala os motores de ajuste do conversor com a referência isotônica anterior. Ajuste final: HI congelado F60, prognóstico C20, seleção S20 e avaliação no teste oficial. Não reajustar o prognóstico em F∪C depois da seleção.

As configurações de HI congeladas já dependeram da seleção anterior e da calibração C. A reutilização dessas escolhas limita a inferência; o desenho não fornece nova confirmação independente. Não chamar S de amostra intocada ou criar intervalos preditivos com garantia formal por reutilizar S. O termo calibração em C designa o ajuste da conversão de condição em RUL.

Para cada representação, comparar regressão linear com penalização quadrática (Ridge), λ∈{0,1;1;10;100}, e floresta aleatória (RF), fixa em 150 árvores, profundidade máxima 12, mínimo de 5 observações por folha, semente 20261016. RF reutiliza configuração anterior; não haverá busca adicional após resultados externos. Padronização ponderada será ajustada somente em C para Ridge; RF não recebe padronização adicional. As famílias têm orçamentos diferentes: os contrastes de informação são interpretados dentro de cada família, não como competição exaustiva entre algoritmos. Todas as RUL previstas são truncadas inferiormente em zero.

Selecionar λ por RMSE em S nos mesmos cortes retrospectivos de 50/70/90% da vida, se ≥39, média quadrática com peso igual por motor; desempatar pelo menor λ. Esses cortes são posições de avaliação, não informação preditiva. Preservar todos os candidatos. Incluir conversor isotônico crescente reaprendido em C nos mesmos ciclos ≥39 (ISO_MATCHED) e conversor original congelado (ISO_FROZEN), contextual, ajustado anteriormente também em ciclos 20–38. Assim, uma diferença para o isotônico original não será confundida automaticamente com valor da trajetória.

## Avaliação e incerteza

FD001 principal e FD003 ajustado no próprio domínio como robustez; transferência direta não será repetida nesta rodada. Mesmo marco causal empírico HI≤0,5 para todos os métodos, sem redefinir F. Avaliar primeira passagem observada, +5/+10/+20 ciclos e última observação oficial; reportar separadamente trajetória completa e truncada, cobertura, antecedência real, RMSE, MAE, viés e fração de sobrestimação de F. O erro F̂−T é igual a RUL prevista menos real no mesmo ciclo. Arquivar previsões em todos os ciclos disponíveis ≥39 e medir RMSE por motor na história como diagnóstico, sem tratar ciclos como unidades independentes.

Contrastes pré-definidos, dentro de Ridge e RF: HI_FULL−HI; HI_FULL−cada ablação parcial; SENSOR_MEAN−SENSOR_RAW; SENSOR_FULL−SENSOR_MEAN; SENSOR_FULL−HI_FULL; HI_FULL−ISO_MATCHED e HI_FULL−ISO_FROZEN. Usar os mesmos motores/ciclos, interseção explícita e denominadores originais. Intervalos descritivos de 95% para diferenças de RMSE: bootstrap pareado de 2.000 amostras por motor, semente 20261016. Essa é incerteza das diferenças de desempenho, não intervalo preditivo individual ou garantia operacional. Não escolher níveis HI ou janelas pelo teste oficial.

## Contribuições dos atributos

No marco 0,5, medir importância por permutação dos grupos HI corrente/inclinação/curvatura/variabilidade de HI_FULL e de cada sensor (todos os seus atributos juntos) de SENSOR_FULL. Vinte permutações, semente fixa; nos folds, permutar entre motores de E do mesmo fold, preservando o modelo usado; no teste oficial, entre os motores com marco disponível. Guardar a variação do erro quadrático e ranks por fold/família. Reportar concordância de ranks entre Ridge/RF e estabilidade entre folds, além dos coeficientes Ridge. Correlação, permutações fora da distribuição e construção do HI limitam interpretação causal; concordância não prova fidelidade. As ablações com reajuste são evidência complementar à dependência por permutação, não verdade física.

## Interpretação e encerramento

Resultado favorável: redução consistente do erro por informação temporal, dentro da mesma família e nos mesmos motores/ciclos, sem perda ocultada de cobertura. Resultado nulo/contrário: intervalos amplos, ganho ausente ou piora preservados; atributos extras não serão mantidos apenas por complexidade. Ganho contra ISO mas não contra HI da mesma família indica efeito de conversor/capacidade, não demonstra valor da história. Ganho dos sensores diretos indica possível perda de informação na compressão em HI. Não declarar vencedor universal nem adoção por um resultado isolado. Antecedência e risco admissíveis continuam sem limites fundamentados.

Saídas em experiments/artifacts/pilot_hi_trajectory_08/: predições, cobertura, resumos, seleção, modelos congelados, contribuições, contrastes, relatório, interpretação, versões/hashes e verificação. Protocolos e resultados P01–P07 são preservados. Testes devem verificar janelas, coeficientes temporais, causalidade, isolamento dos endpoints e separação por motor. Sem inspeções, alteração de P/F, congelamento principal ou edição do artigo nesta rodada.
