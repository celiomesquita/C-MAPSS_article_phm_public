"""Engine-weighted sufficient statistics and predeclared P13.4 comparisons."""
import numpy as np
import pandas as pd
from scipy.optimize import nnls
import pilot_f_uncertainty_10 as p10

CANDIDATES=['M18','NNLS_01','NNLS_1','SIGNED_01','SIGNED_1']
SENSORS=[f's{i}' for i in range(1,22)]


def engine_bank(data,subset):
    bank={}
    for unit,g in data.groupby('unit',sort=True):
        g=g.sort_values('cycle').reset_index(drop=True)
        centred=p10.centred_sensors(g)[SENSORS].to_numpy()
        x=centred[g.cycle.ge(20)]
        initial=centred[g.cycle.between(15,20)]
        cycles=g.loc[g.cycle.ge(20),'cycle'].to_numpy()
        target=np.minimum(1,(int(g.cycle.max())-cycles)/p10.CONFIG[subset]['tau'])**p10.CONFIG[subset]['gamma']
        y=1-target
        bank[int(unit)]=dict(x=x,initial=initial,cycles=cycles,end=int(g.cycle.max()),target=target,
                             gram=x.T@x/len(x),rhs=x.T@y/len(x),terminal=x[-1],
                             n=len(x),sums=x.sum(axis=0),squares=np.square(x).sum(axis=0),
                             ni=len(initial),si=initial.sum(axis=0),qi=np.square(initial).sum(axis=0))
    return bank


def moments(bank,ids):
    records=[bank[int(i)] for i in ids]
    n=sum(r['n'] for r in records);ni=sum(r['ni'] for r in records)
    sums=sum(r['sums'] for r in records);si=sum(r['si'] for r in records)
    scale=np.sqrt(np.maximum(0,(sum(r['squares'] for r in records)-sums*sums/n)/(n-1)))
    initial=np.sqrt(np.maximum(0,(sum(r['qi'] for r in records)-si*si/ni)/(ni-1)))
    direction=np.sign(np.median(np.stack([r['terminal'] for r in records]),axis=0))
    return dict(gram=np.mean([r['gram'] for r in records],axis=0),
                rhs=np.mean([r['rhs'] for r in records],axis=0),scale=scale,
                eligible=(initial>1e-6)&(scale>1e-6),direction=direction)


def solve(m,subset,candidate):
    signed=candidate.startswith('SIGNED')
    alpha=p10.CONFIG[subset]['ridge'] if candidate=='M18' else (.1 if candidate.endswith('_01') else 1.)
    direction=np.ones(21) if signed else m['direction']
    eligible=m['eligible']&(direction!=0)
    factors=np.zeros(21);factors[eligible]=direction[eligible]/m['scale'][eligible]
    gram=m['gram'][np.ix_(eligible,eligible)]*np.outer(factors[eligible],factors[eligible])
    rhs=m['rhs'][eligible]*factors[eligible]
    system=gram+alpha*np.eye(len(rhs))
    if signed:
        beta=np.linalg.solve(system,rhs)
    else:
        design=np.linalg.cholesky(system).T
        response=np.linalg.solve(design.T,rhs)
        beta=nnls(design,response)[0]
    gradient=system@beta-rhs
    active=np.ones(len(beta),dtype=bool) if signed else beta>1e-8
    kkt=max(np.max(abs(gradient[active])) if active.any() else 0.,
            np.max(np.maximum(0,-gradient[~active])) if (~active).any() else 0.)
    assert kkt<1e-8
    full_beta=np.zeros(21);full_beta[eligible]=beta
    return dict(effective=full_beta*factors,beta=full_beta,factors=factors,scale=m['scale'],
                eligible=eligible,direction=direction,alpha=alpha,kkt=float(kkt))


def evaluate(bank,unit,weights):
    r=bank[int(unit)];h=np.clip(1-r['x']@weights,0,1)
    hits=r['cycles'][h<=.5]
    crossing=float(hits[0]) if len(hits) else np.nan
    decision=max(39.,crossing) if np.isfinite(crossing) else np.nan
    if decision>=r['end']: decision=np.nan
    result=dict(unit=int(unit),endpoint=r['end'],crossing=crossing,decision=decision,
                mse=float(np.mean((h-r['target'])**2)),missing=bool(not np.isfinite(decision)))
    for delay in [1,2]:
        scheduled=decision+delay
        result[f'late_d{delay}']=bool(np.isfinite(scheduled) and scheduled>r['end'])
        result[f'exact_d{delay}']=bool(np.isfinite(scheduled) and scheduled==r['end'])
        result[f'reached_d{delay}']=bool(not np.isfinite(scheduled) or scheduled>=r['end'])
        result[f'utilised_d{delay}']=min(scheduled,r['end']) if np.isfinite(scheduled) else r['end']
    return result,h


def summarize(baseline,effects):
    rows=[]
    for candidate in CANDIDATES:
        b=baseline.loc[baseline.candidate.eq(candidate)];e=effects.loc[effects.candidate.eq(candidate)]
        delta=e.delta.abs().dropna()
        rows.append(dict(candidate=candidate,engines=len(b),mse=float(b.mse.mean()),decisions=int((~b.missing).sum()),
                         reached_d1=int(b.reached_d1.sum()),reached_d2=int(b.reached_d2.sum()),
                         late_d1=int(b.late_d1.sum()),late_d2=int(b.late_d2.sum()),
                         mean_life_d1=float(b.utilised_d1.mean()),mean_life_d2=float(b.utilised_d2.mean()),
                         discordance=int(e.presence_discordant.sum()),loo_missing=int(e.missing.sum()),
                         finite_pairs=len(delta),p95_abs=float(delta.quantile(.95)) if len(delta) else np.nan,
                         mean_abs=float(delta.mean()) if len(delta) else np.nan,
                         max_abs=float(delta.max()) if len(delta) else np.nan,
                         mean_hi_rmse=float(e.hi_rmse.mean())))
    return pd.DataFrame(rows)


def choose(metrics):
    metrics=metrics.copy();base=metrics.loc[metrics.candidate.eq('M18')].iloc[0]
    metrics['eligible']=(metrics.decisions.eq(40)&metrics.reached_d1.le(base.reached_d1)&
        metrics.reached_d2.le(base.reached_d2)&metrics.mse.le(1.05*base.mse+1e-12)&
        metrics.discordance.le(base.discordance)&metrics.loo_missing.le(base.loo_missing)&
        metrics.finite_pairs.gt(0)&metrics.p95_abs.le(base.p95_abs+1e-12))
    pool=metrics.loc[metrics.eligible|metrics.candidate.eq('M18')].copy()
    pool['order']=pool.candidate.map({c:i for i,c in enumerate(CANDIDATES)})
    choice=pool.sort_values(['p95_abs','mean_abs','mse','order'],na_position='last').iloc[0]
    return metrics,dict(selected=choice.candidate,selection_eligible=bool(choice.eligible),
                        baseline_complete=bool(base.decisions==40),baseline_reached_d1=int(base.reached_d1),
                        baseline_reached_d2=int(base.reached_d2),selected_p95=float(choice.p95_abs),
                        baseline_p95=float(base.p95_abs),selected_mse=float(choice.mse),baseline_mse=float(base.mse))
