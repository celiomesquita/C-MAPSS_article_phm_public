# P06 — interpretação e decisão

A avaliação em FD003 distinguiu transferência direta dos modelos FD001 de reajuste da mesma formulação em FD003. No teste oficial, o RMSE da fórmula empírica passou de 79,56 para 23,40 ciclos; a adaptação AAKR passou de 80,25 para 26,41, e o controle de margens de 38,58 para 32,41. Os intervalos descritivos pareados dessas mudanças excluíram zero. O resultado sustenta dependência dos parâmetros/conversor em relação ao domínio, sem isolar qual componente produz o ganho do reajuste.

Após reajuste em FD003, a fórmula empírica teve RMSE 23,40 contra 32,41 do controle; a diferença foi −9,00 ciclos, com intervalo descritivo [−14,11;−3,63]. A adaptação AAKR teve RMSE 26,41 e diferença −6,00 [−10,97;−0,89]. A comparação refere-se a estas implementações e ao teste FD003; não constitui superioridade universal ou reprodução integral do estudo publicado.

A ancoragem terminal ainda não foi resolvida. Nos motores completos avaliados fora do ajuste, o HI empírico chegou a zero em 46/100, com antecipação mediana de cinco ciclos entre passagens; 54 não chegaram a zero, HI terminal mediano 0,0163 e nenhuma recuperação depois do primeiro zero. A AAKR chegou a zero em 82/100, com antecipação mediana 18 e 52 recuperações. No teste truncado, a fórmula empírica reajustada não zerou em nenhum motor, mas isso não prova ancoragem em F: os sensores terminais não estão disponíveis ali.

A distribuição de vidas também muda: a mediana completa é 199 ciclos em FD001 e 220,5 em FD003, e o máximo passa de 362 para 525. Não atribuir a perda de transferência apenas ao segundo mecanismo. Os arquivos usados não fornecem classificação independente de qual mecanismo domina cada motor. O exemplo do motor FD003 2 mostra que uma representação transferida pode continuar com HI alto até o endpoint; a heterogeneidade dos padrões de sensores merece investigação específica.

P06 fortalece o uso da fórmula empírica como candidata recalibrável, mas não justifica adotá-la como HI físico ou identificar seu primeiro zero com F. O próximo contraste deve distinguir deslocamento da representação de condição de deslocamento do conversor HI→RUL, examinando os motores com condição terminal mal representada. FD003 agora foi avaliado e deve ser tratado como dado já examinado em futuras adaptações. Inspeções continuam adiadas.

O [relatório](relatorio.md) reúne tabelas e limitações; a [figura](HI_transfer_refit.png) usa motores 1/2/3 fixados previamente. Verificações estão em verification.json; modelos, métricas individuais e seleções permanecem arquivados.
