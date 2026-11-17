# Third-party notices

This repository uses material from third parties. This file lists each item with its license. The
[licensing map](LICENSING.md) covers the original content. Entries are listed in the order they were
added.

## Data Jobs dataset

- **Source:** [Data Jobs dataset](https://huggingface.co/datasets/lukebarousse/data_jobs) by Luke
  Barousse
- **License:** [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), as stated on the
  dataset page
- **Use:** The notebooks load the dataset at run time. The repository does not include the dataset
  files. Saved notebook outputs show unmodified excerpts of the dataset, such as selected rows and
  columns. Charts and tables are derived from the dataset.

## Developer Certificate of Origin

- **Source:** [Developer Certificate of Origin, version 1.1](https://developercertificate.org/) by
  The Linux Foundation and its contributors
- **License:** The text states that everyone may copy and distribute verbatim copies, and that
  changing the text is not allowed.
- **Use:** The file `DCO` holds the text without changes. It is not original content of this
  repository, and the licenses in the [licensing map](LICENSING.md) do not cover it.

## World Bank GDP data

- **Source:** [GDP (current US$)](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD), indicator
  `NY.GDP.MKTP.CD` of the World Development Indicators, published by the World Bank Group. The
  indicator metadata names these sources: country official statistics, national statistical
  organizations and central banks; national accounts data files of the Organisation for Economic
  Co-operation and Development (OECD); and staff estimates of the World Bank.
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), as stated on the indicator
  page, with the World Bank's
  [terms for datasets under this license](https://datacatalog.worldbank.org/public-licenses#cc-by).
- **Credit:** World Bank Group and the data providers named above.
- **Retrieved:** 2026-11-17, with the CSV download link on the indicator page. The file states the
  last updated date 2026-11-11. Its SHA-256 is
  `566e0c9d13467d289eb6e98e79b7a51ceffa57a1d1c22bb548631246958f7141`.
- **Use:** The file `tests/fixtures/dataset-summary/world_bank_gdp.csv` is the data file
  `API_NY.GDP.MKTP.CD_DS2_en_csv_v2_59541.csv` from the downloaded archive
  `API_NY.GDP.MKTP.CD_DS2_en_csv_v2_59541.zip`, extracted and renamed, with its content unmodified.
  It is a test fixture for the dataset summary tool. It is not original content of this repository,
  and the licenses in the [licensing map](LICENSING.md) do not cover it.
