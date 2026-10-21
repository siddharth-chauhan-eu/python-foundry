# 0001: Repository name

**Status:** Accepted

**Date:** 2026-10-21

## Context

The repository started as a place for course exercises and was named `python-learning`. It now holds
course-driven work that the maintainer extended, and it is meant to hold original Python projects.
Some of these projects will not be about data. The old name described the origin of the work, not
its scope.

Readers already know the old name. A rename changes links and local clones, so it needs a record.

## Decision

Rename the repository to `python-foundry`.

The name describes a place where Python work is built. It does not limit the repository to data
work, and it does not refer to courses. The repository stays under the same account.

Names considered and not chosen:

- `python-learning`: describes the origin of the work, not its scope.
- `python-lab`: generic. Many existing repositories use this name.
- `python-data-workbench`: limits the scope to data work.

## Consequences

- GitHub redirects the old repository address to the new one. Existing links keep working.
- Local clones need a new remote address. The README, the project name in `pyproject.toml`, and the
  lock file use the new name.
- Settings, rulesets, alerts, and code scanning stay with the repository.
- Later decisions that the maintainer expects readers to question get their own record in this
  directory.
