# Auditoria de consistência documental: `main.tex` (versão após M42)

## 1. Identificação e cobertura

- **Documento:** `LaTeX/manuscript/main.tex`, 748 linhas, compilado em `main.pdf` (35 páginas). SHA-256 de `main.tex`: `d9de66435065e5bf8dde8b80a5218a78bbd068522c9d5b7ba7cf3b5467096e4c`; de `main.pdf`: `15ca3ac3f008361d108cf66054be32a69974481bf831dbc0528f66bee10b6390`. Auditoria de 18/10/2026.
- **Escopo:** manuscrito inteiro (fonte e PDF extraído com `pdftotext -layout`), `references.bib` e `main.bbl`. Seções antigas (método e resultados de P01 a P06) contra seções novas (P07 a P18). Verificação de números do resumo, das tabelas novas e do texto contra os relatórios de interpretação e as tabelas de resultados arquivadas em `experiments/artifacts/`. Referências a linhas são do arquivo-fonte `main.tex`; as páginas do PDF não foram usadas.
- **Fora do escopo:** validade científica, originalidade e prontidão para submissão; conformidade com o modelo de um periódico (o periódico-alvo não está definido); conferência das citações contra as fontes primárias externas.
- **Normas fornecidas:** nenhuma; requisitos de periódico marcados como não verificados.

## 2. Achados principais

| ID | Classe | Resumo |
|---|---|---|
| DC001 | Maior | Colisões de notação entre seções antigas e novas (ρ, λ, α, τ, k, γ, A) |
| DC002 | Maior | Faixas de economia diferentes entre o resumo e os resultados para a mesma comparação |
| DC003 | Maior | Rótulos de piloto P07 a P13 usados sem definição no artigo |
| DC004 | Maior | Título inventado na entrada `AC2019`; entrada `Miranda2026` com acentos quebrados; notas de verificação impressas |
| DC005 | Menor | Regra de limiar selecionado na Tabela de extensão, fora do conjunto principal do protocolo |
| DC006 | Menor | "earlier fallback analyses" remete a análises não relatadas |
| DC007 | Menor | Dois sentidos de "idade": controle por partição (127 a 146) e limite único de 127 |
| DC008 | Menor | Estado do HI: futuro e "validar" nas seções antigas, "referência de trabalho" nas novas |
| DC009 | Menor | Antecedência necessária de 16 e de 17 ciclos sem explicitar o prazo de execução |
| DC010 | Menor | Identificadores de motor ("unit 55") e rótulo "RF" com dois papéis |

### DC001. Colisões de notação (maior)

| Símbolo | Uso antigo (linha) | Uso novo (linha) |
|---|---|---|
| ρ | escala do alvo de treino, H\*=min{1,(T−t)/ρ}^η (303, 313, 348) | ciclo de remoção ρ_i=τ_i+ε (356, 388) |
| λ | regularização ridge (310, 313) | taxa de restauração λ^π (388) |
| α | nível do marco, t_{i,α} com α=0,5 (340 a 343, 354, 358) | nível de calibração α=0,02 (372); t_{j,α} reaparece na linha 370 no contexto do nível |
| τ | limiar de alerta de detecção (163 a 191) e limiar selecionado τ_k^\* (719 a 722) | ciclo de decisão τ_i (354, 358) e portão τ_0 (384) |
| k | índice de dobra em 𝓕_k, 𝓒_k, 𝓢_k, 𝓔_k (varia nas seções 3 e 12) | posto k=⌈(n+1)(1−α)⌉ (372) e escala k=L_ref/T̄ (390 e seguintes) |
| γ | expoente da curva de inspeção (414, 415) | confiança γ do limite de Clopper-Pearson (382) |
| A | escore de alerta A^0_{i,k} da P02 (171, 173) | oráculo 𝐀 (378), A_age (376), limite de idade A (382) |

**Consequência:** o mesmo símbolo tem dois significados no mesmo documento; a equação da linha 354 usa α do marco e a da linha 372, α da calibração. **Correção:** renomear os usos novos (por exemplo ρ_i→r_i ou ϱ_i; λ^π→ν^π; α_c para o nível de calibração; τ_i→δ_i ou t_i^d; k de posto e escala em outras letras; γ de confiança→c; A de idade→A_L). **Critério de conclusão:** nenhum símbolo com dois significados sem desambiguação; ocorrências conferidas por busca.

