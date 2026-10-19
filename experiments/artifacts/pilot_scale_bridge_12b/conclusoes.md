# P12.2 — ponte de escala k, cenário de 20 anos e estabilidade da ordenação

## Resultado e alcance

Os resultados por **ciclo simulado** de P12.1 permanecem os resultados científicos principais e não mudaram. Esta rodada acrescenta um **cenário operacional de 20 anos condicionado** a k, utilização, limite de LLP, condição inicial e eficiência de restauração. Nenhuma equivalência física é validada; k é uma hipótese de escala calibrada em fontes técnicas secundárias. Sem inspeção, receita, disponibilidade ou valor financeiro de companhia. Exploratório: os motores E já foram examinados em P10–P13.5.

## Calibração e compatibilidade (resumo)

[Ficha completa](../../../references/cenario_economico_20anos/calibracao_k.md). Ciclo C-MAPSS = voo (Saxena et al., secção V). Endpoint C-MAPSS = menor margem normalizada zerada (estol 15%, EGT ≈2%); aproxima-se de remoções por erosão de margem EGT e **não inclui** LLP nem eventos não programados. Dez intervalos regidos por EGT/desempenho (Aircraft Commerce 2003, 2005, 2019) dão mediana de pontos médios de 8.425 EFC (faixa 6.000–16.500; extremos de linha 4.000–19.000). Com T̄ = 206,3 (FD001) e 247,2 (FD003) ciclos, k central = 40,8 e 34,1 (faixa de pontos médios 29,1–80,0 e 24,3–66,7; extremos 19,4–92,1 e 16,2–76,9). O limite de LLP (AC 33.70-1: vida aprovada obrigatória em ciclos de voo, rastreada por motor e peça) foi modelado como contador independente de 20.000 EFC (central), 25.000 e 30.000. Restaurações reais são parciais (margem restaurada ≈70–80%, segunda corrida ≈80% da primeira); a hipótese AGAN é uma simplificação, e ρ=0,8 foi incluído como sensibilidade. Classe de empuxo: C-MAPSS 90.000 lb versus 19.500–33.000 lb nas fontes. A faixa de k reflete incerteza de escala, não precisão.

## Validação do simulador

- Estado estacionário (sem LLP, ρ=1, IC1): média de visitas = H·taxa/k em 2.880 células, |z| máximo 3,94 (limite predeclarado 4; o máximo está próximo do limite, esperado para 2.880 testes com |z|~N(0,1)).
- Horizonte longo (2×10⁶ FC), IC0 e IC1: erro relativo máximo 0,26% (limite 1%).
- Visitas forçadas por LLP idênticas entre as 16 regras em todas as células (diferença 0).

## Cenário central (L_ref=8.425, 1.600 FC/ano, LLP 20.000 EFC, frota madura, ρ=1,0, prazo 1)

H = 32.000 FC = 784 ciclos simulados (FD001) e 939 (FD003). Visitas por posição em 20 anos (média das três repetições), das quais 1,60 são forçadas por LLP e **iguais em todas as regras**:

| Regra | FD001 | FD003 | Eventos de endpoint por posição (FD001 / FD003)* |
|---|---:|---:|---|
| Idade fixa | 6,64 | 7,25 | 0,09 ausência / 0,09 ausência |
| Marco HI | 5,54 | 5,44 | 0 |
| ISO inferior 98%/reserva 15 | 5,51 | 5,43 | 0 |
| RF_SLOPE inferior 98%/reserva 15 | 5,52 | 5,43 | 0 |
| Limiar HI selecionado | 5,14 | 5,21 | 0,03 ausência / 0,05 ausência + 0,02 exata |
| Espera HI selecionada | 5,26 | 5,27 | 0,02 exata / 0,01 ausência |
| ISO central (ponto) reserva 15 | 4,93 | 4,95 | 0,26 ausência + 0,13 exata / 0,44 + 0,06 |

\* Soma dos eventos de endpoint em vidas encerradas por degradação, por posição em 20 anos.

Redução de visitas frente à idade fixa: ISO inferior 98% 17,0% (FD001) e 25,1% (FD003). Custo ilustrativo a US$ 6 milhões por visita: ISO US$ 33,1/32,6 milhões por posição contra idade US$ 39,8/43,5 milhões. Esses números dependem integralmente de k, u, LLP, do custo igual para visita por LLP e por degradação, e de lives renovadas iid dos 100 motores E. Não são previsão de gasto de companhia. Quando a visita por LLP não é um custo comparável (substituição de LLP custa mais, mas é comum a todas as regras), a economia relativa muda; a diferença absoluta entre regras não.

## Sensibilidade: o que muda e o que não muda

