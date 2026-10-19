"""P11.1 report: separate value of the health landmark from the F converter."""

import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import pilot_landmark_control_11a as p


def table(frame):
    rows = ['| '+' | '.join(frame.columns)+' |', '|'+'---|'*len(frame.columns)]
    for r in frame.itertuples(index=False, name=None):
        rows.append('| '+' | '.join(f'{v:.4f}' if isinstance(v, (float, np.floating)) else str(v) for v in r)+' |')
    return '\n'.join(rows)


def main():
    out = p.OUT
    summary = pd.read_csv(out / 'summary.csv')
    contrasts = pd.read_csv(out / 'contrasts.csv')
    decomp = pd.read_csv(out / 'decomposition.csv')
    selected = [f'{m}_LOWER98_M15_D{d}' for m in ['ISO', 'RF_SLOPE'] for d in [1, 2]]
    main = contrasts.loc[contrasts.policy_id.isin(selected)].copy()
    main['saving_percent'] = 100*main.relative_saving
    main['saving_low_percent'], main['saving_high_percent'] = 100*main.saving_ci_low, 100*main.saving_ci_high
    shares = decomp.loc[decomp.policy_id.isin(selected)].groupby(['subset', 'policy_id'], as_index=False).agg(
        life_added_min=('prognosis_life_gain', 'min'), life_added_max=('prognosis_life_gain', 'max'),
        prognosis_share_min=('prognosis_share', 'min'), prognosis_share_max=('prognosis_share', 'max'),
        marker_share_min=('marker_share', 'min'), marker_share_max=('marker_share', 'max'))
    shares.to_csv(out / 'reference_ranges.csv', index=False)
    report = [
        '# P11.1 — controle do marco de condição e ganho incremental do prognóstico',
        '[Protocolo anterior a esta execução](../../protocolo_controle_marco_11a.md). A análise foi '
        'motivada por P11 e usa os mesmos motores já examinados. Não é confirmação independente. '
        'Índice de saúde (HI) supervisionado P10 congelado, disponibilidade ≥39, mesma passagem '
        'causal de 0,5 e mesmos prazos d=1/2. O controle decide no primeiro marco disponível, '
        'retira d ciclos depois e não usa conversor de F, quantil, endpoint ou reserva 15/12.',
        'Os 100 motores de cada domínio se repetem nas três divisões; não são 300 unidades '
        'independentes. ISO é regressão isotônica; RF_SLOPE é floresta aleatória com HI e inclinação '
        'causal. O controle HI utiliza os mesmos parâmetros supervisionados aprendidos em F; '
        'retirar o conversor não torna a construção do HI independente da vida remanescente.',
        '## Controle simples nos motores completos',
        table(summary.loc[summary.method.eq('HI_MARKER') & summary.dataset.eq('complete'),
              ['subset', 'repeat', 'policy_id', 'total', 'decisions', 'without_decision', 'late_count',
               'exact_count', 'mean_utilised', 'mean_unused', 'cost_per_cycle']]),
        '## Incremento sobre HI: limite inferior 98% e reserva de referência 15',
        'same_date e later_date são contagens nos mesmos 100 motores. Ganho de vida é a diferença '
        'média de ciclos simulados aproveitados. Intervalos descritivos de 95%, por 2000 '
        'reamostragens pareadas de motores, por repetição e condicionais a modelos congelados. '
        'A economia percentual é relativa ao controle HI, não à idade fixa ou a uma companhia.',
        table(main[['subset', 'repeat', 'policy_id', 'same_date', 'later_date', 'candidate_without_decision',
                    'candidate_reached', 'reference_reached', 'delta_mean_life', 'life_ci_low', 'life_ci_high',
                    'saving_percent', 'saving_low_percent', 'saving_high_percent']]),
        '![Vida adicional sobre o controle de HI](incremental_life.png)',
        '## De onde veio o ganho frente à idade fixa?',
        'A tabela mostra mínimo/máximo das parcelas entre três repetições; não são intervalos '
        'de confiança. prognosis_share é a parcela do ganho MÉDIO DE VIDA frente à idade fixa '
        'que ocorre depois do controle HI. marker_share é a parcela já obtida pelo marco. '
        'Não são parcelas de poupança monetária e não demonstram decomposição causal externa. '
        'As parcelas de vida são aditivas; percentagens de economia não são: os fatores de '
        'custo se multiplicam, conforme o protocolo.',
        table(shares),
        '## HI versus idade fixa',
        'A idade é o controle P11 conservador, definido em F∪C e sujeito aos eventos externos '
        'já registrados. Não trocar sua definição para favorecer a narrativa; a comparação '
        'não é entre políticas de admissibilidade equivalente ou práticas reais de uma companhia.',
        table(contrasts.loc[contrasts.reference.str.startswith('AGE')]),
        '## Todas as regras: vida e eventos permanecem associados',
        'A previsão central pode prolongar mais a vida enquanto deixa falhas sem prevenção. '
        'Esse ganho não será tratado como vantagem económica admissível. As sensibilidades '
        '95% e reserva12 permanecem comparações, sem adoção. A maior vida frente ao primeiro '
        'marco é estrutural para regras que só podem actuar depois dele; portanto, um intervalo '
        'positivo por si só não demonstra utilidade de informação prognóstica ou segurança.',
        table(contrasts.loc[contrasts.reference.str.startswith('HI_MARKER')]),
        '## Teste truncado',
        'Sem marco utilizável até o truncamento, status censurado. Não criar decisões ou vidas '
        'futuras a partir de RUL verdadeiro. Aferição de uma retirada comprometida não significa '
        'que sua execução foi observada. Nenhum truncado entra em custo de renovação.',
        table(summary.loc[summary.method.eq('HI_MARKER') & summary.dataset.eq('truncated'),
              ['subset', 'repeat', 'policy_id', 'total', 'decisions', 'without_decision',
               'late_count', 'exact_count', 'observed_executions']]),
        '## Limites e decisão científica',
        'Distinguir ganho de condição supervisionada e ganho incremental do conversor/calibração. '
        'Ausência de eventos não certifica risco populacional ≤2%, e as divisões são dependentes. '
        'Não escolher a melhor semente, alterar o HI ou o marco após estes resultados. O controle '
        'simples deve permanecer como referência decisória competitiva. Qualquer otimização '
        'de limiar, espera após marco ou regra futura exige seleção interna e protocolo próprio; '
        'não acrescentar complexidade apenas para obter uma melhoria.',
        'Sem ajuste, inspeção, projeção de 20 anos ou edição do artigo. Custos são normalizados '
        'por exposição simulada; a ponte de escala e os parâmetros empresariais continuam abertos.',
        '[Verificação](verification.json), [controles](controls.csv), [contrastes](contrasts.csv), '
        '[decomposição](decomposition.csv), [metadados](metadata.json) e [manifesto](manifest.json).',
    ]
    (out / 'relatorio.md').write_text('\n\n'.join(report)+'\n', encoding='utf-8')
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.5), sharey=True)
    for ax, subset in zip(axes, ['FD001', 'FD003']):
        for j, (method, delay) in enumerate([(m, d) for m in ['ISO', 'RF_SLOPE'] for d in [1, 2]]):
            g = main.loc[main.subset.eq(subset) & main.policy_id.eq(f'{method}_LOWER98_M15_D{delay}')]
            color = '#2463a6' if method == 'ISO' else '#ce661c'
            ax.scatter(np.full(len(g), j), g.delta_mean_life, color=color)
            for r in g.itertuples():
                ax.annotate(str(r.repeat), (j, r.delta_mean_life), xytext=(5, 2), textcoords='offset points')
        ax.set_xticks(range(4), ['ISO d1', 'ISO d2', 'RF d1', 'RF d2'])
        ax.set_title(subset)
        ax.axhline(0, color='grey', linewidth=1)
        ax.grid(alpha=.2)
        ax.set_xlim(-.5, 3.5)
    axes[0].set_ylabel('Mean life added to HI-marker control (simulated cycles)')
    fig.tight_layout()
    fig.savefig(out / 'incremental_life.png', dpi=180)
    plt.close(fig)
    (out / 'report_metadata.json').write_text(json.dumps(dict(script_sha256=p.p11.sha(p.ROOT / 'experiments/report_pilot_landmark_control_11a.py'),
                                                             source='contrasts.csv', primary_display='lower98, reserve15'), indent=2), encoding='utf-8')
    p.refresh_manifest()


if __name__ == '__main__':
    main()
