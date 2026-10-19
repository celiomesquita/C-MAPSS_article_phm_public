"""P11.2: information-constrained oracles and paired loss decomposition."""
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import pandas as pd
import pilot_policy_selection_13a as p13
import pilot_removal_11 as p11

ROOT = p11.ROOT
SOURCE = p13.OUT
OUT = ROOT/'experiments/artifacts/pilot_loss_decomposition_11b'
RHOS = [1, 12, 15]
SEED = 20261017


def integrity():
    result = {}
    for folder in sorted((ROOT/'experiments/artifacts').glob('pilot_*')):
        f = folder/'manifest.json'
        if folder == OUT or not f.exists():
            continue
        for name, digest in json.loads(f.read_text(encoding='utf-8')).items():
            assert p11.sha(folder/name) == digest, (folder.name, name)
        result[folder.name] = p11.sha(f)
    return result


def information(health, end):
    hits = health.loc[health.cycle.ge(20) & health.cycle.lt(end) & health.hi.le(.5), 'cycle']
    G = float(hits.min()) if len(hits) else np.nan
    A = max(39., G) if np.isfinite(G) else np.nan
    if A >= end:
        A = np.nan
    return G, A


def oracle(end, deadline, access):
    value = max(deadline, access) if np.isfinite(access) else np.nan
    return float(value) if np.isfinite(value) and value < end else np.nan


def outcomes(tau, end, delay, deadline):
    present = bool(np.isfinite(tau))
    scheduled = tau+delay if present else np.nan
    score_time = tau if present else end
    N = float(min(scheduled, end) if present else end)
    return dict(decision=tau, scheduled=scheduled, J=int(score_time > deadline), B=max(0., score_time-deadline),
                N=N, W=end-N, late=int(present and scheduled > end), exact=int(present and scheduled == end),
                missing=int(not present), reached=int(not present or scheduled >= end))


def decompose(row, G, A, rho):
    end, delay = int(row['endpoint']), int(row['delay'])
    deadline = end-rho-delay
    assert deadline >= 1, 'Initial-life constraint requires separate reporting before analysis'
    ts = {'O': oracle(end, deadline, 1.), 'G': oracle(end, deadline, G),
          'A': oracle(end, deadline, A), 'real': row['decision']}
    out = dict(G=G, A=A, deadline=deadline, rho=rho, feasible_access=bool(np.isfinite(A) and A <= deadline),
               information_matched=bool(row['method'] != 'AGE' and
                   (not np.isfinite(ts['real']) or (np.isfinite(A) and ts['real'] >= A))))
    for name, tau in ts.items():
        out.update({f'{name}_{k}': v for k, v in outcomes(tau, end, delay, deadline).items()})
    for metric in ['J', 'B', 'W']:
        out.update({f'{metric}_total': out[f'real_{metric}']-out[f'O_{metric}'],
                    f'{metric}_det': out[f'A_{metric}']-out[f'O_{metric}'],
                    f'{metric}_post': out[f'real_{metric}']-out[f'A_{metric}'],
                    f'{metric}_crossing': out[f'G_{metric}']-out[f'O_{metric}'],
                    f'{metric}_warmup': out[f'A_{metric}']-out[f'G_{metric}']})
    return out


def replay(rows, health, prediction):
    for r in rows.itertuples():
        g = health.loc[health.unit.eq(r.unit) & health.cycle.lt(r.endpoint)]
        if r.method == 'AGE':
            tau = r.control_age-r.delay
            expected = tau if tau >= 1 and tau < r.endpoint else np.nan
        elif r.method in ['HI_THRESHOLD_SELECTED', 'HI_WAIT_SELECTED', 'HI_MARKER']:
            family = 'wait' if r.method == 'HI_WAIT_SELECTED' else 'threshold'
            value = r.selected_value if r.method != 'HI_MARKER' else .5
            expected = p13.condition_action(g, family, value, r.delay)['decision']
        else:
            frame = prediction.loc[prediction.unit.eq(r.unit) & prediction.method.eq(r.method) & prediction.cycle.lt(r.endpoint)]
            expected = p11.decide(frame, r.reserve, r.delay, r.q_late)['decision']
        np.testing.assert_allclose([r.decision, r.scheduled], [expected, expected+r.delay], equal_nan=True, atol=0., rtol=0.)


