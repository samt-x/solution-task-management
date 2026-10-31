---
title: "Timeline with dependencies"
linkTitle: "Timeline"
weight: 35

---

The Timeline view in GitHub Projects shows tasks along a time axis, but does not draw which tasks wait for each other. The charts on this page do. They are generated automatically from the boards every hour, and updated on docs shortly after.

Click a chart to open it in full size. There you can click titles and bars to go to the task, and hover over them to see status, dates and dependencies.

**First version, for trial** ([solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32)). Task titles are in the language they were written in, usually Norwegian.

## Example with test tasks

Seven test tasks in Task management (Project 18) show what the chart looks like with dependencies. They are not real tasks.

[![Timeline with dependencies for the test tasks in Project 18](/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/tidslinje/project-18-en.svg)](/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/tidslinje/project-18-en.svg)

## SAMT-BU framework and generic architecture

Project 5. No tasks here have dependencies yet, and only tasks with dates are included.

[![Timeline with dependencies for Project 5](/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/tidslinje/project-5-en.svg)](/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/tidslinje/project-5-en.svg)

## How to read the chart

- **Bar:** from start date to due date. The colour shows the status on the board. Grey with the title struck through means the task is closed.
- **Dashed bar:** start date only. **Diamond:** due date only.
- **Arrow:** the task the arrow points to waits for the task the arrow comes from.
- **Red arrow:** the task being waited for ends after the waiting task is due to start. The plan does not add up.
- **⛔ before the title:** the task is still waiting for an open task.
- **Red vertical line:** today's date.

Tasks without dates are not included. The number is shown below the chart.

## How a task gets into the chart

1. Set **Start date** and **Due date** on the board. One of them is enough.
2. If the task waits for another task: open the issue, find **Relationships** in the right-hand margin and choose **Mark as blocked by**. Choose the task being waited for. It can be in another repository.

Dependencies can also be searched for on GitHub with **is:blocked**, **is:blocking** and **blocked-by:**.

How «Blocked by» and the label blocked in [Conventions](../konvensjoner/) should be used together is not settled yet. The proposal is that «Blocked by» is used when the task waits for another task, and the label when it waits for something outside GitHub.
