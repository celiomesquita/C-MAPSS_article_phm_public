"""Frozen-pipeline algebra and information-robustness operations for P13.2."""
import numpy as np
import pandas as pd

SENSORS=[f's{i}' for i in range(1,22)]


def noise_model(inputs):
    increments=[]
    centres=[]
    for _,g in inputs.groupby('unit',sort=True):
        raw=g.sort_values('cycle')[SENSORS].to_numpy()
        delta=np.diff(raw,axis=0)[4:19]  # increments whose destination cycles are 6..20
        centres.append(delta.mean(axis=0))
        increments.append(delta-delta.mean(axis=0))
    residual=np.concatenate(increments)
    cov=np.cov(residual,rowvar=False,ddof=1)
    active=np.flatnonzero(np.diag(cov)>1e-12)
    nu=np.sqrt(np.diag(cov)[active])
    z=residual[:,active]/nu
    corr=np.cov(z,rowvar=False,ddof=1)
    values,vectors=np.linalg.eigh(corr)
    order=np.argsort(-values,kind='stable');values=values[order];vectors=vectors[:,order]
    for j in range(vectors.shape[1]):
        if vectors[np.argmax(abs(vectors[:,j])),j]<0: vectors[:,j]*=-1
    positive=values>1e-12
    basis=vectors[:,positive];eigen=values[positive]
    precision=(basis/eigen)@basis.T
    md=np.einsum('ij,jk,ik->i',z,precision,z)
    retained=int(np.searchsorted(np.cumsum(values)/values.sum(),.9)+1)
    return dict(active=active,nu=nu,cov=cov,centre=np.mean(centres,axis=0),
                eigenvalues=values,eigenvectors=vectors,retained=retained,precision=precision,
                md_limit=float(np.quantile(md,.99)),channel_limits=np.quantile(abs(z),.99,axis=0),
                fit_units=sorted(inputs.unit.unique().tolist()))


def variants(noise):
    rows=[dict(variant=0,kind='baseline',direction='baseline',sensor='',epsilon=0.,sign=0)]
    shifts=[np.zeros(21)]
    directions=[]
    for k,channel in enumerate(noise['active']):
        v=np.zeros(21);v[channel]=noise['nu'][k]
        directions.append(('channel',SENSORS[channel],SENSORS[channel],v))
    for k in range(noise['retained']):
        v=np.zeros(21)
        v[noise['active']]=noise['nu']*np.sqrt(max(0,noise['eigenvalues'][k]))*noise['eigenvectors'][:,k]
        directions.append(('joint',f'pc{k+1}','',v))
    for kind,label,sensor,vector in directions:
        for epsilon in [.5,1.]:
            for sign in [-1,1]:
                rows.append(dict(variant=len(rows),kind=kind,direction=label,sensor=sensor,epsilon=epsilon,sign=sign))
                shifts.append(sign*epsilon*vector)
    return pd.DataFrame(rows),np.asarray(shifts)


def ramp(cycles,cutoff=None):
    cycles=np.asarray(cycles)
    if cutoff is None: return np.clip((cycles-20)/20,0,1)
    # Twenty observations end at cutoff; causal support never alters baseline <=20.
    return np.where(cycles>20,np.clip((cycles-(cutoff-19))/19,0,1),0.)


def rolling_ramp(cycles,cutoff=None):
    g=ramp(cycles,cutoff)
    return pd.Series(g).rolling(15,min_periods=15).mean().to_numpy()


def base_contributions(raw,health):
    means=pd.DataFrame(raw).rolling(15,min_periods=15).mean().to_numpy()
    channels=np.array([SENSORS.index(s) for s in health['stats']['channels']])
    weights=health['beta']*health['stats']['direction']/health['stats']['scale']
    c=np.zeros_like(raw,dtype=float)
    c[:,channels]=(means[:,channels]-means[19,channels])*weights
    return c,channels,weights


