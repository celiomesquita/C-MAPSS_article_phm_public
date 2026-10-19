"""P04: causal empirical margins with a healthy deadband; no inspections."""

import hashlib
import importlib.metadata
import json
from datetime import datetime, timezone
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pilot_fd001 import ROOT, SENSORS, read_data, smooth

OUT = ROOT / "experiments/artifacts/pilot_fd001_04"
QUANTILES = [.5, .65, .75, .85, .9, .95, .99, 1.]
PENALTIES = [.25, .5, 1., 2.]


def centred_sensors(data):
    means = smooth(data, 15)
    baseline = means.loc[data.cycle == 20].copy()
    baseline.index = data.loc[data.cycle == 20, "unit"]
    return means-baseline.loc[data.unit].set_axis(data.index)


def fit_reference(data, fit_ids, quantile, centred=None):
    centred = centred_sensors(data) if centred is None else centred
    initial = data.unit.isin(fit_ids) & data.cycle.between(15, 20)
    terminal = data.unit.isin(fit_ids) & (data.cycle == data.end)
    difference = centred.loc[terminal]
    direction = np.sign(difference.median())
    scale = centred.loc[initial].std(ddof=1)
    bound = difference.mul(direction).quantile(quantile, interpolation="higher")
    ref = pd.DataFrame({"sensor": SENSORS, "direction": direction.values,
                        "sigma": scale.values, "bound": bound.values})
    ref["eligible"] = ((ref.sigma > 1e-6) & (ref.direction != 0)
                       & (ref.bound > 3*ref.sigma+1e-6))
    return ref


def transform_hi(data, reference, multiplier=2, centred=None):
    centred = centred_sensors(data) if centred is None else centred
    ref = reference.loc[reference.eligible].set_index("sensor")
    if ref.empty:
        raise ValueError("No eligible HI channels")
    a = centred[ref.index].mul(ref.direction)
    tolerance = multiplier*ref.sigma
    margins = (1-a.sub(tolerance).clip(lower=0).div(ref.bound-tolerance)).clip(0, 1)
    margins.loc[data.cycle < 20] = np.nan
    hi = margins.min(axis=1)
    limiting = pd.Series("", index=data.index, dtype=object)
    valid = hi.notna()
    limiting.loc[valid] = margins.loc[valid].idxmin(axis=1)
    return hi, limiting


def engine_metrics(data, hi, ids):
    rows = []
    for unit in ids:
        mask = (data.unit == unit) & (data.cycle >= 20)
        g = data.loc[mask]
        h = hi.loc[mask]
        zero_cycles = g.loc[h <= 0, "cycle"]
        first = float(zero_cycles.iloc[0]) if len(zero_cycles) else np.nan
        end = int(g.end.iloc[0])
        dif = h.diff().iloc[1:]
        early = g.cycle.between(21, 40)
        rows.append({"unit": int(unit), "end": end, "estimated_F": first,
                     "lead": end-first, "crossed": bool(len(zero_cycles)),
                     "endpoint_hi": float(h.iloc[-1]),
                     "initial_departure_fraction": float((h.loc[early] < 1-1e-12).mean()),
                     "recovered_after_zero": bool((h.loc[g.cycle > first] > 1e-12).any())
                     if len(zero_cycles) else False,
                     "increase_fraction": float((dif > 1e-12).mean()),
                     "normalised_lead": (end-first)/(end-20)})
    return pd.DataFrame(rows)


def choose_quantile(metrics, penalty):
    scored = metrics.copy()
    scored["loss"] = np.where(scored.crossed, scored.normalised_lead, penalty)
    means = scored.groupby("quantile").loss.mean().reset_index()
    best = means.sort_values(["loss", "quantile"]).iloc[0]
    means["chosen"] = means["quantile"] == best["quantile"]
    means["missing_penalty"] = penalty
    return float(best["quantile"]), means


def aggregate(g):
    return {"engines": len(g), "crossings": int(g.crossed.sum()),
            "missing": int((~g.crossed).sum()), "median_lead": g.lead.median(),
            "maximum_lead": g.lead.max(), "endpoint_hi_median": g.endpoint_hi.median(),
            "initial_departure_mean": g.initial_departure_fraction.mean(),
            "recoveries": int(g.recovered_after_zero.sum()),
            "increase_fraction_median": g.increase_fraction.median()}


