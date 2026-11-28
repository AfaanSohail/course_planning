"""Summarize observed local checks without claiming unrun LLM experiments."""
import json
from xml.etree import ElementTree as ET
from reasoning.kg import ROOT, save_json


if __name__=="__main__":
    load=lambda p:json.loads((ROOT/p).read_text())
    reasoning=load("reasoning/outputs/summary.json")
    iteration1=load("evaluation/results/iteration1_rerun/summary.json")
    retrieval=load("evaluation/results/retrieval_validation.json")
    suite=ET.parse(ROOT/"evaluation/results/tests.xml").getroot().find("testsuite")
    clean_xml=ROOT/"evaluation/results/tests_clean_environment.xml"
    clean=ET.parse(clean_xml).getroot().find("testsuite") if clean_xml.exists() else None
    meta=load("report/submission.json")
    audit_path=ROOT/"evaluation/results"/meta['llm_run_id']/"artifact_audit.json"
    audit=json.loads(audit_path.read_text()) if audit_path.exists() else {}
    save_json(ROOT/"evaluation/results/verification_status.json",{
        "graph_sha256":reasoning["graph_sha256"],
        "tests":dict(suite.attrib),
        "fresh_isolated_environment_tests":dict(clean.attrib) if clean is not None else "PENDING",
        "iteration1_rebuild_isomorphic":iteration1["rebuild_isomorphic"],
        "original_queries_rerun":len(iteration1["queries"]),
        "original_queries_semantically_match":all(q["match_after_uri_and_concat_normalization"] for q in iteration1["queries"]),
        "reachability_matches":reasoning["reachability_exact_matches"],
        "reachability_courses":reasoning["courses_with_prerequisites"],
        "invalid_returned_edges":reasoning["invalid_returned_edges"],
        "invalid_or_disconnected_paths":reasoning["invalid_or_disconnected_paths"],
        "natural_language_retrieval_all_passed":retrieval["all_passed"],
        "llm_ab_experiment":({"supplied_response_records":audit['response_records'],
                             "complete_human_reviews":audit['complete_human_reviews'],
                             "truncated_responses":audit['truncated_responses']}
                             if audit else "PENDING: no supplied artifact audit"),
        "graphdb_live_check":meta.get("review_laptop_evidence","PENDING: no live readiness record"),
        "clean_machine_verification":meta.get("clean_machine_scope","PENDING"),
        "review_laptop_verification":meta.get("review_laptop_verified",False),
        "final_submission":"PENDING: demo video URL, final source commit and instructor access confirmation. Trial 3, grading, actual application screenshots and ThinkPad readiness evidence are integrated."})
    print("Updated evaluation/results/verification_status.json")
