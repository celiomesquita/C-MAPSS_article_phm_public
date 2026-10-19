# P02 — refinar detecção e margem, sem inspeção

Rodada exploratória autorizada em 16/10/2026. Protocolo escrito antes da execução. P01 e seus artefactos permanecem intactos. Não é congelamento do protocolo principal.

## Perguntas e desenho

1. A calibração do máximo desvio persistente na fase inicial reduz disparos precoces frente a dois desvios fixos?
2. Quanto da antecipação excessiva decorre de aplicar margem fora da região de decisão, e quanto da escolha dos resíduos usados para estimar essa margem?

Somente as 100 trajectórias completas de `train_FD001.txt`. Mesmos cinco folds externos agrupados de P01, para comparação exploratória pareada; estes motores já foram examinados em P01 e não são teste confirmatório intocado. Dentro de cada fold: 40 motores de ajuste, 20 de calibração, 20 de selecção e 20 de avaliação. Motor inteiro em uma única partição. O teste oficial continua intocado.

## Detector

Manter média móvel causal 15, referência própria inicial 20, dois sensores e persistência de três ciclos. Reutilizar as escalas de P01 estimadas somente em motores de ajuste. Registrar como limitação a curta referência e a correlação temporal.

Converter os desvios absolutos normalizados em um escore: segundo maior desvio por ciclo, seguido do mínimo nos três ciclos consecutivos. O primeiro cruzamento persistente é o ciclo de alerta disponível, sem retroagir P.

Para calibrar o limiar, assumir provisoriamente que ciclos 21–40 também pertencem ao período inicial estável nos motores de ajuste. Calcular um máximo de escore por motor nesse intervalo e os quantis 0,90/0,95/1,00 desses máximos; o limiar é o maior entre dois e o quantil. **Esta estabilidade inicial é hipótese de cenário, não rótulo confirmado de ausência de degradação.** Nenhum ciclo futuro do motor avaliado entra nessa calibração.

Nos 20 motores de selecção, comparar dois desvios fixos com esses três candidatos. Escolher lexicograficamente: cumprir taxa de alertas até 40 ≤ 10%; dentre os que cumprem, maior cobertura de detecção antes de F e maior antecedência mediana; desempate por menor limiar. Sem candidato que cumpra, minimizar a taxa precoce e registrar inviabilidade do critério. O nível 10% é tolerância exploratória de disparo inicial, não requisito de safety. Guardar todas as alternativas e sua selecção. Na avaliação externa, aplicar limiar e sensores congelados.

Sem verdade independente de P, não inferir acurácia de detecção, falsos positivos confirmados ou aumento do P–F físico. Comparar cobertura e antecedência, e avaliar sensibilidade à hipótese inicial antes do congelamento futuro.

## Prognóstico e margens

Quatro regressores e atributos de P01, mesmos parâmetros iniciais, sem busca adicional; ajustar só nos 40 motores de ajuste pós-P. Igual peso total por motor. Guardar previsões dos motores de calibração, selecção e avaliação, para rastreabilidade.

Comparar quatro políticas com gatilho fixo de RUL ajustada ≤ 10 ciclos, acção imediata apenas como cenário exploratório:

- `raw`: sem margem.
- `global`: quantil 0,9 do máximo erro positivo por motor de calibração, em toda a história pós-P.
- `global_gate30`: mesma margem global, mas só actuar se a RUL original também for ≤ 30. Esse controlo isola o efeito de restringir a região de acção.
- `local_gate30`: mesmo gatilho/região de acção, mas margem estimada somente em pontos de calibração cuja **previsão original** seja ≤ 30. Um máximo por motor elegível e quantil 0,9. Não seleccionar pontos pela RUL verdadeira. Registrar quantidade elegível; se menos de 10 motores, indisponibilizar essa variante.

Os números 10/30 são parâmetros exploratórios fixados antes desta rodada, não antecedência logística ou intervalo de inspecção. As margens não fornecem cobertura garantida e não serão chamadas de RUL segura. Sem disparo, registrar chegada ao endpoint. A ausência de previsão por falta de detecção também deve contar nos desfechos.

Escolher variante por modelo somente nos 20 motores de selecção: minimizar primeiro a quantidade que chega ao endpoint, depois a vida média não utilizada. Na avaliação externa, guardar resultados de todas as variantes e marcar a previamente escolhida. Esse critério serve à selecção exploratória, não demonstra admissibilidade operacional. Não escolher modelo vencedor com a avaliação externa.

## Evidência e limites

Reportar resultados por motor, configuração e fold, predições, margens e decisões de selecção. Chegada ao endpoint não é acidente. Diferenças de P01 para P02 combinam detector e menor tamanho de treino; não atribuir toda diferença ao detector. Contrastes entre as quatro políticas de P02 usam exactamente as mesmas previsões.

HI físico, detecção de F por margens físicas, AGAN empírico e explicabilidade continuam sem validação. Não executar inspeção ou gerar achados nesta rodada. Antes de congelar o protocolo principal, especificar o braço futuro de inspeção e os critérios operacionais; ausência observada de falhas não é critério suficiente de congelamento.

Reproduzir: `py experiments/pilot_fd001_02.py`. Saídas em `artifacts/pilot_fd001_02/`, sem sobrescrever P01. O código importado de P01 também terá hash registrado.
