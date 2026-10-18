---
id: 7c264c4f-711d-400b-a2df-30ad7e6745c9
title: "Oppgavestyring"
linkTitle: "Oppgavestyring"
weight: 20
lastmod: 2026-10-18T19:38:42+02:00
last_editor: Erik Hagen

---

Denne seksjonen dokumenterer hvordan SAMT-BU styrer oppgaver i GitHub: hvor oppgavene ligger, hvordan de er organisert, og hvilke regler vi følger. Innholdet er rettet mot alle som skal opprette, følge opp eller administrere oppgaver i prosjektet – pilotdeltakere, arkitekturgruppa og kjerneteamet.

Løsningen er satt sammen av følgende deler:

| Del | Rolle |
|-----|-------|
| **GitHub Issues** | Hver oppgave er et issue i repoet der ansvaret ligger |
| **GitHub Projects** | Ett prosjektbrett per pilot eller arbeidsområde, med status, ansvarlig og frister |
| **Team i GitHub-organisasjonen** | Gir deltakerne tilgang til riktige repoer og brett |
| **Konvensjoner** | Felles regler for merking, beskrivelse og lukking av oppgaver |

Et **prosjektbrett** er et prosjekt i GitHub (GitHub Projects): en samling oppgaver med felles felt, som status, ansvarlig og frist. Samme brett kan vises på flere måter, og hver visning ligger i en egen fane på brettet:

- **Kanban-brett** (i GitHub: Board): én kolonne per steg i arbeidsflyten, for eksempel Ny, Pågår og Ferdig. Hver oppgave er et kort som flyttes fra venstre mot høyre etter hvert som arbeidet går framover. Kolonnene kan også deles inn etter et annet felt, for eksempel ansvarlig eller prioritet.
- **Tabell** (Table): én rad per oppgave, med feltene som kolonner. Egner seg til å sortere og filtrere.
- **Tidslinje** (Roadmap): oppgavene plassert langs en tidsakse etter dato.

Flytter du et kort til en annen kolonne, endres feltet kolonnene bygger på, som oftest status. Endringen vises i alle visningene, fordi det er den samme oppgaven.

Hovedprinsippet er **ett repo til ett prosjektbrett**: hver pilot har sitt eget repo med både innhold og oppgaver, og sitt eget brett. Felles oppgaver og generisk arkitektur har egne repoer.

Status: løsningen er i bruk. Oppsettet ble lagt om høsten 2026, se [Bakgrunn](bakgrunn/). Konvensjonene er gjeldende praksis, med ett åpent spørsmål til arkitekturgruppa.

**Dine oppgaver og brettene** finner du under [Styring → Oppgaver og oppfølging](https://docs.samt-bu.no/prosjektstyring/oppgaver-og-oppfolging/). Denne seksjonen beskriver løsningen bak.

Se underkapitlene for veiledning, oppsett, konvensjoner og [veikart](veikart/).
