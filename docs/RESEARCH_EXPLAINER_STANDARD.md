# Research Explainer Standard

Use this standard when a paper is important enough for a README fold, current Reading Path, anchor/category argument, or high-value research note.

The standard fixes the **reasoning sequence**, not the sentence template.

## 1. Research delta

State the smallest change that makes the paper worth opening.

Preferred internal form:

`previous design → changed variable/control boundary → consequence`

Do not write `proposes a novel framework` or a generic summary of all modules.

## 2. Problem that survives the closest baseline

Explain what still fails under the strongest reasonable existing design. A motivation is weak if the failure disappears under a competent raw-state, matched-budget, or simpler control.

## 3. Mechanism / control flow

Describe what actually executes. Prefer an observable flow such as:

`history → evidence units → access policy → retrieved evidence → consumer-state reconstruction → action`

over a list of module names.

For Agent Memory, locate the change when useful along:

`write → organize → access/admit → consumer state → update/forget → governance`

## 4. Closest comparison

Always answer:

- What is the closest meaningful alternative?
- What is actually held fixed?
- What still changes together?

If several stages move together, interpret the result as evidence for the package before attributing it to one component.

## 5. Decisive evidence

Select only the 1–3 results or ablations that should materially update a researcher’s belief. Include a negative result when it changes the boundary of the claim.

Do not reproduce the whole results table.

## 6. What remains unproven

Name the strongest condition that would weaken the interpretation:

- unmatched retrieval/evidence/token/latency budget;
- stronger raw-state or alternative-representation control;
- simulator-to-real-user transfer;
- provenance/conflict/drift failure;
- lifecycle construction or maintenance cost;
- bundled ablation that does not isolate the claimed mechanism.

This section should be specific enough to imply a decisive follow-up experiment.

## 7. Field-map consequence

Explain which existing research question changes. A paper does not deserve a new field-map node merely because it is recent.

## 8. Related reading

Choose 2–4 works for **contrast or continuation**, not citation completeness. Each link should help answer `compared to what?` or `what should I read next?`.

## README compression

The README fold is not this note shortened mechanically. Compress the same reasoning into 2–4 natural paragraphs that a reader can understand in roughly 60–90 seconds. Preserve the closest comparison, decisive evidence, and caveat; remove implementation detail recoverable from the note.

## Epistemic labels in prose

Keep three levels distinct:

- paper-reported fact;
- curator interpretation;
- open hypothesis / next decisive test.

The reader should not need to infer which level a sentence belongs to.
