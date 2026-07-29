# Prompt Library

Use these as reusable execution patterns. Replace bracketed variables, preserve source traceability, and return the finished artifact unless the user explicitly asks for a copy-ready prompt.

## Discovery

### Stakeholder Interview Script

```text
Create a stakeholder interview script for [product/project].
Goal: uncover business goals, user assumptions, constraints, risks, and success metrics.
Audience: [stakeholder roles].
Output: 10-12 open-ended questions grouped by goals, users, constraints, metrics, and risks.
Rules: avoid leading questions; include follow-up probes; mark assumptions that need user validation.
```

### Problem Framing

```text
Turn this project context into a research-ready problem frame:
[context]
Output:
1. Problem statement
2. Target users and exclusions
3. Key assumptions
4. Research questions
5. Hypotheses
6. Smallest validation plan
Rules: separate known facts from assumptions.
```

### Success Metrics

```text
Help define research and product success metrics for [product].
Inputs: [business goal], [user goal], [current funnel or behavior if known].
Output: leading indicators, lagging indicators, qualitative signals, and what not to measure.
```

## Interviews

### Research Plan

```text
Create a UX research plan for [decision].
Context: [product, audience, stage].
Constraints: [timeline, budget, access].
Output: decision, research goal, questions, method rationale, participant criteria, sample approach, protocol outline, analysis plan, consent/privacy needs, risks, and deliverables.
Rules: state what the method can and cannot establish; treat sample numbers as planning assumptions.
```

### Participant Screener

```text
Create a participant screener for [target user].
Research goal: [goal].
Must include/exclude: [criteria].
Output: screener questions, accepted/rejected answer patterns, quotas if justified, privacy note, and bias risks.
Rules: avoid revealing the desired participant profile; collect only necessary data; do not create discriminatory criteria unrelated to the study.
```

### Interview Guide

```text
Create a semi-structured interview guide for [topic].
Focus on past behavior, recent examples, workarounds, constraints, motivations, and language users naturally use.
Output: opening and consent script, warm-up, core questions, probes, wrap-up, and interviewer notes.
Rules: avoid asking users to design the solution; include recording consent only when recording is planned.
```

### JTBD Interview

```text
Create a jobs-to-be-done interview guide for people who recently [switched/bought/tried/abandoned].
Output questions for: first thought, passive looking, active looking, decision moment, anxieties, tradeoffs, alternatives, desired progress, and post-decision satisfaction.
Rules: anchor every question in a real recent event.
```

## Synthesis

### Transcript Analysis

```text
Analyze these research notes/transcripts:
[notes]
Output:
1. Observed behaviors
2. User goals
3. Pain points
4. Workarounds
5. Repeated language
6. Contradictions and minority signals
7. Candidate themes
8. Evidence strength
For every item, include participant/source ID and a short evidence excerpt or note reference.
Rules: do not invent or clean up quotes; label weak evidence and redact direct identifiers.
```

### Theme Extraction

```text
Cluster these notes into themes:
[notes]
Output a table with theme, supporting evidence, participant/source count, confidence, design implication, and validation needed.
Rules: keep minority/contradictory signals visible.
```

### Insight Statement

```text
Convert these patterns into research insight statements:
[patterns]
Format each as: Users need [need] because [evidence], which means [design/product implication].
Also include confidence, source coverage, and what would disconfirm the insight.
```

### Opportunity Framing

```text
Turn these research findings into opportunity statements:
[findings]
Output: opportunity, affected user segment, evidence, expected impact, risk, smallest experiment, and priority.
Rules: keep solution ideas separate from opportunities.
```

## Personas, Journeys, and Mental Models

### Persona From Data

```text
Create behavior-based personas from this research data:
[data]
Output: behavioral variables, persona groups, goals, triggers, anxieties, constraints, product implications, source coverage, counter-evidence, and confidence.
Rules: do not invent demographics, names, photos, biographies, or quotes. If evidence is insufficient, create explicitly labeled proto-personas with validation questions.
```

### Journey Map

```text
Create a journey map for [user/job] using this evidence:
[data]
Stages: [optional stages].
Output: stage, user goal, actions, touchpoints, emotions, pain points, evidence/source, confidence, and opportunities.
Rules: mark assumed stages and missing evidence; do not smooth over alternate paths or failure states.
```

### Empathy Map

```text
Create an empathy map from these notes:
[notes]
Output: says, thinks, does, feels, pains, gains, evidence strength, and gaps.
Rules: distinguish direct user language from inference.
```

