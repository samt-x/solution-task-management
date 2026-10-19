---
id: 1d9f85e6-8f58-41b1-8eea-45815cfc56cc
title: "Teknisk dokumentasjon"
linkTitle: "Teknisk dokumentasjon"
weight: 40
lastmod: 2026-10-19T10:15:08+02:00
last_editor: Erik Hagen

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

## Samlebrettet: app og nøkkel

Workflowen som fyller samlebrettet (Project 12), logger inn som GitHub-appen **SAMT-BU Task sync**, ikke som en person. Appen eies av organisasjonen og er installert på alle repoene.

| | |
|---|---|
| Tilganger | Lese issues og metadata. Lese og skrive organisasjonsprosjekter. Ingen tilgang til kode. |
| Nøkkel | Privat nøkkel som repo-secret `TASK_SYNC_PRIVATE_KEY` i solution-task-management. Appens Client ID står i workflowen. En kopi av nøkkelen ligger i Bitwarden hos prosjektlederen. |
| Token | Lages på nytt ved hver kjøring og varer i én time. |
| Kjøring | Bare etter tidsplan og manuelt, aldri fra pull requests. Secrets sendes ikke til workflows fra forks. |

**Risiko:** Lekker nøkkelen, kan den brukes til å endre eller slette brett i organisasjonen, men ikke kode eller issues. Brettene kan bygges opp igjen fra issuene, men statuser og felt kan gå tapt. Sannsynligheten er lav, fordi nøkkelen bare finnes i GitHub-secreten og i Bitwarden.

**Ved mistanke om lekkasje:** Gå til appens side under organisasjonens Settings → Developer settings → GitHub Apps → SAMT-BU Task sync → Credentials → Key pairs. Lag en ny nøkkel, legg den inn i secreten og i Bitwarden, og slett den gamle.

**Samlebrettet skal ikke ha automatiske regler.** Auto-close og andre regler som skriver, er slått av. Endringer gjort for hånd på samlebrettet overskrives ved neste kjøring.

## Flytte oppgaver mellom repoer

Når et issue flyttes til et annet repo, beholder det kommentarer og historikk, og blir stående på brettene det var på. Det får nytt nummer i det nye repoet. Gamle lenker sendes videre.

Merkelapper som ikke finnes i det nye repoet, faller bort.

## Nytt brett

1. Kopier malen (Project 7) eller et eksisterende brett
2. Gi det navnet «SAMT-BU» etterfulgt av arbeidsområdet
3. Koble det til repoet
4. Slå på Auto-add med filteret is:issue is:open, og sjekk at regelen er lagret
5. Opprett et chore-issue som spor
