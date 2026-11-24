"""Public interface: Advisor.answer(question) -> {answer, evidence, mode, ...}."""
import json
import re
from reasoning import KG, Reasoner
from reasoning.kg import ROOT
from .config import Config
from .llm import LLMClient
from .retrieval import retrieve


def context_for(retrieval, max_chars):
    # Include all rows. Trim evidence/traces deterministically, announcing omissions.
    # Full untrimmed evidence and traces remain in the returned JSON artifact.
    records = [{"id": f"R{i}", "values": row} for i, row in enumerate(retrieval["rows"], 1)]
    context = {"question": retrieval["question"], "intent": retrieval["intent"], "rows": records,
               "limitations": retrieval["limitations"], "graph_sha256": retrieval["graph_sha256"],
               "evidence": [], "reasoning": [], "omitted_evidence": 0, "omitted_traces": 0}
    if len(json.dumps(context)) > max_chars:
        return None
    # Prioritize concise application conclusions, retaining paths in the evidence array.
    for trace in retrieval["reasoning"]:
        concise = {k: v for k, v in trace.items() if k not in {"paths", "expression_tree", "branches", "runtime_ms"}}
        trial = dict(context, reasoning=context["reasoning"] + [concise])
        if len(json.dumps(trial)) <= max_chars:
            context = trial
        else:
            context["omitted_traces"] += 1
    edges = sorted(retrieval["evidence"], key=lambda e: (e["status"] != "inferred", len(e["o"]), e["id"]))
    for edge in edges:
        trial = dict(context, evidence=context["evidence"] + [edge])
        if len(json.dumps(trial)) <= max_chars - 200:
            context = trial
        else:
            context["omitted_evidence"] += 1
    return context


class Advisor:
    def __init__(self, config=None, reasoner=None, client=None):
        self.config = config or Config()
        self.reasoner = reasoner or Reasoner(KG())
        self.client = client or LLMClient(self.config)

    def answer(self, question, mode="grounded", retrieve_only=False):
        if mode not in {"grounded", "baseline"}:
            raise ValueError("mode must be grounded or baseline")
        if mode == "baseline":
            messages = [{"role": "system", "content": (ROOT / "prompts/baseline.txt").read_text()},
                        {"role": "user", "content": question}]
            completion = self.client.complete(messages)
            return {"question": question, "answer": completion["answer"], "evidence": [], "mode": "baseline",
                    "llm_called": True, "completion": completion, "config": self.config.public()}
        retrieval = retrieve(question, self.reasoner)
        result = {"question": question, "answer": "", "evidence": retrieval["evidence"], "mode": "grounded",
                  "retrieval": retrieval, "llm_called": False, "config": self.config.public()}
        if retrieve_only:
            return dict(result, mode="retrieval_only", answer="Retrieval only; no LLM response generated.")
        if not retrieval["sufficient"]:
            return dict(result, mode="insufficient_evidence", answer="Insufficient evidence: " + " ".join(retrieval["limitations"]))
        context = context_for(retrieval, self.config.context_max_chars)
        if context is None:
            return dict(result, mode="insufficient_evidence", answer="Insufficient evidence within the configured context budget; narrow the question.")
        messages = [{"role": "system", "content": (ROOT / "prompts/grounded.txt").read_text()},
                    {"role": "user", "content": question + "\n\nCONTEXT:\n" + json.dumps(context, ensure_ascii=False)}]
        completion = self.client.complete(messages)
        used = re.findall(r"\[(E[0-9a-f]+|R\d+)\]", completion["answer"])
        available = {e["id"] for e in context["evidence"]} | {r["id"] for r in context["rows"]}
        invalid = sorted(set(used) - available)
        result.update(answer=completion["answer"], llm_called=True, completion=completion,
                      context=context, citation_check={"cited": used, "unknown_ids": invalid,
                      "has_citations": bool(used), "semantic_support_checked": False})
        # Do not rewrite/hide a flawed answer: preserve it for honest manual scoring.
        return result
