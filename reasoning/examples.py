"""Run representative inputs and save actual outputs for the Day 5 walkthrough.

Only inputs are fixed here. Every answer/path/verdict comes from the current KG.
Run with --case chain|eligibility|unlock|degree|unknown, or omit to run all cases.
"""
import argparse
from datetime import datetime, timezone
import hashlib
from pathlib import Path

from .engine import Reasoner
from .kg import KG, ROOT, RES, UCA, save_json

CASES = {
    "chain": ("prerequisite_chain", {"course": "CS421"}),
    "eligibility": ("eligibility", {"student": "S003", "course": "CS421", "term": "2026-fa"}),
    "unlock": ("reverse_unlock", {"student": "S002", "course": "CS225", "term": "2026-fa", "concurrent": False}),
    "degree": ("degree_progress", {"student": "S003"}),
    "unknown": ("prerequisite_chain", {"course": "ZZZZ999"}),
}


def short(term):
    return term.replace(str(RES), "res:").replace(str(UCA), "uca:")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=list(CASES))
    args = parser.parse_args()
    kg = KG()
    reasoner = Reasoner(kg)
    folder = ROOT / "reasoning/outputs/day5"
    source_hashes = {name: hashlib.sha256((ROOT / "reasoning" / name).read_bytes()).hexdigest()
                     for name in ("kg.py", "engine.py", "examples.py")}
    for name in ([args.case] if args.case else CASES):
        template, inputs = CASES[name]
        before = set(kg.explicit)
        result = reasoner.reason(template, **inputs)
        if not all(kg.valid_path(path) for path in result["paths"]):
            raise RuntimeError("A returned path is invalid or disconnected; inspect before reporting.")
        if before != set(kg.explicit):
            raise RuntimeError("Reasoning modified the explicit snapshot.")
        artifact = {"case": name, "input": {"template": template, **inputs},
                    "recorded_utc": datetime.now(timezone.utc).isoformat(),
                    "source_sha256": source_hashes, "all_paths_valid": True,
                    "explicit_graph_unchanged": True, "result": result}
        save_json(folder / f"{name}.json", artifact)
        print(f"\nCASE: {name} | INPUT: {artifact['input']}")
        print("Graph SHA256:", kg.sha256)
        print("Application rule result:", result["answer"])
        print("Verdict:", result["verdict"], "| Returned paths:", len(result["paths"]))
        print("All paths valid: True | Explicit KG unchanged: True | Predictions:", result["predictions"])
        if "truncated" in result:
            print("Traversal truncated:", result["truncated"])
        for option in result.get("options", []):
            print("Option:", short(option["option"]), "| fully met:", option["met"])
            for condition in option["conditions"]:
                print(" ", "MET" if condition["met"] else "UNMET", "|", condition["text"])
        if "dependants" in result:
            newly = [d["course"] for d in result["dependants"] if d["newly_satisfied"]]
            print("Hypothetical assumptions:", result["assumptions"])
            print("Newly satisfied courses:", newly)
        if "requirements" in result:
            print("Recorded requirement groups:", len(result["requirements"]), "| conflicts:", len(result["conflicts"]))
            print("First four groups only; inspect JSON for the full allocation audit:")
            for row in result["requirements"][:4]:
                print(" ", row["requirement"], "| courses remaining:", row["remainingCourses"],
                      "| credits remaining:", row["remainingCredits"])
        first_path = next((p for p in result["paths"] if p), [])
        if first_path:
            print("Path excerpt, first four edges (IRIs shortened for display only):")
            for edge in first_path[:4]:
                print(" ", short(edge["s"]), short(edge["p"]), short(edge["o"]),
                      "|", edge["status"], "| direction:", edge.get("direction", "forward"))
        print("Full input, output and evidence:", f"reasoning/outputs/day5/{name}.json")
        for warning in result.get("warnings", []):
            print("Warning:", warning)


if __name__ == "__main__":
    main()
