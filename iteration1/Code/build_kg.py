"""Rebuild the course-planning RDF graph from the supplied Fall 2026 CSV.

This reproducible ETL reads the course catalog, normalizes its course and
section entities, parses prerequisite clauses and merges the team's curated
UIUC BS CS requirement/policy and synthetic-student A-Boxes. It preserves the
submitted Fall 2026 scope through explicit course/section selection lists.

Example (from the submission root):
    pip install pandas rdflib
    python Code/build_kg.py --output-dir rebuilt

The supplied RDF snapshot remains the authoritative reviewed Iteration 1 graph.
Complex catalog prerequisites are conservatively flagged for review; the
parser may interpret ambiguous prose differently from manually reviewed
clauses in the original graph. Compare rebuilt outputs before replacing it.
"""
from __future__ import annotations

import argparse
import json
import html
import re
import sys
from pathlib import Path

import pandas as pd
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, XSD, OWL
from rdflib.compare import isomorphic

from prereq_parser import parse_prerequisite

UCA = Namespace("https://example.org/uiuc-course-advisor/ontology#")
RES = Namespace("https://example.org/uiuc-course-advisor/resource/")
SOURCE_URL = "https://discovery.cs.illinois.edu/dataset/course-catalog/"

# Scope is frozen to the curated Fall 2026 submission so the rebuild does not
# unexpectedly change if the upstream catalog grows. These codes were selected
# from the approved core departments, gen-ed electives and prerequisite closure.
SELECTED_COURSES = set("""
ACES102 ADV492 AE482 ANSC110 ANSC207 ANTH143 ANTH241 ANTH246 ANTH514 ASRM210 ASRM401 ASRM402
ASRM406 ASRM451 ASRM453 ASRM551 ASRM563 ASTR100 ASTR121 ASTR122 ASTR150 ASTR200 ASTR330 ASTR515
ASTR540 ATMS100 ATMS120 ATMS140 ATMS201 ATMS302 BIOE210 BIOE310 BIOE380 BIOE414 BIOE415 BIOE516
CHEM101 CHEM102 CHEM104 CHEM202 CHEM203 CPSC112 CPSC199 CS100 CS101 CS105 CS107 CS124
CS128 CS173 CS199 CS210 CS211 CS222 CS225 CS233 CS277 CS307 CS340 CS341
CS357 CS361 CS374 CS397 CS400 CS401 CS407 CS409 CS410 CS411 CS412 CS413
CS415 CS417 CS418 CS421 CS422 CS423 CS424 CS425 CS426 CS427 CS433 CS437
CS438 CS439 CS440 CS441 CS444 CS445 CS446 CS447 CS450 CS452 CS460 CS461
CS463 CS464 CS465 CS466 CS468 CS470 CS473 CS475 CS477 CS481 CS483 CS484
CS491 CS492 CS497 CS498 CS499 CS507 CS511 CS512 CS521 CS524 CS527 CS537
CS538 CS542 CS543 CS545 CS546 CS547 CS549 CS556 CS562 CS563 CS565 CS567
CS571 CS574 CS579 CS580 CS581 CS582 CS591 CS597 CS598 CSE401 CSE408 CSE414
CSE422 CSE423 CSE426 CSE427 CSE428 CSE440 CSE441 CSE448 CSE485 CSE511 CSE525 CSE542
DANC246 ECE101 ECE110 ECE120 ECE145 ECE199 ECE200 ECE205 ECE206 ECE210 ECE211 ECE217
ECE220 ECE304 ECE305 ECE310 ECE311 ECE313 ECE314 ECE316 ECE329 ECE330 ECE333 ECE340
ECE342 ECE343 ECE350 ECE364 ECE365 ECE374 ECE380 ECE385 ECE391 ECE395 ECE396 ECE397
ECE398 ECE401 ECE402 ECE404 ECE405 ECE407 ECE408 ECE410 ECE411 ECE414 ECE415 ECE419
ECE420 ECE422 ECE424 ECE427 ECE428 ECE435 ECE437 ECE438 ECE439 ECE441 ECE444 ECE445
ECE448 ECE449 ECE453 ECE455 ECE457 ECE459 ECE463 ECE464 ECE469 ECE470 ECE473 ECE476
ECE478 ECE482 ECE484 ECE486 ECE490 ECE491 ECE493 ECE494 ECE496 ECE498 ECE499 ECE500
ECE509 ECE514 ECE515 ECE517 ECE518 ECE520 ECE523 ECE524 ECE534 ECE535 ECE537 ECE541
ECE544 ECE549 ECE551 ECE563 ECE564 ECE566 ECE579 ECE586 ECE590 ECE592 ECE596 ECE597
ECE598 ECON102 ECON103 ENG100 ENG580 EPSY551 EPSY588 ESE103 ESE117 ESE118 ESE120 ESE140
ESE143 ESE208 FIN221 FSHN101 FSHN120 GEOL100 GEOL107 GEOL117 GEOL118 GEOL143 GEOL208 GGIS100
GGIS103 GLBL118 HDFS143 HK150 IB100 IB108 IB110 IB150 IE300 IE310 IE410 IE534
IS107 LA250 LING570 MATH101 MATH103 MATH112 MATH115 MATH119 MATH124 MATH199 MATH213 MATH220
MATH221 MATH225 MATH231 MATH234 MATH241 MATH257 MATH285 MATH299 MATH314 MATH357 MATH362 MATH390
MATH399 MATH402 MATH403 MATH405 MATH412 MATH413 MATH415 MATH416 MATH417 MATH423 MATH424 MATH427
MATH439 MATH441 MATH442 MATH444 MATH446 MATH447 MATH448 MATH450 MATH453 MATH461 MATH463 MATH464
MATH473 MATH475 MATH482 MATH484 MATH487 MATH489 MATH499 MATH500 MATH502 MATH510 MATH512 MATH514
MATH518 MATH526 MATH531 MATH535 MATH540 MATH542 MATH546 MATH554 MATH558 MATH562 MATH564 MATH570
MATH580 MATH593 MATH597 MCB100 ME445 ME540 MSE101 MSE182 MSE201 MSE280 MSE401 MSE485
NE410 NPRE527 NRES100 NRES103 PHIL101 PHIL316 PHIL419 PHIL420 PHIL439 PHIL514 PHYS100 PHYS101
PHYS102 PHYS110 PHYS199 PHYS211 PHYS212 PHYS213 PHYS214 PHYS222 PHYS225 PHYS246 PHYS325 PHYS326
PHYS329 PHYS360 PHYS370 PHYS394 PHYS395 PHYS401 PHYS402 PHYS403 PHYS404 PHYS407 PHYS419 PHYS420
PHYS427 PHYS435 PHYS436 PHYS446 PHYS466 PHYS485 PHYS486 PHYS487 PHYS496 PHYS497 PHYS503 PHYS505
PHYS508 PHYS513 PHYS515 PHYS523 PHYS524 PHYS535 PHYS540 PHYS561 PHYS565 PHYS567 PHYS575 PHYS580
PHYS582 PHYS590 PHYS593 PHYS596 PHYS597 PHYS599 PLPA200 PSYC514 PSYC588 PSYC594 RHET105 SE522
SHS280 SOC588 STAT100 STAT107 STAT199 STAT200 STAT207 STAT212 STAT385 STAT390 STAT391 STAT400
STAT408 STAT409 STAT410 STAT425 STAT426 STAT428 STAT429 STAT430 STAT431 STAT432 STAT433 STAT434
STAT437 STAT440 STAT441 STAT443 STAT448 STAT480 STAT510 STAT511 STAT525 STAT527 STAT542 STAT546
STAT552 STAT553 STAT555 STAT558 STAT578 STAT588 STAT590 STAT593 TAM413
""".split())

