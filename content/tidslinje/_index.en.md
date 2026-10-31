---
id: b5b5edfa-2185-4b4a-925b-1ef9e8c14868
title: "Timeline with dependencies"
linkTitle: "Timeline"
weight: 35
lastmod: 2026-10-31T02:32:01+01:00
last_editor: Erik Hagen

---

The Timeline view in GitHub Projects shows tasks along a time axis, but does not draw which tasks wait for each other. The charts on this page do. They are generated automatically from the boards every hour, and updated on docs shortly after.

Click a title, a bar or an arrow to see the task in a window on top of the chart. Move the window by its title bar and resize it from the bottom right corner. Links to other tasks inside the window open in the same window. Ctrl-click opens the task on GitHub instead. Hover to see status, dates and dependencies. If the column is narrow, the chart can be scrolled sideways.

The window fetches the task from GitHub. Without logging in, GitHub allows about 60 lookups an hour. If the limit is reached, a link to GitHub is shown instead, and logging in raises the limit.

**First version, for trial** ([solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32)). Task titles are in the language they were written in, usually Norwegian.

## Example with test tasks

Seven test tasks in Task management (Project 18) show what the chart looks like with dependencies. They are not real tasks.

{{< inline-svg "project-18-en.svg" >}}

## SAMT-BU framework and generic architecture

Project 5. No tasks here have dependencies yet, and only tasks with dates are included.

{{< inline-svg "project-5-en.svg" >}}

## How to read the chart

- **Bar:** from start date to due date. The colour shows the status on the board. Grey with the title struck through means the task is closed.
- **Dashed bar:** start date only. **Diamond:** due date only.
- **Arrow:** the task the arrow points to waits for the task the arrow comes from.
- **Red arrow:** the task being waited for ends after the waiting task is due to start. The plan does not add up.
- **Hover over an arrow:** why the task waits, slack or overlap in days, and who linked the tasks and when. Click the arrow to see the dependency and the waiting task in the window.
- **Ring on the arrow:** the dependency is described. Without a ring, the tooltip only says that the description is missing.
- **⚠ below the chart:** a task describes a dependency that is not linked in GitHub.
- **⛔ before the title:** the task is still waiting for an open task.
- **Red vertical line:** today's date.

Tasks without dates are not included. The number is shown below the chart.

## How a task gets into the chart

1. Set **Start date** and **Due date** on the board. One of them is enough.
2. If the task waits for another task: open the issue, find **Relationships** in the right-hand margin and choose **Mark as blocked by**. Choose the task being waited for. It can be in another repository.
3. Write why the task waits under the heading **Avhengigheter** (dependencies) in the issue, one line per task, for example «- #35: needs legal clarification of consent». The Task form has its own field for this. If the task is in another repository, write for example samt-bu-pilot-6#12. The link itself is always the one in step 2. The text only describes it. See [Conventions](../konvensjoner/).

Dependencies can also be searched for on GitHub with **is:blocked**, **is:blocking** and **blocked-by:**.

How «Blocked by» and the label blocked in [Conventions](../konvensjoner/) should be used together is not settled yet. The proposal is that «Blocked by» is used when the task waits for another task, and the label when it waits for something outside GitHub.
