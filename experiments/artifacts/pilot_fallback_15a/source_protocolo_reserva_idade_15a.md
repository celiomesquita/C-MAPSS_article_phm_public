# P15.1 — política candidata de reserva: regra PHM quando houver decisão e regra de idade quando não houver

Especificado em 18/10/2026 antes da execução, por decisão do autor após a leitura do IP 180 (tarefa clássica permanece disponível e há retorno a ela quando o monitoramento não decide) e da tese de Miranda (retorno à tarefa tradicional quando o PHM opera com dados ausentes; se o intervalo tradicional já passou, exige análise de engenharia). Exploratório, RQ1/RQ3/RQ5. A política é **candidata**: não é política final, não concede crédito de manutenção e não valida segurança. Sem inspeção. Não congela o protocolo principal.

## Definição

Para cada motor, a remoção ocorre na primeira das duas ações causais:
- a decisão PHM de uma regra congelada de P13.1 (data de decisão d_PHM, retirada em d_PHM + d), se existir antes de T;
- a regra de idade, que retira o motor na idade A_q (decisão em A_q − d, como no controle AGE de P11), se A_q − d < T.

Então d_h = min(d_PHM, A_q − d) e retirada em d_h + d. Empate: prevalece o PHM. Se nenhuma das duas existir antes de T, permanece a chegada ao endpoint sem decisão, nunca excluída. A regra de idade só atua se o PHM ainda não decidiu quando a idade é atingida; portanto, só usa informação disponível até esse ciclo.

**Consequência estrutural, prevista antes de executar.** O controle de idade de P11 (A = mínimo dos endpoints de F∪C − 1; 127–146 ciclos) é conservador; nas partições conhecidas, cerca de 83% das decisões de ISO inferior 98% ocorrem depois dessa idade (FD001, repetição 1). Com A_0 a política tende a se aproximar da regra de idade em grande parte dos motores. Isso é resultado, não falha, e motiva a grade abaixo.

## Idade de reserva

A_q = ⌊quantil_q(endpoints de F∪C)⌋ − 1, calculado somente nos motores de desenvolvimento da partição (F25 ∪ C15, `fit` e `converter` de `splits.json`), nunca em U ou E. q ∈ {0 (idêntico ao controle AGE de P11), 0,05, 0,10, 0,25, 0,50}. A grade é fixa e declarada antes dos resultados; todos os valores são relatados, nenhum é selecionado, e nenhum é adotado como política. "Dados indisponíveis ou fora do domínio" não ocorrem em C-MAPSS e não são simulados.

## Regras base e dados

Regras PHM de P13.1 (fonte `pilot_policy_selection_13a/decisions.csv`, 100 motores completos por domínio e repetição; repetições separadas, sem somar como 300 motores): ISO_LOWER98_M15, RF_SLOPE_LOWER98_M15, ISO_POINT_M15, RF_SLOPE_POINT_M15, HI_MARKER, HI_THRESHOLD_SELECTED, HI_WAIT_SELECTED; prazos d = 1 e 2. 7 regras × 2 prazos × 5 idades = 70 regras híbridas; mais as 14 originais e os controles AGE_D1/2. Somente train FD001/FD003; sem testes oficiais, RUL, FD002 ou FD004. Nenhum modelo, quantil, reserva ou regra de P13.1 é alterado.

## Medidas

Por domínio, repetição e regra: decisões, ausências, chegadas exatas, ultrapassagens estritas, vida média aproveitada, taxa de restauração por ciclo simulado, **fração de motores em que a regra de idade atuou**, vida cedida frente à regra PHM original (ciclos e %), economia de restauração frente ao controle de idade e frente ao marco HI, e telas de P11 (estrita: decisão em todos e ultrapassagem ≤2%; prudente: também sem chegada exata). Economia: 1 − taxa_híbrida/taxa_referência, com bootstrap de motores (2.000 reamostragens, semente 20261018), pareado. Cenário central de 20 anos (P12.2: L_ref=8.425, 1.600 voos/ano, LLP sem e 20.000, frota madura, ρ=1; mais L_ref=5.000 e 12.000): visitas por posição, com o simulador de P12.2.

## Interpretação prévia

- A política é útil no sentido operacional descrito pelo IP 180 se eliminar ausências de decisão e chegadas ao endpoint das regras PHM sem perder a maior parte da vida aproveitada. A perda de vida é o preço e deve ser relatada ao lado dos eventos.
- Se A_0 reduz a política à regra de idade na maior parte dos motores, o resultado é que a idade conservadora domina; não se aumenta q até obter o resultado desejado.
- A existência de zero eventos em 100 motores reutilizados não prova risco ≤2%. A regra de idade também tem chegadas ao endpoint (motores curtos, T ≤ A + d), que a política herda.
- O comportamento quando o intervalo tradicional já passou (idade excedida antes de o PHM falhar) é tratado aqui como retirada na idade, o que equivale à regra de idade; a tese indica que na prática exigiria análise de engenharia, que não é simulada.

## Verificação e artefatos

Testes antes da execução: o controle AGE de P13.1 corresponde à definição (decisão A − d se < T); com idade infinita o híbrido reproduz exatamente as linhas originais; o híbrido não decide depois de nenhum dos dois componentes; híbrido de AGE com AGE é AGE; A_q usa somente F∪C; A_q não decresce com q; ausência de leitura de test/RUL/FD002/FD004. Verificador independente reconstrói decisões, status, taxas e economias por laços das colunas brutas, refaz A_q a partir de `splits.json` e dos arquivos train, e confere manifestos anteriores. Saídas em `artifacts/pilot_fallback_15a`.
