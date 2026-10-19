"""Independent raw-row reconstruction, KKT and selection checks for P13.4."""
import hashlib
import json
import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits
import pilot_f_uncertainty_10 as p10

ROOT=p10.ROOT
OUT=ROOT/'experiments/artifacts/pilot_hi_stabilization_13d'
CANDIDATES=['M18','NNLS_01','NNLS_1','SIGNED_01','SIGNED_1']
SENSORS=[f's{i}' for i in range(1,22)]


def check_scores(frame,h,target,row):
    hits=frame.loc[h<=.5,'cycle'].to_numpy();cross=float(hits[0]) if len(hits) else np.nan
    end=int(frame.cycle.max());decision=max(39.,cross) if np.isfinite(cross) else np.nan
    if decision>=end: decision=np.nan
    np.testing.assert_allclose([cross,decision,np.mean((h-target)**2)],
                               [row.crossing,row.decision,row.mse],atol=1e-9,equal_nan=True)
    for d in [1,2]:
        scheduled=decision+d
        assert getattr(row,f'late_d{d}')==bool(np.isfinite(scheduled) and scheduled>end)
        assert getattr(row,f'exact_d{d}')==bool(np.isfinite(scheduled) and scheduled==end)
        assert getattr(row,f'reached_d{d}')==bool(not np.isfinite(scheduled) or scheduled>=end)
        np.testing.assert_allclose(getattr(row,f'utilised_d{d}'),min(scheduled,end) if np.isfinite(scheduled) else end)