### DC002. Faixas de economia discordantes (maior)

- **Resumo (linha 58):** "20,0 a 22,9% (FD001) e 29,0 a 30,3% (FD003)" de redução na taxa de restauração por ciclo simulado frente ao controle de idade.
- **Resultados (linha 607 e seguintes):** "20,05 a 23,11% (FD001) e 28,95 a 30,47% (FD003)" de redução do custo normalizado frente ao mesmo controle.
- **Evidência de origem:** as primeiras são as de prazo de execução 1 (P12.1: 20,05 a 22,85% e 28,95 a 30,30%); as segundas cobrem os prazos 1 e 2 e vêm de P11. O texto não declara o prazo nem que são duas medidas distintas (taxa de restauração por ciclo contra custo normalizado).
- **Consequência:** dois pares de números para a mesma comparação, sem explicação. **Correção:** declarar o prazo de execução em ambos e usar um só conjunto, ou explicar a diferença. **Critério:** resumo e corpo com os mesmos números e o prazo declarado.

### DC003. Rótulos de piloto não definidos (maior)

Os rótulos P01 a P06 são definidos no método e nas tabelas. Os rótulos P07 (linhas 580, 586, 594), P08 (580), P09 (366), P10 (586, 597), P11 e subitens (631), P13.1 (378, 631) aparecem sem que o artigo diga o que são, nem sua ordem, nem o protocolo de cada um. P12 e P14 a P18 não aparecem (embora o conteúdo de P12, P14, P15, P16 e P18 esteja nos resultados sem rótulo). **Consequência:** o leitor não mapeia "(P10)" ou "(P13.1)". **Correção:** quadro curto que liste os rótulos ou substituir os rótulos por descrições ("calibração do margem", "seleção de limiar"). **Critério:** todo rótulo usado tem definição no corpo.

### DC004. Bibliografia (maior)

- `AC2019` (linha final do `.bib`): o título "CFM56-5B, CFM56-7B and V2500 removal intervals and shop visits" **foi escrito por mim e não corresponde ao artigo**; o título impresso na fonte é "CFM56-5B/-7B & V2500 experience surge in shop visit activity" (texto extraído de `references/cenario_economico_20anos/fontes_ciclos_k/AC_2019_issue125_CFM56-5B.txt`, p. 27).
- `Miranda2026`: o campo `school` ficou com apóstrofos no lugar dos acentos (`Tecnol'ogico`, `Aeron'autica`, `Jos'e`) e a referência impressa mostra isso (`main.bbl`, linha 34).
- Notas como "citation details to be verified" e "title to be verified against the original" aparecem na lista impressa (linhas 1003 a 1019 do texto extraído). O editor `\todo` não cobre esses campos.
- **Correção:** usar o título verdadeiro da `AC2019`; corrigir acentos de `Miranda2026`; mover as notas de verificação para comentários de `.bib` ou usar marcação que a versão de submissão oculte. **Critério:** nenhum título inventado; PDF sem acentos quebrados.

### DC005. Regra do limiar na Tabela de extensão (menor)

A Tabela `tab:extension` inclui "Selected threshold", enquanto o rascunho do protocolo principal (seção 5, M38) deixa o limiar e a espera selecionados de P13.1 **fora do conjunto principal**. **Correção:** legendar a linha como contraste exploratório ou removê-la. **Critério:** tabelas e protocolo com o mesmo conjunto de regras ou diferença declarada.

### DC006. Análises não relatadas (menor)

Linha 645: "as in the earlier fallback analyses" remete a análises (teto de idade) que o artigo não descreve nem tem rótulo. **Correção:** descrever em uma frase ou remover a referência. **Critério:** nenhuma referência a análise não relatada.

### DC007. "Idade" em dois sentidos (menor)

O controle de idade (A_age=min_{𝓕∪𝓒}T−1, 127 a 146 por partição, linha 376) e o limite único A=127 (linha 382) são distintos. A Tabela `tab:removal-rules` usa o controle por partição e a Tabela `tab:extension` usa a remoção em 127 como referência, ambos chamados de "age" ou "limit" em partes do texto. **Correção:** nomear A_age e A de modo distinto e legendar a referência de cada tabela. **Critério:** cada tabela diz contra que referência compara.

### DC008. Estado do HI e verbos no futuro (menor)

