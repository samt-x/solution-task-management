---
id: bb682277-9c1d-46fb-8611-aae1f1f8fced
title: "Repoer og prosjektbrett"
linkTitle: "Oppsett"
weight: 20
lastmod: 2026-10-18T22:24:53+02:00
last_editor: Erik Hagen

---

Denne siden beskriver hvordan oppgavestyringen er satt opp i GitHub-organisasjonen samt-x per oktober 2026.

## Ett repo til ett brett

| Arbeidsområde | Repo | Prosjektbrett | Mal |
|---|---|---|---|
| Pilot 1 – Overgang ungdomsskole–videregående | samt-bu-pilot-1 | Project 1 | Standard |
| Pilot 2 – Valg av utdanningsløp | samt-bu-pilot-2 | Project 2 | Standard |
| Pilot 3 – Flytting av barn og unge i skoleåret | samt-bu-pilot-3 | **Project 4** | Enkel |
| Pilot 4 – Vitnemål | samt-bu-pilot-4 | **Project 3** | Standard |
| Pilot 5 – Id-er i utdanning | samt-bu-pilot-5 | Project 9 | Standard |
| Pilot 6 – Foreldres tilgang til data | samt-bu-pilot-6 | Project 10 | Standard |
| Rammeverk og generisk arkitektur | samt-bu-architecture | Project 5 | Standard + Proposed |
| Informasjonsmodeller | information-models | Project 6 | Standard |
| Felles oppgaver på tvers av pilotene | samt-bu-common-tasks | – | – |
| Nettstedet docs.samt-bu.no | solution-samt-bu-docs | – | – |
| Oppgavestyring | solution-task-management | – | – |

**Merk:** Project 3 hører til Pilot 4, og Project 4 til Pilot 3. Numrene ble tildelt i den rekkefølgen brettene ble opprettet, og kan ikke endres.

Project 7 og Project 11 er maler for nye brett, se under.

Pilotrepoene inneholder også pilotens sider på docs.samt-bu.no. Oppgavene og innholdet ligger dermed i samme repo.

## Navn på brettene

Alle brett heter «SAMT-BU» etterfulgt av arbeidsområdet, for eksempel «SAMT-BU Pilot 3 – Flytting av barn og unge i skoleåret». Prefikset skiller brettene fra andre prosjekter deltakerne har i GitHub.

## Automatikk

Hvert brett har en regel for automatisk innlegging (Auto-add): alle åpne issues i det tilknyttede repoet legges på brettet. Når et issue lukkes, settes statusen til ferdig.

## Maler for nye brett

| Mal | Brett | Statuser |
|---|---|---|---|
| Enkel | Project 11 «[TEMPLATE] Simple board» | To do, In progress, Done | Standard |
| Standard | Project 7 «[TEMPLATE] Standard board» | To do, Ready, In progress, In review, Done | Standard |

Begge malene har feltene Responsible, Priority, Effort, Estimate (person-days), Start date og Due date, og fem visninger: Board (kanban per status), By responsible (kanban per ansvarlig), Open tasks, My tasks og Timeline. Hva statusene og feltene betyr, står under [Konvensjoner](../konvensjoner/).

Slik lages et nytt brett:

1. Velg New project i organisasjonen og velg en av malene.
2. Gi brettet navn etter mønsteret under.
3. Koble brettet til repoet, og sett regelen for automatisk innlegging (se Automatikk).
4. Legg inn personene som valg i feltet Responsible.

Brettene som fantes før malene, ble lagt over på dem i oktober 2026 ([M2 Malene tatt i bruk](https://github.com/samt-x/solution-task-management/issues/6)). Statusene fikk nye navn, og ingen oppgaver mistet statusen sin. Project 5 har i tillegg steget Proposed, feltet Contributors og visningene All tasks og Closed tasks.

## Tilgang

Tilgang gis gjennom team i organisasjonen. Hver pilot har et team med samme navn som repoet, for eksempel samt-bu-pilot-3, med skrivetilgang til pilotens repo. Kjerneteamet har skrivetilgang til alle repoene.

## Unntak

To kommentarer som er gitt på sider på docs.samt-bu.no, står på brettet for Pilot 4, men ligger i repoet samt-bu-docs. Kommentarpanelet på nettstedet finner bare kommentarer i det repoet, og de kan derfor ikke flyttes.
