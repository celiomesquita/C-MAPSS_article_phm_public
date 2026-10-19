# P19.2 — estabilidade dos coeficientes do HI entre dobras, nos quatro subconjuntos

Especificado em 18/10/2026 (emenda E05), antes do código. Responde ao objetivo de explicabilidade sem ajustar nada: usa só os modelos já gravados (30 por subconjunto: `pilot_f_uncertainty_10/models_*` para FD001 e FD003, `confirmation_19a/models_*` para FD002 e FD004). Não lê dados brutos, não reajusta modelos e não escolhe canais.

## Medidas (por subconjunto e repetição, sobre os pares de dobras)

Para cada par de dobras (45 por repetição), sobre os canais retidos (elegíveis) em ambas: correlação de Spearman entre os pesos do HI; fração de canais com a mesma orientação (sinal da direção); sobreposição (Jaccard) dos canais com peso positivo; sobreposição dos três canais de maior peso. Por canal, subconjunto e repetição: fração das 10 dobras em que é retido, em que tem peso positivo e em que tem orientação positiva, e peso médio e mediano quando positivo.

## Interpretação prévia

Descritivo: estabilidade de coeficientes é uma propriedade de explicação do HI e não prova de fidelidade física (P13.2 a P13.5). O HI é ajustado em 25 motores, e FD002 e FD004 incluem seis regimes normalizados. Todas as repetições e dobras são relatadas; as repetições reutilizam motores e não são somadas como independentes. Sem limiar de aprovação.

## Verificação

Testes com registros sintéticos (pesos idênticos dão Spearman 1 e Jaccard 1; inversão de direção é detectada; canais ausentes são tratados como não retidos). Verificador independente, por laços escalares, relê os modelos e refaz todas as medidas.
