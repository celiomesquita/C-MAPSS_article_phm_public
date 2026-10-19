"""P13.2: full frozen-chain explanations and causal-prefix measurement perturbations."""
import json
import platform
from datetime import datetime,timezone
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits
import explainability_core_13b as core
import pilot_f_uncertainty_10 as p10
import pilot_policy_selection_13a as p13
import pilot_removal_11 as p11

ROOT=p11.ROOT
OUT=ROOT/'experiments/artifacts/pilot_explainability_13b'
KEYS=['subset','repeat','fold','unit']


def integrity():
    result={}
    for folder in sorted((ROOT/'experiments/artifacts').glob('pilot_*')):
        m=folder/'manifest.json'
        if folder==OUT or not m.exists():continue
        for name,digest in json.loads(m.read_text(encoding='utf-8')).items():
            assert p11.sha(folder/name)==digest,(folder.name,name)
        result[folder.name]=p11.sha(m)
    return result


def refresh_manifest():
    (OUT/'manifest.json').write_text(json.dumps({f.name:p11.sha(f) for f in sorted(OUT.iterdir())
                                                if f.is_file() and f.name!='manifest.json'},indent=2),encoding='utf-8')


def prefix_support(outside,cutoff):
    return ~outside[:,4:max(5,int(cutoff)-1)].any(axis=1)


def policy_records(rows,meta,paths,cycles,ISO,RF,variants,outside,phase,cutoff=None):
    result=[]
    V=paths.shape[0]
    acts=core.actions(rows,cycles,paths,ISO,RF)
    accumulated=np.cumsum(outside,axis=1)
    for r,a in zip(rows.itertuples(),acts):
        cuts=np.where(np.isfinite(a['decision']),a['decision'],cycles[-1]).astype(int)
        loc=np.clip(cuts-2,4,outside.shape[1]-1)
        within=(accumulated[np.arange(V),loc]-accumulated[:,3])==0
        base_cut=min(r.decision if r.has_decision else cycles[-1],cycles[-1])
        base_within=(accumulated[0,int(base_cut)-2]-accumulated[0,3])==0
        for v in variants.itertuples():
            k=v.variant
            t=a['decision'][k]
            support_cut=t if np.isfinite(t) else cycles[-1]
            base_cut=r.decision if r.has_decision else cycles[-1]
            in_support=bool(within[k] and base_within)
            result.append(meta|dict(policy_id=r.policy_id,method=r.method,delay=r.delay,phase=phase,
                cutoff=cutoff if cutoff is not None else np.nan,variant=k,kind=v.kind,direction=v.direction,
                sensor=v.sensor,epsilon=v.epsilon,sign=v.sign,decision=t,scheduled=a['scheduled'][k],
                base_decision=r.decision,base_scheduled=r.scheduled,delta_removal=a['scheduled'][k]-r.scheduled,
                missing=bool(a['missing'][k]),base_missing=not r.has_decision,
                late=bool(a['late'][k]),exact=bool(a['exact'][k]),reached=bool(a['reached'][k]),
                base_reached=bool(r.reached_endpoint),within_support=in_support,
                selection_feasible=r.selection_feasible))
    return result


