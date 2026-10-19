"""P13.3: diagnostic refits only; never replaces a frozen HI or policy."""
import hashlib
import json
from pathlib import Path

import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits

import pilot_f_uncertainty_10 as p10

ROOT=p10.ROOT
OUT=ROOT/'experiments/artifacts/pilot_hi_influence_13c'
SENSORS=[f's{i}' for i in range(1,22)]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def effective_weights(health):
    w=np.zeros(21)
    for sensor,b,d,s in zip(health['stats']['channels'],health['beta'],
                            health['stats']['direction'],health['stats']['scale']):
        w[SENSORS.index(sensor)]=b*d/s
    return w


def paths(data,health):
    centred=p10.centred_sensors(data)
    z=p10.p05.standardise(centred,health['stats'])
    h=p10.p05.empirical_hi(z,health['beta'])
    direct=np.clip(1-centred[SENSORS].to_numpy()@effective_weights(health),0,1)
    mask=data.cycle.ge(20).to_numpy()
    np.testing.assert_allclose(h[mask],direct[mask],atol=1e-11)
    frame=data.loc[mask,['unit','cycle']].copy()
    frame['hi']=h[mask]
    return frame


def markers(frame):
    return frame.loc[frame.hi.le(.5)].groupby('unit').cycle.min().reindex(frame.unit.unique())


def design(data,health):
    data=p10.complete_labels(data)
    z=p10.p05.standardise(p10.centred_sensors(data),health['stats'])
    mask=data.cycle.ge(20)
    x=z[np.asarray(mask)]
    y=1-np.minimum(1,data.loc[mask,'rul'].to_numpy()/health['config']['tau'])**health['config']['gamma']
    weights=p10.p05.equal_engine_weights(data.loc[mask,'unit'])
    return x,y,weights


def condition(x):
    if not x.shape[1]: return np.nan,[]
    s=np.linalg.svd(x,compute_uv=False)
    return (float(s[0]/s[-1]) if s[-1]>s[0]*1e-12 else np.inf),s.tolist()


def loss(data,health):
    x,y,w=design(data,health)
    mse=float(np.sum(w*(x@health['beta']-y)**2))
    penalty=float(health['config']['ridge']*np.sum(health['beta']**2))
    return mse,penalty


def refit(data,base,subset,variant):
    assert len(data.unit.unique())==24
    if variant=='full': return p10.fit_health(data,subset)
    labelled=p10.complete_labels(data)
    z=p10.p05.standardise(p10.centred_sensors(labelled),base['stats'])
    beta=p10.p05.fit_empirical(labelled,z,sorted(data.unit.unique()),**base['config'])
    return dict(stats=base['stats'],beta=beta,config=base['config'],fit_units=sorted(data.unit.unique().tolist()))


