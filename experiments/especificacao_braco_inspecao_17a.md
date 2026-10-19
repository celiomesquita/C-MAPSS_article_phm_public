# Especificação do braço de inspeção boroscópica (P17.1)

Redigida em 18/10/2026 por solicitação do autor. **Somente especificação: nada foi executado.** As inspeções simuladas só podem ser executadas depois do congelamento do protocolo principal (decisão do autor). Os valores marcados como **proposta** são candidatos para decisão do autor e não estão adotados. A política candidata é a de M31/M32; a inspeção não tem custo nem duração incrementais (M21), mas o número de inspeções e de reprovações é contado.

## 1. Papel da inspeção na política

- **Gatilhos de remoção** (M32): perda de monitoramento válido, decisão do PHM e **reprovação na inspeção**. A reprovação só **antecipa** a decisão: τ_h = min(τ_PHM, primeira reprovação elegível), retirada em τ_h + d com o mesmo d ∈ {1, 2}. A aprovação nunca posterga a retirada, e a inspeção **não sustenta** a operação quando o PHM está indisponível (M32).
- **Fim das inspeções:** a decisão de remoção por qualquer gatilho encerra as inspeções; o endpoint não é oportunidade de inspeção.
- **Informação para a política:** só o resultado binário (aprova ou reprova) e o ciclo em que ocorreu. A política nunca vê o HI de referência, a RUL verdadeira nem o ciclo real de P ou F.
- **Correspondência com o IP 180:** é um candidato conceitual a "AHM híbrido" (tarefa clássica de inspeção complementada por monitoramento). O IP pressupõe uma tarefa clássica do MRBR; aqui a base é a política de M31.

## 2. Mecanismo gerador da observação (ambiente)

Família já aceita pelo autor (contrato FD001): com q(t) = clip[(H_P − H_ref(t))/(H_P − H_F), 0, 1] e H_F = 0,

p_rep(t) = p_P + (p_F − p_P)·q(t)^γ,  Y_t ~ Bernoulli(p_rep(t)), Y_t = 1 reprova.

**Referência de condição H_ref (ambiente, não o HI estimado).** Está pendente desde M14. **Proposta:** definir a condição do ambiente pela vida restante verdadeira da trajetória completa, que o simulador conhece e a política não: q(t) = 1 − clip(RUL(t)/W, 0, 1), com RUL(t) = T − t e W a janela P–F (em ciclos). Assim P_ref = T − W e q = 0 antes de P_ref; q = 1 em F. É a mesma convenção já usada nos alvos do projeto (min(1, RUL/ρ)^η) e evita usar o HI empírico de M18 como gerador. Alternativa: janela proporcional à vida, W_i = φ·T_i. As duas são hipóteses de cenário, sem calibração, e a escolha é do autor.

**Parâmetros a decidir (propostas de grade, nenhum adotado):**

| Parâmetro | Significado | Proposta |
|---|---|---|
| W | janela P–F em ciclos | grade **{30, 60, 80}** ciclos (decisão de 18/10/2026; justificativa em §2.1); sem referência que a recomende |
| p_P | reprovação sem dano detectável (falso positivo) | 0 como base; sensibilidade 0,02 |
| p_F | reprovação em F | 1 (já candidato no contrato) |
| γ | forma da curva | base **γ = 1** (linear, neutra); sensibilidade {0,26 (antecedente, §6), 2}; proposta provisória, ver §2.2 |
| Δ | intervalo entre inspeções | 5 ciclos (definido pelo autor) |
| dependência | entre inspeções sucessivas | independentes dadas as condições (base); sensibilidade com efeito latente por motor |

## 3. Quando as inspeções começam

O contrato diz "somente no intervalo P–F, nunca antes de P". P físico não é observável; duas leituras:

- **S1, idealizada (informação privilegiada):** inspeções a cada Δ a partir de P_ref = T − W. Usa a data verdadeira de P para iniciar as inspeções: admissível só como cenário idealizado identificado, nunca como política operacional.
- **S2, observável (proposta):** P observável = o **portão de 127 ciclos**: o motor que o PHM mantém em operação além do portão é inspecionado a cada Δ ciclos a partir do ciclo 127, até a decisão. Abaixo de 127 o projeto já tem o limite sem monitoramento e não precisa de informação adicional. Algumas inspeções cairão antes de P_ref (q = 0, reprovação só com p_P), e isso é consistente com a leitura de que a política não conhece P.

