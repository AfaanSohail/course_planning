# course_planning — Iteration 2

Knowledge-Grounded University Course Planning and Prerequisite Advisory System. AI-3001 Knowledge Representation & Reasoning, Ms. Mehreen Javaid. Afaan Sohail (24i-0081), Hassan Tariq (24i-2555), Diya Hurmat (24i-0094).

Repository specified by the team: https://github.com/AfaanSohail/course_planning . Official deadline: **29 November 2026, 11:55 PM PKT**.

This directory is the complete source solution; the sibling `commits/` directory contains prospective daily task/commit guides. The original archive was unpacked into `iteration1/`, preserving its ontology, graph, builder, parser, data, reports, queries, saved outputs and actual screenshots. Original IRIs are unchanged. The source graph is authoritative; rebuilding uses a separate output directory.

## What is implemented and what is pending

Implemented: four multi-hop templates; AND/OR eligibility; cycle/depth guards; target-term concurrency; hypothetical unlock comparison; degree allocations/conflicts; OWL RL closure; evidence-labelled CLI; generic entity/template retrieval; local/API LLM wrapper; prompts; ten-CQ expected-answer generation; immutable paired-run artifacts; human scoring; explainability formatter; full Iteration 1 reproduction/SHACL; unit tests; PDF assembly; viva and GitHub instructions.

Actual reasoning, query and test measurements are retained in their execution artifacts. The selected experiment is qwen3_trial3_kaggle: twenty recorded model calls, no flagged output truncation, and a completed grading sheet assigned equally to Hassan Tariq and Diya Hurmat. The scored summary and comparison table are generated from that sheet. Trial 1 and received archives remain historical evidence. Video and final source commit remain pending. Existing reasoning screenshots are included; actual grounded application, insufficient-evidence and scored-comparison captures are now registered. The PDF remains a draft until submission evidence is complete.

## Repository layout and ownership

```text
reasoning/        Afaan: KG access, four templates, validation, outputs, tests, research
app/              Hassan: entities, retrieval, context, LLM transport, CLI, tests
prompts/          Hassan: exact baseline/grounded system prompts
config/           Shared: credential-free examples and local Ollama Modelfile
evaluation/       Diya: original CQs, real ground truth, A/B harness, human scoring
explainability/   Diya: labelled evidence and actual/pending example records
report/           Diya: report prose, architecture, metadata, screenshots, PDF builder
scripts/          Integration: original ETL/query reproduction and demo helpers
iteration1/       Preserved original submission, including original CSVs and screenshots
.github/          Tests workflow
```

Each owned folder has a README with commands and viva notes. The schedule is not evidence of completed individual work; report actual contributions and ChatGPT use accurately.

## Prerequisites and Python setup

Use Python 3.11 or 3.12, Git, internet for dependency/model downloads, and a local terminal. GraphDB 10.7 and Protégé are needed for the live review. A virtual environment avoids conflicts with ROS/Anaconda plugins. A CPU-only local LLM can be slow; close other applications and use a laptop with sufficient free RAM. The selected 4B model plus a 16K context may exceed a busy 8 GB machine. A machine with 16 GB RAM is a practical starting point to test, not a certified minimum or measured performance guarantee.

From this directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.lock.txt
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q --junitxml=evaluation/results/tests.xml
```

On Windows activate with `.venv\Scripts\Activate.ps1`; set `$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'` before pytest. `pyparsing` is explicitly pinned because the older preinstalled version failed with the installed RDFLib SPARQL engine. The declared dependencies and tests were also verified in a fresh isolated virtual environment (see tests_clean_environment.xml). requirements.lock.txt records that environment, including transitive dependencies. A fresh local Python 3.11.7 environment now passes all 39 tests; the ThinkPad functional readiness record is in report/laptop_checks/readiness.json. CPU latency and the failed complex-question attempt are preserved. If ROS adds packages through PYTHONPATH, unset that variable for the project shell before testing.

## Data preparation and local validation

No new source download is required. The archive already includes the Fall 2026 CSVs, curated A-Boxes and builder/parser. Run:

