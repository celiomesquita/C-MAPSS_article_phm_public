# P20.1 — cenário de 20 anos para os quatro subconjuntos e os três braços

Especificado em 18/10/2026, depois do congelamento, da confirmação e do braço de inspeção, antes do código (emenda E05). Exploratório e condicional. Estende P12.2 (ponte de escala, LLP, utilização, condições iniciais, restauração parcial) a FD002 e FD004 e aos três braços do protocolo congelado (seção 8): **idade fixa de 127 ciclos**, **PHM somente por sensores** e **PHM + inspeção**. Receita, disponibilidade e parâmetros de companhia continuam excluídos (M40).

## Entradas

Só decisões arquivadas: `pilot_policy_selection_13a/decisions.csv` (FD001, FD003) e `confirmation_19a/decisions.csv` (FD002, FD004), 100, 100, 180 e 169 motores de avaliação por repetição. Nenhum arquivo bruto é lido. Para a escala, T̄ de cada subconjunto vem de `lives_*.csv` da confirmação (FD002, FD004) e dos arquivos de treino de FD001 e FD003 já usados em P12.2 (leitura somente da vida por motor).

## Braços e regras (por prazo de execução d ∈ {1, 2})

- **AGE127:** decisão em 127 − d, retirada em 127.
- **PHM:** ISO e RF com inclinação, limite inferior 98% e ponto central (reserva 15), e o marco HI, com monitoramento sempre válido (u = 0).
- **PHM + inspeção:** as mesmas cinco regras com o braço de P17.1 (S2, W = 60, γ = 1, p_P = 0, p_F = 1). Como a inspeção é aleatória, cada motor tem uma distribuição exata de desfechos (data da decisão); no cenário de renovação, cada vida sorteia o motor e depois o desfecho, com números aleatórios comuns a todos os braços.

## Simulação

Igual a P12.2: horizonte 20 × u FC; vida de degradação de k · ρ · (vida aproveitada) FC, com ρ = 1 na primeira vida e ρ ∈ {1; 0,8} nas seguintes; contador de LLP independente; sem limite de restaurações; custo fixo de US$ 6 milhões por visita (5 e 7 em pós-processamento linear). k = L_ref/T̄ com L_ref ∈ {4.000, 5.000, 6.000, 7.000, 8.425, 10.000, 12.000, 14.000, 16.500, 19.000}. Grade completa: 4 subconjuntos × 3 repetições × 10 L_ref × 3 utilizações (1.400, 1.600, 1.900) × 4 LLP (nenhum, 20.000, 25.000, 30.000) × 2 condições iniciais × 2 ρ = 5.760 células; 2.000 réplicas por célula. Cenário central, sem otimização: L_ref = 8.425, 1.600 FC/ano, LLP 20.000, frota madura, ρ = 1.

## Contrastes e validação

Pareados por réplica: cada regra PHM e cada regra híbrida contra AGE127 do mesmo prazo; híbrido contra o PHM da mesma regra. Classificação como em P12.2 (estável, indistinguível, invertido) em relação ao sinal analítico (taxa de renovação 1/E[vida]). Validação, predeclarada: (1) estado estacionário sem LLP, ρ = 1, frota madura: |z| < **4,5** em todas as células e braços (o limite é 4,5 e não 4 porque a família de testes é cerca de oito vezes maior que a de P12.2); (2) horizonte longo (2 × 10⁶ FC), erro relativo da taxa ≤ 1% nas duas condições iniciais; (3) visitas por LLP iguais em todos os braços da mesma réplica; (4) o simulador com desfechos únicos reproduz exatamente `simulate` de P12.2. Falha interrompe o relato.

## Interpretação prévia

Os resultados por ciclo simulado seguem como principais; o cenário é condicional a L_ref, utilização, LLP, condição inicial e ρ. Visitas por LLP são iguais entre braços e diluem diferenças por degradação. Nada seleciona k, utilização ou LLP. Nenhum ganho de companhia é afirmado.
