"""Parse catalog prerequisite prose into AND/OR conditions.

The returned structure is deliberately conservative. In an option, all conditions
must hold (AND); options are alternatives (OR). A CourseChoiceCondition accepts
any of its listed courses. Sentences needing human review are flagged and kept.

Only standard-library modules are used, making the parser importable on its own.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import List

COURSE_RE = re.compile(r"\b([A-Za-z]{2,5})\s*[- ]?\s*(\d{3})\b")
STANDING_RE = re.compile(r"\b(freshman|sophomore|junior|senior|graduate)\s+standing\b", re.I)
RANKS = {"freshman": 1, "sophomore": 2, "junior": 3, "senior": 4, "graduate": 5}


@dataclass
class Condition:
    kind: str
    text: str
    courses: List[str] = field(default_factory=list)
    concurrent: bool = False
    rank: int = 0


@dataclass
class ParseResult:
    source: str
    options: List[List[Condition]]
    status: str


def prerequisite_sentence(description: str) -> str:
    """Return the first catalog sentence after 'Prerequisite:', if present."""
    match = re.search(r"\bPrerequisites?\s*:\s*", description or "", re.I)
    if not match:
        return ""
    body = (description or "")[match.end():].strip()
    # Period followed by whitespace starts the next sentence; leave abbreviations
    # like 'i.e.' alone rather than greedily cutting off after the first period.
    stop = re.search(r"(?<!\bi\.e)(?<!\be\.g)\.(?=\s|$)", body, re.I)
    return (body[:stop.end()] if stop else body).strip()


def course_mentions(text: str, known_subjects=None) -> List[str]:
    """Extract course identifiers, retaining order and subject carry-over."""
    subjects = {str(s).upper() for s in known_subjects} if known_subjects else None
    found, seen = [], set()
    last_subject = None
    for m in COURSE_RE.finditer(text or ""):
        subject, number = m.group(1).upper(), m.group(2)
        if subjects is not None and subject not in subjects:
            continue
        code = subject + number
        if code not in seen:
            found.append(code)
            seen.add(code)
        last_subject = subject
    # A bare course number after an explicit subject uses that subject:
    # 'MATH 415 or 416' -> MATH415, MATH416. Do not interpret arbitrary years.
    if last_subject:
        pat = re.compile(r"\b(?:or|and|,)\s*(\d{3})\b", re.I)
        for m in pat.finditer(text or ""):
            if COURSE_RE.search((text or "")[max(0, m.start()-8):m.end()]):
                continue
            code = last_subject + m.group(1)
            if code not in seen:
                found.append(code)
                seen.add(code)
    return found


def _condition(text: str, subjects=None) -> List[Condition]:
    text = text.strip(" ,;.")
    if not text:
        return []
    concurrent = bool(re.search(r"\bconcurrent\s+(?:enrollment|registration)|\bconcurrently\s+enrolled\b", text, re.I))
    mentions = course_mentions(text, subjects)
    standing = STANDING_RE.search(text)
    consent = bool(re.search(r"\b(consent|permission|approval)\b", text, re.I))
    has_or = bool(re.search(r"\bor\b|\bone of\b|\beither\b", text, re.I))
    uncertain = bool(re.search(r"\b(equivalent|background|experience|knowledge|restricted|intended|specified|program)\b", text, re.I))
    if mentions:
        if has_or and len(mentions) > 1:
            return [Condition("CourseChoiceCondition", text, mentions, concurrent)]
        # Comma-separated and AND-connected identifiers are separate requirements.
        return [Condition("CourseCondition", text, [code], concurrent) for code in mentions]
    if standing:
        return [Condition("StandingCondition", text, rank=RANKS[standing.group(1).lower()])]
    if consent:
        return [Condition("ConsentCondition", text)]
    return [Condition("OtherCondition", text)]


def parse_prerequisite(description: str, known_subjects=None) -> ParseResult | None:
    """Produce a conservative prerequisite tree for a course description.

    The parser does not silently treat unknown prose as a satisfied condition.
    Complex mixed AND/OR clauses are marked needs_review for a human decision.
    """
    source = prerequisite_sentence(description)
    if not source or re.search(r"\b(no prerequisites|there are no prerequisites)\b", source, re.I):
        return None

    needs_review = bool(re.search(
        r"\b(equivalent|restricted|intended|specified|strongly recommend|background|experience|knowledge)\b",
        source, re.I,
    ))
    source_no_end = source.rstrip(".")
    # Alternative approval for the whole expression is a separate option.
    extra_options = []
    tail = re.search(r"(?:;|,)\s*or\s+(consent|permission)\s+of\s+instructors?\s*$", source_no_end, re.I)
    if tail:
        source_no_end = source_no_end[:tail.start()].strip()
        extra_options.append([Condition("ConsentCondition", tail.group().lstrip(";, "))])
    tail = re.search(r"(?:;|,)\s*or\s+(junior|senior|graduate)\s+standing\s*$", source_no_end, re.I)
    if tail:
        source_no_end = source_no_end[:tail.start()].strip()
        extra_options.append([Condition("StandingCondition", tail.group().lstrip(";, "), rank=RANKS[tail.group(1).lower()])])

    conditions = []
    for part in re.split(r"\s*;\s*", source_no_end):
        if not part.strip():
            continue
        # 'X and one of Y,Z' denotes two AND conditions, not one giant OR.
        splits = re.split(r"\s+and\s+(?=(?:one of|either)\b)", part, flags=re.I)
        for segment in splits:
            # Explicit conjunction of unambiguous course groups.
            splits2 = re.split(r"\s+and\s+(?=[A-Z]{2,5}\s*\d{3}\b)", segment)
            for clause in splits2:
                items = _condition(clause, known_subjects)
                conditions.extend(items)
                if not items:
                    needs_review = True
    if not conditions:
        conditions = [Condition("OtherCondition", source_no_end)]
        needs_review = True
    if re.search(r"\bor\s+(?:consent|permission)\b", source_no_end, re.I):
        needs_review = True
    if any(item.kind == "OtherCondition" for item in conditions):
        needs_review = True
    return ParseResult(source=source, options=[conditions] + extra_options,
                       status="needs_review" if needs_review else "parsed")


if __name__ == "__main__":
    example = "Prerequisite: One of CS 233, CS 240, CS 340 or ECE 391; CS 374 or ECE 374; one of MATH 225, MATH 257, MATH 415, MATH 416, ASRM 406, or BIOE 210."
    result = parse_prerequisite(example)
    for n, option in enumerate(result.options, 1):
        print(f"Option {n}:")
        for condition in option:
            print(f"  {condition.kind}: {', '.join(condition.courses) or condition.text}")
