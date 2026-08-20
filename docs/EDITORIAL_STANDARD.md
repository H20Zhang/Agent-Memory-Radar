# Research Radar Editorial Standard

This file is the enforceable prose contract for reader-facing Radar content. It applies to Chinese and English README surfaces, Research Library pages, high-value paper notes, category arguments, and public compactions.

## Research reasoning before prose

A high-value paper explanation should settle these questions before drafting:

1. **Research delta** — `previous design → changed variable → consequence`.
2. **Problem** — what still fails under the closest reasonable prior design?
3. **Mechanism** — what actually happens in the execution/data/control flow?
4. **Closest comparison** — what is held fixed, and what still changes together?
5. **Decisive evidence** — which 1–3 results should update belief?
6. **What remains unproven** — strongest alternative explanation, unmatched budget, or unsupported attribution.
7. **Field-map consequence** — which lifecycle boundary or research question changes?

For Agent Memory, use the lifecycle lens only when it adds information: `write / organize / access / consumer state / update-forget / governance`.

## Chinese-first bilingual rule

`README.md` is the default Chinese surface. `README.en.md` is a complete English counterpart. Reader-facing semantic claims must remain aligned across languages, but prose should be rewritten naturally rather than translated sentence by sentence.

Keep canonical paper titles, benchmark/dataset names, model names, metrics, protocol names, and standard technical terms in English when translation would hurt literature search or precision.

Chinese prose must still use Chinese sentence structure. Keep an English name or acronym as the subject or object when it is the precise term, but express ordinary actions, comparisons, and transitions with Chinese verbs and clauses. Avoid sentences made mostly of English noun phrases connected only by `的`、`与`、`在`.

## Preferred prose

- Put the claim in the first sentence of the paragraph.
- Use active voice and concrete system objects/operations.
- Compare before evaluating: say what changed relative to a baseline before calling it important.
- Use numbers only when they change the interpretation.
- Preserve negative results and budget mismatches.
- State attribution limits directly: `这个实验更支持整套 package，而不是单独证明 X` / `the experiment supports the package more strongly than X`.
- One paragraph should advance one research idea.

## Public entry and navigation style

- Treat README and Research Library pages as indexes, not method manifestos. Open with the collection's subject and direct navigation; do not add thesis blocks about how the Radar thinks or descriptions of its own workflow.
- Navigation labels name destinations, not estimated reading times. Do not package routes as `30 sec / 5 min / 15 min` or put duration estimates in fold summaries.
- Do not repeat the same synthesis as an introduction, table summary, and takeaway. If a table already carries the comparison, add prose only when it contributes a new inference.
- Avoid identical labels on every entry, such as `Research delta` or `Takeaway`, when the sentence can state the claim directly.
- Preserve folds that carry mechanism, evidence, or caveats. Give each fold a short description of its contents rather than a reading-time promise.

## AI-house-style patterns to avoid

Do not make every note sound as if it came from one template. Watch for repeated skeletons across nearby files, especially:

- `真正重要的不是 X，而是 Y` / `the important delta is not X, but Y`;
- `值得注意的是…`, `此外…`, `总的来说…` when they do not add reasoning;
- repeated `this matters because…`, `the strongest result is…`, `the key insight is…` openings;
- generic praise such as `novel`, `robust`, `powerful`, `significant`, `重要`, `强大` without evidence or comparison;
- forced three-part symmetry used for rhythm rather than analysis;
- abstract nouns (`framework`, `paradigm`, `landscape`, `capability`) where an operation can be named;
- conclusion paragraphs that merely restate the opening.

The goal is not to ban words. Detect **pattern density** and rewrite only when the prose becomes generic or repetitive.

## README fold contract

A README fold is a causal explanation, not a shortened paper note. It should naturally cover the surviving problem, actual change, mechanism/control flow, closest comparison, decisive evidence, and strongest caveat. Merge these into 2–4 natural paragraphs when possible; do not force six mini-headings.

## Epistemic language

Distinguish:

- **Paper-reported fact:** `The paper reports…` / `论文报告…`.
- **Curator interpretation:** `This supports… more strongly than…` / `这更支持…而不是…`.
- **Open hypothesis:** `The next decisive test is…` / `下一步最有判别力的实验是…`.

Do not silently promote interpretation into fact.
