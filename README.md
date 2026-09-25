# Lucas Rangel

Senior Data & AI Platform Engineer.

I build reproducible data and AI systems with explicit operating boundaries: source lineage, release controls, testable MLOps, observable retrieval, and infrastructure that can be run locally before it moves to cloud infrastructure.

## Current public references

- [Cloud data FinOps SDD toolkit](https://github.com/LucasRangelSSouza/cloud-data-finops-sdd-toolkit): a 9-rule GCP/AWS cost-signal engine, a deterministic in-repo deck generator, and a release gate that checks every artifact against a versioned checksum manifest.
- [Brazil public data map](https://github.com/LucasRangelSSouza/brazil-public-data-map): public-source registry, privacy gates, layered releases, and checkpointed PNCP/SIOPE extraction behind two published Kaggle datasets.
- [Education finance MLOps](https://github.com/LucasRangelSSouza/education-finance-mlops): anomaly triage on the published SIOPE release, with hash-pinned data, lineage, and a drift gate that blocked a shifted batch.
- [PNCP opportunity recommender](https://github.com/LucasRangelSSouza/pncp-opportunity-recommender): transparent ranking of historical procurement notices from the published PNCP release, with explained scores and offline evaluation.
- [AI platform RAG observability](https://github.com/LucasRangelSSouza/ai-platform-rag-observability): an OpenAI-compatible gateway client, Langfuse-shaped redacted traces, and a cited education corpus built from the published SIOPE release.
- [Distributed agent runtime lab](https://github.com/LucasRangelSSouza/distributed-agent-runtime-lab): idempotent worker runtime, Redis deployment contract, Kubernetes manifests, Terraform validation, and an opt-in public-demo Compose profile validated locally (egress-isolated, only nginx published).

Each repository documents its own verification evidence and known limits. Public data releases are published only after source, privacy, and release-contract review.

The [personal portfolio website](https://github.com/LucasRangelSSouza/lucas-rangel-portfolio) links all six cases with their verified states; no public domain is live yet, so this profile links the source repository.

## Published datasets

- [Brazil Education Data Lake: SIOPE 2019-2023](https://www.kaggle.com/datasets/lucasrangelss/brazil-education-data-lake): 27,830 municipality-year education-finance declarations with IBGE codes.
- [Brazil PNCP Procurement History: January 2025](https://www.kaggle.com/datasets/lucasrangelss/brazil-pncp-procurement-history): a bounded, field-minimized week of public procurement notices.

Both were rebuilt twice with identical manifests and checked by a clean download against their SHA-256 manifests.

## Verified baseline

Every flagship case has a tagged release from a passing public CI baseline (v0.1.0, then v0.2.0 for the data-consuming and demo-facing cases on 2026-09-25). Each release's notes preserve its case-specific boundary: synthetic FinOps telemetry, reviewed data distribution, human review of model or ranking output, grounded retrieval behavior, and local-first distributed-runtime evidence. None claims a cloud deployment or a production system.

## Focus areas

Data platforms, analytical engineering, MLOps, GenAI evaluation, cloud architecture, Kubernetes, Terraform, CI/CD, and FinOps.

## Contact

Email: [lucas.rangel@outlook.com](mailto:lucas.rangel@outlook.com) · [LinkedIn](https://www.linkedin.com/in/lucas-rangel-s-souza/) · [GitHub](https://github.com/LucasRangelSSouza)
