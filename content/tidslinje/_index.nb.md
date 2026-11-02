---
id: b5b5edfa-2185-4b4a-925b-1ef9e8c14868
title: "Tidslinje med avhengigheter"
linkTitle: "Tidslinje"
weight: 35
lastmod: 2026-11-02T02:53:51+01:00
last_editor: Erik Hagen

---

Timeline-visningen i GitHub Projects viser oppgavene langs en tidsakse, men tegner ikke hvilke oppgaver som venter på hverandre. Figurene på denne siden gjør det. De lages automatisk fra brettene hver time, og oppdateres på docs kort tid etter. Et fast skript lager dem etter reglene på denne siden. Feiler en kjøring, står den forrige figuren til feilen er rettet, og datoen under figuren viser når den ble laget. Se [Planlagte kjøringer](../teknisk-dokumentasjon/#planlagte-kjøringer).

Klikk på en tittel, en stolpe eller en pil for å se oppgaven i et vindu over figuren. Vinduet flyttes i tittellinjen og endres i størrelse fra hjørnet nede til høyre. Lenker til andre oppgaver inne i vinduet åpnes i det samme vinduet. Klikk et sted utenfor vinduet som ikke er en lenke, trykk Esc eller klikk × for å lukke det. Ctrl-klikk åpner oppgaven på GitHub i stedet. Hold musa over for å se status, datoer og avhengigheter. Figuren vises i full størrelse i en ramme som kan rulles sidelengs og på høyden. Verktøylinja over figuren zoomer ut og inn (− og +), tilbake til full størrelse (100 %) eller slik at hele bredden får plass (Tilpass bredden). Ctrl + musehjul over figuren zoomer bare figuren. Figuren kan også dras med musa (håndmarkør) i alle retninger. Et klikk uten å dra åpner oppgaven som før. «Åpne figuren i nytt vindu» viser figuren alene, der den kan lagres eller kopieres.

Linja **Vis** under verktøylinja velger hvilke oppgaver som vises: **Alle**, **Aktive** (åpne), **Forsinkede** (sen start, passert frist eller prognose etter fristen), **Ferdige** eller **Avbrutte** (lukket uten å bli gjort). En forelder vises når den selv eller en av sub-issuene passer, så sammenhengen ikke forsvinner. Er du logget inn på docs, finnes også knappen **Mine oppgaver**. Den markerer med gul bakgrunn oppgavene der du er Responsible eller assignee, uansett hvilket utvalg som vises. Valgene gjelder bare til siden lastes på nytt.

Vinduet henter oppgaven fra GitHub. Uten innlogging tillater GitHub omtrent 60 oppslag i timen. Er grensen nådd, vises en lenke til GitHub i stedet, og innlogging hever grensen.

**Første versjon, til utprøving** ([solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32)).

## Eksempel

Fjorten eksempler på brettet [«[EXAMPLE] Timeline»](https://github.com/orgs/samt-x/projects/20) viser hvordan figuren ser ut med avhengigheter. De er ikke oppgaver, og ligger i et eget repo, [solution-task-management-examples](https://github.com/samt-x/solution-task-management-examples). Datoene flyttes automatisk hver uke, så eksemplene alltid ligger rundt dagens dato. Derfor viser eksemplene Start date og Due date som det som har skjedd, ikke historikken. Se [Eksempler i dokumentasjonen](../konvensjoner/#eksempler-i-dokumentasjonen).

- **Lukket:** A er fullført (✓). J ble lukket uten å bli gjort (✕).
- **Uten datoer:** G (med Duration 3) og F (uten varighet) plasseres etter oppgavene de venter på.
- **Passert frist:** B skulle vært ferdig fredag forrige uke.
- **Sen start, og forsinkelsen forplanter seg:** D skulle startet samme fredag, men venter fortsatt på B og C. Når C er ferdig, rekker ikke D fristen sin, og E, som venter på D, blir også sen.
- **Frist og Duration, men ingen startdato:** I har ingen avhengigheter, men i dag pluss varigheten går forbi fristen. H venter på C, og tidligste start etter C pluss varigheten går forbi fristen.
- **Sub-issues:** K har tre sub-issues: K1 er ferdig, K2 er ikke startet og har passert fristen, og K3 pågår, men venter på K2. K viser framdriften 1/3, og klammen har rød kant fordi K2 er forsinket. Hullet i den mørke delen er dagene mellom K1 og K3 da ingen av dem var i arbeid. Klikk ▾ foran K for å folde sub-issuene inn. K3 har Responsible satt, så den markeres med **Mine oppgaver** for den som har det brukernavnet.

{{< inline-svg "project-20-nb.svg" >}}

## Hvor figuren brukes

Tidslinjen for et brett vises på siden **Oppgaver og framdrift** i delprosjektet som eier brettet:

| Delprosjekt | Brett |
|---|---|
| [Pilot 1](/pilotering/pilot-1/oppgaver-og-framdrift/) | Project 1 |
| [Pilot 2](/pilotering/pilot-2/oppgaver-og-framdrift/) | Project 2 |
| [Pilot 3](/pilotering/pilot-3/oppgaver-og-framdrift/) | Project 4 |
| [Pilot 4](/pilotering/pilot-4/oppgaver-og-framdrift/) | Project 3 |
| [Pilot 5](/pilotering/pilot-5/oppgaver-og-framdrift/) | Project 9 |
| [Pilot 6](/pilotering/pilot-6/oppgaver-og-framdrift/) | Project 10 |
| [Pilot 7](/pilotering/pilot-7/oppgaver-og-framdrift/) | Project 19 |
| [Overordnet arkitektur](/arkitektur/overordnet-arkitektur/oppgaver-og-framdrift/) | Project 5 |
| [Informasjonsarkitektur](/arkitektur/informasjonsarkitektur/oppgaver-og-framdrift/) | Project 6 |
| [SAMT-BU Docs](/prosjektleveranser/loesninger/samhandlingsplattform/samt-bu-docs/oppgaver-og-framdrift/) | Project 17 |
| [Oppgavestyring](../oppgaver-og-framdrift/) | Project 18 |

Figurene lages alle her, og sidene henter dem herfra. Se [Teknisk dokumentasjon](../teknisk-dokumentasjon/#tidslinje-med-avhengigheter).

## Slik leser du figuren

- **Stolpe:** fra start til slutt. Fargen viser status på brettet. Grå med strek over tittelen betyr at oppgaven er lukket: **✓** foran tittelen betyr fullført, og **✕** med skravert stolpe betyr lukket uten å bli gjort (i GitHub: «Close as not planned» eller duplikat).
- **Mørk del:** det som har skjedd, fra oppgaven ble flyttet til In progress til den ble lukket, eller til i dag hvis den pågår.
- **Lys stolpe med kant:** både start og slutt er satt (Start date og Due date) eller har skjedd.
- **Stiplet stolpe:** minst én av datoene er beregnet, se under.
- **Gul kant og gul strek under stolpen:** sen start. Oppgaven skulle vært startet og er ikke det. Streken går fra startdatoen til i dag.
- **Rødt etter fristen:** sen slutt. Stolpen forlenges forbi fristen, og delen etter fristen er rød. Helt rød er tiden fra fristen til i dag, når fristen er passert uten at oppgaven er ferdig. Lys rød er prognosen: når oppgaven kan bli ferdig hvis den starter i dag, eller når oppgavene den venter på er ferdige, og varer like lenge som planlagt. Varigheten er Duration, ellers lengden fra Start date til Due date. En forsinkelse forplanter seg derfor: blir én oppgave sen, kan oppgavene som venter på den, bli røde før fristen deres er nådd.
- Bare datoer noen har satt, gir gult og rødt: Start date, Due date, eller en dato regnet med Duration. En antatt varighet gir aldri gult eller rødt.
- **Pil:** oppgaven pila peker på, venter på oppgaven pila kommer fra.
- **Rød pil:** oppgaven det ventes på, slutter etter at den ventende skal starte. Planen henger ikke sammen.
- **Hold musa over en pil:** hvorfor oppgaven venter, slakk eller overlapp i arbeidsdager, og hvem som koblet oppgavene og når. Klikk på pila for å se avhengigheten og oppgaven som venter i vinduet.
- **Ring på pila:** avhengigheten er beskrevet. Uten ring står det bare at den mangler beskrivelse.
- **⚠ under figuren:** en oppgave beskriver en avhengighet som ikke er koblet i GitHub.
- **⛔ foran tittelen:** oppgaven venter fortsatt på en åpen oppgave.
- **Rød loddrett strek:** dagens dato.
- **Sub-issues:** står innrykket under forelderen. Forelderen har en klamme fra første start til siste slutt blant sub-issuene på brettet, med prognosen medregnet, og framdriften etter nummeret, for eksempel «#11 · 1/3» (ferdige av alle sub-issuene, også dem på andre brett). Fargen på klammen er forelderens status på brettet. Den mørke delen er det som har skjedd, som på stolpene: periodene der minst én sub-issue var i arbeid (fra In progress til ferdig, eller til i dag). Et lyst hull betyr at ingen av sub-issuene var i arbeid da. **Rød kant** betyr at minst én sub-issue er forsinket, og den synes også når sub-issuene er foldet inn. En lukket forelder har grå klamme med ✓ når den er fullført, og skravert klamme med ✕ når den er lukket uten å bli gjort. Statusen på forelderen settes for hånd og følger ikke sub-issuene automatisk. **▾** foran tittelen folder sub-issuene inn, **▸** folder dem ut igjen. Pilene til og fra sub-issues som er foldet inn, skjules.

## Hvor datoene kommer fra

Alle oppgavene på brettet er med. Start og slutt finnes hver for seg, i denne rekkefølgen:

1. **Det som har skjedd.** Start er første gang oppgaven ble flyttet til In progress (eller In review) på brettet. Slutt er når oppgaven ble lukket eller flyttet til Done. GitHub registrerer dette selv.
2. **Satt dato:** Start date og Due date på brettet.
3. **Beregnet fra varigheten:** finnes bare den ene datoen, regnes den andre ut med feltet **Duration** (arbeidsdager).
4. **Beregnet fra avhengighetene:** mangler start, starter oppgaven arbeidsdagen etter at den siste oppgaven den venter på, slutter. Den starter likevel ikke før i dag. Venter den ikke på noe, starter den i dag.

Mangler Duration, antas én uke (fem arbeidsdager). Antallet slike oppgaver står under figuren. Pågår en oppgave lenger enn planlagt, forlenges stolpen til i dag. Hold musa over stolpen for å se datoene og hvor de kommer fra.

Planlagte og faktiske datoer har ikke egne felt. Det som har skjedd, ligger i historikken i GitHub.

## Slik får en oppgave riktig plass i figuren

1. Sett **Start date** og **Due date** på brettet, eller én av dem og **Duration**. Uten noen av dem plasseres oppgaven etter oppgavene den venter på.
2. Flytt kortet til **In progress** når arbeidet begynner, og lukk oppgaven når den er ferdig.
3. Venter oppgaven på en annen oppgave: åpne issuet, finn **Relationships** i høyremargen og velg **Mark as blocked by**. Velg oppgaven det ventes på. Den kan ligge i et annet repo.
4. Skriv hvorfor oppgaven venter under overskriften **Avhengigheter** i issuet, én linje per oppgave, for eksempel «- #35: trenger juridisk avklaring av samtykke». Task-skjemaet har et eget felt for det. Er oppgaven i et annet repo, skriv for eksempel samt-bu-pilot-6#12. Selve koblingen er alltid den i steg 3. Teksten beskriver den bare. Se [Konvensjoner](../konvensjoner/).

Deler du en oppgave i mindre oppgaver, gjør dem til sub-issues: åpne forelderen, velg **Create sub-issue** eller **Add existing issue** nederst i beskrivelsen. Sub-issuene må ligge på samme brett for å vises under forelderen i figuren.

Avhengigheter kan også søkes fram på GitHub med **is:blocked**, **is:blocking** og **blocked-by:**.

Venter oppgaven på noe utenfor GitHub, brukes merkelappen blocked i stedet. Den gir ingen pil. Se [Blokkert](../konvensjoner/#blokkert) i Konvensjoner.
