# P11 — decisão causal de remoção sem inspeção

17/10/2026. Protocolo fixado antes de executar P11, após autorização para continuar o plano. RQ1/RQ2/RQ3/RQ5. Usa resultados exploratórios já examinados; não é confirmação intocada, validação operacional ou congelamento do protocolo principal. [Plano](plano_experimentos_remocao.md).

## Congelamento e orçamento

Reutilizar exclusivamente previsões e calibrações externas P10, sem refazer HI, prognóstico ou quantis. FD001 principal e FD003 robustez, três repetições de dez dobras F25/C15/U50/E10, 100 motores completos por repetição. Os mesmos motores se repetem entre divisões; não são 300 unidades independentes. Conservar todos os motores e sementes.

Grelha primária: ISO/RF_SLOPE × previsão central/limite inferior de trajetória 98% × reserva m=15/12 × execução d=1/2, total 16 configurações. Sensibilidade fixa: limite inferior de trajetória 95%, oito configurações. Reserva 12 não é adoptada nem acionada por um critério adaptativo; o gatilho de incerteza elevada continua aberto. Acrescentar dois controles de idade fixa, com d=1 e d=2, e mesma idade física. Nenhuma inspeção.

## Regra e sequência temporal

Acompanhamento PHM a partir do primeiro HI≤0,5 com atributos causais disponíveis (ciclo ≥39). O marco não identifica P ou F. Em cada ciclo permitido, obter antecedência prevista b(t)=RUL̂(t) para âncora central, ou b(t)=max(0,RUL̂(t)−q_late) para o limite inferior; o quantil usa escore máximo temporal de U, nunca E.

Decidir na primeira ocorrência b(t)≤m+d; comprometer a retirada em r=τ+d. Depois de decidir, não adiar a data por novas previsões. A comparação usa tolerância numérica 10⁻⁹ ciclo já fixada, sem ajustar limiar aos resultados. m representa a reserva pretendida na retirada, distinta do prazo de execução d. Guardar b(τ)−d, salto abaixo do limiar e reserva real T−r para aferição. Uma atualização discreta pode deixar reserva menor que m.

Se já estiver abaixo do limiar na primeira oportunidade, decidir imediatamente e registrar insuficiência inicial, sem retroagir a decisão. Não se presume remoção instantânea: d continua valendo. O endpoint T é evento de encerramento do ambiente e somente rótulo de aferição; não é informação para antecipar a decisão. Ações preventivas só são possíveis em t<T. Se o gatilho só ocorreria em T, registrar ausência de decisão preventiva; não conceder ação no instante de falha.

Sem marco ou sem gatilho antes de T: interrupção observacional em T, evento não prevenido e falta de decisão. Essa é a contingência de simulação desta rodada, não recomendação de continuar em serviço até falha. O motor continua no denominador, com vida aproveitada N=T e custo normalizado de uma renovação; a regra não poderá ser candidata completa por ter custo menor nessa situação. Uma contingência operacional mais precoce exigirá outro ensaio pré-especificado; não importar retrospectivamente o endpoint ou a idade mínima de E para salvar resultados.

## Controle de idade fixa

Em cada dobra, usar somente os 40 motores de desenvolvimento F∪C, com vidas completas T_j, para definir A=min_j(T_j)−1 ciclo. É a maior idade inteira que antecede todos os endpoints desse desenvolvimento; com 40 motores, permitir no máximo 2% de chegadas nesse grupo equivale a zero eventos. Decidir em A−d e programar retirada em A, sem sensores e sem consultar U/E. Não aplicar novamente a reserva m a A: seria mudar o controle. Guardar IDs e mínimo utilizado antes de avaliar E.

Esse controle é conservador e tem suporte de cauda limitado; não representa o programa preventivo da companhia, garantia de risco 2% ou idade universalmente ótima. A PHM usa U50 adicional para calibração de previsão, enquanto o controle usa F∪C40 para idade; reportar a diferença de informação/orçamento. Idades externas eventualmente mais competitivas serão outro contraste, não substituição pós-hoc do controle.

