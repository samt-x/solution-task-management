"""Flytter datoene på eksempelbrettet slik at eksemplene ligger rundt dagens dato (solution-task-management#40).

Eksemplene i solution-task-management-examples brukes i dokumentasjonen, blant annet i tidslinjen.
Med faste datoer ville dagens dato vandre forbi dem. example-dates.json gir start og frist per
issue i dager fra mandag denne uka, så stolpene står på samme ukedager uke etter uke, og datoene
endres bare én gang i uka. Lørdag og søndag regnes til neste uke, ellers ville pågående eksempler
ha passert fristen i helgen. Skriptet skriver Start date og Due date på brettet, så GitHub er
fortsatt master og brettet viser det samme som figuren. Bare felt som avviker, skrives.

Token: miljøvariabelen GH_TOKEN (i Actions: token fra appen SAMT-BU Task sync),
ellers `gh auth token`. Kjør med --dry-run for å se hva som ville blitt endret.
"""
import datetime, json, os, subprocess, sys, time, urllib.request

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'example-dates.json')
FIELDS = ('Start date', 'Due date')
DRY = '--dry-run' in sys.argv

TOKEN = os.environ.get('GH_TOKEN') or subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()


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


cfg = json.load(open(CONFIG, encoding='utf-8'))
today = datetime.date.today()
week = today + datetime.timedelta(days=2)   # lørdag og søndag hører til neste uke
monday = week - datetime.timedelta(days=week.weekday())

p = gql('''query($n:Int!){organization(login:"samt-x"){projectV2(number:$n){id title
    fields(first:50){nodes{... on ProjectV2FieldCommon{id name}}}
    items(first:100){nodes{id content{... on Issue{number repository{name}}}
      fieldValues(first:30){nodes{... on ProjectV2ItemFieldDateValue{date field{... on ProjectV2FieldCommon{name}}}}}}}}}}''',
        n=cfg['project'])['organization']['projectV2']
field = {f['name']: f['id'] for f in p['fields']['nodes'] if f and f.get('name') in FIELDS}
print(f'{p["title"]}: mandag denne uka er {monday}')

changed = 0
for it in p['items']['nodes']:
    c = it['content'] or {}
    plan = cfg['issues'].get(str(c.get('number')))
    if not plan or c['repository']['name'] != cfg['repo']:
        continue
    now = {v['field']['name']: v['date'] for v in it['fieldValues']['nodes'] if v and v.get('field')}
    for name, offset in zip(FIELDS, plan):
        want = (monday + datetime.timedelta(days=offset)).isoformat() if offset is not None else None
        if now.get(name) == want:
            continue
        print(f'  #{c["number"]} {name}: {now.get(name)} → {want}')
        changed += 1
        if DRY:
            continue
        if want:
            gql('''mutation($p:ID!,$i:ID!,$f:ID!,$d:Date!){updateProjectV2ItemFieldValue(input:{projectId:$p,itemId:$i,
                fieldId:$f,value:{date:$d}}){clientMutationId}}''', p=p['id'], i=it['id'], f=field[name], d=want)
        else:
            gql('''mutation($p:ID!,$i:ID!,$f:ID!){clearProjectV2ItemFieldValue(input:{projectId:$p,itemId:$i,
                fieldId:$f}){clientMutationId}}''', p=p['id'], i=it['id'], f=field[name])
print(f'{changed} datoer {"ville blitt endret" if DRY else "endret"}')
