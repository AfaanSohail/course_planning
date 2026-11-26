# Selected results and remaining submission work

The selected experiment is qwen3_trial3_kaggle. All twenty original JSON responses, the frozen expected snapshot, model identity, GPU metadata and logs are imported without rewriting the model answers. Earlier trial 1 records remain historical evidence.

The generated summary reports 0/10 correctness for the baseline and 6/10 for the grounded system. Supporting evidence is recorded for 0/10 baseline answers and 9/10 complete grounded answers under the strict review criterion. The recorded claim counts are 6 baseline and 1 grounded unsupported claims. These counts depend on the documented interpretation of qualified baseline refusals; all decisions are retained in grades.csv and evaluation_notes.md. Reviewer names and equal assignments were supplied by the team. Names alone do not independently verify that each review was performed.

A truthful baseline refusal is still incorrect when the question asks for information available in the frozen graph. Grounding passes CQ01, CQ03, CQ04, CQ08, CQ11 and CQ15. CQ02 omits three edges, CQ06 omits three completed requirement groups, CQ10 omits CS 581, and CQ13 adds an unsupported claim about other prerequisites. Full answers remain available for checking. No failed answer has been repaired by hand.

The artifact audit reports twenty model calls, no flagged truncation, no unknown citation IDs and 4,679 valid distinct graph evidence edges. These checks establish artifact consistency rather than semantic correctness. The saved Kaggle test run reports 39 passing tests. The source manifest records no Git commit because the run occurred outside a checkout; preserve that limitation.

The three selected explainability examples are CQ03 eligibility, CQ08 multi-hop traversal and CQ11 inference-dependent aggregate. CQ06 remains available as an error-analysis example. Trial 3 was developed after inspecting earlier failures and is not an independent held-out benchmark.

## Verified laptop and actual captures

The ThinkPad passed fresh Python 3.11.7 environment tests, live GraphDB multi-hop and inference checks, Protege ontology loading, one fresh local Qwen3 answer and insufficient-evidence handling. The actual desktop screenshots for grounded_app, insufficient_evidence and comparison are registered. See report/laptop_checks/readiness.json and report/LAPTOP_READINESS.md. Local CPU inference takes several minutes and uses a smaller context/output allocation than the scored Kaggle run. The earlier CS421 readiness attempt was incorrectly formatted and truncated at 512 output tokens; it remains saved as failed_CS421_grounded.json. A successful short case does not establish correct answers to every unseen question. It is a separate readiness check, not an additional benchmark response.

## Remaining external evidence

1. Externally hosted 3 to 5 minute demo recording and URL.
2. Final implementation source commit after the team commits and pushes the integrated changes, plus instructor access confirmation.
3. Regenerate the final consolidated PDF after supplying those values. Historical Kaggle manifests retain their missing experiment-time Git SHA.

## Commands

```bash
python -m evaluation.score --run-id qwen3_trial3_kaggle
python -m scripts.audit_received_run --run-id qwen3_trial3_kaggle
python -m scripts.verification_status
python -m report.build
# After actual external evidence and metadata are supplied:
python -m report.build --final
```
