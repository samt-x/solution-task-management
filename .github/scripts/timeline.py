"""Tidslinje med avhengigheter fra prosjektbrett (solution-task-management#32).

Timeline-visningen i GitHub Projects tegner ikke avhengighetene mellom issues
(«Blocked by» / «Blocking»). Skriptet leser brettet og tegner en SVG med én rad per
oppgave, en strek for dagens dato og piler fra oppgaven som blokkerer til oppgaven
som venter. Pila er rød når den blokkerende oppgaven slutter etter at den ventende
skal starte.

Alle oppgavene kommer med (se plan). Start og slutt tas fra det som har skjedd
(statusendring til In progress, lukking eller Done), ellers fra Start date og Due date,
ellers regnes de ut fra Duration (arbeidsdager) og oppgavene det ventes på. Mangler
Duration, antas én uke. Stolpen viser hvor datoene kommer fra.

Pilene er lenker til oppgaven som venter. Verktøytipset viser hvorfor (fra overskriften
Avhengigheter i issuet, se describe), slakk eller overlapp i dager, og hvem som koblet
oppgavene og når. En beskrivelse uten «Blocked by» i GitHub gir et varsel under figuren.

Figuren skrives på norsk og engelsk til content/, og vises på siden Tidslinje.
Workflowen committer bare når en fil er endret. Dagens dato er med i figuren, så
den endres minst én gang i døgnet.

Token: miljøvariabelen GH_TOKEN (i Actions: token fra appen SAMT-BU Task sync),
ellers `gh auth token`. Skriptet leser bare brettene og skriver aldri til dem.

Test uten nett: `--data fil.json` leser oppgavene fra en fil i stedet for API-et,
og `--dump fil.json` skriver det som ble hentet. Formatet er lista som `fetch` gir.
"""
import argparse, datetime, html, json, math, os, re, subprocess, sys, time, urllib.request

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ORG = 'samt-x'
# Brett → filnavn uten -nb.svg/-en.svg, relativ til reporoten. Figurene ligger alle på siden Tidslinje og vises på
# sidene Oppgaver og framdrift med inline-svg og stien til Tidslinje (andre argument i shortcoden).
PROJECTS = {1: 'content/tidslinje/project-1',    # Pilot 1 (samt-bu-pilot-1)
            2: 'content/tidslinje/project-2',    # Pilot 2 (samt-bu-pilot-2)
            4: 'content/tidslinje/project-4',    # Pilot 3 (samt-bu-pilot-3) – Project 4 er pilot 3
            3: 'content/tidslinje/project-3',    # Pilot 4 (samt-bu-pilot-4) – Project 3 er pilot 4
            9: 'content/tidslinje/project-9',    # Pilot 5 (samt-bu-pilot-5)
            10: 'content/tidslinje/project-10',  # Pilot 6 (samt-bu-pilot-6)
            19: 'content/tidslinje/project-19',  # Pilot 7 (samt-bu-pilot-7)
            5: 'content/tidslinje/project-5',    # Arkitektur → Overordnet arkitektur (team-architecture)
            6: 'content/tidslinje/project-6',    # Arkitektur → Informasjonsarkitektur (team-semantics; issuene i information-models)
            17: 'content/tidslinje/project-17',  # Docs platform (solution-samt-bu-docs)
            18: 'content/tidslinje/project-18',  # Oppgavestyring (solution-task-management)
            20: 'content/tidslinje/project-20'}  # [EXAMPLE] Timeline: eksemplene i solution-task-management-examples (#40)
# Hvert brett vises på siden Oppgaver og framdrift i innholdsrepoet som eier brettet.
# Eksempeldatoene flyttes hver uke (example-dates.py), så historikken passer ikke med dem. Der leses Start date og
# Due date som det som har skjedd, for eksempler som er startet eller ferdige.
NO_HISTORY = {20}
START, DUE, DURATION = 'Start date', 'Due date', 'Duration'   # dagens dato følger maskinens tidssone (TZ i workflowen)
STARTED = {'In progress', 'In Progress', 'In review'}
DEFAULT_DAYS = 5   # arbeidsdager når Duration mangler

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Farger etter status (GitHubs Primer-palett). Lukkede issues er alltid grå.
COLORS = {'In progress': '#1f6feb', 'In Progress': '#1f6feb', 'In review': '#8250df',
          'Ready': '#54aeff', 'To do': '#54aeff', 'Todo': '#54aeff', 'Backlog': '#9ec9f5',
          'Proposed': '#afb8c1', 'Done': '#2da44e'}
CLOSED = '#8c959f'
DROPPED = {'NOT_PLANNED', 'DUPLICATE'}   # lukket uten å bli gjort (stateReason)
LATE, ARROW, AMBER = '#cf222e', '#57606a', '#bf8700'

