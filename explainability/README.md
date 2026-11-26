# Explainability records

Run commands from the repository root. Existing example_1 through example_5 records contain actual KG retrieval or insufficient-evidence results. They are not LLM answers unless llm_called is true. A retrieval-only record does not satisfy the requirement for three generated system answers.

```bash
python -m scripts.retrieval_examples
```

The formatter separates stored RDF, OWL-inferred triples, computed query/application conclusions and generated prose. It preserves complete query rows, traces and provenance without treating valid edge IDs as proof that a sentence is correct. Option C produces no predictions.

Actual LLM answers and final evaluation artifacts should be committed separately by their assigned members. Retain original response bytes and human-review evidence when importing a completed run. For the viva, explain the distinction between an application verdict and an official registration or degree decision.
