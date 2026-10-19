"""P11.2 evidence tables and exportable figures, with risk beside cost."""
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pilot_loss_decomposition_11b as p


def main():
    s=pd.read_csv(p.OUT/'summary.csv')
    a=pd.read_csv(p.OUT/'availability.csv')
    g=s.loc[s.scope.eq('all')]
    lines=['# P11.2 — decomposição da perda', '',
           'FD001 principal e FD003 robustez; três repetições de100 motores por domínio, reutilizados entre repetições. Modelos e políticas congelados, sem seleção em U/E. O oráculo conhece o endpoint: é referência diagnóstica, não política implementável.', '',
           'O = informação desde o início; G = informação após primeira passagem HI≤0,5; A = informação após disponibilidade ≥39; real = política arquivada. A parcela posterior inclui previsão, quantil e regra, não apenas erro de prognóstico.', '',
           '## Disponibilidade', '', '| Domínio | Repetição | T−G mínimo | T−A mínimo | T−A mediano | Aquecimento máximo |', '|---|---|---|---|---|---|']
    for key,x in a.groupby(['subset','repeat']):
        lines.append(f'| {key[0]} | {key[1]} | {x.crossing_lead.min():g} | {x.available_lead.min():g} | {x.available_lead.median():g} | {x.warmup.max():g} |')
    lines+=['', '## Contraste principal: remoção ideal em T−1', '',
            'Perda de planejamento por detecção/disponibilidade: zero em todas as repetições. As datas dos oráculos O/G/A coincidem neste contraste. Perda posterior pode coexistir com remoção excessivamente antecipada; vida e custo são necessários para identificá-la.', '',
            '| Domínio | Repetição | Política | Vida não aproveitada | Excesso frente a O (ciclos) | Excesso de custo frente a O (%) | Chegadas/100 | Tardias | Ausências |', '|---|---|---|---|---|---|---|---|---|']
    for r in g.loc[g.rho.eq(1)].itertuples():
        lines.append(f'| {r.subset} | {r.repeat} | {r.policy_id} | {r.real_W:.2f} | {r.W_post:.2f} | {100*r.relative_cost_total:.2f} | {r.real_reached_count} | {r.real_late_count} | {r.real_missing_count} |')
    lines+=['', '## Antecedências diagnósticas de12/15 ciclos', '',
            'Não alteram a reserva, o prazo de execução ou a política real. A parcela de detecção é comum às políticas com o mesmo acesso; idade é apenas contextual. As parcelas abaixo são proporções de motores (não percentuais do ganho sobre idade).', '',
            '| Domínio | Repetição | d | ρ | Perda por sinal tardio | Perda por aquecimento | Atraso médio por acesso (ciclos) | A≤D /100 |', '|---|---|---|---|---|---|---|---|']
    for r in g.loc[g.policy_id.str.startswith('HI_MARKER') & g.rho.ne(1)].itertuples():
        feasible=s.loc[s.subset.eq(r.subset)&s.repeat.eq(r.repeat)&s.policy_id.eq(r.policy_id)&s.rho.eq(r.rho)&s.scope.eq('feasible_access')].iloc[0]
        lines.append(f'| {r.subset} | {r.repeat} | {r.delay} | {r.rho} | {100*r.J_crossing:.1f}% | {100*r.J_warmup:.1f}% | {r.B_det:.2f} | {feasible.total} |')
    lines+=['', '![Descarte adicional frente ao oráculo](excess_unused_life.png)', '',
            'Barras: média das três repetições; segmentos: mínimo/máximo entre repetições, não intervalos de confiança. Limiar/espera selecionados têm eventos/ausências em alguns contrastes; menor descarte não significa maior admissibilidade.', '',
            '![Perda de oportunidade por acesso tardio](access_loss.png)', '',
            'As decomposições completas de oportunidade perdida J, atraso B, vida descartada W, custo e respectivos intervalos estão em [summary.csv](summary.csv). O escopo `feasible_access` é diagnóstico condicionado a A≤D, com contagem de excluídos; não substitui a população completa ou sustenta inferência de risco.', '',
            '## Limites', '',
            'Zero eventos observados não demonstra risco populacional ≤2%. Não há penalidade corretiva adicional; parcelas econômicas assinadas são preservadas. Um braço com ausência/chegada não se torna admissível por apresentar menor custo. As quatro escolhas P13.1 sem candidato interno viável continuam identificadas. O bootstrap de2.000 amostras é pareado por motor/domínio/repetição, condicionado aos modelos/seleções, sem reaprendizagem.', '',
            '[Protocolo](../../protocolo_decomposicao_perda_11b.md), [verificação independente](verification.json), [componentes individuais](components.csv), [diagnósticos de previsão](diagnostics.csv) e [manifesto](manifest.json).', '']
    (p.OUT/'relatorio.md').write_text('\n'.join(lines),encoding='utf-8')
    methods=['HI_MARKER_D1','ISO_LOWER98_M15_D1','RF_SLOPE_LOWER98_M15_D1','HI_THRESHOLD_SELECTED_D1','HI_WAIT_SELECTED_D1']
    labels=['Marco HI','ISO inferior98','RF inferior98','Limiar escolhido*','Espera escolhida*']
    fig,axes=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
    fig.suptitle('ρ=1; média e faixa das três repetições (não intervalos de confiança)\n*Regras selecionadas apresentam eventos/ausências em alguns contrastes',fontsize=9)
    for ax,(subset,x) in zip(axes,g.loc[g.rho.eq(1)&g.policy_id.isin(methods)].groupby('subset')):
        for k,policy in enumerate(methods):
            y=x.loc[x.policy_id.eq(policy),'W_post'].to_numpy()
            ax.bar(k,y.mean(),color='#4477aa')
            ax.errorbar(k,y.mean(),yerr=[[y.mean()-y.min()],[y.max()-y.mean()]],fmt='none',ecolor='black',capsize=4)
        ax.set(title=subset+' — prazo 1 ciclo',ylabel='Excesso médio de vida descartada\nfrente ao oráculo (ciclos)')
        ax.set_xticks(range(len(labels)),labels,rotation=25,ha='right')
        ax.grid(axis='y',alpha=.2)
    fig.savefig(p.OUT/'excess_unused_life.png',dpi=160);plt.close(fig)
    fig,axes=plt.subplots(1,2,figsize=(10,4),layout='constrained')
    for ax,(subset,x) in zip(axes,g.loc[g.policy_id.eq('HI_MARKER_D1')].groupby('subset')):
        for repeat,y in x.groupby('repeat'):
            y=y.sort_values('rho')
            ax.plot(y.rho,100*y.J_det,'o-',label=f'Repetição {repeat}')
        ax.set(title=subset+' — prazo 1 ciclo',xlabel='Antecedência-alvo da remoção ρ (ciclos)',ylabel='Oportunidades perdidas por acesso tardio (%)')
        ax.set_xticks([1,12,15]);ax.grid(alpha=.2);ax.legend(fontsize=8)
    fig.savefig(p.OUT/'access_loss.png',dpi=160);plt.close(fig)
    (p.OUT/'report_sources.json').write_text(json.dumps({name:p.p11.sha(p.ROOT/'experiments'/name)
        for name in ['report_pilot_loss_decomposition_11b.py']},indent=2),encoding='utf-8')
    p.refresh_manifest()
    print(g.loc[g.rho.eq(1)&g.policy_id.isin(methods)].groupby(['subset','policy_id'])[['W_post','relative_cost_total','real_reached_count']].agg(['min','max']).to_string())
    print(g.loc[g.policy_id.str.startswith('HI_MARKER')].groupby(['subset','rho'])[['J_det','B_det','J_crossing','J_warmup']].agg(['min','max']).to_string())


if __name__=='__main__':
    main()