TEXT = {
    'nb': {'today': 'I dag', 'months': 'jan feb mar apr mai jun jul aug sep okt nov des',
           'blocked_by': 'Blokkert av', 'blocking': 'Blokkerer', 'outside': 'ikke i figuren',
           'assumed': '{n} oppgaver mangler Duration og er antatt å ta én uke.',
           'legend_arrow': 'Pil: venter på', 'legend_late': 'Rød pil: blokkerende oppgave slutter for sent',
           'legend_actual': 'Mørk: har skjedd', 'legend_set': 'Lys: satte datoer',
           'legend_calc': 'Stiplet: beregnet eller antatt',
           'legend_late_start': 'Gul kant og strek: sen start',
           'legend_done': 'Fullført', 'legend_dropped': 'Skravert og ✕: lukket uten å bli gjort',
           'reason': {'COMPLETED': 'lukket: fullført', 'NOT_PLANNED': 'lukket: ikke gjennomført',
                      'DUPLICATE': 'lukket: duplikat'},
           'legend_overrun': 'Rødt: etter fristen (lyst: prognose)',
           'late_s': 'Sen start: skulle startet {d}', 'late_e': 'Forsinket: skulle vært ferdig {d}',
           'forecast': 'Prognose: ferdig {f}, {n} arbeidsdager etter fristen {d}',
           'made': 'Generert {d} fra', 'empty': 'Ingen oppgaver på brettet ennå.',
           'legend_why': 'Ring: avhengigheten er beskrevet',
           'start': 'Start', 'end': 'Slutt',
           'src': {'actual_s': 'startet (In progress)', 'actual_e': 'ferdig', 'set_s': 'Start date', 'set_e': 'Due date',
                   'due': 'regnet fra slutt og varighet', 'deps': 'etter oppgavene den venter på',
                   'today': 'ikke planlagt, fra i dag', 'start': 'regnet fra start og varighet',
                   'running': 'pågår, forlenget til i dag'},
           'duration': 'Varighet: {n} arbeidsdager', 'no_duration': 'Varighet: ikke satt, antatt {n} arbeidsdager',
           'waits_for': 'venter på', 'why': 'Hvorfor',
           'no_why': 'Ikke beskrevet. Skriv en linje under overskriften Avhengigheter i {o}.',
           'done': '{b} er lukket, så det ventes ikke lenger.',
           'slack': 'Slakk: {n} arbeidsdager', 'overlap': 'Overlapp: {n} arbeidsdager', 'no_slack': 'Ingen slakk',
           'dates': '{b} slutter {end}, {o} starter {start}',
           'added': 'Koblet {d} av {by}', 'click': 'Klikk for å åpne {o}',
           'orphan': '{o} beskriver en avhengighet til {b} under Avhengigheter, men koblingen «Blocked by» finnes ikke i GitHub.'},
    'en': {'today': 'Today', 'months': 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec',
           'blocked_by': 'Blocked by', 'blocking': 'Blocking', 'outside': 'not in the chart',
           'assumed': '{n} tasks have no Duration and are assumed to take one week.',
           'legend_arrow': 'Arrow: waits for', 'legend_late': 'Red arrow: blocking task ends too late',
           'legend_actual': 'Dark: has happened', 'legend_set': 'Light: dates set',
           'legend_calc': 'Dashed: calculated or assumed',
           'legend_late_start': 'Yellow border and line: late start',
           'legend_done': 'Completed', 'legend_dropped': 'Hatched and ✕: closed without being done',
           'reason': {'COMPLETED': 'closed: completed', 'NOT_PLANNED': 'closed: not planned',
                      'DUPLICATE': 'closed: duplicate'},
           'legend_overrun': 'Red: after the due date (light: forecast)',
           'late_s': 'Late start: should have started {d}', 'late_e': 'Overdue: should have been finished {d}',
           'forecast': 'Forecast: finished {f}, {n} working days after the due date {d}',
           'made': 'Generated {d} from', 'empty': 'No tasks on the board yet.',
           'legend_why': 'Ring: the dependency is described',
           'start': 'Start', 'end': 'End',
           'src': {'actual_s': 'started (In progress)', 'actual_e': 'finished', 'set_s': 'Start date', 'set_e': 'Due date',
                   'due': 'calculated from end and duration', 'deps': 'after the tasks it waits for',
                   'today': 'not planned, from today', 'start': 'calculated from start and duration',
                   'running': 'still in progress, extended to today'},
           'duration': 'Duration: {n} working days', 'no_duration': 'Duration: not set, assumed {n} working days',
           'waits_for': 'waits for', 'why': 'Why',
           'no_why': 'Not described. Write a line under the heading Avhengigheter (Dependencies) in {o}.',
           'done': '{b} is closed, so there is no longer anything to wait for.',
           'slack': 'Slack: {n} working days', 'overlap': 'Overlap: {n} working days', 'no_slack': 'No slack',
           'dates': '{b} ends {end}, {o} starts {start}',
           'added': 'Linked {d} by {by}', 'click': 'Click to open {o}',
           'orphan': '{o} describes a dependency on {b} under Avhengigheter, but the «Blocked by» link does not exist in GitHub.'},
}


def token():
    return os.environ.get('GH_TOKEN') or subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()


