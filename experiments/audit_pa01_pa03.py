"""Read-only reconstruction of archived evidence for PA01--PA03; JSON on stdout."""
import hashlib
import importlib.metadata
import json
import platform
import sys
import warnings
from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits

import coefficient_stability_19b as stability
import explainability_core_13b as core
import inspection_arm_17b as inspection
import pilot_explainability_13b as replay

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def close(actual, expected):
    np.testing.assert_allclose(actual, expected, atol=1e-10, rtol=1e-10, equal_nan=True)


def protect():
    paths = list((ROOT / 'experiments/artifacts').glob('*/manifest.json'))
    paths += list((ROOT / 'experiments/congelamento_2026-10-18').glob('*'))
    paths += list((ROOT / 'experiments').glob('*.py'))
    paths += list((ROOT / 'experiments').glob('protocolo*.md'))
    for folder, patterns in ((replay.OUT, ('*.npz', '*.csv*', 'noise_*.joblib', '*.json', '*.py')),
                             (replay.p10.OUT, ('models_*.joblib', 'splits.json')),
                             (stability.SOURCES['FD002'], ('models_*.joblib', 'decisions.csv')),
                             (inspection.OUT, ('*.json', 'expectations.csv.gz')),
                             (stability.OUT, ('*.csv', '*.json'))):
        for pattern in patterns:
            paths += list(folder.glob(pattern))
    paths += list(inspection.SOURCES.values())
    paths += [ROOT / f'CMAPSSData/train_{subset}.txt' for subset in ('FD001', 'FD003')]
    return {str(path.relative_to(ROOT)): digest(path) for path in paths if path.is_file()}


def provenance():
    records = []
    for folder in (replay.OUT, inspection.OUT, stability.OUT):
        metadata = json.loads((folder / 'metadata.json').read_text())
        sources = metadata.get('sources', metadata.get('inputs', {}))
        archives = {}
        if folder == replay.OUT:
            archives = json.loads((folder / 'amendments.json').read_text())['input_archives']
        for name, expected in sources.items():
            name = name.replace('\\', '/')
            if not name.endswith('.py'):
                continue
            path = ROOT / name if '/' in name else ROOT / 'experiments' / name
            content = path.read_bytes()
            lf = content.replace(b'\r\n', b'\n')
            forms = {'exact': content, 'LF': lf, 'CRLF': lf.replace(b'\n', b'\r\n')}
            matches = [form for form, value in forms.items() if hashlib.sha256(value).hexdigest() == expected]
            records.append(dict(archive=folder.name, source=str(path.relative_to(ROOT)),
                                expected_sha256=expected, current_sha256=digest(path), matching_forms=matches))
            if name in archives:
                records[-1]['initial_snapshot_matches'] = digest(folder / archives[name]) == expected
        if folder == replay.OUT:
            final = json.loads((folder / 'final_checks.json').read_text())['current_sources']
            for name, expected in final.items():
                path = ROOT / 'experiments' / name
                records.append(dict(archive='pilot_explainability_13b/final_checks', source=str(path.relative_to(ROOT)),
                                    expected_sha256=expected, current_sha256=digest(path),
                                    matching_forms=['exact'] if digest(path) == expected else [],
                                    archived_snapshot_matches=digest(folder / ('source_' + name)) == expected))
    return records


