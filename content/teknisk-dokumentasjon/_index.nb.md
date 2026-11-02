---
id: 1d9f85e6-8f58-41b1-8eea-45815cfc56cc
title: "Teknisk dokumentasjon"
linkTitle: "Teknisk dokumentasjon"
weight: 40
lastmod: 2026-11-02T03:06:39+01:00
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

Workflowen [Timeline](https://github.com/samt-x/solution-task-management/actions/workflows/timeline.yml) kjører skriptet .github/scripts/timeline.py hver time og ved manuell kjøring. Skriptet leser brettene i PROJECTS (alle oppgavebrettene for delprosjektene og eksempelbrettet Project 20, ikke samlebrettet, porteføljen eller malene): status, Start date, Due date, Duration, statushistorikken og avhengighetene («Blocked by») på hvert issue. Det tegner én SVG per brett og språk til content/tidslinje/. Eksempelet vises på siden [Tidslinje](../tidslinje/), og de ekte brettene på siden Oppgaver og framdrift i delprosjektet som eier brettet. Sidene limer figurene rett inn med shortcoden inline-svg i temaet, så lenker og verktøytips virker. Ligger figuren på en annen side, får shortcoden stien dit som andre argument: inline-svg "project-5-nb.svg" "/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/tidslinje". Figurene lages dermed ett sted, og workflowen skriver ikke til andre repoer. Nytt brett: legg det inn i PROJECTS og lag siden Oppgaver og framdrift, se [Konvensjoner](../konvensjoner/#oppgaver-og-framdrift). Et vanlig bilde ville slått dem av. Id-ene i figuren har brettnummeret i seg, så flere figurer på samme side ikke kolliderer.

**Pilene.** GitHubs avhengigheter har ingen egne felt. Skriptet bygger derfor verktøytipset på pila av tre kilder: «Blocked by» (om pila finnes), hendelsen BlockedByAddedEvent i issuets tidslinje (hvem som koblet og når), og overskriften Avhengigheter i brødteksten til issuet som venter (hvorfor). Overskriften leses av funksjonen describe: punktlinjer som begynner med en issue-henvisning (#35, samt-bu-pilot-6#12 eller full lenke). Står en henvisning der uten tilsvarende «Blocked by», tegnes ingen pil, men det kommer et varsel under figuren. Koblingen i GitHub er altså master, og teksten beskriver den bare. Slakk og overlapp regnes i arbeidsdager mellom slutt og start.

**Datoene.** Alle oppgavene på brettet tegnes. Funksjonen plan finner start og slutt for hver oppgave, i rekkefølgen som står på siden [Tidslinje](../tidslinje/#hvor-datoene-kommer-fra). Det som har skjedd, hentes fra hendelsene ProjectV2ItemStatusChangedEvent i issuets tidslinje, filtrert på brettet (første endring til In progress eller In review, siste endring til Done), og fra closedAt. Tidspunktene regnes om til maskinens tidssone. Duration er et tallfelt i arbeidsdager på alle oppgavebrettene (ikke porteføljen), fra november 2026. Uten Duration antas DEFAULT_DAYS (5). Start regnet fra avhengighetene går rekursivt gjennom oppgavene det ventes på, med vern mot avhengigheter i ring. Oppgaver på andre brett regnes ikke med. Stolpen har tre utseender: lys med kant når begge datoene er satt eller har skjedd, stiplet når en av dem er beregnet, og mørk over for det som har skjedd. Sen start (late_s) er en start fra Start date, eller regnet med en Duration noen har satt, som er passert uten at oppgaven er startet. Den gir gul kant og strek. Planlagt slutt (planned) er Due date, eller start pluss en Duration noen har satt. For åpne oppgaver regnes en prognose (f): faktisk start, ellers den seneste av i dag, Start date og dagen etter at oppgavene det ventes på er ventet ferdige, pluss varigheten (Duration, ellers arbeidsdagene fra Start date til Due date). Er f etter planned, fylles delen etter fristen rød, helt rød til i dag og lys etter. Pilene og avhengighetene bruker f, så forsinkelser forplanter seg. Lukkede oppgaver skilles på stateReason: COMPLETED gir ✓, NOT_PLANNED og DUPLICATE (DROPPED) gir ✕ og skravert stolpe uten mørk del. Shortcoden inline-svg viser figuren i full størrelse i en ramme som rulles begge veier, med en verktøylinje for zoom (− / + / 100 % / Tilpass bredden, og Ctrl + musehjul over figuren), dra med musa (flyttes musa mer enn 5 piksler, svelges klikket, så lenkene ikke åpnes) og en lenke til SVG-fila alene. Brett i NO_HISTORY (eksempelbrettet) leser Start date og Due date som det som har skjedd for oppgaver som er startet eller ferdige, fordi datoene flyttes hver uke.

**Vinduet.** Klikk på en issue-lenke i figuren fanges av partials/issue-popup.html i temaet, som inline-svg tar med. Det henter issuet fra GitHubs REST-API med Accept: application/vnd.github.html+json og viser body_html, GitHubs egen rensede gjengivelse. GitHub kan ikke vises i en iframe. Innloggede brukere bruker sin token (getStoredToken), andre er uten token (cirka 60 oppslag i timen per IP). Svar lagres i minnet så lenge siden er åpen. Pilene har class tl-dep, og da vises verktøytipset øverst i vinduet. Vinduet kan flyttes (pointer-hendelser på tittellinjen) og endres i størrelse (CSS resize). Det lukkes med Esc, × eller klikk utenfor vinduet på noe som ikke er klikkbart (lenke, knapp, skjemafelt). Klikket teller bare når musa også gikk ned utenfor vinduet, så en flytting eller endring av størrelse som slippes utenfor, lukker det ikke.

**Sub-issues, filter og Mine oppgaver** ([solution-task-management#44](https://github.com/samt-x/solution-task-management/issues/44)). Skriptet henter også parent, subIssuesSummary (completed, total) og assignees for hvert issue, og feltet Responsible (enkeltvalg med GitHub-brukernavn som valg). Funksjonen summarize gir hver oppgave depth og kids (sub-issuene på brettet). En forelder med barn på brettet får start, slutt og prognose fra barna (de dypeste regnes først) og ingen egne forsinkelser, og tegnes som en klamme: fargen fra forelderens status (COLORS), mørk fylling for det som har skjedd (funksjonen worked: periodene fra started til ended, eller til i dag, for sub-issuene nedover i treet, uten avbrutte, slått sammen når de møtes; et hull betyr at ingen var i arbeid; framdriften fra subIssuesSummary står bare som tekst), rød kant når is_late gjelder for minst ett barn, grå når forelderen er lukket og skravert når den er avbrutt (DROPPED). Funksjonen order legger barna rett under forelderen. Figuren får data-attributter som skriptet i shortcoden inline-svg bruker: svg har data-tl, data-tl-top og data-tl-rowh; hver rad er en gruppe g.tl-row med data-key, data-parent, data-y (opprinnelig y), data-state (open, done eller dropped), data-late og data-people (assignees og Responsible); pilene har data-from, data-to, data-x1 og data-x2. Stripene (tl-stripe), helgene (tl-vh), de loddrette strekene (tl-vy2) og alt under radene (tl-foot) tilpasses antallet synlige rader. Ved folding og filter flytter skriptet de synlige radene med transform, tegner pilene på nytt med samme regel som timeline.py, og endrer høyden på figuren. Knappene ▾/▸ (g.tl-fold) har display="none" i fila og vises først av skriptet, så figuren uten JavaScript, og «Åpne figuren i nytt vindu», er som før. Mine oppgaver vises bare når localStorage har samt-bu-gh-user (satt ved innlogging på docs), og sammenligner uten hensyn til store og små bokstaver.

Figuren har dagens dato, og endres derfor minst én gang i døgnet. Workflowen committer bare når en figur er endret. Commits fra github-actions[bot] utløser ikke Trigger rebuild, så workflowen ber selv samt-bu-docs bygge på nytt, med org-secreten DOCS_REBUILD_TOKEN. Lesingen bruker samme app som samlebrettet.

Lokalt: kjør skriptet med gh auth token. --out skriver figurene til en annen mappe, --data leser oppgavene fra en JSON-fil i stedet for API-et, og --today setter dagens dato. Avhengigheter kan bare settes i GitHub eller via REST (repos/…/issues/N/dependencies/blocked_by), ikke med gh før versjon 2.94.

Bakgrunn: [solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32).

## Eksempelbrettet

Eksemplene som brukes i dokumentasjonen, ligger i repoet [solution-task-management-examples](https://github.com/samt-x/solution-task-management-examples) og på [Project 20](https://github.com/orgs/samt-x/projects/20) «[EXAMPLE] Timeline». Repoet står i EXCLUDE i sync-all-tasks.py, så eksemplene kommer ikke på samlebrettet.

**Datoene følger dagens dato.** Før tidslinjen tegnes, kjører Timeline skriptet .github/scripts/example-dates.py. Det leser .github/scripts/example-dates.json, som har start og frist per issue i dager fra mandag denne uka (null = ingen dato), og eventuelt Duration som tredje tall, og skriver Start date, Due date og Duration på brettet med appens token. Lørdag og søndag regnes til neste uke, ellers ville pågående eksempler ha passert fristen i helgen. Bare felt som avviker, skrives, så datoene endres én gang i uka. Brettet er fortsatt master, og figuren og brettet viser det samme. Status, avhengigheter og beskrivelser settes i GitHub som ellers. --dry-run viser hva som ville blitt endret.

**Nytt eksempel:** lag issuet i eksempelrepoet med linjen «Eksempel, ikke en oppgave» først, legg det på brettet, og legg inn nummeret med forskyvninger i example-dates.json. Bakgrunn: [solution-task-management#40](https://github.com/samt-x/solution-task-management/issues/40).

## Planlagte kjøringer

Tre workflows i solution-task-management kjører etter tidsplan:

| Workflow | Når | Hva den oppdaterer |
|---|---|---|
| [Sync All tasks](https://github.com/samt-x/solution-task-management/actions/workflows/sync-all-tasks.yml) | 17 minutter over hver time | Samlebrettet (Project 12) |
| [Timeline](https://github.com/samt-x/solution-task-management/actions/workflows/timeline.yml) | 17 minutter over hver time | Tidslinjene på docs, og datoene på eksempelbrettet |
| [Snapshot status](https://github.com/samt-x/solution-task-management/actions/workflows/snapshot-status.yml) | 47 minutter over hver time | Statushistorikken i status/ |

**Motoren er GitHub Actions.** Tidsplanen står som schedule med cron i hver workflow. GitHub starter kjøringen på sine egne maskiner, så det trengs ingen server hos oss. Alle tre kan også kjøres for hånd med «Run workflow». GitHub garanterer ikke tidspunktet: kjøringer kan bli forsinket når det er travelt hos GitHub, og en sjelden gang falle bort. Derfor brukes ikke hel time.

**Faste skript, ikke KI.** Workflowene kjører Python-skript som følger reglene som er beskrevet her og på siden [Tidslinje](../tidslinje/). Ingen KI vurderer noe underveis. Et tilfelle ingen har tenkt på, får derfor enten et svar etter reglene, som alltid har en siste utvei (for eksempel start i dag og én uke antatt varighet), eller så stopper skriptet med en feil. Da committes ingenting, og det forrige resultatet blir stående. Datoen under tidslinjen viser når figuren ble laget.

**Feil meldes som issue.** Siste steg i hver workflow kjører skriptet .github/scripts/workflow-alert.py. Feiler et steg, lager det issuet «Workflow failed: <navn>» med typen Problem og lenke til kjøringen. Issuet havner på Project 18 med Auto-add. Feiler workflowen igjen, kommer det en kommentar på det samme issuet. Neste vellykkede kjøring lukker det, med en kommentar. Skriptet bruker workflowens egen token (GITHUB_TOKEN med issues: write). Timeline har valget test_failure ved manuell kjøring, som feiler med vilje, så varslingen kan testes ([solution-task-management#41](https://github.com/samt-x/solution-task-management/issues/41) var testen).

**Tidsplanen kan bli slått av.** GitHub slår av planlagte workflows i offentlige repoer etter 60 dager uten aktivitet i repoet. Da kjører ingenting, og ingen feil meldes. Timeline og Snapshot status committer selv minst én gang i døgnet, så så lenge de virker, er det aktivitet. Er en workflow slått av, slås den på igjen under Actions → workflowen → «Enable workflow». Risikoen følges opp i [solution-task-management#42](https://github.com/samt-x/solution-task-management/issues/42).

## Flytte oppgaver mellom repoer

Når et issue flyttes til et annet repo, beholder det kommentarer og historikk, og blir stående på brettene det var på. Det får nytt nummer i det nye repoet. Gamle lenker sendes videre.

Merkelapper som ikke finnes i det nye repoet, faller bort.

## Nytt brett

1. Kopier malen (Project 7) eller et eksisterende brett
2. Gi det navnet «SAMT-BU» etterfulgt av arbeidsområdet
3. Koble det til repoet
4. Slå på Auto-add med filteret is:issue is:open, og sjekk at regelen er lagret
5. Opprett et chore-issue som spor
