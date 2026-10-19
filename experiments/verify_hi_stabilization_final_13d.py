"""Additional post-run check of the 60 final F25 models, never scoring U/E."""
import hashlib
import json
import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits
import pilot_f_uncertainty_10 as p10


def main():
    root=p10.ROOT;out=root/'experiments/artifacts/pilot_hi_stabilization_13d'
    splits=json.loads((p10.OUT/'splits.json').read_text());choices=pd.read_csv(out/'selections.csv')
    datasets={s:p10.read_inputs('train',s) for s in ['FD001','FD003']}
    checked=0;max_kkt=0.
    for sp in splits:
        subset=sp['subset'];rep=sp['repeat'];fold=sp['fold']
        model=joblib.load(out/f'selected_hi_{subset}_r{rep}_f{fold}.joblib')
        assert model['fit_units']==sp['fit']
        row=choices.loc[(choices.subset==subset)&(choices.repeat==rep)&(choices.fold==fold)].iloc[0]
        assert row.selected==model['candidate']
        data=p10.complete_labels(datasets[subset].loc[datasets[subset].unit.isin(sp['fit'])].reset_index(drop=True))
        centred=p10.centred_sensors(data);mask=data.cycle.ge(20)
        scale=centred.loc[mask].std().to_numpy()
        initial=centred.loc[data.cycle.between(15,20)].std().to_numpy()
        signed=model['candidate'].startswith('SIGNED')
        direction=np.ones(21) if signed else np.sign(centred.loc[data.cycle.eq(data.end)].median().to_numpy())
        eligible=(initial>1e-6)&(scale>1e-6)&(direction!=0)
        np.testing.assert_array_equal(eligible,model['eligible'])
        np.testing.assert_array_equal(direction,model['direction'])
        np.testing.assert_allclose(scale,model['scale'],atol=1e-9,rtol=1e-8)
        factor=direction[eligible]/scale[eligible]
        x=centred.loc[mask].to_numpy()[:,eligible]*factor
        beta=model['beta'][eligible];weights=p10.p05.equal_engine_weights(data.loc[mask,'unit'])
        y=1-np.minimum(1,data.loc[mask,'rul'].to_numpy()/p10.CONFIG[subset]['tau'])**p10.CONFIG[subset]['gamma']
        gradient=x.T@(weights*(x@beta-y))+model['alpha']*beta
        active=np.ones(len(beta),bool) if signed else beta>1e-8
        kkt=max(np.max(abs(gradient[active])) if active.any() else 0.,
                np.max(np.maximum(0,-gradient[~active])) if (~active).any() else 0.)
        assert kkt<1e-7
        max_kkt=max(max_kkt,float(kkt));checked+=1
    # Protect all earlier experiments, including supplementary final manifests.
    prior={}
    for folder in sorted((root/'experiments/artifacts').glob('pilot_*')):
        if folder==out: continue
        for name in ['manifest.json','final_manifest.json']:
            manifest=folder/name
            if not manifest.exists(): continue
            records=json.loads(manifest.read_text(encoding='utf-8'))
            for file,digest in records.items():
                assert hashlib.sha256((folder/file).read_bytes()).hexdigest()==digest,(folder.name,file)
            prior[f'{folder.name}/{name}']=len(records)
    result=dict(passed=True,final_F25_fits=checked,maximum_kkt=max_kkt,prior_manifests=prior,
                evaluated_groups='F25 optimisation only; no C/U/E scoring')
    (out/'final_fit_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(passed=True,final_F25_fits=checked,maximum_kkt=max_kkt,prior_files=sum(prior.values()))))


if __name__=='__main__':
    with threadpool_limits(limits=1): main()
