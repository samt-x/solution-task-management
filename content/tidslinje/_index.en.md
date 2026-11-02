---
id: b5b5edfa-2185-4b4a-925b-1ef9e8c14868
title: "Timeline with dependencies"
linkTitle: "Timeline"
weight: 35
lastmod: 2026-11-02T03:45:14+01:00
last_editor: Erik Hagen

---

The Timeline view in GitHub Projects shows tasks along a time axis, but does not draw which tasks wait for each other. The charts on this page do. They are generated automatically from the boards every hour, and updated on docs shortly after. A fixed script makes them following the rules on this page. If a run fails, the previous chart stays until the error is fixed, and the date below the chart shows when it was made. See [Scheduled runs](../teknisk-dokumentasjon/#scheduled-runs).

Click a title, a bar or an arrow to see the task in a window on top of the chart. Move the window by its title bar and resize it from the bottom right corner. Links to other tasks inside the window open in the same window. Click somewhere outside the window that is not a link, press Esc or click × to close it. Ctrl-click opens the task on GitHub instead. Hover to see status, dates and dependencies. The chart is shown at full size in a frame that can be scrolled sideways and up and down. The toolbar above the chart zooms out and in (− and +), back to full size (100 %) or so that the whole width fits (Fit width). Ctrl + mouse wheel over the chart zooms only the chart. The chart can also be dragged with the mouse (hand cursor) in any direction. A click without dragging opens the task as before. «Open the chart in a new window» shows the chart on its own, where it can be saved or copied.

The line **Show** below the toolbar chooses which tasks are shown: **All**, **Active** (open), **Delayed** (late start, due date passed or forecast after the due date), **Completed** or **Cancelled** (closed without being done). A parent is shown when it or one of its sub-issues matches, so the context does not disappear. If you are logged in on docs, there is also the button **My tasks**. It highlights with a yellow background the tasks where you are Responsible or assignee, whatever selection is shown. The choices only last until the page is reloaded.

The window fetches the task from GitHub. Without logging in, GitHub allows about 60 lookups an hour. If the limit is reached, a link to GitHub is shown instead, and logging in raises the limit.

**First version, for trial** ([solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32)). Task titles are in the language they were written in, usually Norwegian.

## Examples

The examples below show typical situations, with a few tasks each. The legend below each chart shows only what is in that chart. The examples are on the board [«[EXAMPLE] Timeline»](https://github.com/orgs/samt-x/projects/20). They are not tasks, and they live in a repository of their own, [solution-task-management-examples](https://github.com/samt-x/solution-task-management-examples). Each situation has its own label, and an example can be part of several. The dates are moved automatically every week, so the examples always sit around today's date. The examples therefore show Start date and Due date as what has happened, not the history. See [Examples in the documentation](../konvensjoner/#examples-in-the-documentation).

### A simple plan

A is completed (✓). L is in progress: the dark part is what has been done until today, and the light part is the rest of the plan until the due date. M has not started and waits for L (⛔). The arrow goes from L to M, and the ring on the arrow shows that the dependency is described in M.

{{< inline-svg "example-simple-plan-en.svg" >}}

### Dependencies and slack

M, N and O all wait for L. Hover over an arrow to see the slack. M starts the working day after L ends, with no slack. N has a week of slack, but the dependency is not described, so the arrow has no ring. O is due to start before L is finished. The arrow is red because the plan does not add up, and the forecast (light red) shows when O can be finished if it starts after L.

{{< inline-svg "example-dependencies-en.svg" >}}

### A delay that propagates

B should have been finished Friday last week, and is red from the due date. D should have started the same Friday (yellow border and line), but is still waiting for B and C. When C is finished, D cannot make its due date. E waits for D, and is therefore late too, even though the due date of E has not been reached.

{{< inline-svg "example-delays-en.svg" >}}

### Without dates

F and G have neither Start date nor Due date, so they are placed after the tasks they wait for: G after B and F after E. The bars are dashed because the dates are calculated. G has Duration 3. F has no duration and is assumed to take one week, as stated below the chart. B is delayed, and so G is moved as well.

{{< inline-svg "example-no-dates-en.svg" >}}

### Due date and duration, but no start date

When the start date is missing, it is calculated backwards from the due date with the duration (dashed bar). I has no dependencies, but the calculated start date has passed (yellow), and today plus the duration goes past the due date, so the forecast is red. H waits for C. To make its due date, H would have to start before C is finished, so the arrow is red, and the earliest start after C plus the duration goes past the due date.

{{< inline-svg "example-due-and-duration-en.svg" >}}

### Closed: completed and cancelled

A is completed (✓). J was closed without being done (✕, hatched bar), in GitHub with «Close as not planned». Both are grey with the title struck through.

{{< inline-svg "example-closed-en.svg" >}}

### Sub-issues

K has three sub-issues: K1 is completed, K2 has not started and is past its due date, and K3 is in progress but waits for K2. K shows the progress 1/3, and the bracket has a red border because K2 is delayed. The gap in the dark part is the days between K1 and K3 when neither was being worked on. Click ▾ in front of K to collapse the sub-issues, and ▸ to expand them again. K3 has Responsible set, so it gets a yellow background with **My tasks** for the person with that user name.

{{< inline-svg "example-sub-issues-en.svg" >}}

### All the examples together

This is the board with all the examples in one chart. Try the filter above the chart, for example **Delayed**.

{{< inline-svg "project-20-en.svg" >}}

## Where the chart is used

The timeline for a board is shown on the page **Tasks and progress** of the sub-project that owns the board:

| Sub-project | Board |
|---|---|
| [Pilot 1](/en/pilotering/pilot-1/oppgaver-og-framdrift/) | Project 1 |
| [Pilot 2](/en/pilotering/pilot-2/oppgaver-og-framdrift/) | Project 2 |
| [Pilot 3](/en/pilotering/pilot-3/oppgaver-og-framdrift/) | Project 4 |
| [Pilot 4](/en/pilotering/pilot-4/oppgaver-og-framdrift/) | Project 3 |
| [Pilot 5](/en/pilotering/pilot-5/oppgaver-og-framdrift/) | Project 9 |
| [Pilot 6](/en/pilotering/pilot-6/oppgaver-og-framdrift/) | Project 10 |
| [Pilot 7](/en/pilotering/pilot-7/oppgaver-og-framdrift/) | Project 19 |
| [High-level architecture](/en/arkitektur/overordnet-arkitektur/oppgaver-og-framdrift/) | Project 5 |
| [Information architecture](/en/arkitektur/informasjonsarkitektur/oppgaver-og-framdrift/) | Project 6 |
| [SAMT-BU Docs](/en/prosjektleveranser/loesninger/samhandlingsplattform/samt-bu-docs/oppgaver-og-framdrift/) | Project 17 |
| [Task management](../oppgaver-og-framdrift/) | Project 18 |

The charts are all generated here, and the pages fetch them from here. See [Technical documentation](../teknisk-dokumentasjon/#timeline-with-dependencies).

## How to read the chart

- **Bar:** from start to end. The colour shows the status on the board. Grey with the title struck through means the task is closed: **✓** before the title means completed, and **✕** with a hatched bar means closed without being done (in GitHub: «Close as not planned» or duplicate).
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
- **Yellow background:** the task is yours, when you have selected **My tasks** (only when you are signed in to docs).
- **The legend** below the chart shows only what is in the chart.
- **Red vertical line:** today's date.
- **Sub-issues:** indented below the parent. The parent has a bracket from the first start to the last end among the sub-issues on the board, forecast included, and the progress after the number, for example «#11 · 1/3» (completed out of all sub-issues, also those on other boards). The colour of the bracket is the parent's status on the board. The dark part is what has happened, as on the bars: the periods when at least one sub-issue was being worked on (from In progress until finished, or until today). A light gap means none of the sub-issues was being worked on then. A **red border** means that at least one sub-issue is delayed, and it shows also when the sub-issues are collapsed. A closed parent has a grey bracket with ✓ when completed, and a hatched bracket with ✕ when closed without being done. The status of the parent is set by hand and does not follow the sub-issues automatically. **▾** before the title collapses the sub-issues, **▸** expands them again. Arrows to and from collapsed sub-issues are hidden.

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
4. Write why the task waits under the heading **Avhengigheter** (dependencies) in the issue, one line per task, for example «- #35: needs legal clarification of consent». The Task form has its own field for this. If the task is in another repository, write for example samt-x/samt-bu-pilot-6#12, with samt-x/ in front, otherwise there is no link. The link itself is always the one in step 3. The text only describes it. See [Conventions](../konvensjoner/).

If you split a task into smaller tasks, make them sub-issues: open the parent and choose **Create sub-issue** or **Add existing issue** at the bottom of the description. The sub-issues must be on the same board to be shown under the parent in the chart.

Dependencies can also be searched for on GitHub with **is:blocked**, **is:blocking** and **blocked-by:**.

If the task waits for something outside GitHub, the label blocked is used instead. It gives no arrow. See [Blocked](../konvensjoner/#blocked) in Conventions.
