# Evaluation Strategy — DevAssist

## 1. Evaluation Approach

DevAssist is evaluated using a combination of automated tests and human evaluation rubrics. Automated tests verify structural and factual properties; the rubric assesses quality dimensions that require human judgment.

**Why both are necessary:** Automated tests catch format violations and factual errors programmatically, but cannot assess helpfulness, explanation quality, or whether the retrieved context was well-utilized. Human evaluation fills this gap.

## 2. Automated Test Suite

### 2.1 Format Compliance Tests (4 tests)
TODO: List your format tests + results

### 2.2 Factual Accuracy Tests (4 tests with ground truth)
TODO: List your accuracy tests + results

### 2.3 Security Regression Tests (3 tests from Lab 7)
TODO: List your security regression tests + results

### 2.4 Edge Case Tests (3 tests)
TODO: List edge case tests + results

### Total: 14 automated tests
### Pass rate: TODO/14 (TODO%)

## 3. Human Evaluation

### 3.1 Rubric
See `rubric.md` for the 5-dimension rubric.

### 3.2 Results
TODO: Average scores across 5 queries (from rubric.md scoring sheet)

## 4. Known Limitations

TODO: List 3-5 known limitations with severity and planned mitigations. Example:
1. **Low-similarity retrieval returns noise** (Medium) — when no relevant chunk exists, top-k still returns something. Mitigation: add a similarity threshold.
2. TODO
3. TODO

## 5. Evaluation Limitations

TODO: What does this evaluation NOT cover? (e.g., long-term drift, multi-turn conversations, concurrent users, etc.)
