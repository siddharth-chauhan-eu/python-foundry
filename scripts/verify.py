"""Run the Python-specific checks used by local pre-PR verification."""

from __future__ import annotations

import ast
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



def check_python_syntax() -> None:
    print("\n=== Python source syntax ===", flush=True)
    roots = (
        ROOT / "01-python-fundamentals",
        ROOT / "02-data-analytics",
        ROOT / "scripts",
    )
    files = sorted(
        path
        for root in roots
        for path in root.rglob("*.py")
    )
    if not files:
        raise SystemExit("No Python source files found to syntax-check.")

    for path in files:
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except (SyntaxError, UnicodeDecodeError) as exc:
            print(f"FAILED: {path}: {exc}", flush=True)
            raise SystemExit(1) from exc

    print(f"Syntax OK: {len(files)} Python files", flush=True)

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

    check_python_syntax()

    run_check(
        "Python dependency consistency",
        [uv, "pip", "check", "--python", sys.executable],
    )
    run_check(
        "Python import smoke test",
        [
            sys.executable,
            "-c",
            "import datasets, ipykernel, jupyterlab, matplotlib.pyplot, "
            "notebook, numpy, pandas, seaborn; "
            "print('Python imports OK')",
        ],
    )
    run_check("JupyterLab version", [jupyter, "lab", "--version"])
    run_check("Notebook version", [jupyter, "notebook", "--version"])

    print("\nAll Python-specific verification checks passed.")


if __name__ == "__main__":
    main()
