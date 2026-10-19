"""P06: reconstruct transfer/refit predictions and verify comparative evidence."""

import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.isotonic import IsotonicRegression
from threadpoolctl import threadpool_limits

import pilot_fd001_05 as p05
from pilot_fd001 import ROOT, SEED
from pilot_fd003_06 import OUT, SOURCE_MODELS, complete_labels, load_models, read_inputs


def verify():
    previous_manifest = (OUT / "manifest.json").read_bytes()
    for name in ["pilot_fd001_01","pilot_fd001_02","pilot_fd001_03","pilot_fd001_04","pilot_fd001_05","pilot_fd003_06"]:
        directory = ROOT / "experiments/artifacts" / name
        for file,digest in json.loads((directory / "manifest.json").read_text()).items():
            assert hashlib.sha256((directory / file).read_bytes()).hexdigest() == digest,(name,file)
    meta = json.loads((OUT / "metadata.json").read_text())
    for file,digest in meta["source_hashes"].items():
        assert hashlib.sha256((ROOT / file).read_bytes()).hexdigest() == digest,file
    freeze = json.loads((OUT / "official_freeze.json").read_text())
    assert hashlib.sha256(SOURCE_MODELS.read_bytes()).hexdigest() == freeze["source_models_sha256"]
    assert hashlib.sha256((OUT / "models_official.json").read_bytes()).hexdigest() == freeze["refit_models_sha256"]
    data = complete_labels(read_inputs("train"))
    test_inputs = read_inputs("test")
    labels = np.loadtxt(ROOT / "CMAPSSData/RUL_FD003.txt")
    test = p05.attach_official_labels(test_inputs,labels)
    splits = json.loads((OUT / "splits.json").read_text())
    saved = pd.read_csv(OUT / "predictions.csv")
    selections = pd.read_csv(OUT / "selection.csv")
    all_evaluation = []
    maximum_error = 0.
    for name in [f"fold{i}" for i in range(1,6)]+["official","transfer"]:
        models = load_models(SOURCE_MODELS if name == "transfer" else OUT / f"models_{name}.json")
        partition = None
        if name != "transfer":
            partition = splits["official_training"] if name == "official" else splits["cv"][int(name[-1])-1]
            groups = [partition[k] for k in ["fit","calibration","selection"]]
            if name != "official":
                groups.append(partition["evaluation"])
                all_evaluation.extend(partition["evaluation"])
            ids = sum(groups,[])
            assert len(ids) == len(set(ids)) == 100
        for family, chosen in models.items():
            if partition is not None:
                rows = selections.query("run == @name and family == @family")
                expected = rows.sort_values(["selection_rmse","candidate"]).iloc[0]
                assert chosen["candidate"] == expected.candidate
                assert rows.chosen.sum()==1 and rows.loc[rows.chosen,"candidate"].iloc[0] == expected.candidate
                cal_output = p05.transform_selected(data.drop(columns=["end","rul"]),chosen,family)
                cal = cal_output.unit.isin(partition["calibration"])
                converter = IsotonicRegression(increasing=True,y_min=0.,out_of_bounds="clip")
                converter.fit(cal_output.loc[cal,"hi"],data.loc[cal_output.loc[cal].index,"rul"],
                              sample_weight=p05.equal_engine_weights(cal_output.loc[cal,"unit"]))
                np.testing.assert_allclose(converter.X_thresholds_,chosen["converter"].X_thresholds_)
                np.testing.assert_allclose(converter.y_thresholds_,chosen["converter"].y_thresholds_)
                prediction = np.full(len(data),np.nan)
                prediction[cal_output.index] = cal_output.predicted_rul
                np.testing.assert_allclose(p05.cut_rmse(data,prediction,partition["selection"]),chosen["key"][0])
                if family == "AAKR":
                    assert set(chosen["model"]["bank_units"]) == set(partition["fit"])
                if family == "EMPIRICO":
                    assert (chosen["model"] >= 0).all()
            datasets = ["transfer_complete","transfer_official"] if name == "transfer" else ["official" if name == "official" else "cv"]
            for dataset in datasets:
                truth = test if dataset in ["official","transfer_official"] else data
                inputs = truth.drop(columns=["end","rul"])
                output = p05.transform_selected(inputs,chosen,family)
                if dataset == "cv":
                    output = output.loc[output.unit.isin(partition["evaluation"])]
                archived = saved.query("run == @name and family == @family and dataset == @dataset").sort_values(["unit","cycle"])
                np.testing.assert_array_equal(output.unit,archived.unit)
                np.testing.assert_array_equal(output.cycle,archived.cycle)
                np.testing.assert_allclose(output.hi,archived.hi,atol=1e-10)
                np.testing.assert_allclose(output.predicted_rul,archived.predicted_rul,atol=1e-9)
                np.testing.assert_allclose(truth.loc[output.index,"rul"],archived.actual_rul)
                maximum_error = max(maximum_error,float(np.max(abs(output.predicted_rul.to_numpy()-archived.predicted_rul.to_numpy()))))
    assert sorted(all_evaluation) == list(range(1,101))
    metrics = pd.read_csv(OUT / "metrics_per_engine.csv")
    for (dataset,family,unit),g in saved.groupby(["dataset","family","unit"]):
        row = metrics.query("dataset == @dataset and family == @family and unit == @unit").iloc[0]
        error = g.predicted_rul-g.actual_rul
        np.testing.assert_allclose(row.history_rmse,np.sqrt(np.mean(error**2)))
        np.testing.assert_allclose(row.last_error,error.iloc[-1])
        zero = g.loc[g.hi <= 0,"cycle"]
        assert row.has_zero == bool(len(zero))
        first = float(zero.iloc[0]) if len(zero) else np.nan
        np.testing.assert_allclose(row.first_zero,first,equal_nan=True)
        recovery = bool((g.loc[g.cycle > first,"hi"] > 1e-12).any())
        assert row.recovered_after_zero == recovery
        if dataset in ["cv","transfer_complete"]:
            cuts = g.cycle.isin([int(np.floor(f*g.end.iloc[0])) for f in [.5,.7,.9]])
            np.testing.assert_allclose(row.cuts_mse,np.mean(error.loc[cuts]**2))
    summary = pd.read_csv(OUT / "summary.csv")
    for (dataset,family),g in metrics.groupby(["dataset","family"]):
        row = summary.query("dataset == @dataset and family == @family").iloc[0]
        assert len(g)==g.unit.nunique()==row.engines==100
        np.testing.assert_allclose(row.last_rmse,np.sqrt(np.mean(g.last_error**2)))
        np.testing.assert_allclose(row.last_mae,abs(g.last_error).mean())
        assert row.zero_engines == g.has_zero.sum()
        assert row.recoveries == g.recovered_after_zero.sum()
    errors = metrics.query("dataset in ['official','transfer_official']").pivot(index="unit",columns=["dataset","family"],values="last_error")
    samples = np.random.default_rng(SEED).integers(0,100,(2000,100))
    bootstrap = pd.read_csv(OUT / "bootstrap.csv")
    for row in bootstrap.itertuples():
        aa = errors["official",row.family].to_numpy()
        bb = errors["transfer_official",row.family].to_numpy() if row.contrast == "refit_minus_transfer" else errors["official","MARGEM"].to_numpy()
        difference = np.sqrt(np.mean(aa[samples]**2,axis=1))-np.sqrt(np.mean(bb[samples]**2,axis=1))
        np.testing.assert_allclose(np.quantile(difference,[.025,.975]),[row.p025,row.p975])
    audit = pd.read_csv(OUT / "official_label_audit.csv").sort_values("unit")
    np.testing.assert_allclose(audit.last_rul,labels)
    np.testing.assert_allclose(audit.last_observed+audit.last_rul,audit.endpoint)
    conclusions = """# P06 — interpretação e decisão

A avaliação em FD003 distinguiu transferência direta dos modelos FD001 de reajuste da mesma formulação em FD003. No teste oficial, o RMSE da fórmula empírica passou de 79,56 para 23,40 ciclos; a adaptação AAKR passou de 80,25 para 26,41, e o controle de margens de 38,58 para 32,41. Os intervalos descritivos pareados dessas mudanças excluíram zero. O resultado sustenta dependência dos parâmetros/conversor em relação ao domínio, sem isolar qual componente produz o ganho do reajuste.

Após reajuste em FD003, a fórmula empírica teve RMSE 23,40 contra 32,41 do controle; a diferença foi −9,00 ciclos, com intervalo descritivo [−14,11;−3,63]. A adaptação AAKR teve RMSE 26,41 e diferença −6,00 [−10,97;−0,89]. A comparação refere-se a estas implementações e ao teste FD003; não constitui superioridade universal ou reprodução integral do estudo publicado.

A ancoragem terminal ainda não foi resolvida. Nos motores completos avaliados fora do ajuste, o HI empírico chegou a zero em 46/100, com antecipação mediana de cinco ciclos entre passagens; 54 não chegaram a zero, HI terminal mediano 0,0163 e nenhuma recuperação depois do primeiro zero. A AAKR chegou a zero em 82/100, com antecipação mediana 18 e 52 recuperações. No teste truncado, a fórmula empírica reajustada não zerou em nenhum motor, mas isso não prova ancoragem em F: os sensores terminais não estão disponíveis ali.

A distribuição de vidas também muda: a mediana completa é 199 ciclos em FD001 e 220,5 em FD003, e o máximo passa de 362 para 525. Não atribuir a perda de transferência apenas ao segundo mecanismo. Os arquivos usados não fornecem classificação independente de qual mecanismo domina cada motor. O exemplo do motor FD003 2 mostra que uma representação transferida pode continuar com HI alto até o endpoint; a heterogeneidade dos padrões de sensores merece investigação específica.

P06 fortalece o uso da fórmula empírica como candidata recalibrável, mas não justifica adotá-la como HI físico ou identificar seu primeiro zero com F. O próximo contraste deve distinguir deslocamento da representação de condição de deslocamento do conversor HI→RUL, examinando os motores com condição terminal mal representada. FD003 agora foi avaliado e deve ser tratado como dado já examinado em futuras adaptações. Inspeções continuam adiadas.

O [relatório](relatorio.md) reúne tabelas e limitações; a [figura](HI_transfer_refit.png) usa motores 1/2/3 fixados previamente. Verificações estão em verification.json; modelos, métricas individuais e seleções permanecem arquivados.
"""
    (OUT / "conclusoes.md").write_text(conclusions,encoding="utf-8")
    checks = {"checks":["P01–P06 manifests","source hashes","source and target model freeze hashes",
                         "partitions and engine coverage","internal selections and converter refits",
                         "all transfer/refit HI and RUL predictions","per-engine errors and zero events",
                         "aggregate metrics","paired bootstrap","official label alignment"],
              "maximum_reconstruction_error":maximum_error,
              "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "previous_manifest_sha256":hashlib.sha256(previous_manifest).hexdigest()}
    (OUT / "verification.json").write_text(json.dumps(checks,indent=2),encoding="utf-8")
    manifest = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir()) if p.is_file() and p.name != "manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    print(json.dumps(checks,indent=2))


if __name__ == "__main__":
    with threadpool_limits(limits=2):
        verify()
