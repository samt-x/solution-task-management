---
id: 7c264c4f-711d-400b-a2df-30ad7e6745c9
title: "Task management"
linkTitle: "Task management"
weight: 20
lastmod: 2026-10-18T19:59:20+02:00
last_editor: Erik Hagen

---

This section documents how SAMT-BU manages tasks in GitHub: where tasks live, how they are organised, and which rules we follow. It is aimed at everyone who creates, follows up or administers tasks in the project – pilot participants, the architecture group and the core team.

The solution consists of the following parts:

| Part | Role |
|------|------|
| **GitHub Issues** | Each task is an issue in the repository where the responsibility lies |
| **GitHub Projects** | One project board per pilot or work area, with status, owner and deadlines |
| **Teams in the GitHub organisation** | Give participants access to the right repositories and boards |
| **Conventions** | Shared rules for labelling, describing and closing tasks |

A **project board** is a project in GitHub (GitHub Projects): a collection of tasks with shared fields, such as status, owner and deadline. The same board can be shown in several ways, and each view has its own tab on the board:

- **Kanban board** (in GitHub: Board): one column per step in the workflow, for example New, In progress and Done. Each task is a card that moves from left to right as the work progresses. The columns can also be based on another field, for example owner or priority.
- **Table**: one row per task, with the fields as columns. Useful for sorting and filtering.
- **Timeline** (Roadmap): the tasks placed along a time axis by date.

Moving a card to another column changes the field the columns are based on, usually status. The change shows in all views, because it is the same task.

The main principle is **one repository per project board**: each pilot has its own repository holding both content and tasks, and its own board. Shared tasks and generic architecture have their own repositories.

Status: the solution is in use. The setup was reorganised in autumn 2026, see [Background](bakgrunn/). The conventions are current practice, with one open question for the architecture group.

**Your tasks and the boards** are under [Project governance → Tasks and follow-up](https://docs.samt-bu.no/en/prosjektstyring/oppgaver-og-oppfolging/). This section describes the solution behind them.

See the subsections for guidance, setup, conventions and the [roadmap](veikart/).
