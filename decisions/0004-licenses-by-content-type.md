# 0004. Licenses by content type

**Status:** Accepted **Date:** 2026-10-24

## Context

The repository was first licensed under the MIT License alone. It now holds code, original prose,
figures, and a code of conduct adapted from the Contributor Covenant 3.0. The Contributor Covenant
is licensed under CC BY-SA 4.0, which requires an adaptation to carry the same license.

The MIT License is written for software and its documentation. CC BY 4.0 is written for creative
works and lets the licensor designate the credit line.

## Decision

Each license covers a type of content, not a folder:

- MIT License: code, scripts, notebooks, and configuration.
- CC BY 4.0: original prose and figures.
- CC BY-SA 4.0: the code of conduct.

Content that this list does not name is under the MIT License. The [licensing map](../LICENSING.md)
lists these licenses and gives the credit line for reuse. It has applied since 2026-10-23.

A contribution is licensed under the license that covers the content it changes or adds. Third-party
material keeps its own license, and the [third-party notices](../THIRD_PARTY_NOTICES.md) list it,
including the dataset that the notebooks load.

Alternatives considered:

- One license for all content. It would relicense the code of conduct, which CC BY-SA 4.0 does not
  allow under the MIT License, or it would add a share-alike condition to the code.
- The MIT License for all content except the code of conduct. It leaves figures and prose under a
  software license without a designated credit line.

## Consequences

- The licensing map is the reference for the license of any file.
- A new type of content requires a new row in the map.
- A notebook is one file under the MIT License. Its saved outputs can show third-party material.
- A contribution takes the license of the content it changes.
