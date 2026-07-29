# Example: Interview synthesis

> Fictional example. No real participants, client data, or research findings are included.

## Example request

```text
Synthesize these 4 interview notes into decision-ready insights for a calendar app.

P1: Plans every Sunday and wants a week view. Lost trust when an appointment disappeared.
P2: Plans ad hoc, uses only the day view, and finds the week view crowded.
P3: Plans every Sunday and exports to paper because changes sometimes fail to sync.
P4: Plans ad hoc, wants faster event creation, and didn't mention sync problems.

Show what we still can't conclude.
```

## Example output

**Evidence mode:** Evidence-backed, using 4 fictional interview notes

### Recommendation

Treat reliable saving and sync as a release criterion. Keep day and week planning available without forcing one view. Validate quick-add before committing to a specific interaction.

### Evidence table

| Claim | Type | Evidence/source | Coverage | Counter-evidence | Confidence | Implication | Validation |
|---|---|---|---:|---|---|---|---|
| P1 reported lost trust after an appointment disappeared. P3 reported using paper after sync problems. | Observed | P1 lost trust after an appointment disappeared. P3 uses paper because changes sometimes fail to sync. | 2 of 4 | P2 and P4 didn't mention sync problems. Silence doesn't prove absence. | Medium | Fix saving, sync status, conflict handling, and recovery before adding planning features. | Review logs and test offline edits, multi-device conflicts, and recovery. |
| This sample contains at least 2 planning rhythms: weekly preparation and ad hoc planning. | Observed | P1 and P3 plan on Sunday. P2 and P4 plan ad hoc. | 4 of 4 | People may switch rhythms or combine them. The notes don't cover that. | High for variation, low for prevalence | Support more than 1 entry point and planning rhythm. | Observe recent planning sessions and test whether people find the right workflow. |
| P1 wants a week view. P2 uses the day view and describes the week view as crowded. | Observed | P1 wants a week view. P2 uses the day view and finds the week view crowded. | 2 of 4 | P3 and P4 didn't discuss view preference. | High for the contrast, low for the best default | Keep day and week views as equal options. | Test switching, readability, and default-view choices across both planning rhythms. |
| P4 asked for faster event creation. The other 3 notes don't mention creation speed. | Observed | P4 wants faster event creation. | 1 of 4 | P1 to P3 didn't raise creation speed. P2 also plans ad hoc but didn't mention it. | Low | Prototype quick-add without treating it as a proven top priority. | Compare 2 compact input options on time, errors, and missing details. |

### Decisions supported by the notes

1. Put data integrity ahead of new planning features.
2. Preserve day and week views while the best default remains unknown.
3. Test quick-add with a small prototype before implementation.

### What the notes don't support

- That half of all users experience sync problems or plan weekly.
- That every Sunday planner wants a week view.
- That every ad hoc planner dislikes the week view or needs quick-add.
- That P4 has no sync problems.
- That paper export is a desired feature. For P3, paper appears to be a workaround.
- Which device, state, or technical condition causes sync failures.
- Which week-view or quick-add design will work best.
- That planning rhythm causes view preference.

### Smallest next validation

Combine a technical sync audit with short task-based sessions:

- reproduce saving, offline editing, multi-device sync, conflicts, and recovery;
- ask participants to plan a week, add an ad hoc event, and switch views;
- measure critical errors, sync comprehension, recovery, and event-creation effort;
- include both planning rhythms without treating this sample as market prevalence.
