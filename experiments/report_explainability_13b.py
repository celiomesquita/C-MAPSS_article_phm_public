"""Readable P13.2 evidence and all prespecified diagnostic case sheets."""
from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pilot_explainability_13b as p


def num(x,digits=2):return f'{x:.{digits}f}' if np.isfinite(x) else 'indefinido'


def main():
    out=p.OUT
    summary=pd.read_csv(out/'action_summary.csv')
    ranks=pd.read_csv(out/'rank_comparisons.csv')
    mech=pd.read_csv(out/'mechanism.csv')
    dates=pd.read_csv(out/'repeat_dates.csv')
    attrs=pd.read_csv(out/'attribution_engines.csv')
    support=pd.read_csv(out/'support.csv')
    inventory=pd.read_csv(out/'case_inventory.csv')
    triggers=pd.read_csv(out/'trigger_explanation.csv')
    decisions=pd.read_csv(p.p13.OUT/'decisions.csv')
    snapshots=pd.read_csv(out/'policy_snapshots.csv.gz')
    lines=['# P13.2 — explicabilidade e estabilidade após o marco', '',
        'HI = índice de saúde; ISO = regressão isotônica; RF = floresta aleatória com HI e inclinação. FD001 é o cenário principal; FD003 é extensão de robustez. Três repetições dos mesmos100 motores por domínio, sem300 motores independentes.', '',
        'Modelos, quantis e políticas congelados. Parâmetros das perturbações aprendidos somente em F25, sem uso de C/U/E. Trata-se de robustez informacional de medições; não valida intervenções físicas, margens operacionais ou risco populacional≤2%.', '',
        '## Reconstrução e fidelidade', '',
        f'9.600 decisões basais reproduzidas. Atribuições assinadas e alocação radial respeitam clipping/cancelamento. Violações do sinal previsto da resposta do HI às perturbações: {int(mech.sign_violations.sum())} em {int(mech.sign_checks.sum())} comparações de sinal. Identidade algébrica não comprova utilidade humana da explicação.', '',
        '## Estabilidade de rankings entre ajustes', '',
        '| Domínio | Ranking | Comparações | Spearman mediano | Mínimo | Top5 compartilhado mediano | Não identificáveis |', '|---|---|---|---|---|---|---|']
    for key,g in ranks.loc[ranks.comparison.eq('between_folds')].groupby(['subset','kind']):
        lines.append(f'| {key[0]} | {key[1]} | {len(g)} | {num(g.spearman.median())} | {num(g.spearman.min())} | {num(g.shared_top5.median(),1)} | {int((~g.identified).sum())} |')
    lines+=['', 'Concordância de ranking e fidelidade são critérios distintos. Correlação indefinida não recebe valor1. Empates na fronteira top5 permanecem identificados em `rank_comparisons.csv`. Pesos globais do HI não são apresentados como importância da retirada. ISO e RF recebem o mesmo HI (com inclinação na RF): concordância de sensores após essa representação não é validação independente de importância física.', '',
        '## Por que a regra conservadora atua cedo?', '',
        'Auditoria no instante da decisão, sem mudar a regra. A correção q é congelada; o limite inferior é max(0, previsão−q). Quando chega a zero, variações locais da previsão podem não alterar esse limite ou o gatilho. O quadro abaixo é descritivo, não uma identificação causal do ganho recuperável.', '',
        '| Domínio | Política | Decisões no marco, faixa entre repetições | Limite inferior zero na decisão, faixa | Previsão central já satisfazia o gatilho, faixa |', '|---|---|---|---|---|']
    tr=triggers.loc[triggers.policy_id.str.contains('LOWER98_M15_D1')]
    for key,x in tr.groupby(['subset','policy_id']):
        z=x.groupby('repeat')[['at_gate','lower_zero','central_would_trigger']].mean()*100
        lines.append(f'| {key[0]} | {key[1]} | {num(z.at_gate.min(),0)}–{num(z.at_gate.max(),0)}% | {num(z.lower_zero.min(),0)}–{num(z.lower_zero.max(),0)}% | {num(z.central_would_trigger.min(),0)}–{num(z.central_would_trigger.max(),0)}% |')
    lines+=['',
        '## Sensibilidade da data programada', '',
        'Contraste abaixo: rampa global, amplitude1, canais perturbados individualmente, prazo1. As médias dão peso igual a direções/sinais dentro de cada motor, depois aos motores; mínimo/máximo entre repetições. Ausências permanecem na análise de presença/eventos e ficam fora somente da distância finita, com denominadores publicados.', '',
        '| Domínio | Política | Média absoluta de Δr (ciclos), faixa entre repetições | Fração de deslocamentos>2, faixa | Mudança de presença, faixa |', '|---|---|---|---|---|']
    selected=summary.loc[summary.phase.eq('global')&summary.kind.eq('channel')&summary.epsilon.eq(1)&summary.policy_id.str.endswith('D1')]
    for key,g in selected.groupby(['subset','policy_id']):
        lines.append(f'| {key[0]} | {key[1]} | {num(g.mean_abs_delta.min())}–{num(g.mean_abs_delta.max())} | {num(100*g.shift_gt2.min())}–{num(100*g.shift_gt2.max())}% | {num(100*g.presence_flip.min())}–{num(100*g.presence_flip.max())}% |')
    lines+=['', 'Demais amplitudes, direções conjuntas, prazo2 e diagnóstico local estão em [action_summary.csv](action_summary.csv); efeitos extremos por motor também estão publicados. Diagnósticos locais alinham a rampa à decisão original de cada política e não representam a mesma intervenção no mesmo instante entre políticas diferentes.', '',
        '## Suporte empírico', '', '| Domínio | Tipo | Fração média de incrementos fora do envelope |', '|---|---|---|']
    sup=support.assign(fraction=support.outside_count/support.increments)
    # Equal weight per engine, then repeat; baseline is never counted once per direction.
    for key,g in sup.groupby(['subset','kind']):
        value=g.groupby(['repeat','unit']).fraction.mean().mean()
        lines.append(f'| {key[0]} | {key[1]} | {100*value:.2f}% |')
    lines+=['', 'O envelope foi estimado nos incrementos iniciais F25; a própria trajetória original pode sair dele durante a degradação. Quantis0,99 por critério não dão cobertura conjunta garantida99%. Resultados no suporte possuem denominadores próprios e não substituem todos os motores. Exigir todo o prefixo dentro do envelope é diagnóstico restritivo, não filtro de segurança.', '',
        '## Estabilidade entre repetições', '', '| Domínio | Mediana de diferença absoluta entre datas | Máximo | Presença discordante |', '|---|---|---|---|']
    for s,g in dates.groupby('subset'):
        lines.append(f'| {s} | {num(g.delta_abs.median())} | {num(g.delta_abs.max())} | {int(g.presence_discordant.sum())}/{len(g)} pares motor/política |')
    lines+=['', 'Esses pares reutilizam os mesmos motores e modelos com treino parcialmente compartilhado; não são novas unidades independentes. Perfis de contribuição são comparados na interseção de instantes disponíveis em cada par, em `repeat_contributions.csv`.', '',
        '## Artefatos e limites', '',
        '[Contrastes pareados de datas/presença](action_contrasts.csv), [contrastes ISO/RF](forecast_contrasts.csv), [verificação](verification.json), [verificação das estatísticas](summary_verification.json), [protocolo](../../protocolo_explicabilidade_13b.md) e [convenções anteriores à execução](../../protocolo_explicabilidade_13b_implementacao.md). Bootstrap descritivo de2.000 amostras por motor/domínio/repetição, condicional aos modelos; sem selecionar o melhor explicador ou regra por intervalos.', '',
        'P11.2 localizou a distância ao oráculo após o marco; P13.2 testa se essa cadeia é auditável e estável. Nenhuma resposta de sensibilidade prova que a distância possa ser recuperada com segurança. Não houve inspeção, mudança do HI ou artigo, nova política ou projeção monetária.', '',
        '## Fichas retrospectivas de todos os casos especificados', '']
    # All adverse cases plus the specified extrema/median; each selected engine displays all repeats.
    cache={}
    for split in json.loads((p.p10.OUT/'splits.json').read_text()):
        s,rep,f=split['subset'],split['repeat'],split['fold']
        b=np.load(out/f'baseline_{s}_r{rep}_f{f}.npz')
        for unit in split['evaluation']:
            m=b['unit']==unit
            cache[(s,rep,unit)]={k:b[k][m] for k in ['cycle','C','H','ISO','RF']}
    case_rows=[]
    for (s,unit),reasons in inventory.groupby(['subset','unit'],sort=True):
        unit=int(unit);name=f'case_{s}_u{unit}'
        fig,axes=plt.subplots(2,3,figsize=(14,6),layout='constrained')
        card=[f'# {s}, motor{unit} — diagnóstico retrospectivo', '',
              'Critérios de inclusão: '+', '.join(sorted(reasons.reason.unique()))+'.', '',
              'As três repetições reutilizam este motor. Linha T/vida real é diagnóstico posterior, nunca entrada da previsão. O gráfico usa prazo1; as tabelas incluem os dois prazos. Não há atribuição física a fan/HPC ou conformidade normativa demonstrada.', '',
              f'![Trajetórias e referências](case_{s}_u{unit}.png)', '',
              '| Repetição | Política | Decisão | Remoção | Estado | HI no corte | Previsão | Valor usado no gatilho | Três maiores contribuições absolutas no corte |',
              '|---|---|---|---|---|---|---|---|---|']
        for rep in [1,2,3]:
            b=cache[(s,rep,unit)];t=b['cycle'];pop=decisions.loc[decisions.subset.eq(s)&decisions.repeat.eq(rep)&decisions.unit.eq(unit)]
            end=int(pop.endpoint.iloc[0]);top,bottom=axes[0,rep-1],axes[1,rep-1]
            top.plot(t,b['H'],label='HI');top.axhline(.5,color='grey',ls=':');top.axvline(end,color='black',ls='--',label='T retrospectivo')
            top.set(title=f'Repetição{rep}',ylabel='HI');top.set_ylim(-.05,1.05)
            for method,label,color in [('ISO','ISO','#4477aa'),('RF_SLOPE','RF','#cc6677')]:
                q=float(pop.loc[pop.policy_id.eq(f'{method}_LOWER98_M15_D1'),'q_late'].iloc[0])
                values=b['ISO'] if method=='ISO' else b['RF']
                bottom.plot(t,values,label=label,color=color,alpha=.55)
                bottom.plot(t,np.maximum(0,values-q),label=label+' inferior98',color=color,ls='--')
            bottom.axhline(16,color='black',ls=':',label='Gatilho m+d=16')
            bottom.set(xlabel='Ciclo',ylabel='Vida prevista/limite (ciclos)')
            for r in pop.itertuples():
                cutoff=int(r.decision) if r.has_decision else end-1
                j=int(np.flatnonzero(t==cutoff)[0])
                indices=sorted(range(21),key=lambda k:(-abs(b['C'][j,k]),k))[:3]
                sensors=', '.join(f'{p.core.SENSORS[k]}:{b["C"][j,k]:+.3f}' for k in indices)
                chosen=snapshots.loc[snapshots.subset.eq(s)&snapshots.repeat.eq(rep)&snapshots.unit.eq(unit)&snapshots.policy_id.eq(r.policy_id)&snapshots.cycle.eq(cutoff)]
                z=chosen.iloc[0] if len(chosen) else None
                forecast=b['ISO'][j] if r.method=='ISO' else b['RF'][j] if r.method=='RF_SLOPE' else np.nan
                lower=max(0.,forecast-r.q_late) if np.isfinite(forecast) else np.nan
                state=r.status+('/escolha interna inviável' if r.selection_feasible==False else '')
                card.append(f'| {rep} | {r.policy_id} | {num(r.decision,0)} | {num(r.scheduled,0)} | {state} | {num(b["H"][j],3)} | {num(forecast)} | {num(lower)} | {sensors} |')
                case_rows.append(dict(subset=s,unit=unit,repeat=rep,policy_id=r.policy_id,cutoff=cutoff,
                    decision=r.decision,scheduled=r.scheduled,state=state,hi=b['H'][j],prediction=forecast,lower=lower,top3=sensors))
            top.grid(alpha=.2);bottom.grid(alpha=.2)
        axes[0,0].legend(fontsize=7);axes[1,0].legend(fontsize=6)
        fig.savefig(out/f'{name}.png',dpi=110);plt.close(fig)
        card+=['', 'Tarefa PHM candidata: monitorar somente sensores, preservar referência e disponibilidade; aplicar o gatilho da política congelada e executar no prazo1/2, encerrando o monitoramento para decisão nesse acionamento. O controle por idade usa apenas a contagem de ciclos. Limiar/espera escolhidos pertencem à partição; o quadro de escolhas P13.1 permanece a fonte. Aplicabilidade, criticidade, evidência IP-180/ARP7122 e contingências exigem validação própria.', '']
        (out/f'{name}.md').write_text('\n'.join(card),encoding='utf-8')
        lines.append(f'- [{s}, motor{unit}]({name}.md)')
    pd.DataFrame(case_rows).to_csv(out/'case_sheets.csv',index=False)
    (out/'relatorio.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    # A compact profile plot keeps all sensors; no optimistic channel selection.
    fig,axes=plt.subplots(1,2,figsize=(12,4),layout='constrained')
    for ax,(s,x) in zip(axes,attrs.groupby('subset')):
        profile=x.groupby(['repeat','sensor']).mean_abs.mean().unstack('repeat').reindex(p.core.SENSORS)
        mean=profile.mean(axis=1).to_numpy();lo=mean-profile.min(axis=1);hi=profile.max(axis=1)-mean
        ax.bar(range(21),mean,yerr=np.vstack([lo,hi]),capsize=2)
        ax.set_xticks(range(21),p.core.SENSORS,rotation=70);ax.set(title=s,ylabel='Contribuição absoluta média ao HI')
    fig.suptitle('Peso igual por motor; segmentos = faixa entre três repetições, não intervalos de confiança',fontsize=9)
    fig.savefig(out/'sensor_profiles.png',dpi=160);plt.close(fig)
    (out/'report_metadata.json').write_text(json.dumps(dict(case_engines=len(inventory[['subset','unit']].drop_duplicates()),
        case_sheet_rows=len(case_rows),source_sha256=p.p11.sha(p.ROOT/'experiments/report_explainability_13b.py')),indent=2))
    # Seal the combined manifest only after both independent audits complete.


if __name__=='__main__':main()
