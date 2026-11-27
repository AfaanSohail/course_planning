# Live review and recorded-demo script

Run commands from the repository root after setup. Verify the laptop before the review: local Python environment, GraphDB repository, Protégé, downloaded Ollama model and config, real scored A/B artifacts. A retrieval-only run cannot replace the LLM demonstration.

## Live viva: Afaan

1. Open `iteration1/Ontology/uca_ontology.ttl` in Protégé. Show Course, PrerequisiteExpression, PrerequisiteOption, the condition subclasses, `mentionsCourse`, `hasPrerequisiteCandidate` and `hasPrerequisitePath`. Explain the actual ontology IRIs and AND/OR structure.
2. Start GraphDB and select the existing `Project_uiuc` repository shown in the archived screenshot, or your actual repository ID. If creating a new local repository, select OWL2-RL and import **only** `iteration1/RDF_Knowledge_Graph/uiuc_course_kg.ttl`; it already contains the T-Box. Keep names/configuration truthful and capture the current setup.
3. Export queries with `python -m scripts.export_queries`. Paste `evaluation/queries/Q02.rq` and `Q08.rq` into GraphDB's SPARQL view to show multi-hop traversal. Contrast Q02's possible branches with compulsory prerequisites.
4. Run INF1, INF3 and INF6 with inference enabled. Show actual stored premises and absent inferred conclusions using `reasoning/outputs/inference_examples.json`. In the Workbench disable inference and rerun to demonstrate the difference; do not infer based only on a screenshot.

Optional endpoint capture (adjust the repository ID to the actual server):

```bash
python -m scripts.graphdb_check --endpoint http://localhost:7200/repositories/Project_uiuc --query Q11 --output reasoning/outputs/live_graphdb_Q11.json
python -m scripts.inference_examples
python -m reasoning prerequisite_chain --course CS421 --output reasoning/outputs/live_chain.json
python -m reasoning eligibility --student S003 --course CS421 --output reasoning/outputs/live_eligibility.json
python -m reasoning prerequisite_chain --course CHEM202 --output reasoning/outputs/live_cycle.json
python -m reasoning degree_progress --student S004 --output reasoning/outputs/live_degree.json
python -m reasoning.evaluate
```

Explain at least these three inferred facts from the saved, programmatically checked examples: department → course from inverse `inDepartment`; student → completed course from the completion chain; course → term from the offering chain. Each conclusion is checked absent in explicit RDF and present in closure. Then show how the Python AND/OR verdict differs from an OWL shortcut property.

## Live viva: Hassan

On this ThinkPad, start the preserved runtime with `bash scripts/start_review_model.sh` if the server is not already running on port 11436. Use `config/local.json` copied from `config/review_laptop.example.json`. See `report/LAPTOP_READINESS.md` for the measured CPU latency and preserved failed readiness attempt. The local profile differs from the scored Kaggle settings. Show the actual model config and runtime evidence. Run the app in interactive mode and accept an unseen question from the instructor:

```bash
python -m app --config config/local.json
```

Supported questions should identify a course/student/term as appropriate. An example to practice, not a cached answer:

```bash
python -m app 'Can S004 take CS 425 in Fall 2026?' --config config/local.json --output app/live_unseen.json
```

Open the output and show `retrieval.entities`, `intent`, `query`, `rows`, `context`, the actual provider `completion`, generated `answer` and supporting `evidence` IDs. Explain schema-inferred versus application-rule conclusions and any warnings. The response is obtained live; there is no demo-answer lookup.

Show two insufficient-evidence cases:

```bash
python -m app 'What is the weather for CS 421?' --output app/live_insufficient.json
python -m app 'Can S003 take CS 421 in Fall 2027?' --output app/live_unknown_term.json
```

Point to `mode=insufficient_evidence` and `llm_called=false`. Explain what is missing. Demonstrate that a known course code does not justify answering an unrelated question.

## Live viva: Diya

Open `evaluation/cqs.json`, one real A/B pair, the manifest, human `grades.csv`, `comparison.csv` and `summary.json`. Verify the same question/model/settings and show the actual prompt/context difference. Regenerate the scores, then show three formatted examples and their full raw JSON.

```bash
python -m evaluation.score --run-id qwen3_trial3_kaggle
python -m explainability.format evaluation/results/qwen3_trial3_kaggle/CQ11_B.json explainability/live_inference.md
python -m report.build --final
```

Explain where grounding helped or did not using the saved errors; distinguish a non-hallucinating refusal from a correct substantive answer. Show actual GitHub member commits and the submitted source hash. Do not present the planned contribution table as historical evidence.

## Suggested 3–5 minute recording storyboard

- 0:00–0:30: project, frozen sources, synthetic students, actual ontology/GraphDB setup.
- 0:30–1:15: multi-hop query and one complete AND/OR trace; briefly show the three inference examples.
- 1:15–2:35: live natural-language question → retrieval → actual LLM answer → cited evidence.
- 2:35–3:05: insufficient-evidence response and its missing information.
- 3:05–4:00: real ten-question A/B table, unsupported-claim/evidence scores and one limitation.
- 4:00–4:30: repository, individual contributions and source commit.

Record the actual application with readable text, upload externally, test viewer access, then update `report/submission.json`. These times are a planned storyboard, not a claim that a recording exists. Add real new screenshots to `report/screenshots/manifest.json` with informative captions. Keep the video out of Git and Classroom; include its link in the PDF.
