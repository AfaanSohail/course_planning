"""Generate a human grading sheet, then validate it before reporting accuracy.

No substring/LLM self-grading is accepted as final correctness. Unreviewed values
stay PENDING, never become zero or ten. Every score is tied to its raw artifact.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from reasoning.kg import ROOT, save_json

FIELDS = ["cq", "condition", "correct", "evidence_available", "unsupported_claims",
          "reviewer", "notes", "raw_sha256"]


def rows_for(folder, cases):
    rows = []
    for c in cases:
        for condition in "AB":
            p = folder / f"{c['id']}_{condition}.json"
            rows.append({"cq": c["id"], "condition": condition, "correct": "",
                         "evidence_available": "", "unsupported_claims": "", "reviewer": "", "notes": "",
                         "raw_sha256": hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else "MISSING"})
    return rows


def score(run_id, initialize=False):
    folder = ROOT / "evaluation/results" / run_id
    cases = json.loads((ROOT / "evaluation/cqs.json").read_text())
    grading = folder / "grades.csv"
    if initialize:
        if grading.exists():
            raise SystemExit("grades.csv already exists; preserve the review record.")
        folder.mkdir(parents=True, exist_ok=True)
        with grading.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDS); writer.writeheader(); writer.writerows(rows_for(folder, cases))
        print("Complete grades.csv using SCORING.md, then run without --init.")
        return
    if not grading.exists():
        raise SystemExit("Initialize and complete the grading sheet first (--init).")
    with grading.open() as f:
        grades = list(csv.DictReader(f))
    keys = [(r["cq"], r["condition"]) for r in grades]
    expected = {(c["id"], mode) for c in cases for mode in "AB"}
    if len(keys) != len(expected) or set(keys) != expected:
        raise SystemExit("Grades must contain exactly one A and B row for each of the ten CQs.")
    counts = {mode: {"correct": 0, "evidence": 0, "unsupported_claims": 0, "llm_called": 0} for mode in "AB"}
    by_key = {}
    for g in grades:
        p = folder / f"{g['cq']}_{g['condition']}.json"
        if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest() != g["raw_sha256"]:
            raise SystemExit(f"Missing or changed raw answer: {p}")
        if g["correct"] not in {"Yes", "No"} or g["evidence_available"] not in {"Yes", "No"} or not g["reviewer"].strip() or not g["notes"].strip():
            raise SystemExit(f"Incomplete human review: {g['cq']} {g['condition']}")
        if not g["unsupported_claims"].isdigit():
            raise SystemExit("unsupported_claims must be a manually checked nonnegative integer")
        answer = json.loads(p.read_text())
        mode = g["condition"]
        counts[mode]["correct"] += g["correct"] == "Yes"
        counts[mode]["evidence"] += g["evidence_available"] == "Yes"
        counts[mode]["unsupported_claims"] += int(g["unsupported_claims"])
        counts[mode]["llm_called"] += bool(answer.get("llm_called"))
        by_key[(g["cq"], mode)] = (g, answer)
    comparison = []
    for case in cases:
        ga, a = by_key[(case["id"], "A")]; gb, b = by_key[(case["id"], "B")]
        comparison.append({"CQ / question": case["id"] + " / " + case["question"],
                           "Expected answer": json.dumps(case["expected"], ensure_ascii=False),
                           "LLM only": a["answer"], "KG-grounded": b["answer"],
                           "Correct? A / B": ga["correct"] + " / " + gb["correct"],
                           "Evidence available? A / B": ga["evidence_available"] + " / " + gb["evidence_available"]})
    with (folder / "comparison.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(comparison[0])); writer.writeheader(); writer.writerows(comparison)
    save_json(folder / "summary.json", {"status": "human_review_complete", "questions": len(cases), "conditions": counts})
    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--run-id", required=True)
    p.add_argument("--init", action="store_true")
    a = p.parse_args(); score(a.run_id, a.init)