def explanation_audit():
    splits = json.loads((replay.p10.OUT / 'splits.json').read_text())
    inputs = {subset: replay.p10.read_inputs('train', subset) for subset in ('FD001', 'FD003')}
    groups = ['phase', 'kind', 'epsilon']
    action_totals = []
    support_totals = []
    units = points = original_outside = action_rows = 0
    maximum_error = 0.
    threshold_ranges = []
    for split in splits:
        subset, repeat, fold = (split[key] for key in ('subset', 'repeat', 'fold'))
        tag = f'{subset}_r{repeat}_f{fold}'
        health = joblib.load(replay.p10.OUT / f'models_{tag}.joblib')['health']
        noise = joblib.load(replay.OUT / f'noise_{tag}.joblib')
        reconstructed = core.noise_model(inputs[subset].loc[inputs[subset].unit.isin(split['fit'])])
        assert noise['fit_units'] == reconstructed['fit_units'] == sorted(split['fit'])
        for key in noise:
            close(noise[key], reconstructed[key])
        threshold_ranges.append(dict(tag=tag, active_channels=len(noise['active']),
                                     md_limit=noise['md_limit'],
                                     channel_limits=noise['channel_limits'].tolist()))
        baseline = np.load(replay.OUT / f'baseline_{tag}.npz')
        saved = np.load(replay.OUT / f'global_paths_{tag}.npz')
        shifts = np.load(replay.OUT / f'shifts_{tag}.npz')['shifts']
        frames = {phase: pd.read_csv(replay.OUT / f'{phase}_actions_{tag}.csv.gz')
                  for phase in ('global', 'local')}
        stored_support = pd.read_csv(replay.OUT / f'support_{tag}.csv.gz')
        for unit in np.unique(baseline['unit']):
            raw = inputs[subset].loc[inputs[subset].unit.eq(unit)].sort_values('cycle')[core.SENSORS].to_numpy()[:-1]
            means = pd.DataFrame(raw).rolling(15, min_periods=15).mean().to_numpy()
            contributions, channels, weights = core.base_contributions(raw, health)
            departure = means[19:, channels] - means[19, channels]
            normalised = departure * health['stats']['direction'] / health['stats']['scale']
            published = normalised * health['beta']
            close(published, departure * weights)
            close(contributions[19:, channels], published)
            base_mask = baseline['unit'] == unit
            close(contributions[19:], baseline['C'][base_mask])
            expected_hi = np.clip(1. - np.maximum(published.sum(axis=1), 0.), 0., 1.)
            close(expected_hi, baseline['H'][base_mask])
            maximum_error = max(maximum_error, float(np.max(abs(contributions[19:, channels] - published))))
            units += 1
            points += published.size
            early = core.support(raw[:20], np.arange(1, 21), shifts, noise)
            outside = np.concatenate([early[:, :18], saved['outside'][:, saved['unit'] == unit]], axis=1)
            direct_outside = core.support(raw, np.arange(1, len(raw) + 1), shifts, noise)
            np.testing.assert_array_equal(outside, direct_outside)
            counts = outside[:, 4:].sum(axis=1)
            unit_support = stored_support.loc[stored_support.unit.eq(unit)].sort_values('variant')
            close(counts, unit_support.outside_count)
            close(np.full(len(counts), len(raw) - 5), unit_support.increments)
            accumulated = np.cumsum(outside, axis=1)
            for phase, frame in frames.items():
                group = frame.loc[frame.unit.eq(unit)]
                end = len(raw)
                base_cuts = group.base_decision.fillna(end).to_numpy(dtype=int)
                base_inside = accumulated[0, base_cuts - 2] - accumulated[0, 3] == 0
                if phase == 'global':
                    cuts = group.decision.fillna(end).to_numpy(dtype=int)
                    variants = group.variant.to_numpy(dtype=int)
                    perturbed_inside = accumulated[variants, cuts - 2] - accumulated[variants, 3] == 0
                    expected_inside = base_inside & perturbed_inside
                    original_outside += int((~base_inside[group.variant.eq(0)]).sum())
                else:
                    expected_inside = np.zeros(len(group), dtype=bool)
                    if base_inside.any():
                        for cutoff, local in group.groupby('cutoff'):
                            indices = group.index.get_indexer(local.index)
                            local_outside = core.support(raw[:int(cutoff)], np.arange(1, int(cutoff) + 1),
                                                         shifts, noise, int(cutoff))
                            cumulative = np.cumsum(local_outside, axis=1)
                            cuts = local.decision.fillna(cutoff).to_numpy(dtype=int)
                            variants = local.variant.to_numpy(dtype=int)
                            perturbed_inside = cumulative[variants, cuts - 2] - cumulative[variants, 3] == 0
                            expected_inside[indices] = base_inside[indices] & perturbed_inside
                np.testing.assert_array_equal(expected_inside, group.within_support.to_numpy())
                action_rows += len(group)
        for phase, frame in frames.items():
            frame = frame.loc[frame.epsilon.gt(0)].copy()
            frame['variants'] = 1
            frame['paired_dates'] = frame.decision.notna() & frame.base_decision.notna()
            frame['supported_variants'] = frame.within_support & frame.paired_dates
            action_totals.append(frame.groupby(groups)[['variants', 'paired_dates', 'supported_variants']].sum())
        support_totals.append(stored_support.groupby('kind')[['increments', 'outside_count']].sum())
        print(f'{tag}: contributions, fit-only noise, prefixes and denominators checked', file=sys.stderr)
    totals = pd.concat(action_totals).groupby(groups).sum().sort_index()
    archived = pd.read_csv(replay.OUT / 'action_engines.csv').groupby(groups)[totals.columns].sum().sort_index()
    pd.testing.assert_frame_equal(totals, archived, check_dtype=False)
    support = pd.concat(support_totals).groupby('kind').sum()
    return dict(partitions=len(splits), engine_partition_rows=units, contribution_elements=points,
                maximum_equation_error=maximum_error, action_rows_checked=action_rows,
                baseline_action_prefixes_outside=original_outside,
                denominators=totals.reset_index().to_dict('records'),
                increment_counts=support.reset_index().to_dict('records'), thresholds=threshold_ranges)


