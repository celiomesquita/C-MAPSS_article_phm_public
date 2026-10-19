# Reconstrução experimental

**P11.2 concluída (17/10/2026).** [Interpretação](artifacts/pilot_loss_decomposition_11b/conclusoes.md): oráculos inicial/após sinal coincidiram para retirada T−1; perda de acesso nula. ISO/inferior98/reserva15 descarta36,08–37,90/35,99–40,50 ciclos adicionais FD001/FD003, localizados após o marco, sem provar que sejam recuperáveis. Antecedência diagnóstica15 apresenta acesso tardio em até3/100. Os69 testes e reconstrução independente passaram; nenhum modelo/regra ajustado ou código copiado da versão vizinha. Próximo: P13.2 com foco na etapa pós-marco. Inspeções continuam adiadas.

**P13.2 concluída com resultado misto (17/10/2026).** [Interpretação](artifacts/pilot_explainability_13b/conclusoes.md): mecanismo fiel, mas rankings/datas variáveis e nenhum prefixo completo no suporte inicial.9.600 ações basais e2.187.520 replays verificados;82 testes,66 fichas. Motor55 FD003: marcos451/239/396, diferença máxima217 ciclos na espera. Corrigido erro de registro antes do primeiro resultado perturbado, com originais/log preservados; sem mudança de modelo/regra. Não congelar ou reduzir reservas: primeiro diagnosticar a instabilidade da aprendizagem/marco. Inspeções continuam adiadas.

**P13.1 concluída (17/10/2026), resultado misto.** [Interpretação](artifacts/pilot_policy_selection_13a/conclusoes.md): seleção de limiar/espera em D40 com 240 ajustes HI internos, escolhas congeladas antes de E; quatro escolhas inviáveis em 240. Maior vida externa, mas 0–2 chegadas/100 com limiar e 0–1 com espera; controles HI/ISO inferior98 mantiveram zero. Os 59 testes passaram; emendas do verificador e seus originais preservados. P13 parcialmente concluída; faltam explicabilidade e confirmação do risco. Sem inspeções, projeção monetária ou edição do artigo.

**P11.1 concluída (17/10/2026).** [Interpretação](artifacts/pilot_landmark_control_11a/conclusoes.md): controle de retirada no primeiro HI≤0,5 mais d teve decisão completa sem chegadas; o incremento do ISO/inferior98/reserva15 foi 0,21–1,57/0–0,83 ciclo médio em FD001/FD003. O marco já explicava 95,93–100% do ganho de vida dessa regra frente à idade fixa. Os 49 testes e a reconstrução de controles/contrastes/decomposições passaram; nenhum novo ajuste ou inspeção. Próximo protocolo: seleção/validação decisória P13 com controle HI competitivo; P12 condicionado à ponte de escala.

**P11 concluída (17/10/2026).** [Interpretação](artifacts/pilot_removal_11/conclusoes.md): limite inferior98 teve decisões completas sem chegadas ao endpoint na amostra; âncora central deixou ausências, e o controle de idade também falhou. Ações concentradas no primeiro marco motivaram P11.1, concluída acima. [Plano experimental](plano_experimentos_remocao.md) subordinado ao [executivo](../docs/gestao/plano_executivo_de_melhorias.md): P12/P13 pendentes, sem projeção monetária ou inspeções. Os 43 testes e reconstrução de 31.200 decisões passaram.

**P10 concluída (17/10/2026).** Calibração nominal 98% em 60 partições F25/C15/U50/E10, com n efetivo 49–50. [Interpretação](artifacts/pilot_f_uncertainty_10/conclusoes.md): quantis finitos, mas antecedência limitada; manter HI/isotônico e especificar a regra antes de remover. Emenda numérica de fronteira sem mudança de classificações ou reajuste; 35 testes e reconstrução de todas as previsões passaram. Sem inspeções ou edição do artigo.

**Estado vigente após P08 — M18 (16/10/2026).** A combinação empírica não negativa P05/P06 foi adotada como HI de referência de trabalho, mantendo o isotônico como controle prognóstico. A busca de fórmula perfeita fica encerrada por ora; a prioridade é robustez, incerteza individual de F, explicabilidade e decisão de remoção. A reconstrução física exata não pode ser validada com as informações disponíveis; isso não demonstra limite físico. Resultados e estados de candidatura nos relatórios anteriores são históricos. [Plano vigente](../docs/gestao/plano_executivo_de_melhorias.md); sem novas execuções ou início de inspeções nesta decisão.

