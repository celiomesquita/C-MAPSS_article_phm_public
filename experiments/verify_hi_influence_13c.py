"""Independent checks of saved P13.3 identities, denominators and F-only fits."""
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd
import pilot_f_uncertainty_10 as p10


def main():
    out=p10.ROOT/'experiments/artifacts/pilot_hi_influence_13c'
    for name,digest in json.loads((out/'inputs.json').read_text()).items():
        assert hashlib.sha256((p10.ROOT/name).read_bytes()).hexdigest()==digest
    for name,digest in json.loads((out/'manifest.json').read_text()).items():
        assert hashlib.sha256((out/name).read_bytes()).hexdigest()==digest
    effects=pd.read_csv(out/'effects.csv');fits=pd.read_csv(out/'refits.csv')
    baseline=pd.read_csv(out/'baseline_markers.csv');weights=pd.read_csv(out/'weights.csv')
    assert len(baseline)==600 and len(fits)==300 and len(effects)==3000 and len(weights)==6300
    assert baseline.groupby(['subset','repeat']).unit.nunique().eq(100).all()
    assert not effects.duplicated(['subset','repeat','removed','variant','unit']).any()
    np.testing.assert_allclose(effects.delta,effects.refit-effects.baseline,equal_nan=True)
    assert effects.missing_refit.eq(effects.refit.isna()).all()
    assert effects.missing_baseline.eq(effects.baseline.isna()).all()
    for row in fits.itertuples():
        split=p10.partitions(p10.SEEDS[row.repeat-1])[row.fold-1]
        assert sorted(json.loads(row.fit_units))==sorted(set(split['fit'])-{row.removed})
        if row.variant=='coefficients':
            assert row.mse+row.penalty<=row.baseline_mse_same_F24+row.baseline_penalty+1e-8
    for key,g in weights.groupby(['subset','repeat','removed','variant']):
        a=g.baseline.to_numpy();b=g.refit.to_numpy()
        r=fits.loc[(fits.subset==key[0])&(fits.repeat==key[1])&(fits.removed==key[2])&(fits.variant==key[3])].iloc[0]
        np.testing.assert_allclose(r.weight_relative_l2,np.linalg.norm(a-b)/np.linalg.norm(a),atol=1e-10)
    result=dict(passed=True,baseline_markers=600,refits=300,engine_responses=3000,weights=6300)
    (out/'verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__': main()
