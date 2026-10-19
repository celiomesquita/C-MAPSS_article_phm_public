"""Check public-only renewal reproduction without private archives or NASA data."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "experiments/literal_cycles_2026-10-19"

with tempfile.TemporaryDirectory(prefix="cmapss_literal_public_") as tmp:
    root = Path(tmp)
    exp = root / "experiments"
    bundle = exp / PACKAGE.name
    bundle.mkdir(parents=True)
    shutil.copytree(PACKAGE / "evidence_inputs", bundle / "evidence_inputs")
    shutil.copyfile(PACKAGE / "reference_twenty_year_20a.py", bundle / "reference_twenty_year_20a.py")
    for name in ("twenty_year_20b_literal.py", "renewal_core_20b.py", "verify_twenty_year_20b_literal.py", "protocolo_vinte_anos_20b_literal.md"):
        shutil.copyfile(ROOT / "experiments" / name, exp / name)
    out = root / "reproduced"
    for name in ("twenty_year_20b_literal.py", "verify_twenty_year_20b_literal.py"):
        subprocess.run([sys.executable, str(exp / name), "--output", str(out)], check=True, cwd=root)
    outputs = ("cells.csv", "summary.csv", "contrasts.csv", "validation_stationary.csv", "verification_replicates.csv")
    for name in outputs:
        pd.testing.assert_frame_equal(pd.read_csv(PACKAGE / name), pd.read_csv(out / name), check_exact=False, rtol=1e-12, atol=1e-12)
    report = dict(passed=True, compared_outputs=list(outputs), tolerance=1e-12,
                  no_private_archive=True, no_raw_data=True, independent_verifier=json.loads((out / "verification.json").read_text()))
    (PACKAGE / "public_only_reproduction.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
