# 02 — Data Analytics

Part of [Python Foundry](../README.md).

From DataFrame basics to evidence-aware analysis using real-world job-posting data.

This module builds applied data analytics capability in a single coherent arc — exercises establish
Python patterns for structured data, notebooks develop library skills and apply them to Germany's
data-job market, and a project extends the methodology into a structured study of India.

## Learning Arc

| Phase          | Location                                          | Focus                                                          |
| -------------- | ------------------------------------------------- | -------------------------------------------------------------- |
| Foundations    | `data-jobs-analysis/exercises/`                   | Role matching · type conversion · data cleaning in pure Python |
| Library basics | `data-jobs-analysis/notebooks/01–02`              | Pandas operations and first Matplotlib visualization           |
| Analysis       | `data-jobs-analysis/notebooks/03–05`              | Demand, trends, and compensation for Germany's data-job market |
| Project        | `data-jobs-analysis/project/job-market-analysis/` | Structured notebook study of India's data-job market           |

## Dataset

The notebooks and project use the Data Jobs dataset, a collection of data-role job postings from
calendar year 2023. It covers multiple countries and role types. The
[Data Jobs Analysis](data-jobs-analysis/README.md#data-source) README lists the source, the pinned
revision, and the checksum. The pure-Python exercises use small in-repository examples rather than
the external dataset.

## Environment setup

Run the setup command from the repository root:

```bash
uv sync --locked
```

Use the repository's `.venv` as the notebook kernel. See the
[root setup instructions](../README.md#supported-setup).

See the [Data Jobs Analysis](data-jobs-analysis/README.md) for full documentation.
