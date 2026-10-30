---
name: graft
description: Query and refresh the repo-local Graft code index before reading Aspire source.
---

# Graft for Aspire

Use the approved `@trailhq/trail-code@0.23.0` pin. The global `graft` executable may be a different version, so use the command below. Run from this repository's root and always pass the root explicitly to prevent ancestor/home-index fallback.

```sh
DO_NOT_TRACK=1 npm exec --yes --package=@trailhq/trail-code@0.23.0 -- trail map "$PWD"
DO_NOT_TRACK=1 npm exec --yes --package=@trailhq/trail-code@0.23.0 -- trail ask "<task or symbol>" "$PWD" --source
DO_NOT_TRACK=1 npm exec --yes --package=@trailhq/trail-code@0.23.0 -- trail grep "<literal>" "$PWD" --fixed
DO_NOT_TRACK=1 npm exec --yes --package=@trailhq/trail-code@0.23.0 -- trail skeleton path/to/file "$PWD"
DO_NOT_TRACK=1 npm exec --yes --package=@trailhq/trail-code@0.23.0 -- trail callers Symbol "$PWD" --depth 2
DO_NOT_TRACK=1 npm exec --yes --package=@trailhq/trail-code@0.23.0 -- trail build "$PWD"
DO_NOT_TRACK=1 npm exec --yes --package=@trailhq/trail-code@0.23.0 -- trail build "$PWD" --check --json
```

Start unfamiliar source work with `map`. Use `ask --source` for understanding, `grep` for exhaustive occurrences, `skeleton` for signatures, and `callers` before changing interfaces. Follow the returned exact source spans. Rebuild after changing branches or substantial code changes. Never clip Graft output through head/tail/sed.

The deterministic index is a local cache for the current checkout, not evidence that unmerged branches or other worktrees were indexed. Empty indexes are expected in documentation-only or placeholder repositories. For Markdown/specs and unsupported languages, follow the repository's README/spec map and use text search. Never substitute an ancestor graph.

Do not run `init`, transcript/history imports, workspace sign-in, global hooks, paid `--deep`, or project code/tests as part of indexing. Telemetry stays disabled with `DO_NOT_TRACK=1`. This is development tooling only, not a target Mac or Hermes-profile installation. Existing security and review rules still apply.
