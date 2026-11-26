"""Rebuild RDF, compare isomorphism, run all original queries and SHACL."""
import csv
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from rdflib import Graph, URIRef
from rdflib.compare import isomorphic
from rdflib.namespace import RDF, OWL
from reasoning import KG
from reasoning.kg import ROOT, UCA, save_json
from evaluation.queries import catalog


def main():
    out=ROOT/"evaluation/results/iteration1_rerun";out.mkdir(parents=True,exist_ok=True)
    command=[sys.executable,str(ROOT/"iteration1/Code/build_kg.py"),"--output-dir",str(out/"rebuilt")]
    rebuilt=subprocess.run(command,cwd=ROOT,text=True,capture_output=True)
    (out/"build.log").write_text(rebuilt.stdout+rebuilt.stderr)
    if rebuilt.returncode: raise SystemExit("Iteration 1 rebuild failed; inspect build.log")
    kg=KG();new=Graph().parse(out/"rebuilt/uiuc_course_kg.ttl")
    counts={name:len(set(kg.explicit.subjects(RDF.type,UCA[name]))) for name in
            ["Course","CourseOffering","Section","Instructor","Department","PrerequisiteExpression",
             "PrerequisiteOption","CourseCondition","CourseChoiceCondition","StandingCondition","ConsentCondition","OtherCondition",
             "Student","CourseCompletion","PlannedEnrollment","CoreRequirement","ElectiveRequirement"]}
    ontology=Graph().parse(ROOT/"iteration1/Ontology/uca_ontology.ttl")
    schema_counts={name:len({s for s in ontology.subjects(RDF.type,cls) if isinstance(s,URIRef)}) for name,cls in
                   [("classes",OWL.Class),("object_properties",OWL.ObjectProperty),("datatype_properties",OWL.DatatypeProperty)]}
    reports=[]
    for key,item in catalog().items():
        inferred=key.startswith("INF") or key=="Q11"
        rows=kg.query(item["query"],inferred=inferred)
        path=out/(item["name"]+".csv")
        if rows:
            with path.open("w",newline="") as f:
                writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
        else: path.write_text("")
        old=ROOT/"iteration1/Results/query_results"/(item["name"]+".csv")
        def normalized(records):
            return Counter(tuple(sorted((k,"" if v is None else str(v)) for k,v in row.items())) for row in records)
        original_rows=list(csv.DictReader(old.open())) if old.exists() else []
        # GROUP_CONCAT order is not specified by SPARQL: compare additionally as sets of items.
        def unordered(records):
            cleaned=[]
            for row in records:
                row=dict(row)
                for k,v in row.items():
                    if isinstance(v,str):
                        v=v.replace("https://example.org/uiuc-course-advisor/resource/", "").replace(str(UCA),"uca:")
                        row[k]=v
                    if isinstance(v,str) and " | " in v:row[k]=" | ".join(sorted(v.split(" | ")))
                    elif isinstance(v,str) and ", " in v:row[k]=", ".join(sorted(v.split(", ")))
                cleaned.append(row)
            return normalized(cleaned)
        reports.append({"query":key,"name":item["name"],"rows":len(rows),"original_saved_rows":len(original_rows),
                        "exact_csv_value_match":normalized(rows)==normalized(original_rows),
                        "match_after_uri_and_concat_normalization":unordered(rows)==unordered(original_rows),
                        "uses_closure":inferred})
    from pyshacl import validate
    shapes=Graph().parse(ROOT/"iteration1/RDF_Knowledge_Graph/shapes.ttl",format="turtle")
    conforms,report_graph,report_text=validate(kg.explicit,shacl_graph=shapes,inference="rdfs")
    (out/"shacl_report.txt").write_text(report_text)
    report_graph.serialize(out/"shacl_report.ttl",format="turtle")
    summary={"generated_utc":datetime.now(timezone.utc).isoformat(),"graph_sha256":kg.sha256,
             "explicit_triples":len(kg.explicit),"schema_triples":len(ontology),"abox_triples":len(kg.explicit)-len(ontology),
             "owlrl_closure_triples":len(kg.closure),"schema_counts":schema_counts,"entities":counts,
             "rebuild_isomorphic":isomorphic(kg.explicit,new),"shacl_conforms":bool(conforms),
             "parse_status":dict(Counter(str(v) for v in kg.explicit.objects(None,UCA.parseStatus))),
             "queries":reports,"note":"SHACL may report deliberately seeded synthetic test violations; inspect report."}
    save_json(out/"summary.json",summary);print(json.dumps(summary,indent=2))


if __name__ == "__main__":main()
