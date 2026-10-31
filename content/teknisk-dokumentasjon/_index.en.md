---
id: 1d9f85e6-8f58-41b1-8eea-45815cfc56cc
title: "Technical documentation"
linkTitle: "Technical documentation"
weight: 40
lastmod: 2026-10-31T02:11:13+01:00
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
- Decide the order of columns in a view. Visible fields can be chosen, but a new field always ends up on the right and must be dragged into place in the browser.
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
| Key | Private key as the repository secret `TASK_SYNC_PRIVATE_KEY` in solution-task-management. The app's Client ID is in the workflow. A copy of the key is kept in the project manager's Bitwarden. |
| Token | Created anew on every run and valid for one hour. |
| Runs | Only on schedule and manually, never from pull requests. Secrets are not passed to workflows from forks. |

**Risk:** If the key leaks, it can be used to change or delete boards in the organisation, but not code or issues. The boards can be rebuilt from the issues, but statuses and fields may be lost. The likelihood is low, because the key only exists in the GitHub secret and in Bitwarden.

**If a leak is suspected:** Go to the app's page under the organisation's Settings → Developer settings → GitHub Apps → SAMT-BU Task sync → Credentials → Key pairs. Create a new key, put it in the secret and in Bitwarden, and delete the old one.

**The aggregate board must not have automatic rules.** Auto-close and other rules that write are switched off. Changes made by hand on the aggregate board are overwritten on the next run.

## Status snapshot

The workflow [Snapshot status](https://github.com/samt-x/solution-task-management/actions/workflows/snapshot-status.yml) runs the script .github/scripts/snapshot-status.py every hour and when run manually. The script reads the boards in PROJECTS and writes one Markdown table per board to status/. The workflow only commits when the file has changed, and the message has [skip ci], so docs is not rebuilt. The file has no timestamp; the commit date is the time.

The script uses the same app and key as the aggregate board, but only to read the boards. The commit is made with the workflow's own token (GITHUB_TOKEN), which only applies to this repository. The script can also be run locally with gh auth token.

Background: [solution-task-management#15](https://github.com/samt-x/solution-task-management/issues/15).

## Timeline with dependencies

The workflow [Timeline](https://github.com/samt-x/solution-task-management/actions/workflows/timeline.yml) runs the script .github/scripts/timeline.py every hour and when run manually. The script reads the boards in PROJECTS (currently Project 5 and 18): status, Start date, Due date and the dependencies («Blocked by») of each issue. It draws one SVG per board and language to content/tidslinje/, shown on the page [Timeline](../tidslinje/). The page embeds the charts directly with the theme's inline-svg shortcode, so links and tooltips work. A plain image would disable them. The ids in a chart include the board number, so several charts on one page do not collide.

**The arrows.** GitHub's dependencies have no fields of their own. The script therefore builds the arrow tooltip from three sources: «Blocked by» (whether the arrow exists), the event BlockedByAddedEvent in the issue timeline (who linked and when), and the heading Avhengigheter in the body of the waiting issue (why). The heading is read by the function describe: bullet lines starting with an issue reference (#35, samt-bu-pilot-6#12 or a full link). If a reference there has no matching «Blocked by», no arrow is drawn, but a warning appears below the chart. The link in GitHub is the master, and the text only describes it. Slack and overlap are counted in whole days between due date and start date.

The chart includes today's date, so it changes at least once a day. The workflow only commits when a chart has changed. Commits by github-actions[bot] do not trigger Trigger rebuild, so the workflow itself asks samt-bu-docs to rebuild, using the organisation secret DOCS_REBUILD_TOKEN. Reading uses the same app as the aggregate board.

Locally: run the script with gh auth token. --out writes the charts to another folder, --data reads the tasks from a JSON file instead of the API, and --today sets today's date. Dependencies can only be set in GitHub or via REST (repos/…/issues/N/dependencies/blocked_by), not with gh before version 2.94.

Background: [solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32).

## Moving tasks between repositories

When an issue is moved to another repository, it keeps its comments and history, and stays on the boards it was on. It gets a new number in the new repository. Old links are redirected.

Labels that do not exist in the new repository are dropped.

## New board

1. Copy the template (Project 7) or an existing board
2. Name it «SAMT-BU» followed by the work area
3. Link it to the repository
4. Turn on Auto-add with the filter is:issue is:open, and check that the rule is saved
5. Create a chore issue as a trace
