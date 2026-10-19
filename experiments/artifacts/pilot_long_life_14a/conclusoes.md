# P14.1 — instabilidade e eventos adversos por vida do motor

## Resultado

Classificação predefinida: **concentração parcial**. No FD003, os dois requisitos foram cumpridos. No FD001, houve enriquecimento na cauda longa, mas o intervalo da correlação de postos entre vida e amplitude do marco incluiu zero. Nenhum ajuste novo; somente artefatos M18 arquivados e arquivos train FD001/FD003. FD002/FD004 não foram lidos.

| Domínio | Spearman(T, amplitude do marco) [IC 95%] | Motores com amplitude >10 | Desses, na cauda longa (T ≥ q0,90) | Enriquecimento | Fração da amplitude excedente na cauda |
|---|---|---:|---:|---:|---:|
| FD001 | 0,171 [−0,029; 0,360] | 5 | 2 | 4,0 | 0,73 |
| FD003 | 0,283 [0,086; 0,457] | 29 | 7 | 2,4 | 0,77 |

Cortes da cauda longa: T ≥ 275,1 (FD001) e T ≥ 351,5 (FD003), dez motores em cada domínio. Com cinco motores largos no FD001, as frações são instáveis.

As datas de decisão ISO inferior 98%/reserva 15 tiveram associação positiva com intervalos acima de zero nos dois domínios (FD001 0,308 [0,123; 0,476] em prazo 1; FD003 0,334 [0,153; 0,501]).

## Qualificações

- **A instabilidade é aproximadamente proporcional à vida, não desproporcional.** A amplitude relativa (amplitude/T) não se associou à vida em nenhuma quantidade (Spearman −0,12 a 0,02, intervalos incluindo zero). Motores longos têm amplitudes absolutas maiores porque vivem mais; não há evidência de comportamento qualitativamente distinto.
- **A leitura pela idade observável é mais fraca.** Spearman entre o menor marco entre repetições e a amplitude: 0,13 [−0,09; 0,32] no FD001 e 0,19 [−0,02; 0,38] no FD003 para o marco. Um limite de vida atua pela idade.
- **Os casos extremos não estão todos na cauda.** FD003 motores 55 (T 525, amplitude 212) e 71 (409, 185) estão na cauda longa, mas o motor 42 (193, 60) é curto. No motor 55, o marco mais cedo ocorre no ciclo 239: um limite de vida só truncaria as datas tardias, sem eliminar a amplitude.
- **Os eventos de endpoint concentram-se nos motores curtos, não nos longos.** Por terço de vida, linhas com evento na cadeia M18 de P13.5: FD001 54/40/17 (curta/média/longa) e FD003 76/15/29. O padrão é o mesmo em P11 e P13.1. A exceção conhecida é o FD003 motor 10 (481 ciclos) na cadeia SEL arquivada. Esta medida é descritiva: a contagem exploratória foi vista antes do protocolo.

## Consequência

Um limite de vida para remoção obrigatória tem motivação empírica parcial: reduziria a amplitude absoluta das datas nos motores mais longos, que respondem por cerca de três quartos da amplitude excedente. Não estabiliza o HI, não atua sobre o motor 42 nem sobre o início precoce da amplitude do motor 55, e não trata o risco de endpoint, que se concentra nos motores curtos. Esses são dois problemas distintos:

1. **Estabilidade das datas em vidas longas** — tratável por limite de vida, se especificado em P14.2.
2. **Risco de endpoint em vidas curtas** — permanece com reserva/quantil e precisa ser declarado; um limite de vida não o reduz.

Nenhuma exclusão de motores é sustentada por este resultado. M18, reservas, níveis e regras não mudam. O valor do limite não foi escolhido; deverá vir de fonte operacional ou de regra sobre as vidas dos motores de desenvolvimento, fixada antes da avaliação, e aplicar-se igualmente aos três braços.

## Verificação

Seis testes passaram antes da execução (`experiments/p14a_tests.log`). O verificador independente obteve T pela coluna `endpoint` arquivada, recompôs as amplitudes a partir das decisões por repetição, refez correlações e intervalos com implementação própria de postos (mesma sequência aleatória), enriquecimentos e frações, e recontou 213 linhas de eventos por `status`, sem usar as colunas booleanas. Manifestos anteriores íntegros. Sem emendas.
