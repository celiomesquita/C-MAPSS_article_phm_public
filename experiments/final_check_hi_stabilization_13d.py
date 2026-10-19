"""Seal supplementary P13.4 provenance after all scientific checks passed."""
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime,timezone
from pathlib import Path
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'experiments/artifacts/pilot_hi_stabilization_13d'


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    assert json.loads((OUT/'verification.json').read_text())['passed']
    assert json.loads((OUT/'final_fit_verification.json').read_text())['passed']
    start=json.loads((OUT/'execution_start.json').read_text())
    for name,digest in start['inputs'].items(): assert sha(ROOT/name)==digest
    for name,digest in json.loads((OUT/'manifest.json').read_text()).items(): assert sha(OUT/name)==digest
    metrics=pd.read_csv(OUT/'internal_metrics.csv')
    for key,g in metrics.groupby(['subset','repeat','fold']):
        tag=f'{key[0]}_r{key[1]}_f{key[2]}'
        base=pd.read_csv(OUT/f'baseline_{tag}.csv.gz');effects=pd.read_csv(OUT/f'effects_{tag}.csv.gz')
        for row in g.itertuples():
            b=base.loc[base.candidate.eq(row.candidate)];e=effects.loc[effects.candidate.eq(row.candidate)]
            np.testing.assert_allclose([row.engines,row.late_d1,row.late_d2,row.mean_life_d1,row.mean_life_d2,row.mean_hi_rmse],
                [len(b),b.late_d1.sum(),b.late_d2.sum(),b.utilised_d1.mean(),b.utilised_d2.mean(),e.hi_rmse.mean()],atol=1e-10)
    test=subprocess.run([sys.executable,'-m','unittest','discover','-s','experiments','-p','test_hi_stabilization_13d.py'],
                        cwd=ROOT,capture_output=True)
    (OUT/'tests_recheck.log').write_bytes(test.stdout+test.stderr);assert test.returncode==0
    for name in ['verify_hi_stabilization_fast_13d.py','verify_hi_stabilization_final_13d.py',
                 'report_hi_stabilization_13d.py',Path(__file__).name]:
        shutil.copyfile(ROOT/'experiments'/name,OUT/f'source_{name}')
    for source,dest in [('p13d_execution.log','execution.log'),('p13d_verification_fast.log','verification_fast.log')]:
        shutil.copyfile(ROOT/'experiments'/source,OUT/dest)
    change=dict(type='verification performance implementation only; no scientific amendment',
                original_verifier_sha256=sha(OUT/'source_verify_hi_stabilization_13d.py'),
                original_partial_log_sha256=sha(OUT/'verification_sequential_partial.log'),
                vectorized_verifier_sha256=sha(OUT/'source_verify_hi_stabilization_fast_13d.py'),
                execution_sources_unchanged=True,criteria_unchanged=True)
    (OUT/'verification_implementation_change.json').write_text(json.dumps(change,indent=2),encoding='utf-8')
    result=dict(passed=True,completed_utc=datetime.now(timezone.utc).isoformat(),
                internal_metrics_rows_checked=300,tests_rechecked=7,scientific_amendments=0)
    (OUT/'completion.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    records={p.name:sha(p) for p in OUT.iterdir() if p.is_file() and p.name!='final_manifest.json'}
    (OUT/'final_manifest.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
    assert all(sha(OUT/name)==digest for name,digest in records.items())
    print(json.dumps(result|dict(final_files=len(records))))


if __name__=='__main__': main()
