---
title: "Teknisk dokumentasjon"
linkTitle: "Teknisk dokumentasjon"
weight: 40

---

Denne siden er for den som administrerer brettene. Den samler det vi har lært om hva GitHub Projects kan og ikke kan, og fellene i brukergrensesnittet.

## Hva som kan gjøres med skript

GitHub Projects kan styres gjennom GitHubs programmeringsgrensesnitt (GraphQL). Det krever en nøkkel med tilgang til prosjekter.

**Kan:**

- Opprette og endre felt
- Endre navn på valg i et felt uten å miste verdiene, når valgets id tas med
- Opprette visninger og endre navn, filter og synlige felt
- Kopiere et brett, for eksempel fra malen
- Koble et brett til et repo
- Flytte issues mellom repoer

**Kan ikke:**

- Sette gruppering («Column by»), og heller ikke sortering
- Endre automatiske regler (workflows). De kan bare leses, og filteret i en regel er usynlig.

Det som ikke kan gjøres med skript, må gjøres i nettleseren.

## Feller i brukergrensesnittet

- **Endringer i en visning er ulagret** til du trykker «Save changes». Rett under står «Save changes to new view», som lager en ny visning i stedet.
- **Automatiske regler må redigeres med Edit og lagres med Save.** Lagres Auto-add uten at filteret endres, lagres standardfilteret, som også tar med pull requests.
- **Rekkefølgen på valg i programmeringsgrensesnittet** sier ingenting om rekkefølgen på kolonnene i nettleseren.

## Flytte oppgaver mellom repoer

Når et issue flyttes til et annet repo, beholder det kommentarer og historikk, og blir stående på brettene det var på. Det får nytt nummer i det nye repoet. Gamle lenker sendes videre.

Merkelapper som ikke finnes i det nye repoet, faller bort.

## Nytt brett

1. Kopier malen (Project 7) eller et eksisterende brett
2. Gi det navnet «SAMT-BU» etterfulgt av arbeidsområdet
3. Koble det til repoet
4. Slå på Auto-add med filteret is:issue is:open, og sjekk at regelen er lagret
5. Opprett et chore-issue som spor