## Competitive Intelligence

### Competitor Identification

```text
Identify direct, indirect, and adjacent competitors for [product/category].
Output: competitor type, target user, core promise, key features, pricing/packaging if known, positioning, dated source links, and unknowns.
Rules: verify current facts from primary sources before analysis; distinguish direct evidence from interpretation.
```

### Feature Matrix

```text
Create a competitive feature matrix for [product] against [competitors].
Feature areas: [areas].
Output: dated source matrix, gaps, possible table stakes, possible differentiators, evidence quality, and research questions to validate demand.
Rules: a competitor feature is not evidence of user need; use `Unknown` instead of guessing.
```

### Battle Card

```text
Create a battle card for [competitor].
Output: competitor summary, best-fit customers, strengths, weaknesses, likely objections, product advantages, proof available, proof needed, and talk tracks.
Rules: keep claims evidence-based, verify current competitor facts, and avoid fabricated or manipulative “landmines.”
```

## Reporting and Communication

### Executive Summary

```text
Write an executive UX research summary from these findings:
[findings]
Output: decision needed, top findings, evidence base, recommendation, risks, and next step.
Keep it concise and avoid methodology theatre.
```

### Research Deck Outline

```text
Create a stakeholder deck outline for this research:
[findings/context]
Output: slide-by-slide story arc with title, purpose, evidence, visual suggestion, and speaker note.
Rules: lead with the decision and implications, not the process.
```

### Design Handoff

```text
Turn these research findings into design recommendations:
[findings]
Output: recommendation, rationale, user evidence, affected screens/flows, priority, risk, and validation plan.
```

## Mobile App Research

### Onboarding

```text
Create a research plan for a mobile app onboarding flow.
Context: [app, target user, activation goal].
Output: assumptions, interview questions, usability tasks, metrics, edge cases, and recommended prototype fidelity.
```

### Push Notifications

```text
Create a research guide for push notification preferences in [app].
Cover: trigger value, timing, frequency, wording, opt-in moment, user control, and failure modes.
Rules: include questions about past notification behavior, not only stated preferences.
```

### Gestures and Touch Patterns

```text
Create a usability test script for mobile gestures in [flow].
Output: tasks, observation checklist, success criteria, confusion signals, accessibility concerns, and debrief questions.
```

### Offline and Error States

```text
Create a research checklist for offline, slow network, and error states in [mobile app].
Output: contexts of use, risk scenarios, user expectations, copy questions, recovery flows, and validation tasks.
```

### App Store Review Mining

```text
Analyze these App Store reviews for product research:
[reviews]
Output: themes, severity, user jobs, delight signals, churn risks, feature requests, quote candidates, and follow-up research questions.
Rules: reviews are biased feedback, not representative user research.
```

## Evaluative and Usability Research

### Usability Test Plan

```text
Create a usability test plan for [flow/prototype].
Decision: [what the team will decide from the study].
Audience and context: [participants, device, environment, access needs].
Prototype fidelity and known limitations: [details].
Output:
1. Research questions
2. Participant criteria and sample rationale
3. Realistic task scenarios without UI instructions
4. Observation checklist
5. Task success, critical error, time, confidence, and ease measures
6. Neutral follow-up questions
7. Facilitation and consent notes
8. Analysis and severity rubric
Rules: do not reveal the expected path; distinguish usability problems from preferences; state what this sample cannot establish.
```

### Task Scenario Rewriter

```text
Review these usability tasks:
[tasks]
For each task:
1. Identify clues, leading language, hidden prerequisites, and unrealistic setup
2. Rewrite it around a plausible user goal and context
3. Define success, partial success, failure, and critical errors
4. Note prototype limitations or data setup required
5. Add one neutral post-task question
Rules: do not name controls, labels, or navigation paths being tested.
```

### Usability Findings and Severity

```text
Analyze these usability session notes:
[notes with participant/source IDs]
Output one row per issue:
Issue | Evidence/source | Participants affected | Task impact | Recovery | Frequency in this sample | Severity | Confidence | Recommendation hypothesis | Validation
Rules: preserve successful behavior and contradictions; do not convert small-sample frequency into population prevalence; separate observed issue from proposed fix.
```

### Card Sort and Tree Test Plan

```text
Create an information-architecture research plan for [content/navigation].
Decision: [labels, grouping, hierarchy, or findability].
Inputs: [current structure, candidate labels, target users].
Output: recommended card-sort and/or tree-test method, participant criteria, items/tasks, success measures, analysis plan, and decision rule.
Rules: use card sorting for mental grouping and tree testing for findability; do not treat either as proof of final interaction design.
```

