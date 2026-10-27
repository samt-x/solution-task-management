---
id: 71a9801d-c1a0-4795-8c69-e935427a0b03
title: "Conventions"
linkTitle: "Conventions"
weight: 30
lastmod: 2026-10-27T20:25:02+01:00
last_editor: Erik Hagen

---

**Current practice from October 2026, open to adjustment.** The conventions build on the practice in solution-samt-bu-docs, which has worked well. One question remains open for the architecture group, see the bottom of the page.

## One task, one place

1. **One owner per task.** The task is created where the responsibility lies, see [User guide](../brukerveiledning/). We do not copy tasks between repositories.
2. **Link instead of copy.** If the task affects another area, link to it in a comment. GitHub shows the connection in both tasks.
3. **Sub-issues for dependencies.** When an architecture task depends on a deliverable from a pilot, or vice versa, the other task is added as a sub-issue. This works across repositories, and progress is shown on the board.

The reason is that status and other fields are stored per board. If the same task is on two boards, it gets two statuses that soon diverge.

## Type and labels

**The type says what the issue is. The status says where it is in the flow.** Each issue has one type (issue type), and the types apply to all repositories in the organisation. The type should still be correct when the issue is done. That is why there is no type for «suggestion» or «input». That something is proposed and not yet considered is shown by the status Proposed.

| Type | Used for |
|---|---|
| Task | Something to be done – most things, including follow-up, exploration and investigation |
| Solution proposal | A proposed solution to be assessed, usually together with other proposals in a larger task |
| Question | Something that needs an answer |
| Decision | Something that requires a decision. Say what and by whom. |
| Risk | A risk or concern that should be assessed |
| Problem | Something that is wrong now: a tool that does not work, an error in content or a model, reasoning that does not hold, a contradiction between sources, or something in the way we work. What may go wrong is a Risk. The type was called Bug until October 2026. |

Labels come in addition to the type, and an issue can have several:

| Label | Used for |
|---|---|
| blocked | Waiting for something outside the issue |
| chore | Management and maintenance of repositories, boards and routines |
| future | Not now, but a candidate later |

The labels task, decision and question were used as types before the types arrived (October 2026). They have been replaced by the types and no longer exist. The same goes for GitHub's default labels bug, enhancement, duplicate, invalid and wontfix: the types and the close reasons (below) do the same job, so they were deleted everywhere they had not been used. bug and enhancement remain on older issues in the solution repositories, but are not to be used on new ones. Labels for topics are on hold. Instead, an issue can link to what it concerns (a page, a case, an element in the model) in the field «Gjelder» in the forms, see [samt-bu-architecture#35](https://github.com/samt-x/samt-bu-architecture/issues/35).

## Input and solution proposals

1. **Input is an issue in Proposed**, of any type. Whoever handles the input moves it to To do, or closes it.
2. **No assignment in Proposed.** Assignees are set only when the issue has been considered. The submitter can suggest who should look at it with an @-mention, in the forms' field «Forslag til hvem som bør se på dette» or in the text, for example «Suggestion: @name looks at this». They then get one notification and can follow the thread, without the issue appearing in their task lists as if they had agreed to it.
3. **Solution proposals are linked to the assessment.** When a solution proposal is taken into the work of assessing solutions, it is added as a sub-issue under the larger task. This shows in both directions where the proposal belongs, and the larger task shows how many proposals have been assessed.

## Closing

An issue can be closed from any status, also directly from Proposed. Always choose the right reason when closing, and write a short comment on why.

| Reason in GitHub | Used when | Icon |
|---|---|---|
| Completed | The issue is done. For a solution proposal: assessed and taken forward. | Purple check mark |
| Not planned | The issue is rejected, aborted or cancelled. The comment says which and why. | Grey circle with a slash |
| Duplicate | The issue already exists. Link to the other one. | Grey |

All closed issues end up in Done on the board. The reason is shown by the icon on the card, and you can search for it with «reason:completed» or «reason:"not planned"».

## Fixed headings in the description

