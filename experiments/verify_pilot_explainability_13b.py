"""Independent P13.2 reconstruction using public predictors and raw-prefix algebra."""
import json
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits
import pilot_explainability_13b as p


def predict(bundle,H,slope,baseline=None,start=19):
    iso=bundle['predictors']['ISO']['model']
    I=iso.predict(H.reshape(-1)).reshape(H.shape)
    I[:,:19]=np.nan
    R=np.full_like(H,np.nan) if baseline is None else np.broadcast_to(baseline,H.shape).copy()
    x=np.column_stack((H[:,start:].reshape(-1),slope[:,start:].reshape(-1)))
    R[:,start:]=bundle['predictors']['RF_SLOPE']['model'].predict(x).reshape(H.shape[0],-1)
    return I,R


def reconstruction(raw,health,shifts,cut=None):
    names=p.core.SENSORS
    columns=[names.index(s) for s in health['stats']['channels']]
    # Rolling raw values and added trajectories are evaluated separately.
    means=pd.DataFrame(raw[:,columns]).rolling(15,min_periods=15).mean().to_numpy()
    coef=health['beta']*health['stats']['direction']/health['stats']['scale']
    C=np.zeros_like(raw);C[:,columns]=(means-means[19])*coef
    t=np.arange(1,len(raw)+1)
    if cut is None:g=np.minimum(1,np.maximum(0,(t-20)/20))
    else:g=np.where(t>20,np.minimum(1,np.maximum(0,(t-cut+19)/19)),0)
    m=pd.Series(g).rolling(15,min_periods=15).mean().to_numpy()
    change=np.sum(shifts[:,columns]*coef,axis=1)
    H=np.clip(1-(C.sum(axis=1)[None,:]+change[:,None]*m[None,:]),0,1)[:,19:]
    slope=np.full_like(H,np.nan)
    for j in range(19,H.shape[1]):
        slope[:,j]=((np.arange(20)-9.5)*H[:,j-19:j+1]).sum(axis=1)/665.
    return C[19:],H,slope


def expected_actions(group,cycles,H,I,R):
    result={}
    for r in group.itertuples():
        output=[]
        for k in range(H.shape[0]):
            h=H[k];hits=np.flatnonzero(h<=.5)
            gate=max(39,int(cycles[hits[0]])) if len(hits) else np.nan
            if r.method=='AGE':tau=r.control_age-r.delay
            elif r.method=='HI_MARKER':tau=gate
            elif r.method=='HI_WAIT_SELECTED':tau=gate+r.selected_value
            elif r.method=='HI_THRESHOLD_SELECTED':
                hits=np.flatnonzero(h<=r.selected_value)
                tau=max(39,int(cycles[hits[0]])) if len(hits) else np.nan
            else:
                f=I[k] if r.method=='ISO' else R[k]
                hits=np.flatnonzero((cycles>=39)&(cycles>=gate)&(np.maximum(0,f-r.q_late)<=r.reserve+r.delay+1e-9))
                tau=float(cycles[hits[0]]) if len(hits) else np.nan
            output.append(tau if np.isfinite(tau) and 1<=tau<=cycles[-1] else np.nan)
        result[r.policy_id]=np.array(output)
    return result


def check_actions(table,group,cycles,H,I,R):
    expected=expected_actions(group,cycles,H,I,R)
    for r in group.itertuples():
        g=table.loc[table.policy_id.eq(r.policy_id)].sort_values('variant')
        tau=expected[r.policy_id];rem=tau+r.delay;present=np.isfinite(tau)
        np.testing.assert_allclose(g.decision,tau,atol=0,rtol=0,equal_nan=True)
        np.testing.assert_allclose(g.scheduled,rem,atol=0,rtol=0,equal_nan=True)
        np.testing.assert_array_equal(g.missing,~present)
        np.testing.assert_array_equal(g.late,present&(rem>r.endpoint))
        np.testing.assert_array_equal(g.exact,present&(rem==r.endpoint))
        np.testing.assert_array_equal(g.reached,~present|(rem>=r.endpoint))
        np.testing.assert_allclose(g.delta_removal,rem-r.scheduled,equal_nan=True)


def support_values(raw,shifts,noise,cutoff=None):
    t=np.arange(1,len(raw)+1)
    ramp=np.clip((t-20)/20,0,1) if cutoff is None else np.where(t>20,np.clip((t-cutoff+19)/19,0,1),0.)
    active=noise['active']
    delta=raw[1:,active]-raw[:-1,active]
    z=(delta[None]+np.diff(ramp)[None,:,None]*shifts[:,None,active]-noise['centre'][active])/noise['nu']
    return (np.sum((z@noise['precision'])*z,axis=-1)>noise['md_limit'])|np.any(abs(z)>noise['channel_limits'],axis=-1)


