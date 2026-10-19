"""Independently reconstruct P11 actions, denominators, costs and paired contrasts."""

import json

import numpy as np
import pandas as pd

import pilot_removal_11 as p11


def main():
    out = p11.OUT
    metadata = json.loads((out / 'metadata.json').read_text(encoding='utf-8'))
    assert p11.integrity() == metadata['previous_manifests']
    archived = out / 'frozen_input_archive.json'
    mapping = json.loads(archived.read_text(encoding='utf-8')) if archived.exists() else {}
    for name, digest in metadata['inputs'].items():
        assert p11.sha(p11.ROOT / mapping.get(name, name)) == digest, name
    for name, digest in json.loads((out / 'manifest.json').read_text(encoding='utf-8')).items():
        assert p11.sha(out / name) == digest, name
    decisions = pd.read_csv(out / 'decisions.csv')
    summary = pd.read_csv(out / 'summary.csv')
    contrasts = pd.read_csv(out / 'contrasts.csv')
    splits = json.loads((p11.SOURCE / 'splits.json').read_text(encoding='utf-8'))
    controls = json.loads((out / 'controls.json').read_text(encoding='utf-8'))
    quantiles = pd.read_csv(p11.SOURCE / 'quantiles.csv')
    assert len(decisions) == 31200 and len(summary) == 312 and len(contrasts) == 144
    checked = 0
    for split, control in zip(splits, controls):
        subset, repeat, fold = split['subset'], split['repeat'], split['fold']
        training = p11.read_inputs('train', subset).groupby('unit').cycle.max()
        development = sorted(split['fit']+split['converter'])
        age = int(min(training.loc[development]))-1
        assert control['development'] == development and control['age'] == age
        qs = quantiles.loc[quantiles.subset.eq(subset) & quantiles.repeat.eq(repeat) & quantiles.fold.eq(fold) & quantiles.scope.eq('path')]
        for dataset in ['complete']+(['truncated'] if fold == 1 else []):
            pred = pd.read_csv(p11.SOURCE / f'predictions_{subset}_r{repeat}_f{fold}_{dataset}.csv.gz')
            if dataset == 'complete':
                ends = training.loc[split['evaluation']]
                lasts = ends
            else:
                lasts = p11.read_inputs('test', subset).groupby('unit').cycle.max()
                ends = lasts+pd.Series(np.loadtxt(p11.ROOT / f'CMAPSSData/RUL_{subset}.txt'), index=range(1, 101))
            groups = {(int(unit), method): g.sort_values('cycle') for (unit, method), g in pred.groupby(['unit', 'method'])}
            saved = decisions.loc[decisions.subset.eq(subset) & decisions.repeat.eq(repeat) & decisions.fold.eq(fold) & decisions.dataset.eq(dataset)]
            assert len(saved) == len(ends)*26
            for r in saved.itertuples():
                end, last = int(ends.loc[r.unit]), int(lasts.loc[r.unit])
                tau, lead, shortfall = np.nan, np.nan, np.nan
                initial = False
                if r.method == 'AGE':
                    if age-r.delay <= min(last, end-1):
                        tau = age-r.delay
                    q = 0.
                else:
                    g = groups.get((r.unit, r.method), pred.iloc[:0])
                    g = g.loc[g.in_domain & g.cycle.lt(end)]
                    q = 0. if r.anchor == 'point' else float(qs.loc[qs.method.eq(r.method) & np.isclose(qs.alpha, r.alpha), 'q_late'].iloc[0])
                    initial = bool(len(g) and max(0., g.predicted_rul.iloc[0]-q) < r.reserve+r.delay-1e-9)
                    for point in g.itertuples():
                        current_lead = max(0., point.predicted_rul-q)
                        if current_lead <= r.reserve+r.delay+1e-9:
                            tau = point.cycle
                            lead = current_lead
                            shortfall = max(0., r.reserve+r.delay-current_lead)
                            break
                scheduled = tau+r.delay if np.isfinite(tau) else np.nan
                np.testing.assert_allclose([r.decision, r.scheduled, r.q_late, r.bound_lead, r.trigger_shortfall],
                                           [tau, scheduled, q, lead, shortfall], equal_nan=True, atol=1e-8)
                assert r.initial_insufficient == initial
                assert r.has_decision == bool(np.isfinite(tau))
                assert r.late == bool(np.isfinite(scheduled) and scheduled > end)
                assert r.exact_endpoint == bool(np.isfinite(scheduled) and scheduled == end)
                assert r.execution_observed == bool(np.isfinite(scheduled) and scheduled < end and scheduled <= last)
                if dataset == 'complete':
                    expected = min(scheduled, end) if np.isfinite(scheduled) else end
                    assert r.utilised == expected
                    assert r.reached_endpoint == bool(not np.isfinite(scheduled) or scheduled >= end)
                    assert r.status == ('endpoint_without_decision' if not np.isfinite(scheduled) else
                                        'late_schedule' if scheduled > end else 'at_endpoint' if scheduled == end else 'preventive_schedule')
                else:
                    assert np.isnan(r.utilised) and np.isnan(r.reached_endpoint)
                    if not np.isfinite(scheduled):
                        assert r.status == 'right_censored'
                checked += 1
    for r in summary.itertuples():
        g = decisions.loc[decisions.subset.eq(r.subset) & decisions.dataset.eq(r.dataset) & decisions.repeat.eq(r.repeat) & decisions.policy_id.eq(r.policy_id)]
        assert r.total == len(g) == 100
        assert r.decisions == g.has_decision.sum()
        assert r.late_count == g.late.sum() and r.exact_count == g.exact_endpoint.sum()
        assert r.without_decision == (~g.has_decision).sum()
        if r.dataset == 'complete':
            np.testing.assert_allclose([r.mean_utilised, r.cost_per_cycle, r.restorations_per_10000_cycles],
                                       [g.utilised.mean(), 100/g.utilised.sum(), 1e6/g.utilised.sum()], atol=1e-9)
            strict = bool(g.has_decision.all() and g.late.sum() <= 2)
            assert r.passes_strict_screen == strict
            assert r.passes_prudent_screen == bool(strict and not g.exact_endpoint.any())
    rng = np.random.default_rng(20261017)
    for r in contrasts.itertuples():
        pop = decisions.loc[decisions.dataset.eq('complete') & decisions.subset.eq(r.subset) & decisions.repeat.eq(r.repeat)]
        a = pop.loc[pop.policy_id.eq(r.policy_id)]
        b = pop.loc[pop.policy_id.eq(f'AGE_D{r.delay}')]
        pair = a.merge(b, on=['unit', 'fold'], suffixes=('_a', '_b')).sort_values('unit')
        x, y = pair.utilised_a.to_numpy(), pair.utilised_b.to_numpy()
        idx = rng.integers(0, 100, size=(2000, 100))
        delta = (x[idx]-y[idx]).mean(axis=1)
        saving = 1-y[idx].mean(axis=1)/x[idx].mean(axis=1)
        np.testing.assert_allclose([r.delta_mean_life, r.life_ci_low, r.life_ci_high, r.relative_saving, r.saving_ci_low, r.saving_ci_high],
                                   [(x-y).mean(), *np.quantile(delta, [.025, .975]), 1-y.mean()/x.mean(), *np.quantile(saving, [.025, .975])], atol=1e-9)
    front = pd.read_csv(out / 'frontier.csv')
    for _, g in front.groupby(['subset', 'repeat', 'delay']):
        for a in g.itertuples():
            scores_a = [a.without_decision, a.late_count, a.exact_count, a.mean_unused]
            dominates = False
            for b in g.itertuples():
                scores_b = [b.without_decision, b.late_count, b.exact_count, b.mean_unused]
                dominates |= all(x <= y+1e-9 for x, y in zip(scores_b, scores_a)) and any(x < y-1e-9 for x, y in zip(scores_b, scores_a))
            assert a.non_dominated == (not dominates)
    result = dict(status='passed', decisions_checked=checked, controls_checked=len(controls), summaries_checked=len(summary),
                  paired_contrasts_checked=len(contrasts), frontier_rows_checked=len(front),
                  prior_artifacts_intact=p11.integrity() == metadata['previous_manifests'],
                  verifier_sha256=p11.sha(p11.ROOT / 'experiments/verify_pilot_removal_11.py'))
    (out / 'verification.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    p11.refresh_manifest()
    print(json.dumps(result))


if __name__ == '__main__':
    main()
