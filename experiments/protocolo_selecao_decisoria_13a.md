# P13.1 — seleção interna de regras simples e avaliação externa

17/10/2026, antes da execução. Autorização para continuar após P11.1. RQ1/RQ2/RQ3/RQ7. Hipótese motivada pelos resultados anteriores: pode existir vantagem em escolher o limiar/espera da decisão sem acrescentar modelos preditivos. A fórmula HI de M18 não muda. P13 permanece mais amplo: esta rodada não completa sua avaliação de explicabilidade ou validação operacional.

## Isolamento de ajuste, seleção e avaliação

Conservar as 60 partições externas P10: FD001 principal/FD003 robustez, três sementes e dez dobras, F25/C15/U50/E10. A seleção de novas regras usa somente D=F∪C, 40 motores; U e E não entram na escolha. Não criar um grupo S fictício nem usar E para escolher o limiar que será avaliado no mesmo E.

Dentro de cada D40, quatro blocos internos V10. Permutar IDs de D com semente seed+10000·fold; para cada bloco v, permutar os 30 restantes com semente seed+10000·fold+100·v e usar 25 para aprender HI, deixando cinco sem uso naquele ajuste. Assim o HI interno tem o mesmo orçamento F25 do externo. Cada um dos 40 motores é previsto uma vez sem pertencer ao ajuste que o prevê; modelos internos compartilham treino, portanto os erros não são independentes por isso. Reaprender apenas parâmetros da mesma forma HI, com convenções FD001/FD003 fixas; nenhum conversor é necessário para selecionar regras que só usam HI.

Total: 240 ajustes HI internos e 40 previsões fora de ajuste por dobra externa. Avaliar todos os candidatos nesses 40 motores e congelar escolhas antes de ler as decisões externas de referência ou aplicar os modelos externos. No segundo estágio, aplicar as escolhas ao HI do modelo P10 externo congelado; não treinar com E, não retocar a fórmula e não alterar quantis U. Refazer parâmetros somente nos ajustes internos é necessário para evitar seleção com HI que já viu o endpoint do mesmo motor.

## Candidatos fixados

- Família de limiar: h∈{0,2;0,3;0,4;0,5;0,6;0,7;0,8}; decidir no primeiro evento HI≤h utilizável, com disponibilidade ≥39, e retirar d=1/2 ciclos depois. Conservar memória de evento a partir de HI disponível no ciclo20; recuperação posterior não desfaz a passagem.
- Família de espera: k∈{0;1;2;5;10} ciclos após o primeiro marco HI≤0,5 utilizável; decidir somente ao completar a espera e retirar d ciclos depois. Se a vida terminar antes da decisão, não inventar programação ou voo pós-endpoint. k é espera deliberada da regra, não redução ou extensão do prazo de execução d.

Selecionar separadamente por família e prazo d. Não comparar os dois d como se um prazo logístico mais longo fosse livre escolha económica. Não selecionar entre ISO/RF ou mudar as reservas do autor: essas regras ficam referências fixas. Limiar/espera são parâmetros da decisão exploratória, não nova formulação do HI, novo P/F físico ou adoção de uma política operacional.

## Critério interno e limite de amostra

Exigir decisão em todos os 40 motores e frequência composta de chegada ao endpoint ≤2%, incluindo r=T, r>T e ausência. Esse filtro interno é deliberadamente mais prudente que o alvo do autor de ultrapassagem estrita ≤2%; os dois não serão confundidos. Com n=40, esse filtro admite zero eventos observados; não demonstra risco populacional 2% nem confiança de 98%.

Entre candidatos que passam, maximizar ΣN/40, equivalente a minimizar custo fixo normalizado 40/ΣN. Empates favorecem limiar maior ou espera menor. Se nenhum passar, registrar seleção sem candidato viável; conservar para diagnóstico a alternativa com menos eventos, depois mais vida e desempate prudente, sem classificá-la como admissível. Não ocultar famílias/dobras inviáveis. A grelha não será expandida depois de ver E.

Não calcular um quantil corrigido de 98% com V10 ou D40: isso daria limite não finito. As regras selecionadas são validadas externamente, sem alegar garantia conformal do risco da política. U50 permanece exclusivamente a calibração preditiva P10 das referências fixas, sem ser consumido para selecionar as novas regras.

## Comparação externa

Em E10 de cada dobra, avaliar limiar selecionado, espera selecionada e seis referências fixas de mesmo d: idade P11, marco0,5 P11.1, ISO/central/reserva15, RF/central/reserva15, ISO/inferior98/reserva15, RF/inferior98/reserva15. Oito estratégias por prazo, 16 por motor, total9.600 registros completos. Nenhum teste oficial truncado adicional nesta rodada.

As referências são herdadas sem modificação. Reconstruir o HI externo dos sensores com o modelo P10 congelado e verificar igualdade com as previsões arquivadas para ciclos≥39; isso permite avaliar limiares diferentes sem preencher sensores ou escalas futuras. O próprio HI continua supervisionado por RUL de desenvolvimento. A regra não recebe o endpoint do motor avaliado; o ambiente termina a observação em T, sem ação preventiva em T, como P11.

Por motor e repetição: limiar/espera escolhido, decisão, data programada, vida aproveitada N=min(r,T), vida não aproveitada, ultrapassagem estrita, chegada exacta, ausência de decisão e evento composto. Contagens e custos incluem todos os motores. Para ausências, N=T e evento composto, sem premiar essa exposição por ganho económico admissível.

Reportar 100 motores externos por domínio/repetição, não 300 motores independentes. Mostrar distribuição das escolhas e diferença entre filtro interno e resultado externo. Bootstrap pareado de 2000 amostras, semente20261017, separado por repetição, para diferenças de vida e economia normalizada frente ao marco e ao ISO/inferior98/reserva15; condicionais às seleções/modelos congelados, não reaprendizagem de todo o procedimento. Os 60 modelos externos são de validação cruzada e o conjunto já informou decisões anteriores: não é confirmação intocada de uma frota nova.

## Interpretação e entrega

Favorável: escolha interna acrescenta vida e preserva eventos baixos externamente. Mista: filtro interno zero não se mantém fora da amostra, escolhas instáveis ou ganhos restritos. Contrária: vida maior depende de eventos não prevenidos. Inconclusiva: resolução de cauda e dependência entre divisões impedem recomendação. Não trocar limiar, semente ou reserva após resultados para obter zero eventos.

Preservar protocolo, modelos HI internos, partições, trajetórias HI fora de ajuste, decisões/score de todos os candidatos, escolhas congeladas, decisões externas, resumos, contrastes e hashes. Verificador separado refaz parâmetros/trajectórias internas, escolhas, comparação de HI externo e estatísticas. Testes antes de executar devem cobrir separação por motor, causalidade, memória/espera, seleção sem eventos, desempate e falta de candidato viável.

Não há boroscopia, projeção monetária, mudança da fórmula HI, novo modelo de prognóstico, adoção da reserva12 ou redução automática de incerteza. O ponto ótimo continua condicionado à classe de regras, dados e critérios, sem validação de margens físicas. P12 permanece dependente da ponte de escala para20anos e dos parâmetros empresariais.
