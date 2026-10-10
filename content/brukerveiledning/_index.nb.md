---
title: "Brukerveiledning"
linkTitle: "Brukerveiledning"
weight: 10

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

Oppgaver som er tildelt deg, finner du også under **Assigned to me** i GitHub.

## Lukke en oppgave

- Skriv alltid en **sluttkommentar** om resultatet, med lenke til siden, dokumentet eller endringen
- Lukk som **completed** når oppgaven er gjort, og som **not planned** når den er droppet – og si hvorfor
- Statusen på brettet settes til ferdig automatisk når oppgaven lukkes
