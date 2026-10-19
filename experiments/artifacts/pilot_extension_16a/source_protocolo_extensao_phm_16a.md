# P16.1 — extensão da vida pelo PHM acima do limite de 127 ciclos

Especificado em 18/10/2026 antes da execução, por proposta do autor: **sem dados de sensores o limite seria 127 ciclos; com dados, o PHM pode estender a vida de cada motor segundo a condição do HI.** Isto difere de P15.1 a P15.4, onde a idade era um teto (min entre PHM e idade) e a política colapsava na regra de idade. Aqui a idade é o limite **sem monitoramento**; com monitoramento válido o PHM governa sem teto. Exploratório, sem inspeção, sem refit, política candidata (M27), sem crédito nem validação de segurança.

## Política analisada

- Limite sem dados: remoção em A = 127 ciclos (decisão em τ = A − d), valor único (M30).
- Regras PHM: as 7 regras congeladas de P13.1 (ISO e RF_SLOPE inferior 98% e de ponto, marco HI, limiar e espera selecionados), prazos 1 e 2. Decisão PHM D e retirada D + d, como no original.
- **Verificação de validade do monitoramento.** Para um motor que ainda opera no ciclo τ sem decisão PHM (D > τ ou sem decisão), a continuidade acima de 127 depende de dados válidos. A cada ciclo t = τ, τ+1, …, E (E = D se há decisão, senão T − 1) o monitoramento está inválido com probabilidade u, independente entre ciclos. Se inválido em t = τ: remoção em 127. Se inválido em t > τ: pedido de remoção imediato, retirada em t + d. Se válido em todos: resultado original do PHM. Motores com decisão PHM em ciclo ≤ τ não são afetados (sem indisponibilidade antes do portão; limitação declarada).
- **u é um eixo de sensibilidade, não valor adotado.** Grade: 0 (monitoramento sempre válido, regra PHM original), 0,0005, 0,001, 0,002, 0,005, 0,01, 0,02, 1 (nenhum dado: idade 127). O autor não especificou modelo de perda de dados; a independência entre ciclos é uma hipótese de trabalho, que subestima interrupções longas e correlacionadas.

## Cálculo

Expectativas exatas por motor (soma sobre o primeiro ciclo de falha de validade), sem simulação aleatória: P(primeira falha em t) = u(1−u)^{t−τ}, P(todos válidos) = (1−u)^{E−τ+1}. Com a vida esperada de cada motor somam-se as taxas de restauração por ciclo simulado (n / Σ vida esperada) por conjunto, repetição, regra e prazo; repetições permanecem separadas. Eventos esperados por 100 motores: ultrapassagens estritas, chegadas exatas e ausências de decisão. Para u=0 o resultado é o PHM original; para u=1, o limite de 127.

## Medidas adicionais

- Extensão e = retirada − 127 por motor e regra; fração dos motores estendidos; fração da folga T − 127 recuperada.
- Dependência da condição: HI no ciclo 127 (saída ISO de P10 para os motores E) contra a extensão; Spearman e médias por terço do HI.
- Economia de restauração frente ao limite de 127 e frente ao controle de idade de P13.1, com bootstrap de motores (2.000, semente 20261018) para u=0.
- Contexto de 20 anos de P12.2 (L_ref 8.425, 1.600 voos/ano, LLP 20.000, frota madura) apenas por vida esperada aproximada; sem simulação nova.

## Interpretação prévia

- Com monitoramento válido, a vida nunca é pior que 127: toda perda de dados em t > τ gera retirada em t + d ≥ 127. O custo da perda de dados é o risco de ultrapassagem quando t + d > T, que a análise quantifica por motor.
- Zero ultrapassagens em motores E examinados não prova risco ≤ 2%. As regras PHM de ponto têm eventos próprios (P11/P13.1). O ganho depende da qualidade do PHM e da disponibilidade; nenhum valor de u foi escolhido.
- A extensão acima de 127 entra em uma região onde existem motores que falham; a validade do PHM nessa região é o que a política afirma, e não o limite de 127.

## Verificação e artefatos

Testes antes da execução: u=0 reproduz as linhas originais; u=1 reproduz 127; probabilidades somam 1; fórmula fechada igual à enumeração por força bruta para motores construídos; Monte Carlo grande concorda com a fórmula; entradas sem FD002/FD004. Verificador independente: enumeração por laços das colunas brutas, comparação de médias e eventos esperados, e conferência dos manifestos anteriores. Saídas em `artifacts/pilot_extension_16a`.
