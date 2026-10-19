"""Check freeze transfer, event-control equivalence, provenance and final hashes."""
import json
import platform
from pathlib import Path
import numpy as np
import pandas as pd
import scipy
import sklearn
import pilot_policy_selection_13a as p


def main():
    out = p.OUT
    selection = pd.read_csv(out/'selections.csv')
    decisions = pd.read_csv(out/'decisions.csv')
    freezes = json.loads((out/'selection_freezes.json').read_text())
    for f in freezes:
        s = selection.loc[selection.subset.eq(f['subset']) & selection.repeat.eq(f['repeat']) & selection.fold.eq(f['fold'])]
        pd.testing.assert_frame_equal(s.reset_index(drop=True), pd.DataFrame(f['selections'])[s.columns], check_dtype=False)
    selected = decisions.loc[decisions.phase.eq('selected')].copy()
    selected['family'] = np.where(selected.policy_id.str.contains('THRESHOLD'), 'threshold', 'wait')
    joined = selected.merge(selection, on=['subset', 'repeat', 'fold', 'family', 'delay'], suffixes=('_outer', '_freeze'), validate='many_to_one')
    assert len(joined) == 2400
    np.testing.assert_array_equal(joined.selected_value_outer, joined.selected_value_freeze)
    np.testing.assert_array_equal(joined.selection_feasible_outer, joined.selection_feasible_freeze)
    checked = 0
    # The reconstructed sensor HI must reproduce the fixed 0.5 event control.
    for (s, r, f), g in decisions.loc[decisions.method.eq('HI_MARKER')].groupby(['subset', 'repeat', 'fold']):
        h = pd.read_csv(out/f'outer_health_{s}_r{r}_f{f}.csv.gz')
        for row in g.itertuples():
            action = p.condition_action(h.loc[h.unit.eq(row.unit) & h.cycle.lt(row.endpoint)], 'threshold', .5, row.delay)
            np.testing.assert_allclose([row.decision, row.scheduled], [action['decision'], action['scheduled']], equal_nan=True)
            checked += 1
    source_files = ['pilot_policy_selection_13a.py', 'test_pilot_policy_selection_13a.py',
                    'verify_pilot_policy_selection_13a.py', 'report_pilot_policy_selection_13a.py', Path(__file__).name]
    result = dict(status='passed', frozen_selections_checked=240, transfer_rows_checked=len(joined),
                  marker_equivalence_checked=checked, python=platform.python_version(), numpy=np.__version__,
                  pandas=pd.__version__, scipy=scipy.__version__, sklearn=sklearn.__version__,
                  sources={name:p.p11.sha(p.ROOT/'experiments'/name) for name in source_files},
                  amendments=['CSV index reset in verifier only', 'Windows path normalisation for archived verifier hash lookup'],
                  original_verifier='verifier_original.py', intermediate_verifier='verifier_index_fix.py')
    (out/'final_checks.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    # Keep the execution logs alongside the immutable scientific outputs.
    for source, target in [('p13a_execution.log', 'execution.log'), ('p13a_verification_final.log', 'verification_final.log')]:
        (out/target).write_bytes((p.ROOT/'experiments'/source).read_bytes())
    p.refresh_manifest()
    count = 0
    for folder in sorted((p.ROOT/'experiments/artifacts').glob('pilot_*')):
        if not (folder/'manifest.json').exists():
            continue
        for name, digest in json.loads((folder/'manifest.json').read_text(encoding='utf-8')).items():
            assert p.p11.sha(folder/name) == digest
            count += 1
    print(json.dumps(dict(status='passed', artifact_hashes_checked=count, marker_equivalence_checked=checked)))


if __name__ == '__main__':
    main()
