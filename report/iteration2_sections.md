# Iteration 2: knowledge-grounded course planning

## Objective and scope

The course_planning system answers prerequisite, eligibility and degree-allocation questions over the supplied UIUC Fall 2026 snapshot and the curated Grainger BS Computer Science requirements. It extends Iteration 1 through an executable multi-hop reasoning component and a natural-language application whose context comes from that graph at query time. The students are explicitly synthetic test personas, not records of actual UIUC students. The frozen snapshot is the project's evidence base; it does not establish current registration permission or an official graduation audit.

The consolidated report generator adds the original competency questions and mapping, the preserved ontology/URI design, reproduced graph statistics, original queries with re-executed outputs, and the supplied actual Iteration 1 screenshots. It then appends the Iteration 2 method, measured reasoning results, comparison protocol and explainability records. Results are loaded from execution artifacts; missing experimental outputs are printed as PENDING.

## Method: Option C multi-hop KG reasoning

A prerequisite-course hop is a sequence through an expression, an option, a condition and a referenced course. The reasoner follows these stored edges and records every intermediate entity. It retains a nested expression tree so that different options remain alternatives, conditions within an option remain conjunctions, and a CourseChoiceCondition requires only one of its candidates. Therefore a course appearing on a possible path is not automatically a compulsory prerequisite.

Path-based reasoning has a substantial research history. Lao and Cohen (2010) learn relational retrieval from edge-label sequences; DeepPath learns relational navigation policies (Xiong et al., 2017), and MINERVA conditions navigation on a query (Das et al., 2018). These sources motivated preserving typed paths and examining intermediate decisions. Our implementation is a deterministic symbolic traversal suitable for the supplied graph; it does not implement their trained policies, embeddings or link-prediction objectives. Hogan et al. (2021) informed the distinction between querying, deduction and induction. Option C here produces verified traversals and rule conclusions, with no predicted links.

Prerequisite-chain search uses a path-local ancestry set to stop cycles while allowing the same course to appear on different valid branches. A course-hop depth bound and terminal-path bound control enumeration; the trace explicitly marks cycle stops and truncation. A separate queue-based visited-set closure computes all reachable candidates for comparison with SPARQL. That closure includes the start entity only if a genuine nonzero cycle returns to it. The validation follows SPARQL property-path semantics (Harris and Seaborne, 2013).

Eligibility checks recorded completions, same-term concurrent plans only where allowsConcurrent is true, standing rank and explicit course permissions. Free-text and unknown conditions remain unverified. A single fully met option satisfies the encoded expression. Already completed status and observed offering status are separate from the prerequisite verdict. A stub with no source catalog text cannot be declared unrestricted. needs_review remains a visible warning even if an encoded option succeeds. These are conservative closed-world application rules, distinct from OWL's open-world schema semantics.

Reverse unlock search finds courses that can reach a proposed completion, evaluates each before and after the hypothetical addition, and identifies those whose encoded eligibility changes. Indirect reachability alone does not make a downstream course immediately available. The original what-if queries omit concurrent-plan credit, so that comparison uses the same policy. Hypothetical completions appear only as assumptions and are never inserted into the RDF evidence.

Degree-progress reasoning follows student → completion → allocated requirement → program, using a reverse traversal of the stored program → requirement edge. It reports allocated counts and credits, unmet encoded thresholds, invalid memberships and technical/advanced-elective double-counting conflicts. It inspects existing allocations rather than optimizing a new assignment. Focus-area alternatives and prose-only policies prevent a per-group numeric summary from constituting a graduation decision.

## Architecture and KG-grounded generation

The pipeline is question → entity/intent linking → parameterized SPARQL and Python reasoning → context construction → the configured LLM → generated answer and inspectable graph evidence. It runs locally from the supplied Turtle graph; GraphDB remains available for the required live ontology/inference walkthrough and optional endpoint checks. The app does not require a live GraphDB server to retrieve its graph evidence.

