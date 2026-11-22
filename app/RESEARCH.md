# Research notes: Hassan's scope

Lewis et al. (2020) combine learned model knowledge with retrieved external memory. Their RAG model uses document retrieval and training; this project borrows query-time grounding, not their training procedure or dense index. Our external memory is the existing RDF graph, and deterministic SPARQL/templates retrieve structured rows and paths.

Edge et al. (2024; revised 2025) describe GraphRAG with an entity graph and community summaries for corpus-wide questions. That informed the decision to preserve graph relationships, but our implementation does not build communities or reproduce Microsoft's GraphRAG. It is accurately described as **KG-RAG using SPARQL-generated context and symbolic traces**. Course-specific questions need exact option and transcript evidence rather than global corpus summaries.

Qwen's official release repository documents open model weights under Apache 2.0. Ollama's official documentation describes a compatible `/v1/chat/completions` interface. We select `qwen3:4b-instruct`, a local model without per-call API billing, and fix the same model and generation settings for both experimental conditions. Local hardware, memory and inference time remain practical constraints; no accuracy result follows from model selection.

References:

- Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS. https://arxiv.org/abs/2005.11401
- Edge, D. et al. (2024). *From Local to Global: A Graph RAG Approach to Query-Focused Summarization*. https://arxiv.org/abs/2404.16130
- Qwen Team. Qwen3 official code and releases. https://github.com/QwenLM/Qwen3
- Ollama. OpenAI compatibility. https://docs.ollama.com/api/openai-compatibility
- Ollama. Model library entry. https://ollama.com/library/qwen3:4b-instruct
