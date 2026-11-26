"""Verify that the real natural-language router retrieves the expected CQ rows."""
import json
from app.service import Advisor, context_for
from app.config import Config
from reasoning.kg import ROOT, save_json


if __name__=="__main__":
    cases=json.loads((ROOT/"evaluation/cqs.json").read_text())
    advisor=Advisor(Config.load(ROOT/"config/ollama.example.json"));results=[]
    canonical=lambda rows:sorted(json.dumps(r,sort_keys=True) for r in rows)
    for case in cases:
        output=advisor.answer(case["question"],retrieve_only=True)
        retrieved=output["retrieval"];context=context_for(retrieved,advisor.config.context_max_chars)
        item={"cq":case["id"],"actual_intent":retrieved["intent"],"expected_intent":case["query_id"],
              "intent_match":retrieved["intent"]==case["query_id"],
              "rows_match":canonical(retrieved["rows"])==canonical(case["expected"]),
              "rows":len(retrieved["rows"]),"evidence_edges":len(output["evidence"]),
              "invalid_evidence_edges":sum(not advisor.reasoner.kg.valid_edge(e) for e in output["evidence"]),
              "all_rows_fit_context":context is not None,"llm_called":output["llm_called"],
              "context_characters":len(json.dumps(context)) if context else 0,
              "omitted_evidence":context["omitted_evidence"] if context else None,
              "omitted_traces":context["omitted_traces"] if context else None}
        results.append(item);print(json.dumps(item),flush=True)
    summary={"graph_sha256":advisor.reasoner.kg.sha256,"configuration":advisor.config.public(),"cases":results,
             "all_passed":all(r["intent_match"] and r["rows_match"] and r["all_rows_fit_context"] and
                              r["invalid_evidence_edges"]==0 and not r["llm_called"] for r in results)}
    save_json(ROOT/"evaluation/results/retrieval_validation.json",summary)
    if not summary["all_passed"]:raise SystemExit("Retrieval validation has failures; inspect JSON before LLM evaluation.")
