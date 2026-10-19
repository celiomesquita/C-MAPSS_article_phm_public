"""P05: empirical HI and a terminal-AAKR adaptation, with independent RUL labels."""

import hashlib
import importlib.metadata
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import lsq_linear
from scipy.spatial.distance import cdist
from sklearn.isotonic import IsotonicRegression
from threadpoolctl import threadpool_limits

from pilot_fd001 import ROOT, SEED, SENSORS, read_data
from pilot_fd001_04 import QUANTILES, centred_sensors, fit_reference, transform_hi

OUT = ROOT / "experiments/artifacts/pilot_fd001_05"
FAMILIES = ["MARGEM", "EMPIRICO", "AAKR"]


def read_official_inputs():
    names = ["unit", "cycle", "op1", "op2", "op3"]+SENSORS
    data = pd.read_csv(ROOT / "CMAPSSData/test_FD001.txt", sep=r"\s+", header=None, names=names)
    data[["unit", "cycle"]] = data[["unit", "cycle"]].astype(int)
    return data


def attach_official_labels(data, labels):
    """Labels describe the last observation of each test engine, not training engines."""
    ids = sorted(data.unit.unique())
    labels = np.asarray(labels).reshape(-1)
    if ids != list(range(1, len(ids)+1)) or len(labels) != len(ids):
        raise ValueError("Official RUL vector does not align with test units")
    if not np.isfinite(labels).all() or (labels < 0).any():
        raise ValueError("Invalid official RUL labels")
    last = data.groupby("unit").cycle.max()
    endpoints = last+pd.Series(labels, index=ids)
    out = data.copy()
    out["end"] = out.unit.map(endpoints)
    out["rul"] = out.end-out.cycle
    return out


def fitting_stats(data, fit_ids, centred):
    initial = data.unit.isin(fit_ids) & data.cycle.between(15, 20)
    terminal = data.unit.isin(fit_ids) & (data.cycle == data.end)
    direction = np.sign(centred.loc[terminal].median())
    eligible = (centred.loc[initial].std() > 1e-6) & (direction != 0)
    channels = direction.index[eligible].tolist()
    mask = data.unit.isin(fit_ids) & (data.cycle >= 20)
    scale = centred.loc[mask, channels].std()
    channels = scale.index[scale > 1e-6].tolist()
    return {"channels": channels, "direction": direction.loc[channels].to_numpy(),
            "scale": scale.loc[channels].to_numpy()}


def standardise(centred, stats):
    return centred[stats["channels"]].to_numpy()*stats["direction"]/stats["scale"]


def equal_engine_weights(units):
    units = pd.Series(np.asarray(units))
    weights = 1/units.map(units.value_counts()).to_numpy()
    return weights/weights.sum()


def curve_quality(data, hi, ids):
    """Diagnostics on complete trajectories; interpolation is evaluation only."""
    curves, monotonicities, starts, ends = [], [], [], []
    for unit in ids:
        mask = (data.unit == unit) & (data.cycle >= 20)
        h = np.asarray(hi)[mask]
        delta = np.diff(h)
        monotonicities.append(abs(np.sum(delta > 1e-12)-np.sum(delta < -1e-12))/len(delta))
        curves.append(np.interp(np.linspace(0, 1, 100), np.linspace(0, 1, len(h)), h))
        starts.append(h[0])
        ends.append(h[-1])
    with np.errstate(invalid="ignore", divide="ignore"):
        correlations = np.corrcoef(curves)
    correlations = correlations[np.triu_indices(len(curves), 1)]
    # A constant trajectory is uninformative; it must not score perfect trendability.
    correlations = np.nan_to_num(np.abs(correlations), nan=0.)
    span = np.mean(np.abs(np.asarray(starts)-ends))
    return {"monotonicity": float(np.mean(monotonicities)),
            "trendability": float(np.min(correlations)) if len(correlations) else np.nan,
            "prognosability": float(np.exp(-np.std(ends)/span)) if span > 1e-12 else 0.}


def rank_channels(data, z, ids):
    quality = [curve_quality(data, z[:, j], ids) for j in range(z.shape[1])]
    score = [np.mean(list(q.values())) for q in quality]
    return np.argsort(-np.asarray(score), kind="stable"), quality


