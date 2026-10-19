# P11.1 — valor incremental do prognóstico frente ao marco HI≤0,5

17/10/2026, definido antes da execução desta análise. Autorização: prosseguir com o controle proposto após P11. Questões RQ1/RQ3/RQ7; motivação posterior aos resultados P11. Esta rodada é exploratória, não confirmação independente, nova escolha de HI ou congelamento do protocolo principal.

## Pergunta e controle

P11 concentrou muitas ações no primeiro marco. Verificar quanto da vida/custo frente à idade fixa se deve ao HI e quanto é acrescentado pelas regras que usam previsão de F e incerteza. Não presumir benefício do componente mais complexo.

Usar o mesmo HI supervisionado congelado P10, motores externos completos FD001/FD003, três repetições e dez dobras. É um controle sem conversor prognóstico na decisão, não um HI não supervisionado. A decisão é τ_H=t₀, retirada r_H=t₀+d, para d=1/2. t₀ é o primeiro instante utilizável após o evento causal HI≤0,5, com a mesma disponibilidade ≥39 da comparação P11. Se o evento ocorreu antes de 39, a memória do evento só permite agir a partir de 39; não dar ao controle uma vantagem de aquecimento diferente. Regressões do HI acima de 0,5 não apagam o evento. O marco não identifica P nem F.

A ação usa exclusivamente ciclo e sinal de evento/disponibilidade derivado do HI. Não usa RUL prevista, quantil, margem de 15/12 ou endpoint. Os dois conversores P10 compartilham o mesmo HI; verificar igualdade do sinal nas duas cópias e criar um único controle por d. Decisões só podem ocorrer antes do endpoint de encerramento. Não retroagir, não adiar depois da decisão e não actuar em T. Ausência nos completos permanece evento não prevenido e no denominador; no teste truncado, permanece censura, sem vida completa fictícia.

## Comparações fixadas

Reutilizar todas as decisões P11 sem recalcular ou escolher regras. Comparar as 24 regras PHM por domínio/repetição ao controle HI de mesmo d: 16 primárias e oito sensibilidades95, sem adoptar 12 ou 95%. Comparar também HI versus idade fixa do mesmo d. A idade continua A=min(T_F∪C40)−1, com os eventos externos já observados; não substituí-la após ver o resultado. Nenhum ajuste de modelo, parâmetro, partição ou referência de condição.

Para completos, registrar igualdade de datas, retirada posterior ao marco, ausência de decisão do candidato, ganho individual e médio de vida aproveitada N, custo normalizado n/ΣN e diferença de eventos. Usar 2000 reamostragens pareadas por motor, semente 20261017, para intervalos descritivos 95% das diferenças de vida e custo, por repetição. Sem agregação como 300 motores independentes ou correção para seleção de vencedor. A regra PHM não pode decidir antes do controle que tem a mesma disponibilidade; testar essa invariância, sem equiparar vida maior à admissibilidade.

Decompor o ganho médio de vida frente à idade fixa como

\[
\bar N_P-\bar N_A=(\bar N_H-\bar N_A)+(\bar N_P-\bar N_H).
\]

Reportar a parcela incremental do prognóstico quando o ganho total for positivo; é uma decomposição descritiva neste desenho. Não somar percentuais de economia: os fatores de custo obedecem c_P/c_A=(c_P/c_H)(c_H/c_A). Um controle de idade incompleto ou sujeito a eventos não representa comparação de admissibilidade equivalente ou prática real de companhia.

Para truncados, mostrar disponibilidade da decisão e execução observável; não comparar taxas de renovação ou inventar decisões depois do truncamento. Rótulos RUL só entram na aferição. Não excluir os motores difíceis ou alterar o marco 0,5 para favorecer o prognóstico.

## Interpretação anterior à análise

- Favorável ao prognóstico: vida adicional frente ao controle HI com eventos equivalentes nesta amostra e efeito consistente; não basta superar idade fixa.
- Nula ou pequena: resultado semelhante ao HI, com maior complexidade e informação; atribuir a maior parcela do ganho ao marco, sem exigir superioridade do prognóstico.
- Mista: benefício restrito a regra, domínio ou divisão; qualificar o alcance e distinguir efeito pontual de estabilidade.
- Contrária: vida aparentemente maior depende de falhas não prevenidas ou chega ao endpoint; não premiar essa vantagem económica.

Não fixar após os resultados um limiar para “relevância prática” nem confundir intervalo que exclui zero com ganho operacional suficiente. Os filtros exploratórios e desfechos de P11 continuam iguais. Inspeções, projeção financeira de 20 anos, investigação de outro HI e edição do artigo estão fora desta execução.

## Artefatos e verificação

Preservar P01–P11 por hashes. Registrar antes da execução protocolo, scripts, testes e fontes. Arquivar controles por motor, resumo conjunto com P11, contrastes, decomposição, figura, metadados e manifesto. Verificador separado deve reconstruir t₀ pelas previsões P10 e compará-lo ao marcador de HI, checar decisões, censura, desfechos, resumos e diferenças/intervalos. Nenhum resultado P11 será reescrito; atualizar somente o estado vigente do plano e adicionar o registro técnico da nova análise.
