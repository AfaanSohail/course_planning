import json
import pytest
from report.build import validate_final
from reasoning.kg import ROOT


def test_final_report_rejects_pending_submission():
    meta=json.loads((ROOT/"report/submission.json").read_text())
    with pytest.raises(SystemExit,match="Final report blocked by missing evidence"):
        validate_final(meta,[])
