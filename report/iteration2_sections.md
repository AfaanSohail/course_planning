# Iteration 2 report: multi-hop reasoning

This is Afaan Sohail's reasoning section for the consolidated team report. Application architecture, LLM evaluation, final submission metadata and the other members' sections are integrated separately.

## Purpose and scope

The reasoning component extends the UIUC Fall 2026 RDF graph with prerequisite-chain exploration, synthetic-student eligibility checks, hypothetical reverse unlocks and recorded degree-allocation progress. It follows actual graph relationships, retains intermediate entities and evaluates AND/OR conditions. Option C produces verified graph traversals and computed application conclusions. It does not predict new prerequisite links or insert hypothetical completions into the graph.

## Method: Option C multi-hop KG reasoning

A prerequisite-course hop is a sequence through an expression, an option, a condition and a referenced course. The reasoner follows these stored edges and records every intermediate entity. It retains a nested expression tree so that different options remain alternatives, conditions within an option remain conjunctions, and a CourseChoiceCondition requires only one of its candidates. Therefore a course appearing on a possible path is not automatically a compulsory prerequisite.

Path-based reasoning has a substantial research history. Lao and Cohen (2010) learn relational retrieval from edge-label sequences; DeepPath learns relational navigation policies (Xiong et al., 2017), and MINERVA conditions navigation on a query (Das et al., 2018). These sources motivated preserving typed paths and examining intermediate decisions. Our implementation is a deterministic symbolic traversal suitable for the supplied graph; it does not implement their trained policies, embeddings or link-prediction objectives. Hogan et al. (2021) informed the distinction between querying, deduction and induction. Option C here produces verified traversals and rule conclusions, with no predicted links.

Prerequisite-chain search uses a path-local ancestry set to stop cycles while allowing the same course to appear on different valid branches. A course-hop depth bound and terminal-path bound control enumeration; the trace explicitly marks cycle stops and truncation. A separate queue-based visited-set closure computes all reachable candidates for comparison with SPARQL. That closure includes the start entity only if a genuine nonzero cycle returns to it. The validation follows SPARQL property-path semantics (Harris and Seaborne, 2013).

Eligibility checks recorded completions, same-term concurrent plans only where allowsConcurrent is true, standing rank and explicit course permissions. Free-text and unknown conditions remain unverified. A single fully met option satisfies the encoded expression. Already completed status and observed offering status are separate from the prerequisite verdict. A stub with no source catalog text cannot be declared unrestricted. needs_review remains a visible warning even if an encoded option succeeds. These are conservative closed-world application rules, distinct from OWL's open-world schema semantics.

Reverse unlock search finds courses that can reach a proposed completion, evaluates each before and after the hypothetical addition, and identifies those whose encoded eligibility changes. Indirect reachability alone does not make a downstream course immediately available. The original what-if queries omit concurrent-plan credit, so that comparison uses the same policy. Hypothetical completions appear only as assumptions and are never inserted into the RDF evidence.

Degree-progress reasoning follows student → completion → allocated requirement → program, using a reverse traversal of the stored program → requirement edge. It reports allocated counts and credits, unmet encoded thresholds, invalid memberships and technical/advanced-elective double-counting conflicts. It inspects existing allocations rather than optimizing a new assignment. Focus-area alternatives and prose-only policies prevent a per-group numeric summary from constituting a graduation decision.

## Reasoning evaluation protocol and interpretation

The reachable-prerequisite set for every course with a recorded expression is compared with an independently executed SPARQL property-path closure. Exact match is computed on sets, including cycle semantics. The Q01 eligible-course sets are re-instantiated for all synthetic students using the same offering/exclusion/concurrency scope. Q03 condition-level decisions are compared for CS421 and every synthetic student. Every returned edge in the evaluated traces is checked for explicit membership or genuine closure-only inferred membership.

The scripts also exercise an unknown course, a catalog course without recorded prerequisites, an unmet student case, a cycle and a deliberately shallow depth bound. They record runtime and path-depth statistics. Targets are not reported as results: the generated tables supply the observed metrics. Successful graph-edge validation establishes provenance integrity, not the correctness of a source statement, a prerequisite parse or an adviser policy. One local runtime is an execution measurement rather than a statistically robust benchmark.

## Measured reasoning results