def main():
    OUT.mkdir(exist_ok=False)
    input_paths=[ROOT/'experiments/protocolo_influencia_hi_13c.md',Path(__file__),
                 ROOT/'experiments/test_hi_influence_13c.py',ROOT/'experiments/verify_hi_influence_13c.py',
                 ROOT/'experiments/pilot_f_uncertainty_10.py',ROOT/'experiments/pilot_fd001_05.py',
                 ROOT/'experiments/pilot_fd001_04.py',ROOT/'experiments/pilot_fd003_06.py',
                 p10.OUT/'splits.json']
    input_paths+=list(p10.OUT.glob('models_*.joblib'))
    input_paths+=[ROOT/f'CMAPSSData/train_{s}.txt' for s in ['FD001','FD003']]
    inputs={str(p.relative_to(ROOT)):sha(p) for p in input_paths}
    (OUT/'inputs.json').write_text(json.dumps(inputs,indent=2),encoding='utf-8')
    for path in input_paths:
        if path.suffix in ['.py','.md']:
            (OUT/f'source_{path.name}').write_bytes(path.read_bytes())
    baseline=[];spectra=[];cache={};datasets={}
    for subset in ['FD001','FD003']:
        data=p10.read_inputs('train',subset);datasets[subset]=data
        for repeat,seed in enumerate(p10.SEEDS,1):
            for split in p10.partitions(seed):
                fold=split['fold'];tag=f'{subset}_r{repeat}_f{fold}'
                base=joblib.load(p10.OUT/f'models_{tag}.joblib')['health']
                assert base['fit_units']==split['fit']
                fit=data.loc[data.unit.isin(split['fit'])].reset_index(drop=True)
                ev=data.loc[data.unit.isin(split['evaluation'])].reset_index(drop=True)
                h=paths(ev,base);cross=markers(h)
                for unit,value in cross.items():
                    baseline.append(dict(subset=subset,repeat=repeat,fold=fold,unit=unit,crossing=value))
                x,_,w=design(fit,base);x=x*np.sqrt(w[:,None]);active=base['beta']>1e-8
                cond,s=condition(x);ca,_=condition(x[:,active])
                cr,_=condition(np.vstack([x,np.sqrt(base['config']['ridge'])*np.eye(x.shape[1])]))
                spectra.append(dict(subset=subset,repeat=repeat,fold=fold,channels=x.shape[1],
                                    active=int(active.sum()),condition=cond,active_condition=ca,
                                    penalized_condition=cr,singular_values=json.dumps(s)))
                cache[(subset,repeat,fold)]=(base,split,fit,ev,h)
    bas=pd.DataFrame(baseline);bas.to_csv(OUT/'baseline_markers.csv',index=False)
    pd.DataFrame(spectra).to_csv(OUT/'spectra.csv',index=False)
    # Exact replay against archived P13.2 decisions of the condition marker.
    old=pd.read_csv(ROOT/'experiments/artifacts/pilot_explainability_13b/case_sheets.csv')
    old=old.loc[old.policy_id.eq('HI_MARKER_D1')]
    check=bas.merge(old[['subset','repeat','unit','decision']],on=['subset','repeat','unit'])
    np.testing.assert_allclose(np.maximum(39,check.crossing),check.decision,equal_nan=True)
    candidates=bas.groupby(['subset','unit']).crossing.agg(['min','max','count']).reset_index()
    candidates['span']=candidates['max']-candidates['min']
    candidates.to_csv(OUT/'marker_ranges.csv',index=False)
    cases=candidates.loc[candidates['count'].eq(3)].sort_values(['subset','span','unit'],ascending=[True,False,True]).groupby('subset').head(1)
    cases.to_csv(OUT/'cases.csv',index=False)
    effects=[];fits=[];weights=[]
    for case in cases.itertuples():
        fig,axes=plt.subplots(3,1,figsize=(10,10),sharex=True)
        for repeat in [1,2,3]:
            fold=int(bas.loc[bas.subset.eq(case.subset)&bas.repeat.eq(repeat)&bas.unit.eq(case.unit),'fold'].iloc[0])
            base,split,fit,ev,h=cache[(case.subset,repeat,fold)]
            original=markers(h);wb=effective_weights(base)
            own=h.loc[h.unit.eq(case.unit)]
            axes[repeat-1].plot(own.cycle,own.hi,color='black',lw=2,label='F25 original')
            for removed in split['fit']:
                reduced=fit.loc[fit.unit.ne(removed)].reset_index(drop=True)
                base_loss,base_penalty=loss(reduced,base)
                for variant in ['coefficients','full']:
                    model=refit(reduced,base,case.subset,variant)
                    assert removed not in model['fit_units']
                    assert set(model['fit_units']).isdisjoint(split['evaluation']+split['converter']+split['uncertainty'])
                    updated=paths(ev,model);new=markers(updated);wm=effective_weights(model)
                    mse,penalty=loss(reduced,model)
                    if variant=='coefficients': assert mse+penalty<=base_loss+base_penalty+1e-8
                    cosine=float(wb@wm/(np.linalg.norm(wb)*np.linalg.norm(wm)))
                    fitrow=dict(subset=case.subset,case_unit=case.unit,repeat=repeat,fold=fold,removed=removed,
                                variant=variant,fit_units=json.dumps(model['fit_units']),mse=mse,
                                penalty=penalty,baseline_mse_same_F24=base_loss,baseline_penalty=base_penalty,
                                weight_cosine=cosine,weight_relative_l2=float(np.linalg.norm(wm-wb)/np.linalg.norm(wb)))
                    fits.append(fitrow)
                    for sensor,b0,b1 in zip(SENSORS,wb,wm):
                        weights.append({k:fitrow[k] for k in ['subset','case_unit','repeat','fold','removed','variant']}|dict(sensor=sensor,baseline=b0,refit=b1))
                    for unit in split['evaluation']:
                        mask=h.unit.eq(unit);hb=h.loc[mask,'hi'].to_numpy();hn=updated.loc[updated.unit.eq(unit),'hi'].to_numpy()
                        effects.append(dict(subset=case.subset,case_unit=case.unit,repeat=repeat,fold=fold,
                                            removed=removed,variant=variant,unit=unit,baseline=original.loc[unit],
                                            refit=new.loc[unit],delta=new.loc[unit]-original.loc[unit],
                                            missing_baseline=bool(pd.isna(original.loc[unit])),missing_refit=bool(pd.isna(new.loc[unit])),
                                            hi_rmse=float(np.sqrt(np.mean((hn-hb)**2))),hi_max_abs=float(np.max(abs(hn-hb)))))
                    curve=updated.loc[updated.unit.eq(case.unit)]
                    axes[repeat-1].plot(curve.cycle,curve.hi,color='tab:orange' if variant=='full' else 'tab:blue',alpha=.12)
            axes[repeat-1].axhline(.5,color='grey',ls='--');axes[repeat-1].set_ylabel(f'HI; repeat {repeat}')
            print(f'{case.subset} case {case.unit} repeat {repeat}: 50 diagnostic refits',flush=True)
        axes[0].set_title(f'{case.subset}, engine {case.unit}; blue: coefficients; orange: full refit')
        axes[-1].set_xlabel('Cycle');fig.tight_layout();fig.savefig(OUT/f'case_{case.subset}_{case.unit}.png',dpi=150);plt.close(fig)
    pd.DataFrame(effects).to_csv(OUT/'effects.csv',index=False)
    pd.DataFrame(fits).to_csv(OUT/'refits.csv',index=False)
    pd.DataFrame(weights).to_csv(OUT/'weights.csv',index=False)
    assert all(sha(ROOT/p)==v for p,v in inputs.items())
    (OUT/'manifest.json').write_text(json.dumps({p.name:sha(p) for p in OUT.iterdir() if p.is_file()},indent=2),encoding='utf-8')
    print('Completed: 600 baseline markers, 60 spectra, 300 refits, 3000 paired engine responses.',flush=True)


if __name__=='__main__':
    with threadpool_limits(limits=1): main()