```bash
python -m scripts.reproduce_iteration1
python -m reasoning.evaluate
python -m evaluation.prepare
python -m scripts.export_queries
python -m scripts.inference_examples
python -m scripts.retrieval_examples
python -m scripts.validate_retrieval
python -m scripts.environment
```

The reproduction rebuilds into `evaluation/results/iteration1_rerun/rebuilt/` and checks RDF isomorphism without replacing the reviewed graph. It runs every original Q01–Q15 and INF1–INF6 query, then the supplied SHACL shapes. The output preserves raw CSVs, build/validation logs and actual metrics. Original display differences (full/abbreviated IRIs, unbound cells and unordered GROUP_CONCAT items) are normalized only in an additional comparison; raw outputs stay unchanged. Named classes are counted separately from anonymous OWL class expressions.

The reasoner evaluation independently compares full reachable sets with SPARQL, all synthetic students' Q01 sets and CS421's Q03 conditions, checks actual returned edges and saves negative/cycle/depth examples. Consult the measured summaries instead of copying a historical closure count. A SHACL pass covers the supplied shapes and does not validate every prose degree rule.

## Run the reasoning component

```bash
python -m reasoning prerequisite_chain --course CS421 --output reasoning/outputs/my_chain.json
python -m reasoning eligibility --student S003 --course CS421 --output reasoning/outputs/my_eligibility.json
python -m reasoning reverse_unlock --student S002 --course CS225 --output reasoning/outputs/my_unlock.json
python -m reasoning degree_progress --student S003 --output reasoning/outputs/my_progress.json
python -m reasoning prerequisite_chain --course CHEM202
python -m reasoning prerequisite_chain --course CS421 --max-depth 1
```

A course hop contains expression/option/condition entities. `paths` contains real graph edges and `expression_tree` preserves alternatives. Rule verdicts are computed conclusions; hypothetical completions are assumptions. No predicted links are generated. The API contract is documented in `reasoning/README.md`.

## Free local LLM: Qwen3 4B Instruct with Ollama

Install Ollama using the platform instructions at https://docs.ollama.com/quickstart . It is an external runtime, not a Python dependency. Do not put downloaded model weights in Git. Start the local server (desktop app, or a terminal running `ollama serve`), then:

```bash
ollama pull qwen3:4b-instruct
ollama create course-planning-qwen3 -f config/Modelfile
cp config/ollama.example.json config/local.json
ollama list
ollama show course-planning-qwen3
python -m app 'Can S003 take CS 421 in Fall 2026?' --config config/local.json --output app/answer.json
```

This local configuration requires no API key and has no per-call API billing. Ollama is not installed in this Linux development environment. Supplied external execution records are imported and labelled as such; local model execution is not claimed. Test memory and context handling on your review laptop. If the laptop cannot run the 4B model, change **both** conditions to a smaller Qwen3 model available in the official library and use a new run ID; disclose that change. Do not mix models in one comparison. A smaller model's answer quality must be measured, not assumed.

The credential-free alternative is `config/api.example.json`: set the actual compatible HTTPS endpoint/model, copy to ignored `config/local.json`, and export `COURSE_LLM_API_KEY` in your local shell. Hosted-provider free tiers can change and may require an account; this solution's free choice is local inference. Never save credentials in a config, report, prompt or commit.

The model context is configured through `config/Modelfile`, not just the Python output budget. The context builder includes all query rows or abstains, and reports any omitted traces/evidence. Full provenance remains in the saved JSON. Character limits approximate tokens, so inspect provider errors and length-truncated answers.

## App, unseen questions and missing evidence

```bash
python -m app 'Can S003 take CS 421 in Fall 2026?' --retrieve-only --output app/retrieval.json
python -m app 'For CS 440, show possible prerequisite chains back to root courses.' --config config/local.json --output app/unseen.json
python -m app 'What is the degree progress for S004?' --config config/local.json --output app/degree.json
python -m app 'What is the weather for CS 421?' --output app/insufficient.json
python -m app 'Can S003 take CS 421 in Fall 2027?' --output app/unknown_term.json
python -m app --config config/local.json
```

