# 0008. Apache License 2.0 for code

**Status:** Accepted **Date:** 2026-11-10

## Context

Decision 0004 licenses each type of content separately: code, scripts, notebooks, and configuration
under the MIT License, original prose and figures under CC BY 4.0, and the code of conduct under CC
BY-SA 4.0. The reasons for licensing by content type still hold.

The MIT License has no express patent license. Contributions can come from people whose origin and
employer are not known in advance. The Developer Certificate of Origin certifies the right to submit
a contribution and gives no patent grant.

The Apache License 2.0 contains an express license from each contributor for the patent claims that
their contribution necessarily infringes (section 3). Under section 5, a contribution submitted to
the work is under the terms of the license unless it states otherwise. The license text has no
copyright line, so the copyright notice needs a place of its own.

At acceptance, no contribution from another person has been merged, and the only release, 0.1.0, is
under the MIT License. A change made later, after outside contributions are merged, would depend on
the terms of each contribution.

## Decision

Each license covers a type of content, not a folder:

- Apache License 2.0: code, scripts, notebooks, and configuration.
- CC BY 4.0: original prose and figures.
- CC BY-SA 4.0: the code of conduct.

Content that this list does not name is under the Apache License 2.0. A notebook is one file. The
Apache License 2.0 covers the notebook, except the third-party material in its saved outputs.

A contribution is licensed under the license that covers the content it changes or adds. Third-party
material keeps its own license, and the [third-party notices](../THIRD_PARTY_NOTICES.md) list it,
including the dataset that the notebooks load.

The file `NOTICE` holds the copyright notice. The [licensing map](../LICENSING.md) lists these
licenses and gives the credit line for reuse.

The change applies from the commit that merges this record. Release 0.1.0 stays under the MIT
License.

Alternatives considered:

- Keep the MIT License. It is shorter and carries no patent license.
- The MIT License or the Apache License 2.0, at the choice of the recipient. It adds a choice for
  every recipient and a second license file. The patent license applies only to a recipient who
  chooses the Apache License 2.0.

## Consequences

- The licensing map is the reference for the license of any file.
- A reuser follows the terms of the Apache License 2.0, which include keeping the license text and
  the `NOTICE` file.
- The patent license covers the patent claims that a contribution necessarily infringes, alone or
  combined with the work. It is not a general patent clearance and gives no guarantee against claims
  by third parties. The sign-off of the Developer Certificate of Origin remains a statement by the
  contributor.
- A new type of content requires a new row in the map.
- The license of the dataset that the notebooks load does not change. It is third-party material.
