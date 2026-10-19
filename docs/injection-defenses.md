# Prompt-Injection Defenses: aspire-mcp

> **Owner: @arshi016.** Template only.

Reference: OWASP Top 10 for LLM Applications (prompt injection, excessive agency).

## Principles (from requirements)
- Document and email contents are untrusted data, never instructions.
- Validate all tool inputs.
- Require human confirmation before any action triggered by document content.
- Read-only by default; writes gated behind human approval.

## Layers
### Input validation
- Per-tool schemas, length caps, character filtering. What else?

### Output handling
- Structured/schema-validated results only? Redaction? Leak gate? Block records?

### Action gating
- Which actions need confirmation, by whom, and how is it recorded?

### Context separation
- How is untrusted content marked/isolated from instructions?

### Detection and logging
- What signals indicate an injection attempt? How are they logged and alerted?

## Test cases
- TODO: list of injection payloads and expected behavior (synthetic data only)

## Open questions
- TODO
