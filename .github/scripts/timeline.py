"""Tidslinje med avhengigheter fra prosjektbrett (solution-task-management#32).

Timeline-visningen i GitHub Projects tegner ikke avhengighetene mellom issues
(«Blocked by» / «Blocking»). Skriptet leser brettet og tegner en SVG med én rad per
oppgave som har datoer, en strek for dagens dato og piler fra oppgaven som blokkerer
til oppgaven som venter. Pila er rød når den blokkerende oppgaven slutter etter at
den ventende skal starte.

Figuren skrives på norsk og engelsk til content/, og vises på siden Tidslinje.
Workflowen committer bare når en fil er endret. Dagens dato er med i figuren, så
den endres minst én gang i døgnet.

Token: miljøvariabelen GH_TOKEN (i Actions: token fra appen SAMT-BU Task sync),
ellers `gh auth token`. Skriptet leser bare brettene og skriver aldri til dem.

Test uten nett: `--data fil.json` leser oppgavene fra en fil i stedet for API-et,
og `--dump fil.json` skriver det som ble hentet. Formatet er lista som `fetch` gir.
"""
import argparse, datetime, html, json, os, subprocess, sys, time, urllib.request

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ORG = 'samt-x'
PROJECTS = {5: 'content/tidslinje/project-5',    # brett → filnavn uten -nb.svg/-en.svg, relativ til reporoten
            18: 'content/tidslinje/project-18'}  # testoppgavene #33–#39 ligger her
START, DUE = 'Start date', 'Due date'   # dagens dato følger maskinens tidssone (TZ i workflowen)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Farger etter status (GitHubs Primer-palett). Lukkede issues er alltid grå.
COLORS = {'In progress': '#1f6feb', 'In Progress': '#1f6feb', 'In review': '#8250df',
          'Ready': '#54aeff', 'To do': '#54aeff', 'Todo': '#54aeff', 'Backlog': '#9ec9f5',
          'Proposed': '#afb8c1', 'Done': '#2da44e'}
CLOSED = '#8c959f'
LATE, ARROW = '#cf222e', '#57606a'

