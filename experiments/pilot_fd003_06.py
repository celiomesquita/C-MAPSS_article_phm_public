"""P06: frozen FD001 transfer versus unchanged-method refitting on FD003."""

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
from threadpoolctl import threadpool_limits

import pilot_fd001_05 as p05
from pilot_fd001 import ROOT, SEED, SENSORS

OUT = ROOT / "experiments/artifacts/pilot_fd003_06"
SOURCE_MODELS = ROOT / "experiments/artifacts/pilot_fd001_05/models_official.json"


class FrozenConverter:
    def __init__(self, x, y):
        self.X_thresholds_ = np.asarray(x)
        self.y_thresholds_ = np.asarray(y)

    def predict(self, values):
        return np.interp(values, self.X_thresholds_, self.y_thresholds_)


def load_models(path):
    records = json.loads(Path(path).read_text(encoding="utf-8"))
    models = {}
    for family, record in records.items():
        if family == "MARGEM":
            model = pd.DataFrame(record["reference"])
        elif family == "EMPIRICO":
            model = np.asarray(record["coefficients"])
        else:
            model = record["model"]
            for key in ["columns", "bank", "bank_units", "spread", "loo_terminal_residuals"]:
                model[key] = np.asarray(model[key])
        models[family] = {"candidate": record["candidate"], "config": record["config"],
                          "key": (record["selection_rmse"], record["candidate"]), "model": model,
                          "converter": FrozenConverter(record["converter_hi"], record["converter_rul"]),
                          "stats": {"channels": record["sensors"], "direction": np.asarray(record["direction"]),
                                    "scale": np.asarray(record["scale"])}}
    return models


def save_models(models, name):
    # Reuse the existing serializer, changing its destination only within this call.
    previous = p05.OUT
    try:
        p05.OUT = OUT
        return p05.freeze_models(models, name)
    finally:
        p05.OUT = previous


def read_inputs(kind, subset="FD003"):
    names = ["unit", "cycle", "op1", "op2", "op3"]+SENSORS
    data = pd.read_csv(ROOT / f"CMAPSSData/{kind}_{subset}.txt", sep=r"\s+", header=None, names=names)
    data[["unit", "cycle"]] = data[["unit", "cycle"]].astype(int)
    return data


def complete_labels(data):
    labelled = data.copy()
    labelled["end"] = labelled.groupby("unit").cycle.transform("max")
    labelled["rul"] = labelled.end-labelled.cycle
    return labelled


def engine_metrics(predictions):
    metrics = p05.per_engine_metrics(predictions)
    # Complete target trajectories are also available for frozen-source diagnostics.
    for index, row in metrics.query("dataset == 'transfer_complete'").iterrows():
        g = predictions.query("dataset == @row.dataset and family == @row.family and unit == @row.unit")
        end = g.end.iloc[0]
        cuts = g.cycle.isin([int(np.floor(f*end)) for f in [.5,.7,.9]])
        metrics.loc[index,"cuts_mse"] = np.mean((g.loc[cuts,"predicted_rul"]-g.loc[cuts,"actual_rul"])**2)
    return metrics


def summarise(metrics):
    summary = p05.summaries(metrics)
    for index, row in summary.query("dataset == 'transfer_complete'").iterrows():
        g = metrics.query("dataset == @row.dataset and family == @row.family")
        summary.loc[index,"cuts_rmse"] = np.sqrt(g.cuts_mse.mean())
    return summary


def bootstrap_comparisons(metrics):
    official = metrics.query("dataset in ['official','transfer_official']")
    errors = official.pivot(index="unit", columns=["dataset","family"], values="last_error")
    samples = np.random.default_rng(SEED).integers(0,len(errors),(2000,len(errors)))
    comparisons = [("refit_minus_transfer",("official",f),("transfer_official",f)) for f in p05.FAMILIES]
    comparisons += [("alternative_minus_margin",("official",f),("official","MARGEM")) for f in ["EMPIRICO","AAKR"]]
    rows = []
    for contrast, a, b in comparisons:
        aa, bb = errors[a].to_numpy(), errors[b].to_numpy()
        difference = np.sqrt(np.mean(aa[samples]**2,axis=1))-np.sqrt(np.mean(bb[samples]**2,axis=1))
        rows.append({"contrast":contrast,"family":a[1],
                     "difference":float(np.sqrt(np.mean(aa**2))-np.sqrt(np.mean(bb**2))),
                     "p025":float(np.quantile(difference,.025)),"p975":float(np.quantile(difference,.975))})
    return pd.DataFrame(rows)


