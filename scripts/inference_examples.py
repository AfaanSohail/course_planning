"""Three real inferred conclusions with explicit premises and schema axioms."""
from rdflib.namespace import OWL
from reasoning import KG
from reasoning.kg import ROOT, RES, UCA, save_json


if __name__ == "__main__":
    kg=KG(); c=RES["course/CS421"];s=RES["student/S003"];d=RES["department/CS"]
    offering=next(o for o in kg.objects(c,UCA.hasOffering) if RES["term/2026-fa"] in kg.objects(o,UCA.offeredInTerm))
    cp=next(cp for cp in kg.objects(s,UCA.hasCompletion) if RES["course/CS124"] in kg.objects(cp,UCA.completedCourse))
    specifications=[
        ("inverse_department",(d,UCA.hasCourse,c),[(c,UCA.inDepartment,d)],
         "inDepartment owl:inverseOf hasCourse",UCA.inDepartment,OWL.inverseOf),
        ("completion_chain",(s,UCA.hasCompletedCourse,RES["course/CS124"]),
         [(s,UCA.hasCompletion,cp),(cp,UCA.completedCourse,RES["course/CS124"])],
         "hasCompletion o completedCourse -> hasCompletedCourse",UCA.hasCompletedCourse,OWL.propertyChainAxiom),
        ("offering_chain",(c,UCA.scheduledInTerm,RES["term/2026-fa"]),
         [(c,UCA.hasOffering,offering),(offering,UCA.offeredInTerm,RES["term/2026-fa"])],
         "hasOffering o offeredInTerm -> scheduledInTerm",UCA.scheduledInTerm,OWL.propertyChainAxiom)]
    examples=[]
    for name,conclusion,premises,rule,axiom_s,axiom_p in specifications:
        if conclusion in kg.explicit or conclusion not in kg.closure:raise ValueError("Conclusion must be genuinely inferred")
        if not all(p in kg.explicit for p in premises):raise ValueError("Premises must be stored facts")
        examples.append({"name":name,"conclusion":kg.edge(*conclusion),"premises":[kg.edge(*p) for p in premises],
                         "rule":rule,"schema_axioms":[kg.edge(axiom_s,axiom_p,o) for o in kg.objects(axiom_s,axiom_p)],
                         "absent_from_explicit":True,"present_in_closure":True})
    save_json(ROOT/"reasoning/outputs/inference_examples.json",examples)
    print("Saved three checked OWL deductions with their stored premises.")
