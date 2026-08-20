# Operational Run Policy

## No public operational run logs

This repository publishes no Daily Agent run logs. Accepted outcomes are atomically projected into canonical records, paired deep notes, the Latest Timeline, rolling periods, due closed-period digests, and the evidence-gated Field Map. The corresponding commit preserves the public decision history without creating a second free-form operational surface.

Private scouting, candidate states, lane failures, retry triggers, dissent, and validation traces live only in the git-ignored `.radar-private/runs/<run_id>.json` path or ephemeral Agent memory. They must never be committed elsewhere.

The validator rejects every file under `runs/daily/` and any future configured public operational-run path. It proves the absence of public candidate or workflow inventory mechanically; it does not attempt to classify natural-language Markdown. Historical daily logs removed by this policy remain recoverable from Git history.

Reader-facing history belongs in:

- [`../README.md`](../README.md) and [`../digests/`](../digests/) for time-first synthesis;
- [`../data/papers/`](../data/papers/) for canonical identity and provenance;
- [`../papers/`](../papers/) for evidence-grounded paired deep notes;
- Git history for atomic publication and correction provenance.
