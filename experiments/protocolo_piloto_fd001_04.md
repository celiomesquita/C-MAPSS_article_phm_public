# P04 — HI com tolerância inicial e referência terminal empírica

Protocolo exploratório definido em 16/10/2026 antes da execução de P04, após autorização da formulação pelo autor. RQ1/RQ6: uma margem por sensor com tolerância inicial oferece uma referência de condição interpretável, sem antecipar excessivamente F nem deixar de o representar? A evidência de P03 já é conhecida; as mesmas avaliações externas são reutilizadas e não constituem confirmação independente.

## Construção

Manter média causal de 15 ciclos e referência própria b_ij=x̄_ij(20); HI só existe a partir de 20. Nos 40 motores de ajuste de cada fold, aprender d_j=sign(mediana_i[x̄_ij(T_i)−b_ij]). A dispersão σ_j é o desvio amostral dos resíduos x̄_ij(t)−b_ij nos ciclos 15–20 desses motores, usando a mesma variável filtrada. A estabilidade desses segmentos é hipótese, não observação de motor novo. Excluir σ_j≤10⁻⁶ e direcção nula.

Para q∈{0,50;0,65;0,75;0,85;0,90;0,95;0,99;1}, definir B_j(q)=Q_q^+{d_j[x̄_ij(T_i)−b_ij]} nos motores de ajuste. Reter apenas B_j(q)>3σ_j+10⁻⁶. Essa elegibilidade, comum às três tolerâncias de cada q, evita confundir tolerância com exclusão de canal. Reportar os canais excluídos; a elegibilidade pode variar entre quantis.

A_j=kσ_j, k∈{0,2,3}. k=2 é a formulação principal, k=0 o controle sem tolerância e k=3 sensibilidade. Com a_ij(t)=d_j[x̄_ij(t)−b_ij]:

    m̂_ij(t)=clip(1−max(0,a_ij(t)−A_j)/(B_j−A_j),0,1)
    Ĥ_i(t)=min_j m̂_ij(t).

Não impor monotonicidade, persistência ou P na curva. Registrar o sensor limitante; em empates, a ordem dos sensores resolve apenas a apresentação, não significa causa exclusiva. O mínimo igual a um tem todos os canais empatados. Por álgebra, m̂=0 iff a≥B: o primeiro zero deve ser idêntico entre k=0,2,3 quando os canais são iguais. A tolerância não resolve sozinha os problemas terminais de P03.

## Partições e selecção interna

Reutilizar exactamente splits.json de P03: 40 ajuste, 20 calibração, 20 selecção e 20 avaliação, em cinco folds agrupados por motor. As 20 unidades de calibração permanecem reservadas e não são usadas nesta rodada de HI. Não reestimar referências após seleccionar q. Nenhum endpoint externo entra na transformação.

Seleccionar q nos 20 motores de selecção, usando k=2 e perda média por motor: se houver primeiro zero F̂≤T, L=(T−F̂)/(T−20); caso contrário L=λ. λ=1 é o cenário principal e λ∈{0,25;0,50;2} são sensibilidades ao custo convencional de ausência de passagem. Empates resolvidos pelo menor q. Essa perda equilibra antecipação e ausência, não é custo de manutenção nem critério de safety. Não escolhe um quantil definitivo para o protocolo principal. Se nenhum canal for elegível, o candidato é inválido e não pode ser seleccionado.

Avaliar externamente todos os candidatos, preservando separadamente a curva escolhida internamente para cada λ. A avaliação externa não muda a escolha. Reportar cobertura de primeiro zero, antecipação mediana/máxima entre passagens, HI terminal, fracção de HI<1 nos ciclos 21–40 (hipótese de estabilidade), recuperações após primeiro zero e aumentos de HI por motor. Ausência de zero é censura no endpoint; não imputar um F futuro nem afirmar atraso observado após T. Curvas exemplares: motores 1,2,3, previamente fixados.

## Interpretação e parada

Favorável: tolerância reduz saídas do patamar inicial e a referência seleccionada apresenta passagem próxima ao endpoint com poucas ausências e recuperações. Misto: melhoria do patamar acompanhada de antecipação/ausência ou dependência forte de λ. Contrário: deterioração/inadequação persistente da referência. Reportar dispersão por motor/fold, sem inferência confirmatória ou alegação de HI físico. Concluir a rodada após os cinco folds, sem ajustar grelha ou critério a resultados externos. O início físico de degradação não tem rótulo independente, portanto não validar P com essa mesma construção.

Sem novo treino de RUL, decisões económicas ou simulações de inspeção. Preservar artefatos P01–P03. Saídas: parâmetros, selecção interna, métricas individuais/agregadas, curvas seleccionadas, figura, relatório, metadados e hashes. Testar independência de endpoint externo, causalidade, equivalência dos zeros e selecção independente da avaliação externa.
