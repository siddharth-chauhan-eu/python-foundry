# Contributing

Thank you for your interest. This is a personal Python practice repository. Issues and pull requests
are reviewed as capacity allows, and no response time is promised.

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

## Acceptance and licensing

Submitting a pull request does not guarantee that it will be merged. Changes are judged on fit,
correctness, verification, and maintainability.

By submitting a contribution, you confirm that you have the right to submit it and that it is
licensed under the repository's [MIT License](LICENSE). Do not submit material you do not have the
right to share, or data whose license does not allow redistribution.
