"""Engine-level ranks, fidelity diagnostics, stability, and paired P13.2 contrasts."""
import itertools
import json
import joblib
import numpy as np
import pandas as pd
from scipy.stats import spearmanr
import pilot_explainability_13b as p

K=['subset','repeat','fold','unit']


def rank_comparison(a,b):
    valid=np.isfinite(a)&np.isfinite(b)
    x,y=np.asarray(a)[valid],np.asarray(b)[valid]
    identified=len(x)>1 and np.ptp(x)>0 and np.ptp(y)>0
    rho=float(spearmanr(x,y).statistic) if identified else np.nan
    ix=np.flatnonzero(valid)
    top=lambda z:sorted(ix,key=lambda j:(-z[j],j))[:5]
    ta,tb=top(np.asarray(a)),top(np.asarray(b))
    def boundary(z,t):
        return bool(t and sum(z[valid]==z[t[-1]])>sum(z[t]==z[t[-1]]))
    return dict(channels=int(valid.sum()),identified=identified,spearman=rho,
                shared_top5=len(set(ta)&set(tb)),top5_fraction=len(set(ta)&set(tb))/min(5,len(ix)) if len(ix) else np.nan,
                boundary_tie_a=boundary(np.asarray(a),ta),boundary_tie_b=boundary(np.asarray(b),tb))


def engine_actions(frame):
    rows=[]
    keys=K+['policy_id','method','delay','phase','kind','epsilon']
    for key,g in frame.loc[frame.epsilon.gt(0)].groupby(keys,sort=True):
        present=g.decision.notna();base=g.base_decision.notna();both=present&base
        supported=g.within_support&both
        delta=g.delta_removal.abs()
        rows.append(dict(zip(keys,key))|dict(variants=len(g),paired_dates=int(both.sum()),
            mean_abs_delta=float(delta.loc[both].mean()) if both.any() else np.nan,
            max_abs_delta=float(delta.loc[both].max()) if both.any() else np.nan,
            same_fraction=float(g.delta_removal.loc[both].eq(0).mean()) if both.any() else np.nan,
            shift_gt1=float(delta.loc[both].gt(1).mean()) if both.any() else np.nan,
            shift_gt2=float(delta.loc[both].gt(2).mean()) if both.any() else np.nan,
            presence_delta=float((present.astype(int)-base.astype(int)).mean()),
            presence_flip=float((present!=base).mean()),reached_fraction=float(g.reached.mean()),
            reached_delta=float((g.reached.astype(int)-g.base_reached.astype(int)).mean()),
            supported_variants=int(supported.sum()),
            supported_mean_abs_delta=float(delta.loc[supported].mean()) if supported.any() else np.nan))
    return pd.DataFrame(rows)


def paired_action_contrasts(frame):
    records=[]
    raw=frame.loc[frame.epsilon.gt(0)]
    keys=K+['phase','kind','epsilon','variant']
    for policy,g in raw.loc[raw.method.isin(['HI_THRESHOLD_SELECTED','HI_WAIT_SELECTED'])].groupby('policy_id',sort=True):
        delay=int(g.delay.iloc[0])
        for reference in [f'HI_MARKER_D{delay}',f'ISO_LOWER98_M15_D{delay}']:
            ref=raw.loc[raw.policy_id.eq(reference)]
            merged=g.merge(ref,on=keys,suffixes=('_a','_b'),validate='one_to_one')
            for key,x in merged.groupby(K+['phase','kind','epsilon'],sort=True):
                finite=x.delta_removal_a.notna()&x.delta_removal_b.notna()
                present_a=x.decision_a.notna().astype(int)-x.base_decision_a.notna().astype(int)
                present_b=x.decision_b.notna().astype(int)-x.base_decision_b.notna().astype(int)
                records.append(dict(zip(K+['phase','kind','epsilon'],key))|dict(policy_id=policy,reference=reference,
                    date_pairs=int(finite.sum()),value=float((x.delta_removal_a.abs()-x.delta_removal_b.abs()).loc[finite].mean()) if finite.any() else np.nan,
                    presence_difference=float((present_a-present_b).mean())))
    return pd.DataFrame(records)


