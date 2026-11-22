"""Read the actual Iteration 1 queries. No copied expected answers."""
import re
from pathlib import Path
from reasoning.kg import ROOT


def catalog():
    text = (ROOT / "iteration1/SPARQL_Queries/queries.txt").read_text(encoding="utf-8")
    chunks = re.split(r"^###\s+", text, flags=re.M)
    prefixes = chunks[0]
    return {chunk.splitlines()[0].split("_")[0]:
            {"name": chunk.splitlines()[0], "query": prefixes + "\n" + "\n".join(chunk.splitlines()[1:])}
            for chunk in chunks[1:]}


def parameterized(query_id, student=None, course=None, term=None):
    q = catalog()[query_id]["query"]
    # Bind only typed, validated resource identifiers. Never interpolate raw questions.
    for kind, value in (("student", student), ("course", course), ("term", term)):
        if value is None:
            continue
        value = value.upper().replace(" ", "") if kind == "course" else value
        patterns = {"student": r"S\d{3}", "course": r"[A-Z]{2,6}\d{3}", "term": r"\d{4}-(?:fa|sp|su|wi)"}
        if not re.fullmatch(patterns[kind], value):
            raise ValueError(f"Invalid {kind}: {value}")
        q = re.sub(r"<" + kind + r"/[^>]+>", "<" + kind + "/" + value + ">", q)
        if kind == "course" and query_id == "Q13":
            display = re.sub(r"([A-Z]+)(\d+)", r"\1 \2", value)
            q = q.replace("plus CS 225", "plus " + display)
    return q


def run_query(kg, query_id, **kwargs):
    return kg.query(parameterized(query_id, **kwargs), inferred=query_id.startswith("INF") or query_id == "Q11")
