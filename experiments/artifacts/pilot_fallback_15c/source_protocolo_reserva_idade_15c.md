# P15.3 — política PHM → idade com as idades conservadoras de P15.2

Especificado em 18/10/2026 antes da execução, após o autor autorizar o uso das idades de P15.2: **A = 127 ciclos (FD001) e 144 ciclos (FD003)**. Exploratório, sem inspeção; a política continua candidata (M27): sem crédito, sem validação de segurança. O fallback permanece o testado em P15.1: a regra de idade atua se o PHM ainda não decidiu quando a idade é atingida (decisão em A − d, retirada em A; empate prevalece o PHM). Fallback por indisponibilidade do monitoramento não é simulado.

## Desenho

Mesmas 7 regras PHM de P13.1 e prazos 1 e 2 de P15.1, com a idade fixa por conjunto no lugar da grade de quantis de desenvolvimento. Mesmas medidas, comparações pareadas (bootstrap de motores, semente 20261018), telas de P11 e cenário central de 20 anos de P12.2 (L_ref 5.000, 8.425 e 12.000; 1.600 voos/ano; LLP sem e 20.000; frota madura). Somente train FD001/FD003, motores E de P13.1; repetições separadas.

## Advertência de origem

As idades são o mínimo menos um dos 100 motores de cada conjunto, **inclusive os motores E avaliados**. Logo, a regra de idade nunca encontra o endpoint nesses motores (T ≥ 128 e 145 > A − d), e **zero ausências, chegadas exatas e ultrapassagens são consequência da construção**, não evidência de segurança. As medidas informativas são a fração de motores em que a idade atua e a vida cedida frente ao PHM original.

## Verificação e artefatos

Testes: idades iguais às de P15.2; nenhum motor E com T ≤ A − d; híbrido não posterior a nenhum componente; reprodução do hybrid() de P15.1. Verificador independente por laços das colunas brutas. Saídas em `artifacts/pilot_fallback_15c`.
