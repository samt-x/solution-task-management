---
id: 1d9f85e6-8f58-41b1-8eea-45815cfc56cc
title: "Teknisk dokumentasjon"
linkTitle: "Teknisk dokumentasjon"
weight: 40
lastmod: 2026-10-31T02:11:13+01:00
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
- Bestemme rekkefølgen på kolonnene i en visning. Synlige felt kan velges, men et nytt felt havner alltid til høyre og må dras på plass i nettleseren.
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

## Øyeblikksbilde av status

Workflowen [Snapshot status](https://github.com/samt-x/solution-task-management/actions/workflows/snapshot-status.yml) kjører skriptet .github/scripts/snapshot-status.py hver time og ved manuell kjøring. Skriptet leser brettene i PROJECTS og skriver én Markdown-tabell per brett til status/. Workflowen committer bare når fila er endret, og meldingen har [skip ci], så docs ikke bygges på nytt. Fila har ingen tidsstempel; commit-datoen er tidspunktet.

Skriptet bruker samme app og nøkkel som samlebrettet, men bare til å lese brettene. Commiten gjøres med workflowens egen token (GITHUB_TOKEN), som bare gjelder dette repoet. Skriptet kan også kjøres lokalt med gh auth token.

Bakgrunn: [solution-task-management#15](https://github.com/samt-x/solution-task-management/issues/15).

## Tidslinje med avhengigheter

Workflowen [Timeline](https://github.com/samt-x/solution-task-management/actions/workflows/timeline.yml) kjører skriptet .github/scripts/timeline.py hver time og ved manuell kjøring. Skriptet leser brettene i PROJECTS (nå Project 5 og 18): status, Start date, Due date og avhengighetene («Blocked by») på hvert issue. Det tegner én SVG per brett og språk til content/tidslinje/, som vises på siden [Tidslinje](../tidslinje/). Siden limer figurene rett inn med shortcoden inline-svg i temaet, så lenker og verktøytips virker. Et vanlig bilde ville slått dem av. Id-ene i figuren har brettnummeret i seg, så flere figurer på samme side ikke kolliderer.

**Pilene.** GitHubs avhengigheter har ingen egne felt. Skriptet bygger derfor verktøytipset på pila av tre kilder: «Blocked by» (om pila finnes), hendelsen BlockedByAddedEvent i issuets tidslinje (hvem som koblet og når), og overskriften Avhengigheter i brødteksten til issuet som venter (hvorfor). Overskriften leses av funksjonen describe: punktlinjer som begynner med en issue-henvisning (#35, samt-bu-pilot-6#12 eller full lenke). Står en henvisning der uten tilsvarende «Blocked by», tegnes ingen pil, men det kommer et varsel under figuren. Koblingen i GitHub er altså master, og teksten beskriver den bare. Slakk og overlapp regnes i hele dager mellom frist og startdato.

Figuren har dagens dato, og endres derfor minst én gang i døgnet. Workflowen committer bare når en figur er endret. Commits fra github-actions[bot] utløser ikke Trigger rebuild, så workflowen ber selv samt-bu-docs bygge på nytt, med org-secreten DOCS_REBUILD_TOKEN. Lesingen bruker samme app som samlebrettet.

Lokalt: kjør skriptet med gh auth token. --out skriver figurene til en annen mappe, --data leser oppgavene fra en JSON-fil i stedet for API-et, og --today setter dagens dato. Avhengigheter kan bare settes i GitHub eller via REST (repos/…/issues/N/dependencies/blocked_by), ikke med gh før versjon 2.94.

Bakgrunn: [solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32).

## Flytte oppgaver mellom repoer

Når et issue flyttes til et annet repo, beholder det kommentarer og historikk, og blir stående på brettene det var på. Det får nytt nummer i det nye repoet. Gamle lenker sendes videre.

Merkelapper som ikke finnes i det nye repoet, faller bort.

## Nytt brett

1. Kopier malen (Project 7) eller et eksisterende brett
2. Gi det navnet «SAMT-BU» etterfulgt av arbeidsområdet
3. Koble det til repoet
4. Slå på Auto-add med filteret is:issue is:open, og sjekk at regelen er lagret
5. Opprett et chore-issue som spor
