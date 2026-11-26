import json
import pytest
from app.config import Config
from app.linking import link, route
from app.service import Advisor, context_for
from app.llm import LLMClient, LLMError
from reasoning import KG, Reasoner
from explainability.format import format_answer


class SpyClient:
    """Test-only transport spy; never selectable by experiment CLI."""
    def __init__(self): self.calls=[]
    def complete(self,messages):
        self.calls.append(messages)
        return {"answer":"Test transport response", "request":{"messages":messages}, "raw":{}, "truncated":False}


@pytest.fixture(scope="module")
def reasoner():
    return Reasoner(KG())


def test_linking_and_unseen_codes():
    e=link("Can S003 take cs-421 in Fall 2026?")
    assert e == {"courses":["CS421"],"students":["S003"],"terms":["2026-fa"]}
    assert route("Can S003 take cs-421 in Fall 2026?",e) == "Q03"


def test_downstream_blockers_distinct_from_hypothetical_set_change():
    q="If S002 completes one additional course CS 225, which downstream courses may become available and what other conditions hold? Hypothetically in Fall 2026."
    assert route(q,link(q)) == "Q04"
    q="How does the set of satisfiable options change when S002 hypothetically adds CS 225 in Fall 2026?"
    assert route(q,link(q)) == "Q13"


@pytest.mark.parametrize("question",[
    "What is the weather for CS 421?", "Can S999 take CS 421 in Fall 2026?",
    "Can S003 take CS 999 in Fall 2026?", "Can S003 take CS 421 in Fall 2027?",
    "Can a student take CS 421?", "Can S003 take CS 421 or CS 225?",
])
def test_missing_evidence_never_calls_llm(reasoner,question):
    spy=SpyClient(); answer=Advisor(reasoner=reasoner,client=spy).answer(question)
    assert answer["mode"] == "insufficient_evidence"
    assert not spy.calls and not answer["llm_called"]


def test_baseline_isolation(reasoner):
    spy=SpyClient(); answer=Advisor(reasoner=reasoner,client=spy).answer("Can S003 take CS 421?",mode="baseline")
    assert answer["evidence"] == []
    assert len(spy.calls[0]) == 2
    assert "CONTEXT:" not in spy.calls[0][1]["content"]
    assert "expected" not in json.dumps(spy.calls[0])


def test_grounded_passes_real_context_and_labels(reasoner):
    spy=SpyClient(); answer=Advisor(reasoner=reasoner,client=spy).answer("Can S003 take CS 421 in Fall 2026?")
    assert answer["llm_called"] and answer["evidence"]
    assert "CONTEXT:" in spy.calls[0][1]["content"]
    assert all(reasoner.kg.valid_edge(e) for e in answer["evidence"])
    text=format_answer(answer)
    assert "Explicit knowledge" in text and "Generated text" in text and "Prediction" in text


def test_oversized_rows_abstain():
    retrieval={"question":"x", "intent":"Q01","rows":[{"x":"y"*1000}],"limitations":[],"graph_sha256":"a","reasoning":[],"evidence":[]}
    assert context_for(retrieval,100) is None


def test_unconfigured_provider_is_error():
    with pytest.raises(LLMError): LLMClient(Config()).complete([])


def test_local_model_digest_is_recorded(monkeypatch):
    class Response:
        def __init__(self,data):self.data=data
        def raise_for_status(self):pass
        def json(self):return self.data
    def get(url,timeout):
        return Response({"version":"test-runtime"} if url.endswith("version") else
                        {"models":[{"name":"course-planning-qwen3:latest","digest":"test-digest","details":{}}]})
    monkeypatch.setattr("app.llm.requests.get",get)
    identity=LLMClient(Config(provider="ollama",model="course-planning-qwen3")).runtime_identity()
    assert identity["digest"] == "test-digest" and identity["model_digest_verified"]
