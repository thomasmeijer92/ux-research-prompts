# Example: Mobile onboarding usability test

> Fictional example. No real participants, client data, or research findings are included.

## Example request

```text
Create a usability test plan for the onboarding of an iOS budgeting app.

We need to decide whether account registration should happen before or after the first budget import. We have a clickable prototype, 1 week, and access to 6 existing customers. Include VoiceOver users.
```

## Example output

**Evidence mode:** Research plan

### Recommended approach

Run 6 moderated, comparative usability sessions with 2 prototype variants:

- **Variant A:** create an account, then import a budget.
- **Variant B:** import a budget, then create an account.

Each participant tests both variants. Counterbalance the order so 3 people start with A and 3 start with B. Analyze first exposure separately to keep learning effects visible.

**Decision:** Choose the order that gets people to a usable first budget with fewer critical errors, less registration friction, and clear understanding of data storage.

The study can explain why one order works better in these sessions. It can't establish a conversion difference across the wider market.

### Participants

Recruit:

- 2 experienced VoiceOver users who normally use VoiceOver on their iPhone.
- 4 participants who don't use a screen reader.
- A mix of people with and without previous budget-import experience.

Use existing customers for this round, then note their likely familiarity and brand trust as a limitation. If the available pool doesn't include real VoiceOver users, record VoiceOver usability as unanswered and recruit separately before release.

### Participant operations

- Make participation voluntary and allow people to skip a question or stop.
- Collect informed consent before the session and separate consent for recording.
- State who can access recordings and notes.
- Delete raw recordings and directly identifying notes 30 days after the decision memo is accepted. Retain only pseudonymized synthesis under the repository's retention policy.
- Use the same incentive policy for VoiceOver and non-VoiceOver participants.
- Ask about accommodations during scheduling and provide accessible study materials.

### Prototype gate

Before scheduling sessions, confirm that the prototype supports:

- meaningful accessibility labels and roles;
- a logical focus order;
- spoken status and error feedback;
- operation without drag-only gestures;
- recovery from failed import or registration;
- dummy data, so nobody enters real financial information.

A visual click-through without accessible semantics can't support a valid VoiceOver study. Build the smallest accessible native slice if needed.

### Research questions

1. Can participants reach a usable first budget without help?
2. Where do they hesitate, fail, or consider leaving?
3. When does registration feel justified?
4. Do participants understand what is saved before and after account creation?
5. Can VoiceOver users complete both variants independently?
6. Which order produces fewer severe issues on first exposure?

### Core task

> You installed this app because you want a clearer view of your spending. You have a sample file with an existing budget. Set up the app so you can view and continue working with that budget.

Don't name registration, import controls, or the intended order in the task.

### Post-task questions

- What do you think is saved right now?
- What would you expect to happen if you closed the app?
- Where, if anywhere, did you consider stopping?
- Overall, how easy or difficult was the task? `1 = very difficult`, `7 = very easy`.
- How confident are you that you know what will happen to your budget data? `1 = not at all confident`, `5 = completely confident`.

Use stated preference only as supporting context. Base the decision mainly on observed behavior, errors, recovery, and comprehension.

### Measures

| Measure | Definition |
|---|---|
| Task success | Completed independently, with help, or not completed |
| Critical error | Blocks import, access, storage, privacy, or recovery |
| Time to first value | Start of task to first usable budget view |
| Moderator intervention | Count and reason |
| Registration friction | Hesitation, refusal, confusion, or exit signal |
| Data comprehension | Correct understanding of storage and account linkage |
| Recovery | Independent recovery after an error |
| VoiceOver operation | Labels, focus, announcements, gestures, and traps |

Report counts as `4 of 6 in this sample`, never as population percentages.

### Severity

- **S1, blocking or exclusionary:** task is impossible, data is at risk, or VoiceOver can't proceed.
- **S2, serious:** help is required, storage is misunderstood, or the participant shows a strong exit signal.
- **S3, moderate:** clear delay or confusion with independent recovery.
- **S4, minor:** small wording, feedback, or presentation issue.

### Decision rule

Choose a variant only when it:

1. has no unresolved S1 issue;
2. shows no observed exclusionary VoiceOver issue in the tested tasks and passes a separate accessibility review before release;
3. has at least equal task success;
4. produces fewer serious errors and exit signals;
5. gives participants an accurate understanding of their data.

If results are mixed, registration after import is viable only when pre-account data is safe, temporary, and clearly explained. If an account is required for security, recovery, or storage, keep registration first and reduce its friction.

### 1-week schedule

| Day | Work |
|---|---|
| 1 | Lock the decision rule, check accessibility, prepare prototypes and dummy data |
| 2 | Run an internal pilot, adjust the script, schedule participants |
| 3-4 | Conduct 6 sessions and log issues immediately |
| 5 | Compare variants, review counter-evidence, and write the decision memo |

### Limits and next validation

- Existing customers may trust the product more than new users.
- A prototype doesn't test real import speed, production security, or technical reliability.
- 6 qualitative sessions support a design decision, not a statistical conversion claim.

The smallest follow-up is a production experiment or onboarding benchmark with new users after both variants are technically safe.
