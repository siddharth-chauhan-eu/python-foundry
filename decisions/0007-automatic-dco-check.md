# 0007. Automatic Developer Certificate of Origin check

**Status:** Accepted **Date:** 2026-11-10

## Context

Decision 0006 adopts the Developer Certificate of Origin (DCO) and keeps a manual check: the
maintainer reads the sign-off of each commit before a merge. It states that an automatic check can
replace the manual check and that the change needs a new record.

The check needs no judgement. A missing or mismatched sign-off is a fact of the commit message. A
manual check depends on attention at every merge and leaves no result on the pull request page. A
GitHub App can run the same check on every pull request and report it as a status check that the
ruleset of the default branch can require.

## Decision

The repository keeps the [DCO](../DCO), version 1.1, and adds an automatic check.

- The file `DCO` holds the official text without changes. The text does not allow changes.
- Each commit has a `Signed-off-by` line. This applies to every author, including the maintainer.
  Earlier commits are not changed.
- The [DCO app](https://github.com/apps/dco) checks the sign-off of each commit in a pull request.
  The sign-off must carry the same name and email address as the commit author. The app skips bot
  commits and merge commits. The commits of the maintainer are checked like all others.
- The `DCO` check is a required status check for the default branch, with the other required checks.
- The app runs with its default behavior and has no configuration file. It does not accept
  remediation commits.
- The maintainer keeps the sign-off lines in the squash commit message. The squash merge workflow
  does not change.
- Contributors keep the copyright in their work. Accepting a contribution does not transfer
  ownership and gives the maintainer no right beyond the license that covers the contribution, as
  the [licensing map](../LICENSING.md) sets.
- Third-party material keeps its own license. The sign-off does not replace the maintainer's review
  of license and credit.
- The repository does not adopt a contributor license agreement, a copyright assignment, or an
  indemnity.

Alternatives considered:

- The manual check only. It needs attention at every merge and shows no result on the pull request.
- A job in the verification workflow. It adds no third party, but it adds code to maintain and a
  second place that holds the rule.
- Waiting until the number of pull requests makes the manual check slow, as decision 0006 states.
  The app needs no code and no configuration file in the repository. A sign-off that is missed at
  one merge stays in the history of the default branch, because the ruleset blocks force pushes.

## Consequences

- A pull request with a missing or mismatched sign-off cannot merge until the contributor fixes the
  commits. The contributing guidelines describe the fix.
- The app is a third party. It has read access to repository data and write access to checks.
- When the app is unavailable, merges wait for the check. The maintainer can ask the app to run the
  check again. The app also gives users with write access an override. The override is for an outage
  and does not replace the sign-off rule.
- The sign-off is a statement by the contributor. It is not proof, not a guarantee against claims,
  and not legal advice.
- Clause (d) of the DCO makes the contribution and the sign-off public. The record is kept
  indefinitely and may be redistributed. A contributor can use the GitHub noreply email address to
  keep a personal address private. The sign-off must carry the name and address of the commit
  author.
- The DCO gives no patent grant.
- The DCO text is third-party material. The [third-party notices](../THIRD_PARTY_NOTICES.md) list
  it.
