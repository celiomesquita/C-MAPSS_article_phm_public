# P11 — interpretação das regras de remoção, 17/10/2026

**A âncora central, com as reservas testadas, não produziu uma regra completa de prevenção. O limite inferior de trajetória antecipou as decisões e evitou chegadas ao endpoint nesta amostra, mas ainda não demonstrou um momento ótimo de remoção.** Mantêm-se HI empírico e isotônico como referências. Não se adoptaram reserva 12, nível 95%, política final ou operação além do endpoint.

## Desenho executado e resultado primário

Reutilizaram-se previsões/calibrações P10, sem novo ajuste. Dez dobras em três repetições por domínio, mesmos 100 motores completos em cada repetição. Dezesseis configurações primárias, oito sensibilidades 95% e dois controles de idade fixa; estes aprendem A=min(T de F∪C40)−1 antes de avaliar E. Programação r=τ+d na primeira antecedência prevista ≤m+d; execução d=1/2 e reserva m=15/12, sem escolha adaptativa. Todas as decisões preventivas ocorrem antes de T; depois dele, nenhum sensor foi criado.

| Indicador, amplitudes entre repetições e configurações | FD001 | FD003 |
|---|---|---|
| Ausências de decisão com âncora central, por 100 motores | 4–20 | 5–23 |
| Ultrapassagens programadas com âncora central, por 100 | 0–6 | 0–4 |
| Limite inferior 98%: ausências/chegadas/ultrapassagens | 0/0/0 em todas as oito regras primárias | 0/0/0 em todas as oito regras primárias |
| Controle de idade: chegadas ao endpoint, por 100 | 1–3 | 1–2 |
| Controle de idade: vida média aproveitada, ciclos | 130,12–134,72 | 145,24–148,61 |
| ISO, limite inferior 98%, reserva 15, d=1/2: vida média aproveitada | 167,41–169,23 | 205,70–210,21 |
| Mesmo ISO: vida média não aproveitada | 37,08–38,90 | 36,99–41,50 |

As amplitudes não representam intervalos de confiança sobre 300 motores. A referência nominal 98% é calibração preditiva; zero eventos observado em uma comparação exploratória não comprova risco populacional ≤2%. A idade fixa variou 127–146 em FD001 e 144–155 em FD003; é um controle conservador e não a prática da companhia citada para utilização/custos.

## Interpretação da ausência e da ultrapassagem

Se não há gatilho antes do endpoint, a simulação encerra a vida em T e registra falha não prevenida. O motor permanece na exposição/custo, mas a regra não passa a triagem de completude. Isso evita premiar ausência de retirada como aproveitamento economicamente superior. Não se confunde falta de decisão com uma data programada tardia inexistente.

Com d=1 e τ<T, uma retirada programada após T é impossível por construção, pois r=τ+1≤T. Portanto, a taxa estrita r>T isoladamente seria enganadora; os eventos r=T e sem decisão são essenciais. Com d=2, o máximo atraso programado observado foi um ciclo, sem operação pós-T. Esses fatos não indicam voo seguro ou autorização de ultrapassagem de margem física.

## Economia normalizada, ainda sem projeção empresarial

Para o isotônico com limite inferior 98% e reserva 15, o custo normalizado n/ΣN foi **20,05–23,11% menor em FD001** e **28,95–30,47% menor em FD003** que o controle de idade de mesmo d. Os intervalos descritivos pareados de 95% dessas diferenças favoreceram a PHM nos 12 contrastes, seis por domínio, separados por prazo e repetição. Trata-se de aumento de vida aproveitada frente a esse controle específico.

O controle também apresentou falhas e não passou a triagem de completude. Logo, a comparação não é entre políticas com admissibilidade equivalente e não comprova superioridade perante programas preventivos reais. As percentagens são de custo por ciclo simulado, não poupança monetária em 20 anos, resultado financeiro da easyJet ou ganho do braço com inspeção. Não foram multiplicadas por USD 6 milhões ou por uma frota empresarial.

## Limitação decisória: concentração no primeiro marco

Com reserva 15, o ISO decidiu já no primeiro marco disponível em 55–86% dos motores FD001 e 72–100% dos FD003; a RF temporal em 84–89% e 86–93%, considerando os dois prazos. A reserva prevista no marco já estava abaixo de m+d em muitos desses casos, embora a reserva real retrospectiva fosse frequentemente ampla. Não retroagimos a ação nem reduzimos o prazo de execução.

Essa concentração exige um controle adicional antes de atribuir o benefício à previsão sequencial: retirar no primeiro HI≤0,5 mais d, sem conversão para F ou correção de incerteza. A comparação deverá manter os mesmos motores e verificar quanta vida o prognóstico de facto acrescenta para o mesmo perfil de eventos. É uma hipótese motivada por P11, ainda não executada; não uma análise pré-especificada no protocolo original. O controle de idade também merece contraste mais forte antes da alegação de vantagem económica geral.

Todas as sensibilidades 95% também tiveram decisão completa e zero chegadas nesta amostra, com diferenças de vida aproveitada. Isso não autoriza escolher retrospectivamente 95% ou 12 ciclos nem demonstra redução da incerteza. Nenhum vencedor foi confirmado e a RF temporal não substitui automaticamente o isotônico.

## Verificação e próximos passos

Os 43 testes passaram antes da execução. O verificador independente reconstruiu 31.200 registros de decisão completos/truncados, 60 controles, 312 resumos, 144 contrastes pareados e 108 linhas de fronteira. Todos os artefatos P01–P10 permaneceram íntegros. Uma correção somente no verificador tratou motores truncados sem atributos após aquecimento; também corrigiu o separador Windows no mapeamento de arquivo original. Código/logs anteriores foram preservados; decisões, protocolo e resultados não mudaram.

Próximo contraste prioritário: controle de retirada no primeiro marco para avaliar o valor incremental do prognóstico, mantendo protocolo anterior à nova análise. P12 permanece pendente da ponte entre ciclos simulados e voo/calendário, e o ganho por companhia depende também de frota, procura, disponibilidade e margem incremental. Inspeções continuam posteriores ao congelamento; artigo permanece M17.

Evidências: [protocolo](../../protocolo_remocao_11.md), [relatório](relatorio.md), [decisões](decisions.csv), [verificação](verification.json), [contrastes](contrasts.csv), [controle por dobra](controls.json), [correção do verificador](verifier_correction.json) e [manifesto](manifest.json).
