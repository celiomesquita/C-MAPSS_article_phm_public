# P15.4 — limite único de idade (127 ciclos) para os quatro conjuntos

## Resultado e alcance

Por observação do autor, os quatro conjuntos C-MAPSS são do mesmo tipo de motor simulado sob condições diferentes, de modo que um limite conservador teria um único número. Adotado: **A = 127 ciclos** nos dois conjuntos examinados (mínimo do FD001 menos um; o mínimo do FD003 é 145). Substitui o par 127/144 de P15.2/P15.3, que fica arquivado. FD002 e FD004 continuam reservados: não foram lidos nem calculados, e o limite foi fixado antes de abri-los. Política candidata (M27), sem crédito nem validação de segurança; exploratório, sem inspeção; fallback por idade vencida.

## Consequência estatística da mistura

Nos 200 motores de treino de FD001 e FD003 nenhum tem T ≤ 127. Limite superior de Clopper-Pearson de P(T ≤ 127): **0,80% (confiança 80%), 1,14% (90%) e 1,49% (95%)**, todos ≤ 2%. A limitação de P15.2 (n=100: 2,28% e 2,95% a 90% e 95%) deixa de impedir a afirmação, mas a conclusão vale para a mistura dos dois conjuntos nas proporções amostradas e **em amostra**. Para o FD001 sozinho o limite de 95% continua 2,95%. Se os 509 motores de FD002 e FD004 tiverem todos T > 127, o limite de 95% sobre os 709 motores seria 0,42%. Isso exige abrir esses conjuntos uma única vez, após o congelamento, com a idade já fixa; uma ocorrência deve ser relatada sem ajustar a idade.

## Efeito sobre a política PHM → idade (média das três repetições, prazo 1)

- **FD001:** idêntico a P15.3 (a idade já era 127): a idade atua em 89–99% dos motores; vida de 126–127 ciclos contra 167–192 do PHM original.
- **FD003:** com 127 em vez de 144, a idade atua em 98–100% dos motores (ISO inferior 98%: 98,0%); vida de 126,9–127,0 ciclos contra 208–233 do PHM original. Economia de restauração frente ao controle de idade de P13.1 (vida média 146,7): −15,5% a −15,6% (era −1,9% a −2,9% com 144). Frente ao marco HI: cerca de −63,6%.
- **Cenário central de 20 anos** (L_ref 8.425, 1.600 voos/ano, prazo 1): FD003 com 7,39 visitas por posição sem LLP e 8,15 com LLP 20.000, para qualquer das sete regras. As regras PHM ficam indistinguíveis entre si porque a idade decide em quase todos os motores.
- **Zero ausências, chegadas exatas e ultrapassagens** em todas as 84 combinações é consequência da construção (127 está abaixo do mínimo dos motores E avaliados), não evidência de segurança.

## Interpretação

Um limite único conservador é custoso para o conjunto de vidas mais longas: o FD003 passa a cumprir um limite determinado pelo motor mais curto do FD001. A política com 127 ciclos é, na prática, a regra de idade; o PHM só decide primeiro em 0–2,3% dos motores do FD003 e em até 11% dos do FD001. A concordância do autor com a premissa de que o limite deveria ser único é coerente com a lógica de um documento de limite de vida, que não teria um número por condição de simulação; a validade do número para o tipo de motor depende de FD002 e FD004, ainda não consultados.

## Verificação

Cinco testes passaram antes da execução (idade única igual ao menor mínimo menos um dos conjuntos examinados; nenhum motor E com T ≤ A − d; limites de Clopper-Pearson de n=200 e n=709; decisão em todos sem eventos; entradas sem FD002/FD004). O verificador independente reconstruiu 8.400 linhas híbridas por laços e 84 resumos, e conferiu os manifestos anteriores. Os limites de Clopper-Pearson foram calculados por bisseção da binomial no executor e conferidos nos testes contra a forma fechada 1 − (1 − γ)^(1/n) para k=0. Sem emendas.
