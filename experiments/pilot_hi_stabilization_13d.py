"""P13.4: all selection and stability evaluation restricted to D=F+C."""
import hashlib
import importlib.metadata
import json
from datetime import datetime,timezone
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits
import hi_stabilization_core_13d as core
import pilot_f_uncertainty_10 as p10
from pilot_policy_selection_13a import inner_partitions

ROOT=p10.ROOT
OUT=ROOT/'experiments/artifacts/pilot_hi_stabilization_13d'


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    OUT.mkdir(exist_ok=False)
    files=[ROOT/'experiments'/n for n in ['protocolo_estabilizacao_hi_13d.md','hi_stabilization_core_13d.py',
        'pilot_hi_stabilization_13d.py','test_hi_stabilization_13d.py','verify_hi_stabilization_13d.py',
        'pilot_f_uncertainty_10.py','pilot_policy_selection_13a.py','pilot_fd001.py','pilot_fd001_04.py',
        'pilot_fd001_05.py','pilot_fd003_06.py','pilot_hi_trajectory_08.py']]
    files+=[p10.OUT/'splits.json']+[ROOT/f'CMAPSSData/train_{s}.txt' for s in ['FD001','FD003']]
    files+=list((ROOT/'experiments/artifacts/pilot_policy_selection_13a').glob('inner_hi_*.joblib'))
    inputs={str(p.relative_to(ROOT)):sha(p) for p in files}
    meta=dict(started_utc=datetime.now(timezone.utc).isoformat(),inputs=inputs,
              packages={n:importlib.metadata.version(n) for n in ['numpy','pandas','scipy','scikit-learn','joblib']})
    (OUT/'execution_start.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    for p in files:
        if p.suffix in ['.py','.md']: (OUT/f'source_{p.name}').write_bytes(p.read_bytes())
    splits=json.loads((p10.OUT/'splits.json').read_text(encoding='utf-8'))
    inputs_data={s:p10.read_inputs('train',s) for s in ['FD001','FD003']}
    all_metrics=[];selections=[];provenance=[];total_kkt=0.;total_solutions=0
    for sp in splits:
        subset=sp['subset'];rep=sp['repeat'];fold=sp['fold'];tag=f'{subset}_r{rep}_f{fold}'
        ids=sorted(sp['fit']+sp['converter'])
        data=inputs_data[subset].loc[inputs_data[subset].unit.isin(ids)].reset_index(drop=True)
        bank=core.engine_bank(data,subset)
        assert set(bank).isdisjoint(sp['uncertainty']+sp['evaluation'])
        baselines=[];effects=[]
        for part in inner_partitions(sp):
            inner=part['inner_fold'];key=dict(subset=subset,repeat=rep,fold=fold,inner_fold=inner)
            provenance.append(key|part)
            arrays={n:[] for n in ['effective','beta','factors','scale','eligible','direction','alpha','kkt']}
            base_results={};base_paths={}
            for removed in [0]+part['fit']:
                fit=[i for i in part['fit'] if i!=removed]
                assert set(fit).isdisjoint(part['validation'])
                m=core.moments(bank,fit)
                models=[core.solve(m,subset,c) for c in core.CANDIDATES]
                for name in arrays: arrays[name].append(np.stack([model[name] for model in models]))
                total_solutions+=len(models);total_kkt=max(total_kkt,max(x['kkt'] for x in models))
                if not removed:
                    # Compare all internal M18 fits to the archived original implementation.
                    prior=joblib.load(ROOT/f'experiments/artifacts/pilot_policy_selection_13a/inner_hi_{tag}_v{inner}.joblib')
                    old=np.zeros(21)
                    for sensor,b,d,s in zip(prior['stats']['channels'],prior['beta'],prior['stats']['direction'],prior['stats']['scale']):
                        old[core.SENSORS.index(sensor)]=b*d/s
                    np.testing.assert_allclose(models[0]['effective'],old,atol=1e-8,rtol=1e-7)
                for candidate,model in zip(core.CANDIDATES,models):
                    for unit in part['validation']:
                        result,h=core.evaluate(bank,unit,model['effective'])
                        row=key|dict(candidate=candidate,removed=removed)|result
                        if not removed:
                            baselines.append(row);base_results[(candidate,unit)]=result;base_paths[(candidate,unit)]=h
                        else:
                            b=base_results[(candidate,unit)]
                            row.update(baseline_crossing=b['crossing'],baseline_decision=b['decision'],
                                       delta=result['crossing']-b['crossing'],
                                       presence_discordant=bool(np.isfinite(result['crossing'])!=np.isfinite(b['crossing'])),
                                       hi_rmse=float(np.sqrt(np.mean((h-base_paths[(candidate,unit)])**2))))
                            effects.append(row)
            np.savez_compressed(OUT/f'fits_{tag}_v{inner}.npz',removed=np.array([0]+part['fit']),**{n:np.stack(v) for n,v in arrays.items()})
        baseline=pd.DataFrame(baselines);effect=pd.DataFrame(effects)
        baseline.to_csv(OUT/f'baseline_{tag}.csv.gz',index=False,compression='gzip')
        effect.to_csv(OUT/f'effects_{tag}.csv.gz',index=False,compression='gzip')
        metrics,selection=core.choose(core.summarize(baseline,effect))
        for k,v in dict(subset=subset,repeat=rep,fold=fold).items(): metrics[k]=v
        all_metrics.append(metrics)
        selections.append(dict(subset=subset,repeat=rep,fold=fold)|selection)
        print(f'{tag}: selected {selection["selected"]}; p95 {selection["baseline_p95"]:.2f} -> {selection["selected_p95"]:.2f}',flush=True)
    # Freeze choices before fitting any final outer HI. U/E never evaluated here.
    pd.concat(all_metrics,ignore_index=True).to_csv(OUT/'internal_metrics.csv',index=False)
    pd.DataFrame(selections).to_csv(OUT/'selections.csv',index=False)
    (OUT/'inner_splits.json').write_text(json.dumps(provenance,indent=2),encoding='utf-8')
    freeze=sha(OUT/'selections.csv')
    for sp,choice in zip(splits,selections):
        subset=sp['subset'];data=inputs_data[subset].loc[inputs_data[subset].unit.isin(sp['fit'])].reset_index(drop=True)
        bank=core.engine_bank(data,subset);m=core.moments(bank,sp['fit']);model=core.solve(m,subset,choice['selected'])
        joblib.dump(dict(subset=subset,candidate=choice['selected'],fit_units=sp['fit'],selection_development=sorted(sp['fit']+sp['converter']),
                         selection_sha256=freeze,config=p10.CONFIG[subset],**model),
                    OUT/f'selected_hi_{subset}_r{sp["repeat"]}_f{sp["fold"]}.joblib',compress=3)
    assert freeze==sha(OUT/'selections.csv')
    assert all(sha(ROOT/n)==v for n,v in inputs.items())
    (OUT/'metadata.json').write_text(json.dumps(dict(completed_utc=datetime.now(timezone.utc).isoformat(),
         internal_solutions=total_solutions,outer_fits=60,baseline_responses=12000,exclusion_responses=300000,
         maximum_kkt=total_kkt,selection_sha256=freeze,evaluated_groups='internal V within D=F+C only'),indent=2),encoding='utf-8')
    (OUT/'manifest.json').write_text(json.dumps({p.name:sha(p) for p in OUT.iterdir() if p.is_file()},indent=2),encoding='utf-8')
    print('Completed P13.4; no U/E trajectories scored.',flush=True)


if __name__=='__main__':
    with threadpool_limits(limits=1): main()
