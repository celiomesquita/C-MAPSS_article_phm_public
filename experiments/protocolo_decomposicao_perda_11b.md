# P11.2 — decomposição da perda: detecção e decisão após detecção

**Data:** 17/10/2026. **Estado:** protocolo definido; análise não executada. Prioridade anterior à execução de P13.2. Relacionado a RQ1/RQ2/RQ3/RQ6/RQ7 do [plano executivo](../docs/gestao/plano_executivo_de_melhorias.md).

## 1. Finalidade e proveniência

Separar a perda associada ao instante em que a informação se torna utilizável daquela associada à previsão e à decisão posteriores. A comparação de P11.1 atribui 95,93–100% do ganho de vida frente à idade ao controle HI≤0,5, mas não localiza a distância entre a política e uma referência com conhecimento perfeito do endpoint. Tampouco prova que a limitação está na detecção: retirar imediatamente ao detectar pode descartar vida que um decisor ideal aproveitaria.

A ideia das três referências provém do projeto local `C:/Users/celio/Documents/GitHub/C-MAPSS_article`: [plano, seções3.1 e4.1](../../C-MAPSS_article/docs/plano_pesquisa_artigo.md), `src/planning/policies.py` e `src/analyse_planning.py`, consultados para compreender definições e conferir diferenças de contrato. Nenhum código será copiado ou importado. Este registro atribui a origem interna da ideia, sem inventar uma referência bibliográfica publicada ou transferir seus resultados para a nossa amostra.

Na outra versão, a decomposição dependeu do detector/horizonte: a seção3.1 informa que a hipótese de predominância da detecção não se sustentou para certos detectores até60 ciclos. Essa evidência impede adotar previamente a conclusão “o limite está na detecção”. A contribuição candidata é **localizar e quantificar o mecanismo limitante**, qualquer que seja o resultado.

## 2. Contrato preservado

- Mesmo índice de saúde (HI) empírico M18, modelos P10 e escolhas P13.1 congelados; FD001 principal e FD003 robustez.
- Mesmas60 partições F25/C15/U50/E10, três repetições por domínio; nenhum ajuste em U/E e nenhuma seleção nova de detector, limiar, reserva ou política. Reutilizar previsões e ações completas arquivadas.
- Prazo de execução d∈{1,2}; ultrapassagem estrita r>T continua com alvo experimental≤2% dos motores, decisão ausente e chegada exata em T reportadas separadamente e no evento composto. Não modificar o contrato para que r=T conte como retirada preventiva bem-sucedida.
- Não explorar a tolerância para escolher retrospectivamente os2% de motores que um oráculo deixaria ultrapassar T. Os oráculos são referências diagnósticas com informação privilegiada, não políticas implantáveis ou garantia de risco.
- Custo fixo idêntico por restauração perfeita, sem penalidade financeira adicional por falha. Não importar a razão de custo corretivo/preventivo da outra versão.
- Sem inspeções, novos modelos, extrapolação pós-T, projeção de20anos ou alteração do artigo nesta especificação. Repetições não são motores independentes; IDs dos dois domínios não são pares físicos.

## 3. Disponibilidade da informação

Para cada motor i e modelo externo congelado, definir:

\[
G_i=\inf\{t\geq20:H_i(t)\leq0,5\},\qquad A_i=\max(39,G_i).
\]

Se não houver passagem observada antes de T_i, ou se A_i≥T_i, a informação é indisponível antes do endpoint e não existe decisão preventiva pelo marco. Conservar memória da primeira passagem, mesmo se houver recuperação de HI. G é um evento empírico do HI supervisionado, não P físico validado. A inclui o aquecimento de atributos exigido pelas políticas comparadas.

Comparação principal: usar **o mesmo A_i** para marco0,5, ISO e RF_SLOPE, âncoras centrais/inferiores, e para as regras P13.1 que comprovadamente nunca decidem antes de A. Não impor ao oráculo a espera k nem o limiar posterior selecionado: esses são componentes da decisão a avaliar, não nova indisponibilidade de informação. Registrar separadamente qualquer política que decida antes de A; nesse caso, a comparação não é aninhada e a diferença assinada não pode ser denominada perda de prognóstico não negativa. Idade fixa permanece comparador contextual, pois sua informação está disponível desde o início.

Reportar G, A, A−G, T−G e T−A. Assim, eventual limitação de disponibilidade não será atribuída integralmente à detecção se provier do aquecimento.

## 4. Três referências sob o nosso prazo de execução

Seja ρ a antecedência desejada da **remoção** em relação a T, distinta do prazo de execução d. Contraste principal: ρ=1 ciclo, última retirada inteira estritamente anterior a T. Contrastes diagnósticos fixos: ρ=12 e15, para examinar as antecedências já discutidas pelo autor. Esses contrastes não adotam nova reserva ou novo prazo e não recalibram as políticas reais.

O prazo ideal para a decisão é D_i(ρ,d)=T_i−ρ−d. Verificar D_i≥1; se não ocorrer, registrar impossibilidade mesmo com informação inicial e tratar separadamente a restrição de início da vida. Não ocultar esses motores. Para D_i≥1:

\[
\tau_i^{O}=D_i,\qquad
\tau_i^{A}=\max(A_i,D_i),\qquad
\tau_i^{\pi}=\text{decisão real arquivada},\qquad r=\tau+d.
\]

O é o oráculo que conhece T desde o ciclo1. A é o oráculo que conhece T somente quando o mesmo sinal da política fica utilizável. Se o instante calculado não estiver antes de T, guardar ausência de decisão; não inventar ação em T ou depois dele. A regra real conserva seu gatilho, quantil, reserva e prazo, sem substituir seu preditor pelo endpoint para produzir um resultado supostamente operacional.

Para separar detecção e disponibilidade, acrescentar a referência diagnóstica \(\tau_i^{G}=\max(G_i,D_i)\), sujeita à mesma observação antes de T. Ela só serve à atribuição do atraso entre passagem do sinal e disponibilidade; não é outro detector, preditor ou política adotada.

## 5. Decomposição principal: perda de planejamento

Definir para diagnóstico \(\widetilde\tau=\tau\) quando houver decisão e \(\widetilde\tau=T\) quando não houver. Essa substituição é apenas uma convenção de pontuação, nunca uma decisão simulada. Duas métricas complementares:

\[
J(\tau)=\mathbf1\{\widetilde\tau>D_i\},\qquad
B(\tau)=\max(0,\widetilde\tau-D_i).
\]

J identifica perda da oportunidade de cumprir a antecedência-alvo ρ; B quantifica o atraso em ciclos até a decisão, limitado pelo fim da observação. Ausências são também reportadas à parte. Não confundir J para ρ=12/15 com ultrapassagem de T: perder uma antecedência desejada pode ainda permitir remoção preventiva estrita.

Para cada K∈{J,B}, por motor e depois pela média dos mesmos motores:

\[
\underbrace{K(\tau^\pi)-K(\tau^O)}_{\Delta_{\mathrm{total}}}
=\underbrace{K(\tau^A)-K(\tau^O)}_{\Delta_{\mathrm{det/disp}}}
+\underbrace{K(\tau^\pi)-K(\tau^A)}_{\Delta_{\mathrm{pós}}}.
\]

Quando \(\tau^\pi\geq A\), ambos os termos são não negativos: o primeiro mede a restrição do acesso à informação; o segundo mede o atraso adicional da previsão/política. Refinamento de atribuição:

\[
\Delta_{\mathrm{det/disp}}
=[K(\tau^G)-K(\tau^O)]+[K(\tau^A)-K(\tau^G)].
\]

Os termos refinados são passagem tardia do HI e atraso de disponibilidade. Publicar ambos e sua soma. A divisão em “detecção” e “prognóstico” pode ser usada como abreviação **somente com essas definições explícitas**. O segundo termo principal não identifica erro preditivo puro: contém calibração, reserva, espera e regra de ação. Não calcular percentuais quando a perda total for zero; reportar “sem perda a decompor”. Não truncar diferenças negativas para fabricar parcelas interpretáveis.

Para o controle que decide imediatamente em A, a parcela pós-detecção de J/B é zero por construção. Esse resultado **não** demonstra ausência de potencial para aproveitar mais vida; exige a análise de antecipação e custo abaixo.

**Implicação do resultado anterior.** P11.1 registrou retirada estritamente antes de T para todos os motores completos pelo controle r=A+d. Logo A≤T−1−d=D(1,d), e a parcela de detecção/disponibilidade de J/B para ρ=1 deve ser zero. É consequência lógica do resultado anterior, não medição nova de P11.2. Se a implementação produzir valor diferente, há divergência a investigar. Não alterar o contrato para fabricar predominância da detecção.

## 6. Vida não aproveitada e custo: decomposição complementar

Para todas as três referências e a política, manter \(N=\min(r,T)\) quando houver programação, e N=T em ausência, junto de eventos e ausência. Registrar \(W=T-N\) e a antecedência real T−r quando definida. A decomposição algébrica das médias de W também é telescópica, mas pode ter componentes assinados; identificá-los como diferenças de vida, sem forçar interpretação de perdas não negativas.

No contrasteρ=1, se A≤D, ambos os oráculos podem retirar em T−1 e W^O=W^A=1. Qualquer antecipação adicional da política pertence à etapa pós-detecção, mesmo que a política tenha ganho muito frente à idade. Se A>D, o oráculo limitado pode atingir/ultrapassar T ou ficar sem decisão: N=T não é uma vantagem econômica admissível. Não converter esse caso em suposta economia por detectar tarde.

Taxa de custo normalizada, com C_R=1: \(c_\pi=n/\sum_iN_i^\pi\), sem média das razões individuais. Nos mesmos motores e com o mesmo denominador de referência:

\[
c_\pi-c_O=(c_A-c_O)+(c_\pi-c_A),
\qquad M_\pi=\frac{c_\pi-c_O}{c_O}.
\]

Se apresentar parcelas relativas, dividir ambas por c_O; não somar percentuais com referências distintas. As identidades de custo não tornam as parcelas positivas ou admissíveis. Publicar eventos/ausências ao lado de cada taxa; declarar diagnóstico econômico condicionado quando qualquer braço não cumprir os critérios. Não acrescentar penalidade de falha para tornar a decomposição positiva.

