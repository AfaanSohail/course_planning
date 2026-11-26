# Consolidated report — Diya Hurmat

`iteration2_sections.md` contains the report prose. `build.py` assembles both iterations into **one** PDF and a readable text artifact, inserting tables only from actual JSON/CSV outputs. It imports the original CQ/mapping/design tables, not the original contribution claims. Generated rows and code outputs are execution artifacts, not screenshots.

```bash
python -m report.build
# After real runs, grading, actual screenshots, contribution links and metadata:
python -m report.build --final
```

The default output is clearly labelled DRAFT. It includes current measured graph/reasoner/query results but the scored trial 3 comparison and actual generated answer examples. It must not be submitted as a completed experiment. `--final` checks required run artifacts, human scoring, three actual B answer records, actual Iteration 2 screenshot entries, clean-machine and review-laptop confirmation and completed repository/contribution/video fields. These checks only establish artifact presence and local consistency; a human still verifies the facts and each screenshot's authenticity.

Update `submission.json` with actual commit URLs, the immutable source commit, demo URL, run ID and a truthful clean-machine result. Add actual execution images to `screenshots/manifest.json` using paths relative to the repository and `iteration: 2`. Include captures of the running app with evidence, reasoning summary, comparison table and insufficient-evidence response. Existing images are explicitly archived Iteration 1 evidence.

The final source commit cannot contain its own hash. Commit code/results, record that immutable SHA in the metadata and generate the PDF from it. A later documentation-only commit can store the PDF and recorded source SHA; tag the source commit for the submitted implementation. Identify both commits if relevant, without claiming a self-referential hash. Do not rewrite history after submission.

## How to explain this in the viva

Locate one table's input file and rerun its generating script. Explain every pending field if using a draft. Show your actual authored commits rather than the planned task schedule. ChatGPT was used to assist with code, documentation and prompts, and to cite external code, datasets, ontologies, prompts, libraries, tutorials and other resources. Identify changes each member reviewed and implemented. Demonstrate that no test spy, handmade table or synthetic screenshot became an experimental result.

Current selection: qwen3_trial3_kaggle. Grading entries and scored results are integrated. Final generation also requires screenshot categories grounded_app, insufficient_evidence and comparison, plus review_laptop_verified=true supported by a real check. Kaggle provides isolated-environment execution evidence; it does not establish review-laptop readiness.