STUB_COURSES = set("""
BIOE205 CS125 CS126 CS240 CS241 CS414 CS416 CS419 CS428 CS429 CS431 CS434
CS435 CS436 CS442 CS443 CS448 CS467 CS469 CS474 CS476 CS482 CS493 CS494
CS500 CS510 CS514 CS519 CS522 CS523 CS525 CS526 CS533 CS534 CS536 CS539
CS540 CS541 CS544 CS554 CS555 CS558 CS572 CS575 CS576 CS583 CS584 CS586
CS588 CSE429 ECE361 ECE416 ECE452 ECE460 ECE481 EPSY581 EPSY582 GEOL101 GEOL103 GEOL104
MATH012 MATH210 MATH227 MATH284 MATH286 MATH347 MATH348 MATH408 MATH414 MATH418 MATH481 MATH501
MATH511 MATH525 MATH541 MATH553 MATH561 MSE405 NPRE429 PHYS560 PHYS581 PSYC407 SOC587 STAT361
STAT420 STAT447 STAT571
""".split())

SECTION_COURSES = set("""
CS100 CS101 CS105 CS107 CS124 CS128 CS173 CS199 CS210 CS211 CS222 CS225
CS233 CS277 CS307 CS340 CS341 CS357 CS361 CS374 CS397 CS400 CS401 CS407
CS409 CS410 CS411 CS412 CS413 CS415 CS417 CS418 CS421 CS422 CS423 CS424
CS425 CS426 CS427 CS433 CS437 CS438 CS439 CS440 CS441 CS444 CS445 CS446
CS447 CS450 CS452 CS460 CS461 CS463 CS464 CS465 CS466 CS468 CS470 CS473
CS475 CS477 CS481 CS483 CS484 CS491 CS492 CS497 CS498 CS499 CS507 CS511
CS512 CS521 CS524 CS527 CS537 CS538 CS542 CS543 CS545 CS546 CS547 CS549
CS556 CS562 CS563 CS565 CS567 CS571 CS574 CS579 CS580 CS581 CS582 CS591
CS597 CS598 ENG100 MATH220 MATH221 MATH231 MATH241 MATH257 MATH415 MATH416 PHYS211 PHYS212
""".split())


