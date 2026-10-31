---
title: "Tidslinje med avhengigheter"
linkTitle: "Tidslinje"
weight: 35

---

Timeline-visningen i GitHub Projects viser oppgavene langs en tidsakse, men tegner ikke hvilke oppgaver som venter på hverandre. Figurene på denne siden gjør det. De lages automatisk fra brettene hver time, og oppdateres på docs kort tid etter.

Klikk på en figur for å åpne den i full størrelse. Der kan du klikke på titlene og stolpene for å gå til oppgaven, og holde musa over dem for å se status, datoer og avhengigheter.

**Første versjon, til utprøving** ([solution-task-management#32](https://github.com/samt-x/solution-task-management/issues/32)).

## Eksempel med testoppgaver

Sju testoppgaver i Task management (Project 18) viser hvordan figuren ser ut med avhengigheter. De er ikke ekte oppgaver.

[![Tidslinje med avhengigheter for testoppgavene i Project 18](/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/tidslinje/project-18-nb.svg)](/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/tidslinje/project-18-nb.svg)

## SAMT-BU rammeverk og generisk arkitektur

Project 5. Ingen oppgaver her har avhengigheter ennå, og bare oppgaver med datoer kommer med.

[![Tidslinje med avhengigheter for Project 5](/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/tidslinje/project-5-nb.svg)](/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/tidslinje/project-5-nb.svg)

## Slik leser du figuren

- **Stolpe:** fra startdato til frist. Fargen viser status på brettet. Grå med strek over tittelen betyr at oppgaven er lukket.
- **Stiplet stolpe:** bare startdato. **Rute:** bare frist.
- **Pil:** oppgaven pila peker på, venter på oppgaven pila kommer fra.
- **Rød pil:** oppgaven det ventes på, slutter etter at den ventende skal starte. Planen henger ikke sammen.
- **⛔ foran tittelen:** oppgaven venter fortsatt på en åpen oppgave.
- **Rød loddrett strek:** dagens dato.

Oppgaver uten datoer kommer ikke med. Antallet står under figuren.

## Slik får en oppgave med i figuren

1. Sett **Start date** og **Due date** på brettet. Én av dem holder.
2. Venter oppgaven på en annen oppgave: åpne issuet, finn **Relationships** i høyremargen og velg **Mark as blocked by**. Velg oppgaven det ventes på. Den kan ligge i et annet repo.

Avhengigheter kan også søkes fram på GitHub med **is:blocked**, **is:blocking** og **blocked-by:**.

Hvordan «Blocked by» og merkelappen blocked i [Konvensjoner](../konvensjoner/) skal brukes sammen, er ikke avklart ennå. Forslaget er at «Blocked by» brukes når oppgaven venter på en annen oppgave, og merkelappen når den venter på noe utenfor GitHub.
