"""Synk til samlebrettet «SAMT-BU Overview – All tasks» (A2, solution-task-management#8).

Kopierer alle issues i de offentlige samt-x-repoene til samlebrettet, i én retning.
Porteføljerepoet (EXCLUDE) er ikke med, fordi kortene der ikke er oppgaver.
Status oversettes til det felles nivået; Responsible, Priority og datoene kopieres
fra prosjektbrettet issuet ligger på. Skriptet skriver aldri til prosjektbrettene.

Token: miljøvariabelen GH_TOKEN (i Actions: token fra appen SAMT-BU Task sync),
ellers `gh auth token`. Kjør med --dry-run for å se hva som ville blitt endret.
"""
import json, os, subprocess, sys, time, urllib.request

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ORG = 'samt-x'
TARGET = 12                      # SAMT-BU Overview – All tasks
EXCLUDE = {'samt-bu-portfolio'}   # porteføljekort, ikke oppgaver
DRY = '--dry-run' in sys.argv
SHARED = {'Proposed': 'Not started', 'Backlog': 'Not started', 'Todo': 'Not started', 'To do': 'Not started',
          'Ready': 'Not started', 'In progress': 'In progress', 'In Progress': 'In progress',
          'In review': 'In progress', 'Done': 'Done'}
COPY_SELECT = ['Responsible', 'Priority']
COPY_DATE = ['Start date', 'Due date']

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


def pages(query, path, **v):
    """Henter alle sider for en connection; path peker på connection-objektet."""
    after = None
    while True:
        d = gql(query, after=after, **v)
        c = d
        for k in path:
            c = c[k]
        yield from c['nodes']
        if not c['pageInfo']['hasNextPage']:
            return
        after = c['pageInfo']['endCursor']


# 1. Offentlige repoer med issues
repos = [r for r in pages('''query($after:String){organization(login:"samt-x"){repositories(first:100,after:$after){
    pageInfo{hasNextPage endCursor} nodes{name isPrivate isArchived hasIssuesEnabled}}}}''', ['organization', 'repositories'])
         if not r['isPrivate'] and not r['isArchived'] and r['hasIssuesEnabled'] and r['name'] not in EXCLUDE]
print(f'{len(repos)} offentlige repoer')

# 2. Alle issues i dem
issues = {}
for r in repos:
    for i in pages('''query($after:String,$r:String!){repository(owner:"samt-x",name:$r){issues(first:100,after:$after){
        pageInfo{hasNextPage endCursor} nodes{id number state}}}}''', ['repository', 'issues'], r=r['name']):
        issues[i['id']] = {'repo': r['name'], 'number': i['number'], 'closed': i['state'] == 'CLOSED'}
print(f'{len(issues)} issues')

# 3. Prosjektbrettene (kilder): alle unntatt maler og samlebrettet
FV = '''fieldValues(first:30){nodes{
  ... on ProjectV2ItemFieldSingleSelectValue{name field{... on ProjectV2FieldCommon{name}}}
  ... on ProjectV2ItemFieldDateValue{date field{... on ProjectV2FieldCommon{name}}}}}'''
boards = [p for p in pages('''query($after:String){organization(login:"samt-x"){projectsV2(first:50,after:$after){
    pageInfo{hasNextPage endCursor} nodes{id number title template closed}}}}''', ['organization', 'projectsV2'])
          if not p['template'] and not p['closed'] and p['number'] != TARGET]
source = {}
for b in boards:
    kort = b['title'].removeprefix('SAMT-BU ').split(' – ')[0]
    for it in pages('''query($after:String,$id:ID!){node(id:$id){... on ProjectV2{items(first:100,after:$after){
        pageInfo{hasNextPage endCursor} nodes{content{... on Issue{id}} ''' + FV + '''}}}}}''', ['node', 'items'], id=b['id']):
        cid = (it['content'] or {}).get('id')
        if not cid or cid not in issues:
            continue
        vals = {v['field']['name']: v.get('name') or v.get('date') for v in it['fieldValues']['nodes'] if v and v.get('field')}
        if cid not in source or (not source[cid]['vals'].get('Status') and vals.get('Status')):
            source[cid] = {'board': kort, 'vals': vals}
print(f'{len(boards)} kildebrett, {len(source)} issues ligger på et brett')

# 4. Samlebrettet: felt, valg og eksisterende elementer
T = gql('''query{organization(login:"samt-x"){projectV2(number:%d){id
  fields(first:40){nodes{... on ProjectV2FieldCommon{id name} ... on ProjectV2SingleSelectField{options{id name color description}}}}}}}''' % TARGET)['organization']['projectV2']