Apresentar também o contraste pareado no subconjunto **comum** A≤D, como diagnóstico explicitamente condicionado, junto do tamanho/características dos excluídos. Nunca substituir por ele a análise principal de todos os motores nem estimar risco populacional a partir desse subconjunto selecionado pelo endpoint. Nesse subconjunto, o componente detecção é nulo por definição; sua utilidade é quantificar a antecipação remanescente após haver tempo suficiente.

## 7. Separar previsão, incerteza e política sem novo ajuste

A parcela pós-detecção será relacionada aos diagnósticos P10/P11 já disponíveis: erro assinado da vida remanescente, quantil tardio, limite inferior, reserva, primeira disponibilidade, espera e condição do gatilho. Usar os mesmos instantes arquivados e separar explicação disponível em operação de diagnóstico com T conhecido posteriormente.

Comparar as referências centrais/inferiores já existentes, sem escolher retrospectivamente a que minimize a perda. Esses contrastes mostram dependência do tratamento da incerteza, mas não identificam causalmente erro de modelo puro. Caso seja necessário separar quantitativamente modelo, quantil e regra em uma decomposição adicional, ela exigirá protocolo próprio de ablações; não será introduzida silenciosamente nesta rodada.

## 8. Comparações, incerteza e interpretação

Para cada domínio, repetição, política, d e ρ, mostrar três referências/ação real, oportunidade perdida, atraso, vida não aproveitada, custo, ultrapassagem estrita, chegada exata e ausência. Por política, O e A são os mesmos quando A/d/ρ coincidem; não apresentar cópias como novos motores independentes. Não misturar ρ distintos em uma única parcela média.

Bootstrap descritivo pareado por motor,2.000 reamostragens, semente20261017; mesma reamostragem para O/A/política e parcelas, separado por domínio/repetição. Manter100 motores por repetição, sem juntar300 como independentes. Intervalos condicionais aos modelos/políticas, não à reaprendizagem de todo o processo. Razões de parcelas serão obtidas em cada reamostragem com denominador positivo; reportar quantas tiveram denominador zero, sem substituir por zero. Sem inferência populacional automática de≤2% a partir da validação cruzada.

**Interpretação pré-fixada:**

- Detecção/disponibilidade predominante: parcela positiva maior que a pós-detecção na métrica/horizonte em questão, com magnitude e incerteza reportadas. Localizar se o responsável foi G ou aquecimento. Não generalizar para outros horizontes ou perda econômica.
- Pós-detecção predominante: havia informação em tempo, mas previsão/calibração/regra descartou vida ou perdeu oportunidade. A conclusão será investigar esses componentes, sem preservar a hipótese de predominância da detecção.
- Perda de planejamento nula e vida descartada positiva: o limitante observado é antecipação/conservadorismo na decisão, não atraso de detecção demonstrado por J/B.
- Misto/inconclusivo: parcelas dependem de domínio/horizonte, são pequenas, incertas ou afetadas por ausências/inadmissibilidade. Conservar todos os casos e evitar afirmação universal.

P11.1 permanece válido para sua comparação marginal específica; não será reescrito como prova de que o prognóstico em geral acrescenta pouco, nem de que a detecção necessariamente limita o desempenho. P11.2 poderá explicar **onde** estão as perdas segundo o nosso contrato.

## 9. Apoio da outra versão, limites e entregas

A razão de otimismo1,76–1,91 e a comparação do limite de controle HI com políticas RUL constam da seção3.1 do plano da outra versão. São registros internos de apoio à motivação da seleção separada e dos controles simples; não são novas medições nossas nem confirmação independente. Não importar penalidades, horizontes10–80, famílias de detector, níveis de risco ou código de alarme/taxa de custo. A conveniência de reutilizar código não é necessária para a contribuição.

Saída futura exclusiva: `experiments/artifacts/pilot_loss_decomposition_11b/`, com manifesto de entradas, trajetórias/eventos G/A, decisões oraculares, decisões reais herdadas, componentes por motor, estatísticas, intervalos e denominadores, casos adversos e relatório. Código será desenvolvido localmente a partir deste contrato, sem importar módulos do outro projeto.

Testes antes da execução: informação precoce/tardia/ausente; aquecimento tardio; recuperação após passagem; decisão em D e em D+1; retirada antes/em/após T; ausência pontuada sem criar decisão; não aninhamento; telescopagem de J/B/W/custo; casos de componente econômico negativo; denominador zero e pareamento por motor. Verificador separado reproduzirá referências/identidades sem chamar o gerador de oráculos e conferirá integridade dos resultados anteriores. Não ajustar U/E durante correções; preservar protocolo/versões se houver emendas.

**Próxima ação:** implementar e executar P11.2 antes de P13.2. Depois, orientar as fichas de explicabilidade pelo componente de perda identificado, mantendo os testes de fidelidade já especificados. Este documento acrescenta ideia e protocolo; nenhuma execução ou conclusão empírica nova é declarada.
