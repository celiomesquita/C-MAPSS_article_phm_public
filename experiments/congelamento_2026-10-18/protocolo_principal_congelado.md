# Protocolo principal congelado

**Congelado em 18/10/2026** por decisão do autor ("Pode usar a data de hoje"), depois da aprovação do estado do protocolo e do artigo e da revisão de consistência do manuscrito (M43 e M44). Deriva do rascunho v0 com as decisões M37 a M42. Os hashes das fontes, dos insumos, dos manifestos dos pilotos, do manuscrito e do ambiente estão em `manifest_hashes.json` desta pasta, e o hash do próprio manifesto, em `manifest_hashes.sha256`. Este arquivo é somente leitura. Mudanças só pela seção 13.

## 1. Objetivo e alegações

Determinar o ciclo de remoção de motores turbofan que reduza o custo de restauração por ciclo, dentro de um domínio de segurança e antecedência definido pelo autor, gerando tarefas alternativas com PHM somente por sensores e com PHM + inspeção boroscópica. **Permitido afirmar:** desempenho exploratório condicional às hipóteses, com eventos adversos relatados. **Proibido afirmar:** crédito de manutenção, conformidade com IP-180, AC 120-113 ou ARP7122, risco populacional ≤2%, equivalência física do HI com Saxena, ganho financeiro de companhia.

## 2. Dados e separação

- **Desenvolvimento:** `train_FD001.txt` e `train_FD003.txt` (100 motores completos cada). Os testes oficiais já foram examinados e não servem de confirmação.
- **Confirmação:** FD002 e FD004 (`train_*` até a falha), **intocados** até o congelamento; abertos uma única vez. Não calcular, ler ou graficar antes. Os 509 motores de treino são a amostra de confirmação do limite de 127 ciclos e da política; o teste oficial truncado deles não é usado.
- **Unidade de inferência:** o motor. Repetições de partições sobre os mesmos motores nunca são somadas como motores independentes.
- **Partições de desenvolvimento:** F25/C15/U50/E10 de P10 (três repetições, dez dobras por domínio), com ajuste do HI, dos conversores e da seleção somente em F, C e D (D = F ∪ C), calibração somente em U, avaliação somente em E. Nenhuma escolha em U ou E.

## 3. Pré-processamento e HI (M18, M23)

Média causal de 15 ciclos, referência de cada motor no ciclo 20, HI definido a partir do ciclo 20, canais retidos e direções aprendidos em F, combinação empírica de sensores com pesos não negativos regularizados, parâmetros reaprendidos por domínio e por partição (protocolos P05 e P06). Instabilidades de orientação, de coeficientes e do marco entre repetições (P13.2 a P13.5) são limitações declaradas, sem nova busca de fórmula (M23).

## 4. Prognóstico e incerteza

- Marco de previsão: primeira passagem do HI por 0,5 com pelo menos 39 ciclos de histórico, tratado como entrada observável do prognóstico, não como P nem como gatilho (P07, contrato).
- Conversor HI → RUL isotônico (referência) e RF com inclinação (controle), ajustados em C; previsão de F como t + RUL prevista.
- Margem unilateral conforme de 98%, estatística de ordem corrigida com um escore por motor (máximo do erro após o marco), calibrada só em U50; sensibilidade 95% (P09 e P10).

## 5. Política de remoção (M31, M32)

