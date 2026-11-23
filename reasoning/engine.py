"""Day 3: prerequisite chains and recorded degree-requirement allocation reasoning.

Eligibility and reverse unlock are integrated on later days.
"""
from __future__ import annotations
from collections import deque
from decimal import Decimal
from time import perf_counter
from rdflib.namespace import RDF, RDFS
from .kg import KG, UCA, RES


class Reasoner:
    def __init__(self, kg=None, max_depth=32, max_paths=20000):
        if max_depth < 1 or max_paths < 1:
            raise ValueError("Depth and path limits must be positive")
        self.kg = kg or KG()
        self.max_depth, self.max_paths = max_depth, max_paths
        self.adj = {c: list(self.kg.course_edges(c)) for c in self.kg.courses}


    def reason(self, template, **kwargs):
        started = perf_counter()
        methods = {"prerequisite_chain": self.chain, "degree_progress": self.progress}
        if template not in methods:
            raise ValueError(f"Unknown template {template}; choose {list(methods)}")
        result = methods[template](**kwargs)
        result.update(template=template, graph_sha256=self.kg.sha256,
                      runtime_ms=(perf_counter() - started) * 1000,
                      predictions=[], knowledge_type="verified traversal and application rules")
        return result


    @staticmethod
    def result(answer, paths=None, verdict="no_path", unmet=None, **extra):
        return {"answer": answer, "paths": paths or [], "verdict": verdict, "unmet": unmet or [], **extra}


    def reachable(self, course):
        """Unbounded visited-set closure for evaluation; includes self if a cycle returns to it."""
        start = self.kg.resource("course", course)
        visited, queue = set(), deque([start])
        while queue:
            for target, *_ in self.adj.get(queue.popleft(), []):
                if target not in visited:
                    visited.add(target)
                    queue.append(target)
        return visited


    def chain(self, course):
        kg, start = self.kg, self.kg.resource("course", course)
        if start not in kg.courses:
            return self.result("Unknown course: no catalog evidence.", unmet=["unknown_course"])
        paths, branches, tree, seen_nodes = [], [], {}, set()
        truncated = False

        def walk(node, ancestry, path, branch, depth):
            nonlocal truncated
            seen_nodes.add(node)
            # Tree metadata keeps conjunctions/choices separate; paths are NOT schedules.
            if str(node) not in tree:
                tree[str(node)] = self._expression_tree(node)
            edges = self.adj.get(node, [])
            reason = ("cycle" if node in ancestry else "root" if not edges else
                      "depth_limit" if depth >= self.max_depth else None)
            if reason:
                paths.append(path)
                branches.append({"courses": branch, "stop": reason, "course_hops": depth})
                truncated |= reason == "depth_limit"
                return
            for target, step, option, condition in edges:
                if len(paths) >= self.max_paths:
                    truncated = True
                    return
                walk(target, ancestry | {node}, path + step,
                     branch + [{"course": kg.code(target), "option": str(option),
                                "condition": str(condition)}], depth + 1)

        walk(start, set(), [], [{"course": kg.code(start)}], 0)
        warnings = ["Paths show possible prerequisites, not a claim that every alternative is compulsory."]
        if truncated:
            warnings.append("Traversal truncated: inspect limits before claiming complete chains.")
        return self.result(f"Possible prerequisite chains for {kg.code(start)}.", paths, "satisfied",
                           branches=branches, expression_tree=tree, truncated=truncated,
                           reachable=sorted(kg.code(n) for n in seen_nodes - {start}), warnings=warnings)


    def _expression_tree(self, course):
        kg, result = self.kg, []
        for expr in kg.objects(course, UCA.hasPrerequisiteExpression):
            result.append({"expression": str(expr), "parseStatus": str(kg.value(expr, UCA.parseStatus, "unknown")),
                           "operator": "OR", "options": [
                {"option": str(opt), "operator": "AND", "conditions": [
                    {"condition": str(cond), "types": list(map(str, kg.objects(cond, RDF.type))),
                     "text": str(kg.value(cond, UCA.conditionSourceText, "")),
                     "required": [kg.code(x) for x in kg.objects(cond, UCA.requiredCourse)],
                     "one_of": [kg.code(x) for x in kg.objects(cond, UCA.alternativeCourse)]}
                    for cond in kg.objects(opt, UCA.hasCondition)]}
                for opt in kg.objects(expr, UCA.hasOption)]})
        return result

    def progress(self, student, program="UIUC-BS-CS-2026"):
        kg, s, prog = self.kg, self.kg.resource("student", student), self.kg.resource("program", program)
        reqs = kg.objects(prog, UCA.hasRequirement)
        if (s, RDF.type, UCA.Student) not in kg.explicit or not reqs:
            return self.result("Insufficient evidence: unknown student or program.", unmet=["unknown_entity"])
        rows, paths, conflicts = [], [], []
        technical = RES[f"requirement/{program}/Elective-Technical"]
        advanced = RES[f"requirement/{program}/Elective-Advanced"]
        for cp in kg.objects(s, UCA.hasCompletion):
            allocated = set(kg.objects(cp, UCA.allocatedToRequirement))
            if {technical, advanced} <= allocated:
                conflicts.append({"completion": str(cp), "rule": "technical/advanced electives must be distinct",
                                  "requirements": [str(technical), str(advanced)]})
        for req in reqs:
            allocated = [cp for cp in kg.objects(s, UCA.hasCompletion) if req in kg.objects(cp, UCA.allocatedToRequirement)]
            credits = sum((Decimal(str(kg.value(cp, UCA.creditsEarned, 0))) for cp in allocated), Decimal(0))
            minimum, min_credits = kg.value(req, UCA.minCourses), kg.value(req, UCA.minCredits)
            remaining = max(0, int(minimum) - len(allocated)) if minimum is not None else None
            rem_credits = max(Decimal(0), Decimal(str(min_credits)) - credits) if min_credits is not None else None
            invalid = []
            for cp in allocated:
                paths.append([kg.edge(s, UCA.hasCompletion, cp), kg.edge(cp, UCA.allocatedToRequirement, req),
                              dict(kg.edge(prog, UCA.hasRequirement, req), direction="reverse")])
                for c in kg.objects(cp, UCA.completedCourse):
                    paths.append([kg.edge(s, UCA.hasCompletion, cp), kg.edge(cp, UCA.completedCourse, c)])
                    if (req, UCA.allowsCourse, c) not in kg.explicit:
                        invalid.append(kg.code(c))
            rows.append({"requirement": str(kg.value(req, RDFS.label, req)), "iri": str(req),
                         "minCourses": int(minimum) if minimum is not None else None,
                         "allocatedCourses": len(allocated), "remainingCourses": remaining,
                         "minCredits": float(min_credits) if min_credits is not None else None,
                         "allocatedCredits": float(credits), "remainingCredits": float(rem_credits) if rem_credits is not None else None,
                         "encoded_thresholds_met": remaining in (None, 0) and rem_credits in (None, 0),
                         "invalid_allocations": invalid,
                         "note": str(kg.value(req, UCA.requirementNote, ""))})
        return self.result(f"Recorded degree allocations for synthetic student {student}; not a certified graduation audit.",
                           paths, "unmet" if conflicts or any(not r["encoded_thresholds_met"] for r in rows) else "satisfied",
                           unmet=[r for r in rows if not r["encoded_thresholds_met"]], requirements=rows,
                           conflicts=conflicts, warnings=["Focus areas are alternatives; do not require every focus area.",
                           "GPA, grades, special permissions and prose credit restrictions need an adviser audit.",
                           "Recorded allocations are counted and validated, not automatically optimized."])

