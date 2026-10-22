# 0001. Repository name

**Status:** Accepted **Date:** 2026-10-22

## Context

The repository started as a place for course exercises and was named `python-learning`. It now holds
course-driven work that the maintainer extended, and it is meant to hold original Python projects.
Some of these projects will not be about data. The old name described the origin of the work, not
its scope.

A rename changes the repository address and the setup of local clones, so it needs a record.

## Decision

Rename the repository to `python-foundry`.

The name describes a place where Python work is built. It does not limit the repository to data
work, and it does not refer to courses. The repository stays under the same account.

Names considered and not chosen:

- `python-learning`: describes the origin of the work, not its scope.
- `python-lab`: generic. It says nothing specific to this repository.
- `python-data-workbench`: limits the scope to data work.

## Consequences

- GitHub redirects the old repository address to the new one. Existing links keep working.
- Local clones keep working through the redirect. Update their remote address to the new one.
- The README, the project name in `pyproject.toml`, and the lock file use the new name.
- Settings, rulesets, alerts, and code scanning stay with the repository.
- Do not create another repository named `python-learning` under this account. GitHub ends the
  redirect if the old name is reused.