def run():
    OUT.mkdir(parents=True, exist_ok=True)
    data = read_data()
    centred = centred_sensors(data)
    splits_path = ROOT / "experiments/artifacts/pilot_fd001_03/splits.json"
    splits = json.loads(splits_path.read_text(encoding="utf-8"))
    references, evaluations, selections, selected, trajectories = [], [], [], [], []
    for partition in splits:
        fold = partition["fold"]
        internal = []
        cache = {}
        for q in QUANTILES:
            ref = fit_reference(data, partition["fit"], q, centred)
            refs = ref.assign(fold=fold, quantile=q)
            references.append(refs)
            if not ref.eligible.any():
                continue
            for k in [0, 2, 3]:
                hi, limiting = transform_hi(data, ref, k, centred)
                cache[q, k] = hi, limiting
                ev = engine_metrics(data, hi, partition["evaluation"])
                ev["fold"], ev["quantile"], ev["multiplier"] = fold, q, k
                evaluations.append(ev)
                if k == 2:
                    val = engine_metrics(data, hi, partition["selection"])
                    val["quantile"] = q
                    internal.append(val)
        internal = pd.concat(internal, ignore_index=True)
        for penalty in PENALTIES:
            q, scores = choose_quantile(internal, penalty)
            selections.append(scores.assign(fold=fold))
            for k in [0, 2, 3]:
                hi, limiting = cache[q, k]
                ev = engine_metrics(data, hi, partition["evaluation"])
                ev["fold"], ev["quantile"], ev["multiplier"] = fold, q, k
                ev["missing_penalty"] = penalty
                selected.append(ev)
                if penalty == 1:
                    mask = data.unit.isin(partition["evaluation"]) & (data.cycle >= 20)
                    tr = data.loc[mask, ["unit", "cycle", "end"]].copy()
                    tr["hi"], tr["limiting_sensor"] = hi.loc[mask], limiting.loc[mask]
                    tr["fold"], tr["quantile"], tr["multiplier"] = fold, q, k
                    trajectories.append(tr)
        internal.assign(fold=fold).to_csv(OUT / f"selection_engines_fold{fold}.csv", index=False)
        print(f"fold={fold} completed", flush=True)
    frames = {"reference": pd.concat(references, ignore_index=True),
              "candidate_metrics": pd.concat(evaluations, ignore_index=True),
              "selection": pd.concat(selections, ignore_index=True),
              "selected_metrics": pd.concat(selected, ignore_index=True),
              "selected_trajectories": pd.concat(trajectories, ignore_index=True)}
    summaries = []
    for (penalty, k), g in frames["selected_metrics"].groupby(["missing_penalty", "multiplier"]):
        summaries.append({"missing_penalty": penalty, "multiplier": k, **aggregate(g)})
    frames["selected_summary"] = pd.DataFrame(summaries)
    fold_summaries = []
    for (fold, penalty, k), g in frames["selected_metrics"].groupby(["fold", "missing_penalty", "multiplier"]):
        fold_summaries.append({"fold": fold, "missing_penalty": penalty, "multiplier": k, **aggregate(g)})
    frames["selected_fold_summary"] = pd.DataFrame(fold_summaries)
    candidates = []
    for (q, k), g in frames["candidate_metrics"].groupby(["quantile", "multiplier"]):
        candidates.append({"quantile": q, "multiplier": k, **aggregate(g)})
    frames["candidate_summary"] = pd.DataFrame(candidates)
    for name, frame in frames.items():
        frame.to_csv(OUT / f"{name}.csv", index=False)
    (OUT / "splits.json").write_text(json.dumps(splits, indent=2), encoding="utf-8")
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.5), sharey=True)
    for ax, unit in zip(axes, [1, 2, 3]):
        for k in [0, 2, 3]:
            g = frames["selected_trajectories"].query("unit == @unit and multiplier == @k")
            ax.plot(g.cycle, g.hi, label=f"k={k}")
        ax.axvline(g.end.iloc[0], color="black", ls=":", label="Endpoint")
        ax.set(title=f"Motor {unit}; q={g['quantile'].iloc[0]:g}", xlabel="Ciclo", ylim=(-.03, 1.03))
    axes[0].set_ylabel("HI estimado")
    axes[-1].legend()
    fig.tight_layout()
    fig.savefig(OUT / "HI_examples.png", dpi=160)
    plt.close(fig)
    summary = frames["selected_summary"]
    lines = ["# P04 — resultados exploratórios do HI", "", "Sem inspeção e sem alteração das políticas de remoção.", "",
             "## Curvas seleccionadas internamente", "",
             "λ é a penalização convencional de ausência de zero; k multiplica σ na tolerância inicial.", "",
             "| λ | k | Passagens/100 | Sem zero | Antecipação mediana | Máxima | HI terminal mediano | Saída inicial média | Recuperações |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in summary.itertuples():
        lines.append(f"| {r.missing_penalty:g} | {r.multiplier} | {r.crossings} | {r.missing} | {r.median_lead:.1f} | {r.maximum_lead:.1f} | {r.endpoint_hi_median:.4f} | {r.initial_departure_mean:.3f} | {r.recoveries} |")
    lines += ["", "## Escolhas por fold", ""]
    for penalty in PENALTIES:
        g = frames["selection"].query("missing_penalty == @penalty and chosen")
        lines.append(f"- λ={penalty:g}: quantis {g['quantile'].tolist()}.")
    primary = summary.query("missing_penalty == 1 and multiplier == 2").iloc[0]
    lines += ["", "## Resultado e decisão", "",
              f"Resultado misto. Na configuração principal, {int(primary.crossings)}/100 motores chegaram a zero, com antecipação mediana {primary.median_lead:g} ciclos e máxima {primary.maximum_lead:g}, entre passagens. Houve {int(primary.missing)} ausências e {int(primary.recoveries)} recuperações posteriores a zero. A saída do patamar inicial ocorreu em média em {100*primary.initial_departure_mean:.1f}% dos ciclos 21–40 por motor, apesar da tolerância de dois desvios.", "",
              "A tolerância reduz a resposta à variabilidade inicial, mas não sustenta o patamar pretendido nesta amostra; a interpretação pressupõe que o intervalo 21–40 seja estável, hipótese ainda não confirmada. A referência terminal mantém compromisso forte entre antecipação e ausência, dependente da penalização convencional. Não adoptar ainda o primeiro zero como F nem esta curva como gerador de inspeções. Investigar calibração conjunta da variabilidade entre sensores e heterogeneidade terminal, sem impor monotonicidade para encobrir as recuperações."]
    lines += ["", "## Limites da interpretação", "",
              "A tolerância muda o patamar e a amplitude do HI, mas não o primeiro zero para canais e referências fixos. As três tolerâncias não constituem três evidências independentes de F.", "",
              "A referência terminal é supervisionada pelos endpoints dos motores de ajuste. Não representa limites operacionais certificados. Não há observações posteriores ao endpoint: ausência de zero é censura, não atraso medido.", "",
              "O primeiro zero pode ser seguido de recuperação; monotonicidade não foi imposta. O período inicial assumido estável não tem rótulo físico independente. Se o endpoint cair dentro da região de tolerância, a própria interpretação de saúde precisa de revisão.", "",
              "A perda de selecção e λ são convenções exploratórias, não custos de manutenção ou critérios de segurança. A sensibilidade a λ limita qualquer adopção definitiva. As cinco avaliações externas reutilizam dados já examinados em P01–P03.", "",
              "A lista de sensores elegíveis está em reference.csv (inclui excluídos). Os empates do mínimo têm um representante por ordem de coluna, não uma causa exclusiva.", "",
              "Artefatos: candidate_metrics.csv/candidate_summary.csv (todos os candidatos), selection.csv e selection_engines_fold*.csv (selecção interna), selected_metrics.csv/selected_summary.csv (avaliação das escolhas), selected_trajectories.csv, HI_examples.png, splits.json, metadata.json e manifest.json."]
    (OUT / "relatorio.md").write_text("\n".join(lines)+"\n", encoding="utf-8")
    sources = [Path(__file__), ROOT / "experiments/pilot_fd001.py",
               ROOT / "experiments/protocolo_piloto_fd001_04.md", splits_path,
               ROOT / "CMAPSSData/train_FD001.txt", ROOT / "experiments/test_pilot_fd001_04.py"]
    metadata = {"timestamp_utc": datetime.now(timezone.utc).isoformat(), "quantiles": QUANTILES,
                "multipliers": [0, 2, 3], "missing_penalties": PENALTIES,
                "primary": {"multiplier": 2, "missing_penalty": 1}, "example_engines": [1, 2, 3],
                "versions": {n: importlib.metadata.version(n) for n in ["numpy", "pandas", "matplotlib"]},
                "source_hashes": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir())
                if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


if __name__ == "__main__":
    run()
