"""Resume after a pre-output bookkeeping NameError; preserve the completed baseline."""
import json
from datetime import datetime,timezone
from threadpoolctl import threadpool_limits
import pilot_explainability_13b as p


def main():
    out=p.OUT
    assert not (out/'metadata.json').exists()
    assert (out/'baseline_complete.json').exists()
    assert not list(out.glob('global_actions_*.csv.gz')), 'Unexpected prior intervention outputs'
    initial=json.loads((out/'execution_start.json').read_text(encoding='utf-8'))
    assert p.integrity()==initial['previous_manifests']
    archives={'experiments/pilot_explainability_13b.py':'runner_initial.py',
              'experiments/verify_pilot_explainability_13b.py':'verifier_initial.py',
              'experiments/test_explainability_13b.py':'tests_initial.py'}
    for name,digest in initial['inputs'].items():
        normalized=name.replace('\\','/')
        source=out/archives[normalized] if normalized in archives else p.ROOT/name
        assert p.p11.sha(source)==digest,name
    amended=dict(reason='NameError V in policy record bookkeeping; before first perturbation output',
        time_utc=datetime.now(timezone.utc).isoformat(),input_archives=archives,
        retained='All 60 baseline audits and 9600 original actions; no intervention results existed',
        source_hashes={name:p.p11.sha(p.ROOT/'experiments'/name) for name in
            ['pilot_explainability_13b.py','verify_pilot_explainability_13b.py','test_explainability_13b.py','resume_explainability_13b.py']})
    (out/'amendments.json').write_text(json.dumps(amended,indent=2),encoding='utf-8')
    splits=json.loads((p.p10.OUT/'splits.json').read_text())
    inputs={s:p.p10.read_inputs('train',s) for s in ['FD001','FD003']}
    decisions=p.pd.read_csv(p.p13.OUT/'decisions.csv')
    p.perturbation_phase(splits,inputs,decisions)
    assert p.integrity()==initial['previous_manifests']
    initial.update(finished_utc=datetime.now(timezone.utc).isoformat(),previous_artifacts_intact=True,
                   folds=60,baseline_actions=9600,implementation_amendment='amendments.json')
    (out/'metadata.json').write_text(json.dumps(initial,indent=2),encoding='utf-8')
    p.refresh_manifest()


if __name__=='__main__':
    with threadpool_limits(limits=1):main()
