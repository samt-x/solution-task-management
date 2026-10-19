---
id: 1d9f85e6-8f58-41b1-8eea-45815cfc56cc
title: "Technical documentation"
linkTitle: "Technical documentation"
weight: 40
lastmod: 2026-10-10T22:27:29+02:00
last_editor: Erik Hagen

---

This page is for whoever administers the boards. It collects what we have learned about what GitHub Projects can and cannot do, and the pitfalls in the user interface.

## What can be done with scripts

GitHub Projects can be managed through GitHub's programming interface (GraphQL). It requires a key with access to projects.

**Can:**

- Create and change fields
- Rename options in a field without losing values, when the option's id is included
- Create views and change name, filter and visible fields
- Copy a board, for example from the template
- Link a board to a repository
- Move issues between repositories

**Cannot:**

- Set grouping («Column by»), nor sorting
- Change automatic rules (workflows). They can only be read, and the filter in a rule is invisible.

Whatever cannot be done with scripts must be done in the browser.

## Pitfalls in the user interface

- **Changes to a view are unsaved** until you press «Save changes». Right below is «Save changes to new view», which creates a new view instead.
- **Automatic rules must be edited with Edit and saved with Save.** If Auto-add is saved without changing the filter, the default filter is stored, which also includes pull requests.
- **The order of options in the programming interface** says nothing about the order of columns in the browser.

## The aggregate board: app and key

The workflow that fills the aggregate board (Project 12) signs in as the GitHub App **SAMT-BU Task sync**, not as a person. The app is owned by the organisation and installed on all repositories.

| | |
|---|---|
| Permissions | Read issues and metadata. Read and write organisation projects. No access to code. |
| Key | Private key as the repository secret `TASK_SYNC_PRIVATE_KEY` in solution-task-management. The App ID is in the variable `TASK_SYNC_APP_ID`. A copy of the key is kept in the project manager's Bitwarden. |
| Token | Created anew on every run and valid for one hour. |
| Runs | Only on schedule and manually, never from pull requests. Secrets are not passed to workflows from forks. |

**Risk:** If the key leaks, it can be used to change or delete boards in the organisation, but not code or issues. The boards can be rebuilt from the issues, but statuses and fields may be lost. The likelihood is low, because the key only exists in the GitHub secret and in Bitwarden.

**If a leak is suspected:** Go to the app's page under the organisation's Settings → Developer settings → GitHub Apps → SAMT-BU Task sync → Credentials → Key pairs. Create a new key, put it in the secret and in Bitwarden, and delete the old one.

**The aggregate board must not have automatic rules.** Auto-close and other rules that write are switched off. Changes made by hand on the aggregate board are overwritten on the next run.

## Moving tasks between repositories

When an issue is moved to another repository, it keeps its comments and history, and stays on the boards it was on. It gets a new number in the new repository. Old links are redirected.

Labels that do not exist in the new repository are dropped.

## New board

1. Copy the template (Project 7) or an existing board
2. Name it «SAMT-BU» followed by the work area
3. Link it to the repository
4. Turn on Auto-add with the filter is:issue is:open, and check that the rule is saved
5. Create a chore issue as a trace