def boot_contrasts(engine,indices):
    keys=['subset','repeat','phase','kind','epsilon','policy_id','reference']
    result=[]
    for key,g in engine.groupby(keys,sort=True):
        g=g.set_index('unit').reindex(range(1,101))
        ix=indices[f'{key[0]}_r{key[1]}']
        row=dict(zip(keys,key))
        for metric in ['value','presence_difference']:
            x=g[metric].to_numpy(dtype=float);ok=np.isfinite(x)
            weights=ok[ix];den=weights.sum(axis=1)
            sums=np.where(np.isfinite(x),x,0)[ix].sum(axis=1)
            boot=np.divide(sums,den,out=np.full(len(ix),np.nan),where=den>0)
            row[metric]=float(x[ok].mean()) if ok.any() else np.nan
            ci=np.nanquantile(boot,[.025,.975]) if np.isfinite(boot).any() else [np.nan,np.nan]
            row[metric+'_lo'],row[metric+'_hi']=ci
            row[metric+'_engines']=int(ok.sum());row[metric+'_empty_bootstrap']=int((den==0).sum())
        result.append(row)
    return pd.DataFrame(result)


def main():
    out=p.OUT
    assert (out/'metadata.json').exists()
    decisions=pd.read_csv(p.p13.OUT/'decisions.csv')
    splits=json.loads((p.p10.OUT/'splits.json').read_text())
    attribution=[];rank_sensitivity=[];engines=[];pairs=[];forecast_pairs=[];mechanism=[];support_all=[];triggers=[]
    common_profiles={}
    for split in splits:
        s,rep,fold=split['subset'],split['repeat'],split['fold'];tag=f'{s}_r{rep}_f{fold}'
        b=np.load(out/f'baseline_{tag}.npz');g=np.load(out/f'global_paths_{tag}.npz')
        model=joblib.load(p.p10.OUT/f'models_{tag}.joblib');included=set(model['health']['stats']['channels'])
        variants=pd.read_csv(out/f'variants_{tag}.csv').fillna('')
        shifts=np.load(out/f'shifts_{tag}.npz')['shifts']
        channels=np.array([p.core.SENSORS.index(x) for x in model['health']['stats']['channels']])
        coef=model['health']['beta']*model['health']['stats']['direction']/model['health']['stats']['scale']
        direction=shifts[:,channels]@coef
        for unit in split['evaluation']:
            m=b['unit']==unit;common=b['common'][m];C=b['C'][m]
            cp=C[common];common_profiles[(s,rep,unit)]=(b['cycle'][m][common],cp)
            for j,sensor in enumerate(p.core.SENSORS):
                attribution.append(dict(subset=s,repeat=rep,fold=fold,unit=unit,sensor=sensor,included=sensor in included,
                    instants=len(cp),mean_abs=float(np.mean(abs(cp[:,j]))),mean_signed=float(cp[:,j].mean())))
            unit_rows=decisions.loc[decisions.subset.eq(s)&decisions.repeat.eq(rep)&decisions.fold.eq(fold)&decisions.unit.eq(unit)]
            times=b['cycle'][m];hi=b['H'][m]
            hits=np.flatnonzero(hi<=.5);gate=max(39,int(times[hits[0]])) if len(hits) else np.nan
            for r in unit_rows.itertuples():
                cutoff=int(r.decision) if r.has_decision else int(times[-1])
                k=int(np.flatnonzero(times==cutoff)[0])
                prediction=b['ISO'][m][k] if r.method=='ISO' else b['RF'][m][k] if r.method=='RF_SLOPE' else np.nan
                lower=max(0.,prediction-r.q_late) if np.isfinite(prediction) else np.nan
                triggers.append(dict(subset=s,repeat=rep,fold=fold,unit=unit,policy_id=r.policy_id,method=r.method,
                    anchor=r.anchor,cutoff=cutoff,has_decision=r.has_decision,decision=r.decision,scheduled=r.scheduled,
                    gate=gate,at_gate=bool(r.has_decision and r.decision==gate),hi=hi[k],slope=b['slope'][m][k],
                    prediction=prediction,q_late=r.q_late,lower=lower,reserve=r.reserve,delay=r.delay,
                    lower_zero=bool(np.isfinite(lower) and lower==0),
                    central_would_trigger=bool(np.isfinite(prediction) and prediction<=r.reserve+r.delay+1e-9),
                    actual_rul=r.endpoint-cutoff,forecast_error=prediction-(r.endpoint-cutoff)))
            H=g['H'][:,g['unit']==unit]
            delta=H-H[0]
            wrong=((direction[:,None]>0)&(delta>1e-9))|((direction[:,None]<0)&(delta< -1e-9))
            mechanism.append(dict(subset=s,repeat=rep,fold=fold,unit=unit,
                sign_checks=int(delta.size),sign_violations=int(wrong.sum()),
                saturated_low=float((H[0]<=0).mean()),saturated_high=float((H[0]>=1).mean())))
        sens=pd.read_csv(out/f'sensitivity_{tag}.csv.gz').fillna({'sensor':''})
        sup=pd.read_csv(out/f'support_{tag}.csv.gz');support_all.append(sup)
        for method,x in sens.loc[sens.kind.eq('channel')&sens.epsilon.eq(.5)].groupby('method'):
            for unit,y in x.groupby('unit'):
                by=y.groupby('sensor')[['mean_abs_delta_rul','mean_abs_delta_hi']].mean()/.5
                for sensor in p.core.SENSORS:
                    score=by.loc[sensor] if sensor in by.index else None
                    rank_sensitivity.append(dict(subset=s,repeat=rep,fold=fold,unit=unit,sensor=sensor,method=method,
                        prediction=score.mean_abs_delta_rul if score is not None else 0. if sensor not in included else np.nan,
                        health=score.mean_abs_delta_hi if score is not None else 0. if sensor not in included else np.nan))
        # Paired prognostic sensitivity: identical engines/directions/signs/amplitudes/instants.
        t=sens.loc[sens.epsilon.gt(0)]
        paired=t.loc[t.method.eq('ISO')].merge(t.loc[t.method.eq('RF_SLOPE')],on=K+['phase','variant','kind','direction','sensor','epsilon','sign'],suffixes=('_a','_b'),validate='one_to_one')
        for key,x in paired.groupby(K+['phase','kind','epsilon'],sort=True):
            forecast_pairs.append(dict(zip(K+['phase','kind','epsilon'],key))|dict(policy_id='ISO',reference='RF_SLOPE',
                value=float((x.mean_abs_delta_rul_a-x.mean_abs_delta_rul_b).mean()),presence_difference=np.nan))
        for phase in ['global','local']:
            frame=pd.read_csv(out/f'{phase}_actions_{tag}.csv.gz')
            engines.append(engine_actions(frame));pairs.append(paired_action_contrasts(frame))
        print(tag,'engine summaries complete',flush=True)
    attr=pd.DataFrame(attribution);sensrank=pd.DataFrame(rank_sensitivity)
    engine=pd.concat(engines,ignore_index=True);contrast_engine=pd.concat(pairs,ignore_index=True)
    rng=np.random.default_rng(20261017)
    indices={f'{s}_r{rep}':rng.integers(0,100,(2000,100)) for s in ['FD001','FD003'] for rep in [1,2,3]}
    np.savez_compressed(out/'bootstrap_indices.npz',**indices)
    contrast=boot_contrasts(contrast_engine,indices)
    fcontrast=boot_contrasts(pd.DataFrame(forecast_pairs),indices)
    # Ranked vectors: every engine has equal weight before aggregation.
    vectors=[]
    for key,x in attr.groupby(['subset','repeat','fold','sensor'],sort=True):
        vectors.append(dict(zip(['subset','repeat','fold','sensor'],key))|dict(kind='contribution',score=x.mean_abs.mean()))
    for key,x in sensrank.groupby(['subset','repeat','fold','sensor','method'],sort=True):
        common=dict(zip(['subset','repeat','fold','sensor','method'],key))
        vectors.append(common|dict(kind='prediction_'+key[-1],score=x.prediction.mean()))
        if key[-1]=='ISO':vectors.append(common|dict(kind='sensitivity_HI',score=x.health.mean()))
    vr=pd.DataFrame(vectors);comparisons=[]
    for (s,rep,kind),x in vr.groupby(['subset','repeat','kind'],sort=True):
        for fa,fb in itertools.combinations(sorted(x.fold.unique()),2):
            va=x.loc[x.fold.eq(fa)].set_index('sensor').reindex(p.core.SENSORS).score.to_numpy()
            vb=x.loc[x.fold.eq(fb)].set_index('sensor').reindex(p.core.SENSORS).score.to_numpy()
            comparisons.append(dict(subset=s,repeat=rep,kind=kind,fold_a=fa,fold_b=fb,comparison='between_folds',**rank_comparison(va,vb)))
    for key,x in vr.groupby(['subset','repeat','fold'],sort=True):
        base=x.loc[x.kind.eq('contribution')].set_index('sensor').reindex(p.core.SENSORS).score.to_numpy()
        for kind in ['sensitivity_HI','prediction_ISO','prediction_RF_SLOPE']:
            other=x.loc[x.kind.eq(kind)].set_index('sensor').reindex(p.core.SENSORS).score.to_numpy()
            comparisons.append(dict(subset=key[0],repeat=key[1],kind=kind,fold_a=key[2],fold_b=key[2],comparison='contribution_vs_sensitivity',**rank_comparison(base,other)))
    dates=[];profiles=[]
    for s in ['FD001','FD003']:
        for ra,rb in itertools.combinations([1,2,3],2):
            pop=decisions.loc[decisions.subset.eq(s)]
            paired=pop.loc[pop.repeat.eq(ra)].merge(pop.loc[pop.repeat.eq(rb)],on=['unit','policy_id'],suffixes=('_a','_b'),validate='one_to_one')
            for r in paired.itertuples():
                dates.append(dict(subset=s,unit=r.unit,policy_id=r.policy_id,repeat_a=ra,repeat_b=rb,
                    delta_abs=abs(r.scheduled_a-r.scheduled_b),presence_discordant=r.has_decision_a!=r.has_decision_b))
            for unit in range(1,101):
                ta,ca=common_profiles[(s,ra,unit)];tb,cb=common_profiles[(s,rb,unit)]
                common,ia,ib=np.intersect1d(ta,tb,return_indices=True)
                a=abs(ca[ia]).mean(axis=0);b=abs(cb[ib]).mean(axis=0)
                profiles.append(dict(subset=s,unit=unit,repeat_a=ra,repeat_b=rb,common_instants=len(common),**rank_comparison(a,b)))
    # Inventory all adverse/infeasible cases, plus deterministic retrospective examples.
    decisions=decisions.copy()
    decisions['infeasible']=decisions.selection_feasible.eq(False)
    reasons=[]
    for r in decisions.loc[decisions.reached_endpoint|decisions.infeasible].itertuples():
        reasons.append(dict(subset=r.subset,repeat=r.repeat,unit=r.unit,reason='adverse_or_infeasible'))
    for (s,rep,d),x in decisions.groupby(['subset','repeat','delay']):
        totals=x.groupby('unit').agg(unused=('utilised',lambda v:0.),spread=('scheduled',lambda v:v.max()-v.min()))
        unused=x.assign(w=x.endpoint-x.utilised).groupby('unit').w.max()
        reasons.append(dict(subset=s,repeat=rep,unit=int(unused.sort_values(ascending=False,kind='stable').index[0]),reason=f'max_unused_d{d}'))
        ordered=totals.reset_index().sort_values(['spread','unit'],kind='stable')
        maxspread=ordered.spread.max();first=ordered.loc[ordered.spread.eq(maxspread)].unit.min()
        reasons.append(dict(subset=s,repeat=rep,unit=int(first),reason=f'max_discordance_d{d}'))
        reasons.append(dict(subset=s,repeat=rep,unit=int(ordered.iloc[(len(ordered)-1)//2].unit),reason=f'median_discordance_d{d}'))
    inventory=pd.DataFrame(reasons).drop_duplicates()
    action_summary=[]
    for key,x in engine.groupby(['subset','repeat','policy_id','phase','kind','epsilon'],sort=True):
        row=dict(zip(['subset','repeat','policy_id','phase','kind','epsilon'],key))|dict(engines=len(x))
        for field in ['mean_abs_delta','max_abs_delta','same_fraction','shift_gt1','shift_gt2','presence_flip','presence_delta','reached_delta','reached_fraction','supported_mean_abs_delta']:
            v=x[field].dropna();row[field]=float(v.mean()) if len(v) else np.nan
            row[field+'_engines']=len(v)
            for q,label in [(.05,'q05'),(.5,'median'),(.95,'q95')]:row[field+'_'+label]=float(v.quantile(q)) if len(v) else np.nan
            row[field+'_max']=float(v.max()) if len(v) else np.nan
        row['supported_variant_fraction']=float((x.supported_variants/x.variants).mean())
        action_summary.append(row)
    tables=dict(attribution_engines=attr,sensor_sensitivity_engines=sensrank,rank_vectors=vr,
        rank_comparisons=pd.DataFrame(comparisons),repeat_dates=pd.DataFrame(dates),repeat_contributions=pd.DataFrame(profiles),
        action_engines=engine,action_summary=pd.DataFrame(action_summary),action_contrast_engines=contrast_engine,
        action_contrasts=contrast,forecast_contrast_engines=pd.DataFrame(forecast_pairs),forecast_contrasts=fcontrast,
        mechanism=pd.DataFrame(mechanism),support=pd.concat(support_all,ignore_index=True),case_inventory=inventory,
        trigger_explanation=pd.DataFrame(triggers))
    for name,table in tables.items():table.to_csv(out/f'{name}.csv',index=False)
    (out/'analysis_metadata.json').write_text(json.dumps(dict(counts={k:len(v) for k,v in tables.items()},
        source_sha256=p.p11.sha(p.ROOT/'experiments/analyse_explainability_13b.py')),indent=2))
    # The final reporter seals these additional files after the independent path audit.


if __name__=='__main__':main()
