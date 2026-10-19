"""P13.5 chain construction and decision measures; P10/P11/P11.1 procedures unchanged."""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.isotonic import IsotonicRegression

import pilot_f_uncertainty_10 as p10
import pilot_fd001_05 as p05
import pilot_removal_11 as p11
from pilot_landmark_control_11a import marker_action

SENSORS = [f"s{i}" for i in range(1, 22)]
EPS = p11.EPS
ALPHA = .02
RESERVE = 15
STABILITY_RULES = ["ISO_LOWER98_M15_D1", "ISO_LOWER98_M15_D2", "HI_MARKER_D1", "HI_MARKER_D2"]


def rules():
    out = []
    for method in p10.METHODS:
        for anchor in ["point", "lower"]:
            for delay in [1, 2]:
                level = "POINT" if anchor == "point" else "LOWER98"
                out.append(dict(policy_id=f"{method}_{level}_M{RESERVE}_D{delay}", method=method, anchor=anchor,
                                alpha=0. if anchor == "point" else ALPHA, reserve=RESERVE, delay=delay))
    for delay in [1, 2]:
        out.append(dict(policy_id=f"HI_MARKER_D{delay}", method="HI_MARKER", anchor="condition",
                        alpha=0., reserve=0, delay=delay))
    assert len(out) == 10
    return out


def m18_effective(health):
    stats = health["stats"]
    weights = np.zeros(len(SENSORS))
    for sensor, b, d, s in zip(stats["channels"], health["beta"], stats["direction"], stats["scale"]):
        weights[SENSORS.index(sensor)] = b*d/s
    return weights


def weights_health(effective, subset, fit_units, label):
    """HI=clip(1-x.w,0,1) on centred sensors, expressed in the P10 feature interface."""
    return dict(stats=dict(channels=list(SENSORS), direction=np.ones(len(SENSORS)), scale=np.ones(len(SENSORS))),
                beta=np.asarray(effective, dtype=float), config=p10.CONFIG[subset], fit_units=list(fit_units),
                candidate=label)


def fit_converters(health, converter_inputs, subset, seed):
    frame, _ = p10.features(converter_inputs, health)
    data = p10.attach_labels(frame, converter_inputs.groupby("unit").cycle.max())
    weights = p05.equal_engine_weights(data.unit)
    predictors = {}
    for method in p10.METHODS:
        columns = ["hi", "h_slope"] if method == "RF_SLOPE" else ["hi"]
        if method == "ISO":
            model = IsotonicRegression(increasing=True, y_min=0., out_of_bounds="clip")
            model.fit(data.hi.to_numpy(), data.rul.to_numpy(), sample_weight=weights)
        else:
            model = RandomForestRegressor(n_estimators=150, max_depth=12, min_samples_leaf=5,
                                          n_jobs=4, random_state=seed)
            model.fit(data[columns].to_numpy(), data.rul.to_numpy(), sample_weight=weights)
        predictors[method] = dict(model=model, columns=columns, fit_units=sorted(data.unit.unique().tolist()))
    return dict(health=health, predictors=predictors, subset=subset, seed=seed)


def labelled_predictions(bundle, inputs):
    prediction, health = p10.predict_inputs(bundle, inputs)
    end = inputs.groupby("unit").cycle.max()
    prediction = p10.attach_labels(prediction, end)
    prediction["error"] = prediction.predicted_rul-prediction.rul
    return prediction, health, end


def calibrate_and_evaluate(bundle, u_inputs, e_inputs, u_units, e_units):
    u_pred, u_health, u_end = labelled_predictions(bundle, u_inputs)
    u_scores, _ = p10.score_engines(u_pred, u_health, u_inputs, u_end, u_units)
    quantiles = p10.calibrate(u_scores)
    e_pred, e_health, e_end = labelled_predictions(bundle, e_inputs)
    scores, events = p10.score_engines(e_pred, e_health, e_inputs, e_end, e_units)
    primary = quantiles.loc[quantiles.scope.eq("path") & np.isclose(quantiles.alpha, ALPHA)]
    bands = p10.evaluate_bands(e_pred, scores, events, primary)
    return dict(u_pred=u_pred, u_scores=u_scores, quantiles=quantiles, e_pred=e_pred,
                scores=scores, events=events, bands=bands, endpoints=e_end)


def usable_marker(frame, endpoint):
    usable = frame.loc[frame.cycle.ge(39) & frame.in_domain & frame.cycle.lt(endpoint)]
    return float(usable.cycle.min()) if len(usable) else np.nan


def oracle_terms(action, endpoint, delay):
    """P11.2 rho=1 terms: oracle retires at T-1; W_gap=W-1, J flags decisions after the oracle deadline."""
    deadline = endpoint-1-delay
    assert deadline >= 1
    present = bool(np.isfinite(action["decision"]))
    score_time = action["decision"] if present else endpoint
    utilised = min(action["decision"]+delay, endpoint) if present else endpoint
    return dict(oracle_deadline=deadline, W_gap=float(endpoint-utilised-1), J=int(score_time > deadline),
                B=float(max(0., score_time-deadline)))


