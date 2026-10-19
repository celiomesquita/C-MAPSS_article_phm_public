# P15.2 — idade conservadora por conjunto de dados

Especificado em 18/10/2026 antes da execução, por solicitação do autor: ignorar a ARP7122 e estimar quantidades de ciclos conservadoras para cada conjunto de dados. Interpretação adotada (a corrigir se for outra): a quantidade é a **idade fixa de reserva** da política candidata PHM → idade (M27), um valor por conjunto (FD001, FD003). Exploratório, descritivo, sem inspeção. Não adota política nem concede crédito.

## Quantidade e critério

Idade de retirada A (decisão em A − d). Critério conservador: a estimativa da probabilidade de o endpoint ocorrer em ou antes de A, P(T ≤ A), não excede **2%**, a tolerância experimental de M19 (que não é evidência de segurança). Chegadas exatas contam, pois a convenção do projeto trata T como evento. O prazo d não entra na estimativa de A.

## Dados

Os 100 motores de treino de cada conjunto, até a falha (`train_FD001.txt`, `train_FD003.txt`). **Todos os 100 entram na estimativa**: o resultado é um valor de nível de conjunto, não uma idade ajustada em partição. Por isso é **em amostra** em relação aos motores E de P10 a P15.1; usar o valor nesses motores só pode mostrar consistência com os próprios dados, nunca validação. Sem testes oficiais, arquivos RUL, FD002 ou FD004. A estimativa para FD002/FD004 exigiria premissa própria (regimes distintos), não é feita aqui.

## Estimadores (todos relatados, nenhum selecionado como oficial)

1. **E0, referência do projeto**: A = T_(1) − 1 (mínimo do conjunto menos 1, como o controle de idade de P11 mas com todos os 100 motores).
2. **E1, limite não paramétrico**: A é a maior idade tal que o limite superior de Clopper-Pearson de P(T ≤ A), dado N(A) = nº de motores com T ≤ A entre n=100, é ≤ 2%, para confiança γ ∈ {0,80; 0,90; 0,95}. Se nenhuma idade satisfaz, relatar "inviável com n=100" e o menor limite superior alcançável (N=0) em cada γ.
3. **E2, paramétrico**: ajuste de Weibull de dois parâmetros (posição 0, máxima verossimilhança) e log-normal; A = limite inferior de confiança 95% (bootstrap paramétrico, B=2.000, semente 20261018) do quantil 2% do modelo. Teste de ajuste: estatística de Kolmogorov-Smirnov e Anderson-Darling com valores-p por bootstrap paramétrico (B=500), para dizer se o modelo é plausível. Relatar mesmo que o ajuste seja ruim.
4. **E3, consistência fora da amostra do estimador E0**: para cada motor i, A_(−i) = min dos outros 99 − 1; fração de motores com T_i ≤ A_(−i). Estima a taxa de chegada por idade que um operador que usa esta regra teria com um novo motor da mesma população, sem implicar a população futura.

## Medidas descritivas por conjunto

n, mínimo, quantis 1%, 2,5%, 5%, 10%, mediana, máximo da vida T; vida média aproveitada sob a idade (média de min(T, A)); ciclos não usados médios (T − A para T > A); taxa de restauração 1/vida aproveitada; razão à vida média das regras PHM de P12.1 apenas como contexto.

## Interpretação prévia

- Com n=100 e nenhuma ocorrência, o limite de 2% só pode ser afirmado em confiança baixa (≈86%); isso é uma restrição de tamanho amostral e não depende do método do estimador.
- Estimadores paramétricos extrapolam a cauda; o FD003 reúne dois modos de falha e vidas longas, e o ajuste pode ser ruim; o resultado paramétrico nesse caso é informativo apenas se o teste de ajuste não rejeitar.
- Nenhum valor é adotado. A escolha de A, confiança e estimador é decisão do autor.

## Verificação e artefatos

Testes antes da execução: leitura restrita a train FD001/FD003; Clopper-Pearson reproduz valores conhecidos (N=0, n=100); ordem-estatística reproduz mínimo − 1; E3 conta apenas o motor mínimo quando o mínimo é único; reprodutibilidade das sementes. Verificador independente refaz E0, E1, E3 e as estatísticas descritivas por laços, o limite de Clopper-Pearson por inversão da binomial (sem scipy.stats.beta), e confere manifestos anteriores; E2 é replicado com a mesma sequência aleatória e implementação própria da inversão. Saídas em `artifacts/pilot_conservative_age_15b`.
