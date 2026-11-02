---
id: 072203ad-55a2-401b-8cb6-c6aee71f598d
title: "Brukerveiledning"
linkTitle: "Brukerveiledning"
weight: 10
lastmod: 2026-11-02T10:46:55+01:00
last_editor: Erik Hagen

---

Denne siden forklarer hvor en oppgave skal ligge, og hvordan du oppretter, følger opp, kobler og lukker den. Til slutt står [tips til bruk av GitHub](#tips-github-til-oppgavestyring).

## Hvor skal oppgaven ligge?

Oppgaven opprettes i repoet der **ansvaret** ligger. Still spørsmålene i denne rekkefølgen:

| Spørsmål | Hvis ja, legg oppgaven i |
|---|---|
| Gjelder den én bestemt pilot? | Pilotens repo, samt-bu-pilot-1 til samt-bu-pilot-7 |
| Gjelder den flere piloter, eller pilotene som helhet? | samt-bu-common-tasks |
| Gjelder den generisk arkitektur eller sluttleveransen (rammeverket)? | samt-bu-architecture |
| Gjelder den selve nettstedet docs.samt-bu.no (feil, ny funksjon)? | solution-samt-bu-docs |
| Gjelder den hvordan vi styrer oppgaver? | solution-task-management |

Er du i tvil, legg den der du tror den passer best. Oppgaver kan flyttes mellom repoer uten at noe går tapt.

**Én oppgave, ett sted.** Kopier aldri en oppgave til et annet repo. Berører den flere, lenk i stedet – se [Konvensjoner](../konvensjoner/).

## Opprette en oppgave

1. Gå til repoet, velg **Issues** og **New issue**
2. Velg skjemaet for typen saken har: Task, Solution proposal, Question, Decision, Risk eller Problem. Se [Konvensjoner](../konvensjoner/) for hva de betyr. Skjemaet setter typen for deg. I Problem-skjemaet velger du også hva slags problem det er, eller foreslår et nytt valg.
3. Skriv en kort tittel som sier hva saken gjelder, og fyll ut feltene. Bare de første feltene er påkrevd.
4. I feltet **Gjelder** kan du lime inn en lenke til det saken handler om: en side på docs, et case, en annen oppgave eller et element i Archi-modellen. Hold selve saken kort. Planer, beskrivelser og resultater skriver du på docs-siden, ikke i issuet (se [én master per opplysning](../konvensjoner/#oppgaven-på-github-innholdet-på-docs)).
5. Tildel saken til den eller de som skal jobbe med den (**Assignees**), hvis de har GitHub-bruker. **Unntak:** er saken et innspill som ennå ikke er behandlet, skal den ikke tildeles. Skriv heller @brukernavn i feltet **Forslag til hvem som bør se på dette**. Da får de et varsel og kan følge saken.
6. Lagre med **Create**

Skjemaene gjelder alle repoene i samt-x. Vil du skrive helt fritt, velg **Blank issue** nederst i lista, og velg typen selv i feltet **Type** til høyre.

Oppgaven havner automatisk på repoets prosjektbrett. Alle repoene i tabellen over har eget brett, unntatt samt-bu-common-tasks. Information-models har også brett. Oppgavene fra alle repoene samles hver time på [SAMT-BU Overview – All tasks](https://github.com/orgs/samt-x/projects/12), også fra samt-bu-common-tasks.

## Følge opp

Prosjektbrettene finnes under **Projects** i organisasjonen samt-x, eller via lenken i repoet. På brettet kan du flytte oppgaven mellom statuskolonnene, og sette ansvarlig, prioritet og frist der brettet har slike felt.

### Mine oppgaver på tvers av alle brett

Søket **[Mine åpne oppgaver i samt-x](https://github.com/issues?q=is%3Aissue%20is%3Aopen%20assignee%3A%40me%20org%3Asamt-x)** viser alle åpne oppgaver som er tildelt deg, i alle repoene i organisasjonen. Du må være logget inn på GitHub. Legg gjerne lenken inn som bokmerke.

Dette søket og flere andre, sammen med lenker til alle brettene, finner du samlet under [Styring → Oppgaver og oppfølging](https://docs.samt-bu.no/prosjektstyring/oppgaver-og-oppfolging/).

- Søket viser bare oppgaver der du står som **Assignee**. Det er derfor viktig å tildele oppgaver, se [Konvensjoner](../konvensjoner/).
- Prosjektbrettet for arkitekturgruppa har i tillegg visningen **[My tasks (this project)](https://github.com/orgs/samt-x/projects/5/views/7)**, som viser dine oppgaver på det brettet, med brettets egne felt.
- **Assigned to me** i GitHub viser det samme som søket, men også fra andre organisasjoner du er med i.

### Statuskommentar i arkitekturmøtet

Project 5 har feltet **Comment**, som viser siste status for hver oppgave. Slik oppdaterer du det:

1. Åpne visningen [All tasks](https://github.com/orgs/samt-x/projects/5/views/1). Hver linje er én oppgave.
2. Finn linjen for oppgaven din. Kolonnen Responsible viser hvem som eier den.
3. Dobbeltklikk på cellen i kolonnen Comment, skriv dato og status, for eksempel «23.10: Utkast sendt til Anders», og trykk Enter.

Skriv over den gamle kommentaren. Feltet har bare én linje, og den forrige blir tatt vare på i [statushistorikken](https://github.com/samt-x/solution-task-management/commits/main/status/project-5.md), som oppdateres hver time.

**Lese hele kommentaren:** Lange kommentarer blir kuttet i tabellen. Klikk på tittelen til oppgaven, så åpnes et panel til høyre med hele kommentaren og de andre feltene. Vil du se alle kommentarene samlet, bruk [statustabellen](https://github.com/samt-x/solution-task-management/blob/main/status/project-5.md), som også oppdateres hver time.

## Avhengigheter mellom oppgaver

Når en oppgave ikke kan starte eller bli ferdig før en annen oppgave er gjort, kobler du dem i GitHub. Da ser alle at oppgaven venter, og [tidslinjen](../tidslinje/) tegner en pil mellom dem.

### Innen samme prosjekt

1. Åpne oppgaven som **venter**.
2. Finn **Relationships** i høyremargen, og velg **Mark as blocked by**.
3. Søk opp oppgaven det ventes på, med tittel eller nummer, og velg den.
4. Skriv hvorfor oppgaven venter i beskrivelsen, under overskriften **Avhengigheter**, én linje per oppgave, for eksempel «- #35: trenger juridisk avklaring av samtykke». Task-skjemaet har et eget felt for det.

Oppgaven det ventes på, viser koblingen som **Blocking**. Når den lukkes, regnes ventingen som over.

### På tvers av prosjekter

Koblingen virker også når oppgavene ligger i forskjellige repoer i samt-x, for eksempel en arkitekturoppgave som venter på en leveranse fra en pilot.

- Gjør det samme som over, fra oppgaven som venter. Finner du ikke oppgaven i søket, lim inn lenken til den.
- Under Avhengigheter skriver du organisasjonen og repoet foran nummeret, for eksempel «- samt-x/samt-bu-pilot-6#12: trenger testdata fra piloten». Uten samt-x/ blir det ingen lenke.
- Tidslinjen tegner bare pil mellom oppgaver på **samme brett**. Ligger oppgaven det ventes på, på et annet brett, får den ventende oppgaven ⛔ foran tittelen, og verktøytipset sier at oppgaven det ventes på, ikke er i figuren.

### Venter på, del av, eller venter på noe utenfor GitHub?

| Situasjonen | Bruk |
|---|---|
| Oppgaven venter på en annen oppgave | **Mark as blocked by** (over) |
| Oppgaven er en del av en større oppgave | Sub-issue: åpne den store oppgaven og velg **Create sub-issue** eller **Add existing issue**. Se [Tidslinje](../tidslinje/#slik-får-en-oppgave-riktig-plass-i-figuren). |
| Oppgaven venter på noe som ikke er en oppgave i GitHub (et svar, en avtale, en beslutning et annet sted) | Merkelappen **blocked**, se [Blokkert](../konvensjoner/#blokkert) |

Avhengigheter kan søkes fram med **is:blocked** (venter på noe) og **is:blocking** (noe venter på den).

## Lukke en oppgave

- Skriv alltid en **sluttkommentar** om resultatet, med lenke til siden, dokumentet eller endringen
- Lukk som **completed** når oppgaven er gjort, som **not planned** når den er avvist, avbrutt eller kansellert, og som **duplicate** når den finnes fra før – og si hvorfor
- Statusen på brettet settes til ferdig automatisk når oppgaven lukkes

## Tips: GitHub til oppgavestyring

Her er det som gjør hverdagen enklest, samlet på ett sted. Detaljene står i kapitlene over og i [Konvensjoner](../konvensjoner/).

### Finne fram

- **Dine oppgaver:** bokmerk søket [Mine åpne oppgaver i samt-x](https://github.com/issues?q=is%3Aissue%20is%3Aopen%20assignee%3A%40me%20org%3Asamt-x). Det er den raskeste veien til det du skal gjøre.
- **Alle brettene og de faste søkene** står samlet under [Styring → Oppgaver og oppfølging](https://docs.samt-bu.no/prosjektstyring/oppgaver-og-oppfolging/).
- **Samlebrettet** [SAMT-BU Overview – All tasks](https://github.com/orgs/samt-x/projects/12) viser oppgavene fra alle repoene.
- **Tidslinjen** for hvert brett står på siden «Oppgaver og framdrift» for piloten eller løsningen, se [Tidslinje](../tidslinje/). Er du logget inn på docs, er dine oppgaver markert med gult.

### Nyttige søk

Skriv søket i søkefeltet på [github.com/issues](https://github.com/issues) (krever innlogging) eller i oppgavelisten i et repo. Søkeordene kan kombineres, for eksempel `is:open assignee:@me org:samt-x`.

| Søkeord | Viser |
|---|---|
| `org:samt-x` | bare oppgaver i samt-x |
| `repo:samt-x/samt-bu-pilot-6` | bare oppgaver i ett repo |
| `is:open` | bare åpne oppgaver |
| `assignee:@me` | oppgaver tildelt deg |
| `no:assignee` | oppgaver som ikke er tildelt noen |
| `mentions:@me` | oppgaver der du er @-omtalt |
| `is:blocked` | oppgaver som venter på en annen oppgave |
| `is:blocking` | oppgaver som en annen oppgave venter på |
| `label:blocked` | oppgaver som venter på noe utenfor GitHub |
| `type:Risk` | én type: Task, Decision, Question, Risk … |
| `sort:updated-desc` | sist endret først |

### Lenk, ikke kopier

- `#12` lenker til oppgave 12 i samme repo. Er oppgaven i et annet repo, skriv `samt-x/samt-bu-pilot-6#12`. Du kan også lime inn hele adressen, så viser GitHub den i kortform.
- Lenken gir en merknad i oppgaven det lenkes til, så sammenhengen synes fra begge sider.
- Venter oppgaven på en annen, bruk **Mark as blocked by**. Er den en del av en større oppgave, bruk sub-issue. Se [Avhengigheter mellom oppgaver](#avhengigheter-mellom-oppgaver).
- Vil du nevne et nummer uten å lenke, sett det i kodeformat, se [Skrivetips](../konvensjoner/#skrivetips).

### Varsler

- `@brukernavn` varsler personen og melder vedkommende på hele tråden framover. Bruk det når personen skal følge saken.
- Du får varsler om oppgaver du har opprettet, er tildelt eller er @-omtalt i. Vil du følge en annen oppgave, velg **Subscribe** i høyremargen.
- Varslene samles på [github.com/notifications](https://github.com/notifications). Om de også kommer som e-post, velger du under **Settings → Notifications** i GitHub.

### På brettet

- Sett status **In progress** når du begynner. Når oppgaven lukkes, settes den til ferdig automatisk. Tidslinjen bruker disse tidspunktene som faktisk start og slutt.
- Gi oppgaven **Start date** og **Duration** (arbeidsdager), eller **Due date**. Da får den riktig plass i tidslinjen, se [Tidslinje](../tidslinje/#slik-får-en-oppgave-riktig-plass-i-figuren).
- Klikk på tittelen til en oppgave på brettet for å se og endre alle feltene i et panel, uten å forlate brettet.
- Sub-issues havner på samme brett som oppgaven de er en del av.

### Hurtigtaster

| Tast | Gjør |
|---|---|
| `/` | Går til søkefeltet |
| `?` | Viser alle hurtigtastene på siden |
| `c` | Ny oppgave, fra oppgavelisten i et repo |
| `r` | Siterer teksten du har markert, i svaret ditt |
| `Ctrl+Enter` | Lagrer kommentaren |

Marker tekst i skrivefeltet og lim inn en adresse, så blir teksten en lenke.
