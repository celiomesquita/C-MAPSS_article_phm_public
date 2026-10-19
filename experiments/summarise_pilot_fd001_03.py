"""Verify P03 outputs and report robustness without choosing an outer winner."""

import hashlib
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pilot_fd001_02 import margins, md_table
from pilot_fd001_03 import OUT, ROOT


def run():
    meta = json.loads((OUT / "metadata.json").read_text())
    assert hashlib.sha256((ROOT / "CMAPSSData/train_FD001.txt").read_bytes()).hexdigest() == meta["data_sha256"]
    for relative, digest in meta["source_hashes"].items():
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == digest
    pred = pd.read_csv(OUT / "predictions.csv")
    detections = pd.read_csv(OUT / "detections.csv")
    choices = pd.read_csv(OUT / "detector_selection.csv")
    decisions = pd.read_csv(OUT / "decisions_per_engine.csv")
    calibration = pd.read_csv(OUT / "margins.csv")
    hi = pd.read_csv(OUT / "hi_trajectories.csv")
    hm = pd.read_csv(OUT / "hi_metrics.csv")
    splits = json.loads((OUT / "splits.json").read_text())
    assert not pred.duplicated(["fold","model","role","unit","cycle"]).any()
    assert not detections.duplicated(["config","unit"]).any()
    assert len(detections) == 1800
    assert not decisions.duplicated(["config","model","variant","unit"]).any()
    assert not hi.duplicated(["quantile","unit","cycle"]).any()
    assert np.allclose(hi.loc[hi.cycle == 20,"hi"],1.)
    assert hi.hi.between(0,1).all()
    assert (pred.rul == pred.end-pred.cycle).all()
    for split in splits:
        fold = split["fold"]
        groups = [set(split[r]) for r in ["fit","calibration","selection","evaluation"]]
        assert [len(g) for g in groups] == [40,20,20,20] and len(set.union(*groups)) == 100
        for role in ["calibration","selection","evaluation"]:
            assert set(pred.loc[(pred.fold==fold)&(pred.role==role),"unit"]) == set(split[role])
        for model in pred.model.unique():
            cal = pred.loc[(pred.fold==fold)&(pred.model==model)&(pred.role=="calibration")]
            calculated = margins(cal)
            saved = calibration.loc[(calibration.fold==fold)&(calibration.model==model)].iloc[0]
            assert np.isclose(calculated["global_margin"],saved.global_margin)
            if calculated["local_margin"] is not None:
                assert np.isclose(calculated["local_margin"],saved.local_margin)
        for config,g in choices.loc[choices.fold==fold].groupby("config"):
            feasible = g.loc[g.early_count<=2]
            eligible = feasible if len(feasible) else g
            cols = ["coverage","median_lead","threshold"] if len(feasible) else ["early_count","coverage","median_lead","threshold"]
            ascending = [False,False,True] if len(feasible) else [True,False,False,True]
            expected = eligible.sort_values(cols,ascending=ascending,kind="stable").iloc[0].candidate
            assert g.loc[g.chosen,"candidate"].tolist()==[expected]
    baseline = detections.loc[detections.config=="B0_40_w_15_d_3"].set_index("unit").sort_index()
    p02 = pd.read_csv(ROOT / "experiments/artifacts/pilot_fd001_02/detections.csv").set_index("unit").sort_index()
    np.testing.assert_allclose(baseline.p,p02.p,equal_nan=True)
    for key,g in decisions.groupby(["fold","model","variant"]):
        assert g.margin.nunique()==1
    action_span = decisions.groupby(["model","variant","unit"]).removal.nunique()
    max_distinct_actions = int(action_span.max())
    for (fold,model,config,variant),g in decisions.groupby(["fold","model","config","variant"]):
        p = detections.loc[detections.config==config].set_index("unit").p
        source = pred.loc[(pred.fold==fold)&(pred.model==model)&(pred.role=="evaluation")].copy()
        active = source.cycle >= source.unit.map(p)
        hit = (source.raw-g.margin.iloc[0]).clip(lower=0)<=10
        if variant=="local_gate30": hit &= source.raw<=30
        first = source.loc[active&hit].groupby("unit").cycle.min()
        expected = g.unit.map(first).fillna(g.end).to_numpy()
        np.testing.assert_allclose(g.removal,expected)
    detections["lead"] = detections.end-detections.p
    detections["early_40"] = detections.p<=40
    detections["early_b0"] = detections.p<=detections.b0
    detection_summary = detections.groupby(["config","b0","window","persistence"]).agg(
        engines=("unit","size"), detected=("p","count"), median_P=("p","median"),
        early_40=("early_40","sum"), early_b0=("early_b0","sum"), median_lead=("lead","median")).reset_index()
    decision_summary = decisions.groupby(["config","model","variant"]).agg(
        engines=("unit","size"), endpoints=("endpoint","sum"), mean_unused=("unused","mean")).reset_index()
    assert (decision_summary.engines==100).all()
    policy_ranges = decision_summary.groupby(["model","variant"]).agg(
        min_endpoints=("endpoints","min"), max_endpoints=("endpoints","max"),
        min_unused=("mean_unused","min"),max_unused=("mean_unused","max")).reset_index()
    pspan = detections.groupby("unit").agg(configs_detected=("p","count"),min_P=("p","min"),max_P=("p","max"))
    pspan["span"] = pspan.max_P-pspan.min_P
    hm["lead_HI"] = hm.end-hm.estimated_F
    hm["before_earliest_P"] = hm.estimated_F<hm.earliest_P
    endpoint_zero = hm.endpoint_hi<=0
    hm["zero_at_endpoint"] = endpoint_zero
    recoveries = hi.groupby(["quantile","unit"]).hi.apply(lambda s: bool(((s.shift(1)<=0)&(s>0)).any()))
    hm["recovers_after_zero"] = [recoveries.loc[q,u] for q,u in zip(hm["quantile"],hm.unit)]
    hi_summary = hm.groupby("quantile").agg(
        engines=("unit","size"), zero_crossings=("estimated_F","count"),
        median_endpoint_HI=("endpoint_hi","median"),zero_at_endpoint=("zero_at_endpoint","sum"),
        median_lead_HI=("lead_HI","median"),min_lead_HI=("lead_HI","min"),
        max_lead_HI=("lead_HI","max"),before_earliest_P=("before_earliest_P","sum"),
        recovers_after_zero=("recovers_after_zero","sum")).reset_index()
    for name,frame in [("detector_summary",detection_summary),("decision_summary",decision_summary),
                       ("policy_ranges",policy_ranges),("hi_summary",hi_summary)]:
        frame.to_csv(OUT / f"{name}.csv",index=False)
    pspan.to_csv(OUT / "P_span_per_engine.csv")
    fig,ax=plt.subplots(figsize=(12,4.5))
    ordered = detection_summary.sort_values(["b0","window","persistence"])
    groups = [detections.loc[detections.config==c,"p"].dropna().to_numpy() for c in ordered.config]
    ax.boxplot(groups,tick_labels=[f"{r.b0}/{r.window}/{r.persistence}" for r in ordered.itertuples()],showfliers=False)
    ax.set(xlabel="Stable-period end / smoothing window / persistence (cycles)",ylabel="Detected P cycle",
           title="P03: sensitivity of the available statistical alert")
    ax.tick_params(axis="x",rotation=60,labelsize=8)
    fig.tight_layout();fig.savefig(OUT / "P_robustness.png",dpi=170);plt.close(fig)
    fig,axes=plt.subplots(1,3,figsize=(12,3.8))
    for unit,ax in zip([1,2,3],axes):
        for q,g in hi.loc[hi.unit==unit].groupby("quantile"):
            ax.plot(g.cycle,g.hi,label=f"Terminal q={q:g}")
        ax.axvline(baseline.loc[unit,"p"],color="grey",linestyle=":",label="P02/P03 reference P")
        ax.axvline(hi.loc[hi.unit==unit,"end"].iloc[0],color="black",linestyle="--",label="Benchmark endpoint")
        ax.set(title=f"Engine {unit}",xlabel="Cycle",ylim=(-.03,1.03))
    axes[0].set_ylabel("Empirical HI proxy (not physical margin)")
    axes[0].legend(fontsize=6)
    fig.tight_layout();fig.savefig(OUT / "HI_examples.png",dpi=170);plt.close(fig)
    complete=int((pspan.configs_detected==18).sum())
    report=("# P03 — robustez de P e diagnóstico empírico HI/F\n\n"
        "Rodada exploratória, sem inspeções. Cinco folds por motor, grupos 40/20/20/20 de P02. "
        "Foram examinadas 18 configurações com previsões e margem comuns por modelo/fold. "
        "Não se escolheu configuração vencedora com dados externos. O conjunto de treino agora começa "
        "no ciclo 21; diferenças P02/P03 também reflectem essa mudança e não isolam o detector.\n\n"
        "## Robustez da detecção\n\n"+md_table(detection_summary)+"\n\n"
        f"{complete}/100 motores tiveram alerta nas 18 configurações. A amplitude mediana de P "
        f"no mesmo motor foi {pspan.span.median():.1f} ciclos; a maior foi {pspan.span.max():.1f}. "
        "Amplitudes usam os alertas disponíveis; ausência em alguma configuração não é convertida em P=0. "
        "Alertas até 40 usam um horizonte comum; alertas até B0 usam a hipótese própria de cada configuração. "
        "Nenhum desses indicadores constitui acurácia de P físico. A configuração B0=40/w=15/d=3 "
        "reproduz os alertas de P02, verificação de continuidade do detector.\n\n"
        "![Robustez do ciclo de alerta](P_robustness.png)\n\n"
        "## Efeito nas decisões com previsão controlada\n\n"+md_table(policy_ranges)+"\n\n"
        "As amplitudes da tabela são entre as 18 configurações, não intervalos de confiança nem escolha "
        "de configuração. `raw` não tem margem; `local_gate30` usa margem local e região prevista ≤30. "
        "Ambas têm gatilho 10 e acção imediata como cenário. Detecção variável com desfechos estáveis "
        "significa apenas que as alterações antecedem a região decisória na maioria dos casos; não valida P. "
        f"O máximo de ciclos de remoção distintos por motor/modelo/política entre configurações foi {max_distinct_actions}; "
        "nesta rodada, a invariância verificou-se também por motor, não apenas nas médias agregadas.\n\n"
        "## Proxy HI/F\n\n"+md_table(hi_summary)+"\n\n"
        "Direcções e referências terminais foram aprendidas somente nos motores de ajuste. "
        "O HI é 1 no ciclo 20; não foi forçado a zero no endpoint externo nem a decrescer após P. "
        "`median_lead_HI` é endpoint menos primeira passagem do HI por zero; positivo indica antecipação. "
        "Motores sem passagem por zero até o endpoint ficam censurados, não recebem F inventado. "
        "Recuperação após zero indica instabilidade da interpretação de primeira passagem; não é "
        "restauração física. A proxy não foi usada para agir, calibrar RUL ou simular inspeções.\n\n"
        "![HI nos motores 1, 2 e 3, escolhidos antes da execução](HI_examples.png)\n\n"
        "## Limitações e condições para avançar\n\n"
        "As medianas de P variaram de 38 a 82 ciclos entre configurações, apesar das decisões invariantes. "
        "Isso não justifica escolher a configuração mais tardia como fisicamente mais correcta. "
        "A referência terminal mediana produziu 94 passagens por zero, seis ausências, antecipação mediana "
        "de 42,5 ciclos entre as passagens e máxima de 270, com recuperação após zero em 30 motores. "
        "Com quantil 0,90 houve 41 passagens, 59 ausências e antecipação mediana de cinco ciclos entre "
        "as passagens; a mediana de HI no endpoint foi aproximadamente 0,032. Essa proximidade de zero "
        "não demonstra margem física nem define automaticamente a tolerância de F. Preservar os "
        "casos de ausência e recuperação; não escolher normalização por endpoint externo para removê-los.\n\n"
        "O intervalo inicial estável é assumido; não há rótulo independente de P ou margens físicas FD001. "
        "A proxy mínima entre sensores pode antecipar o zero por variabilidade ou por um canal fraco; "
        "um terminal aprendido da frota não garante zero em cada motor. Não congelar a referência "
        "somente porque ela se correlaciona com o endpoint. Verificar mecanismo, canais e robustez "
        "sem normalização pelo endpoint externo. Segurança e antecedência ainda não estão validadas. "
        "Inspeções continuam adiadas até congelamento do protocolo principal.\n\n"
        "## Verificações e artefactos\n\n"
        "[Protocolo](../../protocolo_piloto_fd001_03.md). Partições disjuntas, escolhas de limiares "
        "reproduzidas das tabelas internas, margens recalculadas da calibração, todas as decisões "
        "recalculadas das mesmas previsões, referência de P02 reproduzida e hashes de dados/fontes "
        "verificados. CSVs preservam os resultados completos por motor, configurações e curvas HI. "
        "Nenhum resultado externo foi usado para substituir a escolha interna de limiar.\n")
    (OUT / "relatorio.md").write_text(report,encoding="utf-8")
    verification={"checks_passed":True,"detector_configs":18,"evaluation_engines":100,
                  "max_distinct_removal_cycles_across_configs":max_distinct_actions,
                  "summary_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (OUT / "verification.json").write_text(json.dumps(verification,indent=2),encoding="utf-8")
    manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(OUT.iterdir())
              if p.is_file() and p.name!="manifest.json"}
    (OUT / "manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    print(detection_summary.to_string(index=False))
    print(policy_ranges.to_string(index=False))
    print(hi_summary.to_string(index=False))
    print(f"Median P span={pspan.span.median():.1f}, max={pspan.span.max():.1f}; complete engines={complete}")
    print("P03 artifact verification passed.")


if __name__=="__main__":
    run()
