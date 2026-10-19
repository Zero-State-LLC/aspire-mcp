# aspire-mcp

Starter repo for an **on-prem MCP server** for the Aspire engagement. Private and
proprietary to Zero State LLC (see `LICENSE`).

## Purpose

The MCP server is the only path by which a locally hosted AI can reach client
systems (loan software, document store, email). It must run fully inside the
client's building, with narrow tools, least privilege and strong audit.

## Scope

- In: the MCP server, its tools, config, auth, audit, and the security work
  (threat model, prompt-injection defenses, red team). Security lead: @arshi016.
- Out: the model host, the client's systems themselves, anything with client data.
  Use synthetic data only.

This is a starting point, not a finished product. It is not deployed anywhere.

## On-prem MCP requirements (checklist)

Sources: Danny's on-prem MCP requirements email (2026-10-14 PT) and the MCP
sections of the Aspire engagement spec (technical requirements only).

**Network / locality**
- [ ] Fully local: no outside network access, no cloud LLMs, no telemetry
- [ ] Single tightly controlled egress gateway for the few integrations that must go out
- [ ] Server reachable only from the agent host (local socket or private network), never the open network

**Tools**
- [ ] Few, narrow, task-specific tools (e.g. "get loan file status", "fetch document X")
- [ ] No raw SQL, no shell, no general file access
- [ ] Read-only by default; any write action gated behind human approval
- [ ] Config file allowlist of tools; nothing outside it is exposed (skeleton: `ASPIRE_MCP_ALLOWED_TOOLS`)
- [ ] Write-type tools produce drafts/queued requests, not direct actions; outbound messages come from reviewed templates with typed fields, not free-form model text
- [ ] Tools return structured, schema-validated results only, never raw documents, file names or extracted identifiers where not needed
- [ ] Result size caps with cursor-based paging

**Least privilege / credentials**
- [ ] Each tool has its own scoped credentials
- [ ] Credentials stored in the client's own vault, never in prompts or code

**Data protection**
- [ ] Borrower personal data masked/redacted before it reaches the model
- [ ] Unmasked only where a tool strictly needs it
- [ ] Output gate (leak check) on every tool result; on failure return a block record instead

**Audit**
- [ ] Every call logged: timestamp, caller, tool, inputs, output summary
- [ ] Log references (IDs, hashes), not content
- [ ] Tamper-evident and exportable by the client for compliance
- [ ] Every refused call is logged too

**Prompt-injection defense**
- [ ] Document and email contents treated as untrusted data
- [ ] Validate all tool inputs
- [ ] Confirmation required before any action triggered by document content
- [ ] Aligned with OWASP guidance on prompt injection and excessive agency

**Auth**
- [ ] Mutual TLS or local tokens between agent and server
- [ ] Caller identity verified on every call
- [ ] Role-based access: each staff role sees only its own tools
- [ ] Short-lived, signed per-session scope token limiting which records a call may touch; injected outside the model, so it never enters model context; model-supplied token-like arguments are overwritten/ignored
- [ ] Server checks signature, expiry and scope, and refuses otherwise

**Ops**
- [ ] Ships as a container or appliance with no external dependencies
- [ ] Updatable offline
- [ ] Health check
- [ ] Kill switch (skeleton: `ASPIRE_MCP_KILL_SWITCH`)

**Red team (before go-live)**
- [ ] Injection via uploaded documents
- [ ] Data exfiltration through tool outputs
- [ ] Privilege escalation

### TODOs (not specified by sources)

- TODO: transport choice for production (stdio vs. local HTTP/socket) and mTLS details
- TODO: which vault product and how tools fetch credentials
- TODO: audit log format, storage and tamper-evidence mechanism; retention period
- TODO: redaction approach and which fields count as personal data
- TODO: human-approval mechanism for writes
- TODO: container base image, offline update/signing process
- TODO: health check interface (endpoint vs. tool vs. CLI)
- TODO: the real tool list and their schemas
- TODO: RBAC role definitions

## Stack

Python 3.11+ with the official MCP Python SDK (`mcp`, FastMCP), stdio transport.

## How to run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env   # no real values needed
python -m aspire_mcp   # starts the server on stdio
```

Try it with the MCP Inspector: `npx @modelcontextprotocol/inspector python -m aspire_mcp`.

Lint and test:

```bash
ruff check . && ruff format --check . && pytest -q
```

## Layout

```
src/aspire_mcp/   server skeleton (config.py, server.py)
tests/            basic tests
docs/             threat model, injection defenses, red-team plan (owner: @arshi016)
```

## Contribution flow

1. Branch from `main` (`feat/...`, `fix/...`, `docs/...`).
2. Open a PR to `main`. CI (lint + test) must pass. Direct pushes and force-pushes to `main` are blocked.
3. Danny reviews and merges.
4. No secrets or client data in any commit. Synthetic data only.