def decisions(prediction, quantiles, endpoints):
    q = {m: float(quantiles.loc[quantiles.method.eq(m) & quantiles.scope.eq("path") &
                                np.isclose(quantiles.alpha, ALPHA), "q_late"].iloc[0]) for m in p10.METHODS}
    rows = []
    for unit in endpoints.index:
        endpoint = int(endpoints.loc[unit])
        frames = {m: prediction.loc[prediction.unit.eq(unit) & prediction.method.eq(m) & prediction.cycle.lt(endpoint),
                                    ["unit", "cycle", "predicted_rul", "in_domain"]].copy() for m in p10.METHODS}
        marker = usable_marker(frames["ISO"], endpoint)
        for rule in rules():
            q_late = 0.
            if rule["method"] == "HI_MARKER":
                action = marker_action(frames["ISO"], rule["delay"])
            else:
                q_late = q[rule["method"]] if rule["anchor"] == "lower" else 0.
                action = p11.decide(frames[rule["method"]], rule["reserve"], rule["delay"], q_late)
            outcome = p11.assess(action, endpoint, endpoint, True)
            rows.append(dict(unit=int(unit), q_late=q_late, usable_marker=marker, **rule, **outcome,
                             **oracle_terms(action, endpoint, rule["delay"])))
    return pd.DataFrame(rows)


def decision_summary(frame):
    keys = ["subset", "chain", "repeat", "policy_id"]
    rows = []
    for key, g in frame.groupby(keys, sort=True):
        n = len(g)
        rows.append(dict(zip(keys, key)) | dict(
            total=n, decisions=int(g.has_decision.sum()), without_decision=int((~g.has_decision).sum()),
            exact_count=int(g.exact_endpoint.sum()), late_count=int(g.late.sum()),
            reached_count=int(g.reached_endpoint.sum()), mean_utilised=float(g.utilised.mean()),
            mean_unused=float((g.endpoint-g.utilised).mean()), mean_oracle_gap=float(g.W_gap.mean()),
            oracle_deadline_misses=int(g.J.sum()), mean_oracle_delay=float(g.B.mean()),
            passes_strict_screen=bool(g.has_decision.all() and g.late.mean() <= .02+EPS)))
    return pd.DataFrame(rows)


def prognosis_summary(events, bands):
    rows = []
    marks = events.loc[events.event.eq("mark")]
    for key, g in marks.groupby(["subset", "chain", "repeat", "method"], sort=True):
        a = g.loc[g.status.eq("available")]
        e = a.error.to_numpy(dtype=float)
        b = bands.loc[bands.subset.eq(key[0]) & bands.chain.eq(key[1]) & bands.repeat.eq(key[2]) & bands.method.eq(key[3])]
        path, point = b.loc[b.available_path], b.loc[b.available_point]
        rows.append(dict(zip(["subset", "chain", "repeat", "method"], key)) | dict(
            engines=len(g), mark_available=len(a), rmse=float(np.sqrt(np.mean(e**2))) if len(e) else np.nan,
            bias=float(np.mean(e)) if len(e) else np.nan, actual_lead_median=float(a.actual_rul.median()),
            path_lower_coverage=float(path.path_lower_coverage.mean()), q_late_median=float(b.q_late.median()),
            q_late_max=float(b.q_late.max()), calibration_n_min=int(b.calibration_n.min()),
            conservative_lead_median=float(point.conservative_lead.median()),
            collapsed_point_fraction=float(point.collapsed_point.mean())))
    return pd.DataFrame(rows)


def between_repeat_ranges(frame):
    """Per engine and chain: max-min over the three repeats; any missing value leaves the range undefined."""
    rows = []
    quantities = [("usable_marker", "ISO_LOWER98_M15_D1", "usable_marker")]
    quantities += [(rule, rule, "decision") for rule in STABILITY_RULES]
    for name, rule, column in quantities:
        data = frame.loc[frame.policy_id.eq(rule)]
        for (subset, chain, unit), g in data.groupby(["subset", "chain", "unit"], sort=True):
            values = g.sort_values("repeat")[column].to_numpy(dtype=float)
            assert len(values) == 3
            complete = bool(np.isfinite(values).all())
            rows.append(dict(subset=subset, chain=chain, unit=int(unit), quantity=name, repeats=len(values),
                             missing_repeats=int((~np.isfinite(values)).sum()),
                             range=float(values.max()-values.min()) if complete else np.nan))
    return pd.DataFrame(rows)


