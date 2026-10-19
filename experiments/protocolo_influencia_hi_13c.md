# P13.3 — influência dos motores e identificabilidade do HI

Especificado em 17/10/2026 antes da execução. Diagnóstico exploratório motivado por P13.2, ligado a RQ6/RQ7 e M18; não é confirmação independente ou procura de nova fórmula.

## Pergunta e hipóteses concorrentes

A instabilidade do marco HI≤0,5 decorre de sensibilidade a motores individuais de F, do reaprendizado das direções/escalas/canais, ou de combinações de sensores pouco identificáveis? Uma matriz correlacionada, isoladamente, não prova não identificabilidade sob restrição não negativa. Ausência de influência individual também não exclui efeito conjunto da composição de F.

## Desenho fixado

1. Reutilizar os 60 ajustes P10 e as partições F25/C15/U50/E10. Ler somente `train_FD001.txt` e `train_FD003.txt`. Rótulos de ajuste: T−t exclusivamente em F. Não ler testes oficiais ou arquivos RUL. M18, conversores, quantis, reservas e políticas operacionais permanecem inalterados.
2. Reconstruir os 600 marcos externos antes de escolher casos diagnósticos. Em cada domínio, selecionar o motor com maior amplitude finita do marco entre as três repetições (desempate pelo menor identificador). Relatar ausências separadamente; não substituir ausências por T. Essa seleção usa E já explorado somente para localizar casos adversos; não autoriza escolher ou validar um modelo em E.
3. Nos 60 F25, calcular os valores singulares da matriz padronizada ponderada por motor, a condição espectral, a condição nas colunas com coeficiente>1e−8, e a condição após acrescentar a penalização ridge M18. Espectro é diagnóstico local da geometria do ajuste, não prova física ou unicidade global.
4. Para os dois casos e suas três partições externas, excluir cada um dos 25 motores F, produzindo 150 exclusões e dois ajustes por exclusão: (a) reaprender somente os coeficientes, mantendo estatísticas F25; (b) reaprender canais, direções, escalas e coeficientes em F24. O primeiro é uma ablação, não um ajuste totalmente independente do motor excluído. Ambos mantêm tau/gamma/ridge M18. Não ajustar conversores ou regras.
5. Avaliar todos os dez motores E de cada uma dessas seis partições. Conservar marcos ausentes, diferenças pareadas finitas, erro de HI e distância entre pesos efetivos β·direção/escala no espaço dos 21 sensores. Para cada exclusão, comparar a perda quadrática não saturada e penalização no MESMO F24, com pesos iguais por motor, para o ajuste basal e para cada variante. Diferenças de penalização entre escalas não são objetivos comuns: comparar o objetivo apenas dentro da variante de estatísticas fixas.
6. Medir separadamente alteração do HI e alteração do primeiro cruzamento; mostrar curvas dos dois casos e a distribuição das exclusões. Não calcular novos índices de risco de remoção com conversores/calibração incompatíveis com o HI reaprendido. Não adoptar uma exclusão, regularização ou variante pelos resultados.

## Evidências e interpretação prévia

Reconstrução basal e identidade dos pesos efetivos são condições de validade. Se pequenas alterações de F moverem muito o marco, há sensibilidade de aprendizagem; se isso ocorrer sobretudo na variante completa, o pré-processamento aprendido participa. Se pesos variarem muito com perda e HI pouco alterados, a importância individual dos sensores é pouco determinada nessa amostra; não afirmar impossibilidade matemática sem prova adicional. Se somente o cruzamento variar muito, examinar proximidade/patamar no limiar. Resultados nulos, mistos e ausências serão preservados.

Unidade: motor original; exclusões e repetições são cenários dependentes. Relatar distribuições descritivas por domínio/repetição, sem testes de população, intervalos artificiais com 300 motores ou alegação de risco≤2%. Nenhum novo parâmetro será escolhido em U/E. Salvar fontes, protocolo, hashes, resultados, verificação e limitações em `artifacts/pilot_hi_influence_13c`. O próximo passo será decidido com base no diagnóstico, sem iniciar inspeções ou monetização.
