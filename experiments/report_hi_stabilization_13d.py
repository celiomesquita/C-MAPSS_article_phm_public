"""Report the preregistered P13.4 comparison, retaining adverse tails."""
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pilot_f_uncertainty_10 as p10

OUT=p10.ROOT/'experiments/artifacts/pilot_hi_stabilization_13d'


def main():
    assert json.loads((OUT/'verification.json').read_text())['passed']
    assert json.loads((OUT/'final_fit_verification.json').read_text())['passed']
    metrics=pd.read_csv(OUT/'internal_metrics.csv');choices=pd.read_csv(OUT/'selections.csv')
    chosen=metrics.merge(choices[['subset','repeat','fold','selected','selection_eligible']],on=['subset','repeat','fold'])
    chosen=chosen.loc[chosen.candidate.eq(chosen.selected)]
    pairs=chosen.merge(metrics.loc[metrics.candidate.eq('M18')],on=['subset','repeat','fold'],suffixes=('_selected','_baseline'))
    pairs['mse_ratio']=pairs.mse_selected/pairs.mse_baseline
    pairs['max_tail_worsened']=pairs.max_abs_selected>pairs.max_abs_baseline
    pairs['life_delta_d1']=pairs.mean_life_d1_selected-pairs.mean_life_d1_baseline
    pairs.to_csv(OUT/'selected_vs_m18.csv',index=False)
    frequency=choices.groupby(['subset','selected']).size().rename('partitions').reset_index()
    frequency.to_csv(OUT/'selection_frequency.csv',index=False)
    summary=[]
    for subset,g in pairs.groupby('subset'):
        summary.append(dict(subset=subset,partitions=len(g),eligible_choices=int(g.selection_eligible.sum()),
                    median_p95_m18=g.p95_abs_baseline.median(),median_p95_selected=g.p95_abs_selected.median(),
                    median_mean_abs_m18=g.mean_abs_baseline.median(),median_mean_abs_selected=g.mean_abs_selected.median(),
                    largest_max_m18=g.max_abs_baseline.max(),largest_max_selected=g.max_abs_selected.max(),
                    maximum_tail_worsened_partitions=int(g.max_tail_worsened.sum()),median_mse_ratio=g.mse_ratio.median(),
                    min_mse_ratio=g.mse_ratio.min(),max_mse_ratio=g.mse_ratio.max(),
                    min_mean_life_delta=g.life_delta_d1.min(),median_mean_life_delta=g.life_delta_d1.median(),
                    max_mean_life_delta=g.life_delta_d1.max(),baseline_decisions=int(g.decisions_baseline.sum()),
                    selected_decisions=int(g.decisions_selected.sum()),selected_reached_d1=int(g.reached_d1_selected.sum()),
                    selected_reached_d2=int(g.reached_d2_selected.sum()),selected_late_d1=int(g.late_d1_selected.sum()),
                    selected_late_d2=int(g.late_d2_selected.sum()),selected_loo_missing=int(g.loo_missing_selected.sum())))
    summary=pd.DataFrame(summary);summary.to_csv(OUT/'summary.csv',index=False)
    fig,axes=plt.subplots(2,2,figsize=(10,8))
    colors={'M18':'black','NNLS_01':'tab:blue','NNLS_1':'tab:cyan','SIGNED_01':'tab:orange','SIGNED_1':'tab:red'}
    for col,subset in enumerate(['FD001','FD003']):
        g=pairs.loc[pairs.subset.eq(subset)]
        for row,metric in enumerate(['p95_abs','max_abs']):
            ax=axes[row,col]
            limit=max(g[metric+'_baseline'].max(),g[metric+'_selected'].max())*1.05
            ax.plot([0,limit],[0,limit],color='grey',ls='--',lw=1)
            for c,color in colors.items():
                part=g.loc[g.selected.eq(c)]
                ax.scatter(part[metric+'_baseline'],part[metric+'_selected'],s=35,color=color,alpha=.7,label=c)
            ax.set(xlabel='M18 (cycles)',ylabel='Internally selected HI (cycles)',title=f'{subset}: '+('95th percentile' if row==0 else 'Maximum'))
            if row==0 and col==0: ax.legend(fontsize=8)
    fig.suptitle('Leave-one-training-engine-out marker changes; internal validation only')
    fig.tight_layout();fig.savefig(OUT/'stability_comparison.png',dpi=170);plt.close(fig)
    rows='\n'.join(f"| {r.subset} | {r.median_p95_m18:.2f} → {r.median_p95_selected:.2f} | {r.median_mean_abs_m18:.3f} → {r.median_mean_abs_selected:.3f} | {r.largest_max_m18:.0f} → {r.largest_max_selected:.0f} | {r.maximum_tail_worsened_partitions} |" for r in summary.itertuples())
    counts='\n'.join(f'| {r.subset} | {r.selected} | {r.partitions} |' for r in frequency.itertuples())
    check=json.loads((OUT/'verification.json').read_text());final=json.loads((OUT/'final_fit_verification.json').read_text())
    text=f'''# P13.4 — estabilização do HI em desenvolvimento

## Resultado e alcance

A comparação produziu indicações internas mais estáveis segundo o critério previamente fixado, sobretudo em FD003. É um resultado misto: a seleção não protegeu todos os máximos individuais, depende da partição e manteve um caso de referência incompleta. M18 continua sendo o controle de trabalho; nenhuma alternativa foi declarada superior em U/E ou adoptada como política operacional.

| Domínio | Mediana entre partições do p95 absoluto, ciclos | Mediana da média absoluta, ciclos | Maior máximo observado, ciclos | Partições com máximo pior |
|---|---:|---:|---:|---:|
{rows}

Os deslocamentos são do primeiro HI≤0,5 após excluir um motor do ajuste, avaliados em motores V internos. As medianas referem-se às30 partições D40 de cada domínio; o maior máximo é o extremo sobre essas partições. Cada D contém40 motores repetidamente utilizados em diferentes divisões. Não são30 populações independentes ou uma estimativa de risco de falha. O máximo223 de FD003 nesta comparação interna é diferente do213 observado no caso externo de P13.3; não se comparam os dois como antes/depois no mesmo motor.

## Protocolo executado

[Protocolo prévio](../../protocolo_estabilizacao_hi_13d.md): cinco alternativas (M18; não negativa com λ0,1/1; assinada com λ0,1/1),240 dobras internas e31.200 soluções, incluindo o controle duplicado de FD001. Cada dobra interna usaF25/V10, com cinco motores D restantes não usados. Cada exclusão reaprendeu canais, escalas e, quando aplicável, orientação. Calcularam-se12.000 respostas basais e300.000 respostas de exclusão; nenhuma representa um novo motor independente. Leram-se somente os arquivos train; nenhum arquivo RUL/test oficial foi utilizado. Os alvos supervisionados vieram de T−t.

Somente D=F∪C participou da aprendizagem/seleção. U/E não foram pontuados, usados para escolher, ou incluídos nas figuras. Isso não elimina o uso exploratório anterior dos dados do projeto. Após congelar as60 indicações, foram ajustados60 HIs em F25 externo, sem lhes aplicar conversores/quantis antigos. C participou da seleção; seu eventual uso posterior para ajustar conversores será explicitado, sem apresentá-lo como avaliação independente.

## Escolhas internas e compromissos

Elegibilidade exigiu completude basal, chegadas compostas não superiores a M18 em ambos os prazos, MSE basal≤1,05×M18, sem aumento de discordâncias de presença ou ausências após exclusão e p95 não superior. Entre elegíveis e a referência de contingência, minimizaram-se p95, média absoluta, MSE e ordem fixa. Não se acrescentou proteção do máximo depois de observar os resultados.

| Domínio | Variante indicada | Partições, de30 |
|---|---|---:|
{counts}

FD001: a razão MSE indicado/M18 variou0,905–1,049 (mediana0,994). FD003:0,710–1,048 (mediana1,000). Portanto, parte da estabilidade foi aceita com até cerca de5% de perda no alvo de HI, conforme tolerância exploratória prévia; não se trata de margem de engenharia validada. O controle M18/NNLS_01 foi exatamente idêntico em FD001.

A vida média aproveitada pelo controle de remoção no marco, prazo1, mudou−0,375 a+3,375 ciclos em FD001 (mediana+2,425) e−0,850 a+11,275 em FD003 (mediana+1,338), entre D40. São diferenças internas no controle simples de marco, não resultados do conversor RUL, custo de renovação, lucro empresarial ou efeito em20anos.

**Resultado adverso preservado:** o máximo de deslocamento piorou em8/30 partições FD001 e3/30 FD003, mesmo com melhora/empate do p95. Logo, reduzir uma medida agregada não demonstra estabilidade uniforme. O relatório mantém todas as variantes, inclusive as inelegíveis, e o máximo não será usado retrospectivamente para trocar as escolhas já congeladas.

**Contingência não elegível:** FD003/repetição2/dobra2 manteve M18: apenas39/40 decisões basais e uma ausência contabilizada como chegada composta em ambos os prazos. Nenhuma alternativa satisfez os filtros. Essa indicação é diagnóstico/contingência, não um ajuste aprovado. Nas30 partições indicadas FD003 houve1.199/1.200 decisões internas e26 ausências de decisão nas exclusões, com denominadores dependentes. As escolhas FD001 tiveram1.200/1.200 e nenhuma ausência nas exclusões. Não houve ultrapassagem estrita basal nas escolhas, mas isso não certifica o limite populacional≤2%.

## Verificação e rastreabilidade

Sete testes passaram antes da execução: reprodução M18 em ambos os domínios, equivalência ridge com todas as linhas, pesos iguais por motor, separação interna, barreira de erro na escolha, ausência sem imputação e controle duplicado. Os240 ajustes M18 internos foram ainda confrontados com os modelos originais P13.1 durante a execução.

A conferência independente reconstruiu{check['reconstructed_responses']:,} respostas a partir das linhas originais, estatísticas e pesos, refez as300 métricas e60 escolhas e verificou optimalidade das{check['internal_solutions']:,} soluções (violação KKT máxima{check['maximum_kkt']:.3e}). Outra conferência verificou os60 ajustes finais somente em F25, com máximo{final['maximum_kkt']:.3e}, e a integridade dos artefatos anteriores.

O verificador sequencial pré-especificado foi interrompido para substituir a repetição de operações tabulares por uma reconstrução vetorizada independente de mesmo escopo. O código inicial e o log parcial foram preservados; não houve mudança dos critérios científicos, modelos, seleções ou resultados. A versão vetorizada e a conferência adicional dos modelos finais foram acrescentadas depois da execução, antes deste relatório. Manifestos e fontes preservam essa ordem.

## Consequência para o plano

P13.4 conclui esta grade exploratória, com59 indicações elegíveis e uma contingência inelegível. Não expandir a grade até obter estabilidade perfeita. O próximo teste deve avaliar a consequência decisória da seleção interna: reconstruir conversores compatíveis com cada HI indicado, recalibrar em U50 e comparar com M18 sob os mesmos prazos1/2, reserva15 e tolerância experimental de ultrapassagem≤2%, sem escolher novamente em U/E. Definir antes da execução como preservar a contingência inelegível e reportar a cauda agravada. Reserva12 permanece sensibilidade condicionada, não redução autorizada pela estabilidade.

Essa avaliação poderá indicar se a estabilidade interna se transfere para marcos, previsões, remoção e exposição. Não sabemos ainda se o extremo externo do motor55 foi corrigido. Os dados existentes continuam exploratórios; evidência independente de risco e plausibilidade física permanece distinta. Sem inspeções, alteração do artigo ou projeção monetária nesta rodada.

![Comparação de estabilidade e caudas](stability_comparison.png)
'''
    (OUT/'conclusoes.md').write_text(text,encoding='utf-8')
    print('Saved comparison, frequency, figure and report.')


if __name__=='__main__': main()
