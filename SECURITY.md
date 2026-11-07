# Security Policy

## Scope

This repository holds personal Python projects. Vulnerability reports are accepted for the default
branch, the latest release, and the dependencies pinned in `uv.lock`.

A report about a dependency states how the issue affects this repository's use of the locked
version. An issue that exists only in an upstream project goes to that project's maintainers.

## Reporting a vulnerability

**Do not disclose a suspected vulnerability in a public issue or pull request.**

Use GitHub private vulnerability reporting:
[Report a vulnerability](https://github.com/siddharth-chauhan-eu/python-foundry/security/advisories/new).
If it is unavailable, send the report to
[siddharthchauhan@duck.com](mailto:siddharthchauhan@duck.com). Include, where applicable:

- the affected file, dependency, or command;
- the affected commit or version, if known;
- a concise description of the issue and its potential impact;
- reproduction steps or a proof of concept; and
- any relevant logs or screenshots with secrets and unrelated personal data removed.

Do not send credentials, private keys, access tokens, or other live secrets.

## Response and disclosure

Reports are reviewed on a best-effort basis. There is no guaranteed acknowledgement or remediation
time.

Public disclosure is coordinated with the maintainer. The default coordination period is 90 calendar
days from the report. The period allows time to investigate and attempt remediation. It does not
promise a fix within that time. The reporter and the maintainer may agree on an earlier or later
date. When no date is agreed, the reporter may disclose after the period.

The maintainer credits the reporter in a public advisory or in release notes only with the
reporter's consent.
