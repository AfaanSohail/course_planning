# ThinkPad review setup

This machine has Python 3.11.7 and an isolated project .venv. Locked dependencies were installed and the local tests passed. Raw test results are in report/laptop_checks/tests.xml and tests.txt. GraphDB was started from the existing Docker container without changing repository data; Q08 and INF1, INF3 and INF6 responses are saved under report/laptop_checks. GraphDB was then returned to its original stopped state to release RAM.

The ThinkPad uses CPU inference. The local readiness profile uses the cached Qwen3 4B Instruct weights with a separate model alias, 4,096 context tokens, a 3,000-character retrieval budget and 512 output tokens. These settings differ from the scored Kaggle experiment. Never merge this local answer with trial 3 or describe local settings as the experiment settings.

The runtime and weights are preserved in ../.local_runtime, outside the submission repository. Keep this directory on the laptop; do not upload model weights to GitHub. The cache is needed by scripts/start_review_model.sh.

## Run the local application

In a terminal in the project root:

```bash
bash scripts/start_review_model.sh
```

If the server is already running on port 11436, skip starting another instance. Otherwise leave that terminal open. In another project terminal:

```bash
source .venv/bin/activate
cp config/review_laptop.example.json config/local.json
python -m app --config config/local.json
```

Enter a supported question with a student, course and term. CPU inference can take several minutes, particularly for a cold prompt. Check actual local timing in report/live_grounded.json. The laptop should be demonstrated with a known-working model server; a saved response is not a live unseen-question answer.

## GraphDB and Protege

```bash
docker start graphdb
```

Open http://localhost:7200 and select Project_uiuc. Use the original ontology in Protege. Avoid running unnecessary applications on this 8 GB laptop. The recorded service checks do not replace the instructor's live walkthrough.

## Screenshot viewer

The viewer displays original execution artifacts and captures only its actual rendered desktop window, without drawing substitute screenshot pixels:

```bash
python scripts/review_display.py --record report/live_grounded.json --capture report/screenshots/grounded_app.png
python scripts/review_display.py --record report/live_insufficient.json --capture report/screenshots/insufficient_evidence.png
python scripts/review_display.py --comparison --capture report/screenshots/comparison.png
```

The captures depend on the local Linux X11/XWayland environment and xwd. On another system use its normal screenshot controls. The viewer itself does not call a model; the saved grounded response must first come from a genuine execution of python -m app. Close the viewer after inspecting it if using it without --capture.

## Preserved failed readiness attempt

The first CS421 response used a 6,000-character context and hit its 512-token output limit after producing the wrong table schema. It is preserved as report/laptop_checks/failed_CS421_grounded.json. This is separate from the scored Kaggle run. The subsequent short MATH241 question tests basic live functionality with a 3,000-character context, not general correctness on complex unseen questions.

## Observed local model result

The readiness request completed in 98.8 seconds, with finish_reason=stop. No output truncation or unknown citation IDs were flagged. This is one CPU timing, not a performance benchmark. GraphDB was stopped after its checks and must be started before the review. The ontology is open in Protege.
