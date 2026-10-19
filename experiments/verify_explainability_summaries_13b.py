"""Independent engine aggregation, ranks, paired bootstrap and case-inventory checks."""
import itertools
import json
import numpy as np
import pandas as pd
from scipy.stats import spearmanr
import pilot_explainability_13b as p

K=['subset','repeat','fold','unit']


def equal(a,b):np.testing.assert_allclose(a,b,atol=1e-9,rtol=1e-9,equal_nan=True)


def main():
    out=p.OUT
    engine=pd.read_csv(out/'action_engines.csv')
    attr=pd.read_csv(out/'attribution_engines.csv')
    original=pd.read_csv(p.p13.OUT/'decisions.csv')
    pairs=pd.read_csv(out/'action_contrast_engines.csv')
    fpairs=pd.read_csv(out/'forecast_contrast_engines.csv')
    keys=K+['policy_id','method','delay','phase','kind','epsilon']
    checked=0
    for split in json.loads((p.p10.OUT/'splits.json').read_text()):
        s,rep,fold=split['subset'],split['repeat'],split['fold'];tag=f'{s}_r{rep}_f{fold}'
        base=np.load(out/f'baseline_{tag}.npz')
        for unit in split['evaluation']:
            m=(base['unit']==unit)&base['common']
            expected=abs(base['C'][m]).mean(axis=0)
            actual=attr.loc[attr.subset.eq(s)&attr.repeat.eq(rep)&attr.fold.eq(fold)&attr.unit.eq(unit)].set_index('sensor').reindex(p.core.SENSORS)
            equal(actual.mean_abs,expected)
            equal(actual.mean_signed,base['C'][m].mean(axis=0))
        for phase in ['global','local']:
            raw=pd.read_csv(out/f'{phase}_actions_{tag}.csv.gz')
            raw=raw.loc[raw.epsilon.gt(0)].copy()
            both=raw.decision.notna()&raw.base_decision.notna()
            raw['abs_delta']=raw.delta_removal.abs()
            raw['same']=np.where(both,raw.delta_removal.eq(0),np.nan)
            raw['gt1']=np.where(both,raw.abs_delta.gt(1),np.nan)
            raw['gt2']=np.where(both,raw.abs_delta.gt(2),np.nan)
            raw['pdiff']=raw.decision.notna().astype(int)-raw.base_decision.notna().astype(int)
            raw['flip']=(raw.decision.notna()!=raw.base_decision.notna()).astype(float)
            raw['rdiff']=raw.reached.astype(int)-raw.base_reached.astype(int)
            raw['paired']=both.astype(int)
            raw['supported']=(both&raw.within_support).astype(int)
            raw['support_delta']=raw.abs_delta.where(raw.supported.eq(1))
            computed=raw.groupby(keys,sort=True).agg(variants=('variant','size'),paired_dates=('paired','sum'),
                mean_abs_delta=('abs_delta','mean'),max_abs_delta=('abs_delta','max'),same_fraction=('same','mean'),
                shift_gt1=('gt1','mean'),shift_gt2=('gt2','mean'),presence_delta=('pdiff','mean'),presence_flip=('flip','mean'),
                reached_fraction=('reached','mean'),reached_delta=('rdiff','mean'),supported_variants=('supported','sum'),
                supported_mean_abs_delta=('support_delta','mean')).reset_index()
            actual=engine.loc[engine.subset.eq(s)&engine.repeat.eq(rep)&engine.fold.eq(fold)&engine.phase.eq(phase)]
            pd.testing.assert_frame_equal(actual.sort_values(keys).reset_index(drop=True)[computed.columns],computed,check_dtype=False,atol=1e-9,rtol=1e-9)
            checked+=len(computed)
            # Rebuild every selected/reference contrast from the underlying identical variants.
            for policy,x in raw.loc[raw.method.isin(['HI_THRESHOLD_SELECTED','HI_WAIT_SELECTED'])].groupby('policy_id'):
                delay=int(x.delay.iloc[0])
                for reference in [f'HI_MARKER_D{delay}',f'ISO_LOWER98_M15_D{delay}']:
                    z=x.merge(raw.loc[raw.policy_id.eq(reference)],on=K+['phase','kind','epsilon','variant'],suffixes=('_a','_b'),validate='one_to_one')
                    for key,g in z.groupby(K+['phase','kind','epsilon']):
                        f=pairs
                        mask=np.ones(len(f),dtype=bool)
                        for name,value in zip(K+['phase','kind','epsilon'],key):mask&=f[name].eq(value).to_numpy()
                        r=f.loc[mask&f.policy_id.eq(policy)&f.reference.eq(reference)].iloc[0]
                        good=g.delta_removal_a.notna()&g.delta_removal_b.notna()
                        equal(r.value,(g.delta_removal_a.abs()-g.delta_removal_b.abs()).loc[good].mean())
                        assert r.date_pairs==good.sum()
                        equal(r.presence_difference,(g.pdiff_a-g.pdiff_b).mean())
        sens=pd.read_csv(out/f'sensitivity_{tag}.csv.gz')
        # Forecast contrast has no missing-decision conditioning.
        idx=K+['variant','phase','kind','epsilon']
        merge=sens.loc[sens.method.eq('ISO')&sens.epsilon.gt(0)].merge(sens.loc[sens.method.eq('RF_SLOPE')&sens.epsilon.gt(0)],on=idx,suffixes=('_a','_b'),validate='one_to_one')
        computed=merge.assign(value=merge.mean_abs_delta_rul_a-merge.mean_abs_delta_rul_b).groupby(K+['phase','kind','epsilon']).value.mean()
        actual=fpairs.loc[fpairs.subset.eq(s)&fpairs.repeat.eq(rep)&fpairs.fold.eq(fold)].set_index(K+['phase','kind','epsilon']).value
        equal(actual.reindex(computed.index),computed)
        print(tag,'statistical inputs verified',flush=True)
    assert checked==len(engine)
    # Ranks and stability are descriptive: undefined correlations remain undefined.
    vectors=pd.read_csv(out/'rank_vectors.csv')
    comparisons=pd.read_csv(out/'rank_comparisons.csv')
    for r in comparisons.itertuples():
        x=vectors.loc[vectors.subset.eq(r.subset)&vectors.repeat.eq(r.repeat)]
        kind_a='contribution' if r.comparison=='contribution_vs_sensitivity' else r.kind
        a=x.loc[x.fold.eq(r.fold_a)&x.kind.eq(kind_a)].set_index('sensor').reindex(p.core.SENSORS).score.to_numpy()
        b=x.loc[x.fold.eq(r.fold_b)&x.kind.eq(r.kind)].set_index('sensor').reindex(p.core.SENSORS).score.to_numpy()
        good=np.isfinite(a)&np.isfinite(b)
        identifiable=good.sum()>1 and np.ptp(a[good])>0 and np.ptp(b[good])>0
        expected=spearmanr(a[good],b[good]).statistic if identifiable else np.nan
        equal(r.spearman,expected);assert r.identified==identifiable and r.channels==good.sum()
        topa=sorted(np.flatnonzero(good),key=lambda j:(-a[j],j))[:5]
        topb=sorted(np.flatnonzero(good),key=lambda j:(-b[j],j))[:5]
        assert r.shared_top5==len(set(topa)&set(topb))
    # Reconstruct same-engine date comparisons across reused repetitions.
    dates=pd.read_csv(out/'repeat_dates.csv')
    assert len(dates)==9600
    lookup=original.set_index(['subset','repeat','unit','policy_id'])
    for r in dates.itertuples():
        a=lookup.loc[(r.subset,r.repeat_a,r.unit,r.policy_id)]
        b=lookup.loc[(r.subset,r.repeat_b,r.unit,r.policy_id)]
        equal(r.delta_abs,abs(a.scheduled-b.scheduled))
        assert r.presence_discordant==(a.has_decision!=b.has_decision)
    # Same bootstrap indices across all contrasts in each domain/repeat.
    rng=np.random.default_rng(20261017);stored=np.load(out/'bootstrap_indices.npz')
    for s in ['FD001','FD003']:
        for rep in [1,2,3]:np.testing.assert_array_equal(stored[f'{s}_r{rep}'],rng.integers(0,100,(2000,100)))
    ci_count=0
    for source,file in [(pairs,'action_contrasts.csv'),(fpairs,'forecast_contrasts.csv')]:
        table=pd.read_csv(out/file)
        for r in table.itertuples():
            g=source.loc[source.subset.eq(r.subset)&source.repeat.eq(r.repeat)&source.phase.eq(r.phase)&source.kind.eq(r.kind)&source.epsilon.eq(r.epsilon)&source.policy_id.eq(r.policy_id)&source.reference.eq(r.reference)].set_index('unit').reindex(range(1,101))
            ix=stored[f'{r.subset}_r{r.repeat}']
            for metric in ['value','presence_difference']:
                v=g[metric].to_numpy();valid=np.isfinite(v);den=valid[ix].sum(axis=1)
                sums=np.nan_to_num(v,nan=0)[ix].sum(axis=1)
                boot=np.divide(sums,den,out=np.full(len(ix),np.nan),where=den>0)
                quantiles=np.nanquantile(boot,[.025,.975]) if np.isfinite(boot).any() else [np.nan,np.nan]
                equal([getattr(r,metric),getattr(r,metric+'_lo'),getattr(r,metric+'_hi')],
                      [v[valid].mean() if valid.any() else np.nan,*quantiles])
                assert getattr(r,metric+'_engines')==valid.sum()
                assert getattr(r,metric+'_empty_bootstrap')==(den==0).sum()
            ci_count+=1
    inv=pd.read_csv(out/'case_inventory.csv')
    listed=set(map(tuple,inv[['subset','repeat','unit']].to_numpy()))
    adverse=original.loc[original.reached_endpoint|original.selection_feasible.eq(False)]
    assert set(map(tuple,adverse[['subset','repeat','unit']].to_numpy()))<=listed
    result=dict(status='passed',engine_action_summaries=checked,rank_comparisons=len(comparisons),
                repeat_date_pairs=len(dates),bootstrap_contrasts=ci_count,all_adverse_cases_included=True,
                source_sha256=p.p11.sha(p.ROOT/'experiments/verify_explainability_summaries_13b.py'))
    (out/'summary_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))  # Final sealing follows completion of both independent audits.


if __name__=='__main__':main()
