# Final Report — DevAssist

## 1. System Overview

TODO: 1 paragraph — what DevAssist does, who it's for, what problem it solves.

## 2. Architecture

TODO: 1-2 paragraphs — components (RAG pipeline, prompt system, validation layers), data flow, tools used.

```
User Query → Input Sanitization → Embed Query → Retrieve top-k → 
  → Inject into Hardened Prompt → Generate → Output Validation → Response
```

## 3. Prompt Design — Mechanistic Justification

This is the heart of the report. For each design decision, explain the mechanism:

### 3.1 System Prompt Structure (Contract Framework — Module 3)

TODO: Why does the contract framework (objective, constraint, format, evaluation) work? Connect to instruction-following alignment.

### 3.2 Citation Format Constraints (Module 4)

TODO: Why does specifying `[Source N]` format work? Connect to format constraints creating structural token patterns that attention reinforces.

### 3.3 RAG Context Injection (Module 6)

TODO: Why does placing retrieved passages in the context reduce hallucination? Connect to attention over context vs. parametric memory.

### 3.4 Security Boundary Tags (Module 7)

TODO: Why do `<context>` boundary tags help? Why are they insufficient alone? Connect to attention's context-agnostic processing.

### 3.5 Temperature Selection

TODO: Why T=0.2 for factual Q&A? Connect to Module 1 sampling — lower temperature concentrates probability mass on high-probability (more likely correct) tokens.

## 4. Evaluation Summary

TODO: Reference evaluation/evaluation.md. Key metrics:
- Automated test pass rate: TODO/14
- Human evaluation average: TODO/15
- Known limitations: TODO

## 5. Cost & Latency Analysis

TODO: Estimate for 100 queries/day:
- Average tokens per query: TODO
- Average latency: TODO ms
- Technique cost multipliers: TODO (e.g., self-consistency ×n)
- RAG overhead: embedding computation + vector search

## 6. Security & Compliance

TODO: Reference docs/risk_register.md and docs/usage_policy.md.
- Defense layers implemented: input sanitization, hardened prompt, output validation
- NIST AI RMF alignment: Govern (usage policy), Map (risk register), Measure (test suite), Manage (defense layers)

## 7. Lessons Learned

TODO: 1 paragraph — what would you do differently? What surprised you?
