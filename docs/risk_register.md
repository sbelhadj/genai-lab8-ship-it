# Risk Register — DevAssist

## NIST AI RMF Aligned

---

| # | Risk | Category | Likelihood | Impact | Mitigation | Regression Test | Status |
|---|------|----------|-----------|--------|------------|----------------|--------|
| 1 | Indirect prompt injection via poisoned docs | Security | Medium | Critical | Hardened prompt with `<context>` boundary tags; output validation | sec_01, sec_02 | Mitigated |
| 2 | System prompt exfiltration | Security | Medium | High | Anti-revelation rules in v1.1; output validator catches leaks | sec_02, sec_03 | Mitigated |
| 3 | Hallucinated citations | Reliability | High | Medium | Citation format check in test suite; output validation | fmt_01, fmt_02 | Monitored |
| 4 | Parametric memory override (model ignores context) | Reliability | Low | High | Strong "ONLY use context" instruction; low temperature | acc_01–acc_04 | Mitigated |
| 5 | Gender/demographic bias in outputs | Ethics | Medium | Medium | TODO: bias-aware prompt guidelines; matched-pair testing | TODO | Open |
| 6 | Out-of-scope queries answered with hallucination | Reliability | Medium | Medium | Out-of-scope refusal instruction; similarity threshold | edge_01, edge_03 | TODO |
| 7 | PII leakage in generated responses | Privacy | Low | Critical | Output validator PII regex check | TODO | Mitigated |
| 8 | Retrieval returns irrelevant chunks | Quality | Medium | Medium | TODO: similarity threshold filter | TODO | Open |
| 9 | Model generates harmful/unsafe content | Safety | Low | Critical | Output validation; hardened prompt rules | TODO | Mitigated |
| 10 | Corpus staleness (outdated docs indexed) | Operational | Medium | Medium | TODO: metadata dating; re-index schedule | TODO | Open |

---

## Summary

- **Mitigated:** 5 risks with active defenses
- **Monitored:** 1 risk with automated detection
- **Open:** 4 risks requiring future work