def check_prefix_support(table,group,outside,last):
    for r in group.itertuples():
        frame=table.loc[table.policy_id.eq(r.policy_id)].sort_values('variant')
        baseline=min(r.decision if r.has_decision else last,last)
        original=not outside[0,4:int(baseline)-1].any()
        expected=[]
        for record in frame.itertuples():
            end=record.decision if np.isfinite(record.decision) else last
            expected.append(original and not outside[record.variant,4:int(end)-1].any())
        np.testing.assert_array_equal(frame.within_support,expected)


def main():
    out=p.OUT
    meta=json.loads((out/'metadata.json').read_text(encoding='utf-8'))
    assert p.integrity()==meta['previous_manifests']
    archives=json.loads((out/'amendments.json').read_text())['input_archives'] if (out/'amendments.json').exists() else {}
    for name,digest in meta['inputs'].items():
        file=out/archives[name.replace('\\','/')] if name.replace('\\','/') in archives else p.ROOT/name
        assert p.p11.sha(file)==digest,name
    for name,digest in json.loads((out/'manifest.json').read_text()).items():assert p.p11.sha(out/name)==digest,name
    baseline_done=json.loads((out/'baseline_complete.json').read_text())
    perturb_start=json.loads((out/'perturbations_start.json').read_text())
    assert baseline_done['timestamp_utc']<=perturb_start['timestamp_utc']
    audit=pd.read_csv(out/'baseline_audit.csv');assert len(audit)==600 and audit.actions_checked.sum()==9600
    decisions=pd.read_csv(p.p13.OUT/'decisions.csv')
    data={s:p.p10.read_inputs('train',s) for s in ['FD001','FD003']}
    counters=dict(baseline_actions=0,global_actions=0,local_actions=0,noise_fits=0,global_path_values=0)
    for split in json.loads((p.p10.OUT/'splits.json').read_text()):
        s,rep,fold=split['subset'],split['repeat'],split['fold'];tag=f'{s}_r{rep}_f{fold}'
        bundle=joblib.load(p.p10.OUT/f'models_{tag}.joblib')
        n=joblib.load(out/f'noise_{tag}.joblib')
        assert n['fit_units']==sorted(split['fit'])
        assert not set(n['fit_units'])&set(split['uncertainty']+split['evaluation']+split['converter'])
        residual=[];centres=[]
        for u in split['fit']:
            raw=data[s].loc[data[s].unit.eq(u),p.core.SENSORS].to_numpy()
            delta=raw[5:20]-raw[4:19]
            centres.append(delta.mean(axis=0));residual.append(delta-delta.mean(axis=0))
        covariance=np.cov(np.vstack(residual),rowvar=False)
        np.testing.assert_allclose(n['cov'],covariance,atol=1e-12)
        np.testing.assert_allclose(n['centre'],np.mean(centres,axis=0),atol=1e-12)
        np.testing.assert_array_equal(n['active'],np.flatnonzero(covariance.diagonal()>1e-12))
        z=np.vstack(residual)[:,n['active']]/n['nu']
        np.testing.assert_allclose(n['md_limit'],np.quantile(np.sum((z@n['precision'])*z,axis=1),.99),rtol=1e-9)
        np.testing.assert_allclose(n['channel_limits'],np.quantile(abs(z),.99,axis=0))
        assert n['eigenvalues'][:n['retained']].sum()/n['eigenvalues'].sum()>=.9
        if n['retained']>1:assert n['eigenvalues'][:n['retained']-1].sum()/n['eigenvalues'].sum()<.9
        counters['noise_fits']+=1
        v=pd.read_csv(out/f'variants_{tag}.csv').fillna('')
        shifts=np.load(out/f'shifts_{tag}.npz')['shifts']
        for r in v.itertuples():
            expected=np.zeros(21)
            if r.kind=='channel':expected[p.core.SENSORS.index(r.sensor)]=n['nu'][list(n['active']).index(p.core.SENSORS.index(r.sensor))]*r.epsilon*r.sign
            elif r.kind=='joint':
                k=int(r.direction[2:])-1
                expected[n['active']]=r.epsilon*r.sign*n['nu']*np.sqrt(n['eigenvalues'][k])*n['eigenvectors'][:,k]
            np.testing.assert_allclose(shifts[r.variant],expected,atol=1e-12)
        base=np.load(out/f'baseline_{tag}.npz');paths=np.load(out/f'global_paths_{tag}.npz')
        global_rows=pd.read_csv(out/f'global_actions_{tag}.csv.gz')
        local_rows=pd.read_csv(out/f'local_actions_{tag}.csv.gz')
        sensitivity=pd.read_csv(out/f'sensitivity_{tag}.csv.gz')
        local_sensitivity=pd.read_csv(out/f'local_sensitivity_{tag}.csv.gz')
        support=pd.read_csv(out/f'support_{tag}.csv.gz')
        for unit in split['evaluation']:
            raw=data[s].loc[data[s].unit.eq(unit),p.core.SENSORS].to_numpy()[:-1]
            b=base['unit']==unit;where=paths['unit']==unit
            group=decisions.loc[decisions.subset.eq(s)&decisions.repeat.eq(rep)&decisions.fold.eq(fold)&decisions.unit.eq(unit)]
            C,H,slopes=reconstruction(raw,bundle['health'],shifts)
            np.testing.assert_allclose(base['C'][b],C,atol=1e-9,rtol=0)
            np.testing.assert_allclose(base['radial'][b].sum(axis=1),1-base['H'][b],atol=1e-9)
            total=C.sum(axis=1);factor=np.divide(np.clip(total,0,1),total,out=np.zeros_like(total),where=total>0)
            np.testing.assert_allclose(base['radial'][b],C*factor[:,None],atol=1e-9)
            np.testing.assert_allclose(paths['H'][:,where],H,atol=1e-9,rtol=0)
            np.testing.assert_allclose(paths['slope'][:,where],slopes,atol=1e-9,rtol=0,equal_nan=True)
            I,R=predict(bundle,H,slopes)
            for name,array in [('ISO',I),('RF',R)]:np.testing.assert_allclose(paths[name][:,where],array,atol=1e-9,rtol=0,equal_nan=True)
            cycles=np.arange(20,len(raw)+1)
            check_actions(global_rows.loc[global_rows.unit.eq(unit)],group,cycles,H,I,R)
            expected=expected_actions(group,cycles,H[:1],I[:1],R[:1])
            for r in group.itertuples():np.testing.assert_allclose(expected[r.policy_id][0],r.decision,equal_nan=True)
            counters['baseline_actions']+=len(group)
            counters['global_actions']+=len(group)*len(v)
            counters['global_path_values']+=H.size
            # Direct evaluation of increment-space support from the raw measurement perturbation.
            t=np.arange(1,len(raw)+1);ramp=np.clip((t-20)/20,0,1)
            delta=raw[1:,n['active']]-raw[:-1,n['active']]
            Z=(delta[None]+np.diff(ramp)[None,:,None]*shifts[:,None,n['active']]-n['centre'][n['active']])/n['nu']
            distance=np.sum((Z@n['precision'])*Z,axis=-1)
            outside=(distance>n['md_limit'])|np.any(abs(Z)>n['channel_limits'],axis=-1)
            np.testing.assert_array_equal(paths['outside'][:,where],outside[:,18:])
            check_prefix_support(global_rows.loc[global_rows.unit.eq(unit)],group,outside,len(raw))
            sup=support.loc[support.unit.eq(unit)].sort_values('variant')
            np.testing.assert_array_equal(sup.outside_count,outside[:,4:].sum(axis=1))
            common=base['common'][b]
            for method,array in [('ISO',I),('RF_SLOPE',R)]:
                rows=sensitivity.loc[sensitivity.unit.eq(unit)&sensitivity.method.eq(method)].sort_values('variant')
                delta=array-array[0]
                np.testing.assert_allclose(rows.mean_abs_delta_rul,np.mean(abs(delta[:,common]),axis=1),atol=1e-9)
                np.testing.assert_allclose(rows.mean_abs_delta_hi,np.mean(abs(H[:,common]-H[0,common]),axis=1),atol=1e-9)
                np.testing.assert_array_equal(rows.support_count,((~outside[:,18:])&(~outside[0,18:])&common).sum(axis=1))
            for cutoff,lr in local_rows.loc[local_rows.unit.eq(unit)].groupby('cutoff'):
                cutoff=int(cutoff)
                subset=group.loc[group.policy_id.isin(lr.policy_id.unique())]
                _,LH,LS=reconstruction(raw[:cutoff],bundle['health'],shifts,cutoff)
                LI,LR=predict(bundle,LH,LS,R[0,:cutoff-19],max(19,cutoff-39))
                check_actions(lr,subset,np.arange(20,cutoff+1),LH,LI,LR)
                local_outside=support_values(raw[:cutoff],shifts,n,cutoff)
                check_prefix_support(lr,subset,local_outside,cutoff)
                for method,forecast in [('ISO',LI),('RF_SLOPE',LR)]:
                    ls=local_sensitivity.loc[local_sensitivity.unit.eq(unit)&local_sensitivity.cutoff.eq(cutoff)&local_sensitivity.method.eq(method)].sort_values('variant')
                    np.testing.assert_allclose(ls.hi,LH[:,-1],atol=1e-9)
                    np.testing.assert_allclose(ls.slope,LS[:,-1],atol=1e-9)
                    np.testing.assert_allclose(ls.prediction,forecast[:,-1],atol=1e-9)
                    np.testing.assert_allclose(ls.delta_prediction,forecast[:,-1]-forecast[0,-1],atol=1e-9)
                    np.testing.assert_array_equal(ls.inside_pair,(~local_outside[:,-1])&(~local_outside[0,-1]))
                counters['local_actions']+=len(lr)
        print(tag,'independently verified',flush=True)
    result=dict(status='passed',**counters,previous_artifacts_intact=p.integrity()==meta['previous_manifests'],
                verifier_sha256=p.p11.sha(p.ROOT/'experiments/verify_pilot_explainability_13b.py'))
    (out/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    p.refresh_manifest();print(json.dumps(result))


if __name__=='__main__':
    with threadpool_limits(limits=1):main()
