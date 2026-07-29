# Example: Discovery research plan

> Fictional example. No real participants, client data, or research findings are included.

## Example request

```text
Create a 2-week discovery research plan for a B2B shift-scheduling app.

The product team needs to decide whether to build employee-led shift swaps next quarter. We can interview 8 employees and 4 managers. We also have support tickets and product analytics.
```

## Example output

**Evidence mode:** Research plan

### Recommended approach

Use a focused mixed-method study:

1. Review support tickets and analytics to locate current swap behavior and failure points.
2. Interview employees about recent swap attempts.
3. Interview managers about approval, coverage, compliance, and exception handling.
4. Map the current workflow and define a decision rule before synthesis.

**Decision:** Decide whether the evidence is strong enough to shape and feasibility-check an employee-led shift-swap concept next quarter, narrow the concept, or defer it.

The study can reveal behavior, constraints, and workflow risk. It can't estimate market-wide demand or prove that a proposed design will improve schedule coverage.

A roadmap commitment also requires technical, legal or policy, operational, and delivery review.

### Known inputs and assumptions

| Item | Status |
|---|---|
| Employees already attempt to swap shifts | Assumed until tickets, analytics, or interviews confirm it |
| Managers spend meaningful time coordinating swaps | Assumed |
| Support tickets include swap-related issues | Known source, coverage still unknown |
| Product analytics can identify swap attempts | Needs instrumentation check |
| 8 employees and 4 managers cover the main contexts | Planning assumption, not representativeness |

### Research objectives

1. Understand the most recent shift-swap journey from trigger to resolution.
2. Identify employee and manager workarounds.
3. Document approval, coverage, compliance, fairness, and notification constraints.
4. Separate frequent problems from costly edge cases.
5. Define what an employee-led flow must prove before roadmap commitment.

### Sources and participants

#### Existing evidence

- Support tickets from the last 90 days, filtered using a documented query.
- Analytics for schedule views, change requests, manager edits, and failed actions.
- Existing policy or compliance documentation supplied by the company.

#### Interviews

- 8 employees who attempted, completed, abandoned, or avoided a shift swap in the last 30 days.
- 4 managers who approved or manually coordinated at least 1 recent swap.

Recruit across relevant contract types, locations, shift patterns, and accessibility needs. Collect only attributes needed to understand the workflow.

### Participant operations

- Make participation voluntary and separate it from performance review or scheduling decisions.
- Don't tell managers who participated or share individual employee responses with them.
- Obtain informed consent before each interview and separate consent for recording.
- Restrict raw notes and recordings to the research team.
- Delete raw recordings and directly identifying notes 30 days after the final decision. Retain only pseudonymized synthesis under the repository's retention policy.
- Use a consistent incentive policy and let participants skip questions or withdraw.
- Offer accessible scheduling, formats, and materials.

### Interview focus

Anchor each conversation in a recent event:

- What triggered the swap?
- What happened first?
- Who became involved?
- Which tools, messages, or workarounds were used?
- Where did the process slow down or fail?
- What information did each person need?
- What made a swap acceptable or unacceptable?
- How was the outcome communicated?
- What happened when no valid replacement existed?

Avoid asking participants to design the feature or predict whether they would use it.

### Analysis

Create:

- a current-state workflow with evidence at each step;
- separate employee and manager needs;
- a list of policy, compliance, fairness, and notification constraints;
- failure modes and edge cases;
- opportunities that remain separate from solution ideas;
- an evidence table with coverage, counter-evidence, confidence, and validation needs.

Report qualitative coverage as counts in this sample. Don't convert interview frequency into population prevalence.

### Decision rule

Set these thresholds before interviews begin. Recommend concept shaping and feasibility review only when:

1. At least 3 participants can recount a recent swap attempt, including its trigger, workaround, and consequence.
2. Those attempts cover at least 2 predeclared contexts: fixed or variable schedules, single or multiple locations, and employee- or manager-initiated changes.
3. Current handling causes an observable cost in at least 3 cases, such as delay, uncovered work, repeated coordination, abandonment, or policy escalation.
4. The 4 managers can state approval and coverage rules consistently enough to prototype.
5. Policy or legal owners confirm that certification, overtime, rest periods, leave, payroll, and local or union rules can be represented or safely escalated.
6. The team can instrument request start, submission, approval, rejection, cancellation, resolution time, and resulting schedule coverage.
7. Technical and delivery review finds a feasible slice that can fail safely.

Recommend a narrower concept when criteria 1-3 are met but policy or edge cases still require manual control. Defer further investment when evidence is mainly stated preference, criteria 5-7 fail, or the workflow can't fail safely.

### 2-week schedule

| Day | Work |
|---|---|
| 1 | Lock decision, scope, definitions, data access, and privacy rules |
| 2-3 | Review tickets and validate analytics instrumentation |
| 3 | Pilot both interview guides |
| 4-7 | Conduct 8 employee and 4 manager interviews |
| 8 | Code evidence and build the current-state workflow |
| 9 | Review contradictions, constraints, and alternative explanations |
| 10 | Deliver recommendation, evidence table, risks, and smallest next test |

### Risks and controls

- **Recall bias:** recruit for a recent swap event and ask for a step-by-step account.
- **Manager authority:** keep manager policy claims separate from employee experience.
- **Analytics gaps:** audit event definitions before using counts.
- **Sensitive employment data:** anonymize participants and avoid unnecessary performance details.
- **Accessibility:** offer accessible scheduling, interview formats, and materials.

### Smallest next validation

If the decision rule supports concept shaping, prototype the riskiest approval and exception flow first. Test it with employees and managers, then complete technical, policy, operational, and delivery review before making a roadmap commitment.
