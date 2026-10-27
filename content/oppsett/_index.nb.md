---
id: bb682277-9c1d-46fb-8611-aae1f1f8fced
title: "Repoer og prosjektbrett"
linkTitle: "Oppsett"
weight: 20
lastmod: 2026-10-27T22:14:46+01:00
last_editor: Erik Hagen

---

Denne siden beskriver hvordan oppgavestyringen er satt opp i GitHub-organisasjonen samt-x per oktober 2026.

## Ett repo til ett brett

| Arbeidsområde | Repo | Prosjektbrett | Mal |
|---|---|---|---|
| Pilot 1 – Overgang ungdomsskole–videregående | samt-bu-pilot-1 | Project 1 | Standard |
| Pilot 2 – Valg av utdanningsløp | samt-bu-pilot-2 | Project 2 | Standard |
| Pilot 3 – Flytting av barn og unge i skoleåret | samt-bu-pilot-3 | **Project 4** | Standard |
| Pilot 4 – Vitnemål | samt-bu-pilot-4 | **Project 3** | Standard |
| Pilot 5 – Id-er i utdanning | samt-bu-pilot-5 | Project 9 | Standard |
| Pilot 6 – Foreldres tilgang til data | samt-bu-pilot-6 | Project 10 | Standard |
| Rammeverk og generisk arkitektur | samt-bu-architecture | Project 5 | Standard |
| Informasjonsmodeller | information-models | Project 6 | Standard |
| Felles oppgaver på tvers av pilotene | samt-bu-common-tasks | – | – |
| Nettstedet docs.samt-bu.no | solution-samt-bu-docs | [Project 17](https://github.com/orgs/samt-x/projects/17) | Standard |
| Oppgavestyring | solution-task-management | [Project 18](https://github.com/orgs/samt-x/projects/18) | Standard |
| Porteføljen (ett kort per arbeidsområde) | samt-bu-portfolio | [Project 13](https://github.com/orgs/samt-x/projects/13) | Eget oppsett |

**Merk:** Project 3 hører til Pilot 4, og Project 4 til Pilot 3. Numrene ble tildelt i den rekkefølgen brettene ble opprettet, og kan ikke endres.

Project 7 og Project 11 er maler for nye brett, se under. [Project 12](https://github.com/orgs/samt-x/projects/12) «SAMT-BU Overview – All tasks» er samlebrettet, se Samlebrettet under. Project 13 er porteføljebrettet, med ett kort per pilot, produkt og arbeidsområde. Feltet Status er fasen der. Feltet Sub-issues progress viser framdriften i oppgavene som er koblet til kortet som sub-issues. Feltet Objective har foreløpig bare et testvalg, til målene er besluttet. Regelen «Auto-add sub-issues to project» er slått av, slik at oppgavene ikke havner på porteføljebrettet. Oversiktsbrettene heter «SAMT-BU Overview – …», slik at de skilles fra delprosjektene i listen over brett.

Pilotrepoene inneholder også pilotens sider på docs.samt-bu.no. Oppgavene og innholdet ligger dermed i samme repo.

## Navn på brettene

Alle brett heter «SAMT-BU» etterfulgt av arbeidsområdet, for eksempel «SAMT-BU Pilot 3 – Flytting av barn og unge i skoleåret». Prefikset skiller brettene fra andre prosjekter deltakerne har i GitHub.

## Automatikk

Hvert brett har en regel for automatisk innlegging (Auto-add): alle åpne issues i det tilknyttede repoet legges på brettet. Når et issue lukkes, settes statusen til ferdig. Nye kort får statusen Proposed (workflowen «Item added to project»), slik at nye innspill havner der til de er behandlet.

**Statushistorikk:** Feltene på et brett har ingen historikk. Workflowen [Snapshot status](https://github.com/samt-x/solution-task-management/actions/workflows/snapshot-status.yml) skriver derfor statusen på Project 5 til fila [status/project-5.md](https://github.com/samt-x/solution-task-management/blob/main/status/project-5.md) i solution-task-management, hver time og ved manuell kjøring. Fila får en ny commit bare når noe er endret, så [historikken til fila](https://github.com/samt-x/solution-task-management/commits/main/status/project-5.md) viser hvordan status og kommentarer har endret seg over tid. Flere brett kan tas med senere ([M4 Comment-feltet i malene](https://github.com/samt-x/solution-task-management/issues/16)).

## Maler for nye brett

| Mal | Brett | Statuser |
|---|---|---|
| Enkel | Project 11 «[TEMPLATE] Simple board» | Proposed, To do, In progress, Done |
| Standard | Project 7 «[TEMPLATE] Standard board» | Proposed, To do, Ready, In progress, In review, Done |

Begge malene har feltene Responsible, Priority, Effort, Estimate (person-days), Start date og Due date, og fem visninger: Board (kanban per status), By responsible (kanban per ansvarlig), Open tasks, My tasks og Timeline. Hva statusene og feltene betyr, står under [Konvensjoner](../konvensjoner/).

**Issue types** er definert for hele organisasjonen (Settings → Planning → Issue types, krever eierrettighet): Task, Solution proposal, Question, Decision, Risk og Problem (het Bug til oktober 2026, samme id). Feltet Type er slått på i alle visningene i begge malene og i Project 5, unntatt Timeline. Brett som ble laget fra malene før oktober 2026, må få feltet slått på for hånd: View → Fields → Type → Save view, og bekreft i dialogen.

**Issue-skjemaer** ligger i repoet [samt-x/.github](https://github.com/samt-x/.github), under `.github/ISSUE_TEMPLATE/`: ett skjema per type, med engelsk typenavn og norsk tekst. Hvert skjema setter typen med `type:`, og alle har feltene «Gjelder» og «Forslag til hvem som bør se på dette». Skjemaene gjelder alle repoer i organisasjonen som ikke har egne skjemaer. Et repo med egen `.github/ISSUE_TEMPLATE/` bruker bare sine egne, så legg ikke inn skjemaer i enkeltrepoer uten å kopiere de felles. Blank issue er fortsatt på (`config.yml`), og lista har en lenke til Konvensjoner. Skjemaene setter ikke brett (`projects:`). Et felles skjema kan ikke peke på riktig brett for hvert repo, og repoene som har brett, legger nye saker inn automatisk. Repoet må være offentlig for at skjemaene skal virke i de offentlige repoene. Lokalt er det klonet til `samt-x-dotgithub/` i workspace, fordi skriptene for alle repoene hopper over mapper som begynner med punktum.

Malene er synlige for alle medlemmer av organisasjonen, men ikke for andre. Medlemmene har lesetilgang (Base role Read). Det er nok til å lage brett fra malene, men ikke til å endre dem. Malene må ikke lukkes, for da forsvinner de fra New project.

Slik lages et nytt brett:

1. Velg New project i organisasjonen og velg en av malene.
2. Gi brettet navn etter mønsteret under.
3. Koble brettet til repoet, og sett regelen for automatisk innlegging (se Automatikk).
4. Legg inn personene som valg i feltet Responsible.

Brettene som fantes før malene, ble lagt over på dem i oktober 2026 ([M2 Malene tatt i bruk](https://github.com/samt-x/solution-task-management/issues/6)). Statusene fikk nye navn, og ingen oppgaver mistet statusen sin. Project 5 har i tillegg feltene Contributors og Comment og visningene All tasks og Closed tasks. Statusen Proposed fantes først bare på Project 5. Den ble lagt inn i begge malene og på alle brettene 27. oktober 2026, uten at noen oppgaver mistet statusen sin ([solution-task-management#20](https://github.com/samt-x/solution-task-management/issues/20)).

## Samlebrettet

[Project 12 «SAMT-BU Overview – All tasks»](https://github.com/orgs/samt-x/projects/12) samler alle issues i de offentlige repoene. Private repoer er ikke med. Statusen oversettes til det felles nivået (se [Konvensjoner](../konvensjoner/)): Not started, In progress eller Done. Lukkede issues blir Done, og åpne issues uten brett blir Not started. Feltet Source status viser brettet og statusen oppgaven har der.

Brettet fylles av workflowen [Sync All tasks](https://github.com/samt-x/solution-task-management/actions/workflows/sync-all-tasks.yml) i repoet solution-task-management, hver time og ved manuell kjøring. Synkingen går bare én vei, og skriver aldri til prosjektbrettene. Alle automatiske regler på samlebrettet er slått av, og skal være det. Tilgangen er beskrevet under [Teknisk dokumentasjon](../teknisk-dokumentasjon/).

## Tilgang

Tilgang gis gjennom team i organisasjonen. Hver pilot har et team med samme navn som repoet, for eksempel samt-bu-pilot-3, med skrivetilgang til pilotens repo. Kjerneteamet har skrivetilgang til alle repoene.

## Unntak

To kommentarer som er gitt på sider på docs.samt-bu.no, står på brettet for Pilot 4, men ligger i repoet samt-bu-docs. Kommentarpanelet på nettstedet finner bare kommentarer i det repoet, og de kan derfor ikke flyttes.
