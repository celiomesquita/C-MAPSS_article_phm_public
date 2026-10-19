# Piloto FD001 01 — detecção e prognóstico sem inspeção

Estado: exploratório, autorizado pelo autor em 16/10/2026. Não retoma os experimentos históricos E01–E07.

**Perguntas.** Como os limites estatísticos e a suavização alteram o ciclo de alerta P? Como quatro regressores e uma margem de sobrestimação alteram previsão e remoção numa simulação sequencial elementar?

## Desenho antes da execução

- Somente `train_FD001.txt`: 100 trajectórias completas. Cinco folds externos agrupados por motor, cada motor avaliado uma vez. Em cada fold, 60 motores para ajuste, 20 para calibração e 20 para avaliação. Teste oficial truncado não utilizado.
- Assume-se saudável o período inicial de 20 ciclos. Cada motor estabelece sua média inicial após esse período. A dispersão dos resíduos filtrados é estimada somente nos motores de ajuste; sensores com dispersão ≤ 1e-6 são excluídos. Não se interpretam os limites como margens físicas de segurança.
- Configuração inicial fixada: média móvel causal de 15 ciclos, afastamento bilateral superior a 2 desvios em pelo menos dois sensores por três ciclos consecutivos. P é o ciclo em que o alerta persistente fica disponível. Ausência de alerta permanece ausência, sem P = 0.
- Sensibilidade do detector: janelas 5/10/15, multiplicador 2/3 e pelo menos 1/2 sensores, sempre persistência 3 e referência inicial 20. Reportar todas as configurações, sem escolher a melhor nos motores externos. Medir disponibilidade do alerta e antecedência até o endpoint; não há rótulo físico independente de P, logo não se mede exactidão de início de degradação.
- Atributos causais: média móvel, desvio padrão, RMS e assimetria por sensor, janela 15. Não incluir ID, endpoint, RUL verdadeira ou ciclo como preditores. Treino e previsão a partir de P; perda de cobertura por detecção ausente deve ser reportada.
- Random Forest, Gradient Boosting, XGBoost e LightGBM, 150 árvores/iterações e parâmetros fixos registrados no código. Ponderação inversa ao número de linhas por motor, para igual peso total por unidade. Sem busca de hiperparâmetros nesta rodada. CatBoost/SHAP indisponíveis no ambiente usado: não substituídos por resultados inventados.
- Margem: quantil empírico 0,9, com arredondamento para cima na ordem amostral, dos máximos erros de sobrestimação por motor de calibração. Subtrair e truncar em zero; não é garantia conformal ou de safety. Não ajustar simultaneamente uma correcção linear nos mesmos resíduos.
- Remoção exploratória: primeiro ciclo disponível com RUL prevista ≤ 0, 5 ou 10 ciclos, antes e depois da margem. Sem disparo, registrar chegada ao endpoint; não conhecer o endpoint para antecipar a acção. Comparadores: remover na detecção P e idade fixa no quantil 0,1 das vidas de ajuste. Esses limiares não são requisitos operacionais certificados nem optimizados.
- Métricas por motor: RMSE ao longo da história pós-P, frequência de sobrestimação, vida não utilizada, exposição e chegada ao endpoint. Agregar dando igual peso aos motores. Chegada ao endpoint não significa acidente aeronáutico.
- Taxa exploratória de restaurações: 1000 dividido pela exposição média. Sua interpretação de renovação depende de vidas AGAN iid, ausência de indisponibilidade e população comparável; não é validação de revisões sucessivas. Custo monetário por exposição resulta dessa taxa multiplicada pelo custo fixo. Nenhuma política será declarada admissível apenas por esse valor.
- Importâncias por redução de impureza são diagnósticas, não SHAP nem demonstração de fidelidade; não comparar magnitudes brutas como consenso físico.

## Limites deliberados desta rodada

Não se constrói HI físico, não se simula inspeção e não se testa fusão PHM + inspeção. Falta definir referência independente para gerar observações e parâmetros da curva. Não há avaliação com utilizadores ou demonstração normativa. As hipóteses deste piloto não congelam o protocolo principal.

O piloto pode mostrar que o detector dispara cedo demais, que a margem é excessiva, que modelos não disparam remoção ou que um comparador simples é superior. Preservar tais resultados. Qualquer escolha posterior baseada nesta rodada é exploratória; seus folds não serão chamados de teste intocado em alegações confirmatórias posteriores.

## Reproduzir

Na raiz, usando o Python global com as dependências registradas em `metadata.json`:

```powershell
py experiments/pilot_fd001.py
py -m unittest discover -s experiments -p test_pilot_fd001.py
```

Saídas: `artifacts/pilot_fd001_01/` (divisões, predições, decisões, sensibilidade, métricas, metadados e figura). O script não modifica os dados brutos. A `.venv` anterior é ambiente do inventário e não foi alterada.
