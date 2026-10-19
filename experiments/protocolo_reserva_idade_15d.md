# P15.4 — limite único de idade para os quatro conjuntos

Especificado em 18/10/2026 antes da execução, por observação do autor: os quatro conjuntos C-MAPSS são do mesmo tipo de motor simulado sob condições diferentes, de modo que um limite de vida conservador num documento teria **um único número**, e não valores por conjunto. Exploratório, sem inspeção; política candidata (M27), sem crédito nem validação de segurança.

## Decisão de projeto

O limite único é o menor valor conservador entre os conjuntos já examinados: **A = 127 ciclos** (mínimo do FD001 menos um; o mínimo do FD003 é 145). Substitui o par 127/144 de P15.2/P15.3, que permanecem arquivados como histórico. A idade é fixada **antes** de abrir FD002 e FD004, que continuam reservados e não são lidos nem calculados aqui.

## Consequências estatísticas

- Com os dois conjuntos examinados (n=200 motores de treino, nenhum com T ≤ 127), o limite superior de Clopper-Pearson de P(T ≤ A) é 0,80% (confiança 80%), 1,14% (90%) e 1,49% (95%), todos ≤ 2%. A limitação de tamanho amostral de P15.2 (n=100) deixa de se aplicar à mistura. Isso vale para a população-mistura dos dois conjuntos nas proporções amostradas, não para cada condição isoladamente; para o FD001 sozinho o limite de 95% permanece 2,95%.
- A afirmação é em amostra. Os 509 motores de treino de FD002 e FD004 servem de confirmação **única**, com a idade já congelada: se nenhum tiver T ≤ 127, o limite superior de 95% sobre os 709 motores seria 0,42%; um evento já deve ser relatado, sem ajuste da idade. A confirmação exige o congelamento do protocolo principal e uma decisão do autor para abrir esses conjuntos.

## Desenho

Mesmas 7 regras PHM de P13.1, prazos 1 e 2, medidas, comparações pareadas, telas e cenário central de 20 anos de P15.3, com A=127 nos dois conjuntos. Zero ausências, chegadas exatas e ultrapassagens continuam consequência da construção, pois 127 está abaixo do mínimo dos motores E avaliados. Informativas: fração em que a idade atua e vida cedida. Somente train FD001/FD003.

## Verificação e artefatos

Testes: idade única igual ao menor mínimo menos um dos conjuntos examinados; nenhum motor E com T ≤ A − d; limites de Clopper-Pearson de n=200 e n=709; entradas sem FD002/FD004. Verificador independente por laços e bisseção binomial. Saídas em `artifacts/pilot_fallback_15d`.