def reconstruct(query, bank, bandwidth, spread):
    """Gaussian AAKR with stable weights at arbitrarily large finite distances."""
    result = np.empty_like(query, dtype=float)
    for start in range(0, len(query), 512):
        chunk = query[start:start+512]
        distances = cdist(chunk/spread, bank/spread, metric="sqeuclidean")
        log_weights = -distances/(2*bandwidth**2)
        weights = np.exp(log_weights-log_weights.max(axis=1, keepdims=True))
        result[start:start+len(chunk)] = (weights@bank)/weights.sum(axis=1, keepdims=True)
    return result


def fit_aakr(data, z, fit_ids, columns, length, bandwidth):
    terminal = data.unit.isin(fit_ids) & (data.cycle > data.end-length)
    bank = z[np.asarray(terminal)][:, columns]
    units = data.loc[terminal, "unit"].to_numpy()
    spread = np.std(bank, axis=0, ddof=1)
    if (spread <= 1e-6).any():
        raise ValueError("Degenerate terminal-bank dispersion")
    terminal_residuals = []
    for unit in fit_ids:
        own_endpoint = (data.unit == unit) & (data.cycle == data.end)
        query = z[np.asarray(own_endpoint)][:, columns]
        other = units != unit
        # Both the reconstruction bank and its metric exclude the query engine.
        other_spread = np.std(bank[other], axis=0, ddof=1)
        estimate = reconstruct(query, bank[other], bandwidth, other_spread)
        terminal_residuals.append(float(np.linalg.norm(query-estimate)))
    terminal_anchor = float(np.median(terminal_residuals))
    initial = np.zeros((1, len(columns)))
    healthy_anchor = float(np.linalg.norm(initial-reconstruct(initial, bank, bandwidth, spread)))
    if healthy_anchor <= terminal_anchor+1e-9:
        raise ValueError("Healthy and terminal reference anchors overlap")
    return {"columns": np.asarray(columns), "bank": bank, "bank_units": units,
            "spread": spread, "bandwidth": bandwidth,
            "terminal_anchor": terminal_anchor, "healthy_anchor": healthy_anchor,
            "loo_terminal_residuals": np.asarray(terminal_residuals)}


def aakr_hi(z, model):
    query = z[:, model["columns"]]
    raw = np.linalg.norm(query-reconstruct(query, model["bank"], model["bandwidth"], model["spread"]), axis=1)
    return np.clip((raw-model["terminal_anchor"])/(model["healthy_anchor"]-model["terminal_anchor"]), 0, 1)


def fit_empirical(data, z, fit_ids, tau, gamma, ridge):
    mask = data.unit.isin(fit_ids) & (data.cycle >= 20)
    x = z[np.asarray(mask)]
    target = 1-np.minimum(1., data.loc[mask, "rul"].to_numpy()/tau)**gamma
    weights = np.sqrt(equal_engine_weights(data.loc[mask, "unit"]))
    design = np.vstack([x*weights[:, None], np.sqrt(ridge)*np.eye(x.shape[1])])
    response = np.r_[target*weights, np.zeros(x.shape[1])]
    solved = lsq_linear(design, response, bounds=(0, np.inf), method="bvls", tol=1e-10)
    if not solved.success:
        raise RuntimeError(solved.message)
    return solved.x


def empirical_hi(z, coefficients):
    return np.clip(1-np.maximum(0, z@coefficients), 0, 1)


def cut_rmse(data, predictions, ids):
    errors = []
    for unit in ids:
        g = data.loc[data.unit == unit]
        endpoint = g.end.iloc[0]
        cuts = [int(np.floor(f*endpoint)) for f in [.5, .7, .9]]
        mask = (data.unit == unit) & data.cycle.isin(cuts)
        errors.extend((np.asarray(predictions)[mask]-data.loc[mask, "rul"].to_numpy())**2)
    return float(np.sqrt(np.mean(errors)))


def candidate_specs(ranking):
    specs = [("MARGEM", f"q{q:g}", {"quantile": q}) for q in QUANTILES]
    for tau, gamma, ridge in itertools.product([60, 100, 140], [1, 2], [0., .1]):
        specs.append(("EMPIRICO", f"t{tau}_g{gamma}_r{ridge:g}",
                      {"tau": tau, "gamma": gamma, "ridge": ridge}))
    subsets = {"all": tuple(range(len(ranking))), "top5": tuple(sorted(ranking[:5])),
               "top10": tuple(sorted(ranking[:10]))}
    seen = set()
    for label, columns in subsets.items():
        if columns in seen:
            continue
        seen.add(columns)
        for length, bandwidth in itertools.product([5, 10], [.5, 2., 8.]):
            specs.append(("AAKR", f"{label}_L{length}_h{bandwidth:g}",
                          {"columns": [int(j) for j in columns], "length": length, "bandwidth": bandwidth}))
    return specs