O autor deve escolher S2 como regra de política e S1 como cenário de referência, ou outra regra de entrada.

## 4. Ordem dentro do ciclo e tratamento exato

1. Fim do ciclo t: dados de sensores, atualização do PHM, decisão do PHM se o gatilho de condição é atingido.
2. Se t está na grade de inspeção (t = 127 + kΔ) e nenhuma decisão foi tomada: inspeção com resultado Y_t.
3. Se Y_t = 1 ou há decisão do PHM em t: decisão em t; retirada em t + d (prazo de execução). A perda de monitoramento segue M32.
4. A retirada em t + d > T é ultrapassagem; = T, chegada exata; sem decisão até T, ausência de decisão (convenções de P11).

**Cálculo.** Dadas as trajetórias congeladas de P13.1, a probabilidade de aprovação até a j-ésima inspeção é Π(1 − p_k) para inspeções independentes. Isso permite **expectativas exatas** por motor, como em P16.1, sem simulação aleatória; efeitos latentes ou dependência exigem Monte Carlo com sementes fixas.

## 5. Contrastes e métricas

- **Contraste principal pareado:** PHM + inspeção contra o mesmo PHM sem inspeção, nos mesmos motores, previsões e prazos. Métricas: inspeções por motor, taxa de reprovação, antecipação média (τ_PHM − τ_h), vida cedida, restaurações por ciclo simulado, ultrapassagens estritas, chegadas exatas e ausências de decisão; cenário de 20 anos de P12.2 com o simulador existente. Custo e duração da inspeção, zero.
- **Observação crítica de desenho.** Como a reprovação só antecipa, o braço híbrido **nunca ganha vida frente ao PHM sozinho**; só pode reduzir eventos ao custo de vida. Nas regras de limite inferior 98% e no marco HI não há eventos em 300 vidas, de modo que o híbrido apenas perde vida nessa amostra. O teste informativo é com regras que **têm eventos**: ISO e RF_SLOPE de ponto central (FD001: 23 ausências e 11 chegadas exatas em 300 vidas para ISO ponto) e as selecionadas de P13.1. Perguntas: (i) quanto da vida a regra de ponto preserva ao sair do mesmo nível de eventos do limite inferior 98% quando a inspeção é adicionada; (ii) se a inspeção substitui parte da margem conforme. Esses contrastes são exploratórios e não comparam admissibilidade igual sem informar eventos.
- **Controle informacional CM03 (inspeção sem PHM): não incluído**, por decisão do autor em 18/10/2026.
- **Sensibilidade:** W, p_P, γ, dependência, S1 contra S2. Relatar também onde a ordenação das regras muda.

## 6. Antecedente próximo (tese de Miranda, ITA)

A tese de Miranda (seção 4.4) usa um POD log-normal de Berens: dano visível quando a condição de saúde (THC) chega a 0,8, POD de 90% em 0,6 e de 99% em 0,5 (o limiar obrigatório de remoção), μ = −0,4417 e σ = 0,1710, inspeções independentes e probabilidade acumulada 1 − Π(1 − POD). Convertida para a família de potência com q normalizado entre 0,8 e 0,5, a curva equivale a γ ≈ 0,26 com p_F ≈ 0,99, isto é, subida rápida logo após P. É um cenário a incluir na grade como "antecedente próximo", não como calibração: a THC dela é uma proxy construída por PCA e não uma medida de boroscopia.

## 7. Limitações previstas

- Nenhum parâmetro tem calibração com imagens, achados ou decisões reais de boroscopia; o resultado é condicional a H_ref, W e à curva. Tamanho e tipo do dano, acesso, instrumento e operador não são representados.
- Resultado binário apenas; "inconclusivo" e "não detectável" (M14) ficam fora por decisão do autor.
- A reprovação por falso positivo (p_P > 0) gera remoção antecipada de motor saudável, que é custo indireto de restauração.
- Os motores E já foram examinados; qualquer contraste é exploratório até a confirmação em FD002/FD004, que exige o congelamento.

## 8. Verificação prevista

Testes: com p_rep ≡ 0 o híbrido reproduz o PHM; com p_rep ≡ 1 reproduz a reprovação na primeira inspeção; a reprovação nunca posterga a retirada; ordem do ciclo e fim das inspeções na decisão; expectativa exata igual à enumeração por força bruta e ao Monte Carlo. Verificador independente por laços das colunas brutas; manifestos anteriores íntegros. Nada disso será executado antes da decisão do autor sobre os pontos abaixo.

