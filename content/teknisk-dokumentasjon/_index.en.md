---
title: "Technical documentation"
linkTitle: "Technical documentation"
weight: 40

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

## Moving tasks between repositories

When an issue is moved to another repository, it keeps its comments and history, and stays on the boards it was on. It gets a new number in the new repository. Old links are redirected.

Labels that do not exist in the new repository are dropped.

## New board

1. Copy the template (Project 7) or an existing board
2. Name it «SAMT-BU» followed by the work area
3. Link it to the repository
4. Turn on Auto-add with the filter is:issue is:open, and check that the rule is saved
5. Create a chore issue as a trace
