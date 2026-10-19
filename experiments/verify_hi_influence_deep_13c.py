"""Post-run verification: reconstruct responses from raw sensors and saved weights."""
import json
import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits
import pilot_f_uncertainty_10 as p10


def main():
    out=p10.ROOT/'experiments/artifacts/pilot_hi_influence_13c'
    effects=pd.read_csv(out/'effects.csv');fits=pd.read_csv(out/'refits.csv');weights=pd.read_csv(out/'weights.csv')
    baseline=pd.read_csv(out/'baseline_markers.csv')
    spectra=pd.read_csv(out/'spectra.csv')
    sensors=[f's{i}' for i in range(1,22)]
    max_kkt=0.;checked=0;changes=[]
    for subset in ['FD001','FD003']:
        data=p10.read_inputs('train',subset)
        for repeat,seed in enumerate(p10.SEEDS,1):
            for split in p10.partitions(seed):
                fold=split['fold'];base=joblib.load(p10.OUT/f'models_{subset}_r{repeat}_f{fold}.joblib')['health']
                fit=p10.complete_labels(data.loc[data.unit.isin(split['fit'])].reset_index(drop=True))
                x=p10.p05.standardise(p10.centred_sensors(fit),base['stats'])[fit.cycle.ge(20)]
                w=p10.p05.equal_engine_weights(fit.loc[fit.cycle.ge(20),'unit'])
                gram=x.T@(w[:,None]*x)
                eigen=np.linalg.eigvalsh(gram)
                assert eigen[0]>0
                row_s=spectra.loc[(spectra.subset==subset)&(spectra.repeat==repeat)&(spectra.fold==fold)].iloc[0]
                np.testing.assert_allclose(np.sqrt(eigen[-1]/eigen[0]),row_s.condition,rtol=1e-8)
                active=base['beta']>1e-8
                ea=np.linalg.eigvalsh(gram[np.ix_(active,active)])
                np.testing.assert_allclose(np.sqrt(ea[-1]/ea[0]),row_s.active_condition,rtol=1e-8)
                ridge=base['config']['ridge']
                np.testing.assert_allclose(np.sqrt((eigen[-1]+ridge)/(eigen[0]+ridge)),row_s.penalized_condition,rtol=1e-8)
                ev=data.loc[data.unit.isin(split['evaluation'])].reset_index(drop=True)
                _,h=p10.features(ev,base)
                for unit,g in h.groupby('unit'):
                    hits=g.loc[g.hi.le(.5),'cycle'];value=hits.min() if len(hits) else np.nan
                    saved=baseline.loc[(baseline.subset==subset)&(baseline.repeat==repeat)&(baseline.unit==unit)].crossing.iloc[0]
                    np.testing.assert_allclose(value,saved,equal_nan=True)
                selected=fits.loc[(fits.subset==subset)&(fits.repeat==repeat)&(fits.fold==fold)]
                if selected.empty: continue
                raw=p10.centred_sensors(ev)[sensors].to_numpy()
                mask=ev.cycle.ge(20).to_numpy()
                for row in selected.itertuples():
                    reduced=data.loc[data.unit.isin(json.loads(row.fit_units))].reset_index(drop=True)
                    labelled=p10.complete_labels(reduced);centred=p10.centred_sensors(labelled)
                    stats=base['stats'] if row.variant=='coefficients' else p10.p05.fitting_stats(labelled,json.loads(row.fit_units),centred)
                    wr=weights.loc[(weights.subset==subset)&(weights.repeat==repeat)&(weights.removed==row.removed)&(weights.variant==row.variant)].set_index('sensor').reindex(sensors)
                    effective=wr.refit.to_numpy()
                    beta=np.array([effective[sensors.index(s)]*scale/direction for s,scale,direction in zip(stats['channels'],stats['scale'],stats['direction'])])
                    assert np.min(beta)>=-1e-12
                    excluded=set(sensors)-set(stats['channels'])
                    assert all(abs(effective[sensors.index(s)])<1e-12 for s in excluded)
                    x=p10.p05.standardise(centred,stats)[labelled.cycle.ge(20)]
                    target=1-np.minimum(1,labelled.loc[labelled.cycle.ge(20),'rul'].to_numpy()/base['config']['tau'])**base['config']['gamma']
                    w=p10.p05.equal_engine_weights(labelled.loc[labelled.cycle.ge(20),'unit'])
                    resid=x@beta-target;pen=base['config']['ridge']
                    np.testing.assert_allclose(np.sum(w*resid**2),row.mse,atol=1e-10)
                    np.testing.assert_allclose(pen*(beta@beta),row.penalty,atol=1e-10)
                    gradient=x.T@(w*resid)+pen*beta
                    active=beta>1e-8
                    violation=max(float(np.max(abs(gradient[active]))) if active.any() else 0.,
                                  float(np.max(np.maximum(0,-gradient[~active])))) if (~active).any() else float(np.max(abs(gradient)))
                    assert violation<1e-7,(subset,repeat,row.removed,row.variant,violation)
                    max_kkt=max(max_kkt,violation)
                    prediction=np.clip(1-raw@effective,0,1)
                    base_h=np.clip(1-raw@wr.baseline.to_numpy(),0,1)
                    saved=effects.loc[(effects.subset==subset)&(effects.repeat==repeat)&(effects.removed==row.removed)&(effects.variant==row.variant)]
                    for result in saved.itertuples():
                        own=mask&ev.unit.eq(result.unit).to_numpy();a=prediction[own];b=base_h[own]
                        cycles=ev.loc[own,'cycle'].to_numpy();hits=cycles[a<=.5]
                        crossing=hits[0] if len(hits) else np.nan
                        np.testing.assert_allclose(crossing,result.refit,equal_nan=True)
                        np.testing.assert_allclose(np.sqrt(np.mean((a-b)**2)),result.hi_rmse,atol=1e-10)
                        checked+=1
                    original=dict(zip(base['stats']['channels'],base['stats']['direction']))
                    current=dict(zip(stats['channels'],stats['direction']))
                    flips=[s for s in original.keys()&current.keys() if original[s]!=current[s]]
                    changes.append(dict(subset=subset,repeat=repeat,removed=row.removed,variant=row.variant,
                                        direction_flips=','.join(sorted(flips)),added=','.join(sorted(current.keys()-original.keys())),
                                        dropped=','.join(sorted(original.keys()-current.keys()))))
    pd.DataFrame(changes).to_csv(out/'preprocessing_changes.csv',index=False)
    result=dict(passed=True,reconstructed_baselines=600,checked_spectra=60,reconstructed_responses=checked,
                checked_optima=300,max_kkt_violation=max_kkt,
                note='KKT conditions check the saved convex nonnegative solutions; this is not a physical validation.')
    (out/'deep_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':
    with threadpool_limits(limits=1): main()
