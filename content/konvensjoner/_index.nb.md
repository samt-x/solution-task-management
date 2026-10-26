---
id: 71a9801d-c1a0-4795-8c69-e935427a0b03
title: "Konvensjoner"
linkTitle: "Konvensjoner"
weight: 30
lastmod: 2026-10-26T23:01:45+01:00
last_editor: Erik Hagen

---

**Gjeldende praksis fra oktober 2026, med mulighet til å justere.** Konvensjonene bygger på praksisen i solution-samt-bu-docs, som har fungert godt. Ett spørsmål står åpent for arkitekturgruppa, se nederst på siden.

## Én oppgave, ett sted

1. **Én eier per oppgave.** Oppgaven opprettes der ansvaret ligger, se [Brukerveiledning](../brukerveiledning/). Vi kopierer ikke oppgaver mellom repoer.
2. **Lenke i stedet for kopi.** Berører oppgaven et annet område, lenkes det til den i en kommentar. GitHub viser koblingen i begge oppgavene.
3. **Underoppgaver ved avhengighet.** Når en arkitekturoppgave er avhengig av en leveranse fra en pilot, eller omvendt, legges den andre oppgaven inn som underoppgave (sub-issue). Det virker på tvers av repoer, og fremdriften vises på brettet.

Grunnen er at status og andre felt lagres per brett. Ligger samme oppgave på to brett, får den to statuser som fort blir ulike.

## Type og merkelapper

**Typen sier hva saken er. Statusen sier hvor den er i løpet.** Hver sak har én type (issue type), og typene gjelder alle repoene i organisasjonen. Typen skal fortsatt være riktig når saken er ferdig. Derfor finnes det ingen type for «forslag» eller «innspill». At noe er foreslått og ikke behandlet, viser statusen Proposed.

| Type | Brukes til |
|---|---|
| Task | Noe som skal gjøres – det meste, også oppfølging, utforsking og utredning |
| Solution proposal | Et løsningsforslag som skal vurderes, som regel sammen med andre forslag i en større oppgave |
| Question | Noe som trenger et svar |
| Decision | Noe som krever en beslutning. Si hva og av hvem. |
| Risk | En risiko eller bekymring som bør vurderes |
| Problem | Noe som er galt nå: et verktøy som ikke virker, en feil i innhold eller en modell, et resonnement som ikke holder, en motsetning mellom kilder, eller noe i måten vi jobber på. Det som kan gå galt, er Risk. Typen het Bug til oktober 2026. |

Merkelapper kommer i tillegg til typen, og en sak kan ha flere:

| Merkelapp | Brukes til |
|---|---|
| blocked | Venter på noe utenfor saken |
| chore | Styring og vedlikehold av repo, brett og rutiner |
| future | Ikke nå, men kandidat senere |

Merkelappene task, decision og question ble brukt som type før typene kom (oktober 2026). De er erstattet av typene og finnes ikke lenger. Merkelapper for tema står på vent. I stedet kan en sak lenke til det den gjelder (en side, et case, et element i modellen) i feltet «Gjelder» i skjemaene, se [samt-bu-architecture#35](https://github.com/samt-x/samt-bu-architecture/issues/35).

## Innspill og løsningsforslag

1. **Et innspill er en sak i Proposed**, av hvilken som helst type. Den som behandler innspillet, flytter det til To do, eller lukker det.
2. **Ingen tildeling i Proposed.** Assignees settes først når saken er behandlet. Den som sender inn, kan foreslå hvem som bør se på saken med @-omtale, i skjemaenes felt «Forslag til hvem som bør se på dette» eller i teksten, for eksempel «Forslag: @navn ser på dette». Da får de ett varsel og kan følge tråden, uten at saken havner i oppgavelistene deres som om de hadde sagt ja.
3. **Løsningsforslag kobles til vurderingen.** Når et løsningsforslag tas inn i arbeidet med å vurdere løsninger, legges det inn som underoppgave (sub-issue) under den større oppgaven. Da ser man i begge retninger hvor forslaget hører hjemme, og den større oppgaven viser hvor mange forslag som er vurdert.

## Lukking

En sak kan lukkes fra hvilken som helst status, også rett fra Proposed. Velg alltid riktig grunn når du lukker, og skriv en kort kommentar om hvorfor.

| Grunn i GitHub | Brukes når | Ikon |
|---|---|---|
| Completed | Saken er gjort. For et løsningsforslag: vurdert og tatt med videre. | Lilla hake |
| Not planned | Saken er avvist, avbrutt eller kansellert. Kommentaren sier hvilket og hvorfor. | Grå sirkel med strek |
| Duplicate | Saken finnes allerede. Lenk til den andre. | Grå |

Alle lukkede saker havner i Done på brettet. Grunnen ser du på ikonet på kortet, og du kan søke på den med «reason:completed» eller «reason:"not planned"».

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
| Comment | Siste statuskommentar, med dato først, for eksempel «23.10: Utkast sendt til Anders». Bare siste kommentar står i feltet. Foreløpig bare på Project 5. | Frivillig |

**Comment har ingen historikk i GitHub.** Skrives feltet over, er forrige kommentar borte fra brettet. Statusen på Project 5 skrives derfor hver time til en fil, og [historikken til fila](https://github.com/samt-x/solution-task-management/commits/main/status/project-5.md) viser tidligere kommentarer og statuser. Se [Oppsett](../oppsett/).

**Faktiske datoer** registrerer GitHub selv: når oppgaven ble opprettet, når den ble flyttet til In progress, og når den ble lukket. Det forutsetter to vaner: flytt kortet til In progress når du begynner, og lukk oppgaven når den er ferdig.

**Blokkert er ikke et steg.** Oppgaven beholder statusen sin og får merkelappen blocked. Skriv i en kommentar hva den venter på, og fjern merkelappen når hindringen er borte. Merkelappen finnes i alle repoene, så blokkerte oppgaver kan søkes fram på tvers.

## Ansvar

- **Responsible**: én person som eier oppgaven, angitt med GitHub-brukernavn, ellers fullt navn
- **Assignees**: alle som jobber med oppgaven, både den ansvarlige og bidragsyterne. Da får de varsler ved endringer, og oppgaven vises under «Assigned to me». Eierskapet står i Responsible, ikke i Assignees.
- Saker i Proposed tildeles ikke, se [Innspill og løsningsforslag](#innspill-og-løsningsforslag).

## Spor for administrative endringer

Endringer i repoer, brett, merkelapper og rutiner får en chore-oppgave som beskriver hva, hvorfor og resultatet. Den legges i repoet endringen gjelder. Sletting skal alltid ha et slikt spor før den gjøres.

## Skrivetips

- Når du skriver om en oppgave uten å ville lenke til den, sett nummeret i kodeformat. Ellers blir det en lenke, og omtalen havner i tidslinjen til den oppgaven.
- Skriv «Project 5», ikke nummertegn foran tallet, av samme grunn.
- Unngå @-omtale med mindre personen skal varsles. En omtale melder personen på hele tråden framover.

## Åpne spørsmål

Ett spørsmål avgjøres ikke av praksisen alene, og er lagt fram for arkitekturgruppa: [Hvem følger med på oppgaver som krysser arkitektur og piloter?](https://github.com/SAMT-X/solution-task-management/issues/1) Svar kan gis i saken, i Teams eller på arkitekturmøtet.

Malene ble innført i oktober 2026, se [Oppsett](../oppsett/). Brettene som fantes fra før, ble lagt over på malene i [M2 Malene tatt i bruk](https://github.com/samt-x/solution-task-management/issues/6).