def as_text(value) -> str:
    if value is None or pd.isna(value):
        return ""
    return html.unescape(str(value).strip())


def number_literal(text):
    match = re.findall(r"\d+(?:\.\d+)?", text)
    if not match:
        return None
    return Literal(match[0], datatype=XSD.decimal), Literal(match[-1], datatype=XSD.decimal)


def course_id(code):
    return RES["course/" + code]


def set_literal(g, subject, prop, text, datatype=None):
    if text:
        g.add((subject, prop, Literal(text, datatype=datatype)))


def course_code(row):
    sub = as_text(row["Subject"]).upper()
    number = as_text(row["Number"])
    if number.endswith(".0"):
        number = number[:-2]
    if not (sub.isalpha() and re.fullmatch(r"\d{3}", number)):
        return None
    return sub + number


def build_catalog(csv_path: Path) -> Graph:
    frame = pd.read_csv(csv_path, low_memory=False, dtype=str, keep_default_na=False)
    frame = frame.drop_duplicates()
    for col in frame.columns:
        frame[col] = frame[col].map(as_text)
    frame["_code"] = frame.apply(course_code, axis=1)
    frame = frame.loc[frame["_code"].isin(SELECTED_COURSES)].copy()
    available = set(frame["_code"])
    if available != SELECTED_COURSES:
        missing = sorted(SELECTED_COURSES - available)
        raise ValueError(f"Missing {len(missing)} selected courses from the catalog: {missing[:12]}")

    g = Graph()
    g.bind("uca", UCA)
    g.bind("res", RES)
    g.bind("rdfs", RDFS)

    term = RES["term/2026-fa"]
    g.add((term, RDF.type, UCA.AcademicTerm))
    g.add((term, RDFS.label, Literal("Fall 2026")))
    g.add((term, UCA.year, Literal(2026, datatype=XSD.integer)))
    g.add((term, UCA.termName, Literal("Fall")))

    # Existing degree groups and the parser can refer to courses outside the
    # snapshot. Represent them as explicitly marked stubs, not invented classes.
    all_codes = SELECTED_COURSES | STUB_COURSES
    for code in sorted(all_codes):
        match = re.fullmatch(r"([A-Z]+)(\d{3})", code)
        if not match:
            continue
        subject, number = match.groups()
        course = course_id(code)
        department = RES["department/" + subject]
        g.add((department, RDF.type, UCA.Department))
        set_literal(g, department, RDFS.label, subject)
        set_literal(g, department, UCA.subjectCode, subject)
        g.add((course, RDF.type, UCA.Course))
        set_literal(g, course, UCA.courseCode, subject + " " + number)
        g.add((course, UCA.courseNumber, Literal(int(number), datatype=XSD.integer)))
        g.add((course, UCA.inDepartment, department))
        if code in STUB_COURSES:
            set_literal(g, course, RDFS.label, subject + " " + number)
            set_literal(g, course, RDFS.comment,
                        "Referenced by a prerequisite, cross-listing or degree requirement but not present in the Fall 2026 catalog snapshot; only its code is known.")

    for code, grouped in frame.groupby("_code", sort=True):
        row = grouped.iloc[0]
        subj = as_text(row["Subject"]).upper()
        course = course_id(code)
        offering = RES[f"offering/{code}/2026-fa"]
        title = as_text(row["Name"])
        set_literal(g, course, RDFS.label, f"{subj} {code[len(subj):]} {title}")
        set_literal(g, course, UCA.courseTitle, title)
        set_literal(g, course, UCA.courseDescription, as_text(row["Description"]))
        set_literal(g, course, UCA.sourceURL, SOURCE_URL, XSD.anyURI)
        attrs = as_text(row["Degree Attributes"])
        set_literal(g, course, UCA.hasDegreeAttribute, attrs)
        credits = number_literal(as_text(row["Credit Hours"]))
        if credits:
            g.add((course, UCA.courseCreditsMin, credits[0]))
            g.add((course, UCA.courseCreditsMax, credits[1]))
        g.add((course, UCA.hasOffering, offering))
        g.add((offering, RDF.type, UCA.CourseOffering))
        g.add((offering, UCA.offeredInTerm, term))
        set_literal(g, offering, RDFS.label, f"{subj} {code[len(subj):]} (Fall 2026)")

        # The 'Same as ECE xxx' notation is a cross-listing, not a
        # prerequisite. Only the explicit forward assertion is stored.
        description = as_text(row["Description"])
        cross = re.search(r"\bSame as\s+([^.;]+)", description, re.I)
        if cross:
            for match in re.finditer(r"\b([A-Za-z]{2,5})\s*(\d{3})\b", cross.group(1)):
                other = match.group(1).upper() + match.group(2)
                if other != code and other in all_codes:
                    g.add((course, UCA.crossListedWith, course_id(other)))

        parsed = parse_prerequisite(description, {c[:-3] for c in all_codes})
        if parsed is not None:
            expr = RES["prereq/" + code]
            g.add((course, UCA.hasPrerequisiteExpression, expr))
            g.add((expr, RDF.type, UCA.PrerequisiteExpression))
            set_literal(g, expr, RDFS.label, f"Prerequisites of {subj} {code[len(subj):]}")
            set_literal(g, expr, UCA.prerequisiteSourceText, parsed.source)
            set_literal(g, expr, UCA.parseStatus, parsed.status)
            for i, option in enumerate(parsed.options, 1):
                opt = RES[f"prereq/{code}/option/{i}"]
                g.add((expr, UCA.hasOption, opt))
                g.add((opt, RDF.type, UCA.PrerequisiteOption))
                set_literal(g, opt, RDFS.label, f"{subj} {code[len(subj):]} prerequisite option {i}")
                for j, condition in enumerate(option, 1):
                    cond = RES[f"prereq/{code}/option/{i}/condition/{j}"]
                    g.add((opt, UCA.hasCondition, cond))
                    g.add((cond, RDF.type, UCA[condition.kind]))
                    set_literal(g, cond, UCA.conditionSourceText, condition.text)
                    short = f"{subj} {code[len(subj):]} opt {i} cond {j}: "
                    if condition.kind == "CourseChoiceCondition":
                        short += "one of " + ", ".join(c[:-3] + " " + c[-3:] for c in condition.courses)
                    elif condition.kind == "CourseCondition":
                        short += "requires " + condition.courses[0][:-3] + " " + condition.courses[0][-3:]
                    elif condition.kind == "StandingCondition":
                        short += f"standing rank >= {condition.rank}"
                    elif condition.kind == "ConsentCondition":
                        short += "consent / approval"
                    else:
                        short += "needs review: " + condition.text
                    set_literal(g, cond, RDFS.label, short)
                    if condition.kind in ("CourseCondition", "CourseChoiceCondition"):
                        g.add((cond, UCA.allowsConcurrent, Literal(condition.concurrent)))
                        pred = UCA.requiredCourse if condition.kind == "CourseCondition" else UCA.alternativeCourse
                        for refcode in condition.courses:
                            if refcode in all_codes and refcode != code:
                                g.add((cond, pred, course_id(refcode)))
                    elif condition.kind == "StandingCondition":
                        g.add((cond, UCA.minimumStandingRank, Literal(condition.rank, datatype=XSD.integer)))

    selected_sections = frame.loc[frame["_code"].isin(SECTION_COURSES)].drop_duplicates(
        subset=["YearTerm", "CRN", "Type Code"], keep="first")
    for _, row in selected_sections.iterrows():
        crn = as_text(row["CRN"])
        typecode = as_text(row["Type Code"])
        if not crn or not typecode:
            continue
        code = row["_code"]
        sec = RES[f"section/2026-fa/{crn}-{typecode}"]
        g.add((sec, RDF.type, UCA.Section))
        g.add((sec, UCA.sectionOf, RES[f"offering/{code}/2026-fa"]))
        label = f"{code[:-3]} {code[-3:]} {as_text(row['Section'])} {as_text(row['Type'])} (CRN {crn}, Fall 2026)"
        set_literal(g, sec, RDFS.label, re.sub(r"\s{2,}", " ", label))
        set_literal(g, sec, UCA.crn, crn)
        for column, prop in [
            ("Section", UCA.sectionCode), ("Type", UCA.sectionType),
            ("Start Time", UCA.startTime), ("End Time", UCA.endTime),
            ("Days of Week", UCA.meetingDays), ("Room", UCA.roomNumber),
            ("Building", UCA.buildingName),
            ("Enrollment Status", UCA.enrollmentStatus),
        ]:
            value = as_text(row[column])
            if column == "Enrollment Status" and value.upper() == "UNKNOWN":
                continue
            set_literal(g, sec, prop, value)
        for instructor in re.split(r"\s*;\s*", as_text(row["Instructors"])):
            instructor = instructor.strip()
            if not instructor:
                continue
            slug = re.sub(r"[^a-z0-9]+", "-", instructor.lower()).strip("-")
            person = RES["instructor/" + slug]
            g.add((person, RDF.type, UCA.Instructor))
            set_literal(g, person, RDFS.label, instructor)
            set_literal(g, person, UCA.instructorName, instructor)
            g.add((sec, UCA.taughtBy, person))
    # These corrections reflect the team's manually reviewed prerequisite
    # choices and cross-listings. They are not substituted for the CSV parse:
    # the base graph is generated above, then the documented differences are
    # applied so the original Iteration 1 outputs are exactly reproducible.
    corrections_file = Path(__file__).with_name("curated_corrections.json")
    if corrections_file.exists():
        corrections = json.loads(corrections_file.read_text(encoding="utf8"))
        for operation in ("remove", "add"):
            statements = corrections.get(operation, [])
            patch = Graph()
            for statement in statements:
                patch.parse(data=statement + "\n", format="nt")
            for triple in patch:
                if operation == "remove":
                    g.remove(triple)
                else:
                    g.add(triple)
    return g


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output-dir", type=Path, default=Path("rebuilt"))
    args = parser.parse_args()
    src, dest = args.input_dir.resolve(), args.output_dir.resolve()
    dest.mkdir(parents=True, exist_ok=True)
    components = [
        ("abox_catalog.ttl", build_catalog(src / "Dataset/course-catalog.csv")),
        ("abox_degree_requirements.ttl", Graph().parse(src / "RDF_Knowledge_Graph/abox_degree_requirements.ttl")),
        ("abox_requirement_links.ttl", Graph().parse(src / "RDF_Knowledge_Graph/abox_requirement_links.ttl")),
        ("abox_students_synthetic.ttl", Graph().parse(src / "RDF_Knowledge_Graph/abox_students_synthetic.ttl")),
    ]
    complete = Graph()
    complete.bind("uca", UCA)
    complete.bind("res", RES)
    complete.parse(src / "Ontology/uca_ontology.ttl", format="turtle")
    for filename, graph in components:
        graph.serialize(destination=str(dest / filename), format="turtle")
        print(f"{filename}: {len(graph):,} triples")
        for triple in graph:
            complete.add(triple)
    complete.serialize(destination=str(dest / "uiuc_course_kg.ttl"), format="turtle")
    print(f"uiuc_course_kg.ttl: {len(complete):,} triples (including ontology)")
    reference = src / "RDF_Knowledge_Graph/uiuc_course_kg.ttl"
    if reference.exists():
        original = Graph().parse(reference, format="turtle")
        rebuilt_on_disk = Graph().parse(dest / "uiuc_course_kg.ttl", format="turtle")
        if isomorphic(original, rebuilt_on_disk):
            print("Reference comparison: exact RDF graph match (isomorphic, including OWL blank nodes).")
        else:
            print("Reference comparison: graphs differ; review the source inputs and curated corrections.")


if __name__ == "__main__":
    main()
