---
id: 71a9801d-c1a0-4795-8c69-e935427a0b03
title: "Konvensjoner"
linkTitle: "Konvensjoner"
weight: 30
lastmod: 2026-10-18T22:24:53+02:00
last_editor: Erik Hagen

---

**Gjeldende praksis fra oktober 2026, med mulighet til å justere.** Konvensjonene bygger på praksisen i solution-samt-bu-docs, som har fungert godt. Ett spørsmål står åpent for arkitekturgruppa, se nederst på siden.

## Én oppgave, ett sted

1. **Én eier per oppgave.** Oppgaven opprettes der ansvaret ligger, se [Brukerveiledning](../brukerveiledning/). Vi kopierer ikke oppgaver mellom repoer.
2. **Lenke i stedet for kopi.** Berører oppgaven et annet område, lenkes det til den i en kommentar. GitHub viser koblingen i begge oppgavene.
3. **Underoppgaver ved avhengighet.** Når en arkitekturoppgave er avhengig av en leveranse fra en pilot, eller omvendt, legges den andre oppgaven inn som underoppgave (sub-issue). Det virker på tvers av repoer, og fremdriften vises på brettet.

Grunnen er at status og andre felt lagres per brett. Ligger samme oppgave på to brett, får den to statuser som fort blir ulike.

## Type angis med merkelapp

| Merkelapp | Brukes til |
|---|---|
| task | Arbeidsoppgave – det meste |
| decision | Krever en beslutning |
| problem | Noe er feil, uklart eller i konflikt |
| chore | Styring og vedlikehold av repo, brett og rutiner |
| future | Ikke nå, men kandidat senere |
| blocked | Venter på noe utenfor oppgaven |

Hver oppgave har én typemerkelapp. future og blocked kommer i tillegg ved behov.

## Faste overskrifter i beskrivelsen

- **Bakgrunn** – hvorfor dette trengs, hva som utløste det
- **Hva skal gjøres** – konkret
- **Ferdig når** – hva som skal foreligge
- **Relatert** – lenker til andre oppgaver, sider eller dokumenter (valgfritt)

For beslutninger i tillegg: **Alternativer** og **Anbefaling**. Selve beslutningen skrives i sluttkommentaren og føres i beslutningsloggen på docs.samt-bu.no.

## Status og felt på brettene

Alle brett bygger på én av to maler, Enkel eller Standard. Navnene i GitHub er på engelsk, slik at brettene fungerer for alle lesere. Tabellen forklarer dem.

| Status | Betydning | Enkel | Standard | Felles nivå |
|---|---|---|---|---|
| To do | Bestemt, men ikke startet | ✓ | ✓ | Ikke startet |
| Ready | Avklart og klar til å starte, neste i køen | | ✓ | Ikke startet |
| In progress | Under arbeid | ✓ | ✓ | Pågår |
| In review | Ute til gjennomgang eller kommentarer | | ✓ | Pågår |
| Done | Ferdig, oppgaven er lukket | ✓ | ✓ | Ferdig |

**Felles nivå** brukes når status rapporteres på tvers av brett. Et brett kan legge til egne steg, for eksempel Proposed (foreslått, ikke behandlet) foran To do, så lenge det er bestemt hvilket felles nivå steget hører til.

**Ready** trengs når flere velger oppgaver fra en felles kø. Er det ikke slik, holder Enkel.

| Felt | Innhold | |
|---|---|---|
| Responsible | Den som eier oppgaven. GitHub-brukernavn, ellers fullt navn. Aldri e-post, for brettene er offentlige. | Bør fylles ut |
| Priority | High, Medium eller Low | Frivillig |
| Effort | Small (under ett dagsverk), Medium (1–5 dagsverk) eller Large (over 5 dagsverk, vurder å dele opp oppgaven) | Frivillig |
| Estimate (person-days) | Anslag i dagsverk. Summeres automatisk i grupperte visninger, for eksempel per ansvarlig. | Frivillig |
| Start date og Due date | Gjeldende plan. Endres når planen endres. | Frivillig |

**Faktiske datoer** registrerer GitHub selv: når oppgaven ble opprettet, når den ble flyttet til In progress, og når den ble lukket. Det forutsetter to vaner: flytt kortet til In progress når du begynner, og lukk oppgaven når den er ferdig.

**Blokkert er ikke et steg.** Oppgaven beholder statusen sin og får merkelappen blocked. Skriv i en kommentar hva den venter på, og fjern merkelappen når hindringen er borte. Merkelappen finnes i alle repoene, så blokkerte oppgaver kan søkes fram på tvers.

## Ansvar

- **Responsible**: én person som eier oppgaven, angitt med GitHub-brukernavn, ellers fullt navn
- **Assignees**: alle som jobber med oppgaven, både den ansvarlige og bidragsyterne. Da får de varsler ved endringer, og oppgaven vises under «Assigned to me». Eierskapet står i Responsible, ikke i Assignees.

## Spor for administrative endringer

Endringer i repoer, brett, merkelapper og rutiner får en chore-oppgave som beskriver hva, hvorfor og resultatet. Den legges i repoet endringen gjelder. Sletting skal alltid ha et slikt spor før den gjøres.

## Skrivetips

- Når du skriver om en oppgave uten å ville lenke til den, sett nummeret i kodeformat. Ellers blir det en lenke, og omtalen havner i tidslinjen til den oppgaven.
- Skriv «Project 5», ikke nummertegn foran tallet, av samme grunn.
- Unngå @-omtale med mindre personen skal varsles. En omtale melder personen på hele tråden framover.

## Åpne spørsmål

Ett spørsmål avgjøres ikke av praksisen alene, og er lagt fram for arkitekturgruppa: [Hvem følger med på oppgaver som krysser arkitektur og piloter?](https://github.com/SAMT-X/solution-task-management/issues/1) Svar kan gis i saken, i Teams eller på arkitekturmøtet.

Malene ble innført i oktober 2026, se [Oppsett](../oppsett/). Brettene som fantes fra før, ble lagt over på malene i [M2 Malene tatt i bruk](https://github.com/samt-x/solution-task-management/issues/6).
