---
id: 9e40a003-0e64-4205-ab23-7b39c52788e7
title: "Bakgrunn og begrunnelse"
linkTitle: "Bakgrunn"
weight: 5
lastmod: 2026-10-10T22:27:29+02:00
last_editor: Erik Hagen

---

Denne siden forklarer hvorfor SAMT-BU styrer oppgaver i GitHub, og hvordan oppsettet har utviklet seg.

## Behovet

SAMT-BU er et samarbeid mellom mange organisasjoner, uten at noen av dem er overordnet de andre. Oppgavene må derfor ligge et sted alle deltakere kan se og bidra, uavhengig av hvilken organisasjon de kommer fra.

Prosjektet har tre typer oppgaver:

- **Pilotoppgaver** – arbeid som hører til én bestemt pilot
- **Tverrgående oppgaver** – felles begrepsapparat, overordnet arkitektur, metodikk, forberedelser til samlinger og avklaringer som gjelder alle
- **Kjerneteamets interne fordeling** – hvem i kjerneteamet gjør hva, og til når

## Hvorfor GitHub for oppgavestyring

Innholdet på docs.samt-bu.no ligger allerede i GitHub. Når oppgavene ligger i samme repo som innholdet de gjelder, kan en oppgave lenke direkte til endringen som løser den, og omvendt.

GitHub krever ingen ny programvare eller nye lisenser. Deltakerne har allerede kontoer, og alt er åpent for alle i organisasjonen.

> **Merk:** Arbeidsformen er ikke knyttet til GitHub. Det samme kan gjøres i andre git-baserte løsninger, som GitLab, Forgejo eller Codeberg, og flere av dem kan driftes i egen regi. GitHub er valgt foreløpig, fordi prosjektets innhold og samarbeidspartnere allerede er der. GitHub er ikke åpen kildekode, og valget er derfor diskutabelt av hensyn til digital suverenitet. Begrunnelsen og avveiningene er beskrevet under [Plattformvalg: GitHub vs. GitLab](/prosjektleveranser/loesninger/cms-loesninger/samt-bu-docs/teknisk-dokumentasjon/github-struktur/#plattformvalg-github-vs-gitlab). Alternativene er også omtalt under [Samskaping → Oppgavestyring](/utkast/temaer/samskaping/oppgavestyring/).

## Slik var det, og slik ble det

**Fram til høsten 2026** lå alle pilotoppgavene i ett felles repo, «Oppgaver», og hver oppgave var merket med hvilken pilot den hørte til. Hver pilot hadde sitt eget prosjektbrett, som hentet oppgaver fra det felles repoet. Tverrgående oppgaver hadde ikke noe naturlig sted, og ble enten merket med en tilfeldig pilot, lagt i Planner eller ikke skrevet ned.

Dette ble tatt opp i et innspill i august 2026: [Innspill om utvidet bruk av GitHub for oppgavestyring](/utkast/diverse/github-oppgavestyring/).

**I oktober 2026** ble oppsettet lagt om til ett repo per prosjektbrett:

- Hver pilot fikk sitt eget repo, som inneholder både pilotens sider på docs.samt-bu.no og pilotens oppgaver
- Pilotoppgavene ble flyttet fra «Oppgaver» til pilotenes egne repoer
- «Oppgaver» fikk nytt navn, samt-bu-common-tasks, og brukes nå bare til felles oppgaver på tvers av pilotene
- Generisk arkitektur og sluttleveransen fikk eget repo, samt-bu-architecture, med eget brett for arkitekturgruppa

Fordelen er at det er entydig hvor en oppgave hører hjemme, og at tilgang kan gis per pilot.

## Forholdet til Planner

Kjerneteamet bruker fortsatt Planner til intern fordeling. Løsningen her endrer ikke på det.

Skulle Planners rolle bli tatt opp senere – av hensyn til lisenser, universell utforming eller digital suverenitet – finnes det prosjektverktøy som kobler seg mot GitHub. Et nærliggende eksempel er [OpenProject](https://interoperable-europe.ec.europa.eu/eu-oss-catalogue/solutions/openproject), som har åpen kildekode og er oppført i EUs katalog over åpen kildekode for offentlig sektor. Det er et eget spørsmål og bør behandles for seg.

## Prinsipiell drøfting

Hvorfor åpen oppgavestyring regnes som god praksis i samarbeid mellom likeverdige organisasjoner, er drøftet under [Samskaping → Oppgavestyring](/utkast/temaer/samskaping/oppgavestyring/).
