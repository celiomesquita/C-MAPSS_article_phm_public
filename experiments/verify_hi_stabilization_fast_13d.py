"""Vectorised raw-row verification; same scope as the sequential verifier."""
import hashlib
import json
import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits
import pilot_f_uncertainty_10 as p10

ROOT=p10.ROOT;OUT=ROOT/'experiments/artifacts/pilot_hi_stabilization_13d'
CANDIDATES=['M18','NNLS_01','NNLS_1','SIGNED_01','SIGNED_1']


def main():
    start=json.loads((OUT/'execution_start.json').read_text())
    for name,digest in start['inputs'].items(): assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
    for name,digest in json.loads((OUT/'manifest.json').read_text()).items():
        assert hashlib.sha256((OUT/name).read_bytes()).hexdigest()==digest
    splits=json.loads((p10.OUT/'splits.json').read_text());parts=json.loads((OUT/'inner_splits.json').read_text())
    inputs={s:p10.read_inputs('train',s) for s in ['FD001','FD003']}
    totals=0;max_kkt=0.;summary=[]
    for sp in splits:
        subset=sp['subset'];rep=sp['repeat'];fold=sp['fold'];tag=f'{subset}_r{rep}_f{fold}'
        ids=sorted(sp['fit']+sp['converter'])
        data=p10.complete_labels(inputs[subset].loc[inputs[subset].unit.isin(ids)].reset_index(drop=True))
        centred=p10.centred_sensors(data).to_numpy();valid=data.cycle.ge(20).to_numpy()
        target=np.minimum(1,data.rul.to_numpy()/p10.CONFIG[subset]['tau'])**p10.CONFIG[subset]['gamma']
        base=pd.read_csv(OUT/f'baseline_{tag}.csv.gz');effects=pd.read_csv(OUT/f'effects_{tag}.csv.gz')
        assert len(base)==200 and len(effects)==5000
        for part in [p for p in parts if (p['subset'],p['repeat'],p['fold'])==(subset,rep,fold)]:
            assert len(part['fit'])==25 and len(part['validation'])==10 and len(part['unused'])==5
            assert set(part['fit']+part['validation']+part['unused'])==set(ids)
            assert not set(part['fit'])&set(part['validation'])
            saved=np.load(OUT/f'fits_{tag}_v{part["inner_fold"]}.npz')
            removeds=[0]+part['fit'];assert saved['removed'].tolist()==removeds
            for ri,removed in enumerate(removeds):
                ids_fit=[u for u in part['fit'] if u!=removed]
                own=data.unit.isin(ids_fit).to_numpy();mask=own&valid
                raw=centred[mask];weights=p10.p05.equal_engine_weights(data.loc[mask,'unit'])
                scale=np.std(raw,axis=0,ddof=1)
                sd0=np.std(centred[own&data.cycle.between(15,20).to_numpy()],axis=0,ddof=1)
                direction=np.sign(np.median(centred[own&data.cycle.eq(data.end).to_numpy()],axis=0))
                gram=raw.T@(weights[:,None]*raw);rhs=raw.T@(weights*(1-target[mask]))
                for ci,c in enumerate(CANDIDATES):
                    signed=c.startswith('SIGNED');dirs=np.ones(21) if signed else direction
                    active_cols=(sd0>1e-6)&(scale>1e-6)&(dirs!=0)
                    np.testing.assert_array_equal(saved['eligible'][ri,ci],active_cols)
                    np.testing.assert_array_equal(saved['direction'][ri,ci],dirs)
                    np.testing.assert_allclose(saved['scale'][ri,ci],scale,atol=1e-9,rtol=1e-8)
                    factor=dirs[active_cols]/scale[active_cols];beta=saved['beta'][ri,ci,active_cols]
                    alpha=p10.CONFIG[subset]['ridge'] if c=='M18' else (.1 if c.endswith('_01') else 1.)
                    assert saved['alpha'][ri,ci]==alpha
                    if not signed: assert np.min(beta)>=-1e-10
                    grad=(gram[np.ix_(active_cols,active_cols)]*np.outer(factor,factor))@beta-rhs[active_cols]*factor+alpha*beta
                    active=np.ones(len(beta),bool) if signed else beta>1e-8
                    kkt=max(np.max(abs(grad[active])) if active.any() else 0.,np.max(np.maximum(0,-grad[~active])) if (~active).any() else 0.)
                    assert kkt<1e-7,(tag,ri,c,kkt)
                    max_kkt=max(max_kkt,float(kkt))
                    w=np.zeros(21);w[active_cols]=beta*factor
                    np.testing.assert_allclose(saved['effective'][ri,ci],w,atol=1e-10)
            # Reconstruct all 130 model responses together for each validation engine.
            weights_all=saved['effective'].reshape(-1,21)
            model_metrics=[]
            for unit in part['validation']:
                own=data.unit.eq(unit).to_numpy()&valid
                cycles=data.loc[own,'cycle'].to_numpy();end=cycles[-1]
                hi=np.clip(1-weights_all@centred[own].T,0,1).reshape(26,5,-1)
                hits=hi<=.5;has=hits.any(axis=2)
                crossing=np.where(has,cycles[np.argmax(hits,axis=2)],np.nan)
                decision=np.maximum(39,crossing);decision=np.where(decision<end,decision,np.nan)
                metrics=dict(crossing=crossing,decision=decision,mse=np.mean((hi-target[own])**2,axis=2),
                             missing=~np.isfinite(decision),baseline_crossing=np.broadcast_to(crossing[0],crossing.shape),
                             baseline_decision=np.broadcast_to(decision[0],decision.shape),delta=crossing-crossing[0],
                             presence_discordant=np.isfinite(crossing)!=np.isfinite(crossing[0]),
                             hi_rmse=np.sqrt(np.mean((hi-hi[0])**2,axis=2)))
                for d in [1,2]:
                    scheduled=decision+d
                    metrics[f'late_d{d}']=np.isfinite(scheduled)&(scheduled>end)
                    metrics[f'exact_d{d}']=np.isfinite(scheduled)&(scheduled==end)
                    metrics[f'reached_d{d}']=~np.isfinite(scheduled)|(scheduled>=end)
                    metrics[f'utilised_d{d}']=np.where(np.isfinite(scheduled),np.minimum(scheduled,end),end)
                model_metrics.append(metrics)
            merged=pd.concat([base.loc[base.inner_fold.eq(part['inner_fold'])],effects.loc[effects.inner_fold.eq(part['inner_fold'])]])
            order=pd.MultiIndex.from_product([removeds,CANDIDATES,part['validation']],names=['removed','candidate','unit'])
            ordered=merged.set_index(['removed','candidate','unit']).reindex(order)
            assert len(ordered)==1300 and not ordered.mse.isna().any()
            for name in model_metrics[0]:
                expected=np.stack([m[name] for m in model_metrics],axis=-1).reshape(-1)
                actual=ordered[name].to_numpy()
                if name in ['baseline_crossing','baseline_decision','delta','presence_discordant','hi_rmse']:
                    mask=order.get_level_values('removed')!=0;expected=expected[mask];actual=actual[mask]
                np.testing.assert_allclose(actual.astype(float),expected.astype(float),atol=1e-9,equal_nan=True,err_msg=f'{tag}: {name}')
            totals+=1300
        for c in CANDIDATES:
            b=base.loc[base.candidate.eq(c)];e=effects.loc[effects.candidate.eq(c)];d=e.delta.abs().dropna()
            summary.append(dict(subset=subset,repeat=rep,fold=fold,candidate=c,mse=b.mse.mean(),decisions=int((~b.missing).sum()),
                    reached_d1=int(b.reached_d1.sum()),reached_d2=int(b.reached_d2.sum()),discordance=int(e.presence_discordant.sum()),
                    loo_missing=int(e.missing.sum()),finite_pairs=len(d),p95_abs=d.quantile(.95) if len(d) else np.nan,
                    mean_abs=d.mean() if len(d) else np.nan,max_abs=d.max() if len(d) else np.nan))
        print(f'{tag}: vectorised independent check passed',flush=True)
    calculated=pd.DataFrame(summary);reported=pd.read_csv(OUT/'internal_metrics.csv');choices=pd.read_csv(OUT/'selections.csv')
    keys=['subset','repeat','fold','candidate'];comparison=calculated.merge(reported,on=keys,suffixes=('_check','_saved'),validate='one_to_one')
    for name in calculated.columns.difference(keys):
        np.testing.assert_allclose(comparison[name+'_check'],comparison[name+'_saved'],atol=1e-9,equal_nan=True)
    for key,g in calculated.groupby(['subset','repeat','fold']):
        b=g.loc[g.candidate.eq('M18')].iloc[0]
        feasible=(g.decisions.eq(40)&g.reached_d1.le(b.reached_d1)&g.reached_d2.le(b.reached_d2)&g.mse.le(1.05*b.mse+1e-12)&
                  g.discordance.le(b.discordance)&g.loo_missing.le(b.loo_missing)&g.finite_pairs.gt(0)&g.p95_abs.le(b.p95_abs+1e-12))
        pool=g.loc[feasible|g.candidate.eq('M18')].copy();pool['order']=pool.candidate.map(dict(zip(CANDIDATES,range(5))))
        winner=pool.sort_values(['p95_abs','mean_abs','mse','order'],na_position='last').iloc[0]
        row=choices.loc[(choices.subset==key[0])&(choices.repeat==key[1])&(choices.fold==key[2])].iloc[0]
        assert row.selected==winner.candidate
        expected_eligibility=bool(feasible.loc[winner.name]);assert row.selection_eligible==expected_eligibility
    assert totals==312000
    result=dict(passed=True,internal_solutions=31200,reconstructed_responses=totals,choices=60,maximum_kkt=max_kkt,
                verification_implementation='independent vectorised raw-row reconstruction; no scientific criterion changed')
    (OUT/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))


if __name__=='__main__':
    with threadpool_limits(limits=1): main()
