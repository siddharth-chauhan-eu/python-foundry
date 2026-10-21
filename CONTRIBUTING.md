# Contributing

Thank you for your interest. This is a personal Python practice repository. Issues and pull requests
are reviewed as capacity allows, and no response time is promised.

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).

## Before opening an issue

1. Search existing issues first.
2. Use an issue form and give enough detail to reproduce the problem.
3. For a security vulnerability, **do not open a public issue**. Follow [SECURITY.md](SECURITY.md).

## Before opening a pull request

Small, self-contained fixes may be submitted directly. For a larger change, a new dependency, or a
change to project structure, open an issue first so the scope can be agreed.

A pull request should:

- address one coherent change;
- explain the problem and the chosen approach;
- include tests or other verification appropriate to the change;
- update documentation when behavior, setup, or commands change; and
- avoid unrelated refactors and formatting changes.

Run the full local verification before you open the pull request, and report the result in the pull
request template:

```bash
uv run --locked python scripts/verify.py
```

The [README](README.md) describes the setup and each individual check.

## Commit messages

Use a short, imperative subject with a type prefix, such as `fix:`, `docs:`, `test:`, `ci:`, or
`chore:`.

## Decision records

A decision record, also called an architecture decision record (ADR), records a durable decision
about this repository. It is not a meeting note and it does not hold private deliberation. A reader
who has the repository and its public references must understand it without other context.

Add a record when a decision is hard to reverse or when a reader may question it. Routine edits,
link fixes, and ordinary maintenance do not need a record.

- Records live in `decisions/`. One file records one decision, and its name is
  `NNNN-short-title.md`.
- Numbers are sequential and are never reused. Refer to a record as `decision NNNN`.
- `decisions/README.md` holds a short orientation, a link to this section, and a title-only index.

Use one of these metadata forms:

```markdown
**Status:** Proposed
```

```markdown
**Status:** Accepted **Date:** YYYY-MM-DD
```

```markdown
**Status:** Superseded **Superseded by:** [decision NNNN](NNNN-short-title.md)
```

`Date` is the acceptance date. It appears only while the status is `Accepted`. When a decision is
superseded, remove its date, set the status to `Superseded`, and link the replacement. Do not delete
the old record.

Do not rewrite an accepted record for style. Record a changed decision in a new record. Correct an
accepted record only to fix a factual error or to remove ambiguity, and keep the change visible in
Git history.

A new record uses this structure:

```markdown
# NNNN. Short title

**Status:** Proposed

## Context

The problem or question, with the evidence needed to understand the choice.

## Decision

What is decided, and the boundary of that decision.

## Consequences

Benefits, costs, trade-offs, risks, and follow-up work.
```

Use `## Decision` for one decision. Use `## Decisions` only when several choices must stand or fall
together. Choices that can change separately get separate records. Make the material alternatives
clear in Context, Decision, or Consequences.

## Acceptance and licensing

Submitting a pull request does not guarantee that it will be merged. Changes are judged on fit,
correctness, verification, and maintainability.

By submitting a contribution, you confirm that you have the right to submit it and that it is
licensed under the repository's [MIT License](LICENSE). Do not submit material you do not have the
right to share, or data whose license does not allow redistribution.
