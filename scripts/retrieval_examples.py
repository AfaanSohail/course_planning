"""Save real retrieved contexts. This does not manufacture LLM responses."""
from app import service
from reasoning.kg import ROOT, save_json
from explainability.format import format_answer

QUESTIONS=[
    "Can S003 take CS 421 in Fall 2026?",
    "For each department, how many available courses fulfill the advanced elective group in Fall 2026?",
    "What is the degree progress for S003?",
    "What is the weather for CS 421?",
    "Can S003 take CS 421 in Fall 2027?",
]


if __name__ == "__main__":
    advisor=service.Advisor()
    for i,q in enumerate(QUESTIONS,1):
        result=advisor.answer(q,retrieve_only=i<=3)
        save_json(ROOT/f"explainability/example_{i}.json",result)
        (ROOT/f"explainability/example_{i}.md").write_text(format_answer(result), encoding="utf-8")
        print(i,result["mode"],len(result["evidence"]))