def stability_audit():
    pairs, channels = stability.run()
    archived_pairs = pd.read_csv(stability.OUT / 'pairs.csv')
    archived_channels = pd.read_csv(stability.OUT / 'channels.csv')
    pd.testing.assert_frame_equal(pairs, archived_pairs, check_dtype=False, atol=1e-12, rtol=1e-12)
    pd.testing.assert_frame_equal(channels, archived_channels, check_dtype=False, atol=1e-12, rtol=1e-12)
    return dict(models=120, fold_pairs=len(pairs), channel_rows=len(channels),
                coefficient='beta; orientation recorded separately; active beta > 1e-9')


def monitoring_audit():
    metadata = json.loads((inspection.OUT / 'metadata.json').read_text())
    input_matches = {}
    for origin, path in inspection.SOURCES.items():
        content = path.read_bytes().replace(b'\r\n', b'\n')
        expected_hash = metadata['inputs'][origin]
        matches = [form for form, value in {'LF': content, 'CRLF': content.replace(b'\n', b'\r\n')}.items()
                   if hashlib.sha256(value).hexdigest() == expected_hash]
        assert matches, origin
        input_matches[origin] = dict(matching_forms=matches, archived_sha256=expected_hash,
                                    current_sha256=digest(path))
    decisions = inspection.load_decisions()
    actual = inspection.expectations(decisions)
    expected = pd.read_csv(inspection.OUT / 'expectations.csv.gz')
    pd.testing.assert_frame_equal(actual, expected, check_dtype=False, atol=1e-10, rtol=1e-10)
    metrics = ['util_h', 'late_h', 'exact_h', 'missing_h', 'inspections', 'rejection',
               'util_p', 'late_p', 'exact_p', 'missing_p']
    difference = float(np.max(abs(actual[metrics].to_numpy() - expected[metrics].to_numpy())))
    confirmation = pd.read_csv(inspection.SOURCES['confirmation'])
    no_landmark = confirmation.loc[confirmation.dataset.eq('complete') & confirmation.first_available.isna()
                                   & confirmation.policy_id.isin(decisions.policy_id)]
    assert not no_landmark.has_decision.any()
    return dict(archived_decision_rows=len(decisions), expectation_rows=len(actual),
                input_matches=input_matches,
                maximum_absolute_error=difference, confirmation_rows_without_landmark=len(no_landmark),
                no_landmark_examples=no_landmark[['subset', 'repeat', 'fold', 'unit', 'policy_id', 'endpoint']]
                .head(6).to_dict('records'), event_priority=['monitoring invalid', 'PHM decision', 'inspection'],
                monitoring_gates=[125, 126], first_S2_inspection=127)


def main():
    before = protect()
    result = dict(started_utc=datetime.now(timezone.utc).isoformat(), python=platform.python_version(),
                  packages={name: importlib.metadata.version(name) for name in ('numpy', 'pandas', 'scipy', 'scikit-learn', 'joblib')},
                  operation='Read-only verification; no fit, optimisation, policy change or archive output',
                  source_provenance=provenance(), protected_before=before)
    with warnings.catch_warnings(record=True) as caught, threadpool_limits(limits=1):
        warnings.simplefilter('always')
        result['PA01_PA02'] = explanation_audit()
        result['PA01_stability'] = stability_audit()
        result['PA03'] = monitoring_audit()
    result['warnings'] = sorted({f'{item.category.__name__}: {item.message}' for item in caught})
    result['protected_unchanged'] = before == protect()
    assert result['protected_unchanged']
    result['finished_utc'] = datetime.now(timezone.utc).isoformat()
    result['status'] = 'passed'
    print(json.dumps(result, indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
