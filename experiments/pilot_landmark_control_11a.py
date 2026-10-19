"""P11.1: HI-event-only removal versus frozen P11 decisions."""

import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

import pilot_removal_11 as p11

ROOT = p11.ROOT
SOURCE = p11.SOURCE
PREVIOUS = p11.OUT
OUT = ROOT / 'experiments/artifacts/pilot_landmark_control_11a'
SEED = 20261017


def integrity():
    records = {}
    for folder in sorted((ROOT / 'experiments/artifacts').glob('pilot_*')):
        path = folder / 'manifest.json'
        if folder == OUT or not path.exists():
            continue
        for name, digest in json.loads(path.read_text(encoding='utf-8')).items():
            assert p11.sha(folder / name) == digest, (folder.name, name)
        records[folder.name] = p11.sha(path)
    return records


def marker_action(frame, delay):
    usable = frame.loc[frame.cycle.ge(39) & frame.in_domain].sort_values('cycle')
    tau = int(usable.cycle.iloc[0]) if len(usable) else np.nan
    return dict(decision=tau, scheduled=tau+delay, first_available=tau,
                initial_insufficient=False, bound_lead=np.nan, trigger_shortfall=np.nan)


def compare_pairs(candidate, reference, rng):
    pairs = candidate.merge(reference, on=['unit', 'fold'], suffixes=('_p', '_b')).sort_values('unit')
    assert len(pairs) == len(candidate) == len(reference)
    x, y = pairs.utilised_p.to_numpy(), pairs.utilised_b.to_numpy()
    indices = rng.integers(0, len(pairs), size=(2000, len(pairs)))
    delta = (x[indices]-y[indices]).mean(axis=1)
    saving = 1-y[indices].mean(axis=1)/x[indices].mean(axis=1)
    both = pairs.has_decision_p & pairs.has_decision_b
    return dict(common=len(pairs), same_date=int((both & pairs.scheduled_p.eq(pairs.scheduled_b)).sum()),
                later_date=int((both & pairs.scheduled_p.gt(pairs.scheduled_b)).sum()),
                earlier_date=int((both & pairs.scheduled_p.lt(pairs.scheduled_b)).sum()),
                candidate_without_decision=int((~pairs.has_decision_p).sum()),
                candidate_reached=int(pairs.reached_endpoint_p.sum()), reference_reached=int(pairs.reached_endpoint_b.sum()),
                delta_mean_life=float(np.mean(x-y)), life_ci_low=float(np.quantile(delta, .025)),
                life_ci_high=float(np.quantile(delta, .975)), relative_saving=float(1-np.mean(y)/np.mean(x)),
                saving_ci_low=float(np.quantile(saving, .025)), saving_ci_high=float(np.quantile(saving, .975)))


def contrasts(previous, controls):
    rng = np.random.default_rng(SEED)
    records = []
    old = previous.loc[previous.dataset.eq('complete')]
    new = controls.loc[controls.dataset.eq('complete')]
    for key, g in old.loc[old.method.ne('AGE')].groupby(['subset', 'repeat', 'policy_id'], sort=True):
        subset, repeat, policy = key
        delay = int(g.delay.iloc[0])
        reference = new.loc[new.subset.eq(subset) & new.repeat.eq(repeat) & new.delay.eq(delay)]
        records.append(dict(subset=subset, repeat=repeat, policy_id=policy, delay=delay,
                            reference=f'HI_MARKER_D{delay}', **compare_pairs(g, reference, rng)))
    for key, g in new.groupby(['subset', 'repeat', 'policy_id'], sort=True):
        subset, repeat, policy = key
        delay = int(g.delay.iloc[0])
        reference = old.loc[old.subset.eq(subset) & old.repeat.eq(repeat) & old.policy_id.eq(f'AGE_D{delay}')]
        records.append(dict(subset=subset, repeat=repeat, policy_id=policy, delay=delay,
                            reference=f'AGE_D{delay}', **compare_pairs(g, reference, rng)))
    return pd.DataFrame(records)


def decomposition(previous, controls):
    rows = []
    old = previous.loc[previous.dataset.eq('complete')]
    new = controls.loc[controls.dataset.eq('complete')]
    for key, g in old.loc[old.method.ne('AGE')].groupby(['subset', 'repeat', 'policy_id'], sort=True):
        subset, repeat, policy = key
        delay = int(g.delay.iloc[0])
        marker = new.loc[new.subset.eq(subset) & new.repeat.eq(repeat) & new.delay.eq(delay)]
        age = old.loc[old.subset.eq(subset) & old.repeat.eq(repeat) & old.policy_id.eq(f'AGE_D{delay}')]
        p, h, a = float(g.utilised.mean()), float(marker.utilised.mean()), float(age.utilised.mean())
        rows.append(dict(subset=subset, repeat=repeat, policy_id=policy, delay=delay,
                         mean_phm=p, mean_marker=h, mean_age=a, total_life_gain=p-a,
                         marker_life_gain=h-a, prognosis_life_gain=p-h,
                         prognosis_share=(p-h)/(p-a) if p > a else np.nan,
                         marker_share=(h-a)/(p-a) if p > a else np.nan,
                         cost_ratio_total=a/p, cost_ratio_marker=a/h, cost_ratio_incremental=h/p))
    return pd.DataFrame(rows)