## 2.1 Janela W: o que se procurou e o que se adota

Busca em 18/10/2026 por uma referência que recomende uma janela P–F em ciclos para dano progressivo de compressor ou turbina de turbofan detectável por boroscópio: **não foi encontrada.** O que existe é qualitativo (diretiva de aeronavegabilidade da FAA de 2011 sobre trincas em revestimento de combustor que exige boroscopia antes do limite cíclico) e a orientação de que intervalos de inspeção vêm do manual do fabricante, de diretivas e do histórico de tendência do operador, que não temos. Portanto W é uma **hipótese de cenário criada e justificada**, não uma referência.

Restrições de projeto para um limite inferior útil:
- **Regra do meio-intervalo da RCM:** inspecionar a no máximo metade do intervalo P–F (atribuída a Moubray, RCM II, por fontes secundárias; não verificada em fonte primária). Com Δ = 5, W ≥ 10.
- **Intervalo P–F líquido:** a janela mínima deve cobrir o pior atraso até a inspeção e o tempo de resposta (reserva 15 + d até 2, isto é, 17): W ≥ Δ + 17 = 22.

Grade {30, 60, 80}: 30 fica logo acima do piso de 22 e próximo da antecedência mediana do marco HI = 0,5 de P07 (39,5 e 33 ciclos; que não é P); 60 é o ponto médio; 80 corresponde a cerca de 39% da vida média do FD001 (206) e 32% da do FD003 (247). Os valores 30/60/80 também aparecem em varreduras de outros documentos do grupo, mas não são referência de P–F e não foram importados como tal. O resultado é condicional a W.

## 2.2 Efeito dos parâmetros na antecedência da inspeção (apoio à decisão)

Para inspeções a cada Δ = 5 ciclos, p_P = 0, p_F = 1 e fase aleatória do calendário, a antecedência da **primeira reprovação** (ciclos antes de F) e a probabilidade de detectar com antecedência de pelo menos 17 ciclos são:

| W | γ | Antecedência média | Mediana | P(antecedência ≥ 17) | P(antecedência ≥ 30) |
|---:|---:|---:|---:|---:|---:|
| 30 | 0,26 | 23,8 | 25 | 94% | 0% |
| 30 | 1 | 16,4 | 17 | 51% | 0% |
| 30 | 2 | 10,9 | 10 | 18% | 0% |
| 60 | 0,26 | 52,6 | 54 | 100% | 100% |
| 60 | 1 | 40,0 | 41 | 99% | 85% |
| 60 | 2 | 27,8 | 28 | 84% | 43% |
| 80 | 0,26 | 72,0 | 73 | 100% | 100% |
| 80 | 1 | 56,6 | 58 | 100% | 99% |
| 80 | 2 | 40,6 | 40 | 97% | 78% |

Cálculo analítico, sem o início das inspeções no portão de 127 (motores que entram no portão já dentro da janela perdem as inspeções anteriores). Leitura: com W = 60 e γ = 1 a inspeção sozinha mandaria remover o motor, em média, cerca de 40 ciclos antes de F; as regras PHM atuais removem o motor, em média, cerca de 38 ciclos antes de F no FD001 (206,3 − 168,2). Parâmetros mais sensíveis tornam a inspeção um **cogatilho que corta a vida**; parâmetros menos sensíveis (γ alto, W curto) a deixam como **rede de segurança tardia**. A grade cobre os dois papéis.

**Proposta provisória para a decisão do autor (que declarou não saber decidir):** manchete em W = 60, γ = 1, p_P = 0, p_F = 1, com sensibilidade em W ∈ {30, 80}, γ ∈ {0,26; 2} e p_P = 0,02. A escolha do ponto central evita privilegiar um extremo; os resultados serão mostrados em toda a grade.

## 9. Decisões do autor e pendências (18/10/2026)

- **W:** sem referência encontrada; adotada a grade {30, 60, 80} com a justificativa de §2.1. Decidido.
- **CM03:** não incluir. Decidido.
- **Regra de entrada (S1 contra S2):** o autor não entendeu a pergunta. Proposta provisória: S2 (portão de 127) como política e S1 apenas como cenário idealizado de referência; sujeita a confirmação.
- **Parâmetros da curva:** o autor não sabe decidir. Proposta provisória de §2.2, sujeita a confirmação.
- **Dependência entre inspeções:** independentes, com sensibilidade de efeito latente por motor, como base.
- **Contrastes primários:** regras que têm eventos (ponto central e selecionadas).
