import argparse
import json
from reasoning.kg import save_json
from .config import Config
from .service import Advisor
from .llm import LLMError


def main():
    p = argparse.ArgumentParser(description="Course-planning QA with graph evidence")
    p.add_argument("question", nargs="?")
    p.add_argument("--config")
    p.add_argument("--baseline", action="store_true")
    p.add_argument("--retrieve-only", action="store_true")
    p.add_argument("--output")
    a = p.parse_args()
    advisor = Advisor(Config.load(a.config))
    def ask(q):
        try:
            result = advisor.answer(q, mode="baseline" if a.baseline else "grounded", retrieve_only=a.retrieve_only)
        except LLMError as error:
            p.exit(2, str(error) + "\n")
        if a.output:
            save_json(a.output, result)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    if a.question:
        ask(a.question)
    else:
        print("Enter a question with course/student/term where needed. Type quit to exit.")
        while True:
            try:
                question = input("course_planning> ").strip()
            except EOFError:
                break
            if question.lower() in {"quit", "exit"}:
                break
            if question:
                ask(question)


if __name__ == "__main__":
    main()
