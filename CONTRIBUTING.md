# Contributing

1. Read [`AGENTS.md`](AGENTS.md) and the requirements checklist in [`README.md`](README.md) first.
2. Branch from `main` (`feat/...`, `fix/...`, `docs/...`) and open a pull request to `main`.
   Use the pull request template. [`CODEOWNERS`](.github/CODEOWNERS) names the reviewers.
3. Before you push, run `ruff check . && ruff format --check . && pytest -q`.
4. CI (lint and test) must pass. Direct pushes and force-pushes to `main` are blocked.
5. No secrets, credentials or real personal data. Synthetic data only.
6. Report vulnerabilities privately per [`SECURITY.md`](SECURITY.md), never in a public issue.
7. Use the issue templates.
