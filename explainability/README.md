# Explainability — Diya Hurmat

```bash
python -m scripts.retrieval_examples
python -m scripts.inference_examples
python -m explainability.format app/answer.json explainability/live_answer.md
```

Three retrieved-context examples are supplied for eligibility, inferred elective counts and degree progress. They contain real KG output and explicitly pending LLM prose. After a live run, format three grounded raw answers (for example CQ03_B, CQ06_B and CQ11_B) with the same command and include them in the report. A retrieval-only record does not satisfy the requirement for three **LLM system answers**; the final report gate requires live B artifacts.

Explicit facts are checked against the input TTL. An inferred edge is absent there and present in the computed OWL RL closure. Computed option verdicts, counts, missing-condition conclusions and allocations are application/query results, not new RDF triples. Generated text is the actual model output only. Option C produces no predictions. Hypothetical completion assumptions remain labelled separately and are never inserted as evidence.

Each JSON keeps full paths and actual SPARQL. The formatter exports them without changing the LLM response. The report uses concise selections and points to the complete machine-readable artifacts. `reasoning/outputs/inference_examples.json` independently records three concrete deductions with their actual stored premises and schema axioms; those are suitable for the live symbolic-inference explanation.

## How to explain this in the viva

Choose one cited edge, show it in the explicit TTL, then choose an inferred edge and show its absence from the stored graph and presence in closure. Explain its recorded premise chain. Finally identify the LLM sentence as generated prose, whose correctness still needs checking. Explain why a 'missing completion' result is an absence check over the snapshot rather than an explicitly stored negative triple.
