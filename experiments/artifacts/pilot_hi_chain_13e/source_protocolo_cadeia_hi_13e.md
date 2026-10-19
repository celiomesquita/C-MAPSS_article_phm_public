# P13.5 — transferência decisória das indicações de HI de P13.4

Especificado antes da execução em 17/10/2026, após autorização do autor para executar o próximo passo do plano. Estudo exploratório de RQ1/RQ2/RQ6/RQ7. Não substitui M18, não congela o protocolo principal, não confirma risco populacional e não adopta política operacional.

## Pergunta

As 60 indicações internas de P13.4 (SEL), quando acompanhadas de conversores reaprendidos e calibração refeita pelos procedimentos inalterados de P10/P11, alteram marco, erro e cobertura do prognóstico, decisões de remoção e estabilidade entre repetições nos motores E10, frente à cadeia M18?

## Cadeias comparadas

- **M18:** reconstrução da cadeia P10. HI M18 ajustado em F25, ISO e RF_SLOPE em C15, quantis em U50. Antes de qualquer análise, a reconstrução deve reproduzir os modelos, previsões completas E10 e quantis arquivados de P10 (tolerância absoluta 10⁻⁹ ciclo nas previsões, igualdade dos quantis). Falha interrompe a rodada sem análise.
- **SEL:** HI indicado e congelado em P13.4 para cada partição, já ajustado em F25 (`selected_hi_*.joblib`), aplicado como HI=clip(1−x·w,0,1) aos sensores centrados (média causal de 15 ciclos e referência no ciclo 20), com w os pesos efetivos salvos. Conversores ISO e RF_SLOPE reaprendidos em C15 com hiperparâmetros, pesos iguais por motor e semente de repetição de P10. Quantis recalculados em U50 com a mesma estatística de ordem corrigida, escopo trajetória e erro tardio.
- Quando a indicação é M18 (2 partições FD001 e 3 FD003), SEL é por definição idêntica à cadeia M18; a equivalência dos pesos (tolerância 10⁻⁸) será verificada, sem gerar cópia numérica paralela. Isso inclui a contingência inelegível FD003/repetição 2/dobra 2, marcada como `contingency_ineligible`.

Nenhuma nova escolha de variante, hiperparâmetro, limiar, reserva ou nível ocorre em C, U ou E. C já participou da escolha de P13.4: os conversores SEL ajustados em C herdam essa dependência, e C não é avaliação independente. U é usado somente para calibrar, E somente para avaliar.

## Dados e separação

As 60 partições P10 (F25/C15/U50/E10; três repetições, dez dobras, FD001 e FD003). Somente `train_FD001.txt` e `train_FD003.txt`; alvos T−t. Os testes oficiais truncados e os arquivos RUL não são lidos: já foram examinados e não acrescentariam confirmação. Cada motor pertence a E exatamente uma vez por repetição; a unidade de análise é o motor. As três repetições reutilizam os mesmos 100 motores por domínio e não são agrupadas como 300 motores independentes. E já foi examinado em P10–P13.2; esta avaliação é exploratória.

## Regras de remoção

Regras fixas, idênticas nas duas cadeias, com tolerância numérica 10⁻⁹ ciclo de P10/P11:

- P11 primárias com reserva 15: ISO e RF_SLOPE × âncora central (POINT) ou limite inferior 98% (LOWER98) × prazo d=1/2 (oito regras). Decisão no primeiro ciclo utilizável com max(0, RUL̂−q)≤15+d; retirada em decisão+d.
- Controle de condição P11.1: retirada no primeiro ciclo utilizável max(39, primeiro HI≤0,5) mais d (duas regras).
- Somente ciclos t<T são observados. Ausência de decisão é chegada ao endpoint sem decisão; não é excluída nem convertida em data tardia. Reserva 12, nível 95% e as regras selecionadas em P13.1 ficam fora: foram fixadas para M18 e transferi-las ao novo HI exigiria nova seleção.