def gql(query, **variables):
    for forsøk in range(4):
        req = urllib.request.Request('https://api.github.com/graphql',
                                     data=json.dumps({'query': query, 'variables': variables}).encode(),
                                     headers={'Authorization': f'bearer {token()}', 'Content-Type': 'application/json'})
        try:
            d = json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:  # nettverk eller sekundær ratebegrensning
            print('  nytt forsøk etter feil:', e); time.sleep(10 * (forsøk + 1)); continue
        if d.get('errors'):
            if 'Something went wrong' in str(d['errors']) and forsøk < 3:  # forbigående feil hos GitHub
                print('  forbigående feil, prøver igjen'); time.sleep(5 * (forsøk + 1)); continue
            raise SystemExit(f'GraphQL-feil: {d["errors"]}')
        return d['data']
    raise SystemExit('Ga opp etter fire forsøk')


ITEMS = '''query($n:Int!,$after:String){organization(login:"samt-x"){projectV2(number:$n){title url
  items(first:50,after:$after){pageInfo{hasNextPage endCursor} nodes{
    content{... on Issue{number title url state stateReason closedAt body repository{name}
      blockedBy(first:20){nodes{number title url state repository{name}}}
      deps:timelineItems(last:30,itemTypes:[BLOCKED_BY_ADDED_EVENT]){nodes{
        ... on BlockedByAddedEvent{createdAt actor{login} blockingIssue{number repository{name}}}}}
      moves:timelineItems(last:50,itemTypes:[PROJECT_V2_ITEM_STATUS_CHANGED_EVENT]){nodes{
        ... on ProjectV2ItemStatusChangedEvent{createdAt status project{number}}}}}}
    fieldValues(first:30){nodes{
      ... on ProjectV2ItemFieldSingleSelectValue{name field{... on ProjectV2FieldCommon{name}}}
      ... on ProjectV2ItemFieldNumberValue{number field{... on ProjectV2FieldCommon{name}}}
      ... on ProjectV2ItemFieldDateValue{date field{... on ProjectV2FieldCommon{name}}}}}}}}}}'''

# Beskrivelse av avhengighetene (solution-task-management#32, nivå 2): overskriften Avhengigheter
# i issuet som venter, én punktlinje per oppgave det venter på, f.eks. «- #35: trenger juridisk
# avklaring av samtykke». Selve koblingen er alltid «Blocked by» i GitHub; teksten bare beskriver den.
SECTION = re.compile(r'^#{2,4}\s*(Avhengigheter|Dependencies)\s*$', re.I | re.M)
REF = re.compile(r'https://github\.com/samt-x/([\w.-]+)/issues/(\d+)|(?:samt-x/)?([\w.-]+)?#(\d+)', re.I)


def describe(body, repo):
    """Gir {nøkkel: tekst} fra overskriften Avhengigheter i brødteksten."""
    m = SECTION.search(body or '')
    if not m:
        return {}
    rest = body[m.end():]
    end = re.search(r'^#{1,4}\s', rest, re.M)
    out = {}
    for line in (rest[:end.start()] if end else rest).splitlines():
        line = line.strip()
        r = REF.search(line) if line[:1] in '-*' else None
        if r:
            out[f'{r.group(1) or r.group(3) or repo}#{r.group(2) or r.group(4)}'] = line[r.end():].strip(' :–—-').strip()
    return out


def fetch(number):
    """Henter brettet. Gir (tittel, url, oppgaver), der hver oppgave er en dict."""
    tasks, after = [], None
    while True:
        p = gql(ITEMS, n=number, after=after)['organization']['projectV2']
        for it in p['items']['nodes']:
            c = it['content']
            if not c:  # utkast og pull requests tas ikke med
                continue
            v = {f['field']['name']: f.get('name') or f.get('date') or f.get('number')
                 for f in it['fieldValues']['nodes'] if f and f.get('field')}
            repo = c['repository']['name']
            why = describe(c['body'], repo)
            added = {f'{e["blockingIssue"]["repository"]["name"]}#{e["blockingIssue"]["number"]}':
                     (e['createdAt'][:10], (e.get('actor') or {}).get('login'))
                     for e in c['deps']['nodes'] if e and e.get('blockingIssue')}
            # Det som har skjedd: første statusendring til In progress på dette brettet, og lukking eller siste
            # endring til Done. GitHub lagrer endringene som hendelser på issuet.
            moves = sorted((e['createdAt'], e['status']) for e in c['moves']['nodes']
                           if e and (e.get('project') or {}).get('number') == number)
            closed = c['state'] == 'CLOSED'
            finished = closed or v.get('Status') == 'Done'
            started = next((local(ts) for ts, s in moves if s in STARTED), None)
            done = [local(ts) for ts, s in moves if s == 'Done']
            ended = local(c['closedAt']) if closed and c['closedAt'] else (done[-1] if finished and done else None)
            if number in NO_HISTORY:
                started = v.get(START) if finished or v.get('Status') in STARTED else None
                ended = v.get(DUE) if finished else None
            blocked_by = []
            for b in c['blockedBy']['nodes']:
                k = f'{b["repository"]["name"]}#{b["number"]}'
                since, by = added.get(k, (None, None))
                blocked_by.append({'key': k, 'title': b['title'], 'url': b['url'], 'closed': b['state'] == 'CLOSED',
                                   'why': why.pop(k, ''), 'since': since, 'by': by})
            tasks.append({'key': f'{repo}#{c["number"]}', 'title': c['title'], 'url': c['url'],
                          'closed': closed, 'finished': finished, 'status': v.get('Status'),
                          'reason': c.get('stateReason') if closed else None,   # COMPLETED, NOT_PLANNED, DUPLICATE
                          'start': v.get(START), 'due': v.get(DUE), 'duration': v.get(DURATION),
                          'started': started, 'ended': ended, 'blocked_by': blocked_by,
                          'orphans': sorted(why)})   # beskrevet, men uten «Blocked by» i GitHub
        if not p['items']['pageInfo']['hasNextPage']:
            break
        after = p['items']['pageInfo']['endCursor']
    return p['title'], p['url'], tasks


