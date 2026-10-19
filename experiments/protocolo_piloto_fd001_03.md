# P03 — robustez de P e diagnóstico de uma proxy HI/F

Rodada exploratória autorizada pelo autor. Protocolo escrito antes da execução. Preservar P01/P02. Não introduzir inspeções ou congelar o protocolo principal.

## Perguntas e controles

Variar o fim do período assumido estável B0 ∈ {30,40,50}, a janela causal do detector w ∈ {5,10,15} e a persistência d ∈ {3,5}. Total: 18 configurações. A referência própria inicial permanece B=20, com dois canais para alerta. O período inicial estável é hipótese, não verdade independente de P.

Usar os mesmos cinco folds e grupos 40/20/20/20 de P02. Dentro de cada configuração, escolher limiar em motores de selecção segundo a regra P02, substituindo 40 por B0; ajustar quantis 0,90/0,95/1 dos máximos iniciais nos motores de ajuste. Não escolher uma configuração vencedora com resultados externos. Reportar tanto alertas até B0 quanto até um horizonte comum de 40 ciclos, para não confundir mudança do horizonte com mudança de desempenho.

## Isolar detecção de prognóstico

Treinar os quatro regressores de P02 uma vez por fold usando todas as observações causalmente disponíveis a partir do ciclo 21, sem filtrar pelo P candidato. Atributos com janela 15 e sensores seleccionados nos motores de ajuste. Previsões e margens ficam idênticas para as 18 configurações dentro de cada modelo/fold. O detector define apenas quando as previsões passam a poder gerar remoção. Assim, diferenças entre configurações são efeitos do calendário de acesso à mesma previsão, não de retreino.

Essa mudança de conjunto de treino impede atribuir diferenças P02/P03 somente ao detector. A referência para contrastes controlados está dentro de P03. Guardar todas as previsões, divisões, limiares e decisões.

Comparar as políticas sem margem e com margem local na região de RUL prevista ≤30, ambas com gatilho ≤10 e acção imediata. Calibrar a margem local uma única vez por modelo/fold, a partir dos motores de calibração e sem filtragem pelo detector. Manter a regra de pelo menos dez motores elegíveis, registrar ausências e não presumir admissibilidade. São políticas de diagnóstico, não variantes seleccionadas para implantação.

## Proxy de condição independente do detector e do preditor de RUL

Seja x̄_ij(t) a média causal de 15 ciclos e b_ij=x̄_ij(20). Nos motores de ajuste, calcular D_ij=x̄_ij(T_i)−b_ij. Direcção d_j=sign(mediana_i D_ij); magnitude L_j(q)=quantil_q(d_j D_ij), q ∈ {0,50;0,90}. Usar canais com magnitude positiva e dispersão não desprezível; guardar direcções e magnitudes. O endpoint de cada motor de ajuste é alvo supervisionado permitido, nunca entrada de motor externo.

Definir m̂_ij(t)=clip[1−d_j(x̄_ij(t)−b_ij)/L_j(q),0,1] e Ĥ_i(t)=min_j m̂_ij(t), para t≥20. Ĥ_i(20)=1. Não impor queda monotónica nem patamar até P: ruído pode produzir recuperação aparente. Não usar P para construir a curva ou a própria curva para validar P circularmente. A referência inicial pode apresentar degradação desconhecida, limitação a declarar.

Essa é uma proxy empírica de afastamento orientado até uma referência terminal aprendida, não a reconstrução das margens físicas de Saxena. Não equivale a limite certificado, confiabilidade ou observação de boroscopia. O primeiro Ĥ=0 é F_HI estimado, distinto do endpoint real. Avaliar antecipação, atraso/censura e distribuição de Ĥ no endpoint nos motores externos. Se F_HI ocorrer antes de P ou cedo demais, preservar a contradição como resultado negativo. Não forçar Ĥ(T_i)=0 com o endpoint do próprio motor externo.

Neste piloto, HI não entra no preditor, na calibração, na política ou na geração de inspeções. Sua capacidade de representar F é uma pergunta separada. Guardar trajectórias de HI e parâmetros por fold; examinar curvas de motores com IDs fixados antes da execução (1,2,3), sem escolher exemplos favoráveis.

## Resultados e interpretação prévia

Por configuração: cobertura de P, mediana e dispersão por motor do ciclo de alerta, alertas até 40, antecedência até F; por política/modelo: chegadas ao endpoint e vida não usada. Para robustez, amplitudes do ciclo P entre configurações no mesmo motor e amplitudes dos desfechos. Motor é unidade primária; nenhuma cópia ou janela constitui motor independente.

Não se mede exactidão de P sem referência independente. Mudanças de B0 alteram uma hipótese do cenário. Mesmos resultados de remoção apesar de P variável indicam apenas insensibilidade da política nessa região de decisão. A proxy HI poderá ser inadequada; não usá-la como justificativa para congelar. Não há alvo operacional de risco definido.

Execução: `py experiments/pilot_fd001_03.py`; verificações e relatório: `py experiments/summarise_pilot_fd001_03.py`. Novas saídas em `artifacts/pilot_fd001_03/`. Manter metadados, hashes e registo técnico. O teste oficial permanece fora da execução; os motores usados já pertencem à exploração.
