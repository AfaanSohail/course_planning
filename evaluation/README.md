# Evaluation — Diya Hurmat

Read [SCORING.md](SCORING.md) for the complete protocol and human grading rules.

- `queries.py` loads and safely parameterizes the original SPARQL.
- `prepare.py` extracts original CQ wording and executes graph-verified expected rows.
- `run.py` records actual isolated LLM-only and grounded calls under one manifest.
- `score.py` validates human reviews and raw hashes before producing the comparison.
- `results/iteration1_rerun/` preserves the real rebuild, queries and SHACL output.
- `results/retrieval_validation.json` checks actual natural-language routing and evidence without calling an LLM.
- `tests/` covers incomplete/changed/duplicate grading records and the final report gate.

Run from the repository root:

```bash
python -m evaluation.prepare
python -m scripts.validate_retrieval
python -m evaluation.run --config config/local.json --run-id NEW_RUN_ID --conditions AB
python -m evaluation.score --run-id NEW_RUN_ID --init
# Perform and record human review; then:
python -m evaluation.score --run-id NEW_RUN_ID
```

## How to explain this in the viva

Show the original wording, graph query, actual A/B prompts and outputs, fixed model/settings, human per-claim judgment and generated table. Explain that retrieval validation is not an LLM accuracy experiment. A model refusal can avoid unsupported claims while failing correctness. The saved raw-file hashes prevent accidentally grading a different response.

## Completed selected run

qwen3_trial3_kaggle is already complete. Do not initialize or rerun into that ID. Its grades.csv, comparison.csv, summary.json and evaluation_notes.md contain the recorded evaluation. Reproduce totals with `python -m evaluation.score --run-id qwen3_trial3_kaggle`. Reviewer assignments were supplied by the team. Review notes define strict complete-answer correctness and enumerate unsupported claims.
