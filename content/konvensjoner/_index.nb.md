---
title: "Konvensjoner"
linkTitle: "Konvensjoner"
weight: 30

---

**Forslag, ikke vedtatt.** Konvensjonene på denne siden er til diskusjon. De bygger på praksisen i solution-samt-bu-docs, som har fungert godt. Diskusjonen foregår i to issues i solution-task-management: «Avtale for felles oppgaver arkitektur/piloter» og «Issue-konvensjon for arkitekturrepoet».

## Én oppgave, ett sted

1. **Én eier per oppgave.** Oppgaven opprettes der ansvaret ligger, se [Brukerveiledning](../brukerveiledning/). Vi kopierer ikke oppgaver mellom repoer.
2. **Lenke i stedet for kopi.** Berører oppgaven et annet område, lenkes det til den i en kommentar. GitHub viser koblingen i begge oppgavene.
3. **Underoppgaver ved avhengighet.** Når en arkitekturoppgave er avhengig av en leveranse fra en pilot, eller omvendt, legges den andre oppgaven inn som underoppgave (sub-issue). Det virker på tvers av repoer, og fremdriften vises på brettet.

Grunnen er at status og andre felt lagres per brett. Ligger samme oppgave på to brett, får den to statuser som fort blir ulike.

## Type angis med merkelapp

| Merkelapp | Brukes til |
|---|---|
| task | Arbeidsoppgave – det meste |
| decision | Krever en beslutning |
| problem | Noe er feil, uklart eller i konflikt |
| chore | Styring og vedlikehold av repo, brett og rutiner |
| future | Ikke nå, men kandidat senere |
| blocked | Venter på noe utenfor oppgaven |

Hver oppgave har én typemerkelapp. future og blocked kommer i tillegg ved behov.

## Faste overskrifter i beskrivelsen

- **Bakgrunn** – hvorfor dette trengs, hva som utløste det
- **Hva skal gjøres** – konkret
- **Ferdig når** – hva som skal foreligge
- **Relatert** – lenker til andre oppgaver, sider eller dokumenter (valgfritt)

For beslutninger i tillegg: **Alternativer** og **Anbefaling**. Selve beslutningen skrives i sluttkommentaren og føres i beslutningsloggen på docs.samt-bu.no.

## Ansvar

- **Responsible** (på brett som har feltet): én person som eier oppgaven
- **Assignees**: alle som jobber med oppgaven, både den ansvarlige og bidragsyterne. Da får de varsler ved endringer, og oppgaven vises under «Assigned to me». Eierskapet står i Responsible, ikke i Assignees.

## Spor for administrative endringer

Endringer i repoer, brett, merkelapper og rutiner får en chore-oppgave som beskriver hva, hvorfor og resultatet. Den legges i repoet endringen gjelder. Sletting skal alltid ha et slikt spor før den gjøres.

## Skrivetips

- Når du skriver om en oppgave uten å ville lenke til den, sett nummeret i kodeformat. Ellers blir det en lenke, og omtalen havner i tidslinjen til den oppgaven.
- Skriv «Project 5», ikke nummertegn foran tallet, av samme grunn.
- Unngå @-omtale med mindre personen skal varsles. En omtale melder personen på hele tråden framover.

## Åpne spørsmål

- Er skillet mellom generisk og pilotspesifikt tydelig nok, eller trengs eksempler?
- Hvem følger med på oppgaver som krysser områder?
- Holder merkelappene over, eller trengs for eksempel deliverable for sluttleveranser?
- Skal konvensjonen gjelde alle repoer, eller bare arbeidsrepoer som samt-bu-architecture?