- **Limite sem monitoramento:** 127 ciclos, valor único para todos os conjuntos (M30), fixado antes de abrir FD002 e FD004.
- **Com monitoramento válido,** o PHM governa sem teto. Decisão no primeiro ciclo após o marco em que [RUL prevista − margem]₊ ≤ reserva + prazo de execução, com reserva 15 (12 apenas como sensibilidade) e prazo 1 ou 2; retirada na decisão + prazo (P11).
- **Perda de monitoramento (M32, M39):** inválido no ciclo de verificação (127 − prazo): remoção em 127; perda detectada depois: pedido imediato e retirada em t + prazo. **Modelo de perda de dados congelado como cenário declarado (M39):** probabilidade u de monitoramento inválido por ciclo, independente entre ciclos, com a grade de sensibilidade {0; 0,0005; 0,001; 0,002; 0,005; 0,01; 0,02; 1} de P16.1, sem calibração (C-MAPSS não a permite) e sem valor de manchete; resultados condicionais a esse modelo. Dado inválido não detectado, interrupções correlacionadas e indisponibilidade antes do portão ficam fora do escopo e são declarados como limitações.
- **Conjunto de regras (M38, decisão do autor em 18/10/2026): fixado e declarado, sem seleção de vencedora.** Principais: ISO e RF com inclinação, limite inferior 98% e reserva 15 (prazos 1 e 2), e o controle pelo marco HI. Contraste do braço de inspeção: as regras de ponto central ISO e RF com inclinação, que têm eventos. Todas são relatadas; a pergunta é o que cada regra custa em vida e em eventos, não qual vence. O limiar e a espera selecionados de P13.1 ficam fora do conjunto principal.
- **Eventos:** ausência de decisão, chegada exata e ultrapassagem estrita ficam sempre separadas e nunca excluídas; a meta de ultrapassagem estrita de até 2% por motor é experimental, não autorização.

## 6. Braço de inspeção (P17.1, M33, M34)

A reprovação só antecipa a decisão (min entre a decisão do PHM e a primeira reprovação) e a aprovação nunca a posterga; a inspeção não sustenta a operação sem PHM. Gerador: p_rep = p_P + (p_F − p_P)·q^γ, com q pela vida restante verdadeira sobre uma janela W do ambiente (grade {30, 60, 80} ciclos); entrada S2 no ciclo 127 com inspeções a cada 5 ciclos; manchete W = 60, γ = 1, p_P = 0, p_F = 1, com sensibilidade em toda a grade, em γ = 0,26 e 2, e em p_P = 0,02. Contrastes primários em regras que têm eventos. Inspeção sem PHM (CM03) não incluída. Custo e duração incrementais zero; contar inspeções e reprovações.

## 7. Economia (M21, M26, P12)

Restauração AGAN com custo fixo de USD 6 milhões (sensibilidade 5 e 7); custo por ciclo simulado como resultado principal e cenário de 20 anos condicionado a k = L_ref/T̄ (L_ref de 4.000 a 19.000 ciclos de voo, calibrado em intervalos de remoção por EGT/desempenho), a 1.400, 1.600 e 1.900 ciclos de voo por ano, com LLP independente em 20.000, 25.000 e 30.000 ciclos e restauração parcial ρ = 0,8 como sensibilidade. Sem número máximo de restaurações; aposentadoria do motor não modelada. Receita, disponibilidade, frota, demanda e margem de companhia dependem de parâmetros não definidos e **estão excluídos do resultado principal (M40, decisão do autor em 18/10/2026)**: o resultado financeiro se restringe a restaurações por ciclo simulado e visitas por posição em 20 anos, com custo fixo de USD 6 milhões por restauração; receita e disponibilidade ficam como extensão condicional não executada, e a receita média por voo da easyJet é apenas um benchmark, não uma contribuição marginal.

## 8. Comparações e métricas

Três braços pareados nos mesmos motores, previsões e sequências de vida: idade fixa de 127 ciclos, PHM somente por sensores e PHM + inspeção. Por motor: decisão, retirada, vida aproveitada, ciclos não usados, eventos separados, inspeções, reprovações e antecipação. Agregados: restaurações por ciclo simulado, economia frente à idade e ao marco HI, intervalos bootstrap de motores (2.000 reamostragens), sem interpretar como população. Relatar todas as repetições, os casos extremos (por exemplo FD003 motor 55) e as seleções inviáveis.

## 9. Explicabilidade

Contribuições assinadas dos sensores ao HI, sensibilidade preditiva e efeito sobre a ação, com réplicas globais e locais (P13.2); concordância entre dobras como estabilidade, não fidelidade; sem alegação de causalidade física.

## 10. Confirmação em FD002 e FD004 (uso único)

Com o congelamento já feito, executar o pipeline completo uma vez em cada conjunto, sem ajuste: (a) contagem de motores com T ≤ 127 sobre os 509 motores de treino; (b) desempenho das regras do conjunto declarado (M38) com partições do mesmo tipo (HI, conversor e margem reaprendidos por domínio, normalização de P18.1); (c) relato integral dos resultados adversos. Uma ocorrência T ≤ 127 não altera o limite e é relatada. O resultado é confirmação sob mudança de domínio (seis condições operacionais), não replicação na mesma população.

