# Method Selection Guide

Use this guide when the method is unclear, the user asks what research to run, or time, access, sample, or risk constraints matter.

## Start With the Decision

Choose a method by the decision it can change, not by the artifact the team expects.

| Decision or question | Default method | Useful evidence | Avoid |
|---|---|---|---|
| What problem is worth solving? | Stakeholder alignment plus generative interviews or contextual inquiry | recent stories, workarounds, support and behavioral data | treating stakeholder beliefs as user evidence |
| Who experiences it, when, and why? | Generative interviews, diary study, or contextual inquiry | past behavior in real context | feature wish lists and future-intent questions |
| Why do people switch, adopt, or leave? | Recent-event JTBD interviews plus behavioral or churn data | decision timelines, alternatives, anxieties, trade-offs | interviewing people without a relevant recent event |
| Can people find or complete something? | Moderated or unmoderated usability testing | task behavior, success, errors, time, confidence | teaching the interface during the task |
| Does the information architecture match expectations? | Open/closed card sorting plus tree testing | groupings, labels, findability paths | using card sorting as proof of final navigation |
| Which design performs better? | Comparative usability test for explanation; controlled experiment for causal effect | behavioral task data or randomized outcome data | calling preference feedback an A/B test |
| How common is a known pattern? | Survey or behavioral analytics with an explicit sampling plan | representative responses or logged behavior | using surveys to discover unknown problems |
| How usable is the experience over time? | Benchmark study with stable tasks and measures | success, time, errors, ease, standardized scale | changing tasks or protocol between waves |
| Where should the roadmap focus? | Evidence synthesis and opportunity framing | user evidence, prevalence/severity data, strategy, feasibility | prioritizing from competitor gaps alone |
| What do competitors currently offer? | Verified desk research and structured UX audit | dated source links, captured flows, reviews | unverified model memory or assuming features equal user value |
| How should findings drive a decision? | Decision-ready report, workshop, or handoff | traceable findings, implications, recommendations, open questions | leading with research process or invented certainty |

## Select by Stage

- **Discovery:** stakeholder interviews, evidence review, competitive scan, assumption mapping.
- **Generative:** user interviews, JTBD, contextual inquiry, diary study.
- **Evaluative:** usability testing, concept testing, tree testing, accessibility testing.
- **Quantitative:** survey, analytics, benchmark, controlled experiment.
- **Synthesis/modeling:** coding, affinity mapping, themes, mental models, personas, journeys.
- **Communication/operations:** report, repository entry, research intake, participant panel, impact tracking.

Combine methods only when each answers a distinct question. A common mixed-method pattern is analytics for `what/where`, qualitative research for `why`, and an experiment for `whether a change caused an outcome`.

## Match Method to Risk

| Decision risk | Minimum credible approach |
|---|---|
| Low and reversible | expert review, evidence scan, or 3-5 lightweight sessions |
| Moderate product impact | multiple sources, relevant participants, explicit counter-evidence, follow-up validation |
| High, costly, regulated, safety-related, or exclusionary | research specialist involvement, representative access needs, formal protocol, privacy/ethics review, and quantitative power or sampling support where applicable |

Do not let urgency lower claim quality. Narrow the question or confidence instead.

## Use Sample Sizes as Starting Points

Sample depends on heterogeneity, study design, risk, incidence, and the claim being made.

- Stakeholder interviews: often 3-6 roles to expose alignment and assumptions.
- Generative interviews: often start with 5-8 people per meaningfully different behavioral segment, then assess whether new sessions still change the model.
- Moderated usability: 5-8 participants per distinct audience or flow can expose obvious issues; add participants for segment comparisons, accessibility needs, or higher-confidence estimates.
- Diary studies: choose enough participants and duration to capture the target behavior's natural frequency and context.
- Surveys: calculate from the intended estimate, precision, confidence, population, expected response rate, and comparison needs.
- Experiments: use a power analysis based on baseline, minimum detectable effect, variance, allocation, and stopping rule.
- Accessibility research: recruit for the actual combinations of disability, assistive technology, platform, and task that matter; do not treat disability as one segment.

Never claim saturation, representativeness, significance, or benchmark validity solely from these heuristics.

## Work Within Appetite

### 30-60 minutes

- Convert a product decision into research questions.
- Audit assumptions and existing evidence.
- Draft a screener, interview guide, usability script, or survey critique.
- Set up a competitive evidence matrix without filling unverified claims.

### 0.5-2 days

- Synthesize supplied interviews, tickets, reviews, or analytics.
- Run a small internal stakeholder round.
- Conduct a verified competitor scan.
- Pilot a research guide or survey with 1-2 people.

### 1-2 weeks

- Conduct a focused interview or usability round.
- Run a short diary study for frequent behavior.
- Create an evidence-backed journey or behavioral segmentation.
- Produce a decision-ready report and validation plan.

If the work exceeds its appetite, narrow the decision, audience, flow, or evidence claim before adding methods.

## Check Method Failure Modes

- Interviews do not predict behavior reliably; anchor on real past events.
- Focus groups reveal social discussion, not private prevalence or unbiased individual preference.
- Surveys quantify the questions and sampling frame chosen; poor questions scale bias.
- Usability tests diagnose interaction problems; they do not validate market demand.
- Competitive analysis shows available patterns and positioning; it does not prove user need.
- App-store and support data overrepresent motivated, frustrated, or engaged users.
- Personas and journeys synthesize evidence; they are not evidence themselves.
- AI-assisted coding accelerates organization but requires human review of code definitions, ambiguous excerpts, minority signals, and source traceability.
- Controlled experiments estimate causal effects only when assignment, instrumentation, exposure, and analysis are sound.

## Recommend the Next Step

End method recommendations with:

1. the decision to make;
2. the minimum method and why;
3. required participants or sources;
4. what the method cannot establish;
5. the decision rule or next validation step.
