import csv
import hashlib
import json
import pytest
import evaluation.score as scoring


def fixture(tmp_path,monkeypatch):
    monkeypatch.setattr(scoring,"ROOT",tmp_path)
    folder=tmp_path/"evaluation/results/run";folder.mkdir(parents=True)
    (tmp_path/"evaluation/cqs.json").write_text(json.dumps([{"id":"CQ01","question":"fixture","expected":[]}]))
    for mode in "AB":
        (folder/f"CQ01_{mode}.json").write_text(json.dumps({"answer":"fixture output","llm_called":True}))
    scoring.score("run",initialize=True)
    return folder


def test_unreviewed_is_not_accuracy(tmp_path,monkeypatch):
    folder=fixture(tmp_path,monkeypatch)
    with pytest.raises(SystemExit,match="Incomplete human review"):scoring.score("run")
    assert not (folder/"summary.json").exists()


def test_changed_answers_and_duplicate_grades_rejected(tmp_path,monkeypatch):
    folder=fixture(tmp_path,monkeypatch)
    with (folder/"grades.csv").open() as f:rows=list(csv.DictReader(f))
    for r in rows:r.update(correct="Yes",evidence_available="No",unsupported_claims="0",reviewer="test",notes="fixture review")
    with (folder/"grades.csv").open("w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=scoring.FIELDS);writer.writeheader();writer.writerows(rows)
    (folder/"CQ01_A.json").write_text("changed")
    with pytest.raises(SystemExit,match="Missing or changed"):scoring.score("run")
    with (folder/"grades.csv").open("w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=scoring.FIELDS);writer.writeheader();writer.writerows(rows+[rows[0]])
    with pytest.raises(SystemExit,match="exactly one"):scoring.score("run")