def label_audit(official):
    audit = official.groupby("unit").agg(last_observed=("cycle","max"),endpoint=("end","first"))
    audit["last_rul"] = audit.endpoint-audit.last_observed
    return audit.reset_index()


def run():
    OUT.mkdir(parents=True,exist_ok=True)
    source_hash = hashlib.sha256(SOURCE_MODELS.read_bytes()).hexdigest()
    # Audit loading against previously archived FD001 outputs before touching FD003 outcomes.
    transfer = load_models(SOURCE_MODELS)
    source_inputs = read_inputs("test","FD001")
    source_predictions = pd.read_csv(SOURCE_MODELS.parent / "predictions.csv").query("dataset == 'official'")
    for family, chosen in transfer.items():
        output = p05.transform_selected(source_inputs,chosen,family)
        archived = source_predictions.query("family == @family").sort_values(["unit","cycle"])
        np.testing.assert_allclose(output.hi,archived.hi,atol=1e-10)
        np.testing.assert_allclose(output.predicted_rul,archived.predicted_rul,atol=1e-9)
    inputs = read_inputs("train")
    data = complete_labels(inputs)
    assert data.unit.nunique() == 100
    splits_file = ROOT / "experiments/artifacts/pilot_fd001_03/splits.json"
    splits = json.loads(splits_file.read_text(encoding="utf-8"))
    predictions, selections, coefficients, channels, shapes = [], [], [], [], []
    for partition in splits:
        name = f"fold{partition['fold']}"
        print(name,"FD003 fitting",flush=True)
        selected, rows, weights, ranking = p05.run_partition(data,partition,name)
        selections.extend(rows)
        coefficients.extend(weights)
        channels.extend(ranking)
        save_models(selected,name)
        for family, chosen in selected.items():
            output = p05.evaluated_predictions(data,chosen,family,partition["evaluation"],name,"cv")
            predictions.append(output)
            health = np.full(len(data),np.nan)
            health[output.index] = output.hi
            shapes.append({"run":name,"family":family,"dataset":"cv",
                           **p05.curve_quality(data,health,partition["evaluation"])})
        print(name,"completed",{f:s['candidate'] for f,s in selected.items()},flush=True)
    final = {"fit":splits[0]["fit"]+splits[0]["evaluation"],
             "calibration":splits[0]["calibration"],"selection":splits[0]["selection"]}
    selected, rows, weights, ranking = p05.run_partition(data,final,"official")
    selections.extend(rows)
    coefficients.extend(weights)
    channels.extend(ranking)
    final_hash = save_models(selected,"official")
    freeze = {"timestamp_utc":datetime.now(timezone.utc).isoformat(),"refit_models_sha256":final_hash,
              "source_models_sha256":source_hash,"selected":{f:s['candidate'] for f,s in selected.items()},
              "target_official_labels_excluded_from_selection":True}
    (OUT / "official_freeze.json").write_text(json.dumps(freeze,indent=2),encoding="utf-8")
    official_inputs = read_inputs("test")
    # Official FD003 labels are read only after all refitting choices have been frozen.
    official = p05.attach_official_labels(official_inputs,np.loadtxt(ROOT / "CMAPSSData/RUL_FD003.txt"))
    assert official.unit.nunique() == 100
    for family in p05.FAMILIES:
        predictions.append(p05.evaluated_predictions(official,selected[family],family,sorted(official.unit.unique()),"official","official"))
        predictions.append(p05.evaluated_predictions(official,transfer[family],family,sorted(official.unit.unique()),"transfer","transfer_official"))
        output = p05.evaluated_predictions(data,transfer[family],family,sorted(data.unit.unique()),"transfer","transfer_complete")
        predictions.append(output)
        shapes.append({"run":"transfer","family":family,"dataset":"transfer_complete",
                       **p05.curve_quality(data,p05.transform_selected(inputs,transfer[family],family).hi.reindex(data.index).to_numpy(),sorted(data.unit.unique()))})
    all_predictions = pd.concat(predictions,ignore_index=True)
    metrics = engine_metrics(all_predictions)
    summary = summarise(metrics)
    bootstrap = bootstrap_comparisons(metrics)
    distributions = []
    for subset in ["FD001","FD003"]:
        lives = complete_labels(read_inputs("train",subset)).groupby("unit").end.first()
        distributions.append({"subset":subset,"engines":len(lives),"minimum":int(lives.min()),
                              "median":float(lives.median()),"mean":float(lives.mean()),"maximum":int(lives.max())})
    last = all_predictions.query("dataset in ['official','transfer_official']").groupby(["dataset","family","unit"]).tail(1).copy()
    last["rul_band"] = pd.cut(last.actual_rul,[-.001,30,60,90,np.inf],labels=["0–30","31–60","61–90",">90"])
    bands = []
    for (dataset,family,band), g in last.groupby(["dataset","family","rul_band"],observed=True):
        error = g.predicted_rul-g.actual_rul
        bands.append({"dataset":dataset,"family":family,"rul_band":band,"engines":len(g),
                      "rmse":float(np.sqrt(np.mean(error**2))),"mae":float(abs(error).mean()),"mean_error":float(error.mean())})
    frames = {"predictions":all_predictions,"metrics_per_engine":metrics,"summary":summary,
              "selection":pd.DataFrame(selections),"empirical_coefficients":pd.DataFrame(coefficients),
              "sensor_ranking":pd.DataFrame(channels),"shape_metrics":pd.DataFrame(shapes),
              "bootstrap":bootstrap,"official_label_audit":label_audit(official),
              "life_distribution":pd.DataFrame(distributions),"official_rul_bands":pd.DataFrame(bands)}
    for name, frame in frames.items():
        frame.to_csv(OUT / f"{name}.csv",index=False)
    (OUT / "splits.json").write_text(json.dumps({"cv":splits,"official_training":final},indent=2),encoding="utf-8")
    fig, axes = plt.subplots(2,3,figsize=(13,7),sharey=True)
    for row, (refit_set,transfer_set) in enumerate([("cv","transfer_complete"),("official","transfer_official")]):
        for ax,unit in zip(axes[row],[1,2,3]):
            for family,color in zip(p05.FAMILIES,["C0","C1","C2"]):
                for dataset,style in [(refit_set,"-"),(transfer_set,"--")]:
                    g = all_predictions.query("dataset == @dataset and family == @family and unit == @unit")
                    ax.plot(g.cycle,g.hi,style,color=color,label=f"{family} {'reajuste' if style == '-' else 'transferência'}")
            ax.set(title=f"FD003 {'completo' if row == 0 else 'truncado'}: motor {unit}",xlabel="Ciclo",ylim=(-.03,1.03))
        axes[row,0].set_ylabel("HI estimado")
    axes[0,2].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(OUT / "HI_transfer_refit.png",dpi=160)
    plt.close(fig)
    lines = ["# P06 — transferência FD001→FD003 e reajuste", "",
             "Extensão de robustez autorizada pelo autor; sem inspeções. FD003 tem uma condição operacional e dois modos de degradação segundo o readme. A AAKR é adaptação do núcleo terminal, não reprodução integral do artigo de Baraldi.","",
             "## Teste oficial FD003 — mesmos 100 motores", "",
             "Transferência mantém os modelos/conversores FD001 congelados; reajuste aprende apenas em treino FD003 e seleciona antes de avaliar os rótulos oficiais.","",
             "| Família | RMSE transferência | RMSE reajuste | MAE transferência | MAE reajuste |","|---|---|---|---|---|"]
    for family in p05.FAMILIES:
        a = summary.query("dataset == 'transfer_official' and family == @family").iloc[0]
        b = summary.query("dataset == 'official' and family == @family").iloc[0]
        lines.append(f"| {family} | {a.last_rmse:.2f} | {b.last_rmse:.2f} | {a.last_mae:.2f} | {b.last_mae:.2f} |")
    lines += ["","Unidade dos erros: ciclos de RUL no último ponto disponível; não erro contra HI físico.","","## Incerteza descritiva pareada","",
              "Contraste refit_minus_transfer: RMSE do reajuste menos transferência, nos mesmos motores. alternative_minus_margin: alternativa menos controle dentro do reajuste. Valores negativos favorecem o primeiro termo.",""]
    for r in bootstrap.itertuples():
        lines.append(f"- {r.contrast}, {r.family}: {r.difference:.2f}; percentis 2,5%–97,5% [{r.p025:.2f}; {r.p975:.2f}].")
    lines += ["","## Trajetórias completas FD003","",
              "cv usa avaliação por motor após reajuste; transfer_complete aplica os modelos FD001 às 100 trajetórias completas FD003, sem reajuste.","",
              "| Dados | Família | RMSE cortes | HI terminal mediano | Passagens/100 | Antecipação mediana | Máxima | Recuperações |","|---|---|---|---|---|---|---|---|"]
    for r in summary.query("dataset in ['cv','transfer_complete']").itertuples():
        lines.append(f"| {r.dataset} | {r.family} | {r.cuts_rmse:.2f} | {r.last_hi_median:.4f} | {r.zero_engines} | {r.median_zero_lead:.1f} | {r.max_zero_lead:.1f} | {r.recoveries} |")
    lines += ["","As antecipações são condicionais a haver passagem por zero. Ausências permanecem censuradas, sem imputar F posterior. As trajetórias completas de cada contraste usam os mesmos motores FD003; seus modelos têm fontes/partições de ajuste diferentes.","",
              "## Escolhas internas finais","",
              *[f"- {f}: {s['candidate']}; RMSE de seleção {s['key'][0]:.2f}." for f,s in selected.items()],"",
              "## Distribuição das vidas completas","",
              *[f"- {d['subset']}: mínimo {d['minimum']}, mediana {d['median']:g}, média {d['mean']:.2f}, máximo {d['maximum']} ciclos." for d in distributions],"",
              "## Limites e consequência científica","",
              "Os modos e a distribuição de vidas mudam entre subconjuntos; não atribuir diferenças exclusivamente ao segundo mecanismo. Não há aqui rótulo independente do mecanismo dominante por motor para estratificar resultados. IDs iguais em FD001 e FD003 não identificam o mesmo motor.","",
              "RUL verdadeira não identifica univocamente o HI físico. Bons erros de prognóstico não tornam o primeiro zero de HI um limite físico, e âncoras aprendidas podem antecipar ou não atingir zero. Na transferência, a referência inicial própria no ciclo 20 é calculada causalmente conforme a fórmula original; não há reaprendizagem de coeficientes, escala da frota ou conversor em FD003.","",
              "As grelhas de P05 permaneceram fixas, inclusive a escala do alvo de RUL do HI empírico. Diferenças de desempenho podem refletir necessidade de calibração, inadequação da representação ou mudança do domínio; esta rodada não separa todas essas causas. Não se escolheu um vencedor ou modificou método pelos resultados oficiais.","",
              "O teste FD003 passa a ser dado já examinado para futuras adaptações. Inspeções e protocolo principal continuam adiados/abertos. Artefatos: modelos por fold/finais, seleções, pesos/rankings, curvas por ciclo, métricas por motor, bootstrap, distribuição de vidas, faixas de RUL, auditoria de rótulos, figura, metadados e manifesto."]
    (OUT / "relatorio.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
    assert hashlib.sha256(SOURCE_MODELS.read_bytes()).hexdigest() == source_hash
    sources = [Path(__file__),ROOT / "experiments/protocolo_piloto_fd003_06.md",
               ROOT / "experiments/test_pilot_fd003_06.py",ROOT / "experiments/pilot_fd001_05.py",
               ROOT / "experiments/pilot_fd001_04.py",ROOT / "experiments/pilot_fd001.py",SOURCE_MODELS,splits_file,
               ROOT / "CMAPSSData/train_FD003.txt",ROOT / "CMAPSSData/test_FD003.txt",
               ROOT / "CMAPSSData/RUL_FD003.txt",ROOT / "CMAPSSData/readme.txt"]
    meta = {"timestamp_utc":datetime.now(timezone.utc).isoformat(),"seed":SEED,"target_subset":"FD003",
            "source_subset":"FD001","source_models_sha256":source_hash,
            "target_models_sha256_before_official_labels":final_hash,"refitting_grid":"Unchanged P05",
            "source_hashes":{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
            "versions":{n:importlib.metadata.version(n) for n in ["numpy","pandas","scipy","scikit-learn","matplotlib"]}}
    (OUT / "metadata.json").write_text(json.dumps(meta,indent=2),encoding="utf-8")
    manifest = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir()) if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    print(summary.to_string(index=False),flush=True)


if __name__ == "__main__":
    with threadpool_limits(limits=2):
        run()