def day(s):
    return datetime.date.fromisoformat(s) if s else None


def local(ts):
    """Tidspunkt fra GitHub (UTC) → dato i maskinens tidssone."""
    return datetime.datetime.fromisoformat(ts.replace('Z', '+00:00')).astimezone().date().isoformat()


def workday(d):
    while d.weekday() >= 5:
        d += datetime.timedelta(days=1)
    return d


def add_days(s, n):
    """Siste arbeidsdag når arbeidet starter s og varer n arbeidsdager."""
    d = workday(s)
    for _ in range(n - 1):
        d = workday(d + datetime.timedelta(days=1))
    return d


def sub_days(e, n):
    """Første arbeidsdag når arbeidet varer n arbeidsdager og slutter e."""
    d = e
    for k in range(n):
        if k:
            d -= datetime.timedelta(days=1)
        while d.weekday() >= 5:
            d -= datetime.timedelta(days=1)
    return d


def count_days(a, b):
    """Arbeidsdager fra og med a til og med b, minst 1."""
    return max(1, sum(1 for k in range((b - a).days + 1) if (a + datetime.timedelta(days=k)).weekday() < 5))


def gap(end, start):
    """Arbeidsdager mellom slutt og start. Negativt tall = overlapp."""
    if start > end:
        return sum(1 for k in range(1, (start - end).days) if (end + datetime.timedelta(days=k)).weekday() < 5)
    return -sum(1 for k in range((end - start).days + 1) if (start + datetime.timedelta(days=k)).weekday() < 5)


def plan(tasks, today):
    """Gir hver oppgave start s og slutt e, og hvor de kommer fra (s_src, e_src).

    Start: det som har skjedd → Start date → slutt minus varighet → dagen etter at oppgavene det
    ventes på slutter, men ikke før i dag. Slutt: det som har skjedd → Due date → start pluss varighet.
    Varigheten er Duration i arbeidsdager, ellers DEFAULT_DAYS (assumed=True)."""
    by = {o['key']: o for o in tasks}
    busy = set()   # vern mot avhengigheter i ring

    def go(o):
        if 's' in o or o['key'] in busy:
            return o
        busy.add(o['key'])
        n = o.get('duration')
        days = max(1, math.ceil(n)) if n else DEFAULT_DAYS
        used = False   # varigheten er brukt
        s, ss = (day(o['started']), 'actual_s') if o.get('started') else (day(o['start']), 'set_s') if o['start'] else (None, None)
        e, es = (day(o['ended']), 'actual_e') if o.get('ended') else (day(o['due']), 'set_e') if o['due'] else (None, None)
        if s is None and e is not None:
            s, ss, used = sub_days(e, days), 'due', True
        # Oppgavene det ventes på, regnes med forventet slutt (f), så en forsinkelse forplanter seg
        after = [go(by[b['key']]).get('f') for b in o['blocked_by'] if b['key'] in by]
        after = [x for x in after if x]
        nxt = workday(max(after) + datetime.timedelta(days=1)) if after else None
        if s is None:
            s, ss = workday(today), 'today'
            if nxt and nxt >= s:
                s, ss = nxt, 'deps'
        if e is None:
            e, es, used = add_days(s, days), 'start', True
        open_ = not o.get('finished')
        started = day(o.get('started'))
        # Sen start: ikke startet, og en start noen har satt (eller regnet med en Duration noen har satt) er passert
        late_s = s if open_ and not started and (ss == 'set_s' or (ss == 'due' and n)) and s < today else None
        # Planlagt slutt: Due date, eller start pluss en Duration noen har satt. Antatt varighet gir aldri rødt.
        planned = e if open_ and (es == 'set_e' or (es == 'start' and n)) else None
        f = None
        if planned:
            # Prognose: start (faktisk, ellers tidligst mulig) pluss varigheten, som er Duration eller planlagt lengde
            span = days if n else (count_days(day(o['start']), day(o['due'])) if o['start'] and o['due'] else None)
            if started:
                fs = started
            else:
                fs = max([workday(today)] + ([nxt] if nxt else []) + ([day(o['start'])] if o['start'] else []))
            fe = add_days(fs, span) if span else planned
            f = max(fe, planned, today if planned < today else planned)
        if es == 'start' and not n and ss == 'actual_s' and open_ and e < today:   # pågår fortsatt, antatt varighet
            e, es = today, 'running'
        e = max(e, s)
        o.update(s=s, e=e, s_src=ss, e_src=es, days=days, assumed=used and not n, late_s=late_s,
                 planned=planned, late_e=planned if planned and planned < today else None, f=max(f or e, e))
        busy.discard(o['key'])
        return o

    for o in tasks:
        go(o)
    return tasks


