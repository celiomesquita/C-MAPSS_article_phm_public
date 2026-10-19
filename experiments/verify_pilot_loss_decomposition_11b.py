"""Independent P11.2 reconstruction without the oracle or summary generators."""
import json
import numpy as np
import pandas as pd
import pilot_loss_decomposition_11b as p


def same(a,b):
    np.testing.assert_allclose(a,b,atol=1e-9,rtol=1e-9,equal_nan=True)


def main():
    out=p.OUT
    meta=json.loads((out/'metadata.json').read_text(encoding='utf-8'))
    assert p.integrity()==meta['previous_manifests']
    for name,digest in meta['inputs'].items():
        assert p.p11.sha(p.ROOT/name)==digest,name
    for name,digest in json.loads((out/'manifest.json').read_text()).items():
        assert p.p11.sha(out/name)==digest,name
    source=pd.read_csv(p.SOURCE/'decisions.csv')
    real=pd.read_csv(out/'replayed_decisions.csv')
    pd.testing.assert_frame_equal(real,source,check_dtype=False,atol=1e-12,rtol=1e-12)
    availability=pd.read_csv(out/'availability.csv')
    components=pd.read_csv(out/'components.csv')
    oracles=pd.read_csv(out/'oracles.csv')
    summary=pd.read_csv(out/'summary.csv')
    diagnostic=pd.read_csv(out/'diagnostics.csv')
    assert [len(x) for x in [availability,real,components,oracles,summary,diagnostic]]==[600,9600,28800,10800,576,19200]
    # Reconstruct real decisions and G/A from immutable trajectories, not from generated fields.
    rawends={s:p.p11.read_inputs('train',s).groupby('unit').cycle.max() for s in ['FD001','FD003']}
    for (subset,rep,fold),rows in source.groupby(['subset','repeat','fold'],sort=True):
        tag=f'{subset}_r{rep}_f{fold}'
        h=pd.read_csv(p.SOURCE/f'outer_health_{tag}.csv.gz')
        forecast=pd.read_csv(p.p13.SOURCE/f'predictions_{tag}_complete.csv.gz')
        for r in rows.itertuples():
            assert r.endpoint==rawends[subset].loc[r.unit]
            x=h.loc[h.unit.eq(r.unit)&h.cycle.lt(r.endpoint)]
            if r.method=='AGE':
                t=r.control_age-r.delay
                expected=t if t<r.endpoint else np.nan
            elif r.method in ['HI_MARKER','HI_WAIT_SELECTED','HI_THRESHOLD_SELECTED']:
                threshold=r.selected_value if r.method=='HI_THRESHOLD_SELECTED' else .5
                hits=x.loc[x.hi.le(threshold),'cycle']
                t=max(39,hits.min()) if len(hits) else np.nan
                t=t+r.selected_value if r.method=='HI_WAIT_SELECTED' else t
                expected=t if np.isfinite(t) and t<r.endpoint else np.nan
            else:
                f=forecast.loc[forecast.unit.eq(r.unit)&forecast.method.eq(r.method)&forecast.cycle.lt(r.endpoint)]
                f=f.loc[f.in_domain]
                f=f.loc[np.maximum(0,f.predicted_rul.to_numpy()-r.q_late)<=r.reserve+r.delay+1e-9]
                expected=f.cycle.min() if len(f) else np.nan
            same([r.decision,r.scheduled],[expected,expected+r.delay])
        av=availability.loc[availability.subset.eq(subset)&availability.repeat.eq(rep)&availability.fold.eq(fold)]
        for r in av.itertuples():
            hits=h.loc[h.unit.eq(r.unit)&h.cycle.ge(20)&h.cycle.lt(r.endpoint)&h.hi.le(.5),'cycle']
            G=hits.min() if len(hits) else np.nan
            A=max(39,G) if np.isfinite(G) and max(39,G)<r.endpoint else np.nan
            same([r.G,r.A,r.warmup,r.crossing_lead,r.available_lead],[G,A,A-G,r.endpoint-G,r.endpoint-A])
        diag=diagnostic.loc[diagnostic.subset.eq(subset)&diagnostic.repeat.eq(rep)&diagnostic.fold.eq(fold)]
        merged=diag.merge(forecast[['unit','cycle','method','hi','h_slope','predicted_rul']],
                          left_on=['unit','snapshot','forecast_method'],right_on=['unit','cycle','method'],how='left',suffixes=('','_ref'),validate='many_to_one')
        np.testing.assert_array_equal(merged.available,merged.cycle.notna())
        for c in ['hi','h_slope','predicted_rul']:
            same(merged[c],merged[c+'_ref'])
        same(merged.error,merged.predicted_rul-(merged.endpoint-merged.snapshot))
    keys=['subset','repeat','fold','unit']
    merged=components.merge(availability[keys+['G','A']],on=keys,suffixes=('','_ref'),validate='many_to_one')
    same(merged.G,merged.G_ref);same(merged.A,merged.A_ref)
    inherited=components.merge(source,on=keys+['policy_id'],suffixes=('','_source'),validate='many_to_one')
    for name in source.columns:
        if name in keys+['policy_id']:
            continue
        a,b=inherited[name],inherited[name+'_source']
        if pd.api.types.is_numeric_dtype(a): same(a,b)
        else: np.testing.assert_array_equal(a.fillna('missing'),b.fillna('missing'))
    T=components.endpoint.to_numpy()
    D=T-components.rho.to_numpy()-components.delay.to_numpy()
    same(components.deadline,D)
    assert (D>=1).all()
    same(components.feasible_access,np.isfinite(components.A)&components.A.le(D))
    matched=components.method.ne('AGE') & (components.decision.isna()|(components.A.notna()&components.decision.ge(components.A)))
    np.testing.assert_array_equal(components.information_matched,matched)
    for name in ['O','G','A','real']:
        if name=='real': tau=components.decision.to_numpy()
        elif name=='O': tau=D.astype(float)
        else:
            tau=np.maximum(D,components[name].to_numpy())
            tau=np.where(tau<T,tau,np.nan)
        r=tau+components.delay.to_numpy()
        exists=np.isfinite(tau)
        time=np.where(exists,tau,T)
        N=np.where(exists,np.minimum(r,T),T)
        expected=dict(decision=tau,scheduled=r,J=(time>D).astype(int),B=np.maximum(0,time-D),N=N,W=T-N,
                      late=(exists&(r>T)).astype(int),exact=(exists&(r==T)).astype(int),
                      missing=(~exists).astype(int),reached=(~exists|(r>=T)).astype(int))
        for metric,values in expected.items(): same(components[f'{name}_{metric}'],values)
    for metric in ['J','B','W']:
        for part,left,right in [('total','real','O'),('det','A','O'),('post','real','A'),('crossing','G','O'),('warmup','A','G')]:
            same(components[f'{metric}_{part}'],components[f'{left}_{metric}']-components[f'{right}_{metric}'])
        same(components[f'{metric}_total'],components[f'{metric}_det']+components[f'{metric}_post'])
        if metric!='W':
            assert (components.loc[matched,f'{metric}_post']>=0).all()
    assert components.loc[components.rho.eq(1),'J_det'].eq(0).all()
    assert components.loc[components.rho.eq(1),'B_det'].eq(0).all()
    for r in oracles.itertuples():
        c=components.loc[components.subset.eq(r.subset)&components.repeat.eq(r.repeat)&components.unit.eq(r.unit)&components.delay.eq(r.delay)&components.rho.eq(r.rho)].iloc[0]
        for m in ['decision','scheduled','J','B','N','W','late','exact','missing','reached']:
            same(getattr(r,m),c[f'{r.oracle}_{m}'])
    # Independent paired bootstrap and all aggregate columns.
    rng=np.random.default_rng(20261017)
    stored=np.load(out/'bootstrap_indices.npz')
    for s in ['FD001','FD003']:
        for rep in [1,2,3]:
            np.testing.assert_array_equal(stored[f'{s}_r{rep}'],rng.integers(0,100,(2000,100)))
    for r in summary.itertuples():
        g=components.loc[components.subset.eq(r.subset)&components.repeat.eq(r.repeat)&components.policy_id.eq(r.policy_id)&components.rho.eq(r.rho)].sort_values('unit')
        mask=np.ones(100,dtype=bool) if r.scope=='all' else g.A.le(g.deadline).to_numpy()
        ix=stored[f'{r.subset}_r{r.repeat}']
        n=int(mask.sum());assert r.total==n and r.excluded==100-n
        assert r.information_matched==g.loc[mask,'information_matched'].sum()
        if n==0: continue
        weights=mask[ix];den=weights.sum(axis=1)
        def means(values): return (np.asarray(values)[ix]*weights).sum(axis=1)/den
        def check_mean(name):
            a=g[name].to_numpy()
            same([getattr(r,name),getattr(r,name+'_lo'),getattr(r,name+'_hi')],
                 [a[mask].mean(),*np.quantile(means(a),[.025,.975])])
        for name in ['O','G','A','real']:
            for m in ['J','B','N','W']: check_mean(name+'_'+m)
            for m in ['late','exact','missing','reached']:
                assert getattr(r,name+'_'+m+'_count')==g.loc[mask,name+'_'+m].sum()
            same(getattr(r,name+'_cost'),n/g.loc[mask,name+'_N'].sum())
        for m in ['J','B','W']:
            for part in ['total','det','post','crossing','warmup']: check_mean(m+'_'+part)
        costs={name:1/means(g[name+'_N']) for name in ['O','A','real']}
        for part,left,right in [('total','real','O'),('det','A','O'),('post','real','A')]:
            diff=getattr(r,left+'_cost')-getattr(r,right+'_cost')
            dist=costs[left]-costs[right]
            same([getattr(r,'cost_'+part),getattr(r,'cost_'+part+'_lo'),getattr(r,'cost_'+part+'_hi')],
                 [diff,*np.quantile(dist,[.025,.975])])
            same([getattr(r,'relative_cost_'+part),getattr(r,'relative_cost_'+part+'_lo'),getattr(r,'relative_cost_'+part+'_hi')],
                 [diff/r.O_cost,*np.quantile(dist/costs['O'],[.025,.975])])
        for m in ['J','B']:
            total=means(g[m+'_total']);det=means(g[m+'_det']);positive=total>0
            assert getattr(r,m+'_share_undefined_bootstrap')==(~positive).sum()
            pt=getattr(r,m+'_det')/getattr(r,m+'_total') if getattr(r,m+'_total')>0 else np.nan
            ci=np.quantile(det[positive]/total[positive],[.025,.975]) if positive.any() else [np.nan,np.nan]
            same([getattr(r,m+'_det_share'),getattr(r,m+'_det_share_lo'),getattr(r,m+'_det_share_hi')],[pt,*ci])
    result=dict(status='passed',real_actions_checked=9600,availability_checked=600,oracle_rows_checked=10800,
                decompositions_checked=28800,summaries_and_bootstrap_checked=576,diagnostics_checked=19200,
                previous_artifacts_intact=p.integrity()==meta['previous_manifests'],
                verifier_sha256=p.p11.sha(p.ROOT/'experiments/verify_pilot_loss_decomposition_11b.py'))
    (out/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    p.refresh_manifest()
    print(json.dumps(result))


if __name__=='__main__':
    main()
