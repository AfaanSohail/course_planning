import argparse
import json
from .engine import Reasoner
from .kg import KG, DEFAULT_KG, save_json


def main():
    p = argparse.ArgumentParser(description="Run verified multi-hop reasoning")
    p.add_argument("template", choices=["prerequisite_chain", "eligibility", "reverse_unlock", "degree_progress"])
    p.add_argument("--kg", default=str(DEFAULT_KG))
    p.add_argument("--course")
    p.add_argument("--student")
    p.add_argument("--term", default="2026-fa")
    p.add_argument("--max-depth", type=int, default=32)
    p.add_argument("--max-paths", type=int, default=20000)
    p.add_argument("--output")
    a = p.parse_args()
    if a.template != "degree_progress" and not a.course:
        p.error("--course is required")
    if a.template != "prerequisite_chain" and not a.student:
        p.error("--student is required")
    kwargs = {"course": a.course} if a.course else {}
    if a.student:
        kwargs["student"] = a.student
    if a.template in {"eligibility", "reverse_unlock"}:
        kwargs["term"] = a.term
    result = Reasoner(KG(a.kg), a.max_depth, a.max_paths).reason(a.template, **kwargs)
    if a.output:
        save_json(a.output, result)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
