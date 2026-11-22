# Evaluation protocol and human scoring — Diya Hurmat

`python -m evaluation.prepare` reads the original 15-question table from the supplied report and selects CQ01, CQ02, CQ03, CQ04, CQ06, CQ08, CQ10, CQ11, CQ13 and CQ15. These include chains, a minimum-two-hop traversal, an OWL-dependent aggregate, transcript decisions, hypothetical effects and evidence questions. Original wording is retained, and explicit instance text supplies synthetic student/course/term details equally to A and B. Expected rows are computed by executing the supplied queries, not copied from narrative answers.

```bash
python -m evaluation.prepare
python -m evaluation.run --config config/local.json --run-id qwen3_trial1 --conditions A
python -m evaluation.run --config config/local.json --run-id qwen3_trial1 --conditions B
python -m evaluation.score --run-id qwen3_trial1 --init
# Open evaluation/results/qwen3_trial1/grades.csv and review each raw answer.
python -m evaluation.score --run-id qwen3_trial1
```

Using `--conditions AB` alternates which condition runs first. Separate A/B runs support the team's planned work days but introduce a time/order limitation. Both modes use the same config, max output tokens, temperature, stateless chat client and exact question. Only B receives graph context and the grounding instructions. It is an end-to-end system comparison, not an isolated causal estimate of retrieval alone. Do not change prompts, model or graph mid-run. The manifest records prompt/question/KG hashes, source commit and settings. For the selected Ollama configuration, the harness reads the actual model digest, details and runtime version and rejects a changed identity between A and B. Also save `ollama list` and `ollama show course-planning-qwen3` for review: a tag alone is not a frozen model digest. Hosted API model identity depends on provider metadata and may be less controllable.

A receives no KG facts, expected rows, synthetic transcript or tools. Those synthetic details naturally disadvantage a memory-only model; acknowledge this when interpreting results. B must use the real question router, not the case's query ID. Confirm that `retrieval.intent` matches the intended question. Human graders can inspect expected rows; neither condition receives the evaluation's expected-answer file.

For every CSV row, fill:

- `correct`: `Yes` only if all requested conclusions agree with expected rows and the response supplies the requested information. A full-list question needs set completeness. A truthful refusal is not a correct substantive answer when the KG can answer it. Mark summaries/incomplete sets according to this preregistered rule, and explain omissions. No partial-credit accuracy is added to the required score.
- `evidence_available`: `Yes` only for inspectable provenance supporting the actual answer. A plausible URL or an invented citation is insufficient. In A, mark `No` unless the actual answer supplies verifiable supporting evidence; no automatic assumption or score is made. In B inspect cited edges/rows, relevance and the full provenance artifact. An unrelated graph attached to a wrong answer does not establish supporting evidence.
- `unsupported_claims`: nonnegative integer, counted by atomic factual claims that are absent from, contradicted by or unjustified by verified context. Enumerate each offending claim in `notes` and say whether contradicted or unverified. An abstention can be incorrect without hallucinating. Shared text is not a second claim unless it makes a distinct assertion.
- `reviewer`: actual human who checked the answer. `notes`: explain correctness, completeness, provenance and every unsupported claim. A second member should independently review disagreements and record the resolution. Do not use an LLM's self-grade as final truth.

The scorer checks one A and B grade per CQ and hashes each reviewed raw file. Missing answers/reviews prevent a scored table. It generates the official six-column `comparison.csv` and totals out of ten only after all reviews. API failures are saved separately and never counted as zero or silently replaced. The summary counts actual LLM calls, so abstention routes cannot masquerade as successful model calls. Unit tests use transport spies; these are not experimental outputs.

Report where B fixed an A error, where both succeeded/failed, unsupported claim counts, supporting evidence counts, truncation/abstentions, router errors, and limits. Do not generalize ten purposively chosen CQs to all university advising. Reachability/SPARQL agreement verifies implementation on this snapshot; it is not an independent truth audit of its catalog parser.

## How to explain this in the viva

Open one A and B raw file, trace its question to the original CQ and expected query, then show the human review. Explain why a refused answer earns zero correctness but may have zero hallucinations. Show the model/settings/hash manifest and why expected answers do not leak into A. Reproduce the table from `grades.csv`; never type the reported score by hand.
