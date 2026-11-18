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

## Supported releases

Security fixes apply to the default branch and the latest release. A release is supported until a
newer release is published. Earlier releases receive no security updates.

## Remediation of findings

Dependabot alerts and code scanning alerts of high or critical severity are fixed before a release
is published. Other findings are handled in routine maintenance. A finding that does not affect this
repository may be dismissed with a recorded reason. A pull request that introduces a high or
critical code scanning alert, or adds a dependency with a high or critical known vulnerability,
cannot be merged.

## Verifying releases

A release tag is a signed annotated tag. The tag page on GitHub shows a Verified label that confirms
the signature and the signing identity.

## Security assessment

This assessment covers the code and the automation in the repository as of the latest release. It
names the most likely problems and the problems with the most impact. The repository runs no network
service and stores no user data.

- **Untrusted input to the command-line tool.** The Dataset Summary tool reads a CSV file that the
  user selects. It loads the whole file into memory, so a very large file can exhaust memory. The
  tool does not run, evaluate, or fetch anything that the file names. It produces two report files.
- **Output files.** The tool writes `summary_report.txt` and `summary_report.json` next to the input
  file and replaces files with those names. A symbolic link with one of these names redirects the
  write to the target of the link.
- **Notebooks.** Running a notebook runs its code with the permissions of the user, so a notebook
  from an untrusted source is a risk. The notebooks download a public dataset at a pinned revision,
  so the input does not change silently.
- **Dependencies.** A vulnerable or malicious release of a third-party package is the most likely
  route to harm. `uv.lock` pins every package. Dependabot raises alerts and updates, and a
  dependency review check blocks a pull request that adds a vulnerable dependency.
- **Automation.** Workflows have read-only repository permissions, use actions pinned to full commit
  SHAs, and do not persist credentials. The Scorecard workflow also requests an identity token to
  publish its results. The repository settings restrict which actions may run. A change to the
  default branch needs a pull request, signed commits, and passing checks.
