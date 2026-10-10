---
title: "Repositories and project boards"
linkTitle: "Setup"
weight: 20

---

This page describes how task management is set up in the GitHub organisation samt-x as of October 2026.

## One repository per board

| Work area | Repository | Project board |
|---|---|---|
| Pilot 1 – Seamless transition between lower and upper secondary school | samt-bu-pilot-1 | Project 1 |
| Pilot 2 – Choice of educational pathway | samt-bu-pilot-2 | Project 2 |
| Pilot 3 – Moving between municipalities | samt-bu-pilot-3 | **Project 4** |
| Pilot 4 – Diplomas | samt-bu-pilot-4 | **Project 3** |
| Pilot 5 – Identifiers in education | samt-bu-pilot-5 | Project 9 |
| Pilot 6 – Parents' access to data | samt-bu-pilot-6 | Project 10 |
| Framework and generic architecture | samt-bu-architecture | Project 5 |
| Information models | information-models | Project 6 |
| Shared tasks across pilots | samt-bu-common-tasks | – |
| The website docs.samt-bu.no | solution-samt-bu-docs | – |
| Task management | solution-task-management | – |

**Note:** Project 3 belongs to Pilot 4, and Project 4 to Pilot 3. The numbers were assigned in the order the boards were created, and cannot be changed.

Project 7 is a template for new boards and is not in use.

The pilot repositories also hold the pilot's pages on docs.samt-bu.no. Tasks and content are therefore in the same repository.

## Board names

All boards are named «SAMT-BU» followed by the work area, for example «SAMT-BU Pilot 3 – Flytting av barn og unge i skoleåret». The prefix distinguishes the boards from other projects participants have in GitHub.

## Automation

Each board has an automatic rule (Auto-add): all open issues in the linked repository are added to the board. When an issue is closed, its status is set to done.

## Fields

The pilot boards use GitHub's default status: Todo, In Progress and Done.

Project 5 (architecture) has a more detailed status flow and its own fields:

| Field | Content |
|---|---|
| Status | Proposed → Backlog → Ready → In progress → In review → Done |
| Responsible | One person who owns the task |
| Contributors | Others contributing |
| Priority | High, Medium or Low |
| Due date | Deadline |

## Access

Access is granted through teams in the organisation. Each pilot has a team with the same name as the repository, for example samt-bu-pilot-3, with write access to the pilot's repository. The core team has write access to all the repositories.

## Exceptions

Two comments given on pages on docs.samt-bu.no appear on the board for Pilot 4, but live in the samt-bu-docs repository. The comment panel on the website only finds comments in that repository, so they cannot be moved.