def predict_hi(data, centred, z, family, model):
    valid = data.cycle >= 20
    hi = np.full(len(data), np.nan)
    if family == "MARGEM":
        return transform_hi(data, model, 2, centred)[0].to_numpy()
    if family == "EMPIRICO":
        hi[np.asarray(valid)] = empirical_hi(z[np.asarray(valid)], model)
    else:
        hi[np.asarray(valid)] = aakr_hi(z[np.asarray(valid)], model)
    return hi


def run_partition(data, partition, run_name):
    centred = centred_sensors(data)
    stats = fitting_stats(data, partition["fit"], centred)
    z = standardise(centred, stats)
    ranking, qualities = rank_channels(data, z, partition["fit"])
    selected, candidate_rows, coefficient_rows, channel_rows = {}, [], [], []
    for j, channel in enumerate(stats["channels"]):
        channel_rows.append({"run": run_name, "sensor": channel, "direction": stats["direction"][j],
                             "scale": stats["scale"][j], "rank": int(np.where(ranking == j)[0][0])+1,
                             **qualities[j]})
    cal = data.unit.isin(partition["calibration"]) & (data.cycle >= 20)
    validation = data.unit.isin(partition["selection"]) & (data.cycle >= 20)
    for family, name, config in candidate_specs(ranking):
        if family == "MARGEM":
            model = fit_reference(data, partition["fit"], config["quantile"], centred)
        elif family == "EMPIRICO":
            model = fit_empirical(data, z, partition["fit"], **config)
            for channel, weight in zip(stats["channels"], model):
                coefficient_rows.append({"run": run_name, "candidate": name, "sensor": channel, "weight": weight})
        else:
            model = fit_aakr(data, z, partition["fit"], **config)
        hi = predict_hi(data, centred, z, family, model)
        converter = IsotonicRegression(increasing=True, y_min=0., out_of_bounds="clip")
        converter.fit(hi[np.asarray(cal)], data.loc[cal, "rul"],
                      sample_weight=equal_engine_weights(data.loc[cal, "unit"]))
        predicted = np.full(len(data), np.nan)
        predicted[np.asarray(validation)] = converter.predict(hi[np.asarray(validation)])
        loss = cut_rmse(data, predicted, partition["selection"])
        candidate_rows.append({"run": run_name, "family": family, "candidate": name,
                               "selection_rmse": loss, "config": json.dumps(config)})
        key = (loss, name)
        if family not in selected or key < selected[family]["key"]:
            selected[family] = {"key": key, "candidate": name, "config": config,
                                "model": model, "converter": converter, "stats": stats}
    for row in candidate_rows:
        row["chosen"] = row["candidate"] == selected[row["family"]]["candidate"]
    return selected, candidate_rows, coefficient_rows, channel_rows


def transform_selected(data, chosen, family):
    centred = centred_sensors(data)
    z = standardise(centred, chosen["stats"])
    hi = predict_hi(data, centred, z, family, chosen["model"])
    valid = data.cycle >= 20
    out = data.loc[valid, ["unit", "cycle"]].copy()
    out["hi"] = hi[np.asarray(valid)]
    out["predicted_rul"] = chosen["converter"].predict(out.hi.to_numpy())
    return out


def evaluated_predictions(data, chosen, family, ids, run_name, dataset):
    # Endpoint and RUL are attached for scoring only after the transformation.
    inputs = data.drop(columns=["end", "rul"], errors="ignore")
    output = transform_selected(inputs, chosen, family)
    output = output.loc[output.unit.isin(ids)].copy()
    output["actual_rul"] = data.loc[output.index, "rul"]
    output["end"] = data.loc[output.index, "end"]
    output["run"], output["family"], output["dataset"] = run_name, family, dataset
    return output


