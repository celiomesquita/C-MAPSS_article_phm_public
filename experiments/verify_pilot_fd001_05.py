"""Reconstruct P05 outputs from frozen models and validate the reported comparison."""

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.isotonic import IsotonicRegression
from threadpoolctl import threadpool_limits

from pilot_fd001 import ROOT, SEED, read_data
from pilot_fd001_04 import centred_sensors
from pilot_fd001_05 import (OUT, attach_official_labels, cut_rmse, equal_engine_weights,
                            predict_hi, read_official_inputs, standardise)


def verify():
    # Verify the archived state before adding diagnostic files.
    prior_manifest = (OUT / "manifest.json").read_bytes()
    for name in ["pilot_fd001_01", "pilot_fd001_02", "pilot_fd001_03", "pilot_fd001_04", "pilot_fd001_05"]:
        directory = ROOT / "experiments/artifacts" / name
        manifest = json.loads((directory / "manifest.json").read_text())
        for filename, digest in manifest.items():
            assert hashlib.sha256((directory / filename).read_bytes()).hexdigest() == digest, (name, filename)
    metadata = json.loads((OUT / "metadata.json").read_text())
    for filename, digest in metadata["source_hashes"].items():
        assert hashlib.sha256((ROOT / filename).read_bytes()).hexdigest() == digest, filename
    freeze = json.loads((OUT / "official_freeze.json").read_text())
    assert hashlib.sha256((OUT / "models_official.json").read_bytes()).hexdigest() == freeze["models_sha256"]
    splits = json.loads((OUT / "splits.json").read_text())
    data = read_data()
    official_inputs = read_official_inputs()
    labels = np.loadtxt(ROOT / "CMAPSSData/RUL_FD001.txt")
    official = attach_official_labels(official_inputs, labels)
    saved = pd.read_csv(OUT / "predictions.csv")
    choices = pd.read_csv(OUT / "selection.csv")
    for split in splits["cv"]:
        groups = sum([split[k] for k in ["fit", "calibration", "selection", "evaluation"]], [])
        assert len(groups) == len(set(groups)) == 100
    final_groups = sum([splits["official_training"][k] for k in ["fit", "calibration", "selection"]], [])
    assert len(final_groups) == len(set(final_groups)) == 100
    max_error = 0.
    for run_name in [f"fold{k}" for k in range(1,6)]+["official"]:
        partition = splits["official_training"] if run_name == "official" else splits["cv"][int(run_name[-1])-1]
        models = json.loads((OUT / f"models_{run_name}.json").read_text())
        for family, detail in models.items():
            records = choices.query("run == @run_name and family == @family")
            best = records.sort_values(["selection_rmse", "candidate"]).iloc[0]
            assert best.candidate == detail["candidate"] and records.chosen.sum() == 1
            assert records.loc[records.chosen, "candidate"].iloc[0] == best.candidate
            stats = {"channels": detail["sensors"], "direction": np.asarray(detail["direction"]),
                     "scale": np.asarray(detail["scale"])}
            if family == "MARGEM":
                model = pd.DataFrame(detail["reference"])
            elif family == "EMPIRICO":
                model = np.asarray(detail["coefficients"])
                assert (model >= 0).all()
            else:
                model = detail["model"].copy()
                for key in ["columns", "bank", "bank_units", "spread", "loo_terminal_residuals"]:
                    model[key] = np.asarray(model[key])
                assert set(model["bank_units"]) == set(partition["fit"])
            centred_train = centred_sensors(data)
            z_train = standardise(centred_train, stats)
            hi_train = predict_hi(data, centred_train, z_train, family, model)
            cal = data.unit.isin(partition["calibration"]) & (data.cycle >= 20)
            converter = IsotonicRegression(increasing=True,y_min=0.,out_of_bounds="clip")
            converter.fit(hi_train[np.asarray(cal)], data.loc[cal,"rul"],
                          sample_weight=equal_engine_weights(data.loc[cal,"unit"]))
            np.testing.assert_allclose(converter.X_thresholds_,detail["converter_hi"])
            np.testing.assert_allclose(converter.y_thresholds_,detail["converter_rul"])
            selection_mask = data.unit.isin(partition["selection"]) & (data.cycle >= 20)
            selection_pred = np.full(len(data),np.nan)
            selection_pred[np.asarray(selection_mask)] = converter.predict(hi_train[np.asarray(selection_mask)])
            np.testing.assert_allclose(cut_rmse(data,selection_pred,partition["selection"]),detail["selection_rmse"])
            query = official_inputs if run_name == "official" else data.drop(columns=["end","rul"])
            centred = centred_sensors(query)
            hi = predict_hi(query,centred,standardise(centred,stats),family,model)
            ids = sorted(query.unit.unique()) if run_name == "official" else partition["evaluation"]
            mask = query.unit.isin(ids) & (query.cycle >= 20)
            expected = saved.query("run == @run_name and family == @family").sort_values(["unit","cycle"])
            np.testing.assert_array_equal(query.loc[mask,"unit"],expected.unit)
            np.testing.assert_array_equal(query.loc[mask,"cycle"],expected.cycle)
            np.testing.assert_allclose(hi[np.asarray(mask)],expected.hi,atol=1e-10)
            predictions = converter.predict(hi[np.asarray(mask)])
            np.testing.assert_allclose(predictions,expected.predicted_rul,atol=1e-9)
            truth = official if run_name == "official" else data
            np.testing.assert_allclose(truth.loc[mask,"rul"],expected.actual_rul)
            max_error = max(max_error,float(np.max(abs(predictions-expected.predicted_rul.to_numpy()))))
    last = saved.sort_values("cycle").groupby(["dataset","family","unit"]).tail(1).copy()
    summary = pd.read_csv(OUT / "summary.csv")
    for (dataset,family), group in last.groupby(["dataset","family"]):
        assert len(group)==100
        row = summary.query("dataset == @dataset and family == @family").iloc[0]
        errors = group.predicted_rul-group.actual_rul
        np.testing.assert_allclose(np.sqrt(np.mean(errors**2)),row.last_rmse)
        np.testing.assert_allclose(np.mean(abs(errors)),row.last_mae)
    official_last = last.query("dataset == 'official'").copy()
    for family,g in official_last.groupby("family"):
        np.testing.assert_allclose(g.sort_values("unit").actual_rul,labels)
    official_last["rul_band"] = pd.cut(official_last.actual_rul,[-.001,30,60,90,np.inf],
                                         labels=["0–30","31–60","61–90",">90"])
    bins = []
    for (family,band),g in official_last.groupby(["family","rul_band"],observed=True):
        error = g.predicted_rul-g.actual_rul
        bins.append({"family":family,"rul_band":band,"engines":len(g),
                     "rmse":float(np.sqrt(np.mean(error**2))),"mae":float(np.mean(abs(error))),
                     "mean_error":float(error.mean())})
    pd.DataFrame(bins).to_csv(OUT / "official_rul_bands.csv",index=False)
    # Independently reproduce the paired bootstrap on last-observation errors.
    official_last["error"] = official_last.predicted_rul-official_last.actual_rul
    errors = official_last.pivot(index="unit",columns="family",values="error")
    samples = np.random.default_rng(SEED).integers(0,100,(2000,100))
    bootstrap = pd.read_csv(OUT / "bootstrap.csv")
    for family in ["EMPIRICO","AAKR"]:
        difference = np.sqrt(np.mean(errors[family].to_numpy()[samples]**2,axis=1))-np.sqrt(np.mean(errors.MARGEM.to_numpy()[samples]**2,axis=1))
        row=bootstrap.query("family == @family").iloc[0]
        np.testing.assert_allclose(np.quantile(difference,[.025,.975]),[row.p025,row.p975])
    conclusions = """# P05 — interpretação dos resultados

O uso correto de RUL_FD001 possibilitou uma avaliação adicional nos 100 motores de teste, com rótulos posteriores ao último ciclo observado e sem sensores futuros. O [relatório](relatorio.md) apresenta a comparação completa; [faixas de RUL](official_rul_bands.csv) separam antecipação e sobrestimação nas diferentes regiões.

O RMSE oficial foi 28,85 ciclos no controle de margens, 27,66 na fórmula empírica e 27,57 na adaptação AAKR. As diferenças relativamente ao controle foram −1,19 e −1,28 ciclos; os intervalos descritivos pareados incluíram zero. A rodada não distingue superioridade conclusiva, e a diferença entre empírico e AAKR é pequena nesta amostra. Não se escolheu um vencedor pelo resultado oficial.

No ajuste final, a fórmula empírica selecionada internamente foi Ĥ=clip[1−max(0,Σ_j w_j d_j(x̄_ij−b_ij)/s_j),0,1], com pesos não negativos e alvo de treino min(1,RUL/100). A penalização dos pesos foi 0,1. Os pesos/direções/escalas e o conversor são os arquivados em models_official.json; o alvo é convencional e não HI físico. As configurações selecionadas variam entre folds, como registrado em selection.csv.

Nas trajetórias completas avaliadas por motor, o HI empírico zerou em 71/100, com antecedência mediana de 14 ciclos e máxima de 49 entre passagens, sem recuperação posterior. A adaptação AAKR zerou em 92/100, com antecedência mediana de 18,5 ciclos, máxima de 64 e 43 recuperações. Esses resultados impedem identificar diretamente o primeiro zero com F. No teste oficial houve zeros antes do truncamento em seis motores com a fórmula empírica e nove com AAKR; todos ainda tinham RUL positiva no último ciclo observado.

A contribuição desta rodada é tornar a formulação empírica estimável e comparável sob referências temporais independentes, identificando seus limites. O próximo protocolo deverá separar a estimação contínua de condição da previsão de primeira passagem e avaliar heterogeneidade terminal/ruído, sem forçar o ponto zero com a vida futura do próprio motor. Uma reprodução integral do estudo publicado requer preservar também seus componentes de extração e busca de atributos; esta rodada avaliou uma adaptação do núcleo terminal. Inspeções continuam adiadas.
"""
    (OUT / "conclusoes.md").write_text(conclusions,encoding="utf-8")
    verification={"checks":["P01–P05 manifests","source hashes","frozen official model hash",
                             "partitions","internal configuration choices","all saved HI and RUL predictions",
                             "calibration converter refits","selection losses","official RUL alignment",
                             "aggregate errors","paired bootstrap"],
                  "max_reconstruction_error":max_error,
                  "prior_manifest_sha256":hashlib.sha256(prior_manifest).hexdigest(),
                  "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT / "verification.json").write_text(json.dumps(verification,indent=2),encoding="utf-8")
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir())
              if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    print(json.dumps(verification,indent=2))


if __name__ == "__main__":
    with threadpool_limits(limits=2):
        verify()
