"""Check the repository's Markdown files with PyMarkdown (lint) and mdformat (format)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def markdown_files() -> list[str]:
    """Return tracked and not-yet-tracked Markdown files, honoring .gitignore."""
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "--", "*.md"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return sorted(set(result.stdout.splitlines()))


def run_tool(label: str, command: list[str]) -> int:
    print(f"\n=== {label} ===", flush=True)
    return subprocess.run(command, cwd=ROOT, check=False).returncode


def main() -> int:
    files = markdown_files()
    if not files:
        print("No Markdown files found.", file=sys.stderr)
        return 1

    # Run both tools so one run reports every problem.
    lint = run_tool(
        "Markdown lint", [sys.executable, "-m", "pymarkdown", "scan", *files]
    )
    fmt = run_tool(
        "Markdown format", [sys.executable, "-m", "mdformat", "--check", *files]
    )
    return 1 if lint or fmt else 0


if __name__ == "__main__":
    raise SystemExit(main())
