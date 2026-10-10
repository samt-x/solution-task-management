---
id: 71a9801d-c1a0-4795-8c69-e935427a0b03
title: "Conventions"
linkTitle: "Conventions"
weight: 30
lastmod: 2026-10-10T22:27:29+02:00
last_editor: Erik Hagen

---

**Current practice from October 2026, open to adjustment.** The conventions build on the practice in solution-samt-bu-docs, which has worked well. Two questions remain open for the architecture group, see the bottom of the page.

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

## Responsibility

- **Responsible** (on boards that have the field): one person who owns the task
- **Assignees**: everyone working on the task, both the owner and contributors. They then get notifications of changes, and the task appears under «Assigned to me». Ownership is in Responsible, not in Assignees.

## Trace for administrative changes

Changes to repositories, boards, labels and routines get a chore task describing what, why and the outcome. It goes in the repository the change concerns. Deletion must always have such a trace before it is carried out.

## Writing tips

- When you write about a task without wanting to link to it, put the number in code format. Otherwise it becomes a link, and the mention appears in that task's timeline.
- Write «Project 5», not a hash sign before the number, for the same reason.
- Avoid @-mentions unless the person should be notified. A mention subscribes the person to the whole thread from then on.

## Open questions

Two things are not settled by the practice alone. Both have been put to the architecture group:

- [Who keeps track of tasks that cross architecture and pilots?](https://github.com/SAMT-X/solution-task-management/issues/1)
- [Any objections to how Responsible and Assignees are used in Project 5?](https://github.com/SAMT-X/solution-task-management/issues/2)

Answers can be given in the issue, in Teams or at the architecture meeting.