def summaries(components, indices):
    result = []
    keys = ['subset', 'repeat', 'policy_id', 'rho']
    for key, frame in components.groupby(keys, sort=True):
        g = frame.sort_values('unit')
        assert len(g) == 100 and g.unit.is_unique
        ix = indices[f'{key[0]}_r{key[1]}']
        for scope in ['all', 'feasible_access']:
            mask = np.ones(100, dtype=bool) if scope == 'all' else g.feasible_access.to_numpy()
            n = int(mask.sum())
            row = dict(zip(keys, key)) | dict(scope=scope, total=n, excluded=100-n,
                      delay=int(g.delay.iloc[0]), information_matched=int(g.loc[mask, 'information_matched'].sum()))
            if n == 0:
                result.append(row)
                continue
            bm = mask[ix]
            bn = bm.sum(axis=1)
            def boot(values):
                return np.divide((np.asarray(values)[ix]*bm).sum(axis=1), bn,
                                 out=np.full(len(ix), np.nan), where=bn > 0)
            def save(name, values):
                values = np.asarray(values, dtype=float)
                row[name] = float(values[mask].mean())
                row[name+'_lo'], row[name+'_hi'] = np.nanquantile(boot(values), [.025, .975])
            for name in ['O', 'G', 'A', 'real']:
                for metric in ['J', 'B', 'N', 'W']:
                    save(f'{name}_{metric}', g[f'{name}_{metric}'])
                for metric in ['late', 'exact', 'missing', 'reached']:
                    row[f'{name}_{metric}_count'] = int(g.loc[mask, f'{name}_{metric}'].sum())
                row[f'{name}_cost'] = n/g.loc[mask, f'{name}_N'].sum()
            for metric in ['J', 'B', 'W']:
                for part in ['total', 'det', 'post', 'crossing', 'warmup']:
                    save(f'{metric}_{part}', g[f'{metric}_{part}'])
            costs = {x: 1/boot(g[f'{x}_N']) for x in ['O', 'A', 'real']}
            for part, left, right in [('total', 'real', 'O'), ('det', 'A', 'O'), ('post', 'real', 'A')]:
                point = row[f'{left}_cost']-row[f'{right}_cost']
                dist = costs[left]-costs[right]
                row['cost_'+part] = point
                row['cost_'+part+'_lo'], row['cost_'+part+'_hi'] = np.nanquantile(dist, [.025, .975])
                row['relative_cost_'+part] = point/row['O_cost']
                row['relative_cost_'+part+'_lo'], row['relative_cost_'+part+'_hi'] = np.nanquantile(dist/costs['O'], [.025, .975])
            for metric in ['J', 'B']:
                total = boot(g[f'{metric}_total'])
                det = boot(g[f'{metric}_det'])
                positive = total > 0
                row[f'{metric}_share_undefined_bootstrap'] = int((~positive).sum())
                row[f'{metric}_det_share'] = row[f'{metric}_det']/row[f'{metric}_total'] if row[f'{metric}_total'] > 0 else np.nan
                ci = np.quantile(det[positive]/total[positive], [.025, .975]) if positive.any() else [np.nan, np.nan]
                row[f'{metric}_det_share_lo'], row[f'{metric}_det_share_hi'] = ci
            result.append(row)
    return pd.DataFrame(result)


