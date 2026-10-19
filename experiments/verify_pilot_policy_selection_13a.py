"""Reconstruct selections and actions independently; check learned HI and bootstrap."""
import json
import joblib
import numpy as np
import pandas as pd
from threadpoolctl import threadpool_limits
import pilot_policy_selection_13a as p


def verify_actions(rows, health, ends):
    for r in rows.itertuples():
        g = health.loc[health.unit.eq(r.unit) & health.cycle.lt(ends.loc[r.unit])].sort_values('cycle')
        family = r.family if hasattr(r, 'family') else ('threshold' if 'THRESHOLD' in r.policy_id else 'wait')
        value = r.value if hasattr(r, 'value') else r.selected_value
        hits = g.loc[g.hi.le(value if family == 'threshold' else .5), 'cycle']
        t = max(39, int(hits.min()))+(int(value) if family == 'wait' else 0) if len(hits) else np.nan
        if not len(g) or t > g.cycle.max():
            t = np.nan
        rem = t+r.delay
        end = ends.loc[r.unit]
        np.testing.assert_allclose([r.decision, r.scheduled, r.utilised],
                                   [t, rem, min(rem, end) if np.isfinite(rem) else end], equal_nan=True)
        assert r.has_decision == bool(np.isfinite(t))
        assert r.reached_endpoint == bool(not np.isfinite(rem) or rem >= end)
        assert r.late == bool(np.isfinite(rem) and rem > end)
        assert r.exact_endpoint == bool(np.isfinite(rem) and rem == end)


