# P15.3 — política PHM → idade com as idades conservadoras de P15.2

## Resultado e alcance

Com as idades autorizadas pelo autor (**127 ciclos no FD001 e 144 no FD003**), a política candidata PHM → idade (M27) se comporta, na prática, como a própria regra de idade. A política continua candidata, sem crédito nem validação de segurança, e o fallback é o testado em P15.1 (idade atua se o PHM ainda não decidiu quando a idade é atingida; decisão em A − d, retirada em A). Fallback por indisponibilidade do monitoramento não foi simulado. Exploratório, sem inspeção, sobre as regras congeladas de P13.1 e motores E já examinados.

## Resultado principal (média das três repetições, prazo 1; vida em ciclos simulados)

| Regra PHM base | Idade atua (FD001 / FD003) | Vida com a política FD001 | FD003 | Vida da regra PHM original FD001 | FD003 |
|---|---|---:|---:|---:|---:|
| ISO inferior 98%/reserva 15 | 89% / 88% | 126,4 | 142,6 | 168,2 | 208,2 |
| RF_SLOPE inferior 98%/reserva 15 | 89% / 87% | 126,3 | 142,6 | 168,0 | 208,1 |
| Marco HI | 89% / 87% | 126,3 | 142,6 | 167,3 | 207,7 |
| Limiar HI selecionado | 97% / 93% | 126,9 | 143,5 | 182,1 | 218,8 |
| Espera HI selecionada | 97% / 92% | 126,9 | 143,4 | 177,1 | 215,9 |
| ISO ponto central | 99% / 97% | 127,0 | 143,9 | 192,1 | 233,0 |

- **A idade decide a retirada em 87–99% dos motores.** O PHM só chega primeiro em 1–13% deles. A vida média fica em 126–127 (FD001) e 143–144 (FD003), muito abaixo da vida do PHM original (167–233).
- **Economia de restauração** frente ao controle de idade de P13.1 (idade das partições, vida média 132,0 e 146,7): de −4,5% a −3,9% no FD001 e de −2,9% a −1,9% no FD003. Ela é negativa porque as novas idades (127 e 144) são menores que as idades de desenvolvimento por partição. Frente ao marco HI, a perda é de cerca de 32% (FD001) e 44–46% (FD003).
- **Cenário central de 20 anos** (P12.2: L_ref 8.425, 1.600 voos/ano, prazo 1; visitas por posição): FD001 6,17–6,20 sem LLP e 6,77–6,80 com LLP 20.000; FD003 6,52–6,58 e 7,58–7,62. A idade fixa de P12.2 tinha 6,64 e 7,25 (com LLP). Os números dependem integralmente de k, utilização e LLP.

## Advertência de origem (zero eventos por construção)

As idades são o mínimo menos um dos 100 motores de cada conjunto, **inclusive os motores E avaliados**. Todos os motores têm T > A − d, de modo que a regra de idade sempre decide antes do endpoint. **Zero ausências, chegadas exatas e ultrapassagens em todas as 84 combinações (regra × prazo × repetição × conjunto) é consequência da construção, não evidência de segurança.** Isso vale para as regras de ponto central, que tinham 23 ausências e 11 chegadas exatas em 300 vidas (FD001), agora sem eventos pelo mesmo motivo. O valor informativo desta rodada é o custo: a vida cedida.

## O que isso significa para a decisão da política

- Com idades tão conservadoras, a política candidata **perde quase todo o ganho de vida do PHM** e se reduz a uma regra de idade. O PHM só atua nos motores que o sinal condena antes de 127 ou 144 ciclos,.
- O resultado vale para a semântica "idade vencida". Se o fallback for por **indisponibilidade do monitoramento** (o caso descrito no IP 180), o PHM decidiria normalmente e a idade só atuaria nos motores sem dados válidos na janela de decisão. Para simulá-lo é preciso especificar um modelo de perda de dados (probabilidade e duração das interrupções, e se uma interrupção cobre a janela de decisão). Não há valor definido pelo autor, e nenhum foi adotado.

## Verificação

Quatro testes passaram antes da execução (idades iguais às de P15.2, nenhum motor E com T ≤ A − d, decisão em todos, entradas restritas). Na primeira execução a função de referências de P15.1 falhou por esperar o quantil 0 de P15.1; foi substituída por uma função local equivalente, sem alterar P15.1. O verificador independente reconstruiu 8.400 linhas híbridas por laços das colunas brutas, os 84 resumos e conferiu os manifestos anteriores. Sem emendas científicas.
