"""Complete each retrospective sheet with event memory and perturbation responses."""
import json
import numpy as np
import pandas as pd
import pilot_explainability_13b as p


def val(x,d=2):return f'{x:.{d}f}' if np.isfinite(x) else 'indefinido'


def main():
    out=p.OUT
    assert (out/'report_metadata.json').exists()
    engine=pd.read_csv(out/'action_engines.csv').set_index(['subset','repeat','unit','policy_id','phase','kind','epsilon'])
    trigger=pd.read_csv(out/'trigger_explanation.csv').set_index(['subset','repeat','unit','policy_id'])
    cases=pd.read_csv(out/'case_sheets.csv')
    crossings={}
    for split in json.loads((p.p10.OUT/'splits.json').read_text()):
        s,rep,fold=split['subset'],split['repeat'],split['fold']
        b=np.load(out/f'baseline_{s}_r{rep}_f{fold}.npz')
        for unit in split['evaluation']:
            mask=(b['unit']==unit)&(b['H']<=.5)
            t=b['cycle'][mask];G=float(t.min()) if len(t) else np.nan
            crossings[(s,rep,unit)]=G
    details=[]
    for (s,unit),table in cases.groupby(['subset','unit'],sort=True):
        file=out/f'case_{s}_u{unit}.md'
        text=file.read_text(encoding='utf-8')
        assert '## Memória do sinal e resposta às perturbações' not in text
        lines=['', '## Memória do sinal e resposta às perturbações', '',
            'G é a primeira passagem HI≤0,5 observada; A=max(39,G) é a primeira disponibilidade do marco, memorizada após eventual recuperação. Nenhum dos dois é P físico validado. Datas e T abaixo são diagnósticos retrospectivos.', '']
        for rep in [1,2,3]:
            G=crossings[(s,rep,unit)]
            lines.append(f'- Repetição{rep}: G={val(G,0)}, A={val(max(39,G) if np.isfinite(G) else np.nan,0)}.')
        lines+=['', 'Resposta por motor, canal individual e amplitude1, ambos os sinais. Global: rampa desde o ciclo20; local: rampa nas20 observações até a decisão original (ou T−1 em ausência). Comparações de datas requerem presença em ambos os replays; mudanças de presença conservam todos os ensaios.', '',
            '| Rep. | Política | Correção q | Reserva | Média absoluta Δr global | Média absoluta Δr local | Mudança de presença global | Mudança de presença local | Variantes globais com prefixo no suporte |',
            '|---|---|---|---|---|---|---|---|---|']
        for r in table.itertuples():
            t=trigger.loc[(s,r.repeat,unit,r.policy_id)]
            g=engine.loc[(s,r.repeat,unit,r.policy_id,'global','channel',1.)]
            l=engine.loc[(s,r.repeat,unit,r.policy_id,'local','channel',1.)]
            lines.append(f'| {r.repeat} | {r.policy_id} | {val(t.q_late)} | {val(t.reserve,0)} | {val(g.mean_abs_delta)} | {val(l.mean_abs_delta)} | {100*g.presence_flip:.2f}% | {100*l.presence_flip:.2f}% | {int(g.supported_variants)}/{int(g.variants)} |')
            details.append(dict(subset=s,unit=unit,repeat=r.repeat,policy_id=r.policy_id,G=crossings[(s,r.repeat,unit)],
                A=t.gate,q=t.q_late,reserve=t.reserve,global_mean_abs_delta=g.mean_abs_delta,
                local_mean_abs_delta=l.mean_abs_delta,global_presence_flip=g.presence_flip,
                local_presence_flip=l.presence_flip,global_supported_variants=int(g.supported_variants),
                variants=int(g.variants)))
        lines+=['', 'Ausência de suporte para todo o prefixo impede interpretar estas respostas como robustez física validada. O perfil sensorial e a regra estão auditados, mas a utilidade humana da explicação, criticidade e crédito de manutenção não foram demonstrados. Aprovação por inspeção não integra esta tarefa PHM.', '']
        file.write_text(text+'\n'.join(lines),encoding='utf-8')
    pd.DataFrame(details).to_csv(out/'case_responses.csv',index=False)
    (out/'case_detail_metadata.json').write_text(json.dumps(dict(rows=len(details),
        source_sha256=p.p11.sha(p.ROOT/'experiments/enrich_explainability_cases_13b.py')),indent=2))
    print(json.dumps(dict(case_response_rows=len(details))))


if __name__=='__main__':main()
