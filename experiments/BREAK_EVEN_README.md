# Break-even cost of end-of-life events — P21.1 and P21.2

Exploratory analyses carried out after the frozen-protocol confirmation, on archived decisions and exact per-engine expectations only. No sensors are read and no model, margin or removal rule is refitted or selected.

## Question and definitions

Every removal, preventive or following an endpoint arrival, is assumed to cost one overhaul `c_R` (US$6 million) and to return the engine to cycle zero. Per simulated cycle the cost is `c_R (varpi + beta * eta)`, where `varpi` is the restoration rate, `eta` the rate of end-of-life events (strict late schedules, exact arrivals and arrivals without decision) and `beta >= 0` the additional consequence cost of an event in overhaul units. For arms A and B,

```
beta* = (varpi_A - varpi_B) / (eta_B - eta_A)
```

is the value above which A is cheaper than B (below it when both differences are negative). The ratio does not depend on the cycle-to-flight mapping or on the horizon; LLP visits common to all arms cancel. It is a decision threshold, not an estimate of what an event costs, and a C-MAPSS endpoint is exhaustion of an operability margin, not necessarily a catastrophic failure.

P21.2 adds an inspection cost `c_I = q_I c_R` (central `q_I = 0.01`; grid 0, 0.005, 0.01, 0.02): `beta* = (Delta varpi + q_I Delta nu) / Delta eta`, with `nu` the inspection rate. Workshop time and corrective repair after an inspection remain zero.

Intervals are 95% paired bootstrap percentiles over engines (B = 4,000, seed 20261021). `beta*` is reported as statistically bounded only if the interval of the avoided events excludes zero. The three repetitions reuse the same engines and are reported as ranges, never pooled.

## Contents

| Path | Contents |
|---|---|
| `protocolo_equilibrio_eventos_21a.md`, `protocolo_custo_inspecao_21b.md` | Protocols written before execution (contrasts C1–C8, grids, verification list, interpretation). |
| `break_even_21a.py`, `break_even_cost_21b.py` | Analyses. `test_*.py` are unit tests; `verify_*.py` rebuild every contrast, preference curve, rate and the frontier from the raw archived expectations with separate code. |
| `make_break_even_tables_21a.py`, `make_break_even_cost_tables_21b.py` | LaTeX tables of the paper and supplement, generated from the summaries. |
| `artifacts/pilot_break_even_21a/`, `artifacts/pilot_break_even_cost_21b/` | Outputs (`rates`, `contrasts`, `contrast_summary`, `preference_curves`, `frontier`, validation, metadata, manifest with SHA-256 hashes, logs) and `conclusoes.md`, the written conclusions in Portuguese. |
| `artifacts/pilot_break_even_cost_21b_failed_run1/` | First P21.2 execution, preserved: it computed all contrasts correctly but its own validation function failed (empty scenario key against NaN; 0/0 for arms without inspections). Only the metadata and validation record are kept. |
| `artifacts/pilot_inspection_17b/`, `artifacts/pilot_inspection_latent_17c/`, `artifacts/pilot_policy_selection_13a/` | The archived inputs read by the scripts (`expectations.csv.gz`, `summary.csv`, `decisions.csv`); their SHA-256 hashes are recorded in each `execution_start.json`. |

## Reproduce

Python with NumPy and pandas. From the repository root:

```text
python -m unittest discover -s experiments -p "test_break_even*.py"
python experiments/break_even_21a.py
python experiments/break_even_cost_21b.py
python experiments/verify_break_even_21a.py
python experiments/verify_break_even_cost_21b.py
```

The scripts overwrite their output directory; run them in a copy of the repository to compare. Re-running in a clean copy of this tree reproduced `rates`, `contrasts`, `contrast_summary`, `preference_curves` and `frontier` of both analyses byte for byte. The verifiers take a few minutes each.

## Reading the results

- Thresholds with a dagger in the paper are not statistically bounded; do not read them as reliable values.
- Results are conditional on the inspection generator (true remaining life inside the simulation, uncalibrated), the monitoring-loss scenario, independent renewal and the archived engines. The 20-year totals of the literal-flight scenario are an arithmetic illustration of the same rates and are not interpreted as maintenance cost.
- None of this establishes a population risk, an economic optimum or maintenance credit.
