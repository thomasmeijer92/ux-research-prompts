---
name: ux-research-prompts
description: Plan and execute AI-assisted UX research workflows, including discovery, stakeholder and user interviews, screeners, usability testing, transcript synthesis, personas, journey maps, JTBD, competitive research, surveys, research metrics, accessibility research, research operations, and stakeholder reporting. Use when the user mentions UX or user research, discovery or generative research, interview guides, prototype or usability testing, questionnaires or surveys, research synthesis, personas, journey maps, jobs to be done, competitor UX analysis, research repositories, or communicating findings.
---

# UX Research Prompts

Use the 125-recipe catalog as a routing system, not as a reason to return generic meta-prompts. Complete the requested research task directly unless the user explicitly asks for a reusable AI prompt.

## Run the Workflow

1. State the product decision the research must inform.
2. Inventory the available evidence and classify the working mode.
3. Select the smallest credible method for the decision, constraints, and risk.
4. Load only the relevant reference file.
5. Produce the requested plan, script, analysis, model, or report.
6. Run the quality gate and recommend the smallest next validation step.

Do not stop for missing context that can be represented safely as a labeled placeholder or assumption. Ask only when the missing answer would materially change the method, participant safety, external scope, or output.

## Classify the Evidence Mode

Use one of these labels in substantive outputs:

- **Evidence-backed:** grounded in supplied notes, transcripts, analytics, recordings, or verified sources.
- **Desk research:** grounded in current public sources; cite them and record the access date.
- **Research plan:** proposes future research; contains no user findings yet.
- **Concept/proto artifact:** assumption-based and explicitly not validated.

Never blend these modes silently. Label mixed outputs at the claim or section level.

## Route the Request

| Need | Read |
|---|---|
| Decide what research to run, estimate effort, or choose a sample approach | `references/method-selection-guide.md` |
| Find a recipe by name, phase, or prompt ID | `references/prompt-catalog.md` |
| Draft or execute a common research workflow | `references/prompt-library.md` |
| Explain methodology lineage, citations, or rigor caveats | `references/methodology-sources.md` |

For ambiguous requests, read the method-selection guide first. For a named artifact such as a screener, JTBD guide, journey map, survey, accessibility plan, or research repository, use the catalog to confirm the matching recipe, then apply the closest detailed pattern from the prompt library.

## Choose the Deliverable

- If asked to **research, analyze, synthesize, create, or prepare**, return the finished artifact.
- If asked for a **prompt, template, or reusable instruction**, return a copy-ready prompt with variables.
- If raw evidence is supplied, preserve traceability from each claim to its source.
- If current competitors, prices, reviews, regulations, platform behavior, or market facts matter, verify them before analysis.

## Protect Research Integrity

- Do not invent participants, quotes, observations, counts, demographics, sources, benchmarks, findings, or confidence.
- Separate `Observed`, `Inferred`, `Assumed`, and `Needs validation`.
- Use past-behavior and recent-event questions before opinions or future intent.
- Keep questions neutral, single-purpose, understandable, and free of the desired answer.
- Preserve minority, contradictory, and negative evidence; do not force consensus.
- Do not infer prevalence from qualitative data. Report source coverage as counts, not percentages, unless the denominator and sampling justify percentages.
- Treat sample-size numbers as planning heuristics, never guarantees of saturation or validity.
- Create personas and journey maps only from evidence, or label them `proto-` and list assumptions.
- Never fabricate persona quotes. Use anonymized verbatim evidence or omit the quote.
- Separate user problems and opportunities from proposed solutions.
- For surveys, avoid double-barreled, leading, loaded, exhaustive-looking, and overlapping answer options.
- For experiments and quantitative studies, define the primary outcome, unit of analysis, guardrails, decision rule, and analysis plan before results.
- Minimize personal data. Anonymize participant identifiers and flag consent, recording, retention, incentive, and accessibility considerations when relevant.
- Do not diagnose disabilities or sensitive traits from behavior. Include people with relevant access needs in research when accessibility is in scope.
- Position AI as an organizer and challenger of evidence, not a participant substitute.

## Apply the Quality Gate

Before finalizing, check:

1. **Decision fit:** Can the output change a real product or design decision?
2. **Evidence traceability:** Can each finding be traced to supplied or cited material?
3. **Bias control:** Are questions neutral and are alternative explanations visible?
4. **Coverage:** Are relevant segments, contexts, edge cases, and contradictory signals represented?
5. **Proportional confidence:** Does the wording match the quality and quantity of evidence?
6. **Actionability:** Are implications separate from recommendations, with owners omitted unless supplied or requested?
7. **Ethics and privacy:** Are consent, data minimization, anonymity, accessibility, and participant burden handled?

## Shape the Output

For plans and scripts, use:

```markdown
## Recommended approach
[method, decision fit, evidence mode, and constraints]

## Research artifact
[ready-to-use plan, screener, guide, tasks, questions, or analysis]

## Assumptions and inputs
[known, assumed, missing, and excluded]

## Quality and validation
[bias risks, evidence limits, and smallest next check]
```

For synthesis, use an evidence table with:

`Claim | Type | Evidence/source | Coverage | Counter-evidence | Confidence | Implication | Validation`

For reusable prompts, use:

```text
Context: [product, audience, market, stage]
Decision: [what this research must inform]
Evidence mode: [evidence-backed, desk research, research plan, or concept/proto]
Source material: [notes, transcripts, analytics, recordings, or links]
Constraints: [time, budget, access, sample, privacy, accessibility]
Task: [artifact to create]
Output: [format and level of detail]
Rules: Separate observed, inferred, assumed, and needs validation. Do not invent evidence.
```

## Keep Source Claims Accurate

The canonical Notion pack contains 100 core prompts plus 25 mobile, quantitative, research-operations, and accessibility prompts as of February 2026. The local catalog preserves all 125 recipe names and routing. Detailed local templates are intentionally compact and strengthened with evidence, privacy, and validation rules; consult the Notion source only when exact source wording or later updates matter.
