"""Independent P11.1 verification of event-only decisions and incremental value."""

import json

import numpy as np
import pandas as pd

import pilot_landmark_control_11a as p


def main():
    out = p.OUT
    metadata = json.loads((out / 'metadata.json').read_text(encoding='utf-8'))
    assert p.integrity() == metadata['previous_manifests']
    for name, digest in metadata['inputs'].items():
        assert p.p11.sha(p.ROOT / name) == digest, name
    for name, digest in json.loads((out / 'manifest.json').read_text(encoding='utf-8')).items():
        assert p.p11.sha(out / name) == digest, name
    controls = pd.read_csv(out / 'controls.csv')
    previous = pd.read_csv(p.PREVIOUS / 'decisions.csv')
    summary = pd.read_csv(out / 'summary.csv')
    contrasts = pd.read_csv(out / 'contrasts.csv')
    decomp = pd.read_csv(out / 'decomposition.csv')
    assert len(controls) == 2400 and len(summary) == 336 and len(contrasts) == 156 and len(decomp) == 144
    checked = 0
    for split in json.loads((p.SOURCE / 'splits.json').read_text(encoding='utf-8')):
        subset, repeat, fold = split['subset'], split['repeat'], split['fold']
        training = p.p11.read_inputs('train', subset).groupby('unit').cycle.max()
        for dataset in ['complete']+(['truncated'] if fold == 1 else []):
            prediction = pd.read_csv(p.SOURCE / f'predictions_{subset}_r{repeat}_f{fold}_{dataset}.csv.gz')
            pred = prediction.loc[prediction.method.eq('ISO')]
            if dataset == 'complete':
                ends = training.loc[split['evaluation']]
                lasts = ends
            else:
                lasts = p.p11.read_inputs('test', subset).groupby('unit').cycle.max()
                ends = lasts+pd.Series(np.loadtxt(p.ROOT / f'CMAPSSData/RUL_{subset}.txt'), index=range(1, 101))
            rows = controls.loc[controls.subset.eq(subset) & controls.repeat.eq(repeat) & controls.fold.eq(fold) & controls.dataset.eq(dataset)]
            assert len(rows) == 2*len(ends)
            for r in rows.itertuples():
                end, last = int(ends.loc[r.unit]), int(lasts.loc[r.unit])
                raw = pred.loc[pred.unit.eq(r.unit)].sort_values('cycle')
                crossing = raw.crossing.iloc[0] if len(raw) else np.nan
                hits = raw.loc[raw.hi.le(.5)]
                if np.isfinite(crossing) and crossing >= 39:
                    assert len(hits) and hits.cycle.min() == crossing
                live = raw.loc[raw.cycle.ge(39) & raw.cycle.ge(crossing) & raw.cycle.lt(end)]
                expected = live.cycle.min() if len(live) else np.nan
                scheduled = expected+r.delay
                np.testing.assert_allclose([r.decision, r.first_available, r.scheduled],
                                           [expected, expected, scheduled], equal_nan=True, atol=1e-9)
                assert r.has_decision == bool(np.isfinite(expected))
                assert r.late == bool(np.isfinite(scheduled) and scheduled > end)
                assert r.exact_endpoint == bool(np.isfinite(scheduled) and scheduled == end)
                assert r.execution_observed == bool(np.isfinite(scheduled) and scheduled < end and scheduled <= last)
                if dataset == 'complete':
                    assert r.utilised == (min(scheduled, end) if np.isfinite(scheduled) else end)
                    assert r.reached_endpoint == bool(not np.isfinite(scheduled) or scheduled >= end)
                else:
                    assert np.isnan(r.utilised) and np.isnan(r.reached_endpoint)
                    if not np.isfinite(expected):
                        assert r.status == 'right_censored'
                checked += 1
    # All inherited P11 summaries must remain equal; verify new-control aggregates directly.
    inherited = summary.loc[summary.method.ne('HI_MARKER')].reset_index(drop=True)
    pd.testing.assert_frame_equal(inherited, pd.read_csv(p.PREVIOUS / 'summary.csv'), check_dtype=False, atol=1e-9, rtol=1e-9)
    for r in summary.loc[summary.method.eq('HI_MARKER')].itertuples():
        g = controls.loc[controls.subset.eq(r.subset) & controls.dataset.eq(r.dataset) & controls.repeat.eq(r.repeat) & controls.policy_id.eq(r.policy_id)]
        assert r.total == len(g) == 100
        assert r.decisions == g.has_decision.sum() and r.late_count == g.late.sum() and r.exact_count == g.exact_endpoint.sum()
        if r.dataset == 'complete':
            np.testing.assert_allclose([r.mean_utilised, r.mean_unused, r.cost_per_cycle],
                                       [g.utilised.mean(), (g.endpoint-g.utilised).mean(), 100/g.utilised.sum()], atol=1e-9)
    rng = np.random.default_rng(20261017)
    all_complete = pd.concat([previous, controls], ignore_index=True)
    all_complete = all_complete.loc[all_complete.dataset.eq('complete')]
    for r in contrasts.itertuples():
        pop = all_complete.loc[all_complete.subset.eq(r.subset) & all_complete.repeat.eq(r.repeat)]
        a = pop.loc[pop.policy_id.eq(r.policy_id)]
        b = pop.loc[pop.policy_id.eq(r.reference)]
        pairs = a.merge(b, on=['unit', 'fold'], suffixes=('_a', '_b')).sort_values('unit')
        assert len(pairs) == r.common == 100
        x, y = pairs.utilised_a.to_numpy(), pairs.utilised_b.to_numpy()
        ix = rng.integers(0, 100, size=(2000, 100))
        delta = (x[ix]-y[ix]).mean(axis=1)
        saving = 1-y[ix].mean(axis=1)/x[ix].mean(axis=1)
        np.testing.assert_allclose([r.delta_mean_life, r.life_ci_low, r.life_ci_high, r.relative_saving, r.saving_ci_low, r.saving_ci_high],
                                   [(x-y).mean(), *np.quantile(delta, [.025, .975]), 1-y.mean()/x.mean(), *np.quantile(saving, [.025, .975])], atol=1e-9)
        both = pairs.has_decision_a & pairs.has_decision_b
        assert r.same_date == (both & pairs.scheduled_a.eq(pairs.scheduled_b)).sum()
        assert r.later_date == (both & pairs.scheduled_a.gt(pairs.scheduled_b)).sum()
        assert r.earlier_date == (both & pairs.scheduled_a.lt(pairs.scheduled_b)).sum()
        assert r.candidate_without_decision == (~pairs.has_decision_a).sum()
        assert r.candidate_reached == pairs.reached_endpoint_a.sum() and r.reference_reached == pairs.reached_endpoint_b.sum()
        if r.reference.startswith('HI_MARKER'):
            assert not r.earlier_date
            assert np.all(x >= y)
    for r in decomp.itertuples():
        pop = all_complete.loc[all_complete.subset.eq(r.subset) & all_complete.repeat.eq(r.repeat)]
        cp = 100/pop.loc[pop.policy_id.eq(r.policy_id), 'utilised'].sum()
        ch = 100/pop.loc[pop.policy_id.eq(f'HI_MARKER_D{r.delay}'), 'utilised'].sum()
        ca = 100/pop.loc[pop.policy_id.eq(f'AGE_D{r.delay}'), 'utilised'].sum()
        np.testing.assert_allclose([r.mean_phm, r.mean_marker, r.mean_age], [1/cp, 1/ch, 1/ca], atol=1e-9)
        np.testing.assert_allclose(r.total_life_gain, r.marker_life_gain+r.prognosis_life_gain, atol=1e-9)
        np.testing.assert_allclose([r.cost_ratio_total, r.cost_ratio_marker, r.cost_ratio_incremental], [cp/ca, ch/ca, cp/ch], atol=1e-9)
        np.testing.assert_allclose(r.cost_ratio_total, r.cost_ratio_marker*r.cost_ratio_incremental, atol=1e-9)
        if r.total_life_gain > 0:
            np.testing.assert_allclose([r.prognosis_share, r.marker_share],
                                       [r.prognosis_life_gain/r.total_life_gain, r.marker_life_gain/r.total_life_gain], atol=1e-9)
    result = dict(status='passed', controls_checked=checked, inherited_summaries_checked=len(inherited),
                  contrasts_checked=len(contrasts), decompositions_checked=len(decomp),
                  previous_artifacts_intact=p.integrity() == metadata['previous_manifests'],
                  verifier_sha256=p.p11.sha(p.ROOT / 'experiments/verify_pilot_landmark_control_11a.py'))
    (out / 'verification.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    p.refresh_manifest()
    print(json.dumps(result))


if __name__ == '__main__':
    main()
