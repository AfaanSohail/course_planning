"""Measure multi-hop reachability, rule agreement and returned-edge validity.

Reachability is independently checked against SPARQL property paths. Q01/Q03 are
the submitted original queries, instantiated for every synthetic student. A
disagreement is an observable result, not silently massaged into a success.
"""
import csv
import json
import platform
from collections import defaultdict
from datetime import datetime, timezone
from time import perf_counter
from rdflib.namespace import RDF
from reasoning import KG, Reasoner
from reasoning.kg import ROOT, PREFIXES, STEP, UCA, save_json
from evaluation.queries import run_query


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)


def evaluate():
    kg, started = KG(), perf_counter()
    reasoner = Reasoner(kg)
    folder = ROOT / "reasoning/outputs"; folder.mkdir(parents=True, exist_ok=True)
    expected = defaultdict(set)
    for row in kg.explicit.query(PREFIXES + f"SELECT DISTINCT ?course ?target WHERE {{ ?course uca:hasPrerequisiteExpression ?e . ?course ({STEP})+ ?target . }}"):
        expected[row.course].add(row.target)
    courses = sorted(set(kg.explicit.subjects(UCA.hasPrerequisiteExpression, None)), key=str)
    reachable_rows, edge_total, invalid_edges, depths, truncated = [], 0, [], [], 0
    disconnected_paths = 0
    for c in courses:
        t = perf_counter(); actual = reasoner.reachable(c)
        closure_ms = (perf_counter() - t) * 1000
        trace = reasoner.reason("prerequisite_chain", course=c)
        truncated += trace["truncated"]
        for branch in trace["branches"]: depths.append(branch["course_hops"])
        for path in trace["paths"]:
            disconnected_paths += not kg.valid_path(path)
            for edge in path:
                edge_total += 1
                if not kg.valid_edge(edge): invalid_edges.append(edge)
        reachable_rows.append({"course": kg.code(c), "expected_size":len(expected[c]), "actual_size":len(actual),
                               "exact_match":actual == expected[c], "missing":json.dumps(sorted(map(str,expected[c]-actual))),
                               "extra":json.dumps(sorted(map(str,actual-expected[c]))), "closure_runtime_ms":closure_ms,
                               "chain_runtime_ms":trace["runtime_ms"], "returned_paths":len(trace["paths"]),
                               "truncated":trace["truncated"]})
    write_csv(folder / "reachability.csv", reachable_rows)
    eligibility_rows, option_rows = [], []
    for s in sorted(kg.explicit.subjects(RDF.type,UCA.Student), key=str):
        sid = str(kg.value(s,UCA.studentIdentifier))
        expected_set={row["courseCode"] for row in run_query(kg,"Q01",student=sid)}
        actual_set=set()
        for c in courses:
            x=reasoner.reason("eligibility",student=sid,course=c)
            if x["registration_ready"]: actual_set.add(kg.code(c))
            for path in x["paths"]:
                disconnected_paths += not kg.valid_path(path)
                for edge in path:
                    edge_total+=1
                    if not kg.valid_edge(edge):invalid_edges.append(edge)
        eligibility_rows.append({"student":sid,"query":"Q01","expected_count":len(expected_set),"actual_count":len(actual_set),
                                 "exact_match":expected_set==actual_set,"missing":json.dumps(sorted(expected_set-actual_set)),
                                 "extra":json.dumps(sorted(actual_set-expected_set))})
        # Compare every encoded CS421 condition, not only one final Boolean.
        rows=run_query(kg,"Q03",student=sid,course="CS421")
        x=reasoner.reason("eligibility",student=sid,course="CS421")
        for option in x["options"]:
            for condition in option["conditions"]:
                matches=[r for r in rows if r["option"]==option["option"] and r["conditionText"]==condition["text"]]
                expected_met=bool(matches) and all(r["conditionStatus"]=="met" for r in matches)
                option_rows.append({"student":sid,"condition":condition["condition"],"query":"Q03",
                                    "expected_met":expected_met,"actual_met":condition["met"],
                                    "exact_match":bool(matches) and expected_met==condition["met"]})
    write_csv(folder / "eligibility.csv", eligibility_rows); write_csv(folder / "option_conditions.csv", option_rows)
    examples={
        "chains_CS421":reasoner.reason("prerequisite_chain",course="CS421"),
        "eligibility_S003_CS421":reasoner.reason("eligibility",student="S003",course="CS421"),
        "unlock_S002_CS225":reasoner.reason("reverse_unlock",student="S002",course="CS225",concurrent=False),
        "progress_S003":reasoner.reason("degree_progress",student="S003"),
        "conflict_S004":reasoner.reason("degree_progress",student="S004"),
        "unknown_course":reasoner.reason("prerequisite_chain",course="ZZZZ999"),
        "no_prerequisites":reasoner.reason("eligibility",student="S001",course="CS100"),
        "failing_student":reasoner.reason("eligibility",student="S001",course="CS421"),
        "cycle_CHEM202":reasoner.reason("prerequisite_chain",course="CHEM202"),
        "depth_limit":Reasoner(kg,max_depth=1).reason("prerequisite_chain",course="CS421")}
    for name, value in examples.items():
        save_json(folder / f"{name}.json",value)
        for path in value["paths"]:
            disconnected_paths += not kg.valid_path(path)
            for edge in path:
                edge_total+=1
                if not kg.valid_edge(edge):invalid_edges.append(edge)
    summary={"generated_utc":datetime.now(timezone.utc).isoformat(),"graph_sha256":kg.sha256,
             "python":platform.python_version(),"courses_with_prerequisites":len(courses),
             "reachability_exact_matches":sum(r["exact_match"] for r in reachable_rows),
             "reachability_exact_match_rate":sum(r["exact_match"] for r in reachable_rows)/len(courses),
             "eligibility_student_set_matches":sum(r["exact_match"] for r in eligibility_rows),
             "eligibility_student_sets_tested":len(eligibility_rows),
             "condition_matches":sum(r["exact_match"] for r in option_rows),"conditions_tested":len(option_rows),
             "returned_edges_checked":edge_total,"invalid_returned_edges":len(invalid_edges),
             "edge_validity_rate":(edge_total-len(invalid_edges))/edge_total if edge_total else None,
             "invalid_or_disconnected_paths":disconnected_paths,
             "maximum_returned_course_depth":max(depths,default=0),
             "mean_returned_course_depth":sum(depths)/len(depths) if depths else None,
             "truncated_course_traces":truncated,"max_depth":reasoner.max_depth,"max_paths":reasoner.max_paths,
             "runtime_seconds":perf_counter()-started,
             "negative_cases":{name:examples[name]["verdict"] for name in ["unknown_course","no_prerequisites","failing_student"]},
             "scope_notes":["Reachable sets include the source only if an actual nonzero cycle returns to it.",
                            "Q01 comparison covers courses with recorded expressions; no-prerequisite courses are separate.",
                            "Q03 is checked for all four students on CS421; not every student-course pair.",
                            "100% edge validity does not establish parser or policy correctness.",
                            "Runtime is one local run, not a statistical benchmark."]}
    save_json(folder / "summary.json",summary)
    save_json(folder / "invalid_edges.json",invalid_edges)
    print(json.dumps(summary,indent=2))


if __name__ == "__main__": evaluate()
