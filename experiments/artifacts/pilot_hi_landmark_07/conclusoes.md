# Interpretação de P07 — resultado misto

## Resposta à pergunta

O marco HI=0,5 está disponível antes do endpoint nos 100 motores completos de FD001 e nos 100 de FD003 quando cada domínio usa os modelos previamente ajustados nos seus próprios dados de desenvolvimento. Para a combinação empírica, a antecedência real mediana foi 39,5 ciclos em FD001 e 33 em FD003; RMSE de previsão de F no primeiro cruzamento foi 17,8461 e 14,8387 ciclos, respectivamente. Esses números medem antecipação e erro na amostra, sem estabelecer tolerância operacional. Não são os RMSE na última observação de P05/P06.

| Cenário completo, modelo ajustado no domínio | Controle de margens: antecedência/RMSE | Empírico: antecedência/RMSE | AAKR terminal: antecedência/RMSE |
|---|---:|---:|---:|
| FD001, 100 motores por família | 40,5 / 16,87 | 39,5 / 17,85 | 56,5 / 22,16 |
| FD003, 100 motores por família | 30,0 / 25,67 | 33,0 / 14,84 | 61,0 / 26,43 |

AAKR significa regressão por kernel autoassociativa, aqui uma adaptação terminal. As primeiras passagens ocorrem em ciclos próprios de cada família. Portanto, a comparação acima não controla a informação temporal. Nos mesmos motores e num ciclo comum ao controle e à combinação empírica, a diferença de RMSE empírico menos controle foi −1,13 ciclos, intervalo descritivo de 95% [−2,74;0,43], em FD001; e −1,05 [−2,96;0,69] em FD003. A grande diferença entre RMSE próprios de FD003 não se mantém com a mesma magnitude ao sincronizar a observação. A sensibilidade a essa sincronização impede atribuir a diferença bruta apenas à qualidade da representação.

## Atualizações, disponibilidade e estabilidade

Cinco ciclos após o marco, o RMSE empírico passou de 17,85 para 17,11 em FD001 e de 14,84 para 14,31 em FD003, nos mesmos 100 motores de cada cenário. O efeito é descritivo; não há previsão de que todo motor melhore. No teste oficial truncado, só 29 motores FD001 e 22 FD003 tinham atingido o marco empírico até a última observação. Seus RMSE condicionais foram 13,46 e 15,87 ciclos. Os outros 71 e 78 motores permanecem sem marco observado; não se estende esse erro a toda a população nem se inventam sensores futuros.

Na transferência direta dos modelos FD001 para FD003, apenas 56/100 trajetórias completas atingiram 0,5 para o HI empírico e para AAKR. O RMSE empírico de 15,59 ciclos nesses 56 não permite equiparar a transferência ao reajuste com cobertura 100/100. A seleção de casos pode mascarar a perda de disponibilidade. O controle transferido alcançou 100/100, mas com RMSE 82,52 no primeiro marco.

O HI empírico voltou acima de 0,5 após a primeira passagem em 7 motores completos FD001 e 10 FD003. O mesmo ocorreu em 19/26 para o controle e 14/23 para AAKR. Não foi acrescentada persistência após observar esses resultados. Os limiares 0,4 e 0,6 estão preservados como sensibilidade, sem escolha retrospectiva de um vencedor.

## Limitação do conversor e próxima decisão

No teste oficial FD001, a RUL prevista no marco empírico teve quartis 42,87–47,62 ciclos, enquanto a RUL real teve quartis 32–48. Em FD003 reajustado, os quartis previstos foram 30,72–33,00 contra 27,75–46 reais. Essa concentração é compatível com um conversor que depende somente do HI corrente próximo de um nível fixo; não demonstra individualização suficiente da velocidade de degradação. O alvo supervisionado continua uma escala empírica, e não o HI físico de Saxena.

A evidência permite continuar a estudar o marco intermediário sem exigir coincidência exata de zero com F. Ainda não permite adotar definitivamente a fórmula, fixar remoção ou iniciar inspeções. A próxima comparação deve isolar o valor da história de degradação: manter a mesma construção de HI e confrontar o conversor corrente com previsores que recebam também sua tendência e evolução, conservando um controle direto por sensores, separação por motor e avaliação nos mesmos ciclos/coberturas. Esse novo contraste requer protocolo próprio antes do ajuste; não foi executado em P07. A fidelidade e estabilidade das contribuições dos sensores e os limites de erro/antecedência admissíveis continuam pendentes.

## Evidência e reprodução

[Protocolo](../../protocolo_marco_hi_50.md), [relatório de todas as famílias e sensibilidades](relatorio.md), [métricas](summary.csv), [comparações pareadas](paired_comparisons.csv), [verificação](verification.json) e [figura](landmark_error_lead.png). Foram verificados 5.400 registros de marco, 3.188 passagens observadas, 154.798 previsões posteriores e 144 comparações pareadas. Os manifestos P01–P06 permanecem íntegros. Os 20 testes passaram antes da execução. Não houve novo treino, mudança dos modelos originais, execução de inspeções ou alteração do artigo M17 nesta rodada.
