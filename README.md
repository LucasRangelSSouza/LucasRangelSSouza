# Lucas Rangel

**Senior Data & AI Platform Engineer**

I build data platforms and AI systems that teams can inspect, reproduce, and operate. My public work centres on Brazilian public data: releases with manifests and clean-download checks, MLOps with drift gates, retrieval that cites its sources and abstains when it cannot, and runtimes that survive worker failure. More than twelve years across software, data engineering, machine learning, and cloud delivery.

[Portfolio](https://rangeltech.net) · [Live RAG chat](https://rag.rangeltech.net) · [Dashboards](https://rangeltech.net/dashboards/pncp/) · [Kaggle catalogue](https://www.kaggle.com/lucasrangelss/datasets) · [LinkedIn](https://www.linkedin.com/in/lucas-rangel-s-souza/) · [lucas.rangel@outlook.com](mailto:lucas.rangel@outlook.com)

## Skills map

| Area | What I do | Where to see it |
|---|---|---|
| Data platforms | Source registries, layered releases (raw, trusted, semantic), data contracts, cost assessment | [brazil-public-data-map](https://github.com/LucasRangelSSouza/brazil-public-data-map), [cloud-data-finops-sdd-toolkit](https://github.com/LucasRangelSSouza/cloud-data-finops-sdd-toolkit) |
| MLOps | Pinned data, lineage, drift gates, review-signal models | [education-finance-mlops](https://github.com/LucasRangelSSouza/education-finance-mlops), [pncp-opportunity-recommender](https://github.com/LucasRangelSSouza/pncp-opportunity-recommender) |
| RAG and LLM systems | Cited retrieval, guardrails, abstention, redacted traces, model serving | [rag-chat](https://github.com/LucasRangelSSouza/rag-chat), [ai-platform-rag-observability](https://github.com/LucasRangelSSouza/ai-platform-rag-observability) |
| Cloud-native orchestration | Redis-coordinated workers, Kubernetes, Terraform, recovery tests | [distributed-agent-runtime-lab](https://github.com/LucasRangelSSouza/distributed-agent-runtime-lab) |

## Pinned work

1. [lucas-rangel-portfolio](https://github.com/LucasRangelSSouza/lucas-rangel-portfolio): static portfolio with evidence-labelled cases, accessibility and link checks.
2. [brazil-public-data-map](https://github.com/LucasRangelSSouza/brazil-public-data-map): public-source registry, privacy and release gates, and Kaggle catalogue tooling.
3. [rag-chat](https://github.com/LucasRangelSSouza/rag-chat): a bounded research chat that loads one versioned corpus per deployment. First profile: PNCP procurement data.
4. [ai-platform-rag-observability](https://github.com/LucasRangelSSouza/ai-platform-rag-observability): the RAG kernel with citation checks, language-matched refusals, and redacted traces.
5. [distributed-agent-runtime-lab](https://github.com/LucasRangelSSouza/distributed-agent-runtime-lab): idempotent worker runtime with a public-demo Compose profile.
6. [qwen-abliterated-api](https://github.com/LucasRangelSSouza/qwen-abliterated-api): self-hosted OpenAI-compatible endpoint for a 27B open model (vLLM, NVFP4, speculative decoding) that powers the live chat. The checkpoint is third-party; the serving is mine.

## Live demos

- [RAG chat](https://rag.rangeltech.net): cited answers over PNCP procurement notices (text plus vector retrieval) and SIOPE education spending (read-only SQL agent). Pick which bases to search, or none.
- [PNCP explorer and dashboard](https://rangeltech.net/dashboards/pncp/): text search, semantic search, and a Metabase dashboard on one Postgres.
- [SIOPE dashboard](https://rangeltech.net/dashboards/siope/): the pure-SQL case.

## Proof map

Each row links a project to an artefact you can run, the check that supports it, and its stated limit.

| Project | Artefact | Validation | Limit |
|---|---|---|---|
| brazil-public-data-map | Kaggle datasets with SHA-256 manifests | Clean download verified against the manifest | Public availability does not settle redistribution terms; each release records its own |
| education-finance-mlops | Anomaly-triage pipeline on a pinned release | A drift gate blocked a shifted batch | Review signals only; no labels, so no accuracy claim |
| pncp-opportunity-recommender | Explained ranking of historical notices | Offline evaluation with hash-verified data | Synthetic profiles measure constraint adherence, not user relevance |
| ai-platform-rag-observability | RAG kernel with cited answers | 124 unit tests, including English and Portuguese cases | Gateway and Langfuse clients were tested against fake servers |
| distributed-agent-runtime-lab | Worker runtime, manifests, Terraform | Local benchmark and worker recovery on a local `kind` cluster | Deterministic stub model; no cloud validation |
| rag-chat | Interface, backend, citation validator | Backend unit tests for language, abstention, and refusal | Lexical retrieval; live evidence is recorded per deployment |

Repositories document their own verification records. None of them claims a production deployment.

## Published datasets

- [Kaggle catalogue](https://www.kaggle.com/lucasrangelss/datasets): PNCP procurement data as subject datasets (raw and trusted Parquet together, semantic separate) plus per-table educational releases, each with a manifest.
- [Brazil Education Data Lake: SIOPE 2019-2023](https://www.kaggle.com/datasets/lucasrangelss/brazil-education-data-lake): 27,830 municipality-year education-finance declarations with IBGE codes.
- [Brazil PNCP Procurement History: January 2025](https://www.kaggle.com/datasets/lucasrangelss/brazil-pncp-procurement-history): an earlier, bounded sample of procurement notices. It is not the demonstration corpus.

## Contact

[lucas.rangel@outlook.com](mailto:lucas.rangel@outlook.com) · [LinkedIn](https://www.linkedin.com/in/lucas-rangel-s-souza/) · [GitHub](https://github.com/LucasRangelSSouza)
