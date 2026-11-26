"""Option C: deterministic bounded traversal plus AND/OR rule evaluation.

An edge is a graph fact. A verdict is a closed-world application rule result.
Hypothetical completions are assumptions in the trace, never evidence edges.
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
        methods = {"prerequisite_chain": self.chain, "eligibility": self.eligibility,
                   "reverse_unlock": self.unlock, "degree_progress": self.progress}
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

    def completions(self, student):
        return {c for cp in self.kg.objects(student, UCA.hasCompletion)
                for c in self.kg.objects(cp, UCA.completedCourse)}

    def eligibility(self, student, course, term="2026-fa", added=None, concurrent=True):
        kg = self.kg
        s, c = kg.resource("student", student), kg.resource("course", course)
        t = kg.resource("term", term)
        if (s, RDF.type, UCA.Student) not in kg.explicit or c not in kg.courses:
            return self.result("Insufficient evidence: unknown student or course.", unmet=["unknown_entity"])
        done = self.completions(s)
        assumptions = {kg.resource("course", a) for a in (added or [])}
        if any(a not in kg.courses for a in assumptions):
            return self.result("Insufficient evidence: unknown hypothetical course.", unmet=["unknown_assumption"])
        plans = {x for plan in kg.objects(s, UCA.hasPlannedEnrollment)
                 if t in kg.objects(plan, UCA.plannedTerm) for x in kg.objects(plan, UCA.plannedCourse)}
        paths, options, warnings = [], [], []
        exprs = kg.objects(c, UCA.hasPrerequisiteExpression)
        for expr in exprs:
            if str(kg.value(expr, UCA.parseStatus, "unknown")) != "parsed":
                warnings.append("Prerequisite parsing needs review; verdict covers encoded conditions only.")
            for opt in kg.objects(expr, UCA.hasOption):
                conditions = []
                for cond in kg.objects(opt, UCA.hasCondition):
                    base = [kg.edge(c, UCA.hasPrerequisiteExpression, expr), kg.edge(expr, UCA.hasOption, opt),
                            kg.edge(opt, UCA.hasCondition, cond)]
                    types = set(kg.objects(cond, RDF.type))
                    candidates = set(kg.objects(cond, UCA.requiredCourse) + kg.objects(cond, UCA.alternativeCourse))
                    met, basis, support = False, "unverified", []
                    if types & {UCA.CourseCondition, UCA.CourseChoiceCondition}:
                        allow = kg.value(cond, UCA.allowsConcurrent)
                        may_plan = concurrent and allow is not None and allow.toPython() is True
                        matches = candidates & (done | assumptions | (plans if may_plan else set()))
                        met = bool(matches)
                        for match in sorted(matches, key=str):
                            prop = UCA.requiredCourse if match in kg.objects(cond, UCA.requiredCourse) else UCA.alternativeCourse
                            paths.append(base + [kg.edge(cond, prop, match)])
                            if match in done:
                                basis = "completed"
                                for cp in kg.objects(s, UCA.hasCompletion):
                                    if match in kg.objects(cp, UCA.completedCourse):
                                        support += [kg.edge(s, UCA.hasCompletion, cp), kg.edge(cp, UCA.completedCourse, match)]
                            elif match in assumptions:
                                basis = "hypothetical completion (assumption, not a stored fact)"
                            else:
                                basis = "concurrent plan in target term"
                                support.append(kg.edge(cond, UCA.allowsConcurrent, allow))
                                for plan in kg.objects(s, UCA.hasPlannedEnrollment):
                                    if match in kg.objects(plan, UCA.plannedCourse) and t in kg.objects(plan, UCA.plannedTerm):
                                        paths.append([kg.edge(s, UCA.hasPlannedEnrollment, plan), kg.edge(plan, UCA.plannedCourse, match)])
                                        support.append(kg.edge(plan, UCA.plannedTerm, t))
                        if not met:
                            for match in sorted(candidates, key=str):
                                prop = UCA.requiredCourse if match in kg.objects(cond, UCA.requiredCourse) else UCA.alternativeCourse
                                paths.append(base + [kg.edge(cond, prop, match)])
                    elif UCA.StandingCondition in types:
                        rank, minimum = kg.value(s, UCA.standingRank), kg.value(cond, UCA.minimumStandingRank)
                        met = rank is not None and minimum is not None and int(rank) >= int(minimum)
                        basis = "standing comparison"
                        if rank is not None:
                            support.append(kg.edge(s, UCA.standingRank, rank))
                        if minimum is not None:
                            support.append(kg.edge(cond, UCA.minimumStandingRank, minimum))
                    elif UCA.ConsentCondition in types:
                        met = (s, UCA.hasPermissionFor, c) in kg.explicit
                        basis = "explicit course permission" if met else "permission not recorded"
                        if met:
                            support.append(kg.edge(s, UCA.hasPermissionFor, c))
                    else:
                        basis = "free text or unknown condition; needs manual review"
                    paths.append(base)
                    paths.extend([[edge] for edge in support])
                    conditions.append({"condition": str(cond), "text": str(kg.value(cond, UCA.conditionSourceText, "")),
                                       "met": met, "basis": basis, "status": "inferred",
                                       "candidates": sorted(kg.code(x) for x in candidates)})
                # A malformed empty option must not silently authorize registration.
                options.append({"option": str(opt), "met": bool(conditions) and all(x["met"] for x in conditions),
                                "conditions": conditions})
        has_offering = False
        for offering in kg.objects(c, UCA.hasOffering):
            if t in kg.objects(offering, UCA.offeredInTerm):
                has_offering = True
                paths.append([kg.edge(c, UCA.hasOffering, offering), kg.edge(offering, UCA.offeredInTerm, t)])
        catalog_known = bool(kg.objects(c, UCA.sourceURL)) and bool(kg.objects(c, UCA.courseTitle))
        ok = any(o["met"] for o in options) if exprs else catalog_known
        unmet = [{"option": o["option"], "conditions": [x for x in o["conditions"] if not x["met"]]}
                 for o in options if not o["met"]]
        if not exprs and not catalog_known:
            unmet = ["stub_course: no catalog prerequisite evidence"]
        if not exprs and catalog_known:
            paths.extend([[kg.edge(c, RDF.type, UCA.Course)]])
            warnings.append("No recorded prerequisite; this is a snapshot closed-world result, not unconditional permission.")
        return self.result(f"{kg.code(c)}: encoded prerequisites {'satisfied' if ok else 'unmet or unverified'} for {student}.",
                           paths, "satisfied" if ok else "unmet", unmet=unmet, options=options,
                           assumptions=sorted(kg.code(x) for x in assumptions), warnings=sorted(set(warnings)),
                           offered_in_term=has_offering, already_completed=c in done,
                           registration_ready=ok and has_offering and c not in done,
                           has_recorded_prerequisites=bool(exprs), student_is_synthetic=True)

    def unlock(self, student, course, term="2026-fa", concurrent=True):
        kg, added = self.kg, self.kg.resource("course", course)
        s = kg.resource("student", student)
        if added not in kg.courses or (s, RDF.type, UCA.Student) not in kg.explicit:
            return self.result("Insufficient evidence: unknown student or course.", unmet=["unknown_entity"])
        dependants, paths = [], []
        # Multi-hop relevance does not imply immediate eligibility: test each target independently.
        for target in kg.courses:
            if target == added or added not in self.reachable(target):
                continue
            before = self.eligibility(student, target, term=term, concurrent=concurrent)
            after = self.eligibility(student, target, term=term, added=[course], concurrent=concurrent)
            if after["already_completed"]:
                continue
            chain = self._path_to(target, added)
            paths.extend([chain] if chain else [])
            paths.extend(before["paths"])
            paths.extend(after["paths"])
            direct = any(x[0] == added for x in self.adj.get(target, []))
            dependants.append({"course": kg.code(target), "direct": direct,
                               "newly_satisfied": before["verdict"] != "satisfied" and after["verdict"] == "satisfied",
                               "offered_in_term": after["offered_in_term"], "dependency_path_truncated": not bool(chain),
                               "before": before["verdict"], "after": after["verdict"], "unmet": after["unmet"],
                               "options_after": after["options"]})
        return self.result(f"Hypothetical impact of completing {kg.code(added)} for {student}.", paths,
                           "satisfied" if dependants else "no_path", dependants=dependants,
                           assumptions=[kg.code(added)], warnings=["Hypothetical completion is evaluated in memory; the stored KG is unchanged. This does not prevent what-if reasoning."])

    def _path_to(self, source, destination):
        queue, seen = deque([(source, [], 0)]), {source}
        while queue:
            node, path, depth = queue.popleft()
            if node == destination:
                return path
            if depth >= self.max_depth:
                continue
            for target, edges, *_ in self.adj.get(node, []):
                if target not in seen:
                    seen.add(target)
                    queue.append((target, path + edges, depth + 1))
        return []

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