Entity linking recognizes course codes, synthetic student IDs and terms. Intent rules select generic query families without consulting the evaluation question file or stored answers. Unknown, ambiguous or unsupported requests receive an insufficient-evidence response. Valid unseen combinations of known entities run against the graph. The scope of natural-language coverage is the implemented templates; arbitrary questions and multi-turn reference resolution remain limitations.

The application uses KG-RAG with SPARQL-generated context, informed by external-memory grounding in Lewis et al. (2020). It preserves relationships as in graph-oriented retrieval, but does not implement the community-index construction or global summarization procedure in Edge et al. (2024). Retrieved records, original query text, reasoning traces, graph hash and evidence edge IDs remain inspectable. OWL-inferred triples are labelled separately by testing membership in the explicit graph and its computed closure.

The grounding prompt restricts the model to the supplied context and asks it to cite edge or result-row IDs, preserve alternative branches and state missing evidence. The LLM remains capable of unsupported prose: prompts and citation-ID checks do not establish semantic correctness. Invalid citations are retained for scoring. Every query row is included or the system abstains if the result table alone exceeds its context budget. Additional evidence and traces may be omitted from the prompt with explicit omitted counts; the full output artifact keeps them. Character budgets approximate model tokens, and length-truncated answers are flagged.

The selected free local configuration uses Qwen3 4B Instruct through Ollama's compatible chat API (Qwen Team; Ollama documentation). Both A and B use the same locally created model, temperature and output budget. The harness records and checks the actual Ollama model digest and runtime version across runs; actual settings and prompt hashes are retained with the experiment. Local inference has no paid API calls, but requires suitable RAM, downloaded model weights and execution time. The selected experiment now contains actual model outputs; suitability remains limited by the recorded errors.

## Reasoning evaluation protocol and interpretation

The reachable-prerequisite set for every course with a recorded expression is compared with an independently executed SPARQL property-path closure. Exact match is computed on sets, including cycle semantics. The Q01 eligible-course sets are re-instantiated for all synthetic students using the same offering/exclusion/concurrency scope. Q03 condition-level decisions are compared for CS421 and every synthetic student. Every returned edge in the evaluated traces is checked for explicit membership or genuine closure-only inferred membership.

The scripts also exercise an unknown course, a catalog course without recorded prerequisites, an unmet student case, a cycle and a deliberately shallow depth bound. They record runtime and path-depth statistics. Targets are not reported as results: the generated tables supply the observed metrics. Successful graph-edge validation establishes provenance integrity, not the correctness of a source statement, a prerequisite parse or an adviser policy. One local runtime is an execution measurement rather than a statistically robust benchmark.

## LLM-only versus KG-grounded experiment

Ten original competency questions are retained verbatim with explicit test instances supplied equally to both modes. The selection covers prerequisite chains, condition evaluation, downstream and hypothetical effects, degree allocations, a two-hop query, cross-listings, an OWL-dependent aggregate and recommendation evidence. Expected answers are re-executed against the frozen graph. The baseline receives neither the graph nor synthetic transcripts, expected outputs or retrieval tools. The grounded mode uses the real router and query-time retrieval, never a case-specific answer lookup.

Both conditions use the same LLM, temperature and maximum output tokens with fresh stateless calls. Their prompts differ to express grounding, so this compares complete systems rather than isolating retrieval as the sole causal variable. Paired runs can alternate order; the daily work plan also permits separately recorded A and B runs under the same immutable manifest. Changes in model, prompts, questions or graph require a new run ID. Provider failures remain errors, and missing calls or reviews block final scoring.

A human reviewer compares each response against the complete expected rows, checks requested-set completeness and substantive conclusions, counts atomic unsupported factual claims, and verifies relevant provenance. A refusal can avoid hallucination while failing to answer an answerable CQ. A second member reviews disagreements. Grades are tied to raw-file hashes. Only after review does the scorer generate the required comparison table, correctness totals out of ten, unsupported-claim totals and evidence counts. No automatic word-match score or fabricated placeholder is treated as a measured result.

