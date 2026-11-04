# Contributing

Thank you for your interest. This is a personal Python repository. Issues and pull requests are
reviewed as capacity allows, and no response time is promised.

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).

## Before opening an issue

1. Search existing issues first.
2. Use an issue form and give enough detail to reproduce the problem.
3. For a security vulnerability, **do not open a public issue**. Follow the
   [security policy](SECURITY.md).

## Before opening a pull request

Small, self-contained fixes may be submitted directly. For a larger change, a new dependency, or a
change to project structure, open an issue first so the scope can be agreed.

A pull request should:

- address one coherent change;
- explain the problem and the chosen approach;
- include tests or other verification appropriate to the change;
- update documentation when behavior, setup, or commands change;
- add a changelog entry when the change is notable (see [Changelog](#changelog)); and
- avoid unrelated refactors and formatting changes.

Run the full local verification before you open the pull request, and report the result in the pull
request description:

```bash
uv run --locked python scripts/verify.py
```

The [README](README.md) describes the setup and each individual check.

Changes reach `main` through pull requests, and each pull request is squash merged. The pull request
title becomes the commit subject, so write it in the commit format below. Write the description in
the pull request template. The verification workflow must pass before a merge.

## Commit messages

Start the subject with a type, an optional scope in parentheses, and a colon. Then write a short
description in the imperative mood, without a final period. Use a scope only for a clearly bounded
area, as in `docs(readme): update the setup steps`.

| Type       | Use for                                     |
| ---------- | ------------------------------------------- |
| `feat`     | A new feature or project                    |
| `fix`      | A correction to behavior or content         |
| `docs`     | Documentation only                          |
| `refactor` | A code change that does not change behavior |
| `test`     | Tests only                                  |
| `chore`    | Maintenance, such as dependency updates     |
| `ci`       | Changes to workflows and automation         |

Keep each commit to one logical change. When the subject is not enough, add a body as a bullet list
that says what changed and why.

End each commit message with a `Signed-off-by` line. See
[Developer Certificate of Origin](#developer-certificate-of-origin).

## Changelog

`CHANGELOG.md` records the notable changes of each release in the
[Keep a Changelog](https://keepachangelog.com/) format.

Add an entry under `## [Unreleased]` in the same pull request when a change is notable. Place it in
one of the groups `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, or `Security`, and describe
the change in one short line.

Notable changes include new or changed content, projects, or commands; corrections to results;
changes to licenses, policies, or community files; and security fixes. Routine dependency updates,
workflow changes, and internal maintenance need no entry.

The maintainer may edit or add an entry before a merge. At a release, the maintainer moves the
`Unreleased` entries under the new version and its date.

## Documentation

- Write in clear, plain English.
- Use sentence case for headings below the title. Names, document titles, acronyms, and adapted text
  keep their original capitals.
- Keep Markdown within the formatting and lint rules that `scripts/verify.py` checks.
- Name the source of any data, code, or idea that you use. Pin the revision of an external dataset.
  Record assumptions and limitations next to the result.
- Do not state details that change often, such as counts, dates, or version lists. Link to the file
  that holds them.

## Decision records

A decision record, also called an architecture decision record (ADR), records a durable decision
about this repository. A record must be understandable from the repository and its public references
alone.

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
correctness, verification, and maintainability. The maintainer makes the final decision on each
change.

By submitting a contribution, you confirm that you have the right to submit it and that it is
licensed under the license that covers the content it changes or adds, as listed in the
[licensing map](LICENSING.md). Do not submit material you do not have the right to share, or data
whose license does not allow redistribution.

You keep the copyright in your contribution. Accepting a contribution does not transfer ownership.
It gives the maintainer no right beyond the license that covers the contribution.

Material from another source keeps its own license. Name the source and its license in the pull
request. When the material is in the repository, it also needs an entry in the
[third-party notices](THIRD_PARTY_NOTICES.md). The maintainer reviews the license and the credit
before a merge. A sign-off does not replace this review.

### Developer Certificate of Origin

This repository uses the [Developer Certificate of Origin](DCO) (DCO), version 1.1. It is a short
statement that you have the right to submit your work. It is not a copyright assignment and not a
contributor license agreement.

Add a sign-off line to the end of each commit message:

```text
Signed-off-by: Your Name <your-email@example.com>
```

Git adds this line when you commit with `git commit -s`. Use the name and email address from your
Git configuration. The sign-off means that you agree to the DCO for that commit. A sign-off is not a
cryptographic signature. It is a line of text in the message.

Every commit needs a sign-off, including the commits of the maintainer. The rule applies to commits
made after the DCO was adopted. Earlier commits are not changed.

To add a missing sign-off to the last commit, run `git commit --amend --signoff --no-edit`. To add
it to every commit of your branch, update your local `main` and run `git rebase --signoff main` from
your branch. Then run `git push --force-with-lease`.

The maintainer checks the sign-off of each commit by hand before a merge. A pull request with a
missing sign-off waits until you fix it. The maintainer keeps the sign-off lines in the squash
commit message.

The DCO states that your contribution and your sign-off are public. The project keeps this record
indefinitely and may redistribute it. Your name and email address stay in the Git history. To keep
your personal email address private, use the noreply email address that GitHub gives you. You can
find it in your GitHub email settings.
