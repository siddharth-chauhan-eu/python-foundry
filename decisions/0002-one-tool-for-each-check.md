# 0002. One tool for each check

**Status:** Accepted **Date:** 2026-10-24

## Context

Two tool sets checked the repository. Python tools were pinned in `uv.lock`. Node tools checked
Markdown and had their own lock file, package manager, and CI job. A custom syntax check in
`scripts/verify.py` repeated the syntax errors that Ruff lint reports.

Ruff replaced the custom syntax check on 2026-10-21. PyMarkdown and mdformat replaced the Node tools
on 2026-10-21.

## Decision

Each kind of check has one owning tool. `uv.lock` pins every tool. `scripts/verify.py` runs all
checks, and CI runs that script.

The owners are:

- Ruff for Python lint, format, and syntax errors.
- pytest for tests.
- PyMarkdown for Markdown lint.
- mdformat for Markdown format.
- uv for the locked environment and its consistency check.

Adding a second tool for a check, or replacing its owner, requires a new decision record.

## Consequences

- Every check runs with uv and Git alone.
- One lock file pins all tool versions.
- A local run and a CI run execute the same script.
- `scripts/verify.py` stops at the first failing check.
- A change of tool requires a new decision record.
