# Lab 8 — Teacher Solution & Answer Key

## Ship It — Instructor Copy

**CONFIDENTIAL**

---

## 1. Expected Test Suite Results (Llama 3.2 3B, prompt v1.1)

| Category | Expected Pass Rate | Notes |
|----------|--------------------|-------|
| Format compliance (4) | 4/4 | Citations consistently present with v1.1 |
| Factual accuracy (4) | 3-4/4 | Occasional parametric override on familiar topics |
| Security regression (3) | 2-3/3 | v1.1 blocks most attacks; translation trick may partially succeed |
| Edge cases (3) | 2-3/3 | Out-of-scope refusal reliable; empty query handling varies |
| **Overall** | **11-14/14** | ~80-100% |

## 2. Human Evaluation Expected Scores

| Dimension | Expected Range (/3) |
|-----------|-------------------|
| Factual Accuracy | 2.4-3.0 |
| Groundedness | 2.2-2.8 |
| Citation Quality | 2.0-2.6 |
| Helpfulness | 2.4-3.0 |
| Conciseness | 2.2-2.8 |

Citation quality typically scores lowest — model sometimes hallucinates [Source N] numbers.

## 3. Grading Priorities

1. **Final report §3 (Mechanistic Justification)** — this is the core assessment. Students must link EVERY design choice to a Module 1-7 mechanism. Vague references ("attention helps") are inadequate; precise reasoning ("boundary tags provide structural tokens that attention uses to separate data from instructions, reducing the probability that injected text is processed as an instruction") demonstrates mastery.

2. **Evaluation suite completeness** — 14 test cases across 4 categories is the minimum. Students who add their own tests show initiative. Human evaluation scoring sheet must be filled.

3. **Risk register substance** — generic entries ("model might hallucinate → tell users to verify") are insufficient. Good entries are specific with regression tests.

4. **Demo quality** — can the student explain WHY each design choice was made?

## 4. Common Issues

- Students who didn't complete Lab 7 will struggle with security deliverables → allow them to focus on evaluation
- Presentation nerves → emphasize that Q&A tests understanding, not performance
- Portfolio reflection rushed → this is 20% of final grade, encourage substantive reflection

---

*CONFIDENTIAL — Lab 8 Teacher Solution*