## Medidas predefinidas

1. **Estabilidade entre repetições (primária para a pergunta de transferência).** Para cada motor E e cadeia, amplitude (máximo−mínimo) entre as três repetições do marco utilizável e das datas de decisão de ISO_LOWER98_M15_D1/D2 e HI_MARKER_D1/D2. Motores sem valor finito em alguma repetição são contados à parte, nunca tratados como amplitude zero. Relatar mediana, p95, máximo e número de motores com amplitude >10 ciclos, e diferença pareada SEL−M18 por motor com bootstrap de 2.000 reamostragens dos motores (semente 20261017).
2. **Decisões por domínio e repetição.** Decisões, ausências, chegadas exatas, ultrapassagens estritas, chegadas compostas, vida média aproveitada min(r,T), vida não utilizada T−min(r,T), distância ao oráculo ρ=1 de P11.2 (W−1) e atraso relativo ao prazo do oráculo. Triagem experimental: decisão em todos os motores e ultrapassagem estrita ≤2%; isso não certifica risco.
3. **Prognóstico.** Disponibilidade do marco, RMSE e viés no marco, cobertura inferior da trajetória a 98%, q_late, n de calibração, antecedência conservadora mediana no marco e fração de colapso.
4. **Contrastes pareados SEL−M18** por domínio e repetição nos motores comuns: diferença da vida média aproveitada para cada regra e diferença do RMSE no marco por método; intervalos bootstrap descritivos, não testes confirmatórios.

## Caudas, contingência e casos

- As 11 partições com máximo interno agravado em P13.4 (`max_tail_worsened`) serão relatadas separadamente: distribuição e máximo de |Δ marco| e |Δ decisão| entre cadeias nos seus motores E.
- Para todos os motores, relatar o maior |Δ marco| e |Δ decisão| entre cadeias por domínio e repetição.
- Agregados incluem as 60 partições tais como congeladas; a contingência inelegível entra com diferença nula por construção e é listada. Não é substituída retrospectivamente.
- FD003 motor 55 e FD001 motor 83 serão descritos em todas as repetições. Foram identificados usando E em P13.2/P13.3; sua descrição não valida a alternativa.

## Interpretação predefinida

- **Transferência favorável:** em ambos os domínios, p95 da amplitude do marco entre repetições não aumenta, e para ISO_LOWER98_M15 em d=1/2 SEL não tem mais ausências, chegadas exatas ou ultrapassagens que M18 em nenhuma repetição.
- **Mista:** melhora em parte dessas medidas acompanhada de piora em outra, perda relevante de vida, cobertura ou antecedência, ou dependência de domínio.
- **Nula/contrária:** sem melhora da estabilidade externa ou com mais eventos de endpoint.

Qualquer resultado mantém M18 como referência até decisão explícita do autor. Não haverá redução de reserva, projeção monetária, inspeção ou alteração do artigo. Não expandir alternativas, grade ou regras depois de observar os resultados.

## Verificação e artefatos

Testes antes da execução: reprodução da cadeia M18 numa partição contra P10; equivalência da HI por pesos efetivos com o caminho P10 para M18; separação F/C/U/E e proveniência de cada indicação; decisões M18 iguais às arquivadas em P11 e P11.1; distância ao oráculo igual à de P11.2; amplitude com valor ausente não convertida em zero; ausência de leitura de arquivos test/RUL.

Verificador independente após a execução: recomputar HI e marcos a partir dos dados brutos por outro caminho (estatísticas por motor de P13.4), refazer previsões a partir dos modelos salvos, quantis a partir dos escores U, decisões, amplitudes, resumos e contrastes, e comparar a cadeia M18 com P10/P11/P11.1/P11.2 arquivados. Manifestos anteriores devem permanecer íntegros.

Salvar fontes, hashes dos insumos, modelos, quantis, previsões E/U, decisões, medidas, verificação e relatório em `artifacts/pilot_hi_chain_13e`.
