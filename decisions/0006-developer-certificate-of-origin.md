# 0006. Developer Certificate of Origin

**Status:** Accepted **Date:** 2026-11-02

## Context

Decision 0004 sets the license of a contribution: it takes the license of the content it changes.
The contributing guidelines ask each contributor to confirm that they have the right to submit the
work. That confirmation is one general statement. It leaves no record that is tied to a commit.

The commit history goes with every clone. A pull request page exists only on GitHub. A record in the
commit message stays with the code.

## Decision

The repository uses the [Developer Certificate of Origin](../DCO), version 1.1 (DCO).

- The file `DCO` holds the official text without changes. The text does not allow changes.
- Each commit has a `Signed-off-by` line. This applies to every author, including the maintainer. It
  applies to commits made after this record is accepted. Earlier commits are not changed.
- The maintainer checks the sign-off of each original commit by hand before a merge. The maintainer
  keeps the sign-off lines in the squash commit message. The squash merge workflow does not change.
- Contributors keep the copyright in their work. Accepting a contribution does not transfer
  ownership and gives the maintainer no right beyond the license that covers the contribution, as
  decision 0004 sets.
- Third-party material keeps its own license. The sign-off does not replace the maintainer's review
  of license and credit.
- The repository does not adopt a contributor license agreement, a copyright assignment, or an
  indemnity. It adds no automatic check at this time.

Alternatives considered:

- No change. The general statement stays, and no record is tied to a commit.
- A contributor license agreement or a copyright assignment. They add more friction and more legal
  weight than a personal repository needs. An assignment would also move ownership to the
  maintainer.
- A sign-off from outside contributors only. It needs an exception list, and a rule that applies to
  everyone is simpler to check. Dependabot commits already carry a sign-off line.
- An automatic check now, such as a GitHub App or a workflow. It adds a dependency and a maintenance
  task that the current number of contributions does not justify.

## Consequences

- A contributor adds `-s` to each commit. A pull request with a missing sign-off waits until the
  contributor fixes it.
- The maintainer checks by hand. When the number of pull requests makes this slow, an automatic
  check can replace it. That change needs a new record.
- The sign-off is a statement by the contributor. It is not proof, not a guarantee against claims,
  and not legal advice.
- Clause (d) of the DCO makes the contribution and the sign-off public. The record is kept
  indefinitely and may be redistributed. A contributor can use the GitHub noreply email address to
  keep a personal address private.
- The DCO gives no patent grant. The licenses of decision 0004 do not change.
- The DCO text is third-party material. The [third-party notices](../THIRD_PARTY_NOTICES.md) list
  it.
