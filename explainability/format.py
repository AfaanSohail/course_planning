import argparse
import json
from pathlib import Path


def format_answer(result):
    lines = ["# Explainability record", "", "Question: " + result["question"], "",
             "Mode: " + result["mode"], "", "## Generated text (LLM)", ""]
    lines.append(result["answer"] if result.get("llm_called") else "PENDING: no LLM text was generated for this record.")
    if not result.get("llm_called"):
        lines += ["", "System status message: " + result["answer"]]
    for status, label in (("explicit", "Explicit knowledge (stored RDF)"), ("inferred", "Inferred knowledge (OWL schema closure)")):
        lines += ["", "## " + label, ""]
        facts = [e for e in result.get("evidence", []) if e["status"] == status]
        if not facts:
            lines.append("No facts of this kind were retrieved.")
        for e in facts:
            lines.append(f"- [{e['id']}] `{e['s']} {e['p']} {e['o']}`")
    retrieval = result.get("retrieval", {})
    lines += ["", "## Application rule results and query provenance", "",
              "These conclusions are computed; they are not asserted RDF triples.", "",
              "```json", json.dumps({"intent": retrieval.get("intent"), "query": retrieval.get("query"),
              "rows": retrieval.get("rows"), "reasoning": retrieval.get("reasoning"),
              "graph_sha256": retrieval.get("graph_sha256")}, indent=2), "```", "",
              "## Prediction", "", "None. Option C verifies graph paths; hypothetical completions are labelled assumptions.", "",
              "## Limitations", "", *["- " + v for v in retrieval.get("limitations", [])]]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("input", type=Path); p.add_argument("output", type=Path)
    a = p.parse_args(); a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(format_answer(json.loads(a.input.read_text(encoding="utf-8"))), encoding="utf-8")
