"""Melder en feilet planlagt workflow som issue, og lukker det når workflowen virker igjen (solution-task-management#32).

Kalles som siste steg i workflowene med tidsplan:
  workflow-alert.py fail <navn> <hva som ikke oppdateres>   når et steg feilet
  workflow-alert.py ok <navn>                                når alt gikk bra
Ett åpent issue per workflow, med tittelen «Workflow failed: <navn>». Feiler den igjen, kommer det
en kommentar på det samme issuet, ikke et nytt. Issuet får typen Problem og havner på Project 18 med Auto-add.

Token: GH_TOKEN (i Actions: GITHUB_TOKEN med issues: write). RUN_URL er lenken til kjøringen.
"""
import json, os, subprocess, sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
mode, name = sys.argv[1], sys.argv[2]
what = sys.argv[3] if len(sys.argv) > 3 else 'resultatet'
REPO = os.environ.get('GITHUB_REPOSITORY', 'samt-x/solution-task-management')
RUN = os.environ.get('RUN_URL', '(ukjent kjøring)')
TITLE = f'Workflow failed: {name}'
DOC = ('https://docs.samt-bu.no/prosjektleveranser/loesninger/samhandlingsplattform/oppgavestyring/'
       'teknisk-dokumentasjon/#planlagte-kjøringer')


def gh(*args, check=True):
    r = subprocess.run(['gh', *args], capture_output=True, text=True, encoding='utf-8')
    if check and r.returncode:
        raise SystemExit(f'gh {" ".join(args[:3])}: {r.stderr}')
    return r.stdout.strip()


found = [i['number'] for i in json.loads(gh('issue', 'list', '-R', REPO, '--state', 'open', '--limit', '100',
                                            '--json', 'number,title')) if i['title'] == TITLE]

if mode == 'ok':
    for n in found:
        gh('issue', 'close', str(n), '-R', REPO, '--reason', 'completed', '--comment',
           f'Virker igjen: {RUN}\n\nLukket automatisk av workflowen.\n\n'
           'Dokumentasjon: ikke berørt, fordi issuet bare meldte en feilet kjøring.')
        print(f'Lukket #{n}')
    sys.exit(0)

if found:
    gh('issue', 'comment', str(found[0]), '-R', REPO, '--body', f'Feilet igjen: {RUN}')
    print(f'Kommenterte #{found[0]}')
    sys.exit(0)

body = f'''### Hva er problemet?

Den planlagte workflowen **{name}** feilet. Kjøringen: {RUN}

Issuet er laget automatisk av workflowen.

### Hva slags problem?

Programvare eller verktøy virker ikke

### Hvorfor er det et problem? Hva får det å si?

Til feilen er rettet, oppdateres ikke {what}. Det forrige resultatet blir stående.

### Slik ser du problemet

Åpne kjøringen over og se hvilket steg som feilet, og feilmeldingen i loggen.

### Forslag til løsning

Rett feilen i skriptet eller workflowen, eller vent hvis feilen var forbigående hos GitHub. Feiler den igjen, kommer det en kommentar her. Issuet lukkes automatisk ved neste vellykkede kjøring.

### Gjelder

{DOC}
'''
url = gh('issue', 'create', '-R', REPO, '--title', TITLE, '--body', body)
n = url.rsplit('/', 1)[1]
gh('api', '-X', 'PATCH', f'repos/{REPO}/issues/{n}', '-f', 'type=Problem', check=False)
print(f'Laget {url}')
