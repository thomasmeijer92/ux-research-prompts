# UX Research Prompts

[![Validate skill](https://github.com/thomasmeijer92/ux-research-prompts/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/thomasmeijer92/ux-research-prompts/actions/workflows/validate-skill.yml)

125 UX research recipes for Codex.

This skill helps Codex choose a credible research method, create the actual research artifact, and keep evidence separate from assumptions. It covers 100 core recipes plus 25 recipes for mobile research, quantitative work, research operations, and accessibility.

## What it can do

- Plan discovery, interviews, usability tests, surveys, and mixed-method research.
- Create screeners, interview guides, task scenarios, research briefs, and analysis plans.
- Synthesize notes and transcripts into traceable themes, insights, opportunities, personas, and journeys.
- Audit competitors with dated sources and explicit evidence gaps.
- Turn findings into decision-ready reports, handoffs, workshops, and repository entries.
- Check claims for bias, overreach, missing evidence, privacy risks, and accessibility gaps.

Codex returns the finished artifact by default. Ask for a reusable prompt or template when that's what you need.

## Install

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/thomasmeijer92/ux-research-prompts.git "${CODEX_HOME:-$HOME/.codex}/skills/ux-research-prompts"
```

Start a new Codex task, then call the skill directly:

```text
Use $ux-research-prompts to create a usability test plan for our onboarding flow.
```

You can also invoke it naturally:

```text
Synthesize these interview notes into evidence-backed insights and show what we still can't conclude.
```

## How it works

The skill starts with the product decision, checks what evidence exists, and selects the smallest credible method. It labels the working mode as:

- **Evidence-backed:** based on supplied research data.
- **Desk research:** based on current public sources.
- **Research plan:** research that still needs to happen.
- **Concept or proto artifact:** assumption-based work that still needs validation.

Before returning an artifact, the skill checks that the method fits the decision, claims trace back to evidence, bias and privacy risks are flagged, confidence is stated, and accessibility is covered.

## Research integrity

The workflow explicitly prohibits invented participants, quotes, findings, sample sizes, demographics, sources, benchmarks, and confidence.

It keeps `Observed`, `Inferred`, `Assumed`, and `Needs validation` separate. Qualitative coverage is reported as source counts rather than population percentages. Personas, journeys, competitor claims, and quantitative conclusions stay tied to the evidence available.

AI can organize and challenge research evidence. Real participants and real behavior remain the source of user insight.

## Examples

Each example uses fictional data and shows the evidence mode, decision, artifact, limitations, and next validation step:

- [Mobile onboarding usability test](examples/usability-test-plan.md)
- [Interview synthesis with contradictory evidence](examples/interview-synthesis.md)
- [2-week discovery research plan](examples/discovery-research-plan.md)

## Repository structure

```text
.
├── .github/
│   └── workflows/
│       └── validate-skill.yml
├── SKILL.md
├── agents/
│   └── openai.yaml
├── examples/
│   ├── discovery-research-plan.md
│   ├── interview-synthesis.md
│   └── usability-test-plan.md
├── references/
│   ├── method-selection-guide.md
│   ├── methodology-sources.md
│   ├── prompt-catalog.md
│   └── prompt-library.md
├── scripts/
│   └── validate_skill.py
└── sources/
    └── notion-original-skill.md
```

- [`SKILL.md`](SKILL.md) contains the workflow, routing, guardrails, and output rules.
- [`prompt-catalog.md`](references/prompt-catalog.md) indexes all 125 recipes.
- [`prompt-library.md`](references/prompt-library.md) contains detailed execution patterns.
- [`method-selection-guide.md`](references/method-selection-guide.md) helps choose a method by decision, risk, and appetite.
- [`notion-original-skill.md`](sources/notion-original-skill.md) preserves the original Notion skill snapshot.
- [`validate_skill.py`](scripts/validate_skill.py) checks metadata, catalog coverage, links, example labels, and public-copy rules.

## Source

The public product source is [UX Research Prompts: 100+ AI-Ready Templates for user research](https://contra.com/products/388QJrXC-ux-research-prompts-100-ai-ready-templates-for-user-research), created by [Thomas Meijer](https://github.com/thomasmeijer92).

The product's original Notion material is preserved in this repository as [`notion-original-skill.md`](sources/notion-original-skill.md). The snapshot keeps the source material inspectable without treating the Notion page as the public product URL.

The current Codex skill routes all 125 recipes and adds instructions for checking evidence, protecting privacy, covering accessibility, handling quantitative claims, and planning validation.

## License

This work is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/).

You can copy, share, adapt, and use it commercially. Give appropriate credit to Thomas Meijer, link to the license, and state whether you changed the material. Don't present the original or an adapted version as work you created from scratch, and don't imply endorsement. Don't add legal or technical restrictions that stop others from using the material under the same terms.

Suggested attribution:

> Based on [UX Research Prompts: 100+ AI-Ready Templates for user research](https://contra.com/products/388QJrXC-ux-research-prompts-100-ai-ready-templates-for-user-research) by Thomas Meijer, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Changes: [describe your changes].
