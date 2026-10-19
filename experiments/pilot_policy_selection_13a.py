"""P13.1: internally selected condition policies with frozen outer HI and references."""

import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits

import pilot_f_uncertainty_10 as p10
import pilot_removal_11 as p11
import pilot_landmark_control_11a as p11a

ROOT = p11.ROOT
SOURCE = p10.OUT
OUT = ROOT / 'experiments/artifacts/pilot_policy_selection_13a'
GRID = {'threshold': [.2, .3, .4, .5, .6, .7, .8], 'wait': [0, 1, 2, 5, 10]}
SEED = 20261017


def integrity():
    records = {}
    for folder in sorted((ROOT / 'experiments/artifacts').glob('pilot_*')):
        manifest = folder / 'manifest.json'
        if folder == OUT or not manifest.exists():
            continue
        for name, digest in json.loads(manifest.read_text(encoding='utf-8')).items():
            assert p11.sha(folder / name) == digest, (folder.name, name)
        records[folder.name] = p11.sha(manifest)
    return records


def inner_partitions(split):
    ids = np.array(sorted(split['fit']+split['converter']))
    seed = split['seed']+10000*split['fold']
    blocks = np.array_split(np.random.default_rng(seed).permutation(ids), 4)
    result = []
    for j, block in enumerate(blocks, start=1):
        rest = np.setdiff1d(ids, block)
        shuffled = np.random.default_rng(seed+100*j).permutation(rest)
        result.append(dict(inner_fold=j, fit=sorted(shuffled[:25].tolist()),
                           unused=sorted(shuffled[25:].tolist()), validation=sorted(block.tolist())))
    return result


def health_values(inputs, model):
    data = inputs.drop(columns=['end', 'rul'], errors='ignore').reset_index(drop=True)
    z = p10.p05.standardise(p10.centred_sensors(data), model['stats'])
    available = data.cycle.ge(20)
    out = data.loc[available, ['unit', 'cycle']].copy()
    out['hi'] = p10.p05.empirical_hi(z, model['beta'])[np.asarray(available)]
    return out


def condition_action(frame, family, value, delay):
    g = frame.sort_values('cycle')
    threshold = value if family == 'threshold' else .5
    hits = g.loc[g.hi.le(threshold), 'cycle']
    first = max(39, int(hits.min())) if len(hits) else np.nan
    tau = first+(int(value) if family == 'wait' else 0)
    observed = bool(len(g) and np.isfinite(tau) and tau <= g.cycle.max())
    return dict(decision=tau if observed else np.nan, scheduled=tau+delay if observed else np.nan,
                first_available=first if len(g) and first <= g.cycle.max() else np.nan,
                initial_insufficient=False, bound_lead=np.nan, trigger_shortfall=np.nan)


def candidate_metrics(decisions):
    rows = []
    for key, g in decisions.groupby(['family', 'value', 'delay'], sort=True):
        rows.append(dict(zip(['family', 'value', 'delay'], key)) |
                    dict(total=len(g), decisions=int(g.has_decision.sum()), events=int(g.reached_endpoint.sum()),
                         late_count=int(g.late.sum()), exact_count=int(g.exact_endpoint.sum()),
                         mean_utilised=float(g.utilised.mean()), cost_per_cycle=len(g)/g.utilised.sum()))
    return pd.DataFrame(rows)


def select_rules(metrics):
    rows = []
    for (family, delay), g in metrics.groupby(['family', 'delay'], sort=True):
        feasible = g.loc[g.decisions.eq(g.total) & g.events.le(.02*g.total+1e-9)].copy()
        pool = feasible if len(feasible) else g.copy()
        pool['prudent_tie'] = pool.value if family == 'threshold' else -pool.value
        keys = ['mean_utilised', 'prudent_tie'] if len(feasible) else ['events', 'mean_utilised', 'prudent_tie']
        ascending = [False, False] if len(feasible) else [True, False, False]
        choice = pool.sort_values(keys, ascending=ascending).iloc[0]
        rows.append(dict(family=family, delay=int(delay), selected_value=float(choice.value),
                         selection_feasible=bool(len(feasible)), feasible_candidates=len(feasible),
                         internal_n=int(choice.total), internal_events=int(choice.events),
                         internal_mean_life=float(choice.mean_utilised)))
    return pd.DataFrame(rows)