def baseline_phase(splits,inputs,decisions):
    audit=[];snapshots=[]
    for split in splits:
        s,rep,fold=split['subset'],split['repeat'],split['fold'];tag=f'{s}_r{rep}_f{fold}'
        bundle=joblib.load(p10.OUT/f'models_{tag}.joblib')
        archived=pd.read_csv(p10.OUT/f'predictions_{tag}_complete.csv.gz')
        dataset=inputs[s].loc[inputs[s].unit.isin(split['evaluation'])].reset_index(drop=True)
        rows=decisions.loc[decisions.subset.eq(s)&decisions.repeat.eq(rep)&decisions.fold.eq(fold)]
        records=[];stored={name:[] for name in ['unit','cycle','C','radial','H','slope','ISO','RF','common']}
        nodes=bundle['predictors']['ISO']['model']
        pd.DataFrame(dict(hi=nodes.X_thresholds_,rul=nodes.y_thresholds_)).to_csv(OUT/f'iso_nodes_{tag}.csv',index=False)
        for unit,g in dataset.groupby('unit',sort=True):
            g=g.sort_values('cycle');raw=g[core.SENSORS].to_numpy();cycles=g.cycle.to_numpy();end=int(cycles[-1])
            C,channels,weights=core.base_contributions(raw,bundle['health'])
            H,slopes=core.health_paths(C,channels,weights,np.zeros((1,21)),cycles)
            ISO,RF=core.forecasts(bundle,H,slopes)
            predictions=archived.loc[archived.unit.eq(unit)]
            maxdif=0.
            for method,array in [('ISO',ISO),('RF_SLOPE',RF)]:
                target=predictions.loc[predictions.method.eq(method)].sort_values('cycle')
                np.testing.assert_allclose(H[0,19:],target.hi,atol=1e-9,rtol=0)
                np.testing.assert_allclose(slopes[0,19:],target.h_slope,atol=1e-9,rtol=0)
                err=float(np.max(abs(array[0,19:]-target.predicted_rul.to_numpy())))
                maxdif=max(maxdif,err);assert err<=1e-9
            # Compare the explicit tree average with the public predictor on all baseline points.
            x=np.c_[H[0,19:],slopes[0,19:]]
            public=bundle['predictors']['RF_SLOPE']['model'].predict(x)
            np.testing.assert_allclose(RF[0,19:],public,atol=1e-9,rtol=0)
            hh,radial,total=core.bounded_contributions(C[19:])
            np.testing.assert_allclose(hh,H[0],atol=1e-9,rtol=0)
            np.testing.assert_allclose(radial.sum(axis=1),1-hh,atol=1e-9,rtol=0)
            group=rows.loc[rows.unit.eq(unit)]
            active=group.loc[group.method.ne('AGE')&group.has_decision,'decision']
            common_end=int(active.min()) if len(active) else end-1
            t=cycles[19:-1];common=(t>=39)&((t-39)%5==0)&(t<=common_end)
            actions=core.actions(group,t,H[:,:-1],ISO[:,:-1],RF[:,:-1])
            for r,a in zip(group.itertuples(),actions):
                np.testing.assert_allclose([r.decision,r.scheduled],[a['decision'][0],a['scheduled'][0]],atol=0,rtol=0,equal_nan=True)
                limit=int(r.decision) if r.has_decision else end-1
                times=set(range(39,limit+1,5))
                if np.isfinite(r.first_available): times.add(int(r.first_available))
                if r.has_decision: times.add(int(r.decision))
                crossing=predictions.crossing.iloc[0]
                if np.isfinite(crossing) and crossing<=limit:times.add(int(crossing))
                for time in sorted(x for x in times if 20<=x<=limit):
                    k=time-20;forecast=ISO[0,k] if r.method=='ISO' else RF[0,k] if r.method=='RF_SLOPE' else np.nan
                    q=r.q_late if np.isfinite(r.q_late) else 0.
                    lead=max(0.,forecast-q) if np.isfinite(forecast) else np.nan
                    snapshots.append(dict(subset=s,repeat=rep,fold=fold,unit=int(unit),policy_id=r.policy_id,
                        cycle=time,endpoint=end,hi=H[0,k],slope=slopes[0,k],ISO=ISO[0,k],RF=RF[0,k],
                        prediction=forecast,q_late=q,lower_lead=lead,reserve=r.reserve,delay=r.delay,
                        trigger_threshold=r.reserve+r.delay,decision=r.decision,scheduled=r.scheduled,
                        is_decision=bool(r.has_decision and time==r.decision),
                        before_availability=time<39,selection_feasible=r.selection_feasible,
                        actual_rul=end-time,retrospective_error=forecast-(end-time)))
            for name,value in dict(unit=np.full(len(t),unit),cycle=t,C=C[19:-1],radial=radial[:-1],
                                  H=H[0,:-1],slope=slopes[0,:-1],ISO=ISO[0,:-1],RF=RF[0,:-1],common=common).items():
                stored[name].append(value)
            audit.append(dict(subset=s,repeat=rep,fold=fold,unit=int(unit),actions_checked=len(group),
                              maximum_prediction_difference=maxdif,contribution_identity=True))
        np.savez_compressed(OUT/f'baseline_{tag}.npz',**{k:np.concatenate(v) for k,v in stored.items()})
        print(tag,'baseline verified',flush=True)
    pd.DataFrame(audit).to_csv(OUT/'baseline_audit.csv',index=False)
    pd.DataFrame(snapshots).to_csv(OUT/'policy_snapshots.csv.gz',index=False,compression='gzip')
    assert len(audit)==600 and sum(x['actions_checked'] for x in audit)==9600
    (OUT/'baseline_complete.json').write_text(json.dumps(dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),
                audited_actions=9600),indent=2),encoding='utf-8')


