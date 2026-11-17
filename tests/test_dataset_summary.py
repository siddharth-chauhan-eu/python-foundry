"""Tests for the dataset-summary CSV inspection CLI."""

from __future__ import annotations

import csv
import json
import shutil
import subprocess
import sys

from helpers import ROOT, load_module

SCRIPT = "01-python-fundamentals/project/dataset-summary/dataset_summary.py"
dataset_summary = load_module("dataset_summary", SCRIPT)

WORLD_BANK_FIXTURE = ROOT / "tests/fixtures/dataset-summary/world_bank_gdp.csv"
WORLD_BANK_IDENTIFIERS = [
    "Country Name",
    "Country Code",
    "Indicator Name",
    "Indicator Code",
]

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


def test_cli_summarizes_world_bank_gdp_export(tmp_path):
    assert WORLD_BANK_FIXTURE.is_file(), f"Missing fixture: {WORLD_BANK_FIXTURE}"
    csv_path = tmp_path / "world_bank_gdp.csv"
    shutil.copyfile(WORLD_BANK_FIXTURE, csv_path)

    result = subprocess.run(
        [sys.executable, "-I", str(ROOT / SCRIPT), str(csv_path)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "Summary generated successfully." in result.stdout
    json_path = tmp_path / "summary_report.json"
    text_path = tmp_path / "summary_report.txt"
    assert json_path.is_file()
    assert text_path.is_file()
    report = json.loads(json_path.read_text("utf-8"))
    text = text_path.read_text("utf-8")

    # Read the fixture independently of the tool under test.
    with csv_path.open(encoding="utf-8-sig", newline="") as file:
        lines = list(csv.reader(file))
    header_index = next(i for i, row in enumerate(lines) if row[:1] == ["Country Name"])
    header = [name for name in lines[header_index] if name.strip()]
    data_rows = [row for row in lines[header_index + 1 :] if any(row)]

    # The header after the export preamble is found, and the empty trailing field of
    # each line is not a column.
    columns = report["columns"]
    assert columns == header
    assert columns[: len(WORLD_BANK_IDENTIFIERS)] == WORLD_BANK_IDENTIFIERS
    year_columns = [name for name in columns if name.isdigit()]
    assert len(year_columns) >= 30
    assert report["total_rows"] == len(data_rows)
    assert report["total_rows"] >= 100
    assert report["total_columns"] == len(columns)

    # Missing values and types are reported for every column and agree with the data.
    for key in ("missing", "missing_percentage", "column_types"):
        assert set(report[key]) == set(columns)
    expected_missing = {
        name: sum(1 for row in data_rows if not row[index].strip())
        for index, name in enumerate(header)
    }
    assert report["missing"] == expected_missing
    for name in columns:
        percent = round(report["missing"][name] / report["total_rows"] * 100, 2)
        assert report["missing_percentage"][name] == percent
    for name in WORLD_BANK_IDENTIFIERS:
        assert report["column_types"][name] == "non-numeric"
    for name in year_columns:
        assert report["column_types"][name] in {"numeric", "empty"}

    # The text report carries the same figures.
    assert "Dataset Summary Report" in text
    assert "File: world_bank_gdp.csv" in text
    assert f"Total Rows: {report['total_rows']}" in text
    assert f"Total Columns: {report['total_columns']}" in text
    for name in columns:
        assert f"- {name}\n" in text
