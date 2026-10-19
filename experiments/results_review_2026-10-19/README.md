# Experimental-results coverage and restoration-cost comparison

This package supports the manuscript *Incremental value of failure forecasts beyond a health-index landmark in conservative turbofan removal on C-MAPSS*. The review was performed after confirmation on 19 October 2026. It organises existing results; it does not refit models, reopen C-MAPSS trajectories, choose a new policy or rerun simulations.

## Scope and interpretation

All 32 scientific experimental series were compared with the manuscript. Inventory and confirmation rehearsal are technical checks. The preserved failed first 20-year run is excluded from scientific benefit claims. Narrative findings were checked against aggregate CSVs where they support the additions; this is not a new independent reconstruction of every model or trajectory.

`experiment_coverage.csv` records coverage and the disposition of gains/non-gains by series. `reviewed_source_inventory.csv` lists the source reports, metadata and aggregate tables with hashes. `contrast_ledger.csv` contains 1,531 directional metric records from the archived paired comparisons, including favourable intervals, point gains with intervals crossing zero, and unfavourable comparisons. Records include repeated engines, overlapping comparisons and sometimes two metrics from one comparison. Their number is not a count of independent discoveries. The descriptive bootstrap intervals are not adjusted for multiple comparisons and do not demonstrate acceptable maintenance risk.

Newly highlighted findings include the early local-calibration life gains; the favourable refitted FD003 HI comparisons; state-specific direct-sensor-history improvements; trajectory-calibration coverage gains; and the positive internal-stability, forecast-error and life outcomes that accompanied unsuccessful full-chain transfer. Their negative or limiting outcomes are retained in the article and Supplementary Material S3. No sensitivity replaces a main rule retrospectively.

## Three-arm restoration expenditure

The central scenario is 20 years at 1,600 operational flight cycles per year, the declared lifetime scale bridge, LLP limit 20,000 flight cycles, mature initial fleet, full restoration and execution lead 1 benchmark cycle. PHM uses ISO, lower 98% anchor, reserve 15. The inspection arm uses the same PHM rule with the declared hypothetical five-benchmark-cycle inspection process. Repetitions reuse engines.

With common restoration cost `c_R`, expected expenditure is `c_R * expected restoration visits`, including forced LLP visits. At the previously declared illustrative US$6 million per restoration:

| Subset | Age 127 | PHM | PHM + inspection |
|---|---:|---:|---:|
| FD001 | 40.56 | 33.01 | 33.94 |
| FD002 | 40.66 | 32.91 | 33.90 |
| FD003 | 48.90 | 32.62 | 33.62 |
| FD004 | 48.75 | 31.46 | 33.25 |

Values are **US$ million per position over 20 years**, computed from unrounded archived visit means. `long_term_restoration_costs.csv` includes the visits, endpoint events and US$5/6/7 million sensitivities. Every arm has the same per-visit restoration charge. Costs exclude discounting, inflation, monitoring, downtime and additional failure-consequence charges; incremental inspection cost is zero. They measure restoration expenditure within this experimental contract, not total maintenance expenditure or company savings. Events must be read alongside costs.

## What a cycle means

One operational flight cycle is counted as engine start, flight, landing and shutdown. The original C-MAPSS simulation records one snapshot per simulated flight. The declared bridge `xi = L_ref / mean endpoint lifetime` stretches the accelerated simulated degradation lifetime into an assumed operational service interval; it does not simulate intra-flight phases. Thus **Age 127 means 127 benchmark cycles, or `127 * xi` operational flight cycles in this calendar scenario**. Execution leads and the inspection cadence scale correspondingly. `cycle_scale.csv` supplies the conversion for every subset. A literal one-to-one interpretation would set `xi=1` and give different calendar costs; those are not the archived central three-arm totals above.

## Reproducing the post-processing

From the repository root, run:

```text
python experiments/review_experiment_outputs_20261019.py
```

NumPy and pandas are required. The script uses existing private-project aggregate files if present; otherwise it reads the small exact copies under `evidence_inputs/`. For the 20-year simulation, the public input contains only the archived central-scenario rows, not a new simulation. `manifest.json` records the script, input and output hashes and the original complete simulation-file hash where available. The input row selection is explicit. Public-only reproduction recovers the contrast and cost summaries without reading raw NASA trajectories or loading fitted model binaries. The private-project inventory itself is preserved as a provenance record and is not reconstructed from an absent private archive.

In a clone of the public repository, `experiments/artifacts/` holds only the published subset of each series, so the script regenerates `reviewed_source_inventory.csv` from that subset and the file differs from the committed one, which was produced from the full private archive; all other tables reproduce byte for byte. After the break-even analyses (P21) were added, three further artifact folders are excluded from the 32 series reviewed.