def range_summary(ranges, seed):
    rng = np.random.default_rng(seed)
    rows = []
    for (subset, quantity), g in ranges.groupby(["subset", "quantity"], sort=True):
        wide = g.pivot(index="unit", columns="chain", values="range")
        missing = g.pivot(index="unit", columns="chain", values="missing_repeats")
        row = dict(subset=subset, quantity=quantity, engines=len(wide))
        for chain in ["M18", "SEL"]:
            r = wide[chain].dropna()
            row.update({f"{chain}_defined": len(r), f"{chain}_undefined": int(wide[chain].isna().sum()),
                        f"{chain}_missing_values": int(missing[chain].sum()),
                        f"{chain}_median": float(r.median()), f"{chain}_p95": float(r.quantile(.95)),
                        f"{chain}_max": float(r.max()), f"{chain}_over10": int((r > 10).sum())})
        pair = wide.dropna()
        a, b = pair.M18.to_numpy(), pair.SEL.to_numpy()
        idx = rng.integers(0, len(pair), size=(2000, len(pair)))
        mean_delta = (b[idx]-a[idx]).mean(axis=1)
        p95_delta = np.quantile(b[idx], .95, axis=1)-np.quantile(a[idx], .95, axis=1)
        row.update(common=len(pair), delta_mean=float(np.mean(b-a)),
                   delta_mean_ci_low=float(np.quantile(mean_delta, .025)), delta_mean_ci_high=float(np.quantile(mean_delta, .975)),
                   delta_p95=float(np.quantile(b, .95)-np.quantile(a, .95)),
                   delta_p95_ci_low=float(np.quantile(p95_delta, .025)), delta_p95_ci_high=float(np.quantile(p95_delta, .975)),
                   engines_improved=int((b < a-EPS).sum()), engines_worsened=int((b > a+EPS).sum()))
        rows.append(row)
    return pd.DataFrame(rows)


def paired_contrasts(frame, events, seed):
    rng = np.random.default_rng(seed)
    rows = []
    for (subset, repeat, policy), g in frame.groupby(["subset", "repeat", "policy_id"], sort=True):
        pair = g.pivot(index="unit", columns="chain", values="utilised").dropna()
        assert len(pair) == 100
        a, b = pair.M18.to_numpy(), pair.SEL.to_numpy()
        idx = rng.integers(0, len(pair), size=(2000, len(pair)))
        delta = (b[idx]-a[idx]).mean(axis=1)
        rows.append(dict(subset=subset, repeat=repeat, measure="mean_utilised", key=policy, common=len(pair),
                         delta=float(np.mean(b-a)), ci_low=float(np.quantile(delta, .025)),
                         ci_high=float(np.quantile(delta, .975)), changed_engines=int((abs(b-a) > EPS).sum())))
    marks = events.loc[events.event.eq("mark") & events.status.eq("available")]
    for (subset, repeat, method), g in marks.groupby(["subset", "repeat", "method"], sort=True):
        pair = g.pivot(index="unit", columns="chain", values="error").dropna()
        a, b = pair.M18.to_numpy(), pair.SEL.to_numpy()
        idx = rng.integers(0, len(pair), size=(2000, len(pair)))
        delta = np.sqrt(np.mean(b[idx]**2, axis=1))-np.sqrt(np.mean(a[idx]**2, axis=1))
        rows.append(dict(subset=subset, repeat=repeat, measure="mark_rmse", key=method, common=len(pair),
                         delta=float(np.sqrt(np.mean(b**2))-np.sqrt(np.mean(a**2))), ci_low=float(np.quantile(delta, .025)),
                         ci_high=float(np.quantile(delta, .975)), changed_engines=int((abs(b-a) > EPS).sum())))
    return pd.DataFrame(rows)


def chain_differences(frame, flags):
    """Engine-level |SEL-M18| differences within the same partition, with P13.4 tail flags."""
    keys = ["subset", "repeat", "fold", "unit", "policy_id"]
    wide = frame.pivot(index=keys, columns="chain", values=["decision", "usable_marker"])
    out = pd.DataFrame(index=wide.index).reset_index()
    for column in ["decision", "usable_marker"]:
        a, b = wide[(column, "M18")].to_numpy(dtype=float), wide[(column, "SEL")].to_numpy(dtype=float)
        out[f"abs_delta_{column}"] = np.abs(b-a)
        out[f"presence_discordant_{column}"] = np.isfinite(a) != np.isfinite(b)
    return out.merge(flags, on=["subset", "repeat", "fold"], how="left", validate="many_to_one")


def tail_summary(differences):
    rows = []
    for (subset, policy, flag), g in differences.groupby(["subset", "policy_id", "max_tail_worsened"], sort=True):
        d, m = g.abs_delta_decision.dropna(), g.abs_delta_usable_marker.dropna()
        rows.append(dict(subset=subset, policy_id=policy, internal_tail_worsened=bool(flag), engines=len(g),
                         partitions=g[["repeat", "fold"]].drop_duplicates().shape[0],
                         decision_finite=len(d), decision_discordant=int(g.presence_discordant_decision.sum()),
                         decision_median=float(d.median()), decision_p95=float(d.quantile(.95)), decision_max=float(d.max()),
                         marker_finite=len(m), marker_discordant=int(g.presence_discordant_usable_marker.sum()),
                         marker_p95=float(m.quantile(.95)), marker_max=float(m.max())))
    return pd.DataFrame(rows)