## População e desfechos

Para completos, N=min(r,T) se houver decisão, ou N=T se não houver. Não creditar voo posterior a T. Registrar separadamente:

- retirada programada estritamente posterior a T (r>T), magnitude do atraso e frequência por motor;
- retirada exactamente em T (r=T), e qualquer chegada ao endpoint (r≥T ou ausência de decisão);
- ausência de marco/gatilho, decisão e execução; reserva real, vida não aproveitada max(T−r,0), insuficiência inicial;
- vida média aproveitada, custo normalizado por ciclo n/ΣN e restaurações equivalentes por 10.000 ciclos **simulados**, não por anos reais.

O alvo fornecido pelo autor é ultrapassagem estrita ≤2%; não o substituir por cobertura nominal nem por 2% dos ciclos. Como a admissibilidade de chegar exactamente a T não foi confirmada pelo autor, reportar dois filtros descritivos: (i) alvo estrito ≤2% com decisão em todos os motores; (ii) esse mesmo filtro sem retiradas exactamente em T. O segundo é triagem prudente de candidatos para estudo, não alteração silenciosa do alvo. Nenhum filtro constitui aprovação operacional. Ausência de decisão não se torna ultrapassagem programada fictícia: é falha separada e impede completude do primeiro filtro.

No teste oficial truncado, avaliar apenas decisões que ocorreriam com sensores observados. Uma retirada já comprometida pode ter data posterior ao truncamento; marcar execução não observada. O rótulo RUL permite aferir a data contra T, mas não criar sensores para futuras decisões. Sem decisão até o truncamento, status censurado; não declarar falha, ausência definitiva de marco ou custo de vida completa. Nenhum desses motores entra na taxa de renovação P11.

## Análise e interpretação prévias

Resumo por domínio, repetição e configuração: 100 completos e, como diagnóstico secundário da primeira dobra, 100 truncados. Para PHM versus controle de mesmo d, usar mesmos motores e bootstrap pareado de 2000 amostras; reportar diferenças de vida média e economia relativa 1−c_PHM/c_idade, com intervalos descritivos 95%. Não são intervalos individuais de F nem correção para seleção de um vencedor entre muitas configurações.

Apresentar todas as regras e fronteira não dominada entre ultrapassagem/eventos e vida/custo; triagem descritiva por repetição e estabilidade entre as três. Nenhuma nova busca de parâmetro, escolha da melhor semente ou exclusão dos motores difíceis FD003. Selecionar uma candidata após comparar E é exploração e não confirma o seu ótimo. Não reunir repetições como motores novos nem declarar risco populacional ≤2% por baixa contagem amostral.

Favorável: ganho de vida/custo entre regras completas com poucos eventos em ambas as extensões. Misto: benefício por domínio/divisão, grande perda de reserva ou forte dependência da âncora. Contrário: nenhuma regra atende à triagem. Inconclusivo: instabilidade/amostra insuficiente impede recomendar. Preservar todos esses resultados; não alterar a fórmula HI para corrigir uma conclusão desfavorável.

## Entrega e limites económicos

Salvar protocolo, fontes e hashes anteriores, regras, controle por dobra, decisões por motor, desfechos, resumos, contrastes, figura e verificação independente. Testes de causalidade, insuficiência, compromisso da data, diferenças r=T/r>T e censura devem passar antes de executar. O verificador reconstruirá decisões a partir das previsões congeladas e endpoints brutos, incluindo controle e estatísticas.

P11 não faz simulação AGAN de 20 anos, monetização por companhia, inspeção ou edição do artigo. P12 depende da ponte de escala, e receita/despesas dependem ainda de frota elegível, disponibilidade, procura e margem incremental. Não converter restaurações equivalentes por exposição simulada em poupança real da easyJet. A tabela de três braços continuará com inspeção não executada.
