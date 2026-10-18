---
id: 072203ad-55a2-401b-8cb6-c6aee71f598d
title: "User guide"
linkTitle: "User guide"
weight: 10
lastmod: 2026-10-18T19:38:42+02:00
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
2. Write a short title saying what is to be done
3. Describe the background, what is to be done, and when the task is finished
4. Assign the task to whoever will work on it (**Assignees**), if they have a GitHub user
5. Save

In the pilot repositories, samt-bu-architecture and information-models, the task is added automatically to the repository's project board. The other repositories have no board of their own.

## Following up

The project boards are under **Projects** in the samt-x organisation, or via the link in the repository. On the board you can move the task between status columns, and set owner, priority and deadline where the board has such fields.

### My tasks across all boards

The search **[My open tasks in samt-x](https://github.com/issues?q=is%3Aissue%20is%3Aopen%20assignee%3A%40me%20org%3Asamt-x)** lists all open tasks assigned to you, in every repository in the organisation. You must be signed in to GitHub. Consider bookmarking the link.

This search and several others, together with links to all the boards, are collected under [Project governance → Tasks and follow-up](https://docs.samt-bu.no/en/prosjektstyring/oppgaver-og-oppfolging/).

- The search only lists tasks where you are an **Assignee**. That is why assigning tasks matters, see [Conventions](../konvensjoner/).
- The architecture group's project board also has the view **[My tasks (this project)](https://github.com/orgs/samt-x/projects/5/views/7)**, which lists your tasks on that board, with the board's own fields.
- **Assigned to me** in GitHub shows the same as the search, but also from other organisations you belong to.

## Closing a task

- Always write a **closing comment** on the outcome, with a link to the page, document or change
- Close as **completed** when the task is done, and as **not planned** when it is dropped – and say why
- The status on the board is set to done automatically when the task is closed
