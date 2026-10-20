# Calibration, reserve and source-provenance checks (20 October 2026)

This post-confirmation analysis separates two policy choices in archived ISO decisions:
nominal calibration 98%/95% and reserve 15/12, in FD001 and FD003, for execution
leads 1 and 2 and three repetitions. It reuses the same 100 engines per subset.
The 4,800 decisions and 1,200 marker records are repeated evaluations, not
independent engines. No models are refitted and no new removal policy is selected.

With Python 3.10+ (standard library only), from the repository root:

```text
python experiments/sa3_20261020/reproduce.py --output /path/to/new_output
python experiments/sa3_20261020/verify.py --output /path/to/new_output
```

The 48 cells reproduce the archived summaries; 72 contrasts separate calibration,
reserve and their interaction. All four combinations had no observed endpoint
events in these development engines. This does not establish population-risk
equivalence. `reference/` stores the exact CSV outputs used for the paper.
Ranges over repetitions and leads are descriptive, not confidence intervals.
`input_provenance.json` records selection from the original archived inputs;
`source_adaptation.json` documents the portable adaptation of the analysis script.
No raw NASA trajectories, model binaries or private repository are needed.

Both factors increase utilised life; the positive interaction prevents assigning
the combined gain to calibration alone. The combined gain over the marker is
2.4--7.0 mean cycles across both leads (3.2--7.0 for lead 1 only). The supplement
reports the separate contrasts in S9.

The public P10 source also resolves the historical source-hash discrepancy.
Its LF-normalised SHA-256 is `bec9cf1780e1bfa142a58b1080d8d52fe8ab4b2c00087f0ba11d10c54ab8e131`.
The historical representation uses CRLF throughout except LF on line 286;
reconstruction gives `2d99ce838a9164282949fb4f88642675b354caead3e50bd316b4d0caae231d92`.
This is a byte-representation difference, not a change in scientific code.
The verifier checks this reconstruction without changing the source.

The economic conclusions remain conditional on the inspection generator and costs:
in the evaluated FD001--FD003 engines, inspection on conservative ISO adds
restorations without reducing observed events. This is empirical dominance in
that scenario, without evidence of exactly zero population benefit. FD004 has
contrasts with statistically unbounded break-even thresholds.