PID = T['id']
F = {f['name']: f for f in T['fields']['nodes'] if f}
existing = {}
for it in pages('''query($after:String,$id:ID!){node(id:$id){... on ProjectV2{items(first:100,after:$after){
    pageInfo{hasNextPage endCursor} nodes{id content{... on Issue{id}} ''' + FV.replace('fieldValues(first:30){nodes{', 'fieldValues(first:30){nodes{ ... on ProjectV2ItemFieldTextValue{text field{... on ProjectV2FieldCommon{name}}}') + '''}}}}}''',
                ['node', 'items'], id=PID):
    cid = (it['content'] or {}).get('id')
    vals = {v['field']['name']: v.get('name') or v.get('date') or v.get('text') for v in it['fieldValues']['nodes'] if v and v.get('field')}
    existing[cid] = {'item': it['id'], 'vals': vals}

# 5. Ønsket tilstand per issue
want = {}
for cid, i in issues.items():
    s = source.get(cid)
    sv = s['vals'] if s else {}
    st = 'Done' if i['closed'] else SHARED.get(sv.get('Status'), 'Not started')
    w = {'Status': st, 'Source status': f"{s['board']}: {sv.get('Status') or '–'}" if s else f"{i['repo']} (no board)"}
    for f in COPY_SELECT + COPY_DATE:
        w[f] = sv.get(f)
    want[cid] = w

# 6. Manglende valg i Responsible og Priority legges til (eksisterende valg beholdes med id)
for f in COPY_SELECT:
    have = {o['name'] for o in F[f]['options']}
    new = sorted({w[f] for w in want.values() if w[f]} - have, key=str.lower)
    if new:
        print(f'  nye valg i {f}: {", ".join(new)}')
        if not DRY:
            opts = [{k: o[k] for k in ('id', 'name', 'color', 'description')} for o in F[f]['options']]
            opts += [{'name': n, 'color': 'GRAY', 'description': ''} for n in new]
            gql('mutation($f:ID!,$o:[ProjectV2SingleSelectFieldOptionInput!]){updateProjectV2Field(input:{fieldId:$f,singleSelectOptions:$o}){clientMutationId}}',
                f=F[f]['id'], o=opts)
if not DRY:
    T = gql('''query{organization(login:"samt-x"){projectV2(number:%d){fields(first:40){nodes{... on ProjectV2FieldCommon{id name} ... on ProjectV2SingleSelectField{options{id name}}}}}}}''' % TARGET)['organization']['projectV2']
    F = {f['name']: f for f in T['fields']['nodes'] if f}
OPT = {f: {o['name']: o['id'] for o in F[f].get('options', [])} for f in ['Status'] + COPY_SELECT}

# 7. Legg til nye elementer
added = [cid for cid in want if cid not in existing]
print(f'  legges til: {len(added)}')
for k in range(0, len(added), 5):
    chunk = added[k:k + 5]
    if DRY:
        continue
    m = ' '.join(f'a{n}:addProjectV2ItemById(input:{{projectId:"{PID}",contentId:"{cid}"}}){{item{{id}}}}' for n, cid in enumerate(chunk))
    d = gql('mutation{' + m + '}')
    for n, cid in enumerate(chunk):
        existing[cid] = {'item': d[f'a{n}']['item']['id'], 'vals': {}}

# 8. Oppdater felt som avviker (samlet i puljer)
ops = []
for cid, w in want.items():
    if cid not in existing:
        continue
    cur = existing[cid]['vals']
    for f, val in w.items():
        if (cur.get(f) or None) == (val or None):
            continue
        fid = F[f]['id']
        if not val:
            ops.append(f'clearProjectV2ItemFieldValue(input:{{projectId:"{PID}",itemId:"{existing[cid]["item"]}",fieldId:"{fid}"}}){{clientMutationId}}')
            continue
        if f in OPT:
            value = f'{{singleSelectOptionId:"{OPT[f][val]}"}}'
        elif f in COPY_DATE:
            value = f'{{date:"{val}"}}'
        else:
            value = '{text:%s}' % json.dumps(val, ensure_ascii=False)
        ops.append(f'updateProjectV2ItemFieldValue(input:{{projectId:"{PID}",itemId:"{existing[cid]["item"]}",fieldId:"{fid}",value:{value}}}){{clientMutationId}}')
print(f'  feltoppdateringer: {len(ops)}')
if not DRY:
    for k in range(0, len(ops), 10):
        gql('mutation{' + ' '.join(f'u{n}:{op}' for n, op in enumerate(ops[k:k + 10])) + '}')

# 9. Fjern elementer som ikke lenger hører hjemme (issue flyttet til privat repo, slettet, eller utkast)
gone = [e['item'] for cid, e in existing.items() if cid not in want]
print(f'  fjernes: {len(gone)}')
if not DRY:
    for k in range(0, len(gone), 25):
        gql('mutation{' + ' '.join(f'd{n}:deleteProjectV2Item(input:{{projectId:"{PID}",itemId:"{i}"}}){{deletedItemId}}'
                                   for n, i in enumerate(gone[k:k + 25])) + '}')
print('ferdig' + (' (dry run – ingenting endret)' if DRY else ''))
