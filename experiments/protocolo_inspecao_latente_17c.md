# P17.2 — sensibilidade do braço de inspeção a um efeito latente por motor

Especificado em 18/10/2026 (emenda E05), depois da execução de P17.1 e antes do código. P17.1 usou inspeções independentes dado o motor. Aqui cada motor tem uma visibilidade do dano diferente e desconhecida pela política, de modo que as inspeções sucessivas do mesmo motor ficam dependentes. Exploratório, condicional ao gerador, sem calibração.

## Modelo

Cada motor i recebe z_i ~ N(0, 1), independente do HI e do PHM. Três variantes, todas com o cenário de P17.1 (S2, p_P = 0, p_F = 1, W = 60, γ = 1) como centro:

- **L1:** janela do motor W_i = 60 · exp(0,25 z_i).
- **L2:** janela do motor W_i = 60 · exp(0,5 z_i).
- **L3:** forma do motor γ_i = exp(0,5 z_i), com W = 60.

Dado z_i, as inspeções são independentes (P17.1). A esperança de cada desfecho do motor é a integral sobre z_i, calculada por quadratura de Gauss-Hermite (probabilista) com 21 nós, determinística e sem sorteio. O limite σ → 0 reproduz P17.1.

## Execução

Mesmas decisões arquivadas, subconjuntos, regras (as cinco regras de P17.1), prazos 1 e 2 e u = 0. Mesmas saídas e bootstrap de motores (2.000, sementes de P17.1) que P17.1, com comparação direta com o cenário independente: variação da taxa de restauração, vida cedida, eventos esperados por 100 motores, inspeções por motor, fração de decisões por reprovação.

## Verificação

Testes: σ → 0 reproduz `hybrid_expectation`; os pesos somam 1 e a quadratura integra momentos conhecidos da normal; a esperança por quadratura coincide com um Monte Carlo de z para um caso; reprovação nunca posterga. Verificador independente: reimplementação escalar de P17.1 (`verify_inspection_arm_17b.one`) com nós de Gauss-Hermite próprios (`numpy.polynomial.hermite_e`).