def perturbation_phase(splits,inputs,decisions):
    for split in splits:
        s,rep,fold=split['subset'],split['repeat'],split['fold'];tag=f'{s}_r{rep}_f{fold}'
        bundle=joblib.load(p10.OUT/f'models_{tag}.joblib')
        noise=core.noise_model(inputs[s].loc[inputs[s].unit.isin(split['fit'])])
        assert noise['fit_units']==sorted(split['fit'])
        joblib.dump(noise,OUT/f'noise_{tag}.joblib',compress=3)
        variants,shifts=core.variants(noise)
        variants.to_csv(OUT/f'variants_{tag}.csv',index=False)
        np.savez_compressed(OUT/f'shifts_{tag}.npz',shifts=shifts)
        rows=decisions.loc[decisions.subset.eq(s)&decisions.repeat.eq(rep)&decisions.fold.eq(fold)]
        global_records=[];local_records=[];sensitivities=[];local_sensitivity=[];support_rows=[]
        saved={name:[] for name in ['unit','cycle','H','slope','ISO','RF','outside']}
        base=np.load(OUT/f'baseline_{tag}.npz')
        for unit,group in rows.groupby('unit',sort=True):
            source=inputs[s].loc[inputs[s].unit.eq(unit)].sort_values('cycle')
            end=int(source.cycle.max());raw=source[core.SENSORS].to_numpy()[:-1];cycles=np.arange(1,end)
            C,channels,weights=core.base_contributions(raw,bundle['health'])
            H,slopes=core.health_paths(C,channels,weights,shifts,cycles)
            ISO,RF=core.forecasts(bundle,H,slopes)
            outside=core.support(raw,cycles,shifts,noise)
            t=cycles[19:];bmask=base['unit']==unit;common=base['common'][bmask]
            meta=dict(subset=s,repeat=rep,fold=fold,unit=int(unit),endpoint=end)
            for field,array in [('H',H),('slope',slopes),('ISO',ISO),('RF',RF)]:
                np.testing.assert_allclose(array[0],base[field][bmask],atol=1e-9,rtol=0,equal_nan=True)
            global_records+=policy_records(group,meta,H,t,ISO,RF,variants,outside,'global')
            for v in variants.itertuples():
                k=v.variant;pair=(~outside[0,18:])&(~outside[k,18:])&common
                for method,array in [('ISO',ISO),('RF_SLOPE',RF)]:
                    delta=array[k]-array[0]
                    sensitivities.append(meta|dict(phase='global',variant=k,kind=v.kind,direction=v.direction,sensor=v.sensor,
                        epsilon=v.epsilon,sign=v.sign,method=method,common_count=int(common.sum()),support_count=int(pair.sum()),
                        mean_abs_delta_hi=float(np.mean(abs(H[k,common]-H[0,common]))),
                        mean_abs_delta_rul=float(np.mean(abs(delta[common]))),
                        supported_abs_delta_rul=float(np.mean(abs(delta[pair]))) if pair.any() else np.nan,
                        mean_delta_rul=float(np.mean(delta[common])),max_abs_delta_rul=float(np.nanmax(abs(delta[19:])))))
                support_rows.append(meta|dict(variant=k,kind=v.kind,direction=v.direction,epsilon=v.epsilon,sign=v.sign,
                    increments=len(cycles)-5,outside_count=int(outside[k,4:].sum()),
                    common_count=int(common.sum()),common_outside=int(outside[k,18:][common].sum())))
            for name,value in dict(unit=np.full(len(t),unit),cycle=t,H=H,slope=slopes,ISO=ISO,RF=RF,outside=outside[:,18:]).items():
                saved[name].append(value)
            # Group equal local cutoffs; the same raw intervention is then shared across policies.
            cutoffs=np.where(group.has_decision,group.decision,end-1).astype(int)
            for cutoff in sorted(set(cutoffs)):
                local_group=group.loc[cutoffs==cutoff]
                X=raw[:cutoff];ct=cycles[:cutoff]
                lc=C[:cutoff]
                LH,LS=core.health_paths(lc,channels,weights,shifts,ct,cutoff)
                LI,LR=core.forecasts(bundle,LH,LS,RF[0,:cutoff-19],max(39,cutoff-19))
                lo=core.support(X,ct,shifts,noise,cutoff)
                local_records+=policy_records(local_group,meta,LH,ct[19:],LI,LR,variants,lo,'local',cutoff)
                for v in variants.itertuples():
                    k=v.variant
                    for method,array in [('ISO',LI),('RF_SLOPE',LR)]:
                        local_sensitivity.append(meta|dict(cutoff=cutoff,variant=k,kind=v.kind,direction=v.direction,
                            epsilon=v.epsilon,sign=v.sign,method=method,hi=LH[k,-1],slope=LS[k,-1],
                            prediction=array[k,-1],base_prediction=array[0,-1],delta_prediction=array[k,-1]-array[0,-1],
                            inside_pair=bool(not lo[k,-1] and not lo[0,-1])))
        np.savez_compressed(OUT/f'global_paths_{tag}.npz',**{k:np.concatenate(v,axis=1 if k in ['H','slope','ISO','RF','outside'] else 0) for k,v in saved.items()})
        for name,records in [('global_actions',global_records),('local_actions',local_records),
                             ('sensitivity',sensitivities),('local_sensitivity',local_sensitivity),('support',support_rows)]:
            pd.DataFrame(records).to_csv(OUT/f'{name}_{tag}.csv.gz',index=False,compression='gzip')
        print(tag,f'{len(variants)} variants, global/local replay complete',flush=True)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    assert not (OUT/'execution_start.json').exists(),'Preserve existing run; diagnose before restarting'
    prior=integrity()
    sources=['pilot_explainability_13b.py','explainability_core_13b.py','test_explainability_13b.py',
             'verify_pilot_explainability_13b.py','protocolo_explicabilidade_13b.md','protocolo_explicabilidade_13b_implementacao.md',
             'pilot_f_uncertainty_10.py','pilot_policy_selection_13a.py','pilot_removal_11.py']
    files=[ROOT/'experiments'/name for name in sources]
    files+=[p10.OUT/'splits.json',p13.OUT/'decisions.csv',p13.OUT/'selections.csv',
            ROOT/'experiments/artifacts/pilot_loss_decomposition_11b/verification.json']
    files+=sorted(p10.OUT.glob('models_*.joblib'))+sorted(p10.OUT.glob('predictions_*_complete.csv.gz'))
    files+=[ROOT/f'CMAPSSData/train_{s}.txt' for s in ['FD001','FD003']]
    meta=dict(started_utc=datetime.now(timezone.utc).isoformat(),previous_manifests=prior,
              inputs={str(f.relative_to(ROOT)):p11.sha(f) for f in files},python=platform.python_version(),
              numpy=np.__version__,pandas=pd.__version__,no_refitting=True,no_inspection=True)
    (OUT/'execution_start.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    splits=json.loads((p10.OUT/'splits.json').read_text(encoding='utf-8'))
    inputs={s:p10.read_inputs('train',s) for s in ['FD001','FD003']}
    decisions=pd.read_csv(p13.OUT/'decisions.csv')
    baseline_phase(splits,inputs,decisions)
    (OUT/'perturbations_start.json').write_text(json.dumps(dict(timestamp_utc=datetime.now(timezone.utc).isoformat()),indent=2))
    perturbation_phase(splits,inputs,decisions)
    assert integrity()==prior
    meta.update(finished_utc=datetime.now(timezone.utc).isoformat(),previous_artifacts_intact=True,
                folds=60,baseline_actions=9600)
    (OUT/'metadata.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    refresh_manifest()


if __name__=='__main__':
    with threadpool_limits(limits=1):main()
