# 0003. CI version and operating system matrix

**Status:** Accepted **Date:** 2026-10-24

## Context

`pyproject.toml` declares Python 3.11 or newer. The README covers setup on macOS, Windows, and
Linux. A matrix of every supported Python version on every supported operating system multiplies the
number of CI jobs. For two Python versions on three operating systems, it gives six jobs.

## Decision

CI runs `scripts/verify.py` on the lowest supported Python version on each supported operating
system, and on the newest supported Python version on Linux.

Since 2026-10-21 this has been four jobs: Python 3.11 on Linux, macOS, and Windows, and Python 3.14
on Linux. `.github/workflows/verification.yml` defines the current jobs.

The lowest version on each operating system exposes failures specific to an operating system. The
newest version on one operating system exposes failures specific to a Python version.

## Consequences

- The newest Python version does not run on macOS or Windows. A failure specific to that combination
  does not appear in CI.
- A new minimum or newest Python version changes the workflow file.
- Each job runs the same script as a local check.