def main():
    meta=json.loads((OUT/'execution_start.json').read_text())
    for name,digest in meta['inputs'].items(): assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
    for name,digest in json.loads((OUT/'manifest.json').read_text()).items():
        assert hashlib.sha256((OUT/name).read_bytes()).hexdigest()==digest
    splits=json.loads((p10.OUT/'splits.json').read_text());inner=json.loads((OUT/'inner_splits.json').read_text())
    datasets={s:p10.read_inputs('train',s) for s in ['FD001','FD003']}
    solutions=responses=0;max_kkt=0.;metrics=[]
    for sp in splits:
        subset=sp['subset'];rep=sp['repeat'];fold=sp['fold'];tag=f'{subset}_r{rep}_f{fold}'
        ids=sorted(sp['fit']+sp['converter']);data=datasets[subset].loc[datasets[subset].unit.isin(ids)].reset_index(drop=True)
        data=p10.complete_labels(data);centred=p10.centred_sensors(data)[SENSORS]
        target=np.minimum(1,data.rul.to_numpy()/p10.CONFIG[subset]['tau'])**p10.CONFIG[subset]['gamma']
        base=pd.read_csv(OUT/f'baseline_{tag}.csv.gz');effects=pd.read_csv(OUT/f'effects_{tag}.csv.gz')
        assert len(base)==200 and len(effects)==5000
        for part in [p for p in inner if p['subset']==subset and p['repeat']==rep and p['fold']==fold]:
            assert set(part['fit']+part['validation']+part['unused'])==set(ids)
            assert not set(part['fit'])&set(part['validation'])
            saved=np.load(OUT/f'fits_{tag}_v{part["inner_fold"]}.npz')
            assert saved['removed'].tolist()==[0]+part['fit']
            for rindex,removed in enumerate(saved['removed']):
                fit=[u for u in part['fit'] if u!=removed];mask=data.unit.isin(fit)&data.cycle.ge(20)
                raw=centred.loc[mask].to_numpy();weights=p10.p05.equal_engine_weights(data.loc[mask,'unit'])
                scale=centred.loc[mask].std().to_numpy()
                initial_std=centred.loc[data.unit.isin(fit)&data.cycle.between(15,20)].std().to_numpy()
                direction=np.sign(centred.loc[data.unit.isin(fit)&data.cycle.eq(data.end)].median().to_numpy())
                for ci,candidate in enumerate(CANDIDATES):
                    signed=candidate.startswith('SIGNED');dirs=np.ones(21) if signed else direction
                    eligible=(initial_std>1e-6)&(scale>1e-6)&(dirs!=0)
                    np.testing.assert_array_equal(eligible,saved['eligible'][rindex,ci])
                    np.testing.assert_allclose(scale,saved['scale'][rindex,ci],atol=1e-9,rtol=1e-8)
                    np.testing.assert_array_equal(dirs,saved['direction'][rindex,ci])
                    factor=dirs[eligible]/scale[eligible];x=raw[:,eligible]*factor
                    beta=saved['beta'][rindex,ci,eligible];alpha=saved['alpha'][rindex,ci]
                    assert alpha==(p10.CONFIG[subset]['ridge'] if candidate=='M18' else (.1 if candidate.endswith('_01') else 1.))
                    if not signed: assert beta.min()>=-1e-10
                    grad=x.T@(weights*(x@beta-(1-target[mask])))+alpha*beta
                    active=np.ones(len(beta),bool) if signed else beta>1e-8
                    kkt=max(np.max(abs(grad[active])) if active.any() else 0.,
                            np.max(np.maximum(0,-grad[~active])) if (~active).any() else 0.)
                    assert kkt<1e-7,(tag,removed,candidate,kkt)
                    max_kkt=max(max_kkt,float(kkt));solutions+=1
                    w=np.zeros(21);w[eligible]=beta*factor
                    np.testing.assert_allclose(w,saved['effective'][rindex,ci],atol=1e-10)
                    selected=(base if not removed else effects)
                    rows=selected.loc[selected.inner_fold.eq(part['inner_fold'])&selected.candidate.eq(candidate)]
                    if removed: rows=rows.loc[rows.removed.eq(removed)]
                    assert sorted(rows.unit)==part['validation']
                    for row in rows.itertuples():
                        own=data.unit.eq(row.unit)&data.cycle.ge(20);raw_v=centred.loc[own].to_numpy()
                        h=np.clip(1-raw_v@w,0,1)
                        check_scores(data.loc[own],h,target[own],row);responses+=1
                        if removed:
                            hb=np.clip(1-raw_v@saved['effective'][0,ci],0,1)
                            np.testing.assert_allclose(np.sqrt(np.mean((h-hb)**2)),row.hi_rmse,atol=1e-10)
                            original=base.loc[base.inner_fold.eq(part['inner_fold'])&base.candidate.eq(candidate)&base.unit.eq(row.unit)].iloc[0]
                            np.testing.assert_allclose(row.delta,row.crossing-original.crossing,equal_nan=True)
                            assert row.presence_discordant==bool(np.isfinite(row.crossing)!=np.isfinite(original.crossing))
        for candidate in CANDIDATES:
            b=base.loc[base.candidate.eq(candidate)];e=effects.loc[effects.candidate.eq(candidate)];d=e.delta.abs().dropna()
            metrics.append(dict(subset=subset,repeat=rep,fold=fold,candidate=candidate,mse=b.mse.mean(),decisions=int((~b.missing).sum()),
                       reached_d1=int(b.reached_d1.sum()),reached_d2=int(b.reached_d2.sum()),
                       discordance=int(e.presence_discordant.sum()),loo_missing=int(e.missing.sum()),finite_pairs=len(d),
                       p95_abs=d.quantile(.95) if len(d) else np.nan,mean_abs=d.mean() if len(d) else np.nan,max_abs=d.max() if len(d) else np.nan))
        print(f'{tag}: independently verified',flush=True)
    check=pd.DataFrame(metrics);reported=pd.read_csv(OUT/'internal_metrics.csv');selections=pd.read_csv(OUT/'selections.csv')
    keys=['subset','repeat','fold','candidate']
    merged=check.merge(reported,on=keys,suffixes=('_check','_reported'),validate='one_to_one')
    for name in check.columns.difference(keys): np.testing.assert_allclose(merged[name+'_check'],merged[name+'_reported'],atol=1e-9,equal_nan=True)
    for key,g in check.groupby(['subset','repeat','fold']):
        b=g.loc[g.candidate.eq('M18')].iloc[0]
        feasible=(g.decisions.eq(40)&g.reached_d1.le(b.reached_d1)&g.reached_d2.le(b.reached_d2)&g.mse.le(1.05*b.mse+1e-12)&
                  g.discordance.le(b.discordance)&g.loo_missing.le(b.loo_missing)&g.finite_pairs.gt(0)&g.p95_abs.le(b.p95_abs+1e-12))
        pool=g.loc[feasible|g.candidate.eq('M18')].copy();pool['order']=pool.candidate.map(dict(zip(CANDIDATES,range(5))))
        winner=pool.sort_values(['p95_abs','mean_abs','mse','order'],na_position='last').iloc[0]
        saved=selections.loc[(selections.subset==key[0])&(selections.repeat==key[1])&(selections.fold==key[2])].iloc[0]
        assert saved.selected==winner.candidate
        final=joblib.load(OUT/f'selected_hi_{key[0]}_r{key[1]}_f{key[2]}.joblib')
        split=next(s for s in splits if (s['subset'],s['repeat'],s['fold'])==key)
        assert final['candidate']==saved.selected and final['fit_units']==split['fit']
        assert final['selection_development']==sorted(split['fit']+split['converter'])
        assert final['selection_sha256']==hashlib.sha256((OUT/'selections.csv').read_bytes()).hexdigest()
    assert solutions==31200 and responses==312000
    result=dict(passed=True,internal_solutions=solutions,reconstructed_responses=responses,choices=60,maximum_kkt=max_kkt)
    (OUT/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':
    with threadpool_limits(limits=1): main()