TEXT = {
    'nb': {'today': 'I dag', 'months': 'jan feb mar apr mai jun jul aug sep okt nov des',
           'blocked_by': 'Blokkert av', 'blocking': 'Blokkerer', 'outside': 'ikke i figuren',
           'no_dates': '{n} oppgaver på brettet har verken startdato eller frist og er ikke med.',
           'legend_arrow': 'Pil: venter på', 'legend_late': 'Rød pil: blokkerende oppgave slutter for sent',
           'legend_open': 'Stiplet: bare startdato', 'legend_due': 'Rute: bare frist',
           'made': 'Generert {d} fra', 'empty': 'Ingen oppgaver på brettet har datoer ennå.'},
    'en': {'today': 'Today', 'months': 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec',
           'blocked_by': 'Blocked by', 'blocking': 'Blocking', 'outside': 'not in the chart',
           'no_dates': '{n} tasks on the board have neither start date nor due date and are not shown.',
           'legend_arrow': 'Arrow: waits for', 'legend_late': 'Red arrow: blocking task ends too late',
           'legend_open': 'Dashed: start date only', 'legend_due': 'Diamond: due date only',
           'made': 'Generated {d} from', 'empty': 'No tasks on the board have dates yet.'},
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
    content{... on Issue{number title url state repository{name}
      blockedBy(first:20){nodes{number title url state repository{name}}}}}
    fieldValues(first:30){nodes{
      ... on ProjectV2ItemFieldSingleSelectValue{name field{... on ProjectV2FieldCommon{name}}}
      ... on ProjectV2ItemFieldDateValue{date field{... on ProjectV2FieldCommon{name}}}}}}}}}}'''


def fetch(number):
    """Henter brettet. Gir (tittel, url, oppgaver), der hver oppgave er en dict."""
    tasks, after = [], None
    while True:
        p = gql(ITEMS, n=number, after=after)['organization']['projectV2']
        for it in p['items']['nodes']:
            c = it['content']
            if not c:  # utkast og pull requests tas ikke med
                continue
            v = {f['field']['name']: f.get('name') or f.get('date')
                 for f in it['fieldValues']['nodes'] if f and f.get('field')}
            tasks.append({'key': f'{c["repository"]["name"]}#{c["number"]}', 'title': c['title'], 'url': c['url'],
                          'closed': c['state'] == 'CLOSED', 'status': v.get('Status'),
                          'start': v.get(START), 'due': v.get(DUE),
                          'blocked_by': [{'key': f'{b["repository"]["name"]}#{b["number"]}', 'title': b['title'], 'url': b['url'],
                                          'closed': b['state'] == 'CLOSED'} for b in c['blockedBy']['nodes']]})
        if not p['items']['pageInfo']['hasNextPage']:
            break
        after = p['items']['pageInfo']['endCursor']
    return p['title'], p['url'], tasks


def day(s):
    return datetime.date.fromisoformat(s) if s else None


def esc(s):
    return html.escape(s or '', quote=True)


def short(s, n):
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


def svg(number, title, url, tasks, lang, today):
    t = TEXT[lang]
    # Figuren limes rett inn i siden (shortcoden inline-svg), så id-er må være unike på tvers av figurene
    ma, mr = f'tl{number}a', f'tl{number}r'
    months = t['months'].split()
    dated = [x for x in tasks if x['start'] or x['due']]
    undated = len(tasks) - len(dated)
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
    dates = [day(x[k]) for x in dated for k in ('start', 'due') if x[k]] + [today]
    first = min(dates) - datetime.timedelta(days=3)
    last = max(dates) + datetime.timedelta(days=4)
    days = (last - first).days + 1
    px = max(5, min(22, 760 / days))   # figuren skal stort sett passe i innholdsspalten på docs
    chart_w = days * px
    W = int(LABEL_W + chart_w + PAD)

    def x(d):
        return LABEL_W + (d - first).days * px

    # Rekkefølge: tidligste dato først, så frist, så nøkkel
    def order(o):
        s, d = day(o['start']), day(o['due'])
        return (s or d, d or s, o['key'])
    dated.sort(key=order)
    row = {o['key']: i for i, o in enumerate(dated)}
    H_rows = len(dated) * ROW_H
    legend_y = TOP + H_rows + 36
    H = int(legend_y + 52)

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" {font} font-size="12">',
           f'<!-- Generert av .github/scripts/timeline.py (solution-task-management#32). Ikke rediger – endre brettet. -->',
           '<defs>'
           f'<marker id="{ma}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="{ARROW}"/></marker>'
           f'<marker id="{mr}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0L10,5L0,10z" fill="{LATE}"/></marker>'
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
        if d.day == 1 or k == 0:
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
        s, d = day(o['start']), day(o['due'])
        color = CLOSED if o['closed'] else COLORS.get(o['status'], '#afb8c1')
        inside = [b for b in o['blocked_by'] if b['key'] in row]
        outside = [b for b in o['blocked_by'] if b['key'] not in row]
        blocking = [p['key'] for p in dated if any(b['key'] == o['key'] for b in p['blocked_by'])]
        tip = [f'{o["key"]} {o["title"]}', f'{o["status"] or "–"}' + (' (closed)' if o['closed'] else ''),
               f'{o["start"] or "…"} → {o["due"] or "…"}']
        if o['blocked_by']:
            tip.append(f'{t["blocked_by"]}: ' + ', '.join(b['key'] + ('' if b in inside else f' ({t["outside"]})') for b in o['blocked_by']))
        if blocking:
            tip.append(f'{t["blocking"]}: ' + ', '.join(blocking))
        tip = esc('\n'.join(tip))
        # ⛔ bare når en åpen oppgave fortsatt blokkerer
        mark = '⛔ ' if not o['closed'] and any(not b.get('closed') for b in o['blocked_by']) else ''
        label = short(f'{mark}{o["title"]}', 48)
        deco = ' text-decoration="line-through"' if o['closed'] else ''
        number = '#' + o['key'].split('#')[1]
        out.append(f'<a href="{esc(o["url"])}" target="_blank"><title>{tip}</title>'
                   f'<text x="{PAD}" y="{mid + 4:.1f}"><tspan fill="#0969da"{deco}>{esc(label)}</tspan>'
                   f'<tspan dx="5" fill="#57606a" font-size="11">{number}</tspan></text></a>')   # dx: Hugos minify fjerner mellomrom først i tspan

        if s and d and d >= s:
            x1, x2 = x(s), x(d) + px
            out.append(f'<a href="{esc(o["url"])}" target="_blank"><title>{tip}</title>'
                       f'<rect x="{x1:.1f}" y="{y + 6}" width="{x2 - x1:.1f}" height="{ROW_H - 12}" rx="4" fill="{color}"/></a>')
        elif s:
            x1 = x(s)
            x2 = max(x(today) + px, x1 + 7 * px) if not d else x1 + px
            out.append(f'<a href="{esc(o["url"])}" target="_blank"><title>{tip}</title>'
                       f'<rect x="{x1:.1f}" y="{y + 6}" width="{x2 - x1:.1f}" height="{ROW_H - 12}" rx="4" fill="{color}" '
                       f'fill-opacity="0.35" stroke="{color}" stroke-dasharray="4 3"/></a>')
        else:
            cx = x(d) + px / 2
            x1, x2 = cx - 7, cx + 7
            out.append(f'<a href="{esc(o["url"])}" target="_blank"><title>{tip}</title>'
                       f'<path d="M{cx:.1f},{mid - 8:.1f}L{cx + 8:.1f},{mid:.1f}L{cx:.1f},{mid + 8:.1f}L{cx - 8:.1f},{mid:.1f}z" fill="{color}"/></a>')
        span[o['key']] = (x1, x2, mid, s or d, d or s)

    # Pilene: fra slutten på den som blokkerer til starten på den som venter
    for o in dated:
        for b in o['blocked_by']:
            if b['key'] not in span:
                continue
            bx1, bx2, by, bstart, bend = span[b['key']]
            ox1, ox2, oy, ostart, oend = span[o['key']]
            late = bend >= ostart and not (o['closed'] and next(p for p in dated if p['key'] == b['key'])['closed'])
            col, mk = (LATE, mr) if late else (ARROW, ma)
            if ox1 - bx2 >= 16:
                path = f'M{bx2:.1f},{by:.1f}H{bx2 + 8:.1f}V{oy:.1f}H{ox1 - 1:.1f}'
            else:  # for lite plass: gå rundt, inn fra venstre
                ymid = oy - ROW_H / 2 if oy > by else oy + ROW_H / 2
                path = (f'M{bx2:.1f},{by:.1f}H{bx2 + 8:.1f}V{ymid:.1f}H{ox1 - 10:.1f}V{oy:.1f}H{ox1 - 1:.1f}')
            out.append(f'<path d="{path}" fill="none" stroke="{col}" stroke-width="1.5" marker-end="url(#{mk})">'
                       f'<title>{esc(o["key"])} ← {esc(b["key"])}</title></path>')

    # I dag
    tx = x(today) + px / 2
    out.append(f'<line x1="{tx:.1f}" y1="{TOP}" x2="{tx:.1f}" y2="{TOP + H_rows + 4}" stroke="{LATE}" stroke-width="1.5"/>')
    out.append(f'<text x="{tx:.1f}" y="{TOP + H_rows + 15}" fill="{LATE}" font-size="10" text-anchor="middle">{esc(t["today"])}</text>')

    # Tegnforklaring og kilde
    ly = legend_y
    lx = PAD
    out.append(f'<path d="M{lx},{ly}H{lx + 28}" stroke="{ARROW}" stroke-width="1.5" marker-end="url(#{ma})"/>'
               f'<text x="{lx + 34}" y="{ly + 4}" fill="#24292f">{esc(t["legend_arrow"])}</text>')
    lx += 170
    out.append(f'<path d="M{lx},{ly}H{lx + 28}" stroke="{LATE}" stroke-width="1.5" marker-end="url(#{mr})"/>'
               f'<text x="{lx + 34}" y="{ly + 4}" fill="#24292f">{esc(t["legend_late"])}</text>')
    lx += 330
    out.append(f'<rect x="{lx}" y="{ly - 6}" width="28" height="12" rx="3" fill="#afb8c1" fill-opacity="0.35" stroke="#afb8c1" stroke-dasharray="4 3"/>'
               f'<text x="{lx + 34}" y="{ly + 4}" fill="#24292f">{esc(t["legend_open"])}</text>')
    lx += 190
    out.append(f'<path d="M{lx + 14},{ly - 7}L{lx + 21},{ly}L{lx + 14},{ly + 7}L{lx + 7},{ly}z" fill="#afb8c1"/>'
               f'<text x="{lx + 34}" y="{ly + 4}" fill="#24292f">{esc(t["legend_due"])}</text>')
    foot = esc(t['made'].format(d=today.isoformat()))
    note = (' ' + esc(t['no_dates'].format(n=undated))) if undated else ''
    out.append(f'<text x="{PAD}" y="{ly + 30}" fill="#57606a" font-size="11">{foot} '
               f'<a href="{esc(url)}" target="_blank"><tspan fill="#0969da">{esc(title)}</tspan></a>.{note}</text>')
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
        n = sum(1 for x in tasks if x['start'] or x['due'])
        print(f'Project {number}: {len(tasks)} oppgaver, {n} med datoer, '
              f'{sum(len(x["blocked_by"]) for x in tasks)} avhengigheter')
        for lang in ('nb', 'en'):
            path = f'{base}-{lang}.svg'
            if a.out:
                path = os.path.join(os.path.abspath(a.out), os.path.basename(path))
            write(path, svg(number, title, url, tasks, lang, today))


main()