def comparisons(decisions):
    rng = np.random.default_rng(SEED)
    rows = []
    for key, g in decisions.loc[decisions.phase.eq('selected')].groupby(['subset', 'repeat', 'policy_id'], sort=True):
        subset, repeat, policy = key
        delay = int(g.delay.iloc[0])
        for reference in [f'HI_MARKER_D{delay}', f'ISO_LOWER98_M15_D{delay}']:
            b = decisions.loc[decisions.subset.eq(subset) & decisions.repeat.eq(repeat) & decisions.policy_id.eq(reference)]
            rows.append(dict(subset=subset, repeat=repeat, policy_id=policy, reference=reference,
                             **p11a.compare_pairs(g, b, rng)))
    return pd.DataFrame(rows)


def refresh_manifest():
    (OUT / 'manifest.json').write_text(json.dumps({x.name: p11.sha(x) for x in sorted(OUT.iterdir())
                                                  if x.is_file() and x.name != 'manifest.json'}, indent=2), encoding='utf-8')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert not (OUT / 'metadata.json').exists(), 'Preserve completed experiment'
    prior = integrity()
    splits = json.loads((SOURCE / 'splits.json').read_text(encoding='utf-8'))
    files = [Path(__file__), ROOT / 'experiments/protocolo_selecao_decisoria_13a.md',
             ROOT / 'experiments/test_pilot_policy_selection_13a.py', ROOT / 'experiments/verify_pilot_policy_selection_13a.py',
             SOURCE / 'splits.json', SOURCE / 'manifest.json', p11.OUT / 'decisions.csv', p11a.OUT / 'controls.csv']
    files += [ROOT / f'experiments/{name}.py' for name in ['pilot_f_uncertainty_10', 'pilot_removal_11',
              'pilot_landmark_control_11a', 'pilot_fd001', 'pilot_fd001_04', 'pilot_fd001_05', 'pilot_fd003_06', 'pilot_hi_trajectory_08']]
    files += [ROOT / f'CMAPSSData/train_{s}.txt' for s in ['FD001', 'FD003']]
    files += sorted(SOURCE.glob('models_*.joblib'))+sorted(SOURCE.glob('predictions_*_complete.csv.gz'))
    initial = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=prior,
                   inputs={str(x.relative_to(ROOT)): p11.sha(x) for x in files}, grid=GRID, bootstrap_seed=SEED)
    (OUT / 'execution_start.json').write_text(json.dumps(initial, indent=2), encoding='utf-8')
    inputs = {s: p10.read_inputs('train', s) for s in ['FD001', 'FD003']}
    decisions_internal, metrics_all, selected_all, partitions, freezes = [], [], [], [], []
    # Phase A never reads outer evaluation outcomes/references or the calibration U paths.
    for split in splits:
        subset, repeat, fold = split['subset'], split['repeat'], split['fold']
        tag = f'{subset}_r{repeat}_f{fold}'
        development = sorted(split['fit']+split['converter'])
        data = inputs[subset].loc[inputs[subset].unit.isin(development)].reset_index(drop=True)
        ends = data.groupby('unit').cycle.max()
        local, trajectories = [], []
        for part in inner_partitions(split):
            j = part['inner_fold']
            fit = data.loc[data.unit.isin(part['fit'])].reset_index(drop=True)
            validation = data.loc[data.unit.isin(part['validation'])].reset_index(drop=True)
            model = p10.fit_health(fit, subset)
            joblib.dump(model, OUT / f'inner_hi_{tag}_v{j}.joblib', compress=3)
            h = health_values(validation, model).assign(inner_fold=j)
            trajectories.append(h)
            partitions.append(dict(subset=subset, repeat=repeat, fold=fold, **part))
            for unit in part['validation']:
                end = int(ends.loc[unit])
                g = h.loc[h.unit.eq(unit) & h.cycle.lt(end)]
                for family, grid in GRID.items():
                    for value in grid:
                        for delay in [1, 2]:
                            action = condition_action(g, family, value, delay)
                            local.append(dict(unit=unit, inner_fold=j, family=family, value=value, delay=delay,
                                              **p11.assess(action, end, end, True)))
        local = pd.DataFrame(local)
        metrics = candidate_metrics(local)
        chosen = select_rules(metrics)
        for frame in [local, metrics, chosen]:
            frame['subset'], frame['repeat'], frame['fold'] = subset, repeat, fold
        decisions_internal.append(local); metrics_all.append(metrics); selected_all.append(chosen)
        pd.concat(trajectories, ignore_index=True).to_csv(OUT / f'inner_health_{tag}.csv.gz', index=False, compression='gzip')
        metrics.to_csv(OUT / f'internal_metrics_{tag}.csv', index=False)
        freezes.append(dict(subset=subset, repeat=repeat, fold=fold, selections=chosen.to_dict('records'),
                            metrics_sha256=p11.sha(OUT / f'internal_metrics_{tag}.csv'),
                            timestamp_utc=datetime.now(timezone.utc).isoformat()))
        (OUT / 'selection_freezes.json').write_text(json.dumps(freezes, indent=2), encoding='utf-8')
        print(tag, 'selection frozen', flush=True)
    selected = pd.concat(selected_all, ignore_index=True)
    for name, frame in [('internal_decisions', pd.concat(decisions_internal, ignore_index=True)),
                        ('internal_metrics', pd.concat(metrics_all, ignore_index=True)), ('selections', selected)]:
        frame.to_csv(OUT / f'{name}.csv', index=False)
    (OUT / 'inner_splits.json').write_text(json.dumps(partitions, indent=2), encoding='utf-8')
    # Phase B starts only after every internal selection is frozen.
    (OUT / 'evaluation_start.json').write_text(json.dumps(dict(timestamp_utc=datetime.now(timezone.utc).isoformat(),
                                                              selections_sha256=p11.sha(OUT / 'selections.csv')), indent=2), encoding='utf-8')
    old = pd.read_csv(p11.OUT / 'decisions.csv')
    marker = pd.read_csv(p11a.OUT / 'controls.csv')
    reference_ids = [f'{rule}_D{d}' for rule in ['AGE', 'ISO_POINT_M15', 'RF_SLOPE_POINT_M15',
                     'ISO_LOWER98_M15', 'RF_SLOPE_LOWER98_M15'] for d in [1, 2]]
    references = pd.concat([old.loc[old.dataset.eq('complete') & old.policy_id.isin(reference_ids)],
                            marker.loc[marker.dataset.eq('complete')]], ignore_index=True)
    references['phase'] = 'reference'
    external, max_hi_difference = [], 0.
    for split in splits:
        subset, repeat, fold = split['subset'], split['repeat'], split['fold']
        tag = f'{subset}_r{repeat}_f{fold}'
        raw = inputs[subset].loc[inputs[subset].unit.isin(split['evaluation'])].reset_index(drop=True)
        ends = raw.groupby('unit').cycle.max()
        bundle = joblib.load(SOURCE / f'models_{tag}.joblib')
        h = health_values(raw, bundle['health'])
        archived = pd.read_csv(SOURCE / f'predictions_{tag}_complete.csv.gz')
        a = archived.loc[archived.method.eq('ISO'), ['unit', 'cycle', 'hi']].sort_values(['unit', 'cycle'])
        b = h.loc[h.cycle.ge(39)].sort_values(['unit', 'cycle'])
        np.testing.assert_array_equal(a[['unit', 'cycle']], b[['unit', 'cycle']])
        diff = float(np.max(abs(a.hi.to_numpy()-b.hi.to_numpy())))
        assert diff < 1e-10
        max_hi_difference = max(max_hi_difference, diff)
        h.to_csv(OUT / f'outer_health_{tag}.csv.gz', index=False, compression='gzip')
        choices = selected.loc[selected.subset.eq(subset) & selected.repeat.eq(repeat) & selected.fold.eq(fold)]
        for unit in split['evaluation']:
            end = int(ends.loc[unit])
            g = h.loc[h.unit.eq(unit) & h.cycle.lt(end)]
            for choice in choices.itertuples():
                name = 'HI_THRESHOLD_SELECTED' if choice.family == 'threshold' else 'HI_WAIT_SELECTED'
                action = condition_action(g, choice.family, choice.selected_value, choice.delay)
                external.append(dict(subset=subset, repeat=repeat, fold=fold, unit=unit, dataset='complete',
                                     policy_id=f'{name}_D{choice.delay}', method=name, anchor=choice.family,
                                     alpha=0., reserve=0, delay=choice.delay, phase='selected',
                                     selected_value=choice.selected_value, selection_feasible=choice.selection_feasible,
                                     **p11.assess(action, end, end, True)))
        print(tag, 'external evaluation', flush=True)
    result = pd.concat([pd.DataFrame(external), references], ignore_index=True)
    for name, frame in [('decisions', result), ('summary', p11.summaries(result)), ('contrasts', comparisons(result))]:
        frame.to_csv(OUT / f'{name}.csv', index=False)
    assert integrity() == prior
    metadata = initial | dict(finished_utc=datetime.now(timezone.utc).isoformat(), previous_artifacts_intact=True,
                             inner_hi_fits=len(partitions), selection_rows=len(selected), external_rows=len(result),
                             maximum_outer_hi_difference=max_hi_difference, no_inspection=True, no_calendar_projection=True,
                             u_used_for_selection=False, outer_predictors_refitted=False)
    (OUT / 'metadata.json').write_text(json.dumps(metadata, indent=2), encoding='utf-8')
    refresh_manifest()


if __name__ == '__main__':
    with threadpool_limits(limits=1):
        main()
