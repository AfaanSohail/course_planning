"""Conservative entity/intent linking; no LLM-generated SPARQL execution."""
import re


def link(question):
    courses = list(dict.fromkeys(a.upper() + b for a, b in re.findall(r"\b([A-Za-z]{2,6})\s*[- ]?\s*(\d{3})\b", question)
                                if a.upper() not in {"CQ", "S"}))
    students = list(dict.fromkeys(re.findall(r"\bS\d{3}\b", question.upper())))
    q = question.lower()
    terms = re.findall(r"\b(20\d{2})-(fa|sp|su|wi)\b", q)
    for season, year in re.findall(r"\b(fall|spring|summer|winter)\s+(20\d{2})\b", q):
        terms.append((year, {"fall": "fa", "spring": "sp", "summer": "su", "winter": "wi"}[season]))
    return {"courses": courses, "students": students, "terms": list(dict.fromkeys(y + "-" + t for y, t in terms))}


def route(question, entities):
    q = question.lower()
    # Reject requests outside recorded catalog facts even if a known code appears.
    if re.search(r"weather|tuition|professor.*(best|rating)|pass rate|salary|scholarship|exam date|guarantee|gpa.*predict", q):
        return None
    if re.search(r"each department|per department|department.*(?:count|how many)", q):
        return "Q11"
    if re.search(r"catalog wording|evidence.*(?:recommend|planned)|supports each recommendation", q):
        return "Q15"
    if re.search(r"cross.list|aliases|substitution", q):
        return "Q10"
    if re.search(r"two.*(?:hop|link)|at least 2|upstream", q):
        return "Q08"
    if re.search(r"chain|back to.*root|prerequisite tree", q):
        return "Q02"
    if re.search(r"progress|credit hours.*needed|still needed.*group|remaining.*requirement", q):
        return "Q06"
    if re.search(r"downstream|opens? up|unlock|additional course|become available", q):
        return "Q04"
    if re.search(r"hypothetical|what.if|how does.*(?:set|change)", q):
        return "Q13"
    if re.search(r"alternative.*(?:met|unmet)|precise.*conditions|can .*take|eligible for|eligibility", q) and entities["courses"]:
        return "Q03"
    if re.search(r"which.*courses.*(?:offered|take|eligible)|catalog courses|what.*courses.*take", q):
        return "Q01"
    if re.search(r"requirement groups.*(?:more than|choices)", q):
        return "Q09"
    return None
