# Grading worksheet — run qwen3_trial1

**AI-assisted pre-review draft, NOT the human review.** Per `evaluation/SCORING.md`, the
`reviewer` must be the actual human who checked each answer, and an LLM grade is not final
truth. Open each `CQxx.md`, check the evidence against the raw answer JSON and expected rows,
make your own decision, and type it into `evaluation/results/qwen3_trial1/grades.csv`.
Do not submit this folder as the human review.

## Suggested values (verify every row)

| CQ | Cond | correct | evidence | unsupported | Confidence / judgement call |
|----|------|---------|----------|-------------|-----------------------------|
| CQ01 | A | No | No | 0 | high; refusal |
| CQ01 | B | Yes | No | 3 | medium; list exact (15/15) but no citations; one closing sentence contradicts its own list, so strict reading → correct=No; count 3–4 |
| CQ02 | A | No | No | 0 | high; refusal, hypothetical example not counted |
| CQ02 | B | No | No | 21 | truncated, 16 edges missing, 4 invented; count 11–24 depending on convention; evidence could defensibly be Yes |
| CQ03 | A | No | No | 0 | medium-high; refusal; 0–2 |
| CQ03 | B | Yes | Yes | 1 | medium; strict reading of "alternatives fully met" → correct=No, unsupported=2 |
| CQ04 | A | No | No | 3 | high on correct; count 0–8 |
| CQ04 | B | No | No | 11 | truncated; 7 blocked courses wrongly listed, 3 omitted; 7 invented row IDs (R29–R35); count 10–17 |
| CQ06 | A | No | No | 1 | medium; 0–2 |
| CQ06 | B | Yes | Yes | 0 | high; all 18 groups match |
| CQ08 | A | No | No | 0 | high; refusal |
| CQ08 | B | No | No | 25 | truncated, 3 of 24 upstream courses; count 13–25 depending on convention |
| CQ10 | A | No | No | 0 | high; refusal |
| CQ10 | B | No | Yes (borderline) | 2 | medium; omits CS 581, drops MATH 412/417 from final list; 0–2 |
| CQ11 | A | No | No | 1 | medium; "Fall 2026 not available" contradicted by KG; 0–1 |
| CQ11 | B | Yes | Yes | 0 | high; all 16 department counts exact |
| CQ13 | A | No | No | 1 | medium; 0–1 |
| CQ13 | B | No | No | 2 | high on correct; refused "insufficient evidence" although R1–R17 = expected; 1–3 |
| CQ15 | A | No | No | 0 | high; truthful refusal |
| CQ15 | B | Yes (borderline) | Yes | 2 | low on correct: truncated, but cut falls in final recap after all 3 courses covered; flip to No if you treat any truncation as incomplete or the "Option 1/2" mislabel as a wrong conclusion |

## Decisions to make once, then apply consistently

1. **Claim-counting convention.** Counts for CQ02_B, CQ04_B and CQ08_B swing a lot depending on
   whether repeated or list-style errors count per item or per line. Pick one rule, write it in
   the report, and apply it to all rows.
2. **Truncation.** SCORING.md fails *incomplete* answers, not truncated ones as such. CQ15_B is the
   only truncated answer where the content is arguably complete.
3. **Self-contradiction.** If an answer's own text contradicts its correct final list (CQ01_B),
   does it still count as correct?

## Side finding (code, not grades)

`citation_check.cited` misses IDs written inside comma-separated or ranged brackets
(e.g. `[R2, R3]`, `R1–R6`). This affects CQ06_B, CQ10_B and CQ15_B. Those IDs exist in the context,
so `unknown_ids` is not affected. It is worth mentioning as a limitation in the report.