## Comparative findings

The selected run is qwen3_trial3_kaggle. All twenty model calls completed without flagged truncation. The recorded grading entries give 0/10 for the baseline and 6/10 for the grounded application. CQ01, CQ03, CQ04, CQ08, CQ11 and CQ15 pass the strict completeness and correctness rule. CQ02 omits three prerequisite edges, CQ06 omits three completed requirement groups, CQ10 omits CS 581, and CQ13 adds an unsupported blanket statement about other prerequisites. The baseline mainly refuses because it lacks the frozen catalog and synthetic transcripts. This can avoid hallucination while failing to answer an answerable question. Grading explanations and unsupported-claim counts are retained per response. Reviewer assignments were supplied by the team, with ten entries each for Hassan Tariq and Diya Hurmat.

Trial 3 was revised after inspecting earlier failures. Runtime context includes query-field explanations, exact row counts and recorded student completion codes, while retaining all query rows and full evidence in the artifacts. The model, settings and expected-question snapshot are unchanged from trial 2. This is a development rerun rather than a held-out evaluation. The ten selected questions and synthetic transcripts limit generalization to real advising. The report reads every numeric total from generated execution or scoring artifacts.

## Explainability examples

The report builder includes three real retrieved-context records for eligibility, multi-hop prerequisites and the inference-dependent elective aggregate. Their generated-text fields now contain the supplied actual grounded CQ03, CQ08 and CQ11 responses, including any errors; the prose is not silently corrected. At final assembly it selects the corresponding live B records and prints the question, actual generated text, query rows, representative graph edges and rule traces. The complete paths remain in the machine-readable artifacts.

Explicit knowledge means an RDF triple directly in the submitted Turtle. Inferred knowledge means a triple absent there and present after OWL RL closure; separately saved symbolic examples include the actual stored premises and schema axiom. Eligibility verdicts and aggregate counts are computed application/query conclusions. Generated text means the actual LLM response. There is no Prediction in Option C; hypothetical completions are assumptions. An unrecorded completion is a closed-world absence check, not a stored negative fact.

## Limitations and integrity

The graph is a scoped historical catalog snapshot with missing-course stubs, ambiguous prerequisite prose and synthetic transcripts. Cross-listings do not establish interchangeability; no owl:sameAs substitution is introduced. The parser keeps difficult clauses for review, and numeric eligibility covers only encoded conditions. GPA, minimum grades, topic-specific approvals, credit caps and other prose policies require human interpretation. Degree allocation is not automatically optimized, and focus areas are alternatives rather than simultaneous graduation obligations.

The local OWL closure count may differ from a historical runtime; the report records the installed dependency versions and measured total. Query comparison normalizes URI display, unbound values and unspecified GROUP_CONCAT order, while preserving the raw outputs for inspection. SHACL validates the supplied structural shapes; conformity does not prove every degree policy, including the separately seeded double-count conflict. GraphDB and Protégé screenshots supplied with Iteration 1 are identified as archived images, not new Iteration 2 executions.

Grounded prose can omit rows, misuse a valid citation or add an unsupported inference. Routing is template-based, context is bounded, and output limits can truncate lists. A context budget is a character approximation, not an exact tokenizer guarantee. A failure to retrieve is reported as insufficient evidence instead of a real-world absence claim. Manual semantic scoring and the live unseen-question demonstration remain necessary.

ChatGPT was used to assist with code, documentation and prompts, and to cite external code, datasets, ontologies, prompts, libraries, tutorials and other resources. The team must review, modify, reproduce and explain the work. The contribution schedule is prospective: no commits were created, backdated or attributed to team members by this scaffold. The final contribution table must cite actual individual commits and the externally hosted demo. Repository creation, instructor access, clean-machine execution and recording are not claimed without evidence.