def main():
    out = p.OUT
    meta = json.loads((out/'metadata.json').read_text())
    assert p.integrity() == meta['previous_manifests']
    for name, digest in meta['inputs'].items():
        source = out/'verifier_original.py' if name.replace('\\', '/') == 'experiments/verify_pilot_policy_selection_13a.py' else p.ROOT/name
        assert p.p11.sha(source) == digest, name
    for name, digest in json.loads((out/'manifest.json').read_text()).items():
        assert p.p11.sha(out/name) == digest, name
    inner = pd.read_csv(out/'internal_decisions.csv')
    metrics = pd.read_csv(out/'internal_metrics.csv')
    selections = pd.read_csv(out/'selections.csv')
    decisions = pd.read_csv(out/'decisions.csv')
    assert [len(x) for x in [inner, metrics, selections, decisions]] == [57600, 1440, 240, 9600]
    freezes = json.loads((out/'selection_freezes.json').read_text())
    start = json.loads((out/'evaluation_start.json').read_text())
    assert len(freezes) == 60 and all(f['timestamp_utc'] <= start['timestamp_utc'] for f in freezes)
    assert start['selections_sha256'] == p.p11.sha(out/'selections.csv')
    raw = {s: p.p10.read_inputs('train', s) for s in ['FD001', 'FD003']}
    for split in json.loads((p.SOURCE/'splits.json').read_text()):
        s, rep, fold = split['subset'], split['repeat'], split['fold']
        tag = f'{s}_r{rep}_f{fold}'
        ends = raw[s].groupby('unit').cycle.max()
        h = pd.read_csv(out/f'inner_health_{tag}.csv.gz')
        for part in p.inner_partitions(split):
            assert not set(part['fit']+part['validation']) & set(split['uncertainty']+split['evaluation'])
            model = joblib.load(out/f'inner_hi_{tag}_v{part["inner_fold"]}.joblib')
            refit = p.p10.fit_health(raw[s].loc[raw[s].unit.isin(part['fit'])].reset_index(drop=True), s)
            np.testing.assert_allclose(model['beta'], refit['beta'], atol=1e-10)
            v = raw[s].loc[raw[s].unit.isin(part['validation'])].reset_index(drop=True)
            expected = p.health_values(v, refit).reset_index(drop=True)
            actual = h.loc[h.inner_fold.eq(part['inner_fold']), ['unit', 'cycle', 'hi']].reset_index(drop=True)
            pd.testing.assert_frame_equal(actual, expected, check_dtype=False, atol=1e-10, rtol=1e-10)
        mask = lambda df: df.subset.eq(s) & df.repeat.eq(rep) & df.fold.eq(fold)
        local = inner.loc[mask(inner)]
        verify_actions(local, h, ends)
        m = metrics.loc[mask(metrics)]
        for r in m.itertuples():
            g = local.loc[local.family.eq(r.family) & local.value.eq(r.value) & local.delay.eq(r.delay)]
            assert r.events == g.reached_endpoint.sum() and r.decisions == g.has_decision.sum()
            np.testing.assert_allclose([r.mean_utilised, r.cost_per_cycle], [g.utilised.mean(), 40/g.utilised.sum()])
        for r in selections.loc[mask(selections)].itertuples():
            candidates = m.loc[m.family.eq(r.family) & m.delay.eq(r.delay)]
            good = candidates.loc[candidates.events.eq(0) & candidates.decisions.eq(40)]
            pool = good if len(good) else candidates
            rank = lambda x: ((-x.mean_utilised, -x.value if r.family == 'threshold' else x.value)
                              if len(good) else (x.events, -x.mean_utilised, -x.value if r.family == 'threshold' else x.value))
            best = sorted(pool.itertuples(), key=rank)[0]
            assert r.selection_feasible == bool(len(good)) and r.selected_value == best.value
        freeze = next(f for f in freezes if f['subset'] == s and f['repeat'] == rep and f['fold'] == fold)
        assert freeze['metrics_sha256'] == p.p11.sha(out/f'internal_metrics_{tag}.csv')
        outer = pd.read_csv(out/f'outer_health_{tag}.csv.gz')
        model = joblib.load(p.SOURCE/f'models_{tag}.joblib')['health']
        expected = p.health_values(raw[s].loc[raw[s].unit.isin(split['evaluation'])].reset_index(drop=True), model)
        pd.testing.assert_frame_equal(outer, expected.reset_index(drop=True), check_dtype=False, atol=1e-10, rtol=1e-10)
        verify_actions(decisions.loc[mask(decisions) & decisions.phase.eq('selected')], outer, ends)
    # Inherited reference rows retain every original value except the phase label.
    original = pd.concat([pd.read_csv(p.p11.OUT/'decisions.csv'), pd.read_csv(p.p11a.OUT/'controls.csv')], ignore_index=True)
    refs = decisions.loc[decisions.phase.eq('reference')]
    keys = ['subset', 'repeat', 'fold', 'unit', 'dataset', 'policy_id']
    inherited = original.merge(refs[keys], on=keys).sort_values(keys).reset_index(drop=True)
    columns = [c for c in inherited.columns if c != 'phase']
    pd.testing.assert_frame_equal(inherited[columns], refs.sort_values(keys).reset_index(drop=True)[columns], check_dtype=False, atol=1e-9, rtol=1e-9)
    summary = pd.read_csv(out/'summary.csv')
    assert len(summary) == 96
    for r in summary.itertuples():
        g = decisions.loc[decisions.subset.eq(r.subset) & decisions.repeat.eq(r.repeat) & decisions.policy_id.eq(r.policy_id)]
        assert len(g) == r.total == 100
        assert r.decisions == g.has_decision.sum() and r.late_count == g.late.sum() and r.exact_count == g.exact_endpoint.sum()
        np.testing.assert_allclose([r.mean_utilised, r.cost_per_cycle], [g.utilised.mean(), 100/g.utilised.sum()])
    contrasts = pd.read_csv(out/'contrasts.csv')
    assert len(contrasts) == 48
    rng = np.random.default_rng(p.SEED)
    for r in contrasts.itertuples():
        pop = decisions.loc[decisions.subset.eq(r.subset) & decisions.repeat.eq(r.repeat)]
        pair = pop.loc[pop.policy_id.eq(r.policy_id)].merge(pop.loc[pop.policy_id.eq(r.reference)], on=['unit', 'fold'], suffixes=('_a', '_b')).sort_values('unit')
        x, y = pair.utilised_a.to_numpy(), pair.utilised_b.to_numpy()
        ix = rng.integers(0, 100, (2000, 100))
        np.testing.assert_allclose([r.delta_mean_life, r.life_ci_low, r.life_ci_high, r.relative_saving, r.saving_ci_low, r.saving_ci_high],
                                   [(x-y).mean(), *np.quantile((x[ix]-y[ix]).mean(axis=1), [.025, .975]), 1-y.mean()/x.mean(), *np.quantile(1-y[ix].mean(axis=1)/x[ix].mean(axis=1), [.025, .975])], atol=1e-9)
    result = dict(status='passed', internal_fits_checked=240, internal_decisions_checked=len(inner), external_selected_checked=2400,
                  inherited_references_checked=len(refs), summaries_checked=96, contrasts_checked=48,
                  verifier_sha256=p.p11.sha(p.ROOT/'experiments/verify_pilot_policy_selection_13a.py'),
                  amendment='CSV index reset only; original verifier and initial log archived; experiment unchanged')
    (out/'verification.json').write_text(json.dumps(result, indent=2))
    p.refresh_manifest()
    print(json.dumps(result))


if __name__ == '__main__':
    with threadpool_limits(limits=1):
        main()