**Critério de sucesso (adotado pelo autor em 18/10/2026, M42): limite de idade com regra estatística fixada antes de abrir os dados.** O limite de 127 ciclos é considerado compatível com o alvo experimental de 2% se o limite superior de Clopper-Pearson unilateral de 95% para P(T ≤ 127) sobre os 509 motores de treino de FD002 e FD004 for ≤ 2%. Isso admite até 4 motores com T ≤ 127 em 509 (nenhum dá 0,59%; um, 0,93%; quatro, 1,79%; cinco, 2,05%, que reprova). Relatar também a mistura de 709 motores (zero ocorrências dá 0,42%; até 7 ocorrências mantêm o limite ≤ 2%). Reprovar o critério não altera o limite durante a confirmação; é um resultado a relatar. O critério não é garantia de risco populacional nem autorização operacional.

O desempenho das regras é relatado integralmente, sem limiar de sucesso: restaurações por ciclo simulado, economia frente ao limite de 127 e ao marco HI com bootstrap de motores, eventos separados com limites de Clopper-Pearson, antecedência e extensão acima de 127. A verificação de direção do sinal proposta antes (M41) não foi adotada.

## 11. Pendências do rascunho: todas resolvidas

1. Normalização por condição operacional: aprovada (M37), procedimento de P18.1.
2. Regras PHM: conjunto fixo e declarado, sem seleção de vencedora (M38).
3. Modelo de perda de dados: cenário declarado, sem calibração (M39).
4. Parâmetros de companhia: excluídos do resultado principal (M40).
5. Atualização completa do manuscrito antes do congelamento (M41) e correções de consistência (M44).
6. Critério de sucesso da confirmação: limite de idade com regra estatística fixada antes de abrir os dados (M42).
7. Data de congelamento: 18/10/2026.

Fora do congelamento, ainda abertos: verificação bibliográfica de `AC2003`, `AC2019`, `Lei2018` e `Miranda2026`; periódico-alvo; implementação do código de confirmação.

## 12. Verificação e rastreabilidade

Cada experimento do protocolo terá testes antes da execução, verificador independente por reconstrução, preservação dos logs de falha, manifestos de hashes, e proibição de leitura de testes oficiais, arquivos RUL de conjuntos já examinados e FD002/FD004 fora da etapa 10.

## 13. Regras após o congelamento e emendas

1. **Abertura de FD002 e FD004.** Os arquivos `train_FD002.txt` e `train_FD004.txt` só podem ser lidos, calculados ou graficados em um único script de confirmação escrito sob este protocolo. Antes da abertura: o script deve existir, passar nos testes em FD001, FD003 e no conjunto sintético, ter verificador independente, e ter o hash registrado em uma emenda de pré-abertura neste arquivo de emendas. A conferência de hash dos arquivos (sem ler o conteúdo como dados) é permitida.
2. **Uso único.** A confirmação é executada uma vez por conjunto. Falhas de execução anteriores a qualquer leitura dos dados de resultado podem ser repetidas; uma repetição depois de ver resultados é um desvio e precisa ser relatada.
3. **Emendas.** Qualquer mudança de regras, parâmetros, critérios, normalização, conjuntos ou métricas é registrada em `emendas.md` desta pasta, com data, motivo, itens afetados e se FD002 e FD004 já foram abertos. Emendas feitas depois da abertura são desvios e entram no artigo.
4. **Resultados adversos.** Todos são preservados e relatados, inclusive ocorrências T ≤ 127 e inversões de sinal; nenhum motivo justifica ajustar o procedimento depois de ver resultados.
5. **Manuscrito.** O texto do artigo pode ser editado, mas não pode afirmar além do que este protocolo e os resultados sustentam. O hash do manuscrito no congelamento está no manifesto.
6. **Estado do código.** O código do pipeline de confirmação com normalização por regime ainda não foi implementado; só o módulo `regime_normalisation.py`, os pilotos e os verificadores existem e estão registrados no manifesto.

