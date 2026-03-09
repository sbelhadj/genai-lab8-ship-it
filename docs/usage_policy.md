# Usage Policy — DevAssist

## Intended Use

DevAssist is a documentation assistant for the TaskFlow project. It answers questions about TaskFlow's architecture, API, installation, configuration, and changelog using a RAG pipeline grounded in the project's official documentation.

## In-Scope Uses

- Answering questions about TaskFlow features, API endpoints, and configuration
- Explaining installation and setup procedures
- Clarifying error messages and troubleshooting steps
- Summarizing changelog entries and version differences

## Out-of-Scope Uses

- Providing legal, medical, financial, or safety-critical advice
- Answering questions unrelated to TaskFlow documentation
- Generating or executing code in production environments
- Replacing human review for security-sensitive decisions
- Processing or storing personally identifiable information (PII)

## Known Limitations

1. **Hallucination risk:** Despite RAG grounding, the model may occasionally generate claims not supported by the retrieved context. Always verify critical information against the source documentation.
2. **Knowledge boundary:** DevAssist only knows what is in its indexed corpus. Questions about topics not covered by the documentation will receive an "I don't have this information" response.
3. **Non-deterministic outputs:** The same question may produce slightly different responses across runs due to the probabilistic nature of text generation.
4. **Security:** While defense-in-depth layers are implemented, no AI system is immune to adversarial attacks. Do not rely on DevAssist for security-sensitive decisions.

## User Responsibilities

- Verify critical information against official documentation
- Report unexpected, incorrect, or harmful outputs to the development team
- Do not attempt to manipulate the system through prompt injection
- Do not input sensitive, confidential, or personal information

## Escalation

If DevAssist produces incorrect or harmful output, contact: TODO (project maintainer email)
