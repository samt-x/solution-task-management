"""Øyeblikksbilde av statusen på prosjektbrett (solution-task-management#15).

Feltene i et GitHub Project har ingen historikk: skrives Comment over, er forrige
kommentar borte. Skriptet skriver derfor brettet til en Markdown-fil i dette repoet.
Workflowen committer fila bare når innholdet er endret, så git-historikken til fila
blir statushistorikken. Fila har ingen tidsstempel – commit-datoen er tidspunktet.

Token: miljøvariabelen GH_TOKEN (i Actions: token fra appen SAMT-BU Task sync),
ellers `gh auth token`. Skriptet leser bare brettene og skriver aldri til dem.
"""
import json, os, subprocess, sys, time, urllib.request

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ORG = 'samt-x'
PROJECTS = {5: 'status/project-5.md'}   # brett → fil, sti relativ til reporoten
STATUS_ORDER = ['Proposed', 'Backlog', 'To do', 'Todo', 'Ready', 'In progress', 'In Progress', 'In review', 'Done']
COLUMNS = ['Status', 'Responsible', 'Due date', 'Comment']

TOKEN = os.environ.get('GH_TOKEN') or subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def gql(query, **variables):
    for forsøk in range(4):
        req = urllib.request.Request('https://api.github.com/graphql',
                                     data=json.dumps({'query': query, 'variables': variables}).encode(),
                                     headers={'Authorization': f'bearer {TOKEN}', 'Content-Type': 'application/json'})
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
  items(first:100,after:$after){pageInfo{hasNextPage endCursor} nodes{
    content{... on Issue{number title url repository{name}}}
    fieldValues(first:30){nodes{
      ... on ProjectV2ItemFieldSingleSelectValue{name field{... on ProjectV2FieldCommon{name}}}
      ... on ProjectV2ItemFieldTextValue{text field{... on ProjectV2FieldCommon{name}}}
      ... on ProjectV2ItemFieldDateValue{date field{... on ProjectV2FieldCommon{name}}}}}}}}}}'''


def cell(s):
    return (s or '').replace('|', '\\|').replace('\n', ' ').strip()


def snapshot(number):
    rows, after = [], None
    while True:
        p = gql(ITEMS, n=number, after=after)['organization']['projectV2']
        for it in p['items']['nodes']:
            c = it['content']
            if not c:  # utkast og pull requests tas ikke med
                continue
            v = {f['field']['name']: f.get('name') or f.get('text') or f.get('date')
                 for f in it['fieldValues']['nodes'] if f and f.get('field')}
            if v.get('Title') == c['title']:
                v.pop('Title')
            rows.append((c, v))
        if not p['items']['pageInfo']['hasNextPage']:
            break
        after = p['items']['pageInfo']['endCursor']

    def key(r):
        s = r[1].get('Status')
        return (STATUS_ORDER.index(s) if s in STATUS_ORDER else len(STATUS_ORDER), r[0]['repository']['name'], r[0]['number'])

    lines = [f'# Status: {p["title"]}', '',
             f'Øyeblikksbilde av [Project {number}]({p["url"]}), skrevet automatisk av '
             '`.github/scripts/snapshot-status.py`. Ikke rediger fila – endre brettet. '
             'Tidligere status finnes i git-historikken til fila.', '',
             '| Oppgave | ' + ' | '.join(COLUMNS) + ' |', '|---' * (len(COLUMNS) + 1) + '|']
    for c, v in sorted(rows, key=key):
        task = f'[{c["repository"]["name"]}#{c["number"]}]({c["url"]}) {cell(c["title"])}'
        lines.append('| ' + ' | '.join([task] + [cell(v.get(col)) for col in COLUMNS]) + ' |')
    return '\n'.join(lines) + '\n', len(rows)


for number, path in PROJECTS.items():
    text, n = snapshot(number)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    old = open(full, encoding='utf-8').read() if os.path.exists(full) else None
    if old == text:
        print(f'Project {number}: uendret ({n} oppgaver)')
    else:
        with open(full, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        print(f'Project {number}: skrev {path} ({n} oppgaver)')
