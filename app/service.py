"""Public interface: Advisor.answer(question) -> {answer, evidence, mode, ...}."""
import json
import re
from collections import Counter
from reasoning import KG, Reasoner
from reasoning.kg import ROOT
from .config import Config
from .llm import LLMClient
from .retrieval import retrieve


SEMANTICS = {
    'Q02': ('Each row is a DIRECT prerequisite edge from fromCode to toCode; option identifies an OR alternative; '
            'conditions in an option are AND, and a one-of group is OR. Render ALL edges in a compact table, '
            'preserving edgeType and option. Do not invent flattened end-to-end paths or combine different branches. '
            'toIsBaseCourse means no recorded course prerequisite, not guaranteed permission.'),
    'Q08': ('Every row ALREADY establishes upstreamCode reachable from the question target via viaCode '
            'in at least two prerequisite-course links. Render ALL rows; do not reject this executed query result '
            'because individual RDF edges were omitted from the prompt. firstHop distinguishes required and possible alternatives.'),
    'Q06': ('Render EVERY requirement row, INCLUDING zero remainingCourses. Remaining credits are '
            'max(0,minCredits-allocatedCredits) when minCredits is known, otherwise unknown. '
            'Focus areas are alternatives, not eight compulsory requirements. Do not add overlapping group totals.'),
    'Q04': ('Rows separate would become satisfiable from still blocked. Render BOTH groups and each '
            'stillRequired condition verbatim; do not describe blocked candidates as unlocked.'),
    'Q13': ('Rows describe the query-level change under the hypothetical assumption. The number of '
            'downstream candidates in the trace is NOT the number newly eligible. Report row membership '
            'without claiming every prerequisite was previously unsatisfied.'),
    'Q10': ('acceptsBothCodes=true means both codes are explicitly mentioned in that downstream prerequisite. '
            'false means explicit acceptance of both was NOT established; it does NOT mean substitution is forbidden. '
            'Cross-listing alone does not establish general substitution policy.'),
    'Q15': ('Render all course rows with catalog wording, requirement, parseStatus and unverified fields. '
            'satisfiedOptions is a COUNT of alternatives, not a list of separate conditions. '
            'Do not invent grades, credits, completed degrees or official registration decisions.'),
}


def guidance_for(retrieval):
    rows = retrieval['rows']
    result = {'row_count': len(rows), 'semantics': SEMANTICS.get(retrieval['intent'],
              'Render every result row. Preserve the scope and limitations of this executed query.')}
    if rows and 'courseCode' in rows[0]:
        result['distinct_course_count'] = len({r['courseCode'] for r in rows})
    for field in ('status', 'eligibleIn'):
        if rows and field in rows[0]:
            result[field + '_row_counts'] = dict(Counter(r[field] for r in rows))
    return result


def citation_ids(answer):
    """Inspect individual/grouped row citations without claiming semantic support."""
    ids = []
    for group in re.findall(r"\[([^\]\n]+)\]", answer):
        for start, end in re.findall(r"\bR(\d+)\s*[-–]\s*R?(\d+)\b", group):
            if 0 <= int(end) - int(start) <= 1000:
                ids.extend(f"R{i}" for i in range(int(start), int(end) + 1))
        ids.extend(re.findall(r"\b(?:E[0-9a-f]+|R\d+)\b", group))
    return list(dict.fromkeys(ids))


def context_for(retrieval, max_chars):
    # Include all rows. Trim evidence/traces deterministically, announcing omissions.
    # Full untrimmed evidence and traces remain in the returned JSON artifact.
    records = [{"id": f"R{i}", "values": row} for i, row in enumerate(retrieval["rows"], 1)]
    context = {"question": retrieval["question"], "intent": retrieval["intent"], "rows": records,
               "limitations": retrieval["limitations"], "graph_sha256": retrieval["graph_sha256"],
               "evidence": [], "reasoning": [], "omitted_evidence": 0, "omitted_traces": 0,
               "result_guide": guidance_for(retrieval),
               "recorded_completed_courses": retrieval.get("recorded_completed_courses", [])}
    if len(json.dumps(context)) > max_chars:
        return None
    # Prioritize concise application conclusions, retaining paths in the evidence array.
    for trace in retrieval["reasoning"]:
        concise = {k: v for k, v in trace.items() if k not in {"paths", "expression_tree", "branches", "runtime_ms"}}
        if "requirements" in concise:
            concise["requirements"] = [{k: v for k, v in row.items() if k != "note"}
                                       for row in concise["requirements"]]
            concise["full_policy_notes_in_artifact"] = True
        if "dependants" in concise:
            # A large what-if trace previously vanished entirely when it exceeded
            # the budget. Keep its conclusion/assumptions before optional detail.
            concise = {k: v for k, v in concise.items() if k != "dependants"}
            concise["hypothetical_policy"] = "Assumptions are evaluated in memory, without storing them as verified completions."
            concise["newly_satisfied"] = [d["course"] for d in trace["dependants"] if d["newly_satisfied"]]
            concise["downstream_course_count"] = len(trace["dependants"])
            concise["full_dependant_details_in_artifact"] = True
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
        used = citation_ids(completion["answer"])
        available = {e["id"] for e in context["evidence"]} | {r["id"] for r in context["rows"]}
        invalid = sorted(set(used) - available)
        result.update(answer=completion["answer"], llm_called=True, completion=completion,
                      context=context, citation_check={"cited": used, "unknown_ids": invalid,
                      "has_citations": bool(used), "semantic_support_checked": False})
        # Do not rewrite/hide a flawed answer: preserve it for honest manual scoring.
        return result
