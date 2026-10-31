---
id: b5b5edfa-2185-4b4a-925b-1ef9e8c14868
title: "Tidslinje med avhengigheter"
linkTitle: "Tidslinje"
weight: 35
lastmod: 2026-10-31T02:11:13+01:00
last_editor: Erik Hagen

---

Timeline-visningen i GitHub Projects viser oppgavene langs en tidsakse, men tegner ikke hvilke oppgaver som venter på hverandre. Figurene på denne siden gjør det. De lages automatisk fra brettene hver time, og oppdateres på docs kort tid etter.

Klikk på en tittel eller en stolpe for å gå til oppgaven på GitHub. Hold musa over for å se status, datoer og avhengigheter. Er spalten smal, kan figuren rulles sidelengs.

**Første versjon, til utprøving** ([solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32)).

## Eksempel med testoppgaver

Sju testoppgaver i Task management (Project 18) viser hvordan figuren ser ut med avhengigheter. De er ikke ekte oppgaver.

{{< inline-svg "project-18-nb.svg" >}}

## SAMT-BU rammeverk og generisk arkitektur

Project 5. Ingen oppgaver her har avhengigheter ennå, og bare oppgaver med datoer kommer med.

{{< inline-svg "project-5-nb.svg" >}}

## Slik leser du figuren

- **Stolpe:** fra startdato til frist. Fargen viser status på brettet. Grå med strek over tittelen betyr at oppgaven er lukket.
- **Stiplet stolpe:** bare startdato. **Rute:** bare frist.
- **Pil:** oppgaven pila peker på, venter på oppgaven pila kommer fra.
- **Rød pil:** oppgaven det ventes på, slutter etter at den ventende skal starte. Planen henger ikke sammen.
- **Hold musa over en pil:** hvorfor oppgaven venter, slakk eller overlapp i dager, og hvem som koblet oppgavene og når. Klikk på pila for å åpne oppgaven som venter.
- **Ring på pila:** avhengigheten er beskrevet. Uten ring står det bare at den mangler beskrivelse.
- **⚠ under figuren:** en oppgave beskriver en avhengighet som ikke er koblet i GitHub.
- **⛔ foran tittelen:** oppgaven venter fortsatt på en åpen oppgave.
- **Rød loddrett strek:** dagens dato.

Oppgaver uten datoer kommer ikke med. Antallet står under figuren.

## Slik får en oppgave med i figuren

1. Sett **Start date** og **Due date** på brettet. Én av dem holder.
2. Venter oppgaven på en annen oppgave: åpne issuet, finn **Relationships** i høyremargen og velg **Mark as blocked by**. Velg oppgaven det ventes på. Den kan ligge i et annet repo.
3. Skriv hvorfor oppgaven venter under overskriften **Avhengigheter** i issuet, én linje per oppgave, for eksempel «- #35: trenger juridisk avklaring av samtykke». Task-skjemaet har et eget felt for det. Er oppgaven i et annet repo, skriv for eksempel samt-bu-pilot-6#12. Selve koblingen er alltid den i steg 2. Teksten beskriver den bare. Se [Konvensjoner](../konvensjoner/).

Avhengigheter kan også søkes fram på GitHub med **is:blocked**, **is:blocking** og **blocked-by:**.

Hvordan «Blocked by» og merkelappen blocked i [Konvensjoner](../konvensjoner/) skal brukes sammen, er ikke avklart ennå. Forslaget er at «Blocked by» brukes når oppgaven venter på en annen oppgave, og merkelappen når den venter på noe utenfor GitHub.
