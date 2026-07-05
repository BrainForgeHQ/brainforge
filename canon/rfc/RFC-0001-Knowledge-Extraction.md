# RFC-0001 — Knowledge Extraction Specification

Status: Draft

Author: BrainForge

---

# Purpose

Define the rules that every Knowledge Extraction Engine must follow.

The objective is to transform Evidence into trustworthy Knowledge Units.

This RFC is independent of any AI model.

---

# Core Principle

Evidence precedes Intelligence.

No Knowledge Unit may exist without traceable evidence.

---

# Input

One or more Evidence objects.

Each Evidence object contains:

- source
- content
- metadata
- provenance

---

# Output

One or more Knowledge Units.

Each Knowledge Unit must contain:

- id
- title
- statement
- supporting evidence
- confidence
- created_at

---

# Requirements

The extraction engine SHALL:

- preserve factual accuracy
- avoid hallucinations
- avoid summarization that removes meaning
- maintain traceability
- preserve context

The extraction engine SHALL NOT:

- invent facts
- merge unrelated concepts
- create unsupported conclusions

---

# Confidence

Each Knowledge Unit shall include a confidence score between 0.0 and 1.0.

---

# Traceability

Every Knowledge Unit must reference one or more Evidence objects.

No orphan Knowledge Units are allowed.

---

# Versioning

Knowledge Units may evolve over time.

Previous versions shall remain reconstructable.

---

# Future Extensions

This specification intentionally avoids defining:

- embeddings
- vector databases
- LLM providers
- reasoning models

Those belong to future RFCs.