---
id: 1d9f85e6-8f58-41b1-8eea-45815cfc56cc
title: "Technical documentation"
linkTitle: "Technical documentation"
weight: 40
lastmod: 2026-11-02T03:42:00+01:00
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

The workflow [Timeline](https://github.com/samt-x/solution-task-management/actions/workflows/timeline.yml) runs the script .github/scripts/timeline.py every hour and when run manually. The script reads the boards in PROJECTS (all task boards of the sub-projects and the example board Project 20, not the aggregate board, the portfolio or the templates): status, Start date, Due date, Duration, the status history and the dependencies («Blocked by») of each issue. It draws one SVG per board and language to content/tidslinje/. The example is shown on the page [Timeline](../tidslinje/), and the real boards on the page Tasks and progress of the sub-project that owns the board. The pages embed the charts directly with the theme's inline-svg shortcode, so links and tooltips work. If the chart lives on another page, the shortcode gets the path to it as its second argument: inline-svg "project-5-en.svg" "/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/tidslinje". The charts are thus generated in one place, and the workflow does not write to other repositories. New board: add it to PROJECTS and create the page Tasks and progress, see [Conventions](../konvensjoner/#tasks-and-progress). A plain image would disable them. The ids in a chart include the board number, and for the examples also the situation, so several charts on one page do not collide.

**The arrows.** GitHub's dependencies have no fields of their own. The script therefore builds the arrow tooltip from three sources: «Blocked by» (whether the arrow exists), the event BlockedByAddedEvent in the issue timeline (who linked and when), and the heading Avhengigheter in the body of the waiting issue (why). The heading is read by the function describe: bullet lines starting with an issue reference (#35, samt-x/samt-bu-pilot-6#12, samt-bu-pilot-6#12 or a full link). If a reference there has no matching «Blocked by», no arrow is drawn, but a warning appears below the chart. The link in GitHub is the master, and the text only describes it. Slack and overlap are counted in working days between end and start.

**The dates.** All tasks on the board are drawn. The function plan finds start and end for each task, in the order described on the page [Timeline](../tidslinje/#where-the-dates-come-from). What has happened comes from the events ProjectV2ItemStatusChangedEvent in the issue timeline, filtered on the board (first change to In progress or In review, last change to Done), and from closedAt. Times are converted to the machine's time zone. Duration is a number field in working days on all task boards (not the portfolio), from November 2026. Without Duration, DEFAULT_DAYS (5) is assumed. A start calculated from the dependencies goes through the blocking tasks recursively, with protection against dependencies in a ring. Blocking tasks on other boards are not counted. The bar has three styles: light with border when both dates are set or have happened, dashed when one is calculated, and dark on top for what has happened. Late start (late_s) is a start from Start date, or calculated with a Duration someone has set, that has passed without the task having started. It gives a yellow border and line. Planned end (planned) is Due date, or start plus a Duration someone has set. For open tasks a forecast (f) is calculated: the actual start, otherwise the latest of today, Start date and the day after the tasks being waited for are expected to finish, plus the duration (Duration, otherwise the working days from Start date to Due date). If f is after planned, the part after the due date is filled red, solid until today and light after. The arrows and dependencies use f, so delays propagate. Closed tasks are told apart by stateReason: COMPLETED gives ✓, NOT_PLANNED and DUPLICATE (DROPPED) give ✕ and a hatched bar without a dark part. The inline-svg shortcode shows the chart at full size in a frame that scrolls both ways, with a toolbar for zoom (− / + / 100 % / Fit width, and Ctrl + mouse wheel over the chart), dragging with the mouse (if the mouse moves more than 5 pixels, the click is swallowed, so links do not open) and a link to the SVG file on its own. Boards in NO_HISTORY (the example board) read Start date and Due date as what has happened for tasks that have started or finished, because the dates are moved every week.

**The window.** A click on an issue link in the chart is caught by partials/issue-popup.html in the theme, included by inline-svg. It fetches the issue from GitHub's REST API with Accept: application/vnd.github.html+json and shows body_html, GitHub's own sanitised rendering. GitHub cannot be shown in an iframe. Logged-in users use their own token (getStoredToken), others go without a token (about 60 lookups an hour per IP). Responses are kept in memory while the page is open. The arrows have class tl-dep, which puts the tooltip at the top of the window. The window can be moved (pointer events on the title bar) and resized (CSS resize). It closes with Esc, × or a click outside the window on something that is not clickable (link, button, form field). The click only counts when the mouse also went down outside the window, so a move or resize released outside does not close it.

**Sub-issues, filter and My tasks** ([solution-task-management#44](https://github.com/samt-x/solution-task-management/issues/44)). The script also fetches parent, subIssuesSummary (completed, total) and assignees for each issue, and the field Responsible (single select with GitHub user names as options). The function summarize gives each task depth and kids (the sub-issues on the board). A parent with children on the board gets start, end and forecast from the children (the deepest first) and no delays of its own, and is drawn as a bracket: the colour from the parent's status (COLORS), a dark fill for what has happened (the function worked: the periods from started to ended, or until today, for the sub-issues down the tree, cancelled ones excluded, merged where they meet; a gap means nobody was working; the progress from subIssuesSummary is only shown as text), a red border when is_late holds for at least one child, grey when the parent is closed and hatched when it is cancelled (DROPPED). The function order puts the children right below the parent. The chart gets data attributes used by the script in the inline-svg shortcode: svg has data-tl, data-tl-top and data-tl-rowh; each row is a group g.tl-row with data-key, data-parent, data-y (original y), data-state (open, done or dropped), data-late and data-people (assignees and Responsible); the arrows have data-from, data-to, data-x1 and data-x2. The stripes (tl-stripe), the weekends (tl-vh), the vertical lines (tl-vy2) and everything below the rows (tl-foot) are fitted to the number of visible rows. On folding and filtering the script moves the visible rows with transform, redraws the arrows with the same rule as timeline.py, and changes the height of the chart. The buttons ▾/▸ (g.tl-fold) have display="none" in the file and are only shown by the script, so the chart without JavaScript, and «Open the chart in a new window», is as before. My tasks is only shown when localStorage has samt-bu-gh-user (set on login to docs), and compares case-insensitively.

**The legend and examples per situation** ([solution-task-management#45](https://github.com/samt-x/solution-task-management/issues/45)). While the chart is drawn, the script collects what has actually been drawn (the set used: arrows, rings, ⛔, dark, light and dashed parts, late start, red after the due date, ✓, ✕, brackets, ▾/▸ and, when a task has an assignee or Responsible, yellow for My tasks). The legend shows only these, in a fixed order. The height depends on the legend, so the top of the SVG is added last. For boards in EXAMPLES (the example board), one extra chart is made per label starting with example/, for example example/sub-issues → content/tidslinje/example-sub-issues-nb.svg, with only the examples that have the label. An example can have several labels. Tasks that are waited for but do not have the label are not in the chart: the arrow is missing, ⛔ is still shown, and the tooltip says «not in the chart». The labels are fetched with labels in the same query.

The chart includes today's date, so it changes at least once a day. The workflow only commits when a chart has changed. Commits by github-actions[bot] do not trigger Trigger rebuild, so the workflow itself asks samt-bu-docs to rebuild, using the organisation secret DOCS_REBUILD_TOKEN. Reading uses the same app as the aggregate board.

Locally: run the script with gh auth token. --out writes the charts to another folder, --data reads the tasks from a JSON file instead of the API, and --today sets today's date. Dependencies can only be set in GitHub or via REST (repos/…/issues/N/dependencies/blocked_by), not with gh before version 2.94.

Background: [solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32).

## The example board

The examples used in the documentation live in the repository [solution-task-management-examples](https://github.com/samt-x/solution-task-management-examples) and on [Project 20](https://github.com/orgs/samt-x/projects/20) «[EXAMPLE] Timeline». The repository is listed in EXCLUDE in sync-all-tasks.py, so the examples do not reach the aggregate board.

**The dates follow today's date.** Before the timeline is drawn, Timeline runs the script .github/scripts/example-dates.py. It reads .github/scripts/example-dates.json, which has the start and due date for each issue in days from Monday this week (null = no date), and optionally Duration as a third number, and writes Start date, Due date and Duration on the board with the app's token. Saturday and Sunday count as the next week, otherwise ongoing examples would pass their due date at the weekend. Only fields that differ are written, so the dates change once a week. The board is still the master, and the chart and the board show the same thing. Status, dependencies and descriptions are set in GitHub as usual. --dry-run shows what would be changed.

**New example:** create the issue in the example repository with the line «Eksempel, ikke en oppgave» (example, not a task) first, add it to the board, give it the label for the situation (example/…), and add its number with offsets to example-dates.json. **New situation:** create the label example/<situation> in the example repository, give it to the examples, and add a subsection with inline-svg "example-<situation>-en.svg" (and -nb) under Examples on the page Timeline. The chart appears on the next run. Background: [solution-task-management#40](https://github.com/samt-x/solution-task-management/issues/40).

## Scheduled runs

Three workflows in solution-task-management run on a schedule:

| Workflow | When | What it updates |
|---|---|---|
| [Sync All tasks](https://github.com/samt-x/solution-task-management/actions/workflows/sync-all-tasks.yml) | 17 minutes past every hour | The aggregate board (Project 12) |
| [Timeline](https://github.com/samt-x/solution-task-management/actions/workflows/timeline.yml) | 17 minutes past every hour | The timelines on docs, and the dates on the example board |
| [Snapshot status](https://github.com/samt-x/solution-task-management/actions/workflows/snapshot-status.yml) | 47 minutes past every hour | The status history in status/ |

**The engine is GitHub Actions.** The schedule is a schedule with cron in each workflow. GitHub starts the run on its own machines, so no server of ours is needed. All three can also be run by hand with «Run workflow». GitHub does not guarantee the time: runs can be delayed when GitHub is busy, and on rare occasions dropped. That is why the full hour is not used.

**Fixed scripts, not AI.** The workflows run Python scripts that follow the rules described here and on the page [Timeline](../tidslinje/). No AI judges anything along the way. A case nobody has thought of therefore either gets an answer from the rules, which always have a last resort (for example start today and an assumed duration of one week), or the script stops with an error. Then nothing is committed, and the previous result stays. The date below the timeline shows when the chart was made.

**Failures are reported as an issue.** The last step in each workflow runs the script .github/scripts/workflow-alert.py. If a step fails, it creates the issue «Workflow failed: <name>» with the type Problem and a link to the run. The issue lands on Project 18 through Auto-add. If the workflow fails again, a comment is added to the same issue. The next successful run closes it, with a comment. The script uses the workflow's own token (GITHUB_TOKEN with issues: write). Timeline has the option test_failure when run by hand, which fails on purpose, so the reporting can be tested ([solution-task-management#41](https://github.com/samt-x/solution-task-management/issues/41) was the test).

**The schedule can be switched off.** GitHub switches off scheduled workflows in public repositories after 60 days without activity in the repository. Then nothing runs, and no failure is reported. Timeline and Snapshot status commit at least once a day themselves, so as long as they work, there is activity. If a workflow has been switched off, switch it on again under Actions → the workflow → «Enable workflow». The risk is followed up in [solution-task-management#42](https://github.com/samt-x/solution-task-management/issues/42).

## Moving tasks between repositories

When an issue is moved to another repository, it keeps its comments and history, and stays on the boards it was on. It gets a new number in the new repository. Old links are redirected.

Labels that do not exist in the new repository are dropped.

## New board

1. Copy the template (Project 7) or an existing board
2. Name it «SAMT-BU» followed by the work area
3. Link it to the repository
4. Turn on Auto-add with the filter is:issue is:open, and check that the rule is saved
5. Create a chore issue as a trace
