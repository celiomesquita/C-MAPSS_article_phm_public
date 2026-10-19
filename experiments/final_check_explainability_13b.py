"""Final trigger/fidelity checks, source lineage, local links and artifact sealing."""
import json
from pathlib import Path
import re
from urllib.parse import unquote
import joblib
import numpy as np
import pandas as pd
import pilot_explainability_13b as p


def main():
    out=p.OUT
    for name in ['verification.json','summary_verification.json']:
        assert json.loads((out/name).read_text())['status']=='passed'
    trigger=pd.read_csv(out/'trigger_explanation.csv')
    decisions=pd.read_csv(p.p13.OUT/'decisions.csv')
    assert len(trigger)==9600
    checked=0;linear_points=0;maximum_linear_error=0.
    for split in json.loads((p.p10.OUT/'splits.json').read_text()):
        s,rep,fold=split['subset'],split['repeat'],split['fold'];tag=f'{s}_r{rep}_f{fold}'
        b=np.load(out/f'baseline_{tag}.npz');g=np.load(out/f'global_paths_{tag}.npz')
        shifts=np.load(out/f'shifts_{tag}.npz')['shifts'];model=joblib.load(p.p10.OUT/f'models_{tag}.joblib')['health']
        ch=[p.core.SENSORS.index(x) for x in model['stats']['channels']]
        coefficient=model['beta']*model['stats']['direction']/model['stats']['scale']
        effect=shifts[:,ch]@coefficient
        for unit in split['evaluation']:
            m=b['unit']==unit;times=b['cycle'][m];H=b['H'][m]
            hits=times[H<=.5];gate=max(39,float(hits.min())) if len(hits) else np.nan
            rows=trigger.loc[trigger.subset.eq(s)&trigger.repeat.eq(rep)&trigger.fold.eq(fold)&trigger.unit.eq(unit)]
            src=decisions.loc[decisions.subset.eq(s)&decisions.repeat.eq(rep)&decisions.fold.eq(fold)&decisions.unit.eq(unit)].set_index('policy_id')
            for r in rows.itertuples():
                original=src.loc[r.policy_id]
                assert r.cutoff==(int(original.decision) if original.has_decision else int(times[-1]))
                j=int(np.flatnonzero(times==r.cutoff)[0])
                np.testing.assert_allclose([r.hi,r.slope,r.gate],[H[j],b['slope'][m][j],gate],equal_nan=True,atol=1e-9)
                prediction=b['ISO'][m][j] if r.method=='ISO' else b['RF'][m][j] if r.method=='RF_SLOPE' else np.nan
                np.testing.assert_allclose(r.prediction,prediction,equal_nan=True,atol=1e-9)
                lower=max(0.,prediction-original.q_late) if np.isfinite(prediction) else np.nan
                np.testing.assert_allclose(r.lower,lower,equal_nan=True,atol=1e-9)
                assert r.lower_zero==bool(np.isfinite(lower) and lower==0)
                assert r.central_would_trigger==bool(np.isfinite(prediction) and prediction<=original.reserve+original.delay+1e-9)
                assert r.at_gate==bool(original.has_decision and original.decision==gate)
                checked+=1
            # Exact finite-difference identity where neither endpoint is clipped.
            N=int(times[-1]);ramp=np.clip((np.arange(1,N+1)-20)/20,0,1)
            mean=pd.Series(ramp).rolling(15,min_periods=15).mean().to_numpy()[19:]
            expected=-effect[:,None]*mean[None,:]
            perturbed=g['H'][:,g['unit']==unit]
            inside=(H[None,:]>1e-12)&(H[None,:]<1-1e-12)&(perturbed>1e-12)&(perturbed<1-1e-12)&(abs(expected)>1e-12)
            err=abs((perturbed-H[None,:])-expected)
            if inside.any():maximum_linear_error=max(maximum_linear_error,float(err[inside].max()))
            assert not (err[inside]>1e-9).any()
            linear_points+=int(inside.sum())
    cases=pd.read_csv(out/'case_sheets.csv');responses=pd.read_csv(out/'case_responses.csv')
    assert len(cases)==len(responses)==3168
    case_keys=['subset','repeat','unit','policy_id']
    pd.testing.assert_frame_equal(cases[case_keys].sort_values(case_keys).reset_index(drop=True),responses[case_keys].sort_values(case_keys).reset_index(drop=True))
    inventory=pd.read_csv(out/'case_inventory.csv')
    assert len(inventory[['subset','unit']].drop_duplicates())==66
    assert len(cases[['subset','unit']].drop_duplicates())==66
    # Every link in the updated research documents and all generated sheets resolves.
    docs=[p.ROOT/name for name in ['docs/gestao/plano_executivo_de_melhorias.md','docs/gestao/registro_tecnico_de_auditoria.md',
          'experiments/README.md','experiments/plano_experimentos_remocao.md']]
    docs+=list(out.glob('*.md'))
    for f in docs:
        for target in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding='utf-8-sig')):
            if '://' in target or target.startswith('#'):continue
            local=unquote(target.split('#')[0])
            assert not local or (f.parent/local).exists(),(f.name,local)
    metadata=json.loads((out/'metadata.json').read_text())
    archives=json.loads((out/'amendments.json').read_text())['input_archives']
    for name,digest in metadata['inputs'].items():
        normalized=name.replace('\\','/')
        path=out/archives[normalized] if normalized in archives else p.ROOT/name
        assert p.p11.sha(path)==digest,name
    assert p.integrity()==metadata['previous_manifests']
    # Current sources are snapshotted as well as hashed; original versions remain archived.
    sources=['explainability_core_13b.py','pilot_explainability_13b.py','resume_explainability_13b.py',
             'test_explainability_13b.py','test_explainability_analysis_13b.py','verify_pilot_explainability_13b.py',
             'analyse_explainability_13b.py','verify_explainability_summaries_13b.py','report_explainability_13b.py',
             'enrich_explainability_cases_13b.py','final_check_explainability_13b.py']
    digests={}
    for name in sources:
        source=p.ROOT/'experiments'/name
        (out/('source_'+name)).write_bytes(source.read_bytes())
        digests[name]=p.p11.sha(source)
    for source,target in [('p13b_execution_resumed.log','execution_resumed.log'),('p13b_verification.log','verification.log'),
                          ('p13b_analysis.log','analysis.log'),('p13b_summary_verification.log','summary_verification.log'),
                          ('p13b_report.log','report.log'),('p13b_case_details.log','case_details.log')]:
        (out/target).write_bytes((p.ROOT/'experiments'/source).read_bytes())
    result=dict(status='passed',trigger_rows_checked=checked,linear_identity_points=linear_points,
        maximum_linear_error=maximum_linear_error,case_engines=66,case_policy_rows=3168,
        local_links_checked=True,original_inputs_and_prior_artifacts_unchanged=True,current_sources=digests,
        tests_before_initial_execution=77,tests_before_resume=78,tests_before_statistical_analysis=82)
    (out/'final_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    p.refresh_manifest()
    count=0
    for folder in (p.ROOT/'experiments/artifacts').glob('pilot_*'):
        f=folder/'manifest.json'
        if not f.exists():continue
        for name,digest in json.loads(f.read_text(encoding='utf-8')).items():
            assert p.p11.sha(folder/name)==digest,(folder.name,name)
            count+=1
    print(json.dumps(dict(status='passed',all_artifact_hashes_checked=count,trigger_rows_checked=checked,
                         case_engines=66,linear_identity_points=linear_points,maximum_linear_error=maximum_linear_error)))


if __name__=='__main__':main()
