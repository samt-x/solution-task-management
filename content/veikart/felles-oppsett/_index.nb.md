---
id: e5ac13b4-873a-45e7-9405-f56a42e5731a
title: "Felles oppsett for prosjektbrettene"
linkTitle: "Felles oppsett"
weight: 10
lastmod: 2026-10-20T22:41:12+02:00
last_editor: Erik Hagen

---

Pilotene og delprosjektene har i dag ulike statuser, felt og visninger på brettene sine. Det gjør det vanskelig å se dem samlet. Målet er ikke at alle skal ha samme oppsett, men at oppsettene skal være **kompatible**.

## Prinsippet

- Det lages to til tre **maler** for prosjektbrett, for eksempel en enkel og en utvidet. Hver pilot eller hvert delprosjekt velger den som passer.
- Hver status i en mal svarer til nøyaktig én status i et **felles, grovere rapporteringsnivå**. Et brett med flere steg, for eksempel et eget steg for avklaring, kan dermed alltid rapporteres inn i det felles oppsettet.
- **Blokkert er et flagg, ikke et steg.** En oppgave kan bli blokkert i hvilket som helst steg, og det skal synes i den felles rapporteringen.

Hvilke statuser malene og det felles nivået får, fastsettes i trinn M1.

## Trinn

| Trinn | Innhold | Issue |
|---|---|---|
| [M1 Maler og felles statusmodell](https://github.com/samt-x/solution-task-management/milestone/1) | Malene, statusene og hvordan de svarer til det felles nivået. Den eksisterende malen, Project 7, oppdateres. | [solution-task-management#4](https://github.com/samt-x/solution-task-management/issues/4) |
| [M2 Malene tatt i bruk](https://github.com/samt-x/solution-task-management/milestone/2) | Hvert brett velger mal og legges om, uten at status på eksisterende oppgaver går tapt. | [solution-task-management#6](https://github.com/samt-x/solution-task-management/issues/6) |
| [M3 Automatisk oppretting av delprosjekter](https://github.com/samt-x/solution-task-management/milestone/9) | Et nytt delprosjekt bestilles i et skjema og godkjennes. Deretter lages repo, team, brett fra malen og porteføljekort automatisk, uten manuelle steg. Sider på docs kommer senere, fordi temaet først må slutte å ha stiene hardkodet. | [solution-task-management#13](https://github.com/samt-x/solution-task-management/issues/13) |
| [M4 Comment-feltet i malene](https://github.com/samt-x/solution-task-management/milestone/10) | Feltet Comment for siste statuskommentar ble testet på Project 5 i oktober 2026. Når det har vist seg å virke, legges det inn i malene, og øyeblikksbildet av status utvides til flere brett. | [solution-task-management#16](https://github.com/samt-x/solution-task-management/issues/16) |