def refresh_manifest():
    (OUT/'manifest.json').write_text(json.dumps({f.name:p11.sha(f) for f in sorted(OUT.iterdir())
                                                if f.is_file() and f.name != 'manifest.json'}, indent=2), encoding='utf-8')


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert not (OUT/'metadata.json').exists(), 'Preserve completed experiment'
    prior = integrity()
    files = [Path(__file__), ROOT/'experiments/test_pilot_loss_decomposition_11b.py',
             ROOT/'experiments/verify_pilot_loss_decomposition_11b.py', ROOT/'experiments/protocolo_decomposicao_perda_11b.md',
             SOURCE/'decisions.csv', SOURCE/'selections.csv', SOURCE/'manifest.json', SOURCE/'verification.json',
             p13.SOURCE/'splits.json', ROOT/'experiments/pilot_removal_11.py', ROOT/'experiments/pilot_policy_selection_13a.py']
    files += sorted(SOURCE.glob('outer_health_*.csv.gz'))+sorted(p13.SOURCE.glob('predictions_*_complete.csv.gz'))
    files += [ROOT/f'CMAPSSData/train_{s}.txt' for s in ['FD001', 'FD003']]
    meta = dict(started_utc=datetime.now(timezone.utc).isoformat(), previous_manifests=prior,
                inputs={str(f.relative_to(ROOT)):p11.sha(f) for f in files}, python=platform.python_version(),
                numpy=np.__version__, pandas=pd.__version__, rhos=RHOS, bootstrap_seed=SEED)
    (OUT/'execution_start.json').write_text(json.dumps(meta, indent=2), encoding='utf-8')
    decisions = pd.read_csv(SOURCE/'decisions.csv')
    avail, all_rows, diagnostic = [], [], []
    oracles = {}
    for split in json.loads((p13.SOURCE/'splits.json').read_text(encoding='utf-8')):
        subset, rep, fold = split['subset'], split['repeat'], split['fold']
        tag = f'{subset}_r{rep}_f{fold}'
        health = pd.read_csv(SOURCE/f'outer_health_{tag}.csv.gz')
        pred = pd.read_csv(p13.SOURCE/f'predictions_{tag}_complete.csv.gz')
        rows = decisions.loc[decisions.subset.eq(subset) & decisions.repeat.eq(rep) & decisions.fold.eq(fold)]
        replay(rows, health, pred)
        for unit, group in rows.groupby('unit', sort=True):
            end = int(group.endpoint.iloc[0])
            G, A = information(health.loc[health.unit.eq(unit)], end)
            common = dict(subset=subset, repeat=rep, fold=fold, unit=unit, endpoint=end)
            avail.append(common | dict(G=G, A=A, warmup=A-G, crossing_lead=end-G, available_lead=end-A))
            for row in group.to_dict('records'):
                for rho in RHOS:
                    comp = decompose(row, G, A, rho)
                    all_rows.append(row | comp)
                    for name in ['O', 'G', 'A']:
                        k = (subset, rep, unit, row['delay'], rho, name)
                        oracles[k] = common | dict(delay=row['delay'], rho=rho, oracle=name, G=G, A=A,
                                                   deadline=comp['deadline']) | {x.removeprefix(name+'_'):v for x,v in comp.items() if x.startswith(name+'_')}
                for method in ['ISO', 'RF_SLOPE']:
                    t = row['decision'] if row['has_decision'] else end-1
                    candidates = pred.loc[pred.unit.eq(unit) & pred.method.eq(method) & pred.cycle.eq(t)]
                    q = candidates.iloc[0] if len(candidates) else None
                    diagnostic.append(common | dict(policy_id=row['policy_id'], forecast_method=method,
                        snapshot=t, snapshot_kind='decision' if row['has_decision'] else 'last_before_endpoint',
                        available=q is not None, hi=q.hi if q is not None else np.nan,
                        h_slope=q.h_slope if q is not None else np.nan,
                        predicted_rul=q.predicted_rul if q is not None else np.nan,
                        actual_rul=end-t, error=q.predicted_rul-(end-t) if q is not None else np.nan,
                        policy_q=row['q_late'], policy_reserve=row['reserve'], policy_anchor=row['anchor']))
        print(tag, 'replayed and decomposed', flush=True)
    components = pd.DataFrame(all_rows)
    rng = np.random.default_rng(SEED)
    indices = {f'{s}_r{rep}':rng.integers(0,100,(2000,100)) for s in ['FD001','FD003'] for rep in [1,2,3]}
    np.savez_compressed(OUT/'bootstrap_indices.npz', **indices)
    tables = dict(availability=pd.DataFrame(avail), replayed_decisions=decisions,
                  oracles=pd.DataFrame(oracles.values()), components=components,
                  diagnostics=pd.DataFrame(diagnostic), summary=summaries(components, indices))
    for name, table in tables.items():
        table.to_csv(OUT/f'{name}.csv', index=False)
    assert integrity() == prior
    meta.update(finished_utc=datetime.now(timezone.utc).isoformat(), counts={k:len(v) for k,v in tables.items()},
                previous_artifacts_intact=True, no_new_fitting=True, no_inspection=True, no_calendar_projection=True)
    (OUT/'metadata.json').write_text(json.dumps(meta, indent=2), encoding='utf-8')
    refresh_manifest()


if __name__ == '__main__':
    main()
