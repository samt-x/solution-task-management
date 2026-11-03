"""Bidragsytere utenfor orgen (solution-task-management#49).

Finner kontoer som har laget en PR, et issue, en kommentar eller en review i et offentlig samt-x-repo,
uten å være medlem av orgen eller ha tilgang til repoet. Uten --update skrives bare lista ut (ved
«Start sesjon», via outside-contributors.sh i workspace-roten). Med --update holdes et fast issue
«Bidragsytere utenfor orgen (N)» i solution-task-management oppdatert (kjøres hver time av Sync All tasks).

Avkryssede kontoer i issuet er vurdert og blir stående som vurdert, så de ikke dukker opp igjen.
Kontoer som blir medlemmer, forsvinner fra lista. Ny konto til vurdering gir en kommentar, som varsler
dem som følger issuet. Issuet har bare login og lenker til bidragene, som alt er offentlige.
Personopplysninger hører hjemme i medlemslista i samt-bu-intern-admin (privat).

Token: GH_TOKEN til lesing (i Actions: token fra appen SAMT-BU Task sync, som ser private medlemskap),
GH_WRITE_TOKEN til issuet (i Actions: GITHUB_TOKEN). Lokalt brukes `gh auth token` til begge.
"""
import json, os, re, subprocess, sys, time, urllib.request

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ORG = 'samt-x'
REPO = 'samt-x/solution-task-management'
TITLE = 'Bidragsytere utenfor orgen'
IGNORE = {'githagen', 'erikhag1test'}     # Eriks testkontoer (se Testkontoer i workspace-minnet)
INSIDE = {'OWNER', 'MEMBER', 'COLLABORATOR'}
UPDATE = '--update' in sys.argv
DOC = ('https://docs.samt-bu.no/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/'
       'teknisk-dokumentasjon/#planlagte-kjøringer')

TOKEN = os.environ.get('GH_TOKEN') or subprocess.run(['gh', 'auth', 'token'], capture_output=True, text=True).stdout.strip()
WRITE_TOKEN = os.environ.get('GH_WRITE_TOKEN') or TOKEN


def gql(query, allow_errors=False, **variables):
    for forsøk in range(4):
        req = urllib.request.Request('https://api.github.com/graphql',
                                     data=json.dumps({'query': query, 'variables': variables}).encode(),
                                     headers={'Authorization': f'bearer {TOKEN}', 'Content-Type': 'application/json'})
        try:
            d = json.load(urllib.request.urlopen(req, timeout=60))
        except Exception as e:  # nettverk eller sekundær ratebegrensning
            print('  nytt forsøk etter feil:', e); time.sleep(10 * (forsøk + 1)); continue
        if d.get('errors'):
            if allow_errors:
                return None
            if 'Something went wrong' in str(d['errors']) and forsøk < 3:  # forbigående feil hos GitHub
                print('  forbigående feil, prøver igjen'); time.sleep(5 * (forsøk + 1)); continue
            raise SystemExit(f'GraphQL-feil: {d["errors"]}')
        return d['data']
    raise SystemExit('Ga opp etter fire forsøk')


def pages(query, path, allow_errors=False, **v):
    """Henter alle sider for en connection; path peker på connection-objektet."""
    after = None
    while True:
        d = gql(query, allow_errors=allow_errors, after=after, **v)
        if d is None:
            return
        c = d
        for k in path:
            c = c[k]
        yield from c['nodes']
        if not c['pageInfo']['hasNextPage']:
            return
        after = c['pageInfo']['endCursor']


def gh(*args, check=True):
    env = dict(os.environ, GH_TOKEN=WRITE_TOKEN)
    r = subprocess.run(['gh', *args], capture_output=True, text=True, encoding='utf-8', env=env)
    if check and r.returncode:
        raise SystemExit(f'gh {" ".join(args[:3])}: {r.stderr}')
    return r.stdout.strip()


# 1. Medlemmer, også private medlemskap når tokenen kan se dem (ellers holder authorAssociation)
members = {m['login'] for m in pages('''query($after:String){organization(login:"samt-x"){membersWithRole(first:100,after:$after){
    pageInfo{hasNextPage endCursor} nodes{login}}}}''', ['organization', 'membersWithRole'], allow_errors=True)}
print(f'{len(members)} medlemmer synlige for tokenen')
# Uten lesetilgang til medlemmene skjuler GitHub private medlemskap også i authorAssociation,
# så alle med privat medlemskap ville sett ut som om de var utenfor orgen. Appen trenger Members: read.
if not members:
    print('::warning::Tokenen ser ingen medlemmer i orgen (mangler Members: read). Issuet oppdateres ikke.')
    sys.exit(0)

# 2. Offentlige repoer
repos = [r['name'] for r in pages('''query($after:String){organization(login:"samt-x"){repositories(first:100,after:$after){
    pageInfo{hasNextPage endCursor} nodes{name isPrivate}}}}''', ['organization', 'repositories']) if not r['isPrivate']]

# 3. Bidrag: issues, PR-er, kommentarer og reviews
A = 'author{login __typename} authorAssociation createdAt url'
found = {}   # login -> {'first': (dato, url, art, ref), 'count': n}


