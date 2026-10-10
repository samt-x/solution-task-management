---
title: "Repoer og prosjektbrett"
linkTitle: "Oppsett"
weight: 20

---

Denne siden beskriver hvordan oppgavestyringen er satt opp i GitHub-organisasjonen samt-x per oktober 2026.

## Ett repo til ett brett

| Arbeidsområde | Repo | Prosjektbrett |
|---|---|---|
| Pilot 1 – Overgang ungdomsskole–videregående | samt-bu-pilot-1 | Project 1 |
| Pilot 2 – Valg av utdanningsløp | samt-bu-pilot-2 | Project 2 |
| Pilot 3 – Flytting av barn og unge i skoleåret | samt-bu-pilot-3 | **Project 4** |
| Pilot 4 – Vitnemål | samt-bu-pilot-4 | **Project 3** |
| Pilot 5 – Id-er i utdanning | samt-bu-pilot-5 | Project 9 |
| Pilot 6 – Foreldres tilgang til data | samt-bu-pilot-6 | Project 10 |
| Rammeverk og generisk arkitektur | samt-bu-architecture | Project 5 |
| Informasjonsmodeller | information-models | Project 6 |
| Felles oppgaver på tvers av pilotene | samt-bu-common-tasks | – |
| Nettstedet docs.samt-bu.no | solution-samt-bu-docs | – |
| Oppgavestyring | solution-task-management | – |

**Merk:** Project 3 hører til Pilot 4, og Project 4 til Pilot 3. Numrene ble tildelt i den rekkefølgen brettene ble opprettet, og kan ikke endres.

Project 7 er en mal for nye brett og er ikke i bruk.

Pilotrepoene inneholder også pilotens sider på docs.samt-bu.no. Oppgavene og innholdet ligger dermed i samme repo.

## Navn på brettene

Alle brett heter «SAMT-BU» etterfulgt av arbeidsområdet, for eksempel «SAMT-BU Pilot 3 – Flytting av barn og unge i skoleåret». Prefikset skiller brettene fra andre prosjekter deltakerne har i GitHub.

## Automatikk

Hvert brett har en regel for automatisk innlegging (Auto-add): alle åpne issues i det tilknyttede repoet legges på brettet. Når et issue lukkes, settes statusen til ferdig.

## Felt

Pilotbrettene bruker GitHubs standardstatus: Todo, In Progress og Done.

Project 5 (arkitektur) har en mer detaljert statusflyt og egne felt:

| Felt | Innhold |
|---|---|
| Status | Proposed → Backlog → Ready → In progress → In review → Done |
| Responsible | Én person som eier oppgaven |
| Contributors | Andre som bidrar |
| Priority | High, Medium eller Low |
| Due date | Frist |

## Tilgang

Tilgang gis gjennom team i organisasjonen. Hver pilot har et team med samme navn som repoet, for eksempel samt-bu-pilot-3, med skrivetilgang til pilotens repo. Kjerneteamet har skrivetilgang til alle repoene.

## Unntak

To kommentarer som er gitt på sider på docs.samt-bu.no, står på brettet for Pilot 4, men ligger i repoet samt-bu-docs. Kommentarpanelet på nettstedet finner bare kommentarer i det repoet, og de kan derfor ikke flyttes.
