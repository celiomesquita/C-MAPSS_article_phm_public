# Forecast-based removal of turbofan engines — reproducibility repository

Public reproducibility repository for the article:

> A. C. P. de Mesquita, "Forecast-based removal of turbofan engines with
> sensor-only prognostics and simulated borescope inspection,"
> *Reliability Engineering & System Safety* (submitted 2026).

## Contents

| Directory | Contents |
|---|---|
| `LaTeX/` | Manuscript LaTeX source, highlights, cover letter, title page |
| `appendix/` | Early-pilot specification, results and information constraints (removed from the article to meet the journal word limit; compiled standalone as `early_pilots.tex`) |
| `experiments/` | Experiment scripts (`.py`), protocols and planning documents (`.md`), frozen-protocol directory, and artifact summaries (`.md`, `.json` — no binary model files or large CSVs) |

## Data

The C-MAPSS benchmark data are **not included** in this repository. They are
publicly available from the NASA Prognostics Center of Excellence Data
Repository:

> A. Saxena, K. Goebel, D. Simon and N. Eklund, "Damage propagation modeling
> for aircraft engine run-to-failure simulation," *Proc. Int. Conf. Prognostics
> and Health Management (PHM)*, 2008.
> <https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/>

Download `CMAPSSData.zip` and place its contents in a `CMAPSSData/` directory
at the repository root before running the scripts.

## Reproducing the experiments

Each experiment script in `experiments/` corresponds to one or more pilots
described in the article. The scripts are numbered to reflect the experimental
sequence (P01–P20). Protocol documents (`.md` files) describe the design
decisions, assumptions and evaluation criteria for each pilot.

Dependencies: Python 3.10+, NumPy, SciPy, scikit-learn, pandas.

Install with:
```bash
pip install numpy scipy scikit-learn pandas
```

Run the frozen-protocol confirmation (FD002/FD004) with:
```bash
cd experiments
python confirmation_19a.py --rehearsal   # dry run on FD001/FD003
# python confirmation_19a.py --confirm   # opens FD002/FD004 once only
```

## Licence

The code is released under the MIT licence. The manuscript text is copyright
of the author; preprint sharing follows Elsevier's article sharing policy.
