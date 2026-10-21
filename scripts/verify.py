"""Run the Python-specific checks used by local pre-PR verification."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_check(label: str, command: list[str]) -> None:
    print(f"\n=== {label} ===", flush=True)
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode:
        print(f"FAILED: {label} (exit code {result.returncode})", flush=True)
        raise SystemExit(result.returncode)


def main() -> None:
    expected_env = (ROOT / ".venv").resolve()
    actual_env = Path(sys.prefix).resolve()

    if actual_env != expected_env:
        raise SystemExit(
            "Verification must run inside this project's .venv. "
            "Invoke it with: uv run --locked python scripts/verify.py"
        )

    uv = shutil.which("uv")
    jupyter = shutil.which("jupyter")

    if not uv or not jupyter:
        raise SystemExit("Required command not found: uv or jupyter.")

    run_check("Ruff lint", [sys.executable, "-m", "ruff", "check", "."])
    run_check(
        "Ruff format check", [sys.executable, "-m", "ruff", "format", "--check", "."]
    )
    run_check("Tests", [sys.executable, "-m", "pytest"])
    run_check("Markdown", [sys.executable, str(ROOT / "scripts" / "check_markdown.py")])
    run_check(
        "Python dependency consistency",
        [uv, "pip", "check", "--python", sys.executable],
    )
    run_check(
        "Python import smoke test",
        [
            sys.executable,
            "-c",
            (
                "import datasets, ipykernel, jupyterlab, matplotlib.pyplot, "
                "notebook, numpy, pandas, seaborn; "
                "print('Python imports OK')"
            ),
        ],
    )
    run_check("JupyterLab version", [jupyter, "lab", "--version"])
    run_check("Notebook version", [jupyter, "notebook", "--version"])
    run_check("Whitespace errors (unstaged)", ["git", "diff", "--check"])
    run_check("Whitespace errors (staged)", ["git", "diff", "--cached", "--check"])

    print("\nAll Python-specific verification checks passed.")


if __name__ == "__main__":
    main()
