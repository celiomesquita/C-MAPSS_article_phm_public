"""Generate transparent P13.1 tables and a lifetime/risk figure."""
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pilot_policy_selection_13a as p


def main():
    summary = pd.read_csv(p.OUT/'summary.csv')
    decisions = pd.read_csv(p.OUT/'decisions.csv')
    selections = pd.read_csv(p.OUT/'selections.csv')
    rows = []
    for r in summary.itertuples():
        g = decisions.loc[decisions.subset.eq(r.subset) & decisions.repeat.eq(r.repeat) & decisions.policy_id.eq(r.policy_id)]
        rows.append(dict(subset=r.subset, repeat=r.repeat, policy=r.policy_id, mean_life=r.mean_utilised,
                         endpoint_events=int(g.reached_endpoint.sum()), strict_late=int(g.late.sum()),
                         exact=int(g.exact_endpoint.sum()), missing=int((~g.has_decision).sum()), cost=r.cost_per_cycle))
    table = pd.DataFrame(rows)
    table.to_csv(p.OUT/'comparison.csv', index=False)
    lines = ['# P13.1 — seleção interna e avaliação externa', '',
             '240 ajustes internos da mesma fórmula de índice de saúde (HI), 60 seleções externas por domínio/repetição/dobra e 9.600 decisões externas. Cada repetição avalia 100 motores por domínio; repetições reutilizam motores. Escolhas usam apenas D40, sem U50/E10.', '',
             '## Escolhas congeladas', '', '| Domínio | Família | Prazo | Valor | Dobras |', '|---|---|---|---|---|']
    for key, g in selections.groupby(['subset', 'family', 'delay', 'selected_value']):
        lines.append('| '+' | '.join(map(str, key))+f' | {len(g)} |')
    lines += ['', f'Seleções sem candidato viável: {int((~selections.selection_feasible).sum())}/240.', '',
              '## Avaliação externa', '', '| Domínio | Repetição | Regra | Vida média | Chegadas/100 | Tardias | Exatas | Sem decisão |', '|---|---|---|---|---|---|---|---|']
    for r in table.itertuples():
        lines.append(f'| {r.subset} | {r.repeat} | {r.policy} | {r.mean_life:.2f} | {r.endpoint_events} | {r.strict_late} | {r.exact} | {r.missing} |')
    lines += ['', 'As chegadas incluem retirada em T, após T ou ausência de decisão. O filtro interno composto ≤2% em 40 motores exige zero eventos observados; difere da tolerância estrita de ultrapassagem >T do autor. Não constitui garantia populacional. Ganhos de vida acompanhados de eventos não são economia admissível demonstrada.', '',
              '[Contrastes pareados e intervalos bootstrap](contrasts.csv): 2.000 reamostragens por motor/repetição, condicionais aos modelos e escolhas; não reaprendem todo o procedimento. Dados já explorados, sem confirmação externa intocada. Nenhuma inspeção ou projeção monetária nesta rodada.', '']
    (p.OUT/'relatorio.md').write_text('\n'.join(lines), encoding='utf-8')
    fig, axes = plt.subplots(1, 2, figsize=(12, 4), layout='constrained')
    for ax, (s, frame) in zip(axes, table.groupby('subset')):
        for name, g in frame.groupby('policy'):
            if name.endswith('D1'):
                ax.scatter(g.mean_life, g.endpoint_events, label=name.removesuffix('_D1'), s=35)
        ax.set(title=s+' — prazo 1 ciclo', xlabel='Vida média aproveitada (ciclos)', ylabel='Chegadas ao endpoint / 100 motores')
        ax.grid(alpha=.2)
    axes[1].legend(fontsize=6, loc='upper left')
    fig.savefig(p.OUT/'life_risk.png', dpi=160)
    plt.close(fig)
    p.refresh_manifest()
    print(table.loc[table.policy.str.contains('SELECTED')].to_string(index=False))
    print(selections.groupby(['subset', 'family', 'selected_value']).size().to_string())


if __name__ == '__main__':
    main()
