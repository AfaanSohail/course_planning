"""Hash the supplied primary artifacts and record their stated provenance."""
import hashlib
from reasoning.kg import ROOT, save_json


if __name__=="__main__":
    inputs={
        "iteration1/Ontology/uca_ontology.ttl":"Preserved user-supplied ontology v1.3; do not change IRIs.",
        "iteration1/RDF_Knowledge_Graph/uiuc_course_kg.ttl":"Reviewed explicit RDF snapshot, including ontology.",
        "iteration1/Dataset/course-catalog.csv":"Supplied Fall 2026 CSV; https://discovery.cs.illinois.edu/dataset/course-catalog/",
        "iteration1/Dataset/uiuc-prerequisites.csv":"QA only; https://github.com/illinois/prerequisites-dataset",
        "iteration1/SPARQL_Queries/queries.txt":"Supplied original CQ and symbolic-inference queries.",
        "iteration1/Report/Report.docx":"Supplied original report with exact CQ wording and mapping.",
        "assignment/KRR_Iteration_2_29_November.docx":"Official requirements supplied by the user; deadline 29 November 2026, 11:55 PM PKT."}
    save_json(ROOT/"evaluation/results/input_provenance.json",[
        {"path":name,"sha256":hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),"provenance":note}
        for name,note in inputs.items()])
    print("Saved primary-input hashes; no source file was changed.")
