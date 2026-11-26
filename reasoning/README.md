# Reasoning — Afaan Sohail

Read `RESEARCH.md`, then `kg.py`, `engine.py`, `evaluate.py` and the tests. Run every command from the repository root.

```bash
python -m reasoning prerequisite_chain --course CS421 --output reasoning/outputs/live_chain.json
python -m reasoning eligibility --student S003 --course CS421 --output reasoning/outputs/live_eligibility.json
python -m reasoning reverse_unlock --student S002 --course CS225 --output reasoning/outputs/live_unlock.json
python -m reasoning degree_progress --student S003 --output reasoning/outputs/live_progress.json
python -m reasoning.evaluate
python -m pytest reasoning/tests -q
```

The default CLI uses concurrent plans; the original Q04/Q13 what-if protocol intentionally does not. Their app retrieval selects `concurrent=False` to reproduce those queries. The CLI can still demonstrate term-aware concurrency through eligibility. No extra prerequisite is assumed to be completed merely because its own prerequisites are met: a recorded completion is the evidence required.

`outputs/reachability.csv` covers every expression-bearing course. `eligibility.csv` compares the four Q01 sets, and `option_conditions.csv` compares the four students' CS421 conditions against Q03. The summary reports measured runtime, depth, truncation and edge validity. These establish agreement with this graph, not the correctness of the original prose parser.

## API for Hassan

```python
from reasoning import KG, Reasoner
reasoner = Reasoner(KG(), max_depth=32, max_paths=20000)
result = reasoner.reason('eligibility', student='S003', course='CS421', term='2026-fa')
```

Templates are `prerequisite_chain(course)`, `eligibility(student, course, term='2026-fa', added=None, concurrent=True)`, `reverse_unlock(student, course, term='2026-fa', concurrent=True)` and `degree_progress(student, program='UIUC-BS-CS-2026')`. Inputs accept compact course codes or resource IRIs. Unknown entities return `no_path`. Unknown template names and invalid limits raise `ValueError`.

Required keys are `answer`, `paths`, `verdict`, `unmet`. Additional fields hold option conditions, assumptions, warnings, runtime and graph SHA256. Every edge has N3-encoded `s`, `p`, `o`, a deterministic `id` and status `explicit` or `inferred`. Parse terms with `rdflib.util.from_n3`; do not strip quotation marks from typed literals. A `direction: reverse` marker means the traversal uses the stored edge in reverse; the RDF triple itself is unchanged. This is how a requirement leads back to its program. `unmet` is grouped by option: a failed alternative need not block a different fully met option. No `predicted` edge is produced; `predictions` is empty.

For chains, `expression_tree` preserves OR options, AND conditions and inner one-of course choices. `branches` links each terminal path to option/condition IDs and reports `root`, `cycle` or `depth_limit`. Root means no further **course** edge; a standing/consent condition may still exist in the expression tree. A stub root is not a verified unrestricted course. `truncated` is explicit if either bound is hit. `reachable()` separately computes the full visited-set closure for comparison, including the source only when an actual cycle returns to it.

Eligibility evaluates direct conditions against the transcript, permission and target-term concurrent plan. It does not recursively demand that already completed courses' prerequisites be re-proven. The verdict refers to encoded prerequisites; `offered_in_term`, `already_completed` and `registration_ready` are separate. Parsing warnings remain visible even if one encoded option passes. Free-text conditions never pass automatically.

Reverse unlock first finds every downstream course that can reach the hypothetical course, then compares before/after direct eligibility. It distinguishes indirect relevance from a course that opens immediately; `dependants[].unmet` explains blockers. No assumption is inserted into the graph. Degree progress checks recorded allocations, both count and credit thresholds, membership in allowed-course lists and the technical/advanced distinct-course conflict. It does not solve a new allocation optimization or certify graduation. Focus-area groups are alternatives, and prose policies need adviser review.

## How to explain this in the viva

Point to an expression's option and condition nodes; explain OR versus AND with the JSON trace. Show why a path through an alternative is only a candidate. Demonstrate a CHEM cycle stopping, an unknown course and a shallow depth limit. Explain the two independent validations: reachability agreement and validity of each returned edge. Show the actual CSV rather than promising a target score. Contrast the unbounded validation closure with bounded path enumeration. Explain why closed-world absence of a completion means unverified and why OWL's open-world semantics alone cannot decide registration.
