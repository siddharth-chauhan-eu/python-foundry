"""Tests for the dataset-summary CSV inspection CLI."""

from __future__ import annotations

import json
import subprocess
import sys

from helpers import ROOT, load_module

SCRIPT = "01-python-fundamentals/project/dataset-summary/dataset_summary.py"
dataset_summary = load_module("dataset_summary", SCRIPT)

STANDARD_CSV = (
    "country,year,gdp,notes\n"
    "India,2020,2667,ok\n"
    "Germany,2021,,missing gdp\n"
    "Japan,2021,4937,\n"
)


def write_csv(tmp_path, text, name="data.csv"):
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    return path


def test_read_csv_file_parses_standard_csv(tmp_path):
    rows = dataset_summary.read_csv_file(write_csv(tmp_path, STANDARD_CSV))

    assert len(rows) == 3
    assert list(rows[0]) == ["country", "year", "gdp", "notes"]
    assert rows[1]["gdp"] == ""


def test_read_csv_file_finds_header_after_preamble(tmp_path):
    header = ",".join(f"c{i}" for i in range(11))
    values = ",".join(str(i) for i in range(11))
    text = f"Data Source,Example Agency\n\n{header}\n{values}\n"

    rows = dataset_summary.read_csv_file(write_csv(tmp_path, text))

    assert len(rows) == 1
    assert rows[0]["c10"] == "10"


def test_read_csv_file_returns_empty_list_for_too_few_columns(tmp_path):
    assert dataset_summary.read_csv_file(write_csv(tmp_path, "a,b\n1,2\n")) == []


def test_count_missing_values_counts_empty_cells(tmp_path):
    rows = dataset_summary.read_csv_file(write_csv(tmp_path, STANDARD_CSV))
    columns = list(rows[0])

    assert dataset_summary.count_missing_values(rows, columns) == {
        "country": 0,
        "year": 0,
        "gdp": 1,
        "notes": 1,
    }


def test_analyze_column_types_covers_every_label():
    rows = [
        {"num": "1", "mix": "1", "text": "a", "none": ""},
        {"num": "2.5", "mix": "abc", "text": "b", "none": ""},
    ]

    assert dataset_summary.analyze_column_types(
        rows, ["num", "mix", "text", "none"]
    ) == {
        "num": "numeric",
        "mix": "mixed",
        "text": "non-numeric",
        "none": "empty",
    }


def test_cli_writes_text_and_json_reports(tmp_path):
    csv_path = write_csv(tmp_path, STANDARD_CSV)

    result = subprocess.run(
        [sys.executable, "-I", str(ROOT / SCRIPT), str(csv_path)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "Summary generated successfully." in result.stdout
    report = json.loads((tmp_path / "summary_report.json").read_text("utf-8"))
    assert report["total_rows"] == 3
    assert report["total_columns"] == 4
    assert report["missing"]["gdp"] == 1
    assert report["missing_percentage"]["gdp"] == 33.33
    assert report["column_types"]["gdp"] == "numeric"
    assert "Total Rows: 3" in (tmp_path / "summary_report.txt").read_text("utf-8")


def test_cli_reports_unsupported_structure(tmp_path):
    csv_path = write_csv(tmp_path, "a,b\n1,2\n")

    result = subprocess.run(
        [sys.executable, "-I", str(ROOT / SCRIPT), str(csv_path)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert "Parsing failed" in result.stdout
    assert not (tmp_path / "summary_report.json").exists()
