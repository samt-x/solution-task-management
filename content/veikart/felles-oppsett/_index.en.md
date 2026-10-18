---
id: e5ac13b4-873a-45e7-9405-f56a42e5731a
title: "Shared setup for the project boards"
linkTitle: "Shared setup"
weight: 10
lastmod: 2026-10-18T17:26:48+02:00
last_editor: Erik Hagen

---

The pilots and sub-projects currently use different statuses, fields and views on their boards, which makes it hard to see them together. The goal is not for everyone to use the same setup, but for the setups to be **compatible**.

## The principle

- Two or three **templates** are made for project boards, for example a simple one and an extended one. Each pilot or sub-project chooses the one that suits it.
- Each status in a template maps to exactly one status in a **shared, coarser reporting level**. A board with more steps, for example a separate refinement step, can therefore always be reported in the shared setup.
- **Blocked is a flag, not a step.** A task can become blocked at any step, and this must be visible in the shared reporting.

The statuses of the templates and the shared level are set in step M1.

## Steps

| Step | Content | Issue |
|---|---|---|
| [M1 Templates and shared status model](https://github.com/samt-x/solution-task-management/milestone/1) | The templates, their statuses and how they map to the shared level. The existing template, Project 7, is updated. | [solution-task-management#4](https://github.com/samt-x/solution-task-management/issues/4) |
| [M2 Templates in use](https://github.com/samt-x/solution-task-management/milestone/2) | Each board chooses a template and is converted, without losing the status of existing tasks. | [solution-task-management#6](https://github.com/samt-x/solution-task-management/issues/6) |
