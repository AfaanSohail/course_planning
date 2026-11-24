"""Check stored/OWL-inferred provenance and hypothetical completion labels."""
import pytest
from reasoning import KG, Reasoner
from reasoning.kg import ROOT, RES, UCA
from rdflib import Graph


@pytest.fixture(scope="module")
def kg():
    return KG()


def test_completion_shortcut_is_inferred_from_stored_premises(kg):
    student, course = RES["student/S003"], RES["course/CS124"]
    completion = next(cp for cp in kg.objects(student, UCA.hasCompletion)
                      if course in kg.objects(cp, UCA.completedCourse))
    assert (student, UCA.hasCompletedCourse, course) not in kg.explicit
    assert kg.edge(student, UCA.hasCompletion, completion)["status"] == "explicit"
    assert kg.edge(completion, UCA.completedCourse, course)["status"] == "explicit"
    # Apply the real schema to just these real premises, keeping this unit test small.
    proof_graph = Graph().parse(ROOT / "iteration1/Ontology/uca_ontology.ttl")
    proof_graph.add((student, UCA.hasCompletion, completion))
    proof_graph.add((completion, UCA.completedCourse, course))
    proof = KG(graph=proof_graph)
    edge = proof.edge(student, UCA.hasCompletedCourse, course)
    assert edge["status"] == "inferred"
    assert proof.valid_edge(edge)


def test_hypothetical_completion_is_an_assumption_not_a_graph_fact(kg):
    reasoner = Reasoner(kg)
    before = set(kg.explicit)
    baseline = reasoner.reason("eligibility", student="S003", course="CS421")
    after = reasoner.reason("eligibility", student="S003", course="CS421", added=["CS374"])
    assert baseline["verdict"] == "unmet"
    assert after["verdict"] == "satisfied"
    assert after["assumptions"] == [kg.code(RES["course/CS374"])]
    assert after["predictions"] == []
    assert all(kg.valid_path(path) for path in after["paths"])
    assert set(kg.explicit) == before