The app prints generated text, graph evidence, query, rows and trace. Retrieval-only mode explicitly produces no LLM answer. Unsupported/unknown questions abstain without a provider call. Personal questions need a student identifier, and general offering questions need a term. Follow-up turns are stateless. The router supports question families, not unrestricted natural language or silent selection of missing personal details. Try a genuinely unseen supported question during the live viva.

## Ten-question experiment and explainability

```bash
python -m evaluation.prepare
python -m evaluation.run --config config/local.json --run-id NEW_RUN_ID --conditions AB
python -m evaluation.score --run-id NEW_RUN_ID --init
# Review each raw answer and fill grades.csv using evaluation/SCORING.md.
python -m evaluation.score --run-id qwen3_trial3_kaggle
python -m explainability.format evaluation/results/qwen3_trial3_kaggle/CQ03_B.json explainability/live_eligibility.md
python -m explainability.format evaluation/results/qwen3_trial3_kaggle/CQ06_B.json explainability/live_progress.md
python -m explainability.format evaluation/results/qwen3_trial3_kaggle/CQ11_B.json explainability/live_inference.md
```

Use `--conditions A` on the planned A day and `--conditions B` on the B day with the same run ID/settings, or `AB` to alternate order. Runs preserve raw provider responses and actual prompts. The harness never sends expected answers to the LLM. Missing model calls, changed artifacts or incomplete human grades prevent a scored report. Correctness, unsupported claims and provenance require human semantic review. See `evaluation/SCORING.md` for the exact rubric, limitations and failure handling. Save Ollama version/model digest alongside each run.

## Report, screenshots and submission

```bash
python -m report.build
# Complete report/submission.json, actual screenshot manifest and A/B scoring.
python -m report.build --final
```

The draft PDF and generated text consolidate both iterations. All inserted metrics/tables come from execution files or identified preserved design tables. The PDF includes the scored trial 3 answers, error notes and provenance. `--final` rejects missing evidence. Record actual screenshots yourself; do not substitute a drawn terminal or generated UI image. Upload one final consolidated PDF to Classroom, with a GitHub URL, usernames, immutable source commit, truthful contribution links and an externally hosted 3–5 minute demo. See `report/README.md` for the source-commit/PDF hash convention and `REVIEW_DEMO.md` for the review.

## GitHub and team work

Follow `GITHUB_SETUP.md`. The supplied URL and usernames are recorded, but no repository settings, invitations, pushes or commits have been performed by this solution. Instructor username and demo URL remain pending. The sibling `commits/Afaan`, `commits/Hassan`, `commits/Diya` directories map the agreed tasks to 21–28 November. Each member must use their own account and commit actual understood work on the actual work day. Do not manufacture authorship or backdate the schedule.

## Sources and resource attribution

Research and primary references are in `reasoning/RESEARCH.md`, `app/RESEARCH.md` and `report/iteration2_sections.md`. The exact source archive is the user-supplied Iteration 1 submission; copied ontology/IRIs and original ETL authorship remain intact. ChatGPT was used to assist with code, documentation and prompts, and to cite external code, datasets, ontologies, prompts, libraries, tutorials and other resources. The team must cite that assistance, review/modify the code, reproduce outputs and defend individual contributions. No API keys, invented experimental outputs, artificial member commits or generated screenshots are included.

## Selected completed experiment

Trial 3 used Qwen3 4B Instruct on Kaggle GPU, with matching A/B settings. See `report/RESULTS_REVIEW.md` for measured totals and remaining errors. Do not rerun into the completed ID; use a new ID for a new experiment. Team-supplied reviewer assignments do not establish individual implementation contributions.

## Verified ThinkPad setup

See `report/LAPTOP_READINESS.md` and `report/laptop_checks/readiness.json`. All 39 tests passed in the new local Python 3.11.7 environment. GraphDB and Protege checks succeeded, a fresh Qwen3 response completed, and actual application screenshots are registered. Local CPU inference is slow and uses the separate `config/review_laptop.example.json` profile. The scored Kaggle experiment remains unchanged.
