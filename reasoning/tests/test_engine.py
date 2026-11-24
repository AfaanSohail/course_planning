"""Small synthetic RDF fixtures isolate semantics from catalog accidents."""
import pytest
from rdflib import Graph, Literal
from rdflib.namespace import RDF
from reasoning import KG, Reasoner
from reasoning.kg import UCA, RES


@pytest.fixture
def fixture():
    g = Graph()
    def add(s, p, o):
        g.add((s, p, o))
    s = RES["student/S900"]
    add(s, RDF.type, UCA.Student); add(s, UCA.standingRank, Literal(2))
    for code in ["CS100", "CS200", "CS300", "CS400", "CS500", "CS600"]:
        c = RES["course/" + code]
        add(c, RDF.type, UCA.Course); add(c, UCA.courseCode, Literal(code))
        add(c, UCA.courseTitle, Literal(code)); add(c, UCA.sourceURL, Literal("fixture"))
    def option(code, number, conditions):
        c, e = RES["course/" + code], RES["prereq/" + code]
        opt = RES[f"prereq/{code}/option/{number}"]
        add(c, UCA.hasPrerequisiteExpression, e); add(e, UCA.parseStatus, Literal("parsed")); add(e, UCA.hasOption, opt)
        for i, (typ, prop, values) in enumerate(conditions):
            k = RES[f"prereq/{code}/option/{number}/condition/{i}"]
            add(opt, UCA.hasCondition, k); add(k, RDF.type, typ); add(k, UCA.conditionSourceText, Literal(str(i)))
            for v in values:
                add(k, prop, v)
        return opt
    def complete(code):
        cp = RES["completion/S900/" + code]
        add(s, UCA.hasCompletion, cp); add(cp, UCA.completedCourse, RES["course/" + code])
    complete("CS100")
    option("CS300",1,[(UCA.CourseChoiceCondition,UCA.alternativeCourse,[RES["course/CS100"],RES["course/CS200"]]),
                      (UCA.StandingCondition,UCA.minimumStandingRank,[Literal(3)])])
    option("CS300",2,[(UCA.ConsentCondition,UCA.conditionSourceText,[Literal("consent")])])
    option("CS400",1,[(UCA.CourseCondition,UCA.requiredCourse,[RES["course/CS500"]])])
    option("CS500",1,[(UCA.CourseCondition,UCA.requiredCourse,[RES["course/CS400"]])])
    option("CS600",1,[(UCA.OtherCondition,UCA.conditionSourceText,[Literal("experience")])])
    return g, s


def test_and_inside_or_between(fixture):
    g,s = fixture; r=Reasoner(KG(graph=g))
    x=r.reason("eligibility",student=s,course="CS300")
    assert x["verdict"] == "unmet"
    assert x["options"][0]["conditions"][0]["met"]
    g.add((s,UCA.hasPermissionFor,RES["course/CS300"]))
    assert r.reason("eligibility",student=s,course="CS300")["verdict"] == "satisfied"


def test_concurrency_requires_target_term(fixture):
    g,s=fixture; c=RES["course/CS400"]; cond=RES["prereq/CS400/option/1/condition/0"]
    g.add((cond,UCA.allowsConcurrent,Literal(True)))
    plan=RES["plan/S900/CS500/2026-sp"]
    g.add((s,UCA.hasPlannedEnrollment,plan)); g.add((plan,UCA.plannedCourse,RES["course/CS500"]))
    g.add((plan,UCA.plannedTerm,RES["term/2026-sp"]))
    r=Reasoner(KG(graph=g))
    assert r.reason("eligibility",student=s,course=c,term="2026-fa")["verdict"] == "unmet"
    assert r.reason("eligibility",student=s,course=c,term="2026-sp")["verdict"] == "satisfied"


def test_cycles_depth_and_edge_provenance(fixture):
    g,_=fixture; kg=KG(graph=g); r=Reasoner(kg)
    result=r.reason("prerequisite_chain",course="CS400")
    assert any(b["stop"] == "cycle" for b in result["branches"])
    assert all(kg.valid_edge(e) for p in result["paths"] for e in p)
    assert RES["course/CS400"] in r.reachable("CS400")
    shallow=Reasoner(kg,max_depth=1).reason("prerequisite_chain",course="CS400")
    assert shallow["truncated"]
    assert shallow["branches"][0]["stop"] == "depth_limit"


def test_unknown_stub_and_free_text(fixture):
    g,s=fixture; stub=RES["course/CS999"]; g.add((stub,RDF.type,UCA.Course))
    r=Reasoner(KG(graph=g))
    assert r.reason("eligibility",student=s,course="CS600")["verdict"] == "unmet"
    assert r.reason("eligibility",student=s,course=stub)["verdict"] == "unmet"
    assert r.reason("eligibility",student="S999",course="CS100")["verdict"] == "no_path"
    assert r.reason("prerequisite_chain",course="FAKE999")["verdict"] == "no_path"


def test_hypothetical_does_not_change_graph(fixture):
    g,s=fixture; before=set(g); r=Reasoner(KG(graph=g))
    x=r.reason("eligibility",student=s,course="CS400",added=["CS500"])
    assert x["verdict"] == "satisfied"
    assert set(g) == before
    assert all(r.kg.valid_edge(e) for p in x["paths"] for e in p)


def test_progress_and_distinct_electives(fixture):
    g,s=fixture; prog=RES["program/P"]; cp=RES["completion/S900/CS100"]
    for name in ["Elective-Technical","Elective-Advanced"]:
        req=RES["requirement/P/"+name]
        g.add((prog,UCA.hasRequirement,req));g.add((req,UCA.minCourses,Literal(1)))
        g.add((req,UCA.minCredits,Literal(4)));g.add((req,UCA.allowsCourse,RES["course/CS100"]))
        g.add((cp,UCA.allocatedToRequirement,req))
    g.add((cp,UCA.creditsEarned,Literal(3)))
    x=Reasoner(KG(graph=g)).reason("degree_progress",student=s,program="P")
    assert len(x["conflicts"]) == 1
    assert x["requirements"][0]["remainingCourses"] == 0
    assert x["requirements"][0]["remainingCredits"] == 1
    assert x["verdict"] == "unmet"


def test_path_limit_and_option_structure(fixture):
    g,_=fixture; r=Reasoner(KG(graph=g),max_paths=1)
    x=r.reason("prerequisite_chain",course="CS300")
    assert x["truncated"] and len(x["paths"]) == 1
    tree=x["expression_tree"][str(RES["course/CS300"])][0]
    assert tree["operator"] == "OR" and tree["options"][0]["operator"] == "AND"
