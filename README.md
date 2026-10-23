# Python Foundry

[![Verification](https://github.com/siddharth-chauhan-eu/python-foundry/actions/workflows/verification.yml/badge.svg)](https://github.com/siddharth-chauhan-eu/python-foundry/actions/workflows/verification.yml)

Python projects built to be reproducible and traceable. Each project locks its environment and
documents its sources, assumptions, and limitations.

Online courses, technical documentation, and public datasets provide references and inputs where
relevant. Each project applies them to a concrete problem and documents its methods, extensions,
sources, dataset revisions, assumptions, and limitations in context.

## Highlights

Start here for the finished projects.

- [India Data Jobs Market Analysis](02-data-analytics/data-jobs-analysis/project/job-market-analysis/README.md):
  a five-notebook study of India's data-job market. It covers market structure, skill demand, skill
  evolution, compensation evidence, and skill strategy for Data Analysts. The dataset revision is
  pinned.
- [Dataset Summary](01-python-fundamentals/project/dataset-summary/README.md): a command-line tool
  that inspects the structure of a CSV file and writes a text summary and a JSON report. It uses
  only the Python standard library and has tests.

## Contents

- [01 — Python Fundamentals](01-python-fundamentals/README.md): core language exercises and a CSV
  inspection command-line tool.
- [02 — Data Analytics](02-data-analytics/README.md): data preparation, analysis, and visualization
  applied to public job-posting data. The dataset is not redistributed in this repository.

## Environment and dependencies

The project environment is managed with [uv](https://docs.astral.sh/uv/). Direct dependencies are
declared in `pyproject.toml`; `uv.lock` records the resolved dependency graph, including
platform-specific markers. The committed lockfile lets `uv` select the applicable locked
dependencies for each supported platform.

### Supported setup

The setup instructions below cover macOS, Windows, and Linux. Install `uv` using a method
appropriate for your operating system. The official [uv installation guide] lists all supported
methods. The project declares Python 3.11 or newer; `uv` can install a compatible interpreter when
one is not already available.

**macOS (Homebrew):**

```bash
brew install uv
```

**Windows (PowerShell with WinGet):**

```powershell
winget install --id=astral-sh.uv -e
```

**Linux (official installer):**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Open a new terminal after installation, then clone the repository and create the environment from
the committed lockfile:

```bash
git clone https://github.com/siddharth-chauhan-eu/python-foundry.git
cd python-foundry
uv sync --locked
```

`uv sync --locked` creates or synchronizes the project-local `.venv` and fails if the lockfile is
out of date instead of silently updating it. `uv` selects a compatible Python interpreter according
to the project configuration and can manage Python installations when needed.

### Run the notebooks

Launch JupyterLab from the repository root:

```bash
uv run --locked jupyter lab
```

Configure your editor or IDE to use the repository's `.venv` Python interpreter. For notebooks,
select that environment as the notebook kernel. The interpreter is `.venv/bin/python` on macOS and
Linux, or `.venv\Scripts\python.exe` on Windows.

For a basic dependency and import check, run:

```bash
uv run --locked python -c "import datasets, matplotlib, numpy, pandas, seaborn; print('Core imports OK')"
```

The initial setup and projects that retrieve external datasets require network access. Reproducible
package versions do not, by themselves, guarantee identical numerical results across operating
systems or hardware. Projects that depend on external data should pin or otherwise document the
input version and source it uses.

### Maintain dependencies

Use `uv` to change dependencies so the manifest and lockfile remain synchronized. Replace the
placeholder names below with actual package names:

```bash
uv add package-name
uv add --dev development-tool
uv lock
uv lock --check
uv sync --locked
```

Commit `pyproject.toml` and `uv.lock` together after reviewing the changes and validating the
result. Do not edit `uv.lock` manually. See the [uv project documentation] for additional commands
and configuration options.

## Repository layout

```text
python-foundry/
├── .github/
├── 01-python-fundamentals/
├── 02-data-analytics/
├── decisions/
├── scripts/
└── tests/
```

## Checks

Run `uv run --locked python scripts/verify.py` for the full local pre-PR verification. It requires
only uv and Git. It checks Ruff lint and format, tests, Markdown lint and format, the locked Python
environment, Python imports, Jupyter commands, and Git whitespace. `uv run --locked` first
synchronizes the project-local `.venv` from `uv.lock`. The script does not format files or change
Git staging.

GitHub Actions runs the same script on every pull request and on every push to `main`. The Python
versions and operating systems it covers are defined in `.github/workflows/verification.yml`.

**Lint and format Python (Ruff, pinned in `uv.lock`):**

```bash
uv run --locked ruff check .
uv run --locked ruff format --check .
```

To apply Ruff formatting, run `uv run --locked ruff format .` and review the resulting changes.

**Run the tests (pytest, pinned in `uv.lock`):**

```bash
uv run --locked pytest
```

**Check Markdown (PyMarkdown lint and mdformat format, pinned in `uv.lock`):**

```bash
uv run --locked python scripts/check_markdown.py
```

To apply Markdown formatting, run `uv run --locked mdformat $(git ls-files '*.md')` and review the
resulting changes.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to report issues and propose changes.

## Security

Report suspected vulnerabilities privately, as described in [SECURITY.md](SECURITY.md). Do not open
a public issue for a vulnerability.

## Licensing

This repository uses more than one license. The [licensing map](LICENSING.md) lists the license for
each type of content.

[uv installation guide]: https://docs.astral.sh/uv/getting-started/installation/
[uv project documentation]: https://docs.astral.sh/uv/guides/projects/