## Quantitative Research

### Survey Plan and Draft

```text
Design a survey for [decision].
Target population and sampling frame: [who and how reached].
Constructs to measure: [known concepts].
Constraints: [length, channels, languages, privacy].
Output:
1. Research questions and constructs
2. Sampling and response-rate assumptions
3. Screener and survey flow
4. Neutral questions with mutually exclusive, collectively appropriate response options
5. Branching and randomization
6. Pilot and cognitive-testing plan
7. Analysis plan tied to each question
8. Limitations and claims the survey cannot support
Rules: avoid double-barreled, leading, loaded, ambiguous, and forced-response questions; include `Prefer not to say` when appropriate.
```

### Analytics-to-Research Bridge

```text
Turn these analytics observations into a research plan:
[metric definitions, time range, segments, funnel or event data]
Output:
1. What the data directly shows
2. Instrumentation or denominator checks
3. Plausible explanations, labeled as hypotheses
4. Qualitative questions and participant criteria
5. Recommended interviews or usability tasks
6. How qualitative findings will reconnect to the metrics
Rules: do not infer intent or causality from behavioral correlation alone.
```

### Experiment Plan

```text
Create an experiment plan for [change].
Decision and hypothesis: [details].
Baseline and traffic: [if known].
Output:
1. Testable hypothesis and causal estimand
2. Unit of assignment and unit of analysis
3. Primary outcome, guardrails, and diagnostic metrics
4. Minimum detectable effect and power-analysis inputs
5. Exposure, eligibility, duration, and stopping rule
6. Instrumentation and sample-ratio checks
7. Segment and multiple-comparison policy
8. Qualitative companion research
9. Decision rule and risks
Rules: do not invent sample size, effect, significance, or runtime when inputs are missing.
```

### Benchmark Study

```text
Design a repeatable usability benchmark for [product/flow].
Output: fixed tasks, participant definition, environment, success/error/time measures, questionnaire choice, protocol, baseline plan, reporting table, and rerun cadence.
Rules: separate descriptive benchmarks from external norms; document every protocol change between waves.
```

## Accessibility and Inclusive Research

### Accessibility Research Plan

```text
Create an accessibility research plan for [product/flow].
Decision: [what must improve].
Known platforms, standards, and assistive technologies: [details].
Output:
1. Relevant access needs and exclusion risks
2. Standards/expert-review scope
3. Participant criteria based on lived experience and actual technology use
4. Accessible recruitment, consent, scheduling, and incentive plan
5. Realistic tasks and observation protocol
6. Environment and assistive-technology setup
7. Issue severity and prioritization
8. Remediation validation plan
Rules: do not simulate disability as a replacement for participants; do not infer diagnoses; let participants control disclosure and accommodations.
```

### Inclusive Edge-Case Review

```text
Review [flow/concept] for exclusion risks.
Consider permanent, temporary, and situational constraints across vision, hearing, mobility, cognition, language, connectivity, device, privacy, and stress.
Output: scenario, affected people/context, likely barrier, current evidence, design question, research method, and priority.
Rules: treat this as hypothesis generation until validated with relevant people.
```

## Research Operations

### Research Repository Design

```text
Design a research repository for [team/product].
Inputs: current tools, study volume, users of the repository, privacy constraints, and maintenance capacity.
Output:
1. Minimal taxonomy and study template
2. Claim-to-evidence traceability model
3. Participant anonymization and access controls
4. Tags and retrieval examples
5. Retention, archive, ownership, and review cadence
6. Migration and adoption plan
Rules: optimize for findability and maintenance; do not store unnecessary participant identifiers.
```

### Research Intake and Prioritization

```text
Create a research intake process for [team].
Inputs: demand, researcher capacity, planning cadence, and decision types.
Output: intake questions, triage criteria, decision-risk score, appetite, service levels, accept/defer/decline draft responses, and review cadence.
Rules: prioritize decision impact and timing over requester seniority; separate research requests from solution-validation requests.
```

### Participant Panel Plan

```text
Create a participant panel plan for [product/audience].
Output: recruitment channels, consent and re-contact language needs, minimal profile data, inclusion criteria, incentive approach, contact-frequency limits, accessibility accommodations, retention/deletion policy, panel health measures, and governance.
Rules: comply with applicable privacy rules; avoid collecting sensitive attributes without a justified research need and proper safeguards.
```
