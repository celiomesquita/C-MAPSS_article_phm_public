# Literal flight-cycle renewal scenario — P20.2

One benchmark cycle is **assumed** to represent one flight of each engine: start, flight, landing, shutdown. A flight of a twin-engine aircraft adds one cycle to each position. Thus 20 years at 1,600 flights/year is 32,000 cycles **per position**, not 64,000. The numerical model does not simulate intra-flight phases or validate the physical degradation rate.

The main scenario uses `xi=1`, AGE127, always-valid monitoring, a mature initial fleet, full restoration, an independent 20,000-flight LLP counter and the archived PHM/inspection rules. The inspection generator remains entry 127, interval 5, W=60, gamma=1, pP=0, pF=1. Two execution leads and all five PHM controls are retained. No sensor data or model refitting is required. This analysis follows confirmation and is exploratory.

The original scaled P20.1 results and the 32-series review remain unchanged. Their totals have a different time mapping and must not be combined with the literal totals. The review's 1,531 directional records exclude this subsequent analysis.

## Central outcome

Means over three repeated partitions, execution lead one flight, US$ million per position over 20 years, at US$6 million per visit:

| Subset | Age 127 | Conservative PHM | Same PHM + inspection |
|---|---:|---:|---:|
| FD001 | 1516.70 | 1146.82 | 1182.36 |
| FD002 | 1516.77 | 1139.59 | 1175.85 |
| FD003 | 1516.61 | 928.22 | 959.22 |
| FD004 | 1516.74 | 897.02 | 956.68 |

For two equivalent positions, multiply expected costs by two. This does not assert independent engines or quantify joint aircraft risk. Costs are fixed restoration expenditure; they exclude inflation, discounting, inspection/monitoring charges, downtime and extra consequences of endpoint events. US$5/7 million per visit multiply every total by 5/6 or 7/6. No company savings or operational optimum is established.

Expected visits are about 252.8 for age removal, 149.5–191.1 for conservative ISO, and 159.4–197.1 with inspection. FD004 conservative ISO has 0.8855 simulated mean endpoint events per position, versus 0.0188 with inspection. Read `summary.csv` and `cells.csv` for all event categories, point-anchor controls, conditional Monte Carlo errors and both leads. Large absolute costs follow from repeating the benchmark's short life under the literal assumption, and are not operator expenditure forecasts.

## Reproduction

Requires Python, NumPy and pandas. From the repository root, where the runner, numerical core, verifier and protocol are installed under `experiments/`:

```text
python experiments/twenty_year_20b_literal.py --output /path/to/new_output
python experiments/verify_twenty_year_20b_literal.py --output /path/to/new_output
```

Use a new output directory: completed runs cannot be overwritten. Without the private archive, the runner reads the included `evidence_inputs/` selection and reproduces the same renewal simulation without raw NASA trajectories or fitted models. The reference P20.1 source is supplied for AST comparison; it is not imported and does not require its older plotting dependencies. The package contains copies of the four runnable/protocol files for provenance; install the Python files at `experiments/` when reproducing in this repository layout.

`metadata.json` records environment, seeds, original decision-file hashes, selected input hashes and validation. Inputs contain only the required columns and complete-engine rules. The numerical core's eight functions are unchanged from corrected P20.1. The verifier implements outcome generation and renewal through separate scalar code.

All 264 arm/cell combinations pass the stationary no-LLP check (maximum |z| 2.3035, threshold 4.5). LLP visits are identical across arms per replica. Scalar verification checks 121,406 outcome atoms and exactly reproduces five counts for 12 replicates in each of 264 combinations (3,168 replicate comparisons). Deterministic AGE127 is also verified at new and mature starts without LLP. No failed scientific run occurred. Early shell quoting and a declaration-order issue were corrected before execution; they produced no model results. A later verifier path fallback enables public-only reproduction and leaves its numerical checks unchanged.

Monte Carlo standard errors are **conditional on the archived empirical engine pools**. They do not include population, model-selection or physical-model uncertainty. Repeated partitions reuse engines. `manifest.json` covers all packaged inputs and outputs except itself. No remote publication is performed by the scripts.
