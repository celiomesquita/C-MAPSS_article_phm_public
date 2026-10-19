# P14.1 — concentração da instabilidade e dos eventos adversos por vida do motor

Especificado em 18/10/2026, antes da execução, após autorização do autor da sequência M24. Diagnóstico exploratório, sem novo ajuste, ligado a RQ1/RQ5/RQ7. Não reabre a comparação de HI, não escolhe valor de limite de vida, não congela o protocolo principal e não confirma risco.

## Pergunta

A instabilidade entre repetições do marco HI≤0,5 e das decisões de remoção da cadeia M18 concentra-se nos motores de vida mais longa? Se sim, um limite de vida para remoção obrigatória (remoção em min(decisão PHM, limite)) tem motivação empírica além do realismo operacional. Se não, essa premissa fica motivada apenas pela prática operacional.

## Transparência prévia

Antes de redigir este protocolo, foram vistos: (a) as vidas de FD003 motores 55 (525 ciclos, máximo do subconjunto) e 10 (481), e de FD001 motor 83 (293, acima do p95 de 287); (b) uma contagem exploratória, por motor, dos eventos de endpoint em P11, P13.1 e P13.5, que sugeriu concentração desses eventos em motores de vida curta (por exemplo FD003 motor 99, 145 ciclos; FD001 motor 91, 135 ciclos), à excepção do motor 10 em P13.5. Por isso, a análise dos eventos é descritiva e não entra no critério de interpretação.

## Dados e separação

- Somente artefatos já arquivados: amplitudes da cadeia M18 em `pilot_hi_chain_13e/ranges.csv` (100 motores por domínio; três repetições) e decisões completas de `pilot_removal_11`, `pilot_policy_selection_13a` e `pilot_hi_chain_13e`.
- Vida T de cada motor lida em `train_FD001.txt` e `train_FD003.txt`. Nenhum arquivo test, RUL, FD002 ou FD004 é lido: FD002/FD004 ficam reservados, intocados, para a confirmação prevista em M24.
- Unidade de análise: motor. Repetições não são observações independentes.
- A cadeia SEL de P13.5 não entra nas medidas de estabilidade (arquivada por M23); seus eventos entram apenas na tabela descritiva, rotulados.

## Medidas predefinidas

Para cada domínio e cada quantidade M18 (`usable_marker`, `ISO_LOWER98_M15_D1/D2`, `HI_MARKER_D1/D2`), com amplitude finita:

1. **Correlação de postos** de Spearman entre T e amplitude absoluta, com intervalo bootstrap percentil 95% (2.000 reamostragens de motores, semente 20261018). Motores sem amplitude finita são contados à parte, não convertidos em zero.
2. **Enriquecimento na cauda longa.** Cauda longa: T ≥ quantil 0,90 de T no domínio (regra fixada pela distribuição de vida, não pela instabilidade). Entre os motores com amplitude >10 ciclos, relatar contagem e fração na cauda longa e o enriquecimento = fração / fração populacional da cauda. Relatar também a fração da amplitude excedente Σmax(amplitude−10, 0) atribuída à cauda longa.
3. **Amplitude relativa** amplitude/T: Spearman com T e intervalo bootstrap. Distingue instabilidade que cresce mais do que proporcionalmente com a vida de instabilidade apenas proporcional.
4. **Leitura observável.** Spearman entre a amplitude e o menor marco utilizável entre as repetições (idade observável no momento do sinal), com intervalo bootstrap. Um limite de vida atua pela idade, não por T.
5. **Eventos adversos (descritivo).** Para P11 (todas as regras), P13.1 (regras selecionadas) e P13.5 (M18 e SEL separadas): contagem de linhas com ausência de decisão, chegada exata, ultrapassagem estrita ou chegada ao endpoint, por terço de T do domínio (cortes nos quantis 1/3 e 2/3) e por motor, com T e posição de T.

## Interpretação predefinida

Aplicada à quantidade primária `usable_marker`; as demais quantidades são relatadas como consistência.

- **Concentração sustentada:** nos dois domínios, limite inferior do intervalo de Spearman(T, amplitude) >0 **e** enriquecimento ≥2 entre os motores com amplitude >10 ciclos.
- **Parcial:** apenas um domínio cumpre, ou apenas um dos dois requisitos.
- **Não sustentada:** nenhum domínio cumpre os dois requisitos.

Com 5–29 motores acima de 10 ciclos por domínio, as frações são instáveis; contagens serão sempre relatadas junto das razões. A amplitude relativa e a leitura observável qualificam, mas não alteram, a classificação.

## Consequência

- Sustentada ou parcial: especificar P14.2 (premissa de limite de vida), com valor do limite fixado antes de qualquer avaliação, a partir de fonte operacional ou de regra sobre as vidas dos motores de desenvolvimento, nunca escolhido pela estabilidade observada em E; o limite aplica-se igualmente aos braços idade fixa, PHM e PHM + inspeção. Motores não são excluídos: os que atingem o limite contam como remoções por limite de vida.
- Não sustentada: o limite de vida pode ser mantido apenas como realismo operacional, sem alegação de estabilização.
- Em qualquer caso, M18 permanece; nenhuma reserva, nível ou regra muda; eventos em motores curtos, se confirmados pela medida 5, são registrados como risco distinto que um limite de vida não trata.

## Verificação e artefatos

Testes antes da execução: leitura restrita a train FD001/FD003; amplitude ausente não convertida em zero; cálculo do enriquecimento e da amplitude excedente num exemplo construído; reprodutibilidade do bootstrap com a semente; classificação de eventos idêntica às colunas arquivadas.

Verificador independente: obtém T pelas colunas `endpoint` arquivadas (não pelos arquivos train), recalcula amplitudes a partir de `decisions.csv` de P13.5 e marcos por repetição, e refaz correlações (implementação de postos própria), enriquecimentos, frações e tabelas de eventos. Manifestos anteriores devem permanecer íntegros.

Saídas em `artifacts/pilot_long_life_14a`: fontes, hashes dos insumos, tabelas, figura amplitude×T, verificação, manifesto e `conclusoes.md`.
