"""Immutable explicit snapshot, optional OWL RL closure, and typed RDF evidence.

Never write a completion, hypothetical fact, or prediction into either graph.
N3 term strings preserve literal datatypes, languages and blank-node identity.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, RDFS
from rdflib.util import from_n3

ROOT = Path(__file__).resolve().parents[1]
UCA = Namespace("https://example.org/uiuc-course-advisor/ontology#")
RES = Namespace("https://example.org/uiuc-course-advisor/resource/")
DEFAULT_KG = ROOT / "iteration1/RDF_Knowledge_Graph/uiuc_course_kg.ttl"
PREFIXES = f"BASE <{RES}>\nPREFIX uca: <{UCA}>\nPREFIX rdfs: <{RDFS}>\nPREFIX rdf: <{RDF}>\n"
STEP = "uca:hasPrerequisiteExpression/uca:hasOption/uca:hasCondition/(uca:requiredCourse|uca:alternativeCourse)"


def save_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


class KG:
    def __init__(self, path=DEFAULT_KG, graph=None):
        self.path = Path(path)
        self.explicit = graph if graph is not None else Graph().parse(self.path, format="turtle")
        self._closure = None
        self.sha256 = (hashlib.sha256(self.path.read_bytes()).hexdigest()
                       if graph is None else "unit-test-fixture")
        self.courses = sorted(set(self.explicit.subjects(RDF.type, UCA.Course)), key=str)

    @property
    def closure(self):
        if self._closure is None:
            from owlrl import DeductiveClosure, OWLRL_Semantics
            self._closure = Graph()
            self._closure += self.explicit
            DeductiveClosure(OWLRL_Semantics).expand(self._closure)
        return self._closure

    def resource(self, kind, value):
        if isinstance(value, URIRef):
            return value
        if str(value).startswith(str(RES)):
            return URIRef(value)
        code = str(value).upper().replace(" ", "") if kind == "course" else str(value)
        return RES[f"{kind}/{code}"]

    def objects(self, s, p):
        return sorted(set(self.explicit.objects(s, p)), key=str)

    def value(self, s, p, default=None):
        return self.explicit.value(s, p, default=default)

    def code(self, node):
        return str(self.value(node, UCA.courseCode, str(node).split("/")[-1]))

    def edge(self, s, p, o):
        triple = (s, p, o)
        if triple in self.explicit:
            status = "explicit"
        elif triple in self.closure:
            status = "inferred"
        else:
            raise ValueError(f"Not a graph fact: {triple!r}")
        terms = [x.n3() for x in triple]
        return dict(zip(("s", "p", "o"), terms), status=status,
                    id="E" + hashlib.sha256(" ".join(terms).encode()).hexdigest()[:16])

    def valid_edge(self, edge):
        triple = tuple(from_n3(edge[k]) for k in ("s", "p", "o"))
        if edge["status"] == "explicit":
            return triple in self.explicit
        return edge["status"] == "inferred" and triple not in self.explicit and triple in self.closure

    def outgoing(self, node):
        return [self.edge(node, p, o) for p, o in sorted(self.explicit.predicate_objects(node), key=lambda x: tuple(map(str, x)))]

    def valid_path(self, path):
        previous = None
        for edge in path:
            if not self.valid_edge(edge):
                return False
            start, end = (edge["o"], edge["s"]) if edge.get("direction") == "reverse" else (edge["s"], edge["o"])
            if previous is not None and previous != start:
                return False
            previous = end
        return True

    def course_edges(self, course):
        """Each hop contains the actual expression, option, condition and course."""
        for expr in self.objects(course, UCA.hasPrerequisiteExpression):
            for option in self.objects(expr, UCA.hasOption):
                for condition in self.objects(option, UCA.hasCondition):
                    for prop in (UCA.requiredCourse, UCA.alternativeCourse):
                        for target in self.objects(condition, prop):
                            triples = [(course, UCA.hasPrerequisiteExpression, expr),
                                       (expr, UCA.hasOption, option),
                                       (option, UCA.hasCondition, condition), (condition, prop, target)]
                            yield target, [self.edge(*t) for t in triples], option, condition

    def query(self, text, inferred=False):
        result = (self.closure if inferred else self.explicit).query(text)
        return [{str(v): str(row[v]) if row[v] is not None else None for v in result.vars} for row in result]