def per_engine_metrics(predictions):
    rows = []
    for (dataset, run_name, family, unit), g in predictions.groupby(["dataset", "run", "family", "unit"]):
        error = g.predicted_rul-g.actual_rul
        zero = g.loc[g.hi <= 0, "cycle"]
        first = float(zero.iloc[0]) if len(zero) else np.nan
        terminal = float(g.end.iloc[0])
        last = g.iloc[-1]
        early = g.cycle.between(21, 40)
        cuts = g.cycle.isin([int(np.floor(f*terminal)) for f in [.5, .7, .9]])
        rows.append({"dataset": dataset, "run": run_name, "family": family, "unit": int(unit),
                     "history_rmse": float(np.sqrt(np.mean(error**2))),
                     "history_mae": float(np.mean(abs(error))),
                     "cuts_mse": float(np.mean(error.loc[cuts]**2)) if dataset == "cv" else np.nan,
                     "last_error": float(error.iloc[-1]), "last_hi": float(last.hi),
                     "last_actual_rul": float(last.actual_rul), "first_zero": first,
                     "zero_lead": terminal-first, "has_zero": bool(len(zero)),
                     "recovered_after_zero": bool((g.loc[g.cycle > first, "hi"] > 1e-12).any()),
                     "initial_departure_fraction": float((g.loc[early, "hi"] < 1-1e-12).mean()) if early.any() else np.nan,
                     "increase_fraction": float((g.hi.diff().iloc[1:] > 1e-12).mean())})
    return pd.DataFrame(rows)


