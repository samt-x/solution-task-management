---
id: 072203ad-55a2-401b-8cb6-c6aee71f598d
title: "Brukerveiledning"
linkTitle: "Brukerveiledning"
weight: 10
lastmod: 2026-10-31T00:33:27+01:00
last_editor: Erik Hagen

---

Denne siden forklarer hvor en oppgave skal ligge, og hvordan du oppretter, følger opp og lukker den.

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

I pilotrepoene, samt-bu-architecture og information-models havner oppgaven automatisk på repoets prosjektbrett. De øvrige repoene har ikke eget brett.

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

## Lukke en oppgave

- Skriv alltid en **sluttkommentar** om resultatet, med lenke til siden, dokumentet eller endringen
- Lukk som **completed** når oppgaven er gjort, som **not planned** når den er avvist, avbrutt eller kansellert, og som **duplicate** når den finnes fra før – og si hvorfor
- Statusen på brettet settes til ferdig automatisk når oppgaven lukkes