**P09 concluída (17/10/2026).** Novas partições F40/C20/U20/E20 em três repetições; a forma HI foi mantida e os parâmetros reaprendidos. Calibração de intervalos/bandas de F por motor, distinta do bootstrap de diferenças de desempenho. [Interpretação](artifacts/pilot_f_uncertainty_09/conclusoes.md): ganho pontual não assegurou melhor cobertura de trajetória; manter referência M18 e examinar calibração/antecedência antes de remoção. Sem inspeções ou edição do artigo.

## R00.1 — Inventário e ambiente

Na raiz do projeto, em PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe experiments\inventory.py
```

O inventário usa apenas a biblioteca padrão. Nenhuma dependência de treino foi
selecionada ou instalada nesta etapa. O ambiente de treino será definido no
piloto, com versões e disponibilidade de GPU registradas; este ambiente é o da
auditoria dos dados.

Configuração: [configs/inventory.json](configs/inventory.json).
Saídas: [artifacts/inventory/inventory.json](artifacts/inventory/inventory.json),
[resumo CSV](artifacts/inventory/summary.csv) e
[ambiente](artifacts/inventory/environment.freeze.txt).

O script valida 26 colunas, valores finitos, identificadores inteiros positivos,
ordenação das unidades, ciclos consecutivos iniciados em 1, contagens por
subconjunto e correspondência entre quantidade de rótulos RUL e motores de
teste. Registra SHA-256 de todos os arquivos de entrada e verifica que não
mudaram durante a execução. Retorna código diferente de zero se a validação falhar.

Os 21 sensores e três condições operacionais não são selecionados ou normalizados
nesta etapa. IDs de motor são locais ao subconjunto e partição; usar a chave
`(subset, partition, unit_id)` nas etapas seguintes. Estatísticas globais do
inventário não devem orientar pré-processamento ou ajuste de modelos.

Os testes oficiais são truncados. O rótulo RUL informa ciclos remanescentes até
o fim de vida, sem fornecer sensores futuros. Não permite reconstruir o instante
de cruzamento de um THC derivado. As políticas completas serão avaliadas em
trajetórias completas, com partições por motor.

## Piloto FD001 01 — nova rodada exploratória

O autor autorizou os primeiros experimentos. O [protocolo](protocolo_piloto_fd001_01.md)
define detecção de P, quatro regressores e decisões sequenciais exploratórias, com
cinco folds por motor e calibração separada. Não reativa R00.2/E07 históricos.
O piloto usa Python global e registra versões exactas nas saídas; a `.venv` do
inventário permanece independente. Os dados originais não são modificados.

```powershell
py experiments/pilot_fd001.py
py experiments/summarise_pilot_fd001.py
py -m unittest discover -s experiments -p test_pilot_fd001.py
```

Não há HI físico ou inspeção simulada nesta rodada. Sua representação permanece
uma dependência para comparar PHM + inspeção. Novas execuções não serão ajustadas
para recuperar os números históricos do manuscrito.

P01 está concluída: [relatório](artifacts/pilot_fd001_01/relatorio.md),
[metadados](artifacts/pilot_fd001_01/metadata.json) e
[manifesto de hashes](artifacts/pilot_fd001_01/manifest.json).

## P02 — refinamento sem inspeção

[Protocolo](protocolo_piloto_fd001_02.md) e [relatório](artifacts/pilot_fd001_02/relatorio.md).
Rodada concluída com selecção interna por motor e contrastes entre margem global,
região de acção e margem local. Artefactos de P01 permanecem intactos. Inspeções
só serão executadas após congelar o protocolo principal, ainda em aberto.

```powershell
py experiments/pilot_fd001_02.py
py experiments/summarise_pilot_fd001_02.py
py -m unittest discover -s experiments -p test_pilot_fd001*.py
```

## P03 — robustez de P e proxy HI/F

[Protocolo](protocolo_piloto_fd001_03.md): 18 configurações de fase inicial,
suavização e persistência; previsões comuns entre configurações; diagnóstico
separado de HI/F empírico aprendido nos motores de ajuste. Sem inspeção e sem
congelamento do protocolo principal.

```powershell
py experiments/pilot_fd001_03.py
py experiments/summarise_pilot_fd001_03.py
py -m unittest discover -s experiments -p test_pilot_fd001*.py
```
# P04 — avaliação do HI com tolerância inicial

O [protocolo](protocolo_piloto_fd001_04.md) e o [relatório](artifacts/pilot_fd001_04/relatorio.md) documentam a fórmula autorizada, seus controles e o resultado misto. Executar com `py experiments/pilot_fd001_04.py` a partir da raiz; verificar fronteiras com `py -m unittest discover -s experiments -p test_pilot_fd001*.py`. Usa os splits arquivados de P03, sem treinar RUL nem simular inspeções. Não é HI físico nem referência final de inspeção. As fontes e artefatos têm hashes em `metadata.json` e `manifest.json`.
# P05 — HI empírico, AAKR e RUL oficial

O [protocolo P05](protocolo_piloto_fd001_05.md), o [relatório](artifacts/pilot_fd001_05/relatorio.md) e a [interpretação](artifacts/pilot_fd001_05/conclusoes.md) distinguem RUL verdadeira de HI físico e uma adaptação do núcleo AAKR de uma reprodução integral. Executar `py experiments/pilot_fd001_05.py` e verificar com `py experiments/verify_pilot_fd001_05.py`. A seleção é interna por motor; modelos oficiais foram congelados antes de calcular resultados com RUL_FD001. O teste oficial já foi avaliado; futuras modificações não terão esse conjunto como teste intocado. Sem inspeções.
# P06 — transferência e reajuste em FD003

O [protocolo](protocolo_piloto_fd003_06.md), o [relatório](artifacts/pilot_fd003_06/relatorio.md) e a [interpretação](artifacts/pilot_fd003_06/conclusoes.md) documentam a extensão autorizada pelo autor. Executar `py experiments/pilot_fd003_06.py` e verificar com `py experiments/verify_pilot_fd003_06.py`. Reutiliza o núcleo P05 sem alterar seus arquivos. Testes: `py -m unittest discover -s experiments -p test_pilot_fd*.py`. FD001 permanece o cenário principal; FD003 é robustez, com transferência dos modelos congelados e reajuste separado. Ambos os testes oficiais já foram avaliados; sem inspeções ou HI físico/F validado.
# P07 — marco intermediário HI=0,5

O [protocolo](protocolo_marco_hi_50.md) foi executado reutilizando somente as predições congeladas P05/P06, sem novo treino. [Relatório](artifacts/pilot_hi_landmark_07/relatorio.md) e [interpretação](artifacts/pilot_hi_landmark_07/conclusoes.md): cobertura 100/100 nos motores completos após ajuste no domínio; para o HI empírico, antecedência mediana/RMSE de F de 39,5/17,85 ciclos em FD001 e 33/14,84 em FD003. Comparações em ciclos comuns limitam a atribuição das diferenças à representação. Ausências até truncamento, transferência, recuperações e sensibilidades estão preservadas. Não redefine F ou P, não adota fórmula final e não inicia inspeções.

Executar `py experiments/pilot_hi_landmark_07.py` e verificar com `py experiments/verify_pilot_hi_landmark_07.py`. Testes: `py -m unittest discover -s experiments -p test_pilot*.py`. O artigo permanece na versão M17, anterior à execução de P07.

# P08 — trajetória do HI e engenharia de atributos

[Protocolo](protocolo_trajetoria_hi_08.md), [relatório](artifacts/pilot_hi_trajectory_08/relatorio.md) e [interpretação](artifacts/pilot_hi_trajectory_08/conclusoes.md). Fórmula empírica HI congelada; novos conversores Ridge/RF usam somente C20, seleção S20 e avaliação E20/teste. Onze representações, controles isotônicos, ablações de inclinação/curvatura/variabilidade e controles por sensores correntes/médias/estatísticas completas; ciclos comuns ≥39. Resultado misto: pequeno ganho pontual de RF no marco, com intervalos incluindo zero; sem ganho geral em Ridge ou concordância estável de importância. Sem inspeções ou edição do artigo M17.

Executar `py experiments/pilot_hi_trajectory_08.py`, gerar relatório com `py experiments/report_pilot_hi_trajectory_08.py` e verificar com `py experiments/verify_pilot_hi_trajectory_08.py`. Testes: `py -m unittest discover -s experiments -p test_pilot*.py` (24 testes antes da execução). Modelos por partição são serializados em joblib e previsões completas em CSV comprimido; eventos, coberturas, contrastes e ranks ficam em CSV. Não chamar o bootstrap das diferenças de intervalo preditivo individual.

Uma emenda de pós-processamento recalculou Spearman na interseção dos sensores, preservando a versão anterior e sem mudar previsões ou erros; ver [registro](artifacts/pilot_hi_trajectory_08/rank_correction.json). O script principal e o verificador já contemplam a definição corrigida. Os 25 testes passaram após acrescentar regressão para canais diferentes entre partições.

# P09 — robustez e incerteza de F

[Protocolo](protocolo_incerteza_f_09.md), [relatório](artifacts/pilot_f_uncertainty_09/relatorio.md), [interpretação](artifacts/pilot_f_uncertainty_09/conclusoes.md) e [verificação](artifacts/pilot_f_uncertainty_09/verification.json). Executar `py experiments/pilot_f_uncertainty_09.py`, verificar com `py experiments/verify_pilot_f_uncertainty_09.py` e gerar relatório com `py experiments/report_pilot_f_uncertainty_09.py`. Testes: `py -m unittest discover -s experiments -p test_pilot*.py` (29 passaram antes da execução).

F ajusta HI, C ajusta conversores e U calibra exclusivamente incerteza nesta rodada; não selecionar em U/E. Três repetições não são 300 motores independentes. Os quantis por motor seguem rank corrigido, preservando +infinito quando a amostra não sustenta o nível. As coberturas oficiais truncadas se referem somente à trajetória observada. Alvos nominais de 90%/95% não são requisitos de safety, e o limite inferior de F não define sozinho uma remoção. Todos os métodos/repetições/ausências permanecem arquivados.

# P10 — calibração 98% e antecedência disponível

[Protocolo](protocolo_incerteza_f_10.md), [relatório](artifacts/pilot_f_uncertainty_10/relatorio.md), [interpretação](artifacts/pilot_f_uncertainty_10/conclusoes.md) e [verificação](artifacts/pilot_f_uncertainty_10/verification.json). Execução: `py experiments/pilot_f_uncertainty_10.py`; verificação: `py experiments/verify_pilot_f_uncertainty_10.py`; relatório: `py experiments/report_pilot_f_uncertainty_10.py`. Testes: `py -m unittest discover -s experiments -p test_pilot*.py` (35 passaram).

Três repetições de dez dobras por domínio; ISO e RF_SLOPE pré-fixados. A calibração U50 é exclusiva e usa o máximo temporal por motor; nenhum ajuste por U/E. A fração de motores com L−t≥m+d é diagnóstico de informação, sem adotar âncora ou política. 98% nominal não comprova ultrapassagem ≤2% na futura decisão. Os dados já foram examinados; não são teste confirmatório intocado.

O código atual inclui tolerância de 10⁻⁹ ciclo para comparações de reserva no limiar. Os artefatos preservam a execução inicial e a [emenda](artifacts/pilot_f_uncertainty_10/amendment_numeric_boundary.json), produzida uma única vez por `correct_numeric_boundary_10.py`, sem reajuste. Não reaplicar a emenda aos arquivos já corrigidos; `frozen_input_archive.json` mapeia os hashes das fontes originalmente executadas.

# P11 — remoção e custo normalizado

[Protocolo](protocolo_remocao_11.md), [relatório](artifacts/pilot_removal_11/relatorio.md), [interpretação](artifacts/pilot_removal_11/conclusoes.md) e [verificação](artifacts/pilot_removal_11/verification.json). Execução: `py experiments/pilot_removal_11.py`; verificação: `py experiments/verify_pilot_removal_11.py`; relatório: `py experiments/report_pilot_removal_11.py`. Testes: `py -m unittest discover -s experiments -p test_pilot*.py` (43 passaram antes de executar). O script protege a rodada concluída contra reexecução sobre os mesmos artefatos.

São 16 regras primárias, oito sensibilidades95 e dois controles de idade. Somente previsões/quantis P10 congelados; nenhum ajuste ou inspeção. Fontes e logs do verificador inicial foram arquivados após correção para truncados sem previsões e separador Windows no mapeamento; decisões não mudaram. Não interpretar custo por exposição simulada como poupança monetária de 20 anos. O controle P11.1 subsequente qualificou a atribuição do benefício ao prognóstico, preservando os artefatos desta rodada.

# P11.1 — controle de condição e incremento do conversor

[Protocolo](protocolo_controle_marco_11a.md), [relatório](artifacts/pilot_landmark_control_11a/relatorio.md), [interpretação](artifacts/pilot_landmark_control_11a/conclusoes.md) e [verificação](artifacts/pilot_landmark_control_11a/verification.json). Executar `py experiments/pilot_landmark_control_11a.py`, verificar com `py experiments/verify_pilot_landmark_control_11a.py` e gerar relatório com `py experiments/report_pilot_landmark_control_11a.py`. O script protege a rodada concluída contra reexecução. Testes: `py -m unittest discover -s experiments -p test_pilot*.py` (49 passaram antes da execução).

Controle sem conversor/quantil na decisão, com o mesmo HI supervisionado e aquecimento P11. Todos os artefatos anteriores permanecem intactos; 2.400 controles, 156 contrastes e 144 decomposições conferidos, sem emendas. Decompor ganhos de vida aditivamente e fatores de custo multiplicativamente; não somar percentagens de economia. O resultado não torna o HI não supervisionado nem comprova risco populacional ou ganho financeiro empresarial.
# P13.3 — diagnóstico de influência da aprendizagem do HI

[Protocolo](protocolo_influencia_hi_13c.md), [resultados](artifacts/pilot_hi_influence_13c/conclusoes.md), [verificação](artifacts/pilot_hi_influence_13c/verification.json) e [reconstrução aprofundada](artifacts/pilot_hi_influence_13c/deep_verification.json). Execução protegida contra sobrescrita: `py experiments/pilot_hi_influence_13c.py`. Verificação: `py experiments/verify_hi_influence_13c.py` e `py experiments/verify_hi_influence_deep_13c.py`; relatório: `py experiments/report_hi_influence_13c.py`. Cinco testes pré-execução: `py -m unittest discover -s experiments -p test_hi_influence_13c.py`. Foram300 ajustes diagnósticos F24 e3.000 respostas dependentes; identificada instabilidade da orientação mediana e dos coeficientes em FD003. Sem nova política/fórmula adoptada, inspeções ou uso dos arquivos RUL/test oficiais.
# P13.4 — estabilização do HI somente em desenvolvimento

[Protocolo](protocolo_estabilizacao_hi_13d.md), [resultados](artifacts/pilot_hi_stabilization_13d/conclusoes.md), [conferência integral](artifacts/pilot_hi_stabilization_13d/verification.json) e [ajustes finais F25](artifacts/pilot_hi_stabilization_13d/final_fit_verification.json). Execução protegida: `py experiments/pilot_hi_stabilization_13d.py`. Verificação integral vetorizada: `py experiments/verify_hi_stabilization_fast_13d.py`; modelos finais: `py experiments/verify_hi_stabilization_final_13d.py`; relatório: `py experiments/report_hi_stabilization_13d.py`. O verificador sequencial original e seu log parcial foram preservados. Sete testes pré-execução: `py -m unittest discover -s experiments -p test_hi_stabilization_13d.py`. Foram31.200 soluções,312.000 respostas internas e60 indicações (59 elegíveis/uma contingência), sem U/E na escolha ou avaliação. Melhora agregada não protege todos os máximos; conversores/calibração novos ainda precisam ser testados com os HIs indicados.

# P13.5 — transferência decisória das indicações de HI

[Protocolo](protocolo_cadeia_hi_13e.md), [resultados](artifacts/pilot_hi_chain_13e/conclusoes.md) e [verificação](artifacts/pilot_hi_chain_13e/verification.json). Execução protegida contra sobrescrita: `py experiments/pilot_hi_chain_13e.py`. Verificação independente: `py experiments/verify_hi_chain_13e.py`; figura: `py experiments/report_hi_chain_13e.py`. Oito testes pré-execução: `py -m unittest discover -s experiments -p test_hi_chain_13e.py`. Cadeias M18 (reprodução de P10) e SEL (60 indicações de P13.4, conversores reaprendidos em C15, quantis em U50) avaliadas nos mesmos E10, com dez regras fixas e 12.000 decisões. Somente arquivos train. Resultado misto, sem transferência favorável: mais vida e menor erro no marco, mas estabilidade entre repetições pior em FD001 e eventos de endpoint do FD003 motor 10 em SEL. M18 permanece referência.
