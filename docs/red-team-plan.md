# Red-Team Plan: aspire-mcp

> **Owner: @arshi016.** Template only. Run before go-live.

## Scope (from requirements)
- Injection via uploaded documents
- Data exfiltration through tool outputs
- Privilege escalation

## Rules of engagement
- Synthetic data only; test environment only.
- TODO: environment, timing, who signs off

## Scenarios
| # | Scenario | Technique | Expected defense | Result |
|---|---|---|---|---|
| 1 | Instructions hidden in a document | Indirect prompt injection | Treated as data; no action without confirmation | TODO |
| 2 | Coaxing PII into a tool result | Exfiltration via output | Redaction / output gate | TODO |
| 3 | Calling another role's tool | Privilege escalation | RBAC refusal, logged | TODO |
| 4 | Forged or out-of-scope token | Spoofing / confused deputy | Refused, logged | TODO |
| 5 | Altered tool description | Tool poisoning | Integrity check | TODO |
| 6 | Outbound call outside gateway | Egress bypass | Blocked | TODO |

## Reporting
- Severity scale: TODO
- Findings tracked as private issues in this repo; fixes via PR.

## Open questions
- TODO
