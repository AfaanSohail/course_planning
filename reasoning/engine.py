"""Day 2: bounded prerequisite chains with intermediate entities and AND/OR structure.

Eligibility, reverse unlock and degree progress are integrated on later days.
"""
from __future__ import annotations
from collections import deque
from time import perf_counter
from rdflib.namespace import RDF
from .kg import KG, UCA


class Reasoner:
    def __init__(self, kg=None, max_depth=32, max_paths=20000):
        if max_depth < 1 or max_paths < 1:
            raise ValueError("Depth and path limits must be positive")
        self.kg = kg or KG()
        self.max_depth, self.max_paths = max_depth, max_paths
        self.adj = {c: list(self.kg.course_edges(c)) for c in self.kg.courses}


    def reason(self, template, **kwargs):
        started = perf_counter()
        methods = {"prerequisite_chain": self.chain}
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