The following values come from the committed [reasoning summary](../reasoning/outputs/summary.json), generated at `2026-11-21T12:12:36.077075+00:00` using Python `3.11.7`. They are historical execution measurements, not a claim that the benchmark was rerun on the report-writing date. This section was assembled from that file without editing its values.

| Measurement | Recorded result |
|---|---|
| Courses with recorded prerequisite expressions | 339 |
| Reachability exact matches | 339 / 339 |
| Reachability exact-match rate | 100% |
| Student eligibility-set matches | 4 / 4 |
| Condition-level matches | 12 / 12 |
| Returned evidence edges checked | 206635 |
| Invalid evidence edges | 0 |
| Invalid or disconnected paths | 0 |
| Maximum returned course depth | 12 |
| Mean returned course depth | 5.486440053994355 |
| Truncated course traces | 0 |
| Configured depth limit | 32 |
| Configured path limit | 20000 |
| Recorded runtime in seconds | 12.406906367000374 |

Graph SHA256: `ac0352a0246d3e67fae34d3fd27f3847bb9a3d7897478f19e865478f2a1ea2a8`.

Summary-file SHA256: `32a52b6f8df45126f4376928b24226e6319f0bd3be3923c89dc152bc66497f8e`.

The actual negative-case verdicts were:

- `unknown_course`: `no_path`.
- `no_prerequisites`: `satisfied`.
- `failing_student`: `unmet`.

Reachability agreement covers every expression-bearing course in this snapshot. Eligibility-set agreement covers the four synthetic students under Q01's offering, completion and concurrency scope. The condition-level comparison uses CS421 for those students, not every possible student-course combination. A zero invalid-edge count establishes provenance integrity on the checked paths. It does not establish that the original prerequisite prose was parsed perfectly or that the system can grant registration permission. The runtime is one measured run and should not be generalized to other machines.

## Symbolic inference and viva evidence

The three symbolic examples are stored in [inference_examples.json](../reasoning/outputs/inference_examples.json). The day 7 script checks that each conclusion is absent from the explicit graph and present in OWL RL closure, while its premises are stored facts. The examples demonstrate an inverse department relationship, the student-completion property chain and the offering-term property chain. These schema deductions remain distinct from the Python reasoner's closed-world eligibility verdicts.

[REVIEW_DEMO.md](../REVIEW_DEMO.md) describes the multi-hop SPARQL and ontology walkthrough. The public Python API is documented in [reasoning/README.md](../reasoning/README.md). A path through one prerequisite alternative is possible evidence, not proof that every alternative is compulsory.

## Limitations

The catalog contains missing-course stubs and prerequisites marked needs_review. Free-text, consent and unknown conditions remain unverified unless the graph supplies suitable evidence. A base course in a returned path means no further recorded course prerequisite, not an unrestricted real-world course.

Cycles require guards, and depth/path limits can truncate enumeration. Truncation is labelled in the returned trace. The separate reachable-set validation follows nonzero-cycle SPARQL semantics. Observed graph agreement does not replace an independent audit of the parser or catalog policies.

Hypothetical completions are evaluated in memory and are never recorded as verified transcript facts. Degree progress counts recorded allocations rather than solving an optimal allocation problem. Focus areas are alternatives, and prose-only policies prevent numeric progress from becoming a certified graduation decision. Student records are synthetic. GPA, minimum grades and institutional approval rules remain outside a complete automated audit.

## References

- Lao, N. & Cohen, W. W. (2010). *Relational retrieval using a combination of path-constrained random walks*. Machine Learning 81, 53–67. https://doi.org/10.1007/s10994-010-5205-8
- Xiong, W., Hoang, T. & Wang, W. Y. (2017). *DeepPath: A Reinforcement Learning Method for Knowledge Graph Reasoning*. EMNLP, 564–573. https://doi.org/10.18653/v1/D17-1060
- Das, R. et al. (2018). *Go for a Walk and Arrive at the Answer: Reasoning Over Paths in Knowledge Bases using Reinforcement Learning*. ICLR. https://arxiv.org/abs/1711.05851
- Hogan, A. et al. (2021). *Knowledge Graphs*. ACM Computing Surveys 54(4), Article 71. https://doi.org/10.1145/3447772
- Harris, S. & Seaborne, A. (eds., 2013). *SPARQL 1.1 Query Language*. W3C. https://www.w3.org/TR/sparql11-query/
- W3C (2012). *OWL 2 Web Ontology Language Profiles (Second Edition)*. https://www.w3.org/TR/owl2-profiles/
