# Application — Hassan Tariq

The root README contains setup. Start with `linking.py` (entities and intents), `retrieval.py` (actual query execution and evidence), `service.py` (context and public API), and `llm.py` (provider transport).

```bash
python -m app 'Can S003 take CS 421 in Fall 2026?' --retrieve-only --output app/retrieval.json
python -m app 'Can S003 take CS 421 in Fall 2026?' --config config/local.json --output app/answer.json
python -m app 'What is the weather for CS 421?' --output app/insufficient.json
python -m app --config config/local.json
python -m pytest app/tests -q
```

`Advisor(Config.load('config/local.json')).answer(question)` returns `{answer, evidence, mode}` with full retrieval, trace, prompt, raw provider completion, citations and settings. Baseline mode never sends retrieval. `retrieve_only=True` produces `mode=retrieval_only`, never a fake LLM answer. Unsupported intents, unknown entities/terms, stubs, ambiguous entities or an oversized result table produce `mode=insufficient_evidence`; no LLM is called. Transport errors are errors, never fallback results.

The CLI prints the unabridged JSON: generated answer, graph triples with IDs, SPARQL, rows, rule trace and provenance. Save it with `--output` to inspect with an editor. The generic template router supports the selected CQs and paraphrases; it does not route on CQ IDs or read `evaluation/cqs.json`. Personal questions must identify the student. General offering/department questions must specify a term. Without a term, eligibility uses the sole Fall 2026 snapshot, which is explicitly recorded in the query/trace. Follow-ups are stateless, so repeat entities.

Context keeps every result row or abstains if those rows alone exceed the configured budget. It adds concise traces and as many graph facts as fit, with omitted counts. All untrimmed evidence remains in the output artifact. Character limits approximate tokens: confirm the request fits the selected model; provider context errors are saved as errors. The default Ollama Modelfile sets a larger context than an unconfigured local server. `completion.truncated` flags output-length limits. Do not silently score a truncated set as complete.

Citation validation only checks IDs, not whether an edge logically supports a sentence. Invalid or missing citations are retained for review and scoring; the program does not falsely certify the LLM prose as correct. Query row IDs support aggregates; graph edge IDs support explicit/inferred facts. Prompts instruct the model to preserve the distinction and abstain when needed. Retrieved catalog prose is treated as data, not instructions.

## How to explain this in the viva

Type a new code/student question and show the linked entities, selected query, actual context, LLM output and its cited IDs. Explain why changing the transcript or graph changes retrieval, while there is no cached demo answer. Show an unsupported term and explain why it abstains before calling the model. Explain that prompt restrictions reduce risk but do not prove semantic faithfulness; humans still review unsupported claims. Show that the same client and settings serve both A and B.

The evaluation harness also records Ollama runtime/model identity through the local metadata API and refuses to resume the same run with a changed model digest or runtime version. Direct CLI answers retain actual provider metadata in their completion artifacts.