- **Background** – why this is needed, what triggered it
- **What to do** – concretely
- **Done when** – what must be in place
- **Related** – links to other tasks, pages or documents (optional)

For decisions also: **Alternatives** and **Recommendation**. The decision itself is written in the closing comment and recorded in the decision log on docs.samt-bu.no.

## Status and fields on the boards

Every board is based on one of two templates, Simple or Standard. The names in GitHub are in English, so the boards work for all readers.

| Status | Meaning | Simple | Standard | Shared level |
|---|---|---|---|---|
| Proposed | Suggested, not yet considered. Input starts here, see [Input and solution proposals](#input-and-solution-proposals). | ✓ | ✓ | Not started |
| To do | Agreed, but not started | ✓ | ✓ | Not started |
| Ready | Clarified and ready to start, next in line | | ✓ | Not started |
| In progress | Being worked on | ✓ | ✓ | In progress |
| In review | Out for review or comments | | ✓ | In progress |
| Done | Completed, the task is closed | ✓ | ✓ | Done |

**The shared level** is used when status is reported across boards. A board may add its own steps, as long as it is decided which shared level the step belongs to. Proposed was such a step on Project 5 until October 2026. It is now part of both templates and on all boards.

**Ready** is needed when several people pick tasks from a shared queue. If that is not the case, Simple is enough.

| Field | Content | |
|---|---|---|
| Responsible | The person who owns the task. GitHub username, otherwise full name. Never an e-mail address, since the boards are public. | Should be filled in |
| Priority | High, Medium or Low | Optional |
| Effort | Small (less than one person-day), Medium (1–5 person-days) or Large (more than 5 person-days, consider splitting the task) | Optional |
| Estimate (person-days) | Estimate in person-days. Summed automatically in grouped views, for example per responsible person. | Optional |
| Start date and Due date | The current plan. Changed when the plan changes. | Optional |
| Comment | The latest status comment, dated first, for example «23.10: Draft sent to Anders». Only the latest comment is kept in the field. Only on Project 5 for now. | Optional |

**Comment has no history in GitHub.** When the field is overwritten, the previous comment is gone from the board. The status of Project 5 is therefore written to a file every hour, and the [history of that file](https://github.com/samt-x/solution-task-management/commits/main/status/project-5.md) shows earlier comments and statuses. See [Setup](/en/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/oppsett/).

**Actual dates** are recorded by GitHub itself: when the task was created, when it was moved to In progress, and when it was closed. This relies on two habits: move the card to In progress when you start, and close the task when it is done.

**Blocked is not a step.** The task keeps its status and gets the label blocked. Say in a comment what it is waiting for, and remove the label when the obstacle is gone. The label exists in all the repositories, so blocked tasks can be searched for across them.

## Responsibility

- **Responsible**: one person who owns the task, given as GitHub username, otherwise full name
- **Assignees**: everyone working on the task, both the owner and contributors. They then get notifications of changes, and the task appears under «Assigned to me». Ownership is in Responsible, not in Assignees.
- Issues in Proposed are not assigned, see [Input and solution proposals](#input-and-solution-proposals).

## Trace for administrative changes

Changes to repositories, boards, labels and routines get a chore task describing what, why and the outcome. It goes in the repository the change concerns. Deletion must always have such a trace before it is carried out.

## Writing tips

- When you write about a task without wanting to link to it, put the number in code format. Otherwise it becomes a link, and the mention appears in that task's timeline.
- Write «Project 5», not a hash sign before the number, for the same reason.
- Avoid @-mentions unless the person should be notified. A mention subscribes the person to the whole thread from then on.

## Open questions

One question is not settled by the practice alone, and has been put to the architecture group: [Who keeps track of tasks that cross architecture and pilots?](https://github.com/SAMT-X/solution-task-management/issues/1) Answers can be given in the issue, in Teams or at the architecture meeting.

The templates were introduced in October 2026, see [Setup](/en/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/oppsett/). The boards that existed before were moved over to the templates in [M2 Templates in use](https://github.com/samt-x/solution-task-management/issues/6).
