# P19.1 — pipeline de confirmação em FD002 e FD004, especificado sem abrir os dados

Especificado em 18/10/2026, depois do congelamento (`congelamento_2026-10-18/`) e antes de qualquer leitura de `train_FD002.txt` ou `train_FD004.txt`. Registra os detalhes que o protocolo congelado deixou em aberto (emenda E01 em `emendas.md`, com FD002 e FD004 não abertos). Não muda regras, parâmetros fixos, critérios ou métricas do protocolo congelado.

## Lacunas do protocolo congelado que esta especificação fecha

1. **Configuração do HI (τ, γ, ridge) para FD002 e FD004.** Em FD001 e FD003 os valores vieram da grade interna de P05 e P06. Para os domínios novos usa-se a **mesma grade e o mesmo critério** (12 candidatos τ ∈ {60, 100, 140}, γ ∈ {1, 2}, ridge ∈ {0; 0,1}; RMSE do conversor isotônico nos cortes de 50, 70 e 90% da vida; empate pelo nome), uma vez por domínio, em um **grupo de configuração** de 80 motores sorteados com semente fixa (40 de ajuste, 20 de conversor, 20 de seleção). Esses 80 motores **não entram** nas partições de avaliação. Normalizador de regimes e HI são ajustados nos 40 de ajuste. A configuração escolhida é registrada e congelada antes de qualquer partição de avaliação.
2. **Partições de avaliação.** Sobre os motores restantes do domínio: 10 dobras, três repetições (sementes de P10), E = um bloco da permutação, e, com os demais, F = 25, C = 15, U = 50 motores sorteados (os mesmos tamanhos de desenvolvimento). Todos os motores restantes entram em E uma vez por repetição. Repetições reusam motores e nunca são somadas.
3. **Normalização.** `RegimeNormaliser(k=6)` (P18.1) ajustado em F de cada dobra, aplicado a F, C, U, E. Nenhuma outra variante.
4. **Unidade de avaliação.** Treino completo (vidas até a falha); o teste oficial truncado de FD002 e FD004 **não é lido**.

## Saídas por domínio, repetição e dobra

- Previsões ISO e RF com inclinação em U e E; escores por motor e margens de 98% e 95% calibradas só em U (como P10).
- Regras (M38): ISO e RF com inclinação, limite inferior 98%, reserva 15, prazos 1 e 2; controle pelo marco HI; ISO e RF de ponto central, reserva 15 (contraste do braço de inspeção, sem inspeção); controle de idade fixa em 127 (decisão em 127 − d, retirada em 127). Sensibilidades: limite inferior 95% e reserva 12.
- Extensão acima de 127 sob monitoramento inválido com probabilidade u da grade de M39 (expectativas exatas de P16.1).
- Eventos separados (sem decisão, chegada exata, ultrapassagem estrita) com limites de Clopper-Pearson unilaterais de 95%; restaurações por 10.000 ciclos simulados, economia frente a 127 e ao marco HI com bootstrap de motores (2.000 reamostragens); cobertura da trajetória, antecedência conservadora e largura das margens; diagnósticos de regime (silhueta, menor grupo, concordância entre sementes); canais retidos e disponibilidade do marco.
- **Critério do limite de idade (M42):** contagem de motores com T ≤ 127 nos 509 motores de treino de FD002 e FD004 (todos, inclusive o grupo de configuração), limite superior de Clopper-Pearson unilateral de 95% ≤ 2% (até 4 ocorrências), e na mistura de 709 motores (até 7). Relatado como passa ou não passa e nunca como garantia.

Fora desta especificação: braço de inspeção (P17.1), cenário de 20 anos, receita e disponibilidade. Itens do protocolo congelado (seção 7) que não pertencem à seção 10.

## Trava de abertura

O módulo só lê FD002 e FD004 por `open_confirmation()`, que exige: (a) emenda de pré-abertura em `emendas.md` com o SHA-256 do módulo, dos testes e do verificador atuais; (b) que os hashes dos arquivos de treino coincidam com o manifesto do congelamento; (c) que não exista marcador de abertura anterior. O marcador `abertura.json` é gravado antes da leitura. Repetir exige renomear o marcador e registrar o motivo em `emendas.md`.

## Ensaio (sem FD002 e FD004)

Ensaio com 200 motores de FD001 ∪ FD003 e regimes sintéticos de P18.1, com os mesmos procedimentos e tamanhos de grupo (80 de configuração, 5 dobras, uma repetição). É teste de código, não resultado científico.

## Verificação

Testes unitários antes da execução (contagem de Clopper-Pearson, reprodução exata das partições de P10, disjunção, trava de abertura, causalidade das previsões, calibração só em U) e verificador independente que recalcula as decisões, as margens, as contagens e os agregados a partir das previsões gravadas. O verificador roda no ensaio e, depois, na confirmação.
