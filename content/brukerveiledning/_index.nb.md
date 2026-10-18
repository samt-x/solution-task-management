---
id: 072203ad-55a2-401b-8cb6-c6aee71f598d
title: "Brukerveiledning"
linkTitle: "Brukerveiledning"
weight: 10
lastmod: 2026-10-18T17:26:48+02:00
last_editor: Erik Hagen

---

Denne siden forklarer hvor en oppgave skal ligge, og hvordan du oppretter, følger opp og lukker den.

## Hvor skal oppgaven ligge?

Oppgaven opprettes i repoet der **ansvaret** ligger. Still spørsmålene i denne rekkefølgen:

| Spørsmål | Hvis ja, legg oppgaven i |
|---|---|
| Gjelder den én bestemt pilot? | Pilotens repo, samt-bu-pilot-1 til samt-bu-pilot-6 |
| Gjelder den flere piloter, eller pilotene som helhet? | samt-bu-common-tasks |
| Gjelder den generisk arkitektur eller sluttleveransen (rammeverket)? | samt-bu-architecture |
| Gjelder den selve nettstedet docs.samt-bu.no (feil, ny funksjon)? | solution-samt-bu-docs |
| Gjelder den hvordan vi styrer oppgaver? | solution-task-management |

Er du i tvil, legg den der du tror den passer best. Oppgaver kan flyttes mellom repoer uten at noe går tapt.

**Én oppgave, ett sted.** Kopier aldri en oppgave til et annet repo. Berører den flere, lenk i stedet – se [Konvensjoner](../konvensjoner/).

## Opprette en oppgave

1. Gå til repoet, velg **Issues** og **New issue**
2. Skriv en kort tittel som sier hva som skal gjøres
3. Beskriv bakgrunnen, hva som skal gjøres, og når oppgaven er ferdig
4. Tildel oppgaven til den eller de som skal jobbe med den (**Assignees**), hvis de har GitHub-bruker
5. Lagre

I pilotrepoene, samt-bu-architecture og information-models havner oppgaven automatisk på repoets prosjektbrett. De øvrige repoene har ikke eget brett.

## Følge opp

Prosjektbrettene finnes under **Projects** i organisasjonen samt-x, eller via lenken i repoet. På brettet kan du flytte oppgaven mellom statuskolonnene, og sette ansvarlig, prioritet og frist der brettet har slike felt.

### Mine oppgaver på tvers av alle brett

Søket **[Mine åpne oppgaver i samt-x](https://github.com/issues?q=is%3Aissue%20is%3Aopen%20assignee%3A%40me%20org%3Asamt-x)** viser alle åpne oppgaver som er tildelt deg, i alle repoene i organisasjonen. Du må være logget inn på GitHub. Legg gjerne lenken inn som bokmerke.

- Søket viser bare oppgaver der du står som **Assignee**. Det er derfor viktig å tildele oppgaver, se [Konvensjoner](../konvensjoner/).
- Prosjektbrettet for arkitekturgruppa har i tillegg visningen **[My tasks (this project)](https://github.com/orgs/samt-x/projects/5/views/7)**, som viser dine oppgaver på det brettet, med brettets egne felt.
- **Assigned to me** i GitHub viser det samme som søket, men også fra andre organisasjoner du er med i.

## Lukke en oppgave

- Skriv alltid en **sluttkommentar** om resultatet, med lenke til siden, dokumentet eller endringen
- Lukk som **completed** når oppgaven er gjort, og som **not planned** når den er droppet – og si hvorfor
- Statusen på brettet settes til ferdig automatisk når oppgaven lukkes
