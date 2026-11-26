# Explainability records

The selected trial 3 examples are live_eligibility.md (CQ03), live_multihop.md (CQ08), and live_inference.md (CQ11). These contain actual LLM answers, stored/inferred evidence and query provenance. Full raw answers are under evaluation/results/qwen3_trial3_kaggle. The live_progress.md example explicitly records CQ06's incomplete answer for error analysis.

```bash
python -m explainability.format evaluation/results/qwen3_trial3_kaggle/CQ03_B.json explainability/live_eligibility.md
python -m explainability.format evaluation/results/qwen3_trial3_kaggle/CQ08_B.json explainability/live_multihop.md
python -m explainability.format evaluation/results/qwen3_trial3_kaggle/CQ11_B.json explainability/live_inference.md
```

Stored triples, OWL-inferred triples, computed query/application conclusions and LLM-generated prose have distinct labels. Option C produces no predictions. A valid edge does not prove a generated sentence is correct.

For the viva, trace one cited result to its query and full graph evidence. Explain how the multi-hop rows preserve potential branches and why an absent completion is not a stored negative fact.
