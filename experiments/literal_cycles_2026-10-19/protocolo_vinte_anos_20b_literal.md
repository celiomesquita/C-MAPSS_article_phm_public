# P20.2 — um ciclo por voo, três braços e quatro subconjuntos

Autorizado pelo autor em 19/10/2026: um ciclo de cada motor corresponde a um voo da aeronave; cada voo de um bimotor acrescenta um ciclo a cada posição. A frase “Pode prosseguir” autoriza o recálculo e a atualização do artigo, suplemento e plano. Protocolo escrito antes da execução desta análise; posterior à confirmação e, portanto, exploratório. Não modifica o protocolo congelado nem os resultados P20.1.

## Contrato

- `xi=1`: idade 127, reserva 15, execução 1/2, inspeção a cada cinco ciclos e janela de dano 60 são contados em voos por motor.
- 20 anos × 1.600 voos/ano = 32.000 ciclos por posição, não 64.000. Duas posições equivalentes têm o dobro da despesa esperada; não se infere independência ou risco conjunto dos motores.
- Restauração completa, frota madura, contador LLP 20.000 independente e não reiniciado nas restaurações de degradação; custo US$6 milhões por visita, incluindo LLP. US$5/7 milhões são multiplicadores lineares. Inspeção e monitoramento sem custo incremental; sem desconto, inflação, indisponibilidade ou consequências monetárias dos eventos.
- Monitoramento sempre válido; gerador de inspeção P17/P20.1 inalterado: entrada 127, passo 5, W=60, gamma=1, pP=0, pF=1. Rejeição só antecipa.

## Dados e braços

Somente decisões completas arquivadas P13.1 e P19.1, sem sensores, ajuste, escolha de política ou abertura de dados novos. Preservar três repetições e dois prazos; 100/180/100/169 motores FD001/FD002/FD003/FD004 por repetição. Guardar cópia das colunas necessárias e hashes dos arquivos originais.

IDADE127, PHM e híbrido para ISO/inferior98/reserva15, RF-slope/inferior98/reserva15, marco HI e as duas previsões de ponto. Tabela principal: prazo 1 e três braços ISO conservador; tabela de visitas/eventos mantém controles e ponto. As outras regras/prazo permanecem nos CSVs; não selecionar retrospectivamente vencedora.

## Simulação e orçamento

Reutilizar sem mudança as funções do simulador corrigido P20.1, em módulo portátil com NumPy/pandas. 2.000 réplicas por célula, semente 20261019 e chaves subconjunto/repetição; números aleatórios comuns aos braços. Doze células centrais, 22 braços por célula. Sem nova grade de escala ou ajuste de parâmetros. Registrar duração e erro Monte Carlo; não adaptar orçamento para favorecer sinais.

## Verificações antes de relatar

1. Probabilidades por motor somam um; índice do motor, vida e eventos preservados. Comparar o núcleo copiado com a AST das funções originais.
2. Recalcular distribuições por implementação escalar independente e conferir pesos/vida/eventos de todos os braços/células.
3. Reproduzir exatamente as cinco contagens de renovação por implementação escalar independente em 12 réplicas por braço/célula, incluindo início com distribuição de vida ponderada por comprimento e contador LLP independente.
4. Sem LLP e com início estacionário, comparar a média com `32000/E[vida]` em todos os braços/células; máximo |z| < 4,5. Preservar e investigar qualquer falha sem mudar limiar após observar resultados.
5. Visitas LLP idênticas entre braços de cada réplica; caso determinístico idade 127 sem LLP confere contagens exatas para início novo/maduro. Evento adverso não é excluído do custo nem da simulação.

Falha material impede relato até diagnóstico e correção documentados. Alterações de implementação recebem emenda, sem sobrescrever execução falha.

## Saídas e interpretação prévia

Visitas de degradação/LLP e totais, eventos ausente/exato/tardio, despesa por posição e média das três repetições, contrastes pareados e erros Monte Carlo condicionais. A incerteza Monte Carlo não é incerteza populacional; repetições reutilizam motores e não ampliam amostra independente.

Se a ordenação persistir em relação a P20.1, relatar estabilidade nas duas convenções examinadas, sem validar equivalência física. Se mudar, explicar efeitos de horizonte, LLP e início. Valores absolutos grandes são consequência do pressuposto, não razão para ajustar a escala. Empate não autoriza superioridade. Não inferir ótimo econômico ou aceitabilidade de risco. Manter P20.1 como sensibilidade histórica com ponte no suplemento, claramente separado do cenário literal agora principal.

## Artefatos

`experiments/twenty_year_20b_literal.py`, `experiments/verify_twenty_year_20b_literal.py`, pacote `experiments/literal_cycles_2026-10-19/` com entradas pequenas, código de referência, CSVs, validação, manifesto e README. A reprodução pública não requer os sensores ou modelos privados. Publicação remota não está incluída nesta execução.
