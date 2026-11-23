"""Validate the reasoning features available through Day 3.

Catalog checks use the real preserved KG. The small RDF fixture isolates a
credit-shortfall case without depending on an accidental catalog example.
"""
from decimal import Decimal
import hashlib

import pytest
from rdflib import Graph, Literal
from rdflib.namespace import RDF

from reasoning import KG, Reasoner
from reasoning.kg import DEFAULT_KG, PREFIXES, RES, STEP, UCA
from evaluation.queries import run_query


@pytest.fixture(scope="module")
def kg():
    return KG()


@pytest.fixture(scope="module")
def reasoner(kg):
    return Reasoner(kg)


def test_loader_preserves_snapshot_hash_and_course_index(kg):
    assert kg.sha256 == hashlib.sha256(DEFAULT_KG.read_bytes()).hexdigest()
    assert set(kg.courses) == set(kg.explicit.subjects(RDF.type, UCA.Course))
    assert kg.courses


def test_reachability_agrees_with_sparql(reasoner, kg):
    query = PREFIXES + f"SELECT DISTINCT ?target WHERE {{ <course/CS421> ({STEP})+ ?target . }}"
    expected = {row.target for row in kg.explicit.query(query)}
    assert expected
    assert reasoner.reachable("CS421") == expected


def test_chains_preserve_real_connected_edges_and_options(reasoner, kg):
    result = reasoner.reason("prerequisite_chain", course="CS421")
    assert result["paths"] and not result["truncated"]
    assert all(kg.valid_path(path) for path in result["paths"])
    expression = result["expression_tree"][str(RES["course/CS421"])][0]
    assert expression["operator"] == "OR"
    assert all(option["operator"] == "AND" for option in expression["options"])


def test_catalog_cycle_stops_with_valid_evidence(reasoner, kg):
    result = reasoner.reason("prerequisite_chain", course="CHEM202")
    assert any(branch["stop"] == "cycle" for branch in result["branches"])
    assert all(kg.valid_path(path) for path in result["paths"])


def test_depth_and_path_limits_are_reported(kg):
    shallow = Reasoner(kg, max_depth=1).reason("prerequisite_chain", course="CS421")
    assert shallow["truncated"]
    assert any(branch["stop"] == "depth_limit" for branch in shallow["branches"])
    bounded = Reasoner(kg, max_paths=1).reason("prerequisite_chain", course="CS421")
    assert bounded["truncated"] and len(bounded["paths"]) == 1


def test_unknown_entities_have_no_verified_answer(reasoner):
    assert reasoner.reason("prerequisite_chain", course="ZZZZ999")["verdict"] == "no_path"
    assert reasoner.reason("degree_progress", student="S999")["verdict"] == "no_path"


def test_degree_allocations_agree_with_original_q06(reasoner, kg):
    expected = {row["requirement"]: row for row in run_query(kg, "Q06")}
    actual = reasoner.reason("degree_progress", student="S003")
    assert {row["requirement"] for row in actual["requirements"]} == set(expected)
    for row in actual["requirements"]:
        reference = expected[row["requirement"]]
        assert row["allocatedCourses"] == int(reference["allocatedCourses"])
        assert Decimal(str(row["allocatedCredits"])) == Decimal(reference["allocatedCredits"])
        if row["remainingCourses"] is not None:
            assert row["remainingCourses"] == int(reference["remainingCourses"])
    assert all(kg.valid_path(path) for path in actual["paths"])


def test_seeded_double_count_is_flagged(reasoner):
    result = reasoner.reason("degree_progress", student="S004")
    assert result["conflicts"]
    assert result["verdict"] == "unmet"
    assert any(conflict["completion"].endswith("/CS411") for conflict in result["conflicts"])


def test_credit_shortfall_blocks_a_met_course_count():
    graph = Graph()
    student, program = RES["student/S900"], RES["program/TEST"]
    completion, course = RES["completion/S900/CS100"], RES["course/CS100"]
    requirement = RES["requirement/TEST/Core"]
    for triple in [
        (student, RDF.type, UCA.Student),
        (student, UCA.hasCompletion, completion),
        (completion, UCA.completedCourse, course),
        (completion, UCA.allocatedToRequirement, requirement),
        (completion, UCA.creditsEarned, Literal(3)),
        (program, UCA.hasRequirement, requirement),
        (requirement, UCA.allowsCourse, course),
        (requirement, UCA.minCourses, Literal(1)),
        (requirement, UCA.minCredits, Literal(4)),
    ]:
        graph.add(triple)
    result = Reasoner(KG(graph=graph)).reason("degree_progress", student="S900", program="TEST")
    row = result["requirements"][0]
    assert row["remainingCourses"] == 0
    assert row["remainingCredits"] == 1
    assert not row["encoded_thresholds_met"]
    assert result["verdict"] == "unmet"


def test_reasoning_does_not_mutate_explicit_graph(reasoner, kg):
    before = set(kg.explicit)
    reasoner.reason("degree_progress", student="S004")
    reasoner.reason("prerequisite_chain", course="CS421")
    assert set(kg.explicit) == before
