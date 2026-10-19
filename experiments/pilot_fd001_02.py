"""P02: exploratory nested selection of detector and decision calibration."""

import hashlib
import importlib.metadata
import json
import platform
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.model_selection import GroupKFold, GroupShuffleSplit

from pilot_fd001 import BASELINE, ROOT, SEED, SENSORS, features, models, read_data, smooth

OUT = ROOT / "experiments/artifacts/pilot_fd001_02"
VARIANTS = ["raw", "global", "global_gate30", "local_gate30"]


def detector_score(data, fit_ids):
    means = smooth(data, 15)
    centres = data.loc[data.cycle <= BASELINE].groupby("unit")[SENSORS].mean()
    residual = means - centres.loc[data.unit].set_axis(data.index)
    scales = residual.loc[(data.cycle <= BASELINE) & data.unit.isin(fit_ids)].std()
    selected = scales.index[scales > 1e-6].tolist()
    z = residual[selected].abs().div(scales[selected])
    second = pd.Series(np.partition(z.to_numpy(), -2, axis=1)[:, -2], index=data.index)
    second.loc[data.cycle <= BASELINE] = np.nan
    score = second.groupby(data.unit).transform(lambda s: s.rolling(3, min_periods=3).min())
    return score, selected


def points_at(data, score, threshold):
    return data.loc[score > threshold].groupby("unit").cycle.min()


def detector_stats(data, points, ids):
    ends = data.loc[data.unit.isin(ids)].groupby("unit").end.first()
    p = points.reindex(ids)
    leads = ends.reindex(ids) - p
    return {"early_count": int((p <= 40).sum()), "coverage": int((leads > 0).sum()),
            "median_lead": float(leads[leads > 0].median()) if (leads > 0).any() else 0.}


def margins(cal):
    error = (cal.raw - cal.rul).clip(lower=0)
    global_errors = error.groupby(cal.unit).max()
    local_errors = error.loc[cal.raw <= 30].groupby(cal.loc[cal.raw <= 30, "unit"]).max()
    return {"global_margin": float(np.quantile(global_errors, .9, method="higher")),
            "local_margin": float(np.quantile(local_errors, .9, method="higher")) if len(local_errors) >= 10 else None,
            "global_engines": len(global_errors), "local_engines": len(local_errors)}


def simulate(data, pred, ids, variant, calibration):
    margin = calibration["local_margin"] if variant == "local_gate30" else calibration["global_margin"]
    if margin is None:
        return pd.DataFrame()
    margin = 0. if variant == "raw" else margin
    rows = []
    for unit in ids:
        end = int(data.loc[data.unit == unit, "end"].iloc[0])
        g = pred.loc[pred.unit == unit]
        hit = (g.raw - margin).clip(lower=0) <= 10
        if variant.endswith("gate30"):
            hit &= g.raw <= 30
        cycles = g.loc[hit, "cycle"]
        removal = int(cycles.iloc[0]) if len(cycles) else end
        rows.append({"unit": unit, "variant": variant, "removal": removal, "end": end,
                     "endpoint": removal >= end, "unused": end - removal, "prediction_available": len(g) > 0,
                     "margin": margin})
    return pd.DataFrame(rows)


def split_units(dev, fold):
    inside, sel = next(GroupShuffleSplit(n_splits=1, test_size=.25, random_state=SEED + 100 + fold)
                       .split(dev, groups=dev.unit))
    pool = dev.iloc[inside]
    fit, cal = next(GroupShuffleSplit(n_splits=1, test_size=1/3, random_state=SEED + 200 + fold)
                   .split(pool, groups=pool.unit))
    return [sorted(frame.unit.unique().tolist()) for frame in [pool.iloc[fit], pool.iloc[cal], dev.iloc[sel]]]


