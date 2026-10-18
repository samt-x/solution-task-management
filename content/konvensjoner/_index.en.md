---
id: 71a9801d-c1a0-4795-8c69-e935427a0b03
title: "Conventions"
linkTitle: "Conventions"
weight: 30
lastmod: 2026-10-10T23:11:08+02:00
last_editor: Erik Hagen

---

**Current practice from October 2026, open to adjustment.** The conventions build on the practice in solution-samt-bu-docs, which has worked well. One question remains open for the architecture group, see the bottom of the page.

## One task, one place

1. **One owner per task.** The task is created where the responsibility lies, see [User guide](../brukerveiledning/). We do not copy tasks between repositories.
2. **Link instead of copy.** If the task affects another area, link to it in a comment. GitHub shows the connection in both tasks.
3. **Sub-issues for dependencies.** When an architecture task depends on a deliverable from a pilot, or vice versa, the other task is added as a sub-issue. This works across repositories, and progress is shown on the board.

The reason is that status and other fields are stored per board. If the same task is on two boards, it gets two statuses that soon diverge.

## Type is given by label

| Label | Used for |
|---|---|
| task | A work task – most things |
| decision | Requires a decision |
| problem | Something is wrong, unclear or in conflict |
| chore | Management and maintenance of repositories, boards and routines |
| future | Not now, but a candidate later |
| blocked | Waiting for something outside the task |

Each task has one type label. future and blocked are added when needed.

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
| To do | Agreed, but not started | ✓ | ✓ | Not started |
| Ready | Clarified and ready to start, next in line | | ✓ | Not started |
| In progress | Being worked on | ✓ | ✓ | In progress |
| In review | Out for review or comments | | ✓ | In progress |
| Done | Completed, the task is closed | ✓ | ✓ | Done |

**The shared level** is used when status is reported across boards. A board may add its own steps, for example Proposed (suggested, not yet considered) before To do, as long as it is decided which shared level the step belongs to.

**Ready** is needed when several people pick tasks from a shared queue. If that is not the case, Simple is enough.

| Field | Content | |
|---|---|---|
| Responsible | The person who owns the task. GitHub username, otherwise full name. Never an e-mail address, since the boards are public. | Should be filled in |
| Priority | High, Medium or Low | Optional |
| Effort | Small (less than one person-day), Medium (1–5 person-days) or Large (more than 5 person-days, consider splitting the task) | Optional |
| Estimate (person-days) | Estimate in person-days. Summed automatically in grouped views, for example per responsible person. | Optional |
| Start date and Due date | The current plan. Changed when the plan changes. | Optional |

**Actual dates** are recorded by GitHub itself: when the task was created, when it was moved to In progress, and when it was closed. This relies on two habits: move the card to In progress when you start, and close the task when it is done.

**Blocked is not a step.** The task keeps its status and gets the label blocked. Say in a comment what it is waiting for, and remove the label when the obstacle is gone. The label exists in all the repositories, so blocked tasks can be searched for across them.

## Responsibility

- **Responsible**: one person who owns the task, given as GitHub username, otherwise full name
- **Assignees**: everyone working on the task, both the owner and contributors. They then get notifications of changes, and the task appears under «Assigned to me». Ownership is in Responsible, not in Assignees.

## Trace for administrative changes

Changes to repositories, boards, labels and routines get a chore task describing what, why and the outcome. It goes in the repository the change concerns. Deletion must always have such a trace before it is carried out.

## Writing tips

- When you write about a task without wanting to link to it, put the number in code format. Otherwise it becomes a link, and the mention appears in that task's timeline.
- Write «Project 5», not a hash sign before the number, for the same reason.
- Avoid @-mentions unless the person should be notified. A mention subscribes the person to the whole thread from then on.

## Open questions

One question is not settled by the practice alone, and has been put to the architecture group: [Who keeps track of tasks that cross architecture and pilots?](https://github.com/SAMT-X/solution-task-management/issues/1) Answers can be given in the issue, in Teams or at the architecture meeting.

The templates were introduced in October 2026, see [Setup](/en/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/oppsett/). The boards that existed before are moved over to the templates in [M2 Templates in use](https://github.com/samt-x/solution-task-management/issues/6).
