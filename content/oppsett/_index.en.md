---
id: bb682277-9c1d-46fb-8611-aae1f1f8fced
title: "Repositories and project boards"
linkTitle: "Setup"
weight: 20
lastmod: 2026-10-27T23:11:04+01:00
last_editor: Erik Hagen

---

This page describes how task management is set up in the GitHub organisation samt-x as of October 2026.

## One repository per board

| Work area | Repository | Project board | Template |
|---|---|---|---|
| Pilot 1 – Seamless transition between lower and upper secondary school | samt-bu-pilot-1 | Project 1 | Standard |
| Pilot 2 – Choice of educational pathway | samt-bu-pilot-2 | Project 2 | Standard |
| Pilot 3 – Moving between municipalities | samt-bu-pilot-3 | **Project 4** | Standard |
| Pilot 4 – Diplomas | samt-bu-pilot-4 | **Project 3** | Standard |
| Pilot 5 – Identifiers in education | samt-bu-pilot-5 | Project 9 | Standard |
| Pilot 6 – Parents' access to data | samt-bu-pilot-6 | Project 10 | Standard |
| Pilot 7 – Digital dialogue between kindergarten/school and home | samt-bu-pilot-7 | Project 19 | Standard |
| Framework and generic architecture | samt-bu-architecture | Project 5 | Standard |
| Information models | information-models | Project 6 | Standard |
| Shared tasks across pilots | samt-bu-common-tasks | – | – |
| The website docs.samt-bu.no | solution-samt-bu-docs | [Project 17](https://github.com/orgs/samt-x/projects/17) | Standard |
| Task management | solution-task-management | [Project 18](https://github.com/orgs/samt-x/projects/18) | Standard |
| The portfolio (one card per work area) | samt-bu-portfolio | [Project 13](https://github.com/orgs/samt-x/projects/13) | Own setup |

**Note:** Project 3 belongs to Pilot 4, and Project 4 to Pilot 3. The numbers were assigned in the order the boards were created, and cannot be changed.

Project 7 is the template for new boards, see below. Project 11 is a former template kept for reference. [Project 12](https://github.com/orgs/samt-x/projects/12) «SAMT-BU Overview – All tasks» is the aggregate board, see The aggregate board below. Project 13 is the portfolio board, with one card per pilot, product and work area. Its Status field is the phase. The field Sub-issues progress shows the progress of the tasks linked to the card as sub-issues. The field Objective has only a test value for now, until the goals are decided. The rule «Auto-add sub-issues to project» is switched off, so that the tasks do not end up on the portfolio board. The overview boards are called «SAMT-BU Overview – …», so that they stand apart from the sub-projects in the list of boards.

The pilot repositories also hold the pilot's pages on docs.samt-bu.no. Tasks and content are therefore in the same repository.

## Board names

All boards are named «SAMT-BU» followed by the work area, for example «SAMT-BU Pilot 3 – Flytting av barn og unge i skoleåret». The prefix distinguishes the boards from other projects participants have in GitHub.

## Automation

Each board has an automatic rule (Auto-add): all open issues in the linked repository are added to the board. When an issue is closed, its status is set to done. New cards get the status Proposed (the workflow «Item added to project»), so that new input lands there until it has been considered.

**Status history:** The fields on a board have no history. The workflow [Snapshot status](https://github.com/samt-x/solution-task-management/actions/workflows/snapshot-status.yml) therefore writes the status of Project 5 to the file [status/project-5.md](https://github.com/samt-x/solution-task-management/blob/main/status/project-5.md) in solution-task-management, every hour and when run manually. The file only gets a new commit when something has changed, so the [history of the file](https://github.com/samt-x/solution-task-management/commits/main/status/project-5.md) shows how statuses and comments have changed over time. More boards can be added later ([M4 Comment field in the templates](https://github.com/samt-x/solution-task-management/issues/16)).

## The template for new boards

| Template | Board | Statuses |
|---|---|---|
| Standard | Project 7 «[TEMPLATE] Standard board» | Proposed, To do, Ready, In progress, In review, Done |

The Simple template (Project 11) was retired in October 2026, and Pilot 3 (Project 4), the only board that used it, got the statuses Ready and In review without any task losing its status. Project 11 is now called «[REFERENCE] Simple board», is no longer marked as a template and therefore does not show in New project. It is kept to be able to test the shared level across boards with different steps ([solution-task-management#22](https://github.com/samt-x/solution-task-management/issues/22)).

The template has the fields Responsible, Priority, Effort, Estimate (person-days), Start date and Due date, and five views: Board (kanban by status), By responsible (kanban by responsible person), Open tasks, My tasks and Timeline. What the statuses and fields mean is described under [Conventions](/en/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/konvensjoner/).

**Issue types** are defined for the whole organisation (Settings → Planning → Issue types, requires owner rights): Task, Solution proposal, Question, Decision, Risk and Problem (called Bug until October 2026, same id). The Type field is switched on in all views of the template and in Project 5, except Timeline. Boards created from the templates before October 2026 must have the field switched on by hand: View → Fields → Type → Save view, and confirm in the dialog.

**Issue forms** live in the repository [samt-x/.github](https://github.com/samt-x/.github), under `.github/ISSUE_TEMPLATE/`: one form per type, with the type name in English and the text in Norwegian. Each form sets the type with `type:`, and all have the fields «Gjelder» (concerns) and «Forslag til hvem som bør se på dette» (suggestion for who should look at this). The forms apply to every repository in the organisation that has no forms of its own. A repository with its own `.github/ISSUE_TEMPLATE/` uses only its own, so do not add forms to a single repository without copying the shared ones. Blank issue is still enabled (`config.yml`), and the list has a link to Conventions. The forms do not set a board (`projects:`). A shared form cannot point to the right board for each repository, and the repositories that have a board add new issues to it automatically. The repository must be public for the forms to work in the public repositories. Locally it is cloned to `samt-x-dotgithub/` in the workspace, because the scripts for all repositories skip folders starting with a dot.

The templates are visible to all members of the organisation, but not to others. Members have read access (Base role Read). That is enough to create boards from the templates, but not to change them. The templates must not be closed, because they then disappear from New project.

To create a new board:

1. Choose New project in the organisation and pick the Standard template.
2. Name the board following the pattern below.
3. Link the board to the repository, and set the rule for automatic adding (see Automation).
4. Add the people as options in the Responsible field.

The boards that existed before the templates were moved over to them in October 2026 ([M2 Templates in use](https://github.com/samt-x/solution-task-management/issues/6)). The statuses were renamed, and no task lost its status. Project 5 also has the fields Contributors and Comment and the views All tasks and Closed tasks. The status Proposed first existed only on Project 5. It was added to the templates and to all boards on 27 October 2026, without any task losing its status ([solution-task-management#20](https://github.com/samt-x/solution-task-management/issues/20)).

## The aggregate board

[Project 12 «SAMT-BU Overview – All tasks»](https://github.com/orgs/samt-x/projects/12) collects all issues in the public repositories. Private repositories are not included. The status is translated to the shared level (see [Conventions](/en/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/konvensjoner/)): Not started, In progress or Done. Closed issues become Done, and open issues without a board become Not started. The field Source status shows the board and the status the task has there.

The board is filled by the workflow [Sync All tasks](https://github.com/samt-x/solution-task-management/actions/workflows/sync-all-tasks.yml) in the repository solution-task-management, every hour and when run manually. The sync goes one way only, and never writes to the project boards. All automatic rules on the aggregate board are switched off, and must stay that way. Access is described under [Technical documentation](/en/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/teknisk-dokumentasjon/).

## Access

Access is granted through teams in the organisation. Each pilot has a team with the same name as the repository, for example samt-bu-pilot-3, with write access to the pilot's repository. The core team has write access to all the repositories.

## Exceptions

Two comments given on pages on docs.samt-bu.no appear on the board for Pilot 4, but live in the samt-bu-docs repository. The comment panel on the website only finds comments in that repository, so they cannot be moved.