def note(node, art, ref):
    a = node.get('author')
    if not a or a['__typename'] == 'Bot' or node['authorAssociation'] in INSIDE:
        return
    login = a['login']
    if login in members or login in IGNORE:
        return
    f = found.setdefault(login, {'first': None, 'count': 0})
    f['count'] += 1
    first = (node['createdAt'][:10], node['url'], art, ref)
    if f['first'] is None or first < f['first']:
        f['first'] = first


for r in repos:
    for i in pages('''query($after:String,$r:String!){repository(owner:"samt-x",name:$r){issues(first:50,after:$after){
        pageInfo{hasNextPage endCursor} nodes{number ''' + A + ''' comments(first:100){nodes{''' + A + '''}}}}}}''',
                   ['repository', 'issues'], r=r):
        ref = f'{r}#{i["number"]}'
        note(i, 'issue', ref)
        for c in i['comments']['nodes']:
            note(c, 'kommentar', ref)
    for p in pages('''query($after:String,$r:String!){repository(owner:"samt-x",name:$r){pullRequests(first:50,after:$after){
        pageInfo{hasNextPage endCursor} nodes{number ''' + A + ''' comments(first:100){nodes{''' + A + '''}}
        reviews(first:50){nodes{''' + A + '''}}}}}}''', ['repository', 'pullRequests'], r=r):
        ref = f'{r}#{p["number"]}'
        note(p, 'PR', ref)
        for c in p['comments']['nodes']:
            note(c, 'kommentar', ref)
        for c in p['reviews']['nodes']:
            note(c, 'review', ref)
print(f'{len(repos)} offentlige repoer, {len(found)} kontoer utenfor orgen')


def line(login, checked):
    f = found[login]
    dato, url, art, ref = f['first']
    return (f'- [{"x" if checked else " "}] `{login}` · [profil](https://github.com/{login}) · '
            f'første: [{ref}]({url}) ({art}, {dato}) · {f["count"]} bidrag i alt')


# 4. Les avkrysningene i det faste issuet
issue = None
for i in json.loads(gh('issue', 'list', '-R', REPO, '--state', 'open', '--limit', '200', '--json', 'number,title,body')):
    if i['title'].startswith(TITLE + ' ('):
        issue = i
        break
old_body = (issue or {}).get('body') or ''
vurdert = set(re.findall(r'^- \[[xX]\] `([^`]+)`', old_body, re.M))
kjent = set(re.findall(r'^- \[[ xX]\] `([^`]+)`', old_body, re.M))

ny = sorted((l for l in found if l not in vurdert), key=lambda l: found[l]['first'])
ferdig = sorted((l for l in found if l in vurdert), key=str.lower)

print(f'Til vurdering ({len(ny)}):')
for l in ny:
    print(' ', line(l, False)[6:])
if ferdig:
    print(f'Vurdert ({len(ferdig)}): {", ".join(ferdig)}')

if not UPDATE:
    sys.exit(0)

# 5. Oppdater issuet bare når lista er endret
body = f'''### Hva skal gjøres?

Kontoer utenfor orgen som har bidratt i et offentlig repo i samt-x (PR, issue, kommentar eller review). Lista oppdateres hver time av workflowen Sync All tasks. Arbeidsflyten er beskrevet i samt-x/solution-task-management#49.

Kryss av når kontoen er vurdert: ført inn i medlemslista (privat, kjerneteamet) og avgjort om den skal inviteres, og til hvilket team. Avkryssede blir stående, så de ikke dukker opp igjen. Kontoer som blir medlemmer av orgen, forsvinner fra lista.

**Til vurdering ({len(ny)})**

{chr(10).join(line(l, False) for l in ny) or 'Ingen.'}

**Vurdert ({len(ferdig)})**

{chr(10).join(line(l, True) for l in ferdig) or 'Ingen.'}

### Ferdig når

Issuet står åpent og oppdateres løpende.

### Gjelder

{DOC}

### Forslag til hvem som bør se på dette

@erikhag1git
'''
title = f'{TITLE} ({len(ny)})'
if issue is None:
    url = gh('issue', 'create', '-R', REPO, '--title', title, '--body', body)
    n = url.rsplit('/', 1)[1]
    gh('api', '-X', 'PATCH', f'repos/{REPO}/issues/{n}', '-f', 'type=Task', check=False)
    print(f'Laget {url}')
elif old_body.replace('\r', '').strip() != body.strip() or issue['title'] != title:
    n = str(issue['number'])
    gh('issue', 'edit', n, '-R', REPO, '--title', title, '--body', body)
    print(f'Oppdaterte #{n}')
else:
    n = str(issue['number'])
    print(f'#{n} er uendret')

# 6. Kommentar for nye kontoer, så de som følger issuet, får varsel
nye = [l for l in ny if l not in kjent]
if issue is not None and nye:
    gh('issue', 'comment', n, '-R', REPO, '--body',
       'Ny til vurdering:\n\n' + '\n'.join(line(l, False)[6:] for l in nye))
    print(f'Kommenterte #{n}: {", ".join(nye)}')