def esc(s):
    return html.escape(s or '', quote=True)


def fmt(d, lang):
    return f'{d.day}.{d.month}.' if lang == 'nb' else f'{TEXT["en"]["months"].split()[d.month - 1]} {d.day}'


def short(s, n):
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


def svg(number, title, url, tasks, lang, today):
    t = TEXT[lang]
    # Figuren limes rett inn i siden (shortcoden inline-svg), så id-er må være unike på tvers av figurene
    ma, mr, mh = f'tl{number}a', f'tl{number}r', f'tl{number}h'
    months = t['months'].split()
    dated = plan([dict(x) for x in tasks], today)
    assumed = sum(1 for x in dated if x['assumed'])
    LABEL_W, ROW_H, TOP, PAD = 360, 26, 58, 14
    font = 'font-family="-apple-system,Segoe UI,Helvetica,Arial,sans-serif"'

    if not dated:
        h = 70
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="700" height="{h}" viewBox="0 0 700 {h}" {font} font-size="13">'
                f'<rect width="700" height="{h}" fill="#ffffff"/>'
                f'<text x="{PAD}" y="30" fill="#24292f">{esc(t["empty"])}</text>'
                f'<text x="{PAD}" y="52" fill="#57606a" font-size="11">{esc(t["made"].format(d=today.isoformat()))} '
                f'<a href="{esc(url)}" target="_blank"><tspan fill="#0969da">{esc(title)}</tspan></a></text></svg>\n')

    # Tidsaksen: alle datoer pluss i dag, med litt luft på hver side
    dates = [x[k] for x in dated for k in ('s', 'e', 'f')] + [today]
    first = min(dates) - datetime.timedelta(days=3)
    last = max(dates) + datetime.timedelta(days=4)
    days = (last - first).days + 1
    px = max(5, min(22, 760 / days))   # figuren skal stort sett passe i innholdsspalten på docs
    chart_w = days * px
    W = int(LABEL_W + chart_w + PAD)

    def x(d):
        return LABEL_W + (d - first).days * px

    # Rekkefølge: start, så slutt, så nøkkel
    dated.sort(key=lambda o: (o['s'], o['e'], o['key']))
    row = {o['key']: i for i, o in enumerate(dated)}
    H_rows = len(dated) * ROW_H

    # Tegnforklaringen brytes over flere linjer når figuren er smal
    legend = [('arrow', t['legend_arrow']), ('late', t['legend_late']), ('actual', t['legend_actual']),
              ('set', t['legend_set']), ('calc', t['legend_calc']), ('late_start', t['legend_late_start']),
              ('overrun', t['legend_overrun']), ('done', t['legend_done']), ('dropped', t['legend_dropped']),
              ('why', t['legend_why'])]
    places, lx, ly = [], PAD, 0
    for kind, text in legend:
        w = 34 + len(text) * 6.4 + 24
        if lx > PAD and lx + w > W - PAD:
            lx, ly = PAD, ly + 22
        places.append((kind, text, lx, ly))
        lx += w
    legend_y = TOP + H_rows + 36
    foot_y = legend_y + ly + 30
    orphans = [(o['key'], ref) for o in tasks for ref in o.get('orphans', [])]
    H = int(foot_y + 22 + 16 * len(orphans))

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" {font} font-size="12">',
           f'<!-- Generert av .github/scripts/timeline.py (solution-task-management#32). Ikke rediger – endre brettet. -->',
           '<defs>'
           f'<marker id="{ma}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="{ARROW}"/></marker>'
           f'<marker id="{mr}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="{LATE}"/></marker>'
           f'<pattern id="{mh}" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
           f'<rect width="6" height="6" fill="#ffffff"/><line x1="0" y1="0" x2="0" y2="6" stroke="{CLOSED}" stroke-width="2"/></pattern>'
           '</defs>',
           f'<rect width="{W}" height="{H}" fill="#ffffff"/>']

    # Bakgrunn: annenhver rad, helger, månedsnavn og dagstall
    for i in range(len(dated)):
        if i % 2:
            out.append(f'<rect x="0" y="{TOP + i * ROW_H}" width="{W}" height="{ROW_H}" fill="#f6f8fa"/>')
    step = 1 if px >= 18 else (2 if px >= 11 else 7)
    for k in range(days):
        d = first + datetime.timedelta(days=k)
        if d.weekday() >= 5:
            out.append(f'<rect x="{x(d):.1f}" y="{TOP}" width="{px:.1f}" height="{H_rows}" fill="#eaeef2" opacity="0.6"/>')
        nxt = (d.replace(day=28) + datetime.timedelta(days=4)).replace(day=1)
        if d.day == 1 or (k == 0 and (nxt - d).days * px >= 70):   # første måned bare når navnet får plass
            out.append(f'<text x="{x(d) + 2:.1f}" y="20" fill="#24292f" font-weight="600">{months[d.month - 1]} {d.year}</text>')
            out.append(f'<line x1="{x(d):.1f}" y1="8" x2="{x(d):.1f}" y2="{TOP + H_rows}" stroke="#d0d7de"/>')
        if (step == 7 and d.weekday() == 0) or (step < 7 and k % step == 0):
            out.append(f'<text x="{x(d) + px / 2:.1f}" y="44" fill="#57606a" font-size="10" text-anchor="middle">{d.day}</text>')
    out.append(f'<line x1="0" y1="{TOP - 0.5}" x2="{W}" y2="{TOP - 0.5}" stroke="#d0d7de"/>')
    out.append(f'<line x1="{LABEL_W - 0.5}" y1="0" x2="{LABEL_W - 0.5}" y2="{TOP + H_rows}" stroke="#d0d7de"/>')

    # Stolpene og titlene
    span = {}
    for i, o in enumerate(dated):
        y = TOP + i * ROW_H
        mid = y + ROW_H / 2
        s, d = o['s'], o['e']
        color = CLOSED if o['closed'] else COLORS.get(o['status'], '#afb8c1')
        inside = [b for b in o['blocked_by'] if b['key'] in row]
        blocking = [p['key'] for p in dated if any(b['key'] == o['key'] for b in p['blocked_by'])]
        dropped = o['closed'] and o.get('reason') in DROPPED   # lukket uten å bli gjort
        tip = [f'{o["key"]} {o["title"]}', f'{o["status"] or "–"}'
               + (f' ({t["reason"].get(o.get("reason"), t["reason"]["COMPLETED"])})' if o['closed'] else ''),
               f'{t["start"]}: {fmt(s, lang)} ({t["src"][o["s_src"]]})',
               f'{t["end"]}: {fmt(d, lang)} ({t["src"][o["e_src"]]})']
        if o.get('duration'):
            tip.append(t['duration'].format(n=f'{o["duration"]:g}'))
        elif o['assumed']:
            tip.append(t['no_duration'].format(n=o['days']))
        if o['late_s']:
            tip.append(t['late_s'].format(d=fmt(o['late_s'], lang)))
        if o['late_e']:
            tip.append(t['late_e'].format(d=fmt(o['late_e'], lang)))
        if o['planned'] and o['f'] > o['planned'] and o['f'] > today:
            over = sum(1 for k in range(1, (o['f'] - o['planned']).days + 1)
                       if (o['planned'] + datetime.timedelta(days=k)).weekday() < 5)
            tip.append(t['forecast'].format(f=fmt(o['f'], lang), n=over, d=fmt(o['planned'], lang)))
        if o['blocked_by']:
            tip.append(f'{t["blocked_by"]}: ' + ', '.join(b['key'] + ('' if b in inside else f' ({t["outside"]})') for b in o['blocked_by']))
        if blocking:
            tip.append(f'{t["blocking"]}: ' + ', '.join(blocking))
        tip = esc('\n'.join(tip))
        # ⛔ bare når en åpen oppgave fortsatt blokkerer
        # ✕ lukket uten å bli gjort, ✓ fullført, ⛔ venter fortsatt på en åpen oppgave
        mark = ('✕ ' if dropped else '✓ ' if o['closed'] else
                '⛔ ' if any(not b.get('closed') for b in o['blocked_by']) else '')
        label = short(f'{mark}{o["title"]}', 48)
        deco = ' text-decoration="line-through"' if o['closed'] else ''
        number = '#' + o['key'].split('#')[1]
        out.append(f'<a href="{esc(o["url"])}" target="_blank"><title>{tip}</title>'
                   f'<text x="{PAD}" y="{mid + 4:.1f}"><tspan fill="#0969da"{deco}>{esc(label)}</tspan>'
                   f'<tspan dx="5" fill="#57606a" font-size="11">{number}</tspan></text></a>')   # dx: Hugos minify fjerner mellomrom først i tspan

        # Stolpen viser hvor datoene kommer fra: lys med kant når begge er satt eller har skjedd, stiplet når en av
        # dem er beregnet. Det som har skjedd (fra start til slutt, eller til i dag), tegnes mørkt over.
        x1, x2 = x(s), x(d) + px
        firm = o['s_src'] in ('actual_s', 'set_s') and o['e_src'] in ('actual_e', 'set_e')
        edge = AMBER if o['late_s'] else color
        if dropped:   # skravert, uten mørk del: det som var planlagt, ble ikke gjort
            bar = [f'<rect x="{x1:.1f}" y="{y + 6}" width="{x2 - x1:.1f}" height="{ROW_H - 12}" rx="4" '
                   f'fill="url(#{mh})" stroke="{CLOSED}"/>']
        else:
            bar = [f'<rect x="{x1:.1f}" y="{y + 6}" width="{x2 - x1:.1f}" height="{ROW_H - 12}" rx="4" fill="{color}" '
                   + (f'fill-opacity="0.35" stroke="{edge}"/>' if firm else
                      f'fill-opacity="0.12" stroke="{edge}" stroke-dasharray="4 3"/>')]
        if o.get('started') and not dropped:
            a1 = x(max(day(o['started']), s))
            a2 = x(d) + px if o.get('ended') else min(x(today) + px, x2)
            if a2 > a1:
                bar.append(f'<rect x="{a1:.1f}" y="{y + 6}" width="{a2 - a1:.1f}" height="{ROW_H - 12}" rx="4" fill="{color}"/>')
        if o['late_s']:
            # Sen start: gul kant, og gul strek under stolpen fra startdatoen til i dag
            bar.append(f'<line x1="{x(o["late_s"]):.1f}" y1="{y + ROW_H - 3}" x2="{x(today) + px / 2:.1f}" y2="{y + ROW_H - 3}" '
                       f'stroke="{AMBER}" stroke-width="2" stroke-dasharray="4 2"/>')
        end = x2
        if o['planned'] and o['f'] > o['planned']:
            # Sen slutt: stolpen forlenges forbi fristen og fylles rødt; helt rødt til i dag, lyst for prognosen etter
            r1, rt, end = x(o['planned']) + px, x(today) + px, x(o['f']) + px
            if min(rt, end) > r1:
                bar.append(f'<rect x="{r1:.1f}" y="{y + 6}" width="{min(rt, end) - r1:.1f}" height="{ROW_H - 12}" fill="{LATE}"/>')
            if end > max(r1, rt):
                bar.append(f'<rect x="{max(r1, rt):.1f}" y="{y + 6}" width="{end - max(r1, rt):.1f}" height="{ROW_H - 12}" '
                           f'fill="{LATE}" fill-opacity="0.25" stroke="{LATE}" stroke-dasharray="4 3"/>')
        out.append(f'<a href="{esc(o["url"])}" target="_blank"><title>{tip}</title>{"".join(bar)}</a>')
        span[o['key']] = (x1, end, mid, s, o['f'])

    # Pilene: fra slutten på den som blokkerer til starten på den som venter. Hver pil er en lenke til
    # oppgaven som venter (der koblingen og beskrivelsen står), med et bredt usynlig treffområde.
    titles = {p['key']: p['title'] for p in dated}
    for o in dated:
        for b in o['blocked_by']:
            if b['key'] not in span:
                continue
            bx1, bx2, by, bstart, bend = span[b['key']]
            ox1, ox2, oy, ostart, oend = span[o['key']]
            slack = gap(bend, ostart)   # arbeidsdager mellom slutt og start; negativ = overlapp
            late = slack < 0 and not b['closed']
            col, mk = (LATE, mr) if late else (ARROW, ma)
            if ox1 - bx2 >= 16:
                path = f'M{bx2:.1f},{by:.1f}H{bx2 + 8:.1f}V{oy:.1f}H{ox1 - 1:.1f}'
                corner = oy
            else:  # for lite plass: gå rundt, inn fra venstre
                ymid = oy - ROW_H / 2 if oy > by else oy + ROW_H / 2
                path = (f'M{bx2:.1f},{by:.1f}H{bx2 + 8:.1f}V{ymid:.1f}H{ox1 - 10:.1f}V{oy:.1f}H{ox1 - 1:.1f}')
                corner = ymid
            # Ringen står der pila svinger mot målet – unikt per par, også når flere piler deler start eller mål
            ob, bb = '#' + o['key'].split('#')[1], '#' + b['key'].split('#')[1]
            tip = [f'{o["key"]} {o["title"]}', f'{t["waits_for"]} {b["key"]} {titles.get(b["key"], b["title"])}',
                   f'{t["why"]}: {b["why"]}' if b.get('why') else t['no_why'].format(o=ob)]
            if b['closed']:
                tip.append(t['done'].format(b=bb))
            else:
                when = t['dates'].format(b=bb, end=fmt(bend, lang), o=ob, start=fmt(ostart, lang))
                tip.append((t['slack'].format(n=slack) if slack > 0 else t['overlap'].format(n=-slack) if slack < 0
                            else t['no_slack']) + f' ({when})')
            if b.get('since'):
                tip.append(t['added'].format(d=fmt(day(b['since']), lang), by=b.get('by') or '?'))
            tip.append(t['click'].format(o=ob))
            dot = (f'<circle cx="{bx2 + 8:.1f}" cy="{corner:.1f}" r="3.2" fill="#ffffff" stroke="{col}" stroke-width="1.5"/>'
                   if b.get('why') else '')
            # class tl-dep: vinduet i shortcoden inline-svg viser verktøytipset over oppgaven som venter
            out.append(f'<a class="tl-dep" href="{esc(o["url"])}" target="_blank"><title>{esc(chr(10).join(tip))}</title>'
                       f'<path d="{path}" fill="none" stroke="{col}" stroke-width="1.5" marker-end="url(#{mk})"/>{dot}'
                       f'<path d="{path}" fill="none" stroke="#000000" stroke-opacity="0" stroke-width="10" pointer-events="stroke"/></a>')

    # I dag
    tx = x(today) + px / 2
    out.append(f'<line x1="{tx:.1f}" y1="{TOP}" x2="{tx:.1f}" y2="{TOP + H_rows + 4}" stroke="{LATE}" stroke-width="1.5"/>')
    out.append(f'<text x="{tx:.1f}" y="{TOP + H_rows + 15}" fill="{LATE}" font-size="10" text-anchor="middle">{esc(t["today"])}</text>')

    # Tegnforklaring og kilde
    grey = '#8c959f'
    sample = {'arrow': lambda lx, ly: f'<path d="M{lx},{ly}H{lx + 28}" stroke="{ARROW}" stroke-width="1.5" marker-end="url(#{ma})"/>',
              'late': lambda lx, ly: f'<path d="M{lx},{ly}H{lx + 28}" stroke="{LATE}" stroke-width="1.5" marker-end="url(#{mr})"/>',
              'actual': lambda lx, ly: f'<rect x="{lx}" y="{ly - 6}" width="28" height="12" rx="3" fill="{grey}"/>',
              'set': lambda lx, ly: f'<rect x="{lx}" y="{ly - 6}" width="28" height="12" rx="3" fill="{grey}" fill-opacity="0.35" stroke="{grey}"/>',
              'calc': lambda lx, ly: (f'<rect x="{lx}" y="{ly - 6}" width="28" height="12" rx="3" fill="{grey}" fill-opacity="0.12" '
                                      f'stroke="{grey}" stroke-dasharray="4 3"/>'),
              'done': lambda lx, ly: f'<text x="{lx + 8}" y="{ly + 4}" fill="#24292f">✓</text>',
              'dropped': lambda lx, ly: f'<rect x="{lx}" y="{ly - 6}" width="28" height="12" rx="3" fill="url(#{mh})" stroke="{CLOSED}"/>',
              'late_start': lambda lx, ly: (f'<rect x="{lx}" y="{ly - 6}" width="28" height="12" rx="3" fill="{grey}" fill-opacity="0.35" '
                                            f'stroke="{AMBER}"/><line x1="{lx}" y1="{ly + 9}" x2="{lx + 28}" y2="{ly + 9}" '
                                            f'stroke="{AMBER}" stroke-width="2" stroke-dasharray="4 2"/>'),
              'overrun': lambda lx, ly: (f'<rect x="{lx}" y="{ly - 6}" width="14" height="12" fill="{LATE}"/>'
                                         f'<rect x="{lx + 14}" y="{ly - 6}" width="14" height="12" fill="{LATE}" fill-opacity="0.25" '
                                         f'stroke="{LATE}" stroke-dasharray="4 3"/>'),
              'why': lambda lx, ly: f'<circle cx="{lx + 14}" cy="{ly}" r="3.2" fill="#ffffff" stroke="{ARROW}" stroke-width="1.5"/>'}
    for kind, text, lx, dy in places:
        ly = legend_y + dy
        lx = round(lx)
        out.append(sample[kind](lx, ly) + f'<text x="{lx + 34}" y="{ly + 4}" fill="#24292f">{esc(text)}</text>')
    foot = esc(t['made'].format(d=today.isoformat()))
    note = (' ' + esc(t['assumed'].format(n=assumed))) if assumed else ''
    # dx: Hugos minify fjerner mellomrom mellom tekst og lenke
    out.append(f'<text x="{PAD}" y="{foot_y}" fill="#57606a" font-size="11">{foot}'
               f'<a href="{esc(url)}" target="_blank"><tspan dx="4" fill="#0969da">{esc(title)}</tspan></a>.{note}</text>')
    for i, (k, ref) in enumerate(orphans):
        out.append(f'<text x="{PAD}" y="{foot_y + 18 + i * 16}" fill="{LATE}" font-size="11">'
                   f'⚠ {esc(t["orphan"].format(o=k, b=ref))}</text>')
    out.append('</svg>')
    return '\n'.join(out) + '\n'


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    old = open(full, encoding='utf-8').read() if os.path.exists(full) else None
    if old == text:
        print(f'  uendret: {path}')
    else:
        with open(full, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        print(f'  skrev: {path}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', help='les oppgavene fra JSON i stedet for API-et (test)')
    ap.add_argument('--dump', help='skriv oppgavene som ble hentet til JSON')
    ap.add_argument('--out', help='skriv SVG-ene hit i stedet for til content/ (test)')
    ap.add_argument('--today', help='dagens dato, ÅÅÅÅ-MM-DD (test)')
    a = ap.parse_args()
    today = day(a.today) or datetime.date.today()
    for number, base in PROJECTS.items():
        if a.data:
            d = json.load(open(a.data, encoding='utf-8'))
            title, url, tasks = d['title'], d['url'], d['tasks']
        else:
            title, url, tasks = fetch(number)
        if a.dump:
            with open(a.dump, 'w', encoding='utf-8') as f:
                json.dump({'title': title, 'url': url, 'tasks': tasks}, f, ensure_ascii=False, indent=1)
        n = sum(1 for x in tasks if x['start'] or x['due'] or x.get('started') or x.get('ended'))
        print(f'Project {number}: {len(tasks)} oppgaver, {n} med datoer, '
              f'{sum(len(x["blocked_by"]) for x in tasks)} avhengigheter')
        for lang in ('nb', 'en'):
            path = f'{base}-{lang}.svg'
            if a.out:
                path = os.path.join(os.path.abspath(a.out), os.path.basename(path))
            write(path, svg(number, title, url, tasks, lang, today))


main()
