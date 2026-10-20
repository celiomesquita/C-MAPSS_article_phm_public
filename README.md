# C-MAPSS turbofan removal: companion artifacts

Companion reproducibility artifacts for the manuscript:

> Antonio C. P. Mesquita, "Conservative forecast rules can act like health-index landmarks: evidence from simulated turbofan removal", prepared for *Reliability Engineering & System Safety*.

## Contents

| Directory | Contents |
|---|---|
| `appendix/` | Current supplementary methods and results (`supplementary.tex` / `.pdf`), the archived early-pilot specification and results (`early_pilots.tex` / `.pdf`), and the bibliography needed for standalone compilation. |
| `experiments/` | Original experiment scripts, protocols and artifact summaries (the frozen-protocol directory is not distributed here). |
| `experiments/results_review_2026-10-19/` | Coverage of 32 scientific series; 1,531 directional contrast records including non-gains; three-arm restoration-cost tables; source inventory, small aggregate evidence inputs and hashes. |
| `experiments/literal_cycles_2026-10-19/` | Subsequent literal-flight analysis: selected archived decisions, three-arm costs/events, conditional Monte Carlo errors, portable numerical core, independent verifier and public-only reproduction. |
| `experiments/BREAK_EVEN_README.md` and `experiments/artifacts/pilot_break_even_21a/`, `.../pilot_break_even_cost_21b/` | Break-even cost of end-of-life events (P21.1) and its sensitivity to the inspection cost (P21.2): protocols, code, tests, independent verifiers, archived inputs, outputs with hashes and written conclusions. |

The review package was prepared after confirmation. It organises existing results without refitting, selecting a new policy or rerunning the experiments. The failed first 20-year run remains a provenance record and is not used as evidence of a maintenance benefit. Read the package README for scope and limitations.

## Dependencies

Python 3.10+ with NumPy and pandas for the post-processing and renewal analyses below; the original model-fitting pilots in `experiments/` also use SciPy and scikit-learn.

## Reproduce the aggregate review

With NumPy and pandas installed, run from the repository root:

```text
python experiments/review_experiment_outputs_20261019.py
```

The supplied aggregate evidence inputs reproduce the contrast and cost tables without raw NASA trajectories or model binaries. This post-processing is distinct from reproducing the original model-fitting experiments. The frozen environment and per-experiment protocols document those original runs.

## Cycles and costs

The current 20-year scenario assumes one benchmark cycle per flight of each engine (xi=1). A twin-engine aircraft adds one cycle to each position per flight: 32,000 cycles per position over 20 years at 1,600 flights/year. The AGE127, conservative PHM and PHM-plus-inspection comparison is in `experiments/literal_cycles_2026-10-19/`; the earlier scale-bridge scenario remains a separate sensitivity in Supplementary Material S4 and the archived review package. Expected cost for two equivalent positions is twice the per-position value; no engine independence or joint aircraft risk is inferred. Costs are fixed restoration expenditure, with zero incremental inspection charge in the main analysis (a positive inspection cost is a sensitivity in `experiments/BREAK_EVEN_README.md`), not observed total maintenance costs or company savings. The 20-year totals are an arithmetic illustration; the paper's economic comparison is the break-even cost of an end-of-life event. Read event outcomes alongside costs.

## Data

Raw C-MAPSS data are not included. They are available from the [NASA Prognostics Data Repository](https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/). Place the extracted files under `CMAPSSData/` when reproducing the original experiments; the aggregate-review command does not require them.

> Saxena, A., Goebel, K., Simon, D. and Eklund, N. (2008). Damage propagation modeling for aircraft engine run-to-failure simulation. International Conference on Prognostics and Health Management.

## Supplementary PDFs

From `appendix/`, compile each source with `latexmk -pdf supplementary.tex` or `latexmk -pdf early_pilots.tex`. The supplementary source uses the adjacent `references.bib` for portability.

## Licence

The code is released under the MIT licence. The manuscript text is copyright of the author; preprint sharing follows Elsevier's article sharing policy.

## Reproduce the literal-flight scenario

Install NumPy and pandas, then use a new output directory:

```text
python experiments/twenty_year_20b_literal.py --output /path/to/new_output
python experiments/verify_twenty_year_20b_literal.py --output /path/to/new_output
```

No raw NASA trajectories or private fitted models are needed for this renewal analysis. The archived aggregate review and this new simulation have different scopes; the earlier review retains its original scale-bridge tables.

## Reproduce the break-even analyses

```text
python experiments/break_even_21a.py
python experiments/break_even_cost_21b.py
python experiments/verify_break_even_21a.py
python experiments/verify_break_even_cost_21b.py
```

The archived inputs are included; no raw NASA trajectories or fitted models are needed. See `experiments/BREAK_EVEN_README.md` for definitions, scope and limitations. This repository has no DOI; the version used for the paper is identified by its commit hash.

## Calibration/reserve attribution and source provenance (20 October 2026)

`experiments/sa3_20261020/` provides selected archived inputs, the portable
standard-library analysis, exact reference CSVs and an independent verification
of the paired contrasts and P10 source-byte reconstruction. See its README.
Supplementary Sections S7--S9 include the fuller methods, adverse results and
separate calibration/reserve effects. `release_sa3_2026-10-20.json` records that scientific update;
`release_title_update_2026-10-20.json` identifies the current files after the
manuscript title was harmonised. Earlier manifests remain historical records.
The final manuscript identifies this repository version by commit hash; no DOI
is assigned. Full texts of third-party papers used for local checking are excluded.

## Manuscript title update (20 October 2026)

The supplement and this README use the final submission title. This update
changes identification only; scientific methods, results and reproducibility
inputs remain unchanged. The title-update manifest lists the current hashes
and identifies the preceding release without rewriting historical manifests.