- **Sem LLP, frota madura (IC1)**: a redução frente à idade é constante em k (FD001 21,3–22,3%, FD003 29,0–29,8% em toda a grade), igual à taxa analítica de P12.1. O fator k não altera a ordenação nem a razão entre regras nesse caso: apenas escala o número de visitas.
- **LLP**: a visita forçada reinicia a degradação e interrompe vidas longas. A redução frente à idade cai para 9,9–20,6% (FD001) e 15,6–27,4% (FD003) com LLP 20.000 e frota madura, mais baixa e mais dispersa entre repetições nos maiores L_ref. LLP de 25.000–30.000 reduz esse efeito. A contagem de visitas forçadas é a mesma entre regras, mas elas truncam vidas por degradação de forma diferente.
- **Condição inicial**: com motor novo (IC0) e sem LLP, o total é 5% menor que o estacionário para L_ref=4.000 (razão de borda 0,95), 10% menor para o L_ref central (0,90) e 21–24% menor para L_ref=19.000 (0,76–0,79), porque o primeiro intervalo ainda não terminou no horizonte. O efeito de borda não é corrigido; é reportado.
- **Restauração parcial (ρ=0,8)**: aumenta o número de visitas em todas as regras e muda pouco a ordenação (τ de Kendall médio 0,985 contra 0,980 com ρ=1).
- **Custo (US$ 5/6/7 milhões)**: com custo fixo comum, escala os valores e **não altera a ordenação**.
- **Utilização (1.400/1.600/1.900 FC/ano)**: efeito pequeno sobre a estabilidade (fração estável do par ISO vs marco HI 79–81%).

## Estabilidade da ordenação

Ordenação das 16 regras por visitas totais frente à ordenação analítica: τ de Kendall médio 0,98 (mínimo 0,81), 0,993 para k<30 e 0,960 para k>80 (mínimos 0,81 na faixa 50–80 e 0,84 acima de 80, onde o horizonte contém poucas vidas). Pares pré-declarados (7 pares × 2 prazos × 2.880 células), classificados por diferença média ≥ 2 EP das réplicas (variabilidade do processo para os 100 motores, não incerteza de população):

| Par | Estável | Indistinguível | Invertido |
|---|---:|---:|---:|
| ISO inferior 98% vs idade | 5.759 | 1 | 0 |
| Marco HI vs idade | 5.758 | 2 | 0 |
| Limiar HI selecionado vs marco HI | 5.760 | 0 | 0 |
| Espera HI selecionada vs marco HI | 5.760 | 0 | 0 |
| ISO central (ponto) vs ISO inferior 98% | 5.760 | 0 | 0 |
| **ISO inferior 98% vs marco HI** | **4.615** | **1.145** | 0 |
| **RF_SLOPE inferior 98% vs ISO inferior 98%** | **3.255** | **2.407** | **98** |

- Quatro das sete comparações são estáveis em praticamente todas as condições; a ordenação entre idade, marco HI e regras selecionadas não depende de k, utilização, LLP, condição inicial ou ρ. **Estabilidade de sinal não é relevância**: ISO inferior 98% vs marco HI tem efeito de −0,53% (FD001) e −0,25% (FD003) nas visitas totais, no máximo −2,3%, e fica indistinguível em 36% das células do FD003 (3,4% no FD001), mais quando há LLP 20.000 (22,4% de células indistinguíveis contra 18,0% sem LLP). Concordante com P11.1.
- ISO vs RF_SLOPE: diferença analítica de ordem 10⁻⁵ por ciclo simulado (≤1,7×10⁻⁵), praticamente nula. As 98 "inversões" ocorrem onde o sinal analítico não tem sentido prático; concentram-se em motor novo (IC0) com LLP 20.000 (43 de 98), em k alto (taxa de inversão 9% para k>80) e em horizontes curtos.
- As regras selecionadas e centrais de ponto ordenam-se como no analítico, mas as economias vêm acompanhadas de ausências e chegadas exatas ao endpoint (tabela do cenário central), e o resultado de admissibilidade de P13.1 e P11 vale para essas contagens, sem prova de risco ≤2%.

## Condições em que a ordenação permanece estável

Entre idade, marco HI, regras de limite inferior 98% e regras selecionadas/centrais: estável (sinal) em todas as combinações simuladas. Entre marco HI e ISO/RF inferior 98%: sinal estável apenas parcialmente e magnitude pequena em qualquer combinação. Nada na grade torna uma região de k "correta"; a ordenação é estável porque depende da taxa por ciclo simulado, que k não altera.

## Limitações e hipóteses não validadas

- k, L_ref e a leitura "intervalo de remoção ≙ vida até o endpoint" são hipóteses; o motor C-MAPSS é de classe de empuxo diferente e as fontes são especializadas, não dados abertos.
- Visita por LLP renova toda a degradação e custa o mesmo que visita por degradação; não há fusão com remoções próximas ao limite de LLP. Aposentadoria do motor não modelada.
- Vidas renovadas iid por reposição dos 100 motores E (não são motores independentes entre repetições). Sem receita, disponibilidade, spares, demanda ou margem; sem inspeção.
- Os EP medem variabilidade do processo de 20 anos para esses 100 motores, não incerteza de população; a incerteza sobre os motores está nos intervalos bootstrap de P12.1.

## Verificação

Dez testes passaram antes da execução; o primeiro registro mostrou uma falha por erro do próprio teste (horizonte de 1 FC curto demais para observar a visita forçada); o horizonte do teste foi corrigido para 30 FC, o log inicial original foi sobrescrito por engano ao copiar o log corrigido e foi **recriado** reexecutando a versão original do teste (`experiments/p12b_tests_initial.log`, com nota no cabeçalho); a falha reproduzida é a mesma. Sem efeito sobre a execução. O verificador independente reimplementou o simulador por laços por réplica para 32 células estratificadas (todos os níveis de LLP, IC e ρ), 96 pares regra-célula e 64 contrastes, com médias e desvios idênticos a 10⁻⁹; refez os sinais analíticos a partir das colunas brutas, 5 valores de τ com implementação própria, o invariante de LLP e o teste estacionário (|z| máximo 3,94), e confirmou os manifestos anteriores. Sem emendas científicas.