- Linha 348: "The criterion for adopting an empirical HI **will** concern validated condition representation…", no futuro, enquanto as seções novas já tratam o HI como referência de trabalho adotada.
- Linha 91, objetivo 3: "derive and **empirically validate** a sensor-based HI formulation", enquanto a discussão diz que a manutenção do HI não é validação física. Esclarecimento de redação: o texto deve indicar o sentido de "validar" (utilidade prognóstica em dados de desenvolvimento). A adequação científica do objetivo fica com a revisão substantiva.

### DC009. Antecedência de 16 e de 17 ciclos (menor)

O texto das explicações (linha 637 e seguintes) cita "required lead of κ+ε=16 cycles" e a tabela de marco usa "κ+ε=17". Ambas corretas (prazos 1 e 2), mas o texto não explicita o prazo em nenhuma delas. **Correção:** acrescentar "(ε=1)" e "(ε=2)". **Critério:** cada valor com seu prazo.

### DC010. Identificadores e rótulos (menor)

"unit 55" (linhas 637 e 641) usa o identificador de motor do arquivo, não definido no artigo. O rótulo "RF" nomeia, nas seções P01 e P02, uma família de regressão por floresta aleatória e, nas novas, a floresta sobre HI e inclinação. A definição existe nas duas, mas o duplo papel pode confundir. **Correção:** definir "unit" e distinguir os dois usos.

## 3. Verificação numérica

| Item | Localização | Objeto de suporte | Resultado |
|---|---|---|---|
| Faixas de taxas de restauração e vidas utilizadas | Tabela `tab:removal-rules` | `pilot_renewal_12a/rates.csv` (recalculado) | Consistente: 8 de 8 faixas e 4 contagens de eventos (5, 0, 0, 34 e 5, 0, 0, 42) |
| Extensão, economia e sensibilidade a u | Tabela `tab:extension`; texto | `pilot_extension_16a/summary.csv` e `condition_dependence.csv` (recalculado) | Consistente: 8 de 8 extensões e economias, u=0,005 e 0,02 |
| Teste de regimes | Tabela `tab:regime-test` | `pilot_regime_synthetic_18a/summary.csv` | Consistente nas 4 linhas |
| Marco e margem (P07, P10) | Tabela `tab:landmark-margin` | Relatórios de interpretação | Consistente; valores não recalculados dos arquivos brutos |
| Resumo contra corpo | Linha 58 | Corpo e tabelas | Consistente exceto DC002 |
| Contagem "200 motores, 0,80/1,14/1,49%" | Seção do limite de idade | Teste de P15.4 | Consistente |

Nenhuma das discrepâncias de DC002 é erro de transcrição; são conjuntos de prazo diferentes não declarados. Direção: não há padrão sistemático entre os achados numéricos.

## 4. Siglas e termos

Siglas conferidas: PHM, RUL, HI, IP-180, MSG-3, C-MAPSS, RMSE, AAKR, ISO, RF, F, P, FD001, FD003, FD002, FD004; EGT é escrita por extenso e "LLP" não é usada (usa-se "life-limited parts"). Definição antes do primeiro uso no corpo: confirmada para todas, com "ISO" definida na linha 366 e usada pela primeira vez na linha 582. Exceções menores: "FD002" e "FD004" são citadas no resumo (linha 58) sem que a sigla seja explicada ali (os quatro subconjuntos são descritos na introdução e no método), e "RF" tem dois papéis (DC010). Nenhuma lista de siglas existe nem é exigida.

## 5. Referências cruzadas e metadados

- Rótulos definidos: 17. Todos os alvos de `\cref` existem (14 alvos distintos); sem referências indefinidas na compilação.
- Rótulos de seção `sec:intro`, `sec:pilot-discussion`, `sec:pilot-conclusion` não são referenciados; sem problema.
- Todas as tabelas novas são citadas no texto.
- Citações: 22 chaves únicas em 17 comandos `\cite`; todas existem em `references.bib` (56 entradas). A identidade das citações com as fontes externas não foi verificada (ver DC004).
- Nomes, filiação e correspondência: um único autor; consistente com o `\ead` e a afiliação.

## 6. Resumo e palavras-chave

Há apenas o resumo em inglês. As palavras-chave (6, depois de remover a ARP7122) são consistentes com o corpo. O resumo não contém números sem lastro no corpo; a ressalva é DC002.

## 7. Livro-razão de cobertura

