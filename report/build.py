"""One consolidated PDF, assembled only from preserved source and real artifacts.

Draft generation is offline. Final generation rejects missing experimental,
review, screenshot, contribution and submission evidence.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import re
import textwrap
from pathlib import Path
from xml.etree import ElementTree as ET

from docx import Document
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS, OWL
from reasoning.kg import ROOT, UCA, RES
from evaluation.queries import catalog


def read_json(path, default=None):
    return json.loads(path.read_text()) if path.exists() else default


def validate_final(meta, screenshots):
    problems=[]
    for key in ("repository_url","demo_video_url"):
        if not str(meta[key]).startswith("https://"):problems.append(key)
    if not re.fullmatch(r"[0-9a-f]{40}",meta["final_commit_hash"]):problems.append("final_commit_hash")
    if not meta["clean_machine_verified"]:problems.append("clean_machine_verified")
    if not meta.get("review_laptop_verified",False):problems.append("review_laptop_verified")
    for category in ("grounded_app", "insufficient_evidence", "comparison"):
        if not any(s.get("category")==category and (ROOT/s["path"]).exists() for s in screenshots):
            problems.append("actual screenshot: "+category)
    for member in meta["members"]:
        if not member["github"] or not member["verified_commit_urls"]:problems.append("actual commit links for "+member["name"])
    run=ROOT/"evaluation/results"/meta["llm_run_id"]
    summary=read_json(run/"summary.json",{})
    if summary.get("status")!="human_review_complete" or summary.get("questions")!=10:
        problems.append("complete human-reviewed ten-question A/B results")
    if not (run/"comparison.csv").exists():problems.append("comparison.csv")
    # Revalidate raw answer hashes and the human review rather than trusting a stale summary.
    if summary.get("status")=="human_review_complete":
        from evaluation.score import score
        try:score(meta["llm_run_id"])
        except SystemExit as error:problems.append("invalid scoring artifacts: "+str(error))
    for cq in meta.get("explainability_cqs", ["CQ03","CQ08","CQ11"]):
        record=read_json(run/f"{cq}_B.json",{})
        if not record.get("llm_called") or not record.get("evidence"):problems.append("live explainability answer "+cq)
    for cq in ["CQ01","CQ02","CQ03","CQ04","CQ06","CQ08","CQ10","CQ11","CQ13","CQ15"]:
        for mode in "AB":
            record=read_json(run/f"{cq}_{mode}.json",{})
            if not record.get("llm_called"):problems.append(f"real LLM call {cq}_{mode}")
    if len([s for s in screenshots if s.get("iteration")==2 and (ROOT/s["path"]).exists()])<3:
        problems.append("at least three actual Iteration 2 execution screenshots")
    if problems:raise SystemExit("Final report blocked by missing evidence:\n- "+"\n- ".join(problems))


def assemble(final=False):
    meta=read_json(ROOT/"report/submission.json")
    screenshots=read_json(ROOT/"report/screenshots/manifest.json",[])
    if final:validate_final(meta,screenshots)
    blocks=[]
    def heading(t):blocks.append(("heading",t))
    def para(t):blocks.append(("paragraph",str(t)))
    def code(t):blocks.append(("code",str(t)))
    def table(headers,rows):blocks.append(("table",headers,rows))
    heading("course_planning — Consolidated Iterations 1 and 2")
    para("FINAL" if final else "DRAFT: scored trial 3 results are included. Final video, source commit and live review evidence remain pending.")
    para(meta["course"]+" | Instructor: "+meta["instructor"])
    table(["Team member","Roll number","GitHub"],[[m["name"],m["roll"],m["github"]] for m in meta["members"]])
    para("Repository: "+meta["repository_url"])
    para("Submitted implementation source commit: "+meta["final_commit_hash"])
    para("External demo video: "+meta["demo_video_url"])
    heading("Problem, data and Iteration 1 design")
    para("Knowledge-Grounded University Course Planning and Prerequisite Advisory System: use the supplied UIUC Fall 2026 catalog and curated BS Computer Science requirements to explain possible prerequisites, synthetic-student eligibility and recorded degree allocations. Data flows through RDF, ontology rules, SPARQL, multi-hop reasoning, retrieval and an LLM answer with evidence.")
    stats=read_json(ROOT/"evaluation/results/iteration1_rerun/summary.json")
    if stats:
        table(["Measured artifact","Result"],[[k,str(stats[k])] for k in ["explicit_triples","schema_triples","abox_triples","owlrl_closure_triples","rebuild_isomorphic","shacl_conforms"]])
        table(["Named ontology declarations","Count"],[[k,v] for k,v in stats["schema_counts"].items()])
        table(["Entity class","Observed instances"],list(stats["entities"].items()))
        para("Parse statuses: "+json.dumps(stats["parse_status"])+". Source SHA256: "+stats["graph_sha256"])
        para("The current local OWL RL count supersedes the historical closure count in project notes. The input TTL and ontology remain unchanged. SHACL conformity covers the supplied structural shapes; the separate Python degree-policy check can still detect the seeded distinct-electives conflict.")
    else:para("PENDING: run scripts.reproduce_iteration1.")
    original=Document(ROOT/"iteration1/Report/Report.docx")
    # Import original wording/design, avoiding its old progress/contribution assertions.
    imported=[(1,"Original competency questions"),(2,"Original CQ-to-KG mapping"),
              (6,"Catalog column to RDF mapping"),(7,"Preserved URI design"),
              (15,"Ontology classes"),(16,"Ontology object properties"),(17,"Ontology datatype properties"),
              (18,"Schema constructs"),(19,"Ontology restrictions"),(20,"Operational rules")]
    for index,title in imported:
        heading(title)
        rows=[[c.text for c in row.cells] for row in original.tables[index].rows]
        if index==2:
            # This source table has CQ labels and field/value rows, not a conventional header.
            table(["CQ / field","Original mapping"],rows)
        else:table(rows[0],rows[1:])
    heading("Data sources, cleaning and transformation")
    para("Source files: iteration1/Dataset/course-catalog.csv (catalog snapshot), uiuc-prerequisites.csv (QA only), and the curated requirement/student A-Boxes. The original build_kg.py and prereq_parser.py are preserved and executed by the reproduction script. Curated corrections are retained. HTML entities and whitespace are normalized; duplicate rows are removed; repeated section rows are merged; null fields produce no empty RDF literal. Referenced missing courses become labelled stubs with no invented titles or offerings. The builder's graph-isomorphism result and raw build log are retained.")
    decisions=[[c.text for c in row.cells[:2]] for row in original.tables[5].rows]
    table(decisions[0],decisions[1:])
    buildlog=ROOT/"evaluation/results/iteration1_rerun/build.log"
    if buildlog.exists():code(buildlog.read_text())
    heading("Re-executed SPARQL queries and outputs")
    if stats:
        table(["Query","Current rows","Archived rows","Match after URI/concat normalization"],
              [[q["query"],q["rows"],q["original_saved_rows"],q["match_after_uri_and_concat_normalization"]] for q in stats["queries"]])
    for key,item in catalog().items():
        heading(item["name"])
        code(item["query"])
        path=ROOT/"evaluation/results/iteration1_rerun"/(item["name"]+".csv")
        if path.exists():
            with path.open() as f:
                reader=csv.DictReader(f);rows=list(reader)
                if rows:table(reader.fieldnames,[[r.get(k,"") for k in reader.fieldnames] for r in rows])
                else:para("Executed query returned no rows.")
        else:para("PENDING: re-execute this query.")
    heading("Three verified symbolic inference examples")
    inf=read_json(ROOT/"reasoning/outputs/inference_examples.json",[])
    for example in inf:
        heading(example["name"])
        para(example["rule"])
        code(json.dumps(example,indent=2))
    if not inf:para("PENDING: run scripts.inference_examples.")
    heading("Preserved actual screenshots")
    for shot in screenshots:
        path=ROOT/shot["path"]
        if path.exists():blocks.append(("image",path,shot["caption"]))
    heading("Iteration 2 architecture")
    blocks.append(("architecture",))
    para("Diagram source: report/architecture.mmd. Local RDF retrieval is the executable default; GraphDB is used separately for the live query/inference walkthrough.")
    source=(ROOT/"report/iteration2_sections.md").read_text()
    paragraphs=re.split(r"\n\s*\n",source)
    for text in paragraphs:
        if text.startswith("#"):heading(text.lstrip("# "))
        else:para(text)
    heading("Measured modern-reasoning results")
    reasoning=read_json(ROOT/"reasoning/outputs/summary.json")
    if reasoning:
        table(["Observed metric","Result"],[[k,json.dumps(v)] for k,v in reasoning.items() if k not in {"scope_notes"}])
        for note in reasoning["scope_notes"]:para(note)
        for filename in ["eligibility.csv","option_conditions.csv"]:
            heading(filename)
            with (ROOT/"reasoning/outputs"/filename).open() as f:
                reader=csv.DictReader(f);rows=list(reader)
                table(reader.fieldnames,[[r[k] for k in reader.fieldnames] for r in rows])
    else:para("PENDING: run reasoning.evaluate.")
    routing=read_json(ROOT/"evaluation/results/retrieval_validation.json")
    if routing:
        heading("Natural-language retrieval validation (no model calls)")
        table(["CQ","Intent match","Expected-row match","Evidence edges","Invalid edges","Rows fit context","Omitted evidence / traces"],
              [[r["cq"],r["intent_match"],r["rows_match"],r["evidence_edges"],r["invalid_evidence_edges"],
                r["all_rows_fit_context"],str(r["omitted_evidence"])+" / "+str(r["omitted_traces"])] for r in routing["cases"]])
        para("These are retrieval checks, not LLM accuracy measurements. Full evidence remains in the JSON; context omissions are counted.")
    test_file=ROOT/"evaluation/results/tests.xml"
    if test_file.exists():
        suite=ET.parse(test_file).getroot().find("testsuite")
        if suite is not None:para("Actual pytest run: "+json.dumps(suite.attrib))
    clean_test_file=ROOT/"evaluation/results/tests_clean_environment.xml"
    if clean_test_file.exists():
        suite=ET.parse(clean_test_file).getroot().find("testsuite")
        if suite is not None:para("Actual fresh isolated virtual-environment pytest run: "+json.dumps(suite.attrib)+". This is not a separate-laptop certification.")
    readiness=read_json(ROOT/"report/laptop_checks/readiness.json")
    if readiness:
        heading("Observed review-laptop checks")
        para("Fresh laptop environment: "+str(readiness.get("environment"))+"; passing tests: "+str(readiness.get("tests_passed")))
        para("Protege: "+str(readiness.get("protege")))
        table(["GraphDB query", "Inference", "Observed rows"],
              [[q["query"],str(run["inference"]),run["rows"]] for q in readiness.get("graphdb",[]) for run in q["runs"]])
        para("Local CPU readiness response: "+json.dumps(readiness.get("local_llm",{})))
        para("The first CS421 readiness answer was incorrectly formatted and truncated at its local output limit. It is preserved separately. The successful short MATH241 answer establishes basic execution, not correctness on all unseen questions. Neither local answer is part of the scored Kaggle experiment.")
        para("Current GraphDB state: "+str(readiness.get("graphdb_current_state")))
    heading("Ten-question A/B comparison")
    cases=read_json(ROOT/"evaluation/cqs.json",[])
    run=ROOT/"evaluation/results"/meta["llm_run_id"]
    comparison=run/"comparison.csv"
    if comparison.exists():
        with comparison.open() as f:comparisons=list(csv.DictReader(f))
        # Full cells may exceed one page; the renderer permits within-row splitting.
        table(list(comparisons[0]),[[r[k] for k in comparisons[0]] for r in comparisons])
        para("Scored totals: "+json.dumps(read_json(run/"summary.json")))
        grades=list(csv.DictReader((run/"grades.csv").open()))
        decisions={(g["cq"],g["condition"]):g["correct"] for g in grades}
        for label,pair in [("Grounding helped",("No","Yes")),("Grounding worsened",("Yes","No")),
                           ("Both correct",("Yes","Yes")),("Both incorrect",("No","No"))]:
            selected=[c["id"] for c in cases if (decisions[c["id"],"A"],decisions[c["id"],"B"])==pair]
            para(label+": "+(", ".join(selected) if selected else "none in this run")+".")
        heading("Recorded error and unsupported-claim analysis")
        for g in grades:para(g["cq"]+" "+g["condition"]+" — "+g["reviewer"]+": "+g["notes"])
    else:
        para("Scoring is PENDING. Supplied response records, where present, are shown below without rewriting the model's answers. No human correctness totals are claimed. Table cells are labelled excerpts; the full answers follow the verified expected rows.")
        rows=[]
        for case in cases:
            answers=[read_json(run/f"{case['id']}_{mode}.json",{}).get('answer','PENDING: response not supplied') for mode in 'AB']
            rows.append([case['id']+' / '+case['question'], 'Full verified rows below',
                         *[a[:220]+(' … [excerpt; full answer below]' if len(a)>220 else '') for a in answers],
                         'PENDING / PENDING','PENDING / PENDING'])
        table(["CQ / question","Expected answer","LLM only","KG-grounded","Correct? A / B","Evidence available? A / B"],rows)
        audit=read_json(run/'artifact_audit.json')
        if audit:
            heading("Supplied experiment artifact audit")
            for key in ['response_records','llm_calls_recorded','complete_human_reviews','distinct_evidence_edges_checked',
                        'invalid_evidence_edges','truncated_responses','records_with_unknown_citations','integrity_findings']:
                para(key+': '+json.dumps(audit[key]))
            para("The run manifest reports "+audit['manifest']['platform']+" and source commit: "+audit['manifest']['commit']+
                 ". This is supplied execution metadata, not an independently witnessed model run. Invalid citations and truncation are retained for human scoring.")
    for case in cases:
        heading(case["id"]+" — verified expected rows")
        para(case["question"])
        expected=case["expected"]
        if expected:table(list(expected[0]),[[r.get(k) for k in expected[0]] for r in expected])
        for mode in 'AB':
            record=read_json(run/f"{case['id']}_{mode}.json")
            if record:
                heading(case['id']+' condition '+mode+' — full supplied model answer')
                para(record['answer'])
                para('finish_reason: '+str(record.get('completion',{}).get('finish_reason'))+
                     '; truncated: '+str(record.get('completion',{}).get('truncated'))+
                     '; human correctness/evidence review pending unless scored above.')
    heading("Three explainability records")
    for index,cq in enumerate(meta.get("explainability_cqs", ["CQ03","CQ08","CQ11"]),1):
        record=read_json(run/f"{cq}_B.json") or read_json(ROOT/f"explainability/example_{index}.json")
        if not record:
            para("PENDING explainability example "+cq);continue
        heading(cq+" — "+record["question"])
        para("Generated text (LLM): "+(record["answer"] if record.get("llm_called") else "PENDING: retrieval-only output; no generated answer is claimed."))
        retrieval=record.get("retrieval",{})
        for status,label in [("explicit","Explicit knowledge (stored)"),("inferred","Inferred knowledge (OWL schema closure)")]:
            para(label+" — representative retrieved triples (full evidence in JSON):")
            facts=[e for e in record.get("evidence",[]) if e["status"]==status]
            if facts:code(json.dumps(facts[:5],indent=2))
            else:para("No retrieved triples of this kind in this answer.")
        paths=[p for t in retrieval.get("reasoning",[]) for p in t["paths"] if p]
        if paths:code(json.dumps({"one_complete_returned_path":paths[0]},indent=2))
        para("Query/application conclusions (computed, not asserted RDF):")
        code(json.dumps({"rows":retrieval.get("rows"),"limitations":retrieval.get("limitations")},indent=2))
        para("Prediction: none. Hypothetical completions, where used, are assumptions. Full query, paths and graph hash remain in the raw JSON.")
    heading("Contribution and submission evidence")
    para(meta["contribution_note"])
    table(["Member / GitHub","Planned scope","Verified representative commits"],
          [[m["name"]+" / "+m["github"],m["planned_scope"],"\n".join(m["verified_commit_urls"]) or "PENDING — do not claim planned work as completed personal contribution"] for m in meta["members"]])
    heading("Recorded execution environment")
    environment=ROOT/"evaluation/results/environment.txt"
    if environment.exists():code(environment.read_text())
    else:para("PENDING: record python -m pip freeze and platform details.")
    return blocks


def render(blocks, path):
    from html import escape
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, LongTable, TableStyle, Image, XPreformatted
    from reportlab.graphics.shapes import Drawing, Rect, String, Line, Polygon
    font=Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    if font.exists():
        pdfmetrics.registerFont(TTFont("Body",str(font)));font_name="Body"
    else:font_name="Helvetica"
    styles=getSampleStyleSheet()
    body=ParagraphStyle("ReportBody",parent=styles["BodyText"],fontName=font_name,fontSize=9,leading=12,spaceAfter=6,wordWrap="CJK")
    small=ParagraphStyle("ReportSmall",parent=body,fontSize=7,leading=9,spaceAfter=2)
    title=ParagraphStyle("ReportHeading",parent=body,fontSize=13,leading=17,spaceBefore=12,spaceAfter=7,keepWithNext=True)
    mono=ParagraphStyle("ReportCode",parent=body,fontName="Courier",fontSize=6.4,leading=8,spaceAfter=5)
    def p(text,style=body):return Paragraph(escape(str(text)).replace("\n","<br/>"),style)
    story=[];text_output=[]
    for block in blocks:
        kind=block[0]
        if kind=="heading":story.append(p(block[1],title));text_output.extend(["\n# "+block[1],""])
        elif kind=="paragraph":story.append(p(block[1]));text_output.extend([block[1],""])
        elif kind=="code":
            lines=[]
            for line in block[1].splitlines():
                lines.extend(textwrap.wrap(line,110,replace_whitespace=False,drop_whitespace=False) or [""])
            # Individual lines remain splittable across pages.
            story.append(XPreformatted(escape("\n".join(lines)),mono))
            text_output.extend(["```",block[1],"```",""])
        elif kind=="table":
            headers,rows=block[1:];n=len(headers)
            if not n:continue
            cells=[[p(x,small) for x in headers]]+[[p("" if x is None else x,small) for x in row] for row in rows]
            tab=LongTable(cells,colWidths=[(A4[0]-72)/n]*n,repeatRows=1,splitByRow=1,splitInRow=1,hAlign="LEFT")
            tab.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colors.HexColor("#dce8f2")),
                ("GRID",(0,0),(-1,-1),0.3,colors.lightgrey),("VALIGN",(0,0),(-1,-1),"TOP"),
                ("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4)]))
            story.extend([tab,Spacer(1,7)])
            def cell(x):return str(x if x is not None else "").replace("|","\\|").replace("\n","<br>")
            text_output.append("| "+" | ".join(map(cell,headers))+" |")
            text_output.append("| "+" | ".join(["---"]*n)+" |")
            text_output.extend("| "+" | ".join(map(cell,row))+" |" for row in rows);text_output.append("")
        elif kind=="image":
            img=Image(str(block[1]));width=A4[0]-72;scale=min(width/img.imageWidth,360/img.imageHeight)
            img.drawWidth=img.imageWidth*scale;img.drawHeight=img.imageHeight*scale
            story.extend([img,p(block[2],small),Spacer(1,7)])
            text_output.extend([f"![{block[2]}]({block[1].relative_to(ROOT)})",""])
        elif kind=="architecture":
            drawing=Drawing(510,220)
            labels=["Catalog + curated data","Original ETL / parser","Explicit KG + ontology",
                    "User question","Entity / intent linking","SPARQL + OWL/Python",
                    "Labelled rows + paths","Local LLM / abstention","Answer + graph evidence"]
            def arrow(x1,y1,x2,y2):
                drawing.add(Line(x1,y1,x2,y2,strokeColor=colors.steelblue))
                if x2>x1:points=[x2,y2,x2-5,y2+3,x2-5,y2-3]
                else:points=[x2,y2,x2-3,y2+5,x2+3,y2+5]
                drawing.add(Polygon(points,fillColor=colors.steelblue,strokeColor=colors.steelblue))
            for i,label in enumerate(labels):
                x=(i%3)*170;y=165-(i//3)*65
                drawing.add(Rect(x,y,158,42,fillColor=colors.HexColor("#edf4fa"),strokeColor=colors.steelblue))
                drawing.add(String(x+6,y+19,label,fontName="Helvetica",fontSize=8))
                if i%3<2:arrow(x+158,y+20,x+169,y+20)
            arrow(419,165,419,142)
            drawing.add(Line(419,100,419,89,strokeColor=colors.steelblue))
            drawing.add(Line(419,89,79,89,strokeColor=colors.steelblue))
            arrow(79,89,79,77)
            drawing.add(String(5,10,"Human scoring compares actual grounded and baseline answers after generation.",fontName="Helvetica",fontSize=8))
            story.append(drawing);text_output.extend(["Architecture: see report/architecture.mmd.",""])
    def page(canvas,doc):
        canvas.saveState();canvas.setFont("Helvetica",8);canvas.drawString(36,22,"course_planning | source-based consolidated report")
        canvas.drawRightString(A4[0]-36,22,str(doc.page));canvas.restoreState()
    SimpleDocTemplate(str(path),pagesize=A4,rightMargin=36,leftMargin=36,topMargin=36,bottomMargin=36,
                      title="course_planning consolidated report").build(story,onFirstPage=page,onLaterPages=page)
    path.with_suffix(".md").write_text("\n".join(text_output),encoding="utf-8")


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("--final",action="store_true");args=parser.parse_args()
    name="consolidated_report_FINAL.pdf" if args.final else "consolidated_report_DRAFT.pdf"
    render(assemble(args.final),ROOT/"report"/name)
    print("Generated report/"+name)
