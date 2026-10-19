"""Report P11 decisions and normalised economics; no 20-year monetary forecast."""

import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import pandas as pd

import pilot_removal_11 as p11


def table(frame):
    lines = ['| '+' | '.join(frame.columns)+' |', '|'+'---|'*len(frame.columns)]
    for row in frame.itertuples(index=False, name=None):
        lines.append('| '+' | '.join(f'{v:.4f}' if isinstance(v, (float, np.floating)) else str(v) for v in row)+' |')
    return '\n'.join(lines)


def main():
    out = p11.OUT
    summary = pd.read_csv(out / 'summary.csv')
    contrasts = pd.read_csv(out / 'contrasts.csv')
    decisions = pd.read_csv(out / 'decisions.csv')
    front = pd.read_csv(out / 'frontier.csv')
    complete = summary.loc[summary.dataset.eq('complete')]
    primary = complete.loc[complete.phase.ne('sensitivity')]
    ranges = primary.groupby(['subset', 'policy_id'], as_index=False).agg(
        strict_pass_repeats=('passes_strict_screen', 'sum'), prudent_pass_repeats=('passes_prudent_screen', 'sum'),
        late_min=('late_count', 'min'), late_max=('late_count', 'max'),
        exact_max=('exact_count', 'max'), missing_max=('without_decision', 'max'),
        mean_life_min=('mean_utilised', 'min'), mean_life_max=('mean_utilised', 'max'),
        unused_min=('mean_unused', 'min'), unused_max=('mean_unused', 'max'))
    ranges.to_csv(out / 'primary_ranges.csv', index=False)
    marking = decisions.loc[decisions.dataset.eq('complete') & decisions.phase.ne('control')].copy()
    marking['at_first_available'] = marking.has_decision & marking.decision.eq(marking.first_available)
    mark_summary = marking.groupby(['subset', 'repeat', 'policy_id'], as_index=False).agg(
        decisions=('has_decision', 'sum'), at_first_available=('at_first_available', 'sum'),
        initial_insufficient=('initial_insufficient', 'sum'))
    mark_summary.to_csv(out / 'first_opportunity.csv', index=False)
    columns = ['subset', 'repeat', 'policy_id', 'decisions', 'without_decision', 'late_count', 'exact_count',
               'mean_utilised', 'mean_unused', 'initial_insufficient_count', 'median_real_reserve',
               'restorations_per_10000_cycles', 'passes_strict_screen', 'passes_prudent_screen']
    chosen = ['ISO_LOWER98_M15_D1', 'ISO_LOWER98_M15_D2', 'RF_SLOPE_LOWER98_M15_D1', 'RF_SLOPE_LOWER98_M15_D2']
    report = [
        '# P11 — comparação de regras de remoção sem inspeção',
        '[Protocolo anterior à execução](../../protocolo_remocao_11.md). Previsões P10 congeladas, '
        'sem novo ajuste do índice de saúde (HI), modelos ou quantis. FD001 principal; FD003 robustez; '
        'três repetições com os mesmos 100 motores por domínio. ISO é isotônico; RF_SLOPE é floresta '
        'aleatória com HI e inclinação causal. As 26 regras são 16 primárias, oito sensibilidades '
        '95% e dois controles de idade fixa. São comparações exploratórias, não 300 motores independentes.',
        '## Triagem das regras primárias',
        'Decisão no primeiro ciclo permitido em que a antecedência prevista é ≤reserva+execução; '
        'retirada comprometida decisão+d. LOWER98 usa limite inferior calibrado pelo máximo temporal '
        'em U; POINT usa previsão central. Reserva 12 é apenas sensibilidade de política, sem adoção. '
        'A idade de controle é o menor endpoint dos 40 motores F∪C menos um, definida antes de E. '
        'A ausência de decisão preventiva antes do endpoint permanece no denominador e impede '
        'completude; não é convertida em programação tardia fictícia.',
        'strict_pass_repeats exige decisão em todos os motores e ultrapassagem estrita ≤2% na repetição. '
        'prudent_pass_repeats também exige nenhuma retirada programada exactamente no endpoint, '
        'como triagem conservadora, sem alterar o alvo do autor. Nenhum filtro valida risco populacional '
        'ou admissibilidade operacional. A tabela mostra amplitudes entre divisões, não intervalos de confiança.',
        'Com execução de um ciclo e decisões apenas antes de T, r=τ+1≤T por construção: '
        'a ultrapassagem estrita isolada não detecta todas as falhas. É indispensável conservar '
        'chegadas exactas e ausências de decisão. Com dois ciclos, a programação mais tardia '
        'ainda observável pode ser T+1; a curta magnitude não valida operação depois do endpoint.',
        table(ranges),
        '![Vida aproveitada e chegadas ao endpoint](removal_tradeoff.png)',
        'A figura inclui chegadas exactas, programações tardias e ausência de decisão; '
        'essa frequência composta é distinta do alvo de 2% de ultrapassagem estrita.',
        '## Reserva de referência 15 — comparação por repetição',
        table(primary.loc[primary.policy_id.isin(chosen+['AGE_D1', 'AGE_D2']), columns]),
        '## Diferenças pareadas frente ao controle de idade fixa',
        'Vida média em ciclos simulados; custo normalizado n/ΣN. Economia relativa '
        '1−c_PHM/c_idade. Intervalos descritivos de 95% de 2000 reamostragens pareadas por motor, '
        'separadamente por repetição, condicionais aos modelos congelados. Não corrigem a escolha '
        'entre várias regras e não são projeções de resultado financeiro de companhia. O controle '
        'também apresentou eventos não prevenidos; não tratar a comparação como tendo admissibilidade equivalente.',
        table(contrasts.loc[contrasts.policy_id.isin(chosen)]),
        '## Todas as regras e sensibilidade pré-fixada',
        table(complete[columns]),
        '## Decisão já na primeira oportunidade',
        'A insuficiência inicial refere-se à reserva PREVISTA pelo limite no primeiro marco, '
        'não à reserva real retrospectiva. Uma decisão imediata no marco pode ter antecedência '
        'real ampla. Essa concentração limita inferir que o prognóstico sequencial individualiza '
        'o momento ótimo. at_first_available conta decisões no primeiro marco disponível.',
        table(mark_summary.loc[mark_summary.policy_id.isin(chosen)]),
        '## Teste truncado: diagnóstico condicional',
        'Somente decisões possíveis com os dados observados; ausência até o truncamento é censura, '
        'não falha definitiva. A data de uma retirada comprometida pode ser confrontada com o endpoint '
        'obtido de RUL, sem observar sua execução e sem criar sensores futuros. Nenhum truncado '
        'entra na taxa de renovação. conditional_late_fraction usa apenas decisões disponíveis.',
        table(summary.loc[summary.dataset.eq('truncated'), ['subset', 'repeat', 'policy_id', 'total', 'decisions',
              'without_decision', 'late_count', 'exact_count', 'conditional_late_fraction', 'observed_executions']]),
        '## Fronteira descritiva',
        'Não dominadas por menor/igual número de ausências, ultrapassagens e chegadas exactas, '
        'e menor/igual vida não aproveitada, com melhoria estrita em pelo menos um indicador. '
        'Comparar somente primárias/controle com o mesmo prazo d; não seleccionar a melhor semente.',
        table(front.loc[front.non_dominated, columns]),
        '## Limites e rastreabilidade',
        'Não houve simulação de 20 anos, monetização, inspeção ou edição do artigo. As métricas '
        'por 10.000 ciclos referem-se à exposição simulada, sem afirmar equivalência com voo real. '
        'P12 ainda exige ponte de escala; ganho empresarial exige margem incremental, demanda, '
        'disponibilidade e harmonização monetária. O marco não identifica P e o endpoint não '
        'valida margens físicas de sensores. Zero eventos em uma amostra exploratória não certifica risco ≤2%.',
        'O primeiro verificador encontrou motores truncados sem qualquer previsão após aquecimento; '
        'a correção trata esse grupo como trajetória vazia, preservando decisões e resultados. '
        'Houve ainda correção de separador Windows no mapeamento de fonte arquivada. '
        'Código original e logs foram preservados. [Correção do verificador](verifier_correction.json).',
        '[Verificação independente](verification.json); [metadados](metadata.json); '
        '[controle congelado por dobra](controls.json); [decisões](decisions.csv); '
        '[contrastes](contrasts.csv); [manifesto](manifest.json).',
    ]
    (out / 'relatorio.md').write_text('\n\n'.join(report)+'\n', encoding='utf-8')
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for ax, subset in zip(axes, ['FD001', 'FD003']):
        for method, color in [('AGE', '#555555'), ('ISO', '#2463a6'), ('RF_SLOPE', '#ce661c')]:
            for anchor, marker in [('age', 'X'), ('point', 'o'), ('lower', '^')]:
                g = primary.loc[primary.subset.eq(subset) & primary.method.eq(method) & primary.anchor.eq(anchor)]
                ax.scatter(g.mean_utilised, 100*g.reached_count/g.total, color=color, marker=marker, alpha=.65, s=38)
        ax.set(title=subset, xlabel='Mean utilised life (simulated cycles)', ylabel='Endpoint arrivals incl. no decision (%)')
        ax.grid(alpha=.2)
    legend = [Line2D([], [], marker='o', color=c, linestyle='', label=m) for m, c in [('Age', '#555555'), ('ISO', '#2463a6'), ('RF temporal', '#ce661c')]]
    legend += [Line2D([], [], marker=m, color='black', linestyle='', label=a) for a, m in [('Central', 'o'), ('Lower 98%', '^')]]
    fig.legend(handles=legend, loc='lower center', ncol=5, frameon=False)
    fig.tight_layout(rect=[0, .08, 1, 1])
    fig.savefig(out / 'removal_tradeoff.png', dpi=180)
    plt.close(fig)
    (out / 'report_metadata.json').write_text(json.dumps(dict(script_sha256=p11.sha(p11.ROOT / 'experiments/report_pilot_removal_11.py'),
                                                             source='summary.csv', no_calendar_projection=True), indent=2), encoding='utf-8')
    p11.refresh_manifest()


if __name__ == '__main__':
    main()
