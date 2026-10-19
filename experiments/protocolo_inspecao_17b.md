# P17.1 — execução do braço de inspeção boroscópica (protocolo de execução)

Escrito em 18/10/2026, depois do congelamento e da confirmação, antes do código. Executa o braço já especificado em `especificacao_braco_inspecao_17a.md` e congelado na seção 6 do protocolo principal. Os detalhes abaixo fecham lacunas de execução (emenda E04). **Nenhum sensor nem arquivo bruto é lido:** as decisões do PHM vêm das decisões arquivadas de P13.1 (FD001 e FD003, desenvolvimento) e de `confirmation_19a/decisions.csv` (FD002 e FD004, já examinados). Os resultados nos quatro subconjuntos são exploratórios; as vidas e as decisões do PHM são tratadas como fixas.

## Definição

Para o motor com fim de vida T, prazo de execução d e decisão do PHM D (se existir), com probabilidade u de monitoramento inválido por ciclo (M39, detectado de imediato), a decisão ocorre no primeiro ciclo t, entre o início e T − 1, em que: o monitoramento está inválido (para t ≥ 127 − d); ou t = D; ou há inspeção em t e ela reprova. A retirada é em t + d (convenção de P16.1). Aprovação não posterga. As inspeções terminam na decisão e T não é oportunidade. Ordem do ciclo: validade, decisão do PHM, inspeção.

- **Probabilidade de reprovação:** p(t) = p_P + (p_F − p_P)·q(t)^γ, com q(t) = 1 − clip((T − t)/W, 0, 1); inspeções independentes dado o motor.
- **Entrada S2 (política observável):** t = 127, 132, 137, … ≤ T − 1. **S1 (idealizada, informação privilegiada):** t = max(1, T − W) + 5k ≤ T − 1.
- **Expectativas exatas** (sem sorteio) de vida aproveitada, chegada estrita além de T, chegada exata, ausência de decisão, número de inspeções e probabilidade de a decisão vir de reprovação. Referência pareada: o mesmo PHM sem inspeção, mesmo u (P16.1).

## Cenários

Manchete: S2, W = 60, γ = 1, p_P = 0, p_F = 1, u = 0. Sensibilidades: W ∈ {30, 80}; γ ∈ {0,26; 2} com W = 60; p_P = 0,02 com W = 60, γ = 1; S1 com W ∈ {30, 60, 80}, γ = 1. A grade de u de M39 só no cenário manchete.

## Regras (M38)

Contrastes primários, regras que têm eventos: ISO e RF com inclinação, ponto central, reserva 15. Também relatadas: ISO e RF com limite inferior 98% e o marco HI (sem eventos no desenvolvimento), prazos 1 e 2.

## Saídas

Por motor e agregadas por subconjunto, repetição, regra, prazo, cenário e u: restaurações por 10.000 ciclos simulados (híbrido e PHM), variação relativa da taxa, vida cedida por motor, eventos esperados por 100 motores, inspeções por motor, fração de decisões por reprovação, economia frente a 127; intervalos bootstrap de motores (2.000) para a variação da taxa. Custo e duração da inspeção, zero. Cenário de 20 anos e receita não entram.

## Verificação

Testes (antes da execução): p ≡ 0 reproduz `engine_expectation` de P16.1; p ≡ 1 dá reprovação na primeira inspeção; a vida esperada do híbrido nunca excede a do PHM; enumeração por força bruta e Monte Carlo concordam; ordem do ciclo e fim das inspeções. Verificador independente por laços recalcula todas as expectativas, os agregados e as comparações com o PHM. Não há leitura de FD002 ou FD004 brutos.