def md_table(frame):
    out = ["| " + " | ".join(frame.columns) + " |", "| " + " | ".join(["---"] * len(frame.columns)) + " |"]
    for row in frame.itertuples(index=False, name=None):
        out.append("| " + " | ".join(f"{v:.3f}" if isinstance(v, float) else str(v) for v in row) + " |")
    return "\n".join(out)


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    data = read_data()
    source = ROOT / "CMAPSSData/train_FD001.txt"
    initial_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    partitions, detector_rows, detections, calibration_rows, selection_rows = [], [], [], [], []
    prediction_rows, decision_rows, metric_rows = [], [], []
    for fold, (dev_idx, test_idx) in enumerate(GroupKFold(5).split(data, groups=data.unit), 1):
        fit_ids, cal_ids, sel_ids = split_units(data.iloc[dev_idx], fold)
        test_ids = sorted(data.iloc[test_idx].unit.unique().tolist())
        groups = list(map(set, [fit_ids, cal_ids, sel_ids, test_ids]))
        assert [len(g) for g in groups] == [40, 20, 20, 20]
        assert len(set.union(*groups)) == 100
        partitions.append({"fold": fold, "fit": fit_ids, "calibration": cal_ids, "selection": sel_ids, "evaluation": test_ids})
        score, selected = detector_score(data, fit_ids)
        early = (data.cycle.between(21, 40)) & data.unit.isin(fit_ids)
        null = score.loc[early].groupby(data.loc[early, "unit"]).max()
        candidates = [("fixed2", 2.)] + [(f"null_q{q}", max(2., float(np.quantile(null, q, method="higher"))))
                                          for q in [.9, .95, 1.]]
        entries = []
        for label, threshold in candidates:
            points = points_at(data, score, threshold)
            stats = detector_stats(data, points, sel_ids)
            entries.append({"fold": fold, "candidate": label, "threshold": threshold, **stats})
        feasible = [e for e in entries if e["early_count"] <= 2]
        best = min(feasible, key=lambda e: (-e["coverage"], -e["median_lead"], e["threshold"])) if feasible else min(
            entries, key=lambda e: (e["early_count"], -e["coverage"], -e["median_lead"], e["threshold"]))
        for e in entries:
            e["chosen"] = e["candidate"] == best["candidate"]
            e["selection_feasible"] = bool(feasible)
            detector_rows.append(e)
        points = points_at(data, score, best["threshold"])
        fixed = points_at(data, score, 2.)
        for unit in test_ids:
            end = int(data.loc[data.unit == unit, "end"].iloc[0])
            detections.append({"fold": fold, "unit": unit, "end": end, "p": points.get(unit, np.nan),
                               "p_fixed2": fixed.get(unit, np.nan), "threshold": best["threshold"],
                               "candidate": best["candidate"], "selection_feasible": bool(feasible)})
        x = features(data, selected)
        valid = (data.cycle >= data.unit.map(points)) & x.notna().all(axis=1)
        train = valid & data.unit.isin(fit_ids)
        counts = data.loc[train].groupby("unit").size()
        weights = 1. / data.loc[train, "unit"].map(counts)
        weights /= weights.mean()
        for name, model in models().items():
            print(f"fold={fold} model={name} threshold={best['threshold']:.3f} rows={int(train.sum())}", flush=True)
            model.fit(x.loc[train], data.loc[train, "rul"], sample_weight=weights)
            parts = {}
            for role, ids in [("calibration", cal_ids), ("selection", sel_ids), ("evaluation", test_ids)]:
                mask = valid & data.unit.isin(ids)
                out = data.loc[mask, ["unit", "cycle", "rul", "end"]].copy()
                out["raw"] = np.maximum(0., model.predict(x.loc[mask]))
                out["fold"], out["model"], out["role"] = fold, name, role
                prediction_rows.append(out)
                parts[role] = out
            calibration = margins(parts["calibration"])
            calibration_rows.append({"fold": fold, "model": name, **calibration})
            choices = []
            for variant in VARIANTS:
                trial = simulate(data, parts["selection"], sel_ids, variant, calibration)
                if trial.empty:
                    continue
                choices.append({"variant": variant, "endpoint_count": int(trial.endpoint.sum()),
                                "mean_unused": float(trial.unused.mean())})
            choice = min(choices, key=lambda c: (c["endpoint_count"], c["mean_unused"], VARIANTS.index(c["variant"])))
            for c in choices:
                selection_rows.append({"fold": fold, "model": name, **c, "chosen": c["variant"] == choice["variant"]})
                result = simulate(data, parts["evaluation"], test_ids, c["variant"], calibration)
                result["fold"], result["model"], result["chosen"] = fold, name, c["variant"] == choice["variant"]
                decision_rows.append(result)
            for unit, g in parts["evaluation"].groupby("unit"):
                metric_rows.append({"fold": fold, "model": name, "unit": int(unit),
                                    "rmse": float(np.sqrt(np.mean((g.raw-g.rul)**2)))})
    files = {"detector_selection": detector_rows, "detections": detections, "margins": calibration_rows,
             "policy_selection": selection_rows, "metrics_per_engine": metric_rows}
    for label, rows in files.items():
        pd.DataFrame(rows).to_csv(OUT / (label + ".csv"), index=False)
    pred = pd.concat(prediction_rows, ignore_index=True)
    decisions = pd.concat(decision_rows, ignore_index=True)
    pred.to_csv(OUT / "predictions.csv", index=False)
    decisions.to_csv(OUT / "decisions_per_engine.csv", index=False)
    summary = decisions.groupby(["model", "variant"]).agg(engines=("unit", "size"),
                endpoints=("endpoint", "sum"), mean_unused=("unused", "mean"), mean_exposure=("removal", "mean")).reset_index()
    chosen = decisions.loc[decisions.chosen].groupby("model").agg(engines=("unit", "size"),
                endpoints=("endpoint", "sum"), mean_unused=("unused", "mean"), mean_exposure=("removal", "mean")).reset_index()
    summary.to_csv(OUT / "decision_summary.csv", index=False)
    chosen.to_csv(OUT / "selected_policy_summary.csv", index=False)
    (OUT / "splits.json").write_text(json.dumps(partitions, indent=2), encoding="utf-8")
    assert initial_hash == hashlib.sha256(source.read_bytes()).hexdigest()
    metadata = {"timestamp_utc": datetime.now(timezone.utc).isoformat(), "python": platform.python_version(),
                "seed": SEED, "data_sha256": initial_hash, "scripts": {
                    str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in [Path(__file__), ROOT / "experiments/pilot_fd001.py", ROOT / "experiments/protocolo_piloto_fd001_02.md"]},
                "versions": {n: importlib.metadata.version(n) for n in ["numpy", "pandas", "scikit-learn", "xgboost", "lightgbm"]},
                "scope": "Exploratory refinement; no inspection or physical HI; no untouched confirmatory test"}
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    detection = pd.DataFrame(detections)
    detector_summary = pd.DataFrame([{"detector": col, "detected": int(detection[col].notna().sum()),
             "median_P": float(detection[col].median()), "alerts_by_40": int((detection[col] <= 40).sum()),
             "median_lead": float((detection.end - detection[col]).median())} for col in ["p_fixed2", "p"]])
    detector_summary.to_csv(OUT / "detector_summary.csv", index=False)
    report = "# P02 — resultados exploratórios sem inspeção\n\n" + (
        "Cinco folds por motor, com 40/20/20/20 motores para ajuste/calibração/selecção/avaliação. "
        "Todos os limiares e variantes escolhidos apenas na partição interna de selecção. "
        "Os motores externos já foram explorados em P01; não há confirmação independente.\n\n"
        "## Detector\n\n" + md_table(detector_summary) + "\n\n"
        "A calibração assume ciclos 21–40 estáveis. Alertas precoces são diagnóstico dessa hipótese, "
        "não falsos positivos confirmados. Ausência de detecção é preservada. Não se mede P físico.\n\n"
        "## Todas as variantes\n\n" + md_table(summary) + "\n\n"
        "`raw`: sem margem; `global`: margem de máximos por motor; `global_gate30`: mesma margem "
        "apenas na região prevista ≤30; `local_gate30`: margem estimada nessa região. "
        "Gatilho ≤10 e acção imediata, sem antecedência logística validada.\n\n"
        "## Variante escolhida internamente por modelo\n\n" + md_table(chosen) + "\n\n"
        "A selecção minimiza primeiro chegadas ao endpoint, depois vida não usada. Não demonstra safety "
        "nem selecciona um modelo vencedor. Mais exposição só é economicamente preferível dentro de "
        "um domínio admissível ainda não estabelecido. A diferença para P01 também inclui menor conjunto "
        "de treino; não é efeito isolado do detector. Nenhuma inspeção foi simulada.\n\n"
        "## Rastreabilidade\n\n[Protocolo](../../protocolo_piloto_fd001_02.md). "
        "CSVs guardam todas as escolhas, margens, predições e decisões por motor. "
        "Metadados guardam hashes, versões e partições; manifesto cobre todos os artefactos. "
        "Sem alterações aos dados ou resultados de P01. O protocolo principal não está congelado.\n")
    (OUT / "relatorio.md").write_text(report, encoding="utf-8")
    manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir())
                if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(detector_summary.to_string(index=False), flush=True)
    print(summary.to_string(index=False), flush=True)
    print("INTERNALLY SELECTED:\n" + chosen.to_string(index=False), flush=True)


if __name__ == "__main__":
    run()
