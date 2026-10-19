# Threat Model (STRIDE): aspire-mcp

> **Owner: @arshi016.** Template only. Fill in, challenge and extend.

## 1. System overview
- TODO: diagram (agent host, MCP server, tools, client systems, vault, audit store, egress gateway)
- TODO: trust boundaries (model <-> agent runtime <-> MCP server <-> client systems)
- Assets: personal data, documents, email, credentials, audit log integrity, tool allowlist/config

## 2. Assumptions
- Everything runs on-prem; no cloud models; one controlled egress gateway.
- Document and email contents are untrusted.
- TODO: what is trusted about the agent host and the operators?

## 3. STRIDE

| Category | Example threats | Mitigations | Status |
|---|---|---|---|
| Spoofing | Unauthenticated caller; forged scope token | mTLS/local tokens, caller identity check, signed short-lived tokens | TODO |
| Tampering | Altered tool config/allowlist; altered audit log; modified dependency | Signed config, tamper-evident log, pinned deps | TODO |
| Repudiation | Action without attributable record | Per-call audit incl. refusals | TODO |
| Information disclosure | PII in tool results; exfiltration via outputs or egress | Redaction, output gate, egress allowlist | TODO |
| Denial of service | Oversized inputs, runaway calls | Input caps, rate limits, kill switch | TODO |
| Elevation of privilege | Role sees other roles' tools; tool exceeds scope | RBAC, per-tool scoped credentials | TODO |

## 4. MCP-specific risks

### Tool poisoning
Malicious or altered tool descriptions/metadata steering the model.
- How are tool definitions reviewed, pinned and integrity-checked?
- Can a tool description change at runtime?

### Prompt injection through tool results
Documents/emails returned by tools carrying instructions.
- Which tools return content derived from untrusted input?
- What structure/schema constrains results?

### Confused deputy
The server acting with its own privileges on behalf of a misled model or caller.
- Is every call bound to the requesting user's scope, not the server's?

### Token passthrough
Accepting or forwarding tokens not issued for this server.
- Does the server ever forward client tokens downstream? (It should not.)
- Are model-supplied token-like arguments ignored?

### Over-broad scopes
- Does each tool's credential grant only what that tool needs?
- Read vs. write separation?

### Supply chain
- Dependency pinning, hashes, SBOM, offline update signing
- Container base image provenance

## 5. Open questions
- TODO
