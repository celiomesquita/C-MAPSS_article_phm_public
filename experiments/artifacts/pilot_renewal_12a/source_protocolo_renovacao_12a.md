# P12.1 — renovação AGAN por exposição simulada e horizonte parametrizado

Especificado em 18/10/2026 antes da execução, após autorização do autor para prosseguir com o plano (M24/M25). Exploratório, RQ3. Estágio sem inspeção (o braço híbrido segue adiado até o congelamento), sem projeção calendário validada e sem valor financeiro de companhia. Não congela o protocolo principal.

## Pergunta

Para as 16 regras congeladas de P13.1 (selecionadas e de referência, incluindo os controles de idade e de marco HI), quantas restaurações AGAN, que custo acumulado e que eventos de endpoint resultam quando as vidas são renovadas por reposição de motores E sobre uma exposição comum? A taxa analítica (restaurações por ciclo simulado) é reproduzida por simulação de renovação? Como os resultados dependem do efeito de borda quando o horizonte é curto?

## Ponte de escala: não decidida

O autor ainda não definiu a correspondência entre ciclos simulados do C-MAPSS e ciclos de voo. Este protocolo **não escolhe** essa ponte. Os resultados primários são **por exposição simulada**, sem calendário. O horizonte de 20 anos (M21; cenário de 1.600 ciclos de voo/ano, 32.000 em 20 anos) entra apenas como parâmetro aritmético: H = 32.000/k ciclos simulados, com k ∈ {1, 10, 50, 100, 150} ciclos de voo por ciclo simulado, valores de grade sem recomendação nem justificativa física. Com k=1 (hipótese direta), a vida média de ~170–210 ciclos implica cerca de 150–190 restaurações por posição em 20 anos, número que serve para explicitar a necessidade da ponte e não é previsão. Não se reescalam o intervalo de cinco ciclos, os prazos 1–2 nem as reservas de 15/12.

## Dados e entradas

- `pilot_policy_selection_13a/decisions.csv` (fase `selected` e `reference`; 16 regras; 100 motores completos E por domínio e repetição). Uma vida = motor de E com `utilised` = min(data de retirada, endpoint) se há decisão, ou endpoint se não há. Eventos: ausência de decisão, chegada exata ao endpoint, ultrapassagem estrita, conforme `status`.
- Somente train FD001/FD003 (via artefatos). Sem testes oficiais, arquivos RUL, FD002 ou FD004. Nenhuma regra, modelo ou quantil é alterado.
- Unidade de inferência: motor. As três repetições reutilizam os mesmos 100 motores e permanecem separadas; não somar como 300.

## Contabilidade

- Custo fixo por restauração perfeita (AGAN): 1 unidade normalizada; em USD, 6 milhões (M21), com sensibilidade linear 5/7 milhões. Sem custos complementares. Boroscopia inexistente nesta etapa.
- Posição de motor com restauração inicial comum não contada. Cada vida termina em restauração; contar somente restaurações em t ≤ H. A vida incompleta no fim do horizonte é registrada como exposição residual, sem cobrança.
- **Taxa analítica** por regra/domínio/repetição: n/Σ utilised (restaurações por ciclo simulado). Contrastes pareados entre regras sobre os mesmos 100 motores com bootstrap de motores (2.000 reamostragens, semente 20261018).
- **Simulação de renovação**: R=2.000 réplicas por domínio/repetição/H; em cada réplica, sequência de índices de motores sorteados com reposição (semente por domínio/repetição/H, idêntica para todas as regras: mesmas sequências de motores entre políticas). Cada regra consome a sequência até exceder H. Trajetórias intactas; nenhum sensor fragmentado.
- Medidas por regra e H: restaurações por posição (média e desvio das réplicas), custo acumulado, ciclos aproveitados (min(H, soma das vidas completas) e residual), eventos de endpoint por posição (contagem esperada de chegadas/ausências e de ultrapassagens estritas) e razão eventos/vidas. Diferenças pareadas das regras frente a idade (AGE) e frente ao marco HI (HI_MARKER), por réplica, com média e percentis 2,5/97,5 das réplicas, interpretados como variabilidade do processo para os 100 motores, não incerteza de população.
- **Validação do simulador.** Com H_val = 1.000.000 ciclos simulados e R=2.000, restaurações por ciclo simuladas devem coincidir com a taxa analítica em ±1% relativo para cada regra. Falha interrompe o relato do horizonte curto; não se aumenta R para forçar concordância.
- **Efeito de borda.** Para cada H, relatar a razão (restaurações simuladas/H)/(taxa analítica); onde a vida média é comparável a H, a razão é arredondamento de inteiros, não evidência de efeito da regra.

## Interpretação predefinida

- O custo normalizado é só frequência de restauração; menor custo não classifica admissibilidade. Cada tabela mostra eventos de endpoint e ausências na mesma linha.
- Economia frente a idade e frente ao marco HI é relatada como diferença de restaurações e de custo acumulado, com variabilidade das réplicas e, na taxa analítica, o intervalo bootstrap dos motores. Sem valor financeiro de companhia, sem receita, disponibilidade ou margem.
- Escolher uma regra vencedora global é proibido; as 16 regras são cenários avaliados. As quatro escolhas internas inviáveis de P13.1 permanecem como diagnósticos.
- Resultado favorável à validação do simulador não valida custo real, frequência real de revisão ou a ponte de escala.

## Verificação e artefatos

Testes antes da execução: caso construído de renovação (contagem de restaurações e residual), mesmas sequências entre regras, motores ausentes de decisão com vida igual ao endpoint, ausência de leitura de arquivos test/RUL/FD002/FD004, concordância simulação×taxa analítica num caso sintético longo. Verificador independente: reconstrói vidas e taxas analíticas dos CSV brutos, repete a simulação com implementação em laços e as mesmas sequências para um subconjunto de réplicas (identidade exata), refaz o bootstrap com semente própria igual e confere manifestos anteriores. Saídas em `artifacts/pilot_renewal_12a`: fontes, hashes, tabelas por regra/H, contrastes, figura de restaurações versus H, validação, verificação e `conclusoes.md`.

## Pendências (autor)

Ponte ciclos simulados→ciclos de voo; frota elegível, procura, disponibilidade efetiva, margem incremental, moeda e ano-base para M22; parâmetros do braço de inspeção. Nenhuma foi assumida aqui.
