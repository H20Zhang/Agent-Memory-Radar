# Research Compactions

Daily curation optimizes for **recall and provenance**. Compactions optimize for **attention at different time scales**.

## Reader-facing windows

The repository landing page keeps compactions useful without growing forever:

- **Weekly — last 1 month:** show every available weekly compaction from the most recent ~31 days.
- **Monthly — last 1 quarter:** show every available monthly compaction from the most recent 3 calendar months.
- **Yearly — all available years:** keep the full list of yearly research maps because the list grows slowly.

Older weekly and monthly compactions remain available in their archive directories even after they fall off the README.

## Weekly

Weekly files live under [`weekly/`](weekly/) using ISO week names such as `2026-W32.md`.

A weekly compaction should not concatenate daily summaries. It should answer:

- What changed in the agent-memory design space this week?
- Which 3–5 papers are actually worth reading, and why?
- What tensions or contradictory design choices appeared?
- Which hidden assumptions or missing evaluations became visible?

## Monthly

Monthly files live under [`monthly/`](monthly/) using names such as `2026-08.md`.

A monthly compaction should synthesize the weekly reports plus canonical paper records into a research map: dominant shifts, strongest papers, emerging/declining themes, unresolved trade-offs, and what evidence would change the current view. During an active month the file may be rolling; after month-end it becomes the final monthly snapshot.

## Yearly

Yearly files live under [`yearly/`](yearly/) using names such as `2026.md`.

A yearly compaction is the highest-level research map. It should synthesize the year's finalized monthly compactions and canonical papers into:

- the major design-space shifts that survived beyond a few weeks;
- the strongest / field-shaping papers and benchmarks;
- themes that strengthened, weakened, or disappeared;
- durable trade-offs and unresolved research questions;
- major corrections to earlier monthly interpretations;
- what evidence would falsify the resulting yearly thesis.

A current-year file may be rolling, but **coverage must be stated explicitly**. Do not call it a full-year view unless the whole year has been covered or systematically backfilled.

## Raw daily logs

Daily run logs are intentionally demoted to archival provenance under `runs/daily/YYYY/MM/DD.md`. They are not the primary browsing interface.
