---
id: b5b5edfa-2185-4b4a-925b-1ef9e8c14868
title: "Timeline with dependencies"
linkTitle: "Timeline"
weight: 35
lastmod: 2026-11-01T23:14:41+01:00
last_editor: Erik Hagen

---

The Timeline view in GitHub Projects shows tasks along a time axis, but does not draw which tasks wait for each other. The charts on this page do. They are generated automatically from the boards every hour, and updated on docs shortly after.

Click a title, a bar or an arrow to see the task in a window on top of the chart. Move the window by its title bar and resize it from the bottom right corner. Links to other tasks inside the window open in the same window. Click somewhere outside the window that is not a link, press Esc or click × to close it. Ctrl-click opens the task on GitHub instead. Hover to see status, dates and dependencies. If the column is narrow, the chart can be scrolled sideways.

The window fetches the task from GitHub. Without logging in, GitHub allows about 60 lookups an hour. If the limit is reached, a link to GitHub is shown instead, and logging in raises the limit.

**First version, for trial** ([solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32)). Task titles are in the language they were written in, usually Norwegian.

## Example

Seven examples on the board [«[EXAMPLE] Timeline»](https://github.com/orgs/samt-x/projects/20) show what the chart looks like with dependencies. They are not tasks, and they live in a repository of their own, [solution-task-management-examples](https://github.com/samt-x/solution-task-management-examples). The dates are moved automatically every week, so the examples always sit around today's date. The examples therefore show Start date and Due date as what has happened, not the history. Two of them have no dates and are placed after the tasks they wait for: G with Duration 3, and F without a duration. B has passed its due date, which was Friday last week. D should have started the same day (late start), but is still waiting for B and C. When C is finished, D cannot make its due date, and E, which waits for D, is late too. See [Examples in the documentation](../konvensjoner/#examples-in-the-documentation).

{{< inline-svg "project-20-en.svg" >}}

## Where the chart is used

The timeline for a board is shown on the page **Tasks and progress** of the sub-project that owns the board:

- [Architecture → High-level architecture → Tasks and progress](/en/arkitektur/overordnet-arkitektur/oppgaver-og-framdrift/) (Project 5)
- [Task management → Tasks and progress](../oppgaver-og-framdrift/) (Project 18)

The charts are all generated here, and the pages fetch them from here. See [Technical documentation](../teknisk-dokumentasjon/#timeline-with-dependencies).

## How to read the chart

- **Bar:** from start to end. The colour shows the status on the board. Grey with the title struck through means the task is closed.
- **Dark part:** what has happened, from when the task was moved to In progress until it was closed, or until today if it is still going on.
- **Light bar with border:** both start and end are set (Start date and Due date) or have happened.
- **Dashed bar:** at least one of the dates is calculated, see below.
- **Yellow border and yellow line under the bar:** late start. The task should have started and has not. The line runs from the start date until today.
- **Red after the due date:** late end. The bar is extended past the due date, and the part after the due date is red. Solid red is the time from the due date until today, when the due date has passed without the task being finished. Light red is the forecast: when the task can be finished if it starts today, or when the tasks it waits for are finished, and lasts as long as planned. The duration is Duration, otherwise the length from Start date to Due date. A delay therefore propagates: if one task is late, the tasks waiting for it can turn red before their own due date is reached.
- Only dates someone has set give yellow and red: Start date, Due date, or a date calculated with Duration. An assumed duration never gives yellow or red.
- **Arrow:** the task the arrow points to waits for the task the arrow comes from.
- **Red arrow:** the task being waited for ends after the waiting task is due to start. The plan does not add up.
- **Hover over an arrow:** why the task waits, slack or overlap in working days, and who linked the tasks and when. Click the arrow to see the dependency and the waiting task in the window.
- **Ring on the arrow:** the dependency is described. Without a ring, the tooltip only says that the description is missing.
- **⚠ below the chart:** a task describes a dependency that is not linked in GitHub.
- **⛔ before the title:** the task is still waiting for an open task.
- **Red vertical line:** today's date.

## Where the dates come from

All tasks on the board are included. Start and end are found separately, in this order:

1. **What has happened.** Start is the first time the task was moved to In progress (or In review) on the board. End is when the task was closed or moved to Done. GitHub records this itself.
2. **Date set:** Start date and Due date on the board.
3. **Calculated from the duration:** if only one of the dates exists, the other is calculated with the field **Duration** (working days).
4. **Calculated from the dependencies:** if start is missing, the task starts the working day after the last task it waits for ends. It does not start before today, though. If it waits for nothing, it starts today.

If Duration is missing, one week (five working days) is assumed. The number of such tasks is shown below the chart. If a task goes on longer than planned, the bar is extended to today. Hover over the bar to see the dates and where they come from.

Planned and actual dates have no separate fields. What has happened is in the history in GitHub.

## How a task gets the right place in the chart

1. Set **Start date** and **Due date** on the board, or one of them and **Duration**. Without any of them, the task is placed after the tasks it waits for.
2. Move the card to **In progress** when work begins, and close the task when it is done.
3. If the task waits for another task: open the issue, find **Relationships** in the right-hand margin and choose **Mark as blocked by**. Choose the task being waited for. It can be in another repository.
4. Write why the task waits under the heading **Avhengigheter** (dependencies) in the issue, one line per task, for example «- #35: needs legal clarification of consent». The Task form has its own field for this. If the task is in another repository, write for example samt-bu-pilot-6#12. The link itself is always the one in step 3. The text only describes it. See [Conventions](../konvensjoner/).

Dependencies can also be searched for on GitHub with **is:blocked**, **is:blocking** and **blocked-by:**.

If the task waits for something outside GitHub, the label blocked is used instead. It gives no arrow. See [Blocked](../konvensjoner/#blocked) in Conventions.
