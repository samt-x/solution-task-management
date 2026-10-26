---
id: 072203ad-55a2-401b-8cb6-c6aee71f598d
title: "User guide"
linkTitle: "User guide"
weight: 10
lastmod: 2026-10-26T03:10:45+01:00
last_editor: Erik Hagen

---

This page explains where a task should live, and how to create, follow up and close it.

## Where should the task live?

Create the task in the repository where the **responsibility** lies. Ask the questions in this order:

| Question | If yes, put the task in |
|---|---|
| Does it concern one specific pilot? | The pilot's repository, samt-bu-pilot-1 to samt-bu-pilot-6 |
| Does it concern several pilots, or the pilots as a whole? | samt-bu-common-tasks |
| Does it concern generic architecture or the final deliverable (the framework)? | samt-bu-architecture |
| Does it concern the website docs.samt-bu.no itself (bugs, new features)? | solution-samt-bu-docs |
| Does it concern how we manage tasks? | solution-task-management |

If in doubt, put it where you think it fits best. Tasks can be moved between repositories without losing anything.

**One task, one place.** Never copy a task to another repository. If it affects several, link instead – see [Conventions](../konvensjoner/).

## Creating a task

1. Go to the repository, choose **Issues** and **New issue**
2. Choose the form for the issue's type: Task, Solution proposal, Question, Decision, Risk or Bug. See [Conventions](../konvensjoner/) for what they mean. The form sets the type for you.
3. Write a short title saying what the issue is about, and fill in the fields. Only the first fields are required. The forms are in Norwegian.
4. In the field **Gjelder** (concerns) you can paste a link to what the issue is about: a page on docs, a case, another task or an element in the Archi model.
5. Assign the issue to whoever will work on it (**Assignees**), if they have a GitHub user. **Exception:** if the issue is input that has not yet been considered, do not assign it. Write @username in the field **Forslag til hvem som bør se på dette** (suggestion for who should look at this) instead. They get a notification and can follow the issue.
6. Save with **Create**

The forms apply to all repositories in samt-x. To write freely, choose **Blank issue** at the bottom of the list, and set the type yourself in the **Type** field on the right.

In the pilot repositories, samt-bu-architecture and information-models, the task is added automatically to the repository's project board. The other repositories have no board of their own.

## Following up

The project boards are under **Projects** in the samt-x organisation, or via the link in the repository. On the board you can move the task between status columns, and set owner, priority and deadline where the board has such fields.

### My tasks across all boards

The search **[My open tasks in samt-x](https://github.com/issues?q=is%3Aissue%20is%3Aopen%20assignee%3A%40me%20org%3Asamt-x)** lists all open tasks assigned to you, in every repository in the organisation. You must be signed in to GitHub. Consider bookmarking the link.

This search and several others, together with links to all the boards, are collected under [Project governance → Tasks and follow-up](https://docs.samt-bu.no/en/prosjektstyring/oppgaver-og-oppfolging/).

- The search only lists tasks where you are an **Assignee**. That is why assigning tasks matters, see [Conventions](../konvensjoner/).
- The architecture group's project board also has the view **[My tasks (this project)](https://github.com/orgs/samt-x/projects/5/views/7)**, which lists your tasks on that board, with the board's own fields.
- **Assigned to me** in GitHub shows the same as the search, but also from other organisations you belong to.

### Status comment in the architecture meeting

Project 5 has the field **Comment**, which shows the latest status of each task. To update it:

1. Open the view [All tasks](https://github.com/orgs/samt-x/projects/5/views/1). Each row is one task.
2. Find the row for your task. The Responsible column shows who owns it.
3. Double-click the cell in the Comment column, write the date and status, for example «23.10: Draft sent to Anders», and press Enter.

Overwrite the old comment. The field holds a single line, and the previous one is kept in the [status history](https://github.com/samt-x/solution-task-management/commits/main/status/project-5.md), which is updated every hour.

**Reading the whole comment:** Long comments are cut off in the table. Click the title of the task to open a panel on the right with the whole comment and the other fields. To see all the comments together, use the [status table](https://github.com/samt-x/solution-task-management/blob/main/status/project-5.md), which is also updated every hour.

## Closing a task

- Always write a **closing comment** on the outcome, with a link to the page, document or change
- Close as **completed** when the task is done, as **not planned** when it is rejected, aborted or cancelled, and as **duplicate** when it already exists – and say why
- The status on the board is set to done automatically when the task is closed
