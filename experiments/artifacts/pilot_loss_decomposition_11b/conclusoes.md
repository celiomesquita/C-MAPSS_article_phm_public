# P11.2 — a perda remanescente está após o marco, sob a referência oracular

17/10/2026. [Protocolo anterior à execução](../../protocolo_decomposicao_perda_11b.md). HI M18, preditores, quantis e políticas congelados; mesmas60 partições externas FD001/FD003, três repetições por domínio. Nenhum ajuste em U/E, inspeção ou mudança do artigo. [Relatório](relatorio.md), [estatísticas e intervalos](summary.csv), [componentes individuais](components.csv) e [verificação independente](verification.json).

## Resultado principal

Para retirada ideal no ciclo T−1, com prazo de execução de1/2 ciclos, o oráculo informado desde o início e o informado somente após HI≤0,5 utilizável produziram **as mesmas datas em todos os motores**. A perda de oportunidade e o atraso atribuíveis à detecção/disponibilidade foram zero. O aquecimento também não restringiu nenhuma passagem observada: G=A nos600 registros motor/repetição/domínio.

O sinal ficou disponível no mínimo11 ciclos antes de T em FD001 e10 em FD003; mediana36 ciclos nos dois domínios quando descritas as observações repetidas. Esses600 registros não são600 motores independentes: cada domínio contém100 motores reutilizados em três repetições. As estatísticas inferenciais são separadas por domínio/repetição.

| Regra, intervalos entre repetições e prazos | FD001: excesso de vida descartada frente ao oráculo | FD003: excesso de vida descartada frente ao oráculo | Chegadas observadas |
|---|---|---|---|
| Marco HI≤0,5 | 36,29–38,62 ciclos | 36,04–41,22 ciclos | 0/100 em cada repetição/prazo |
| ISO/inferior98/reserva15 | 36,08–37,90 ciclos | 35,99–40,50 ciclos | 0/100 em cada repetição/prazo |
| RF temporal/inferior98/reserva15 | 35,57–38,23 ciclos | 35,80–40,73 ciclos | 0/100 em cada repetição/prazo |
| Limiar selecionado P13.1 | 21,80–24,34 ciclos | 25,67–28,32 ciclos | 0–2/100, conforme domínio/repetição/prazo |
| Espera selecionada P13.1 | 26,30–28,73 ciclos | 27,64–33,23 ciclos | 0–1/100 |

O oráculo descarta um ciclo por definição; os valores acima são o descarte adicional. A decomposição atribui esse excesso à etapa posterior ao sinal, pois ambos os oráculos têm o mesmo acesso em tempo suficiente. **Isso contraria a hipótese de que detectar tarde explique a perda principal nesse contrato.** Não significa que todo o excesso possa ser recuperado: conhecer T após o marco é uma concessão oracular, não informação disponível ao modelo real.

As âncoras centrais apresentam menor descarte, mas7–17 chegadas/100 para ISO e6–12 para RF entre os contrastes, dependendo de domínio/repetição/prazo. Menor descarte não demonstra política admissível. P13.1 também conserva as quatro escolhas internas inviáveis e as chegadas; não escolher retrospectivamente o melhor resultado.

## Antecedências diagnósticas e custo

Com antecedência desejada de12 ciclos para a remoção, a parcela de oportunidades perdidas por acesso tardio foi0–2/100 em FD001 e0–1/100 em FD003. Para15 ciclos,1–3/100 e2–3/100, respectivamente; atraso médio por acesso chegou a0,10 ciclo por motor. A parcela de aquecimento permaneceu zero. São diagnósticos de um requisito mais antecipado, não adoção de nova política/reserva ou varredura de prazo logístico.

No contraste básico, as parcelas econômicas de detecção são zero. O excesso de custo normalizado da regra ISO/inferior98/reserva15 frente ao oráculo foi21,32–22,64% em FD001 e17,12–19,69% em FD003. Esse é um afastamento de uma referência com informação perfeita, não economia realizável, valor monetário ou ganho por companhia. Os componentes econômicos dos diagnósticos12/15 continuam assinados e são publicados junto dos eventos. Não há penalidade adicional por falha para tornar a decomposição positiva.

## Interpretação e próxima decisão

P11.1 mostrou pequeno ganho do conversor **dentro das regras conservadoras comparadas**. P11.2 mostra que o sinal não chegou tarde para o requisito básico: a distância à referência ideal permanece na etapa que utiliza a informação após o marco. Essa etapa inclui qualidade/informação da representação HI, erro e incerteza preditivos, quantil, reserva e gatilho; a decomposição não identifica qual deles seria corrigível nem separa erro puro de conservadorismo.

Assim, a contribuição defensável é a localização condicionada da perda e a distinção entre ganho marginal sobre um controle simples e distância até uma referência ideal. Não se demonstrou superioridade geral, reconstrução do P físico, garantia populacional de risco≤2% ou possibilidade de recuperar todo o descarte adicional com segurança.

Próxima ação: executar P13.2 com foco nos casos em que o limite inferior/reserva aciona a retirada perto do primeiro marco apesar de ainda haver vida. Avaliar fidelidade e estabilidade da cadeia sensor→HI→previsão/incerteza→decisão. A eventual separação causal entre erro, quantil e reserva requer protocolo próprio de ablações, não ajuste retrospectivo em U/E.

## Rastreabilidade

69 testes aprovados antes da execução. Reproduzidas9.600 decisões; gerados600 registros de disponibilidade,10.800 referências oraculares não duplicadas por política,28.800 decomposições,19.200 diagnósticos preditivos e576 resumos, incluindo o escopo condicionado A≤D. Bootstrap pareado de2.000 amostras por domínio/repetição, com os mesmos índices para todos os braços e parcelas.

O primeiro acionamento do verificador ocorreu antes de o runner terminar de escrever as tabelas e falhou por ausência de `metadata.json`; log preservado como `verification_premature.log`. Aguardar a conclusão e repetir a checagem não alterou código, dados, protocolo ou resultados. O resultado final consta de `verification.json`. O código foi desenvolvido neste projeto, sem importar/copiar a implementação do projeto vizinho. Modelos e artefatos anteriores permanecem íntegros.
