"""Query-time SPARQL rows plus actual graph evidence and reasoning traces."""
from rdflib import Literal, URIRef
from rdflib.namespace import RDF, RDFS
from reasoning.kg import UCA, RES
from evaluation.queries import parameterized
from .linking import link, route

COURSE_REQUIRED = {"Q02", "Q03", "Q04", "Q08", "Q10", "Q13"}
STUDENT_REQUIRED = {"Q01", "Q03", "Q04", "Q06", "Q13", "Q15"}
TERM_REQUIRED = {"Q01", "Q11"}


def retrieve(question, reasoner):
    kg = reasoner.kg
    entities = link(question)
    intent = route(question, entities)
    errors = []
    if intent is None:
        errors.append("No supported catalog/degree question template could be identified.")
    for key, required in (("courses", COURSE_REQUIRED), ("students", STUDENT_REQUIRED), ("terms", TERM_REQUIRED)):
        if intent in required and len(entities[key]) != 1:
            errors.append(f"Specify exactly one {key[:-1]} for this question.")
    if len(entities["students"]) > 1 or len(entities["courses"]) > 1 or len(entities["terms"]) > 1:
        errors.append("Multiple entities are ambiguous for the selected single-target template.")
    for kind, values in (("course", entities["courses"]), ("student", entities["students"]), ("term", entities["terms"])):
        for value in values:
            node = kg.resource(kind, value)
            if not any(kg.explicit.triples((node, None, None))):
                errors.append(f"Unknown {kind}: {value}.")
            elif kind == "term" and not list(kg.explicit.subjects(UCA.offeredInTerm, node)):
                errors.append(f"No offering snapshot is recorded for term {value}.")
            elif kind == "course" and not kg.objects(node, UCA.courseTitle):
                errors.append(f"{value} is a stub with no catalog text; evidence is incomplete.")
    result = {"question": question, "intent": intent, "entities": entities, "rows": [], "evidence": [],
              "reasoning": [], "sufficient": False, "limitations": errors, "graph_sha256": kg.sha256}
    if errors:
        return result
    student = entities["students"][0] if entities["students"] else None
    course = entities["courses"][0] if entities["courses"] else None
    term = entities["terms"][0] if entities["terms"] else "2026-fa"
    kwargs = {"student": student, "course": course, "term": term}
    query = parameterized(intent, **kwargs)
    result.update(query=query, rows=kg.query(query, inferred=intent == "Q11"),
                  query_uses_closure=intent == "Q11")
    if intent == "Q01":
        result["limitations"].append("Q01 covers courses with recorded prerequisite options; no-recorded-prerequisite courses are outside this query's scope.")
    if intent == "Q02":
        result["reasoning"].append(reasoner.reason("prerequisite_chain", course=course))
    elif intent == "Q03":
        result["reasoning"].append(reasoner.reason("eligibility", student=student, course=course, term=term))
    elif intent in {"Q04", "Q13"}:
        result["reasoning"].append(reasoner.reason("reverse_unlock", student=student, course=course, term=term, concurrent=False))
    elif intent == "Q06":
        result["reasoning"].append(reasoner.reason("degree_progress", student=student))
    elif intent in {"Q01", "Q15"}:
        targets = ([kg.resource("course", row["courseCode"]) for row in result["rows"]]
                   if intent == "Q01" else [c for plan in kg.objects(kg.resource("student", student), UCA.hasPlannedEnrollment)
                                           for c in kg.objects(plan, UCA.plannedCourse)])
        for target in sorted(set(targets), key=str):
            result["reasoning"].append(reasoner.reason("eligibility", student=student, course=target, term=term, concurrent=intent != "Q15"))
    evidence = {}

    def add(edge):
        evidence[edge["id"]] = edge

    for trace in result["reasoning"]:
        for path in trace["paths"]:
            for edge in path:
                add(edge)
        result["limitations"].extend(trace.get("warnings", []))
    # A bounded query-specific subgraph. Rows remain separate derived records,
    # never reified as invented RDF facts.
    seeds = {kg.resource("course", c) for c in entities["courses"]}
    if student:
        seeds.add(kg.resource("student", student))
    if intent in {"Q06", "Q09", "Q11"}:
        seeds.add(RES["program/UIUC-BS-CS-2026"])
    code_keys = {"courseCode", "fromCode", "toCode", "upstreamCode", "viaCode", "alias", "downstreamCode"}
    for row in result["rows"]:
        for key, value in row.items():
            if value is None:
                continue
            if key in code_keys:
                seeds.add(kg.resource("course", value))
            if key == "requirement":
                seeds.update(kg.explicit.subjects(RDFS.label, Literal(value)))
    for seed in sorted(seeds, key=str):
        for edge in kg.outgoing(seed):
            add(edge)
        # Expand structural nodes, not arbitrary neighbors or entire departments.
        for p in (UCA.hasPrerequisiteExpression, UCA.hasCompletion, UCA.hasPlannedEnrollment, UCA.hasOffering, UCA.hasRequirement):
            for node in kg.objects(seed, p):
                for edge in kg.outgoing(node):
                    add(edge)
                if p == UCA.hasPrerequisiteExpression:
                    for option in kg.objects(node, UCA.hasOption):
                        for edge in kg.outgoing(option):
                            add(edge)
                        for cond in kg.objects(option, UCA.hasCondition):
                            for edge in kg.outgoing(cond):
                                add(edge)
    if intent == "Q11":
        req, t = RES["requirement/UIUC-BS-CS-2026/Elective-Advanced"], kg.resource("term", term)
        for c in kg.objects(req, UCA.allowsCourse):
            if (c, UCA.scheduledInTerm, t) not in kg.closure:
                continue
            for d in kg.objects(c, UCA.inDepartment):
                for triple in ((d, UCA.hasCourse, c), (c, UCA.maySatisfyRequirement, req), (c, UCA.scheduledInTerm, t)):
                    add(kg.edge(*triple))
                for triple in ((c, UCA.inDepartment, d), (req, UCA.allowsCourse, c)):
                    add(kg.edge(*triple))
                for o in kg.objects(c, UCA.hasOffering):
                    if t in kg.objects(o, UCA.offeredInTerm):
                        add(kg.edge(c, UCA.hasOffering, o)); add(kg.edge(o, UCA.offeredInTerm, t))
    result["evidence"] = list(evidence.values())
    # No-result queries are abstentions, not assertions that no real-world course exists.
    result["sufficient"] = bool(result["rows"] or result["reasoning"])
    if not result["sufficient"]:
        result["limitations"].append("Query returned no records in this snapshot; no real-world conclusion is justified.")
    result["limitations"] = sorted(set(result["limitations"]))
    return result
