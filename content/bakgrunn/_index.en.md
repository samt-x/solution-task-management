---
id: 9e40a003-0e64-4205-ab23-7b39c52788e7
title: "Background and rationale"
linkTitle: "Background"
weight: 5
lastmod: 2026-10-11T00:43:18+02:00
last_editor: Erik Hagen

---

This page explains why SAMT-BU manages tasks in GitHub, and how the setup has evolved.

## The need

SAMT-BU is a collaboration between many organisations, none of which is superior to the others. Tasks therefore need to live somewhere all participants can see and contribute, regardless of which organisation they come from.

The project has three kinds of tasks:

- **Pilot tasks** – work belonging to one specific pilot
- **Cross-cutting tasks** – shared terminology, overall architecture, methodology, preparations for workshops and clarifications that affect everyone
- **The core team's internal allocation** – who in the core team does what, and by when

## Why GitHub for task management

The content of docs.samt-bu.no already lives in GitHub. When tasks are in the same repository as the content they concern, a task can link directly to the change that resolves it, and vice versa.

GitHub requires no new software or licences. Participants already have accounts, and everything is open to everyone in the organisation.

> **Note:** The way of working is not tied to GitHub. The same can be done in other git-based solutions such as GitLab, Forgejo or Codeberg, several of which can be self-hosted. GitHub has been chosen for now because the project's content and partners are already there. GitHub is not open source, so the choice is debatable from a digital sovereignty perspective. The rationale and trade-offs are described under [Platform choice: GitHub](/en/prosjektleveranser/loesninger/samhandlingsplattform/plattformvalg/). The alternatives are also discussed under [Co-creation → Task management](/en/utkast/temaer/samskaping/oppgavestyring/).

## How it was, and how it became

**Until autumn 2026**, all pilot tasks were in one shared repository, «Oppgaver» (Tasks), and each task was labelled with the pilot it belonged to. Each pilot had its own project board, which pulled tasks from the shared repository. Cross-cutting tasks had no natural home, and were either labelled with an arbitrary pilot, put in Planner, or not written down at all.

This was raised in a proposal in August 2026: [Suggestion: wider use of GitHub for task management](/en/utkast/diverse/github-oppgavestyring/).

**In October 2026** the setup was reorganised to one repository per project board:

- Each pilot got its own repository, holding both the pilot's pages on docs.samt-bu.no and the pilot's tasks
- Pilot tasks were moved from «Oppgaver» to the pilots' own repositories
- «Oppgaver» was renamed samt-bu-common-tasks, and is now used only for tasks shared across pilots
- Generic architecture and the final deliverable got their own repository, samt-bu-architecture, with a separate board for the architecture group

The benefit is that it is unambiguous where a task belongs, and that access can be granted per pilot.

## Relationship to Planner

The core team still uses Planner for internal allocation. This solution does not change that.

Should Planner's role be reconsidered later – for reasons of licensing, accessibility or digital sovereignty – there are project tools that integrate with GitHub. A nearby example is [OpenProject](https://interoperable-europe.ec.europa.eu/eu-oss-catalogue/solutions/openproject), which is open source and listed in the EU catalogue of open source solutions for the public sector. That is a separate question and should be handled separately.

## Discussion of principles

Why open task management is considered good practice in collaboration between equal organisations is discussed under [Co-creation → Task management](/en/utkast/temaer/samskaping/oppgavestyring/).
