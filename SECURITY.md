# Security Policy

This is a private, proprietary repository of Zero State LLC.

## Reporting a vulnerability

Do not open a public issue. Report privately to the repository owner via a
GitHub private security advisory on this repo:
https://github.com/Zero-State-LLC/aspire-mcp/security/advisories/new

## Ground rules

- No secrets, credentials, tokens, keys or client data in this repo, ever. Use
  `.env` locally (gitignored) and the client's vault in deployments.
- Use synthetic data only in tests and fixtures.
- Dependencies are pinned and reviewed; new dependencies need a note in the PR.
- Security design docs live in `docs/` (threat model, injection defenses, red-team plan).

## Status

Starter code. Not production-ready and not deployed anywhere.