def refresh_manifest():
    (OUT / 'manifest.json').write_text(json.dumps({p.name: p11.sha(p) for p in sorted(OUT.iterdir())
                                                  if p.is_file() and p.name != 'manifest.json'}, indent=2), encoding='utf-8')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert not (OUT / 'metadata.json').exists(), 'Preserve completed analysis'
    before = integrity()
    files = [Path(__file__), ROOT / 'experiments/pilot_removal_11.py',
             ROOT / 'experiments/protocolo_controle_marco_11a.md', ROOT / 'experiments/test_pilot_landmark_control_11a.py',
             ROOT / 'experiments/verify_pilot_landmark_control_11a.py', PREVIOUS / 'decisions.csv',
             PREVIOUS / 'manifest.json', SOURCE / 'splits.json', SOURCE / 'manifest.json']
    files += sorted(SOURCE.glob('predictions_*_complete.csv.gz'))+sorted(SOURCE.glob('predictions_*_truncated.csv.gz'))
    files += [ROOT / f'CMAPSSData/{kind}_{s}.txt' for s in ['FD001', 'FD003'] for kind in ['train', 'test', 'RUL']]
    initial = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=before,
                   inputs={str(p.relative_to(ROOT)): p11.sha(p) for p in files}, bootstrap_seed=SEED)
    (OUT / 'execution_start.json').write_text(json.dumps(initial, indent=2), encoding='utf-8')
    previous = pd.read_csv(PREVIOUS / 'decisions.csv')
    splits = json.loads((SOURCE / 'splits.json').read_text(encoding='utf-8'))
    rows = []
    for split in splits:
        subset, repeat, fold = split['subset'], split['repeat'], split['fold']
        for dataset in ['complete']+(['truncated'] if fold == 1 else []):
            pred = pd.read_csv(SOURCE / f'predictions_{subset}_r{repeat}_f{fold}_{dataset}.csv.gz')
            a = pred.loc[pred.method.eq('ISO'), ['unit', 'cycle', 'hi', 'crossing', 'in_domain']].reset_index(drop=True)
            b = pred.loc[pred.method.eq('RF_SLOPE'), ['unit', 'cycle', 'hi', 'crossing', 'in_domain']].reset_index(drop=True)
            pd.testing.assert_frame_equal(a, b)
            env = previous.loc[previous.subset.eq(subset) & previous.repeat.eq(repeat) & previous.fold.eq(fold) &
                               previous.dataset.eq(dataset) & previous.policy_id.eq('AGE_D1')]
            for r in env.itertuples():
                # The environmental endpoint ends observation; it does not trigger this policy.
                frame = a.loc[a.unit.eq(r.unit) & a.cycle.lt(r.endpoint), ['cycle', 'in_domain']]
                for delay in [1, 2]:
                    action = marker_action(frame, delay)
                    rows.append(dict(subset=subset, repeat=repeat, fold=fold, dataset=dataset, unit=r.unit,
                                     policy_id=f'HI_MARKER_D{delay}', method='HI_MARKER', anchor='condition', alpha=0.,
                                     reserve=0, delay=delay, phase='control',
                                     **p11.assess(action, r.endpoint, r.last_observed, dataset == 'complete')))
        print(subset, repeat, fold, 'marker control', flush=True)
    controls = pd.DataFrame(rows)
    result = contrasts(previous, controls)
    assert not result.loc[result.reference.str.startswith('HI_MARKER'), 'earlier_date'].any()
    summary = pd.concat([p11.summaries(previous), p11.summaries(controls)], ignore_index=True)
    for name, data in [('controls', controls), ('summary', summary), ('contrasts', result),
                        ('decomposition', decomposition(previous, controls))]:
        data.to_csv(OUT / f'{name}.csv', index=False)
    assert integrity() == before
    metadata = initial | dict(finished_utc=datetime.now(timezone.utc).isoformat(), no_refitting=True,
                             no_inspection=True, no_calendar_projection=True, previous_artifacts_intact=True,
                             control_rows=len(controls), contrasts=len(result))
    (OUT / 'metadata.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
    refresh_manifest()
    print(summary.loc[summary.method.eq('HI_MARKER') & summary.dataset.eq('complete'),
                      ['subset', 'repeat', 'policy_id', 'decisions', 'late_count', 'exact_count', 'mean_utilised']].to_string(index=False))


if __name__ == '__main__':
    main()
