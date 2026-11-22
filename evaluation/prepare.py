"""Generate original CQ wording and expected answers by executing source queries."""
import argparse
from datetime import datetime, timezone
from xml.etree import ElementTree as ET
from zipfile import ZipFile
from reasoning import KG
from reasoning.kg import ROOT, save_json
from .queries import run_query

SELECTION = {
    "CQ01": "Instance: synthetic student S002; target term Fall 2026.",
    "CQ02": "Instance: CS 421.",
    "CQ03": "Instance: synthetic student S003; target course CS 421; Fall 2026.",
    "CQ04": "Instance: synthetic student S002 hypothetically completes CS 225; Fall 2026.",
    "CQ06": "Instance: synthetic student S003; program UIUC BS CS, catalog year 2026.",
    "CQ08": "Instance: CS 440.",
    "CQ10": "Instance: CS 374.",
    "CQ11": "Instance: advanced elective group; Fall 2026.",
    "CQ13": "Instance: synthetic student S002 hypothetically adds CS 225; Fall 2026.",
    "CQ15": "Instance: synthetic student S002's planned courses; Fall 2026.",
}


def original_cqs():
    with ZipFile(ROOT / "iteration1/Report/Report.docx") as z:
        doc = ET.fromstring(z.read("word/document.xml"))
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    cqs = {}
    for table in doc.findall(".//w:tbl", ns):
        for row in table.findall("w:tr", ns):
            cells = [" ".join(t.text or "" for t in c.findall(".//w:t", ns)).strip() for c in row.findall("w:tc", ns)]
            if len(cells) >= 2 and cells[0] in {f"CQ{i:02}" for i in range(1,16)} and cells[0] not in cqs:
                cqs[cells[0]] = cells[1]
    if len(cqs) != 15:
        raise ValueError("Could not extract all original CQs from supplied report")
    return cqs


def prepare(kg):
    original = original_cqs()
    cases = []
    for cq, instance in SELECTION.items():
        query_id = cq.replace("CQ", "Q")
        rows = run_query(kg, query_id)
        if not rows:
            raise ValueError(f"No expected rows for {cq}; inspect query/graph before evaluating")
        cases.append({"id": cq, "original_question": original[cq], "instance": instance,
                      "question": original[cq] + " " + instance, "query_id": query_id,
                      "expected": rows, "expected_graph_sha256": kg.sha256,
                      "rubric": "Correct iff all requested facts agree with the expected rows; no contradicted conclusion. "
                                "For exhaustive lists, verify completeness. Uncertainty can avoid hallucination but does not earn correctness for an unanswered CQ. "
                                "Rows are snapshot ground truth; judge limitations/AND-OR interpretation separately."})
    save_json(ROOT / "evaluation/cqs.json", cases)
    save_json(ROOT / "evaluation/results/ground_truth_manifest.json", {
        "created_utc": datetime.now(timezone.utc).isoformat(), "graph_sha256": kg.sha256,
        "source": "original CQ table and re-executed Iteration 1 queries", "case_count": len(cases)})
    return cases


if __name__ == "__main__":
    prepare(KG())
    print("Wrote evaluation/cqs.json from real SPARQL executions.")