## References and resource attribution

Lao, N. and Cohen, W. W. (2010). Relational retrieval using a combination of path-constrained random walks. Machine Learning 81, 53–67. https://doi.org/10.1007/s10994-010-5205-8

Xiong, W., Hoang, T. and Wang, W. Y. (2017). DeepPath: A Reinforcement Learning Method for Knowledge Graph Reasoning. EMNLP, 564–573. https://doi.org/10.18653/v1/D17-1060

Das, R. et al. (2018). Go for a Walk and Arrive at the Answer: Reasoning Over Paths in Knowledge Bases using Reinforcement Learning. ICLR. https://arxiv.org/abs/1711.05851

Hogan, A. et al. (2021). Knowledge Graphs. ACM Computing Surveys 54(4), Article 71. https://doi.org/10.1145/3447772

Lewis, P. et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. NeurIPS. https://arxiv.org/abs/2005.11401

Edge, D. et al. (2024; revised 2025). From Local to Global: A Graph RAG Approach to Query-Focused Summarization. https://arxiv.org/abs/2404.16130

Harris, S. and Seaborne, A., eds. (2013). SPARQL 1.1 Query Language. W3C. https://www.w3.org/TR/sparql11-query/

W3C (2012). OWL 2 Web Ontology Language Profiles (Second Edition). https://www.w3.org/TR/owl2-profiles/

UIUC course-catalog dataset. https://discovery.cs.illinois.edu/dataset/course-catalog/ (supplied Fall 2026 CSV; source evidence, not a newly downloaded catalog).

Illinois prerequisites dataset. https://github.com/illinois/prerequisites-dataset (supplied QA-only CSV).

UIUC Grainger BS Computer Science catalog. https://catalog.illinois.edu/undergraduate/engineering/computer-science-bs/ (Iteration 1 curated requirement provenance; current web page is not substituted for the supplied snapshot).

Qwen Team. Qwen3 official repository and model releases. https://github.com/QwenLM/Qwen3

Ollama. OpenAI-compatible API and selected model entry. https://docs.ollama.com/api/openai-compatibility ; https://ollama.com/library/qwen3:4b-instruct

RDFLib and OWL-RL libraries. https://github.com/RDFLib/rdflib ; https://github.com/RDFLib/OWL-RL

pySHACL. https://github.com/RDFLib/pySHACL ; pandas. https://pandas.pydata.org/docs/ ; Requests. https://requests.readthedocs.io/ ; pytest. https://docs.pytest.org/ ; python-docx. https://python-docx.readthedocs.io/ ; ReportLab. https://www.reportlab.com/docs/reportlab-userguide.pdf

Ontotext GraphDB documentation. https://graphdb.ontotext.com/documentation/10.7/ ; Protégé. https://protege.stanford.edu/

Project code/prompt provenance: supplied Iteration 1 archive, this repository's `iteration1/Code`, `reasoning`, `app`, `evaluation`, and `prompts`; ChatGPT use is disclosed above. Exact package versions are recorded in the environment artifact. Research titles and links were checked against primary publication/release pages on 21 November 2026.

## Selected Kaggle experiment findings

The selected manifest records Linux, Python 3.12.15, Ollama 0.40.18 and Qwen3 4B Q4_K_M. Runtime evidence reports full GPU loading. The artifact audit checks all twenty actual responses, source and prompt hashes, request settings and graph evidence. Its recorded results are included alongside the scored comparison. It establishes artifact consistency and graph membership, not infallible prose.

Trial 1 and trial 2 remain historical runs. Their truncation and semantic problems are not silently replaced. Trial 3 has no flagged output truncation and no unknown citation IDs, but still has omissions and one unsupported grounded claim under the recorded rubric. No result was manually repaired. The manifest's missing Git commit is preserved because Kaggle ran outside a checkout; the final implementation commit must be recorded separately.