def bounded_contributions(c):
    total=np.sum(c,axis=-1)
    loss=np.clip(total,0,1)
    factor=np.divide(loss,total,out=np.zeros_like(total),where=total>0)
    return 1-loss,c*factor[...,None],total


def health_paths(c,channels,weights,shifts,cycles,cutoff=None):
    effect=shifts[:,channels]@weights
    total=c.sum(axis=1)
    H=1-np.clip(total[None,:]+effect[:,None]*rolling_ramp(cycles,cutoff)[None,:],0,1)
    # Only cycles >=20 enter the HI trajectory; the cycle20 reference is preserved.
    H=H[:,19:]
    u=np.arange(20)-9.5
    slopes=np.full_like(H,np.nan)
    slopes[:,19:]=np.lib.stride_tricks.sliding_window_view(H,20,axis=1)@u/(u@u)
    return H,slopes


def forecasts(bundle,H,slopes,rf_prefix=None,changed_cycle=39):
    iso=bundle['predictors']['ISO']['model']
    ISO=np.interp(H,iso.X_thresholds_,iso.y_thresholds_)
    RF=np.full_like(H,np.nan) if rf_prefix is None else np.broadcast_to(rf_prefix,H.shape).copy()
    start=max(19,changed_cycle-20)
    x=np.stack([H[:,start:],slopes[:,start:]],axis=-1).reshape(-1,2).astype(np.float32)
    model=bundle['predictors']['RF_SLOPE']['model']
    result=np.zeros(len(x))
    for tree in model.estimators_: result+=tree.predict(x,check_input=False)
    RF[:,start:]=(result/len(model.estimators_)).reshape(H.shape[0],H.shape[1]-start)
    ISO[:,:19]=np.nan
    return ISO,RF


def actions(rows,cycles,H,ISO,RF):
    output=[]
    V=H.shape[0]
    eligible=cycles>=39
    marker=H<=.5
    first=np.where(marker.any(axis=1),np.argmax(marker,axis=1)+int(cycles[0]),np.nan)
    first=np.maximum(39,first)
    for r in rows.itertuples():
        if r.method=='AGE':
            decision=np.full(V,r.control_age-r.delay)
        elif r.method in ['HI_MARKER','HI_WAIT_SELECTED']:
            decision=first+(r.selected_value if r.method=='HI_WAIT_SELECTED' else 0)
        elif r.method=='HI_THRESHOLD_SELECTED':
            hit=H<=r.selected_value
            decision=np.where(hit.any(axis=1),np.argmax(hit,axis=1)+int(cycles[0]),np.nan)
            decision=np.maximum(39,decision)
        else:
            forecast=ISO if r.method=='ISO' else RF
            leads=np.maximum(0,forecast-r.q_late)
            hit=eligible[None,:] & (cycles[None,:]>=first[:,None]) & (leads<=r.reserve+r.delay+1e-9)
            decision=np.where(hit.any(axis=1),np.argmax(hit,axis=1)+int(cycles[0]),np.nan)
        decision=np.where((decision>=1)&(decision<=cycles[-1]),decision,np.nan)
        removal=decision+r.delay
        end=r.endpoint
        output.append(dict(policy_id=r.policy_id,decision=decision,scheduled=removal,
                           first_available=first,late=np.isfinite(decision)&(removal>end),
                           exact=np.isfinite(decision)&(removal==end),missing=~np.isfinite(decision),
                           reached=~np.isfinite(decision)|(removal>=end)))
    return output


def support(raw,cycles,shifts,noise,cutoff=None):
    active=noise['active']
    increments=np.diff(raw[:,active],axis=0)
    dg=np.diff(ramp(cycles,cutoff))
    z=(increments[None,:,:]+shifts[:,None,active]*dg[None,:,None]-noise['centre'][active])/noise['nu']
    md=np.einsum('vti,ij,vtj->vt',z,noise['precision'],z,optimize=True)
    outside=(md>noise['md_limit']) | np.any(abs(z)>noise['channel_limits'],axis=2)
    return outside
