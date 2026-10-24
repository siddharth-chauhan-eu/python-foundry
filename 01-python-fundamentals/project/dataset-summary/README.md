# Dataset Summary

Part of [01 — Python Fundamentals](../../README.md).

Structural inspection for CSV files — no dependencies, no data-specific assumptions.

A command-line tool that analyzes CSV datasets and generates a human-readable text summary and a
structured JSON report. Handles both standard and wide/messy formats (e.g., World Bank exports).

## Motivation

Working with public datasets (e.g., World Bank) requires an initial step: understanding structure
before analysis. This tool provides a single-command way to inspect columns, missing values, and
basic data types.

## Requirements

- Python standard library only. The [project configuration](../../../pyproject.toml) sets the
  supported Python versions.

## Usage

```bash
python dataset_summary.py <csv_file>
```

Example:

```bash
python dataset_summary.py sample_data.csv
```

## Output

Two files are written to the same directory as the input:

| File                  | Description            |
| --------------------- | ---------------------- |
| `summary_report.txt`  | Human-readable summary |
| `summary_report.json` | Structured report      |

**JSON structure:**

```json
{
    "column_types": {
        "country": "non-numeric",
        "gdp": "numeric",
        "inflation": "mixed",
        "notes": "non-numeric",
        "year": "mixed"
    },
    "columns": [
        "country",
        "year",
        "gdp",
        "inflation",
        "notes"
    ],
    "file": "sample_data.csv",
    "missing": {
        "country": 1,
        "gdp": 1,
        "inflation": 2,
        "notes": 1,
        "year": 0
    },
    "missing_percentage": {
        "country": 10.0,
        "gdp": 10.0,
        "inflation": 20.0,
        "notes": 10.0,
        "year": 0.0
    },
    "total_columns": 5,
    "total_rows": 10
}
```

## Capabilities

Given a CSV file, the tool:

- detects a valid header row (including in messy or wide files)
- computes total rows and columns
- counts missing values (absolute and percentage)
- infers column types: `numeric` · `non-numeric` · `mixed` · `empty`

## Parsing strategy

Two-stage approach:

1. Standard parsing via `csv.DictReader`
2. Fallback: scan lines for a structurally valid header row and retry

Type inference is based on the composition of non-empty values — no column names or dataset-specific
rules.

## Assumptions

- Delimiter is comma (`,`)
- Encoding is UTF-8 (BOM supported)
- File fits in memory

## Known limitations

| Case                                 | Behavior                     |
| ------------------------------------ | ---------------------------- |
| Non-comma delimiter (e.g., `;`)      | Incorrect parsing            |
| Very large files                     | High memory usage            |
| Inconsistent row lengths             | Partial parsing              |
| Corrupted CSV                        | Returns empty dataset        |
| `nan`, `inf`, or `1_000` in a column | Counted as numeric           |
| Usage, file, or parse error          | Message printed, exit code 0 |

## Non-goals

This tool does not:

- detect delimiters automatically
- validate schemas
- clean or transform data
- perform statistical analysis

## Validation

Validated against:

- structured datasets
- edge-case synthetic dataset (sample_data.csv)
- real-world messy datasets (e.g., World Bank exports)

## Design principles

- Structure over assumptions
- No hardcoded column names or dataset-specific rules
- Deterministic output
- Fail safely — no crashes on malformed input
- Standard library only

## Project structure

```text
dataset-summary/
├── dataset_summary.py
├── sample_data.csv
└── README.md
```

## Boundary

This tool is limited to structural inspection and reporting. It does not alter, validate, or
interpret data beyond basic type inference.
