# Visual Curation Policy

Agent Memory Radar uses visuals as **research compression**, not decoration. The goal is to let a researcher understand the mechanism, delta, evidence, and caveat faster than by reading prose alone.

## When to generate a figure

- **Required:** papers with importance >= 4/5.
- **Required:** weekly, monthly, and yearly compactions.
- **Optional:** lower-importance papers whose mechanism is unusually hard to understand from text.
- **Skip:** incremental papers where a figure would mostly restate the abstract.

## Rendering policy

Final researcher-facing visuals should be generated with **GPT Image** rather than Mermaid-first diagrams. The visual style should remain consistent with the repository: clean GitHub-native research cards, white background, restrained blue/teal accents, strong typography, high information density, and minimal decorative imagery.

Generated figures are curator interpretations, not reproductions of the paper's original figures. Each figure should say so when ambiguity is possible.

### Invocation isolation

While per-paper visual backfill exists, generate **exactly one named paper per GPT Image invocation**. A per-paper render must stay inside that paper's grounded brief: mechanism, memory/data/control flow, comparison, evidence, and limitation.

Do **not** render repository dashboards, status/QC UI, paper-count summaries, multi-paper collages, or maintenance metadata as a substitute for a paper explainer. If a render introduces fabricated paper IDs, dates, publication status, benchmark numbers, or repository state, Visual QA must reject it rather than crop or salvage it.

Only after required per-paper backfill is healthy should compaction maps be generated, one named weekly/monthly/yearly synthesis per invocation.

## Paper figure: required information

A useful paper figure must communicate concrete content from the full paper:

1. **Problem** — what specifically fails in the prior design.
2. **Core mechanism** — the actual data/control flow, not a generic agent-memory pipeline.
3. **Memory design** — what is written, how it is organized, how it is read, and how it changes or is forgotten.
4. **Compared to what** — the closest prior design point and the real technical delta.
5. **Evidence** — the strongest experiment or ablation supporting the interpretation; use exact numbers only when verified.
6. **Why it matters + limitation** — one consequential takeaway and one evidence-backed caveat.

If the paper does not support one of these fields, mark it unknown or omit it rather than inventing content.

## Weekly research map

The weekly figure is a cross-paper synthesis. It must show:

- 2–4 design-space shifts supported by multiple papers, or explicitly label a single-paper observation as an **early signal**;
- representative papers for each shift;
- a `so what` statement for each shift;
- papers worth reading, ranked independently from relevance;
- open tensions and what evidence to watch next.

It must not be a collage of paper summaries.

## Monthly design-space map

The monthly figure should show movement rather than volume:

- older/default design assumptions -> current movement;
- strongest signals and the papers supporting them;
- persistent vs weakening themes;
- unresolved trade-offs;
- concrete falsification conditions that would weaken the curator's current interpretation.

## Yearly research map

The yearly figure is the most compressed visual layer. It should show only signals that survived beyond a short-lived weekly spike:

- the year's durable design-space transitions;
- the strongest / field-shaping papers or benchmarks supporting each transition;
- themes that strengthened, weakened, or disappeared over the year;
- durable trade-offs and open research gaps;
- important corrections where an earlier monthly narrative did not survive later evidence;
- 2–4 concrete conditions that would falsify the final yearly thesis.

If the current-year coverage is partial, the visual must state the coverage window prominently and must not imply a full-year reconstruction.

## Iterative multi-role review

Visual generation is iterative, not one-shot. For every required visual:

1. **Research Analyst** drafts the factual visual brief from full-paper evidence.
2. **Skeptical Reviewer** challenges unsupported claims, vague boxes, and misleading comparisons.
3. **Visual Editor** removes generic content and optimizes hierarchy and information density.
4. **Image Generator** renders the figure from the revised brief.
5. **Visual QA Reviewer** inspects the rendered image for text errors, empty visual metaphors, claim/evidence mismatch, and readability.
6. If QA finds a material issue, revise the brief and regenerate. Prefer 2–3 strong iterations over accepting the first image.

A visual is publishable only when it contains paper-specific information that materially reduces reading effort.