| Categoria | Estado | Observação |
|---|---|---|
| Números e unidades | Parcialmente verificado | 4 tabelas novas recalculadas dos arquivos; tabelas P01 a P06 não reauditadas por terem sido congeladas antes; texto de P07 a P18 conferido contra relatórios |
| Siglas, termos e notação | Verificado | Colisões em DC001 |
| Referências cruzadas e metadados | Verificado | 17 rótulos, 22 chaves |
| Frente da obra institucional | Não aplicável | Artigo de periódico |
| Resumos paralelos | Não aplicável | Só um resumo |
| Normas de periódico | Não verificado | Periódico não definido |

## 8. Itens que exigem esclarecimento

1. O periódico-alvo e seu modelo (limite de palavras, estilo de referências, marcação editorial).
2. Se os rótulos de piloto devem ser mantidos no artigo ou substituídos por descrições.
3. Se o limiar selecionado deve continuar na Tabela de extensão.

## 9. Acompanhamento

Nenhuma correção foi aplicada: esta auditoria é apenas documental. Aguardando autorização para corrigir DC001 a DC010. As correções devem ser seguidas de nova compilação e nova checagem dos itens afetados.

## 10. Correções aplicadas e rechecagem (18/10/2026)

O autor decidiu que os rótulos de piloto P07 em diante virão como descrições e autorizou as correções. Cópias anteriores em `historico/main_before_consistency_corrections.tex` e `historico/references_before_consistency_corrections.bib`. Versão corrigida: 35 páginas, compilação sem referências indefinidas, caixas largas nem erros.

| ID | Estado | O que foi feito e como foi rechecado |
|---|---|---|
| DC001 | Resolvido | Usos novos renomeados: ciclo de remoção ρ_i→ϱ_i; ciclo de decisão e portão τ_i, τ_0→δ_i, δ_0; taxa de restauração λ^π→ϖ^π; nível de calibração α→α_c e posto k→χ (com o marco t_{j,α}, α=0,5, explicado); escala k→ξ; confiança γ→ψ; limite de idade A→A_L; oráculo 𝐀→𝐎_s; regime c(t)→ζ(t) com médias e desvios μ^reg, σ^reg. Busca por símbolo após a correção: ρ, λ, τ, γ e k só ocorrem nos sentidos antigos nas linhas citadas na seção 2 |
| DC002 | Resolvido | Resumo e corpo agora usam as mesmas faixas para o prazo de execução 1 (20,05 a 22,85% e 28,95 a 30,30%) e o corpo acrescenta as do prazo 2 (20,39 a 23,11% e 29,29 a 30,47%), conferidas recalculando das decisões arquivadas |
| DC003 | Resolvido | Todos os rótulos P07 em diante, que apareciam entre parênteses, foram removidos ou trocados por descrições; busca por "(P" seguido de dígitos retorna zero |
| DC004 | Resolvido | Título de `AC2019` corrigido para "CFM56-5B/-7B & V2500 experience surge in shop visit activity" (fonte, p. 27); acentos de `Miranda2026` corrigidos (`main.bbl`, linha 34, mostra `{\'o}`); notas "to be verified" movidas para comentários `% TODO` do `.bib` e ausentes da lista impressa. A verificação das citações contra as fontes continua pendente (`AC2003`, `AC2019`, `Lei2018`, `Miranda2026`) |
| DC005 | Resolvido | Linha rotulada "Selected threshold (exploratory contrast)" e legenda declara que está fora do conjunto principal |
| DC006 | Resolvido | Frase reescrita como "a variant examined during development and not detailed here" |
| DC007 | Resolvido | A legenda da tabela de regras define o controle de idade por partição (A_age) e diz que difere do limite único A_L; a tabela de extensão compara com A_L=127 |
| DC008 | Resolvido | "will concern" passou a "concerns"; o objetivo 3 passou de "empirically validate" a "empirically evaluate, by its prognostic utility on held-out engines" |
| DC009 | Resolvido | "(ε=1)" e "(ε=2)" explicitados junto das antecedências de 16 e 17 ciclos |
| DC010 | Resolvido | "unit 55" passou a "engine 55 in the file numbering"; "RF" passou a "RF-slope" nas seções novas; resumo diz "The multi-condition subsets FD002 and FD004" |

Pendências que a correção não fecha: verificação bibliográfica das quatro entradas acima e definição do periódico-alvo. Nenhum achado novo foi encontrado na rechecagem dos itens afetados, mas a rechecagem não substitui nova leitura completa.
