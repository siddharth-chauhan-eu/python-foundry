# 0005. Community health scope

**Status:** Accepted **Date:** 2026-10-24

## Context

The repository is a personal project with one maintainer. It has no releases and no deployed
service. Issues and pull requests can still arrive from outside, so the repository defines how to
report a problem, report a vulnerability, and contribute.

## Decision

The repository has these community files:

- `SECURITY.md`, which directs vulnerability reports to GitHub private vulnerability reporting.
- Issue forms and a pull request template in `.github`.
- `CONTRIBUTING.md`, which states that the maintainer makes the final decision on each change.
- `CODE_OF_CONDUCT.md`, adapted from the Contributor Covenant 3.0.

These files were added on 2026-10-21 and 2026-10-22.

The license of a contribution follows [decision 0004](0004-licenses-by-content-type.md).

## Consequences

- The repository documents a route for bugs, vulnerabilities, and contributions.
- The scope suits one maintainer. It defines no process for a dispute with the maintainer, and
  reports about the maintainer's conduct go to the maintainer.
- A second maintainer, or a release that others depend on, would change the scope. A new decision
  record would cover the change.