def freeze_models(selected, run_name):
    frozen = {}
    for family, chosen in selected.items():
        model = chosen["model"]
        detail = {"candidate": chosen["candidate"], "config": chosen["config"],
                  "selection_rmse": chosen["key"][0],
                  "sensors": chosen["stats"]["channels"],
                  "direction": chosen["stats"]["direction"].tolist(),
                  "scale": chosen["stats"]["scale"].tolist(),
                  "converter_hi": chosen["converter"].X_thresholds_.tolist(),
                  "converter_rul": chosen["converter"].y_thresholds_.tolist()}
        if family == "MARGEM":
            detail["reference"] = model.to_dict(orient="records")
        elif family == "EMPIRICO":
            detail["coefficients"] = model.tolist()
        else:
            detail["model"] = {k: v.tolist() if isinstance(v, np.ndarray) else v for k, v in model.items()}
        frozen[family] = detail
    path = OUT / f"models_{run_name}.json"
    path.write_text(json.dumps(frozen, indent=2), encoding="utf-8")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def summaries(metrics):
    rows = []
    for (dataset, family), g in metrics.groupby(["dataset", "family"]):
        rows.append({"dataset": dataset, "family": family, "engines": len(g),
                     "history_rmse_engine_mean": g.history_rmse.mean(),
                     "last_rmse": float(np.sqrt(np.mean(g.last_error**2))),
                     "last_mae": float(abs(g.last_error).mean()),
                     "cuts_rmse": float(np.sqrt(g.cuts_mse.mean())) if dataset == "cv" else np.nan,
                     "last_hi_median": g.last_hi.median(), "zero_engines": int(g.has_zero.sum()),
                     "median_zero_lead": g.zero_lead.median(), "max_zero_lead": g.zero_lead.max(),
                     "recoveries": int(g.recovered_after_zero.sum()),
                     "initial_departure_mean": g.initial_departure_fraction.mean()})
    return pd.DataFrame(rows)


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    data = read_data()
    splits_file = ROOT / "experiments/artifacts/pilot_fd001_03/splits.json"
    splits = json.loads(splits_file.read_text(encoding="utf-8"))
    predictions, selections, coefficients, channels, shapes = [], [], [], [], []
    for partition in splits:
        run_name = f"fold{partition['fold']}"
        print(run_name, "fitting", flush=True)
        selected, rows, weights, ranking = run_partition(data, partition, run_name)
        selections.extend(rows)
        coefficients.extend(weights)
        channels.extend(ranking)
        freeze_models(selected, run_name)
        for family, chosen in selected.items():
            output = evaluated_predictions(data, chosen, family, partition["evaluation"], run_name, "cv")
            predictions.append(output)
            hi = np.full(len(data), np.nan)
            hi[output.index] = output.hi
            shapes.append({"run": run_name, "family": family,
                           **curve_quality(data, hi, partition["evaluation"])})
        print(run_name, "completed", {f: s['candidate'] for f,s in selected.items()}, flush=True)
    # The official label vector is not read until all candidate selection is complete.
    final = {"fit": splits[0]["fit"]+splits[0]["evaluation"],
             "calibration": splits[0]["calibration"], "selection": splits[0]["selection"]}
    selected, rows, weights, ranking = run_partition(data, final, "official")
    selections.extend(rows)
    coefficients.extend(weights)
    channels.extend(ranking)
    freeze_hash = freeze_models(selected, "official")
    (OUT / "official_freeze.json").write_text(json.dumps({"timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "models_sha256": freeze_hash, "selected": {f:s['candidate'] for f,s in selected.items()},
        "label_use": "Official labels excluded from fitting, calibration and selection"}, indent=2), encoding="utf-8")
    official_inputs = read_official_inputs()
    official = attach_official_labels(official_inputs, np.loadtxt(ROOT / "CMAPSSData/RUL_FD001.txt"))
    for family, chosen in selected.items():
        predictions.append(evaluated_predictions(official, chosen, family, sorted(official.unit.unique()), "official", "official"))
    all_predictions = pd.concat(predictions, ignore_index=True)
    metrics = per_engine_metrics(all_predictions)
    summary = summaries(metrics)
    bootstrap = []
    errors = metrics.query("dataset == 'official'").pivot(index="unit", columns="family", values="last_error")
    rng = np.random.default_rng(SEED)
    samples = rng.integers(0, len(errors), (2000, len(errors)))
    for family in ["EMPIRICO", "AAKR"]:
        difference = np.sqrt(np.mean(errors[family].to_numpy()[samples]**2, axis=1))-np.sqrt(np.mean(errors.MARGEM.to_numpy()[samples]**2, axis=1))
        bootstrap.append({"family": family, "comparison": "RMSE minus MARGEM",
                          "difference": float(np.sqrt(np.mean(errors[family]**2))-np.sqrt(np.mean(errors.MARGEM**2))),
                          "p025": float(np.quantile(difference,.025)), "p975": float(np.quantile(difference,.975))})
    label_audit = official.groupby("unit").agg(last_observed=("cycle", "max"), endpoint=("end", "first"))
    label_audit["last_rul"] = label_audit.endpoint-label_audit.last_observed
    frames = {"predictions": all_predictions, "metrics_per_engine": metrics, "summary": summary,
              "selection": pd.DataFrame(selections), "empirical_coefficients": pd.DataFrame(coefficients),
              "sensor_ranking": pd.DataFrame(channels), "shape_metrics": pd.DataFrame(shapes),
              "bootstrap": pd.DataFrame(bootstrap), "official_label_audit": label_audit.reset_index()}
    for name, frame in frames.items():
        frame.to_csv(OUT / f"{name}.csv", index=False)
    (OUT / "splits.json").write_text(json.dumps({"cv": splits, "official_training": final}, indent=2), encoding="utf-8")
    fig, axes = plt.subplots(2, 3, figsize=(13, 7), sharey="row")
    for row, dataset in enumerate(["cv", "official"]):
        for ax, unit in zip(axes[row], [1,2,3]):
            for family in FAMILIES:
                g = all_predictions.query("dataset == @dataset and unit == @unit and family == @family")
                ax.plot(g.cycle, g.hi, label=family)
            if dataset == "cv":
                ax.axvline(g.end.iloc[0], color="black", ls=":")
            ax.set(title=f"{dataset}: motor {unit}", xlabel="Ciclo", ylim=(-.03,1.03))
        axes[row,0].set_ylabel("HI estimado")
    axes[0,-1].legend()
    fig.tight_layout()
    fig.savefig(OUT / "HI_examples.png", dpi=160)
    plt.close(fig)
    lines = ["# P05 — HI empírico e AAKR terminal", "", "Rodada exploratória sem inspeções. AAKR é adaptação do núcleo terminal, não reprodução integral de Baraldi et al. (2018).", "",
             "RUL_FD001 rotula o último ciclo de cada motor de teste. Não fornece HI físico nem sensores futuros. As configurações foram selecionadas antes da avaliação oficial, com registro em official_freeze.json.", "",
             "## Utilidade prognóstica", "", "Conversor isotônico HI→RUL idêntico entre famílias, aprendido em motores separados.", "",
             "| Dados | Família | RMSE nos cortes | RMSE último ciclo | MAE último ciclo | RMSE médio por motor na história |",
             "|---|---|---|---|---|---|"]
    for r in summary.itertuples():
        cuts = f"{r.cuts_rmse:.2f}" if np.isfinite(r.cuts_rmse) else "—"
        lines.append(f"| {r.dataset} | {r.family} | {cuts} | {r.last_rmse:.2f} | {r.last_mae:.2f} | {r.history_rmse_engine_mean:.2f} |")
    lines += ["", "No último ciclo das trajetórias CV a RUL verdadeira é zero; no teste oficial ela varia de 7 a 145. Não comparar essas colunas entre conjuntos como dificuldade equivalente.", "", "## Diagnóstico de condição", "",
              "| Dados | Família | HI mediano no último ciclo | Motores com zero | Antecipação mediana do zero | Máxima | Recuperações | Saída inicial média |",
              "|---|---|---|---|---|---|---|---|"]
    for r in summary.itertuples():
        lines.append(f"| {r.dataset} | {r.family} | {r.last_hi_median:.4f} | {r.zero_engines} | {r.median_zero_lead:.1f} | {r.max_zero_lead:.1f} | {r.recoveries} | {r.initial_departure_mean:.3f} |")
    lines += ["", "No teste oficial, o último HI é anterior a F: não equivale a HI terminal. Ausências de zero permanecem censuradas; sensores posteriores ao truncamento não foram simulados. Saída inicial é proporção de ciclos 21–40 por motor, sob hipótese de estabilidade não confirmada.", "", "## Escolhas no ajuste final", ""]
    for family, chosen in selected.items():
        lines.append(f"- {family}: {chosen['candidate']}; RMSE interno {chosen['key'][0]:.2f} ciclos.")
    lines += ["", "## Incerteza descritiva no teste oficial", "", "Diferença de RMSE relativamente ao controle; valores negativos favorecem a alternativa.", ""]
    for r in bootstrap:
        lines.append(f"- {r['family']}: {r['difference']:.2f} ciclos; percentis 2,5%–97,5% do bootstrap pareado [{r['p025']:.2f}; {r['p975']:.2f}].")
    lines += ["", "## Limites e decisão", "",
              "O alvo de treino do HI empírico é uma função convencional de RUL. A avaliação externa mede utilidade prognóstica e comportamento da curva, sem observar o HI verdadeiro. Boa previsão por um conversor não demonstra recuperação de margens físicas nem fidelidade causal dos pesos.", "",
              "AAKR emprega atributos causais e seleção de subconjuntos determinística, substituindo componentes do artigo original. A comparação identifica desempenho destas implementações sob este orçamento, não superioridade sobre a reprodução integral de Baraldi. O número de configurações por família é diferente e está preservado em selection.csv.", "",
              "O conversor e as referências usam 40/20/20/20 em CV e 60/20/20 no ajuste oficial, sem reajuste depois da seleção. Não há escolha retrospectiva por menor RMSE oficial. A ausência ou antecipação excessiva de zeros limita o uso do HI para F e para inspeções, mesmo quando os erros de RUL forem menores.", "",
              "Artefatos: predições por ciclo, métricas por motor, todas as escolhas internas, coeficientes, rankings, modelos completos e conversores, auditoria de rótulos, bootstrap, figura, partições e metadados. Inspeções e protocolo principal permanecem suspensos/abertos."]
    (OUT / "relatorio.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    sources = [Path(__file__), ROOT / "experiments/protocolo_piloto_fd001_05.md",
               ROOT / "experiments/test_pilot_fd001_05.py", ROOT / "experiments/pilot_fd001.py",
               ROOT / "experiments/pilot_fd001_04.py", splits_file,
               ROOT / "CMAPSSData/train_FD001.txt", ROOT / "CMAPSSData/test_FD001.txt",
               ROOT / "CMAPSSData/RUL_FD001.txt"]
    metadata = {"timestamp_utc": datetime.now(timezone.utc).isoformat(), "seed": SEED,
                "source_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
                "versions": {n:importlib.metadata.version(n) for n in ["numpy","pandas","scipy","scikit-learn","matplotlib"]},
                "aakr_source": "https://doi.org/10.1016/j.ymssp.2017.09.013",
                "aakr_scope": "Terminal reconstruction kernel; adapted features, subset search and normalisation",
                "official_models_sha256_before_labels": freeze_hash}
    (OUT / "metadata.json").write_text(json.dumps(metadata,indent=2), encoding="utf-8")
    manifest = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir())
                if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest,indent=2), encoding="utf-8")
    print(summary.to_string(index=False), flush=True)


if __name__ == "__main__":
    with threadpool_limits(limits=2):
        run()
