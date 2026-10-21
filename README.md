# Python Learning

[![Verification](https://github.com/siddharth-chauhan-eu/python-learning/actions/workflows/verification.yml/badge.svg)](https://github.com/siddharth-chauhan-eu/python-learning/actions/workflows/verification.yml)

_Python projects spanning foundational tooling and domain-focused data work._

This repository brings together practical Python implementations, utilities, and applied projects,
from core language concepts to domain-focused data analysis. The work emphasizes sound engineering,
clear reasoning, traceable inputs, and reproducible execution.

Online courses, technical documentation, and public datasets provide references and inputs where
relevant. Projects apply those concepts to concrete problems, with methods, extensions, sources,
dataset revisions, assumptions, and limitations documented in context.

## Portfolio

- [01 — Python Fundamentals](01-python-fundamentals/README.md): core Python concepts and practical
  tooling, including focused exercises and a CSV inspection CLI.
- [02 — Data Analytics](02-data-analytics/README.md): data preparation, analysis, and visualization,
  from library fundamentals to domain-focused job-market analysis.

## 01 — Python Fundamentals

The fundamentals module covers core language concepts through focused implementations, followed by a
command-line project designed around a practical data-inspection task.

- **`exercises/`** — output formatting, variables and types, strings, control flow, validation, and
  data structures.
- **`project/dataset-summary/`** — a CSV structural-inspection CLI built with the Python standard
  library.

See the [Python Fundamentals README](01-python-fundamentals/README.md) for implementation details
and usage instructions.

## 02 — Data Analytics

Applied analysis using Python libraries and the 2023 Data Jobs dataset. The work progresses from
library fundamentals to domain-specific analysis, with project-level documentation for methods and
source-data provenance.

- **`data-jobs-analysis/exercises/`** — data-oriented Python exercises, including role matching and
  type conversion.
- **`data-jobs-analysis/notebooks/`** — Pandas and Matplotlib fundamentals, followed by job-demand,
  skill-trend, and compensation analysis focused on Germany.
- **`data-jobs-analysis/project/job-market-analysis/`** — a five-notebook analysis of India's
  data-job market.

The [Data Jobs Analysis README](02-data-analytics/data-jobs-analysis/README.md) documents the
dataset source, pinned revision, and project-specific details. The dataset is not redistributed in
this repository.

See the [Data Analytics README](02-data-analytics/README.md) for the module overview.

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
git clone https://github.com/siddharth-chauhan-eu/python-learning.git
cd python-learning
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
python-learning/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── config.yml
│   │   └── suggestion.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── dependabot.yml
│   └── workflows/
│       └── verification.yml
├── 01-python-fundamentals/
│   ├── exercises/
│   ├── project/
│   │   └── dataset-summary/
│   └── README.md
├── 02-data-analytics/
│   ├── data-jobs-analysis/
│   │   ├── exercises/
│   │   ├── notebooks/
│   │   ├── project/
│   │   │   └── job-market-analysis/
│   │   └── README.md
│   └── README.md
├── scripts/
│   ├── check_markdown.py
│   └── verify.py
├── tests/
├── .gitattributes
├── .gitignore
├── .mdformat.toml
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── pyproject.toml
├── README.md
├── SECURITY.md
└── uv.lock
```

## Checks

Run `uv run --locked python scripts/verify.py` for the full local pre-PR verification. It requires
only uv and Git. It checks Ruff lint and format, tests, Markdown lint and format, the locked Python
environment, Python imports, Jupyter commands, and Git whitespace. `uv run --locked` first
synchronizes the project-local `.venv` from `uv.lock`. The script does not format files or change
Git staging.

GitHub Actions runs the same script on every pull request and on every push to `main`. It uses
Python 3.11 on Linux, macOS, and Windows, and Python 3.14 on Linux.

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

## License

This repository is licensed under the [MIT License](LICENSE). The exception is
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), which is adapted from the Contributor Covenant 3.0 and
licensed under CC BY-SA 4.0.

[uv installation guide]: https://docs.astral.sh/uv/getting-started/installation/
[uv project documentation]: https://docs.astral.sh/uv/guides/projects/
