#!/usr/bin/env python3
"""Skriver .github/CODEOWNERS i alle repoene i samt-x fra tabellen i Konvensjoner.

Kilden er tabellen under «Hvem behandler pull requests» i
content/konvensjoner/_index.nb.md i solution-task-management. Første kolonne har ett
eller flere repoer i `kodeformat`, andre kolonne eieren: et teamnavn (`samt-bu-editorial`)
eller en person med @ foran (`@erikhag1git`).

Uten argument vises hva som ville blitt endret, og ingenting skrives. Skriptet sjekker også
- at alle repoene i orgen (unntatt arkiverte) står i tabellen, og at tabellen ikke har ukjente repoer
- at eierteamet har Write (eller mer) på repoet. Ellers ignorerer GitHub linja uten feilmelding.

  python codeowners.py            # vis avvik og hva som ville blitt skrevet
  python codeowners.py --apply    # skriv filene som er ulike (commit med [skip ci])

Laget 2026-11-15 (s119, solution-task-management#46). Krever gh med Contents write på repoene.
"""
import json
import os
import re
import subprocess
import sys

ORG = "samt-x"
HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "..", "..", "content", "konvensjoner", "_index.nb.md")
HEADING = "## Hvem behandler pull requests"
PATH = ".github/CODEOWNERS"
WRITE_ROLES = {"write", "maintain", "admin"}


def gh(*args, check=True):
    r = subprocess.run(["gh", "api", *args], capture_output=True, text=True, encoding="utf-8")
    if check and r.returncode != 0:
        raise RuntimeError(f"gh api {' '.join(args)}: {r.stderr.strip()}")
    return r


def read_table():
    text = open(SOURCE, encoding="utf-8").read()
    if HEADING not in text:
        sys.exit(f"Fant ikke «{HEADING}» i {SOURCE}")
    section = text.split(HEADING, 1)[1].split("\n## ", 1)[0]
    owners = {}
    for line in section.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 2:
            continue
        repos = re.findall(r"`([^`]+)`", cols[0])
        owner = re.findall(r"`([^`]+)`", cols[1])
        if not repos or not owner:
            continue  # overskriftsraden
        for repo in repos:
            if repo in owners:
                sys.exit(f"{repo} står to ganger i tabellen")
            owners[repo] = owner[0]
    return owners


def org_repos():
    r = gh(f"orgs/{ORG}/repos", "--paginate", "--jq", ".[] | select(.archived|not) | .name")
    return set(r.stdout.split())


def owner_ref(owner):
    return owner if owner.startswith("@") else f"@{ORG}/{owner}"


def has_write(owner, repo):
    if owner.startswith("@"):
        r = gh(f"repos/{ORG}/{repo}/collaborators/{owner[1:]}/permission", "--jq", ".role_name", check=False)
    else:
        r = gh(f"orgs/{ORG}/teams/{owner}/repos/{ORG}/{repo}",
               "-H", "Accept: application/vnd.github.v3.repository+json", "--jq", ".role_name", check=False)
    return r.returncode == 0 and r.stdout.strip() in WRITE_ROLES


def content(owner):
    return (
        "# Generert fra tabellen «Hvem behandler pull requests» i Konvensjoner\n"
        "# (samt-x/solution-task-management, content/konvensjoner/). Endre tabellen der, ikke her,\n"
        "# og kjør .github/scripts/codeowners.py --apply.\n"
        f"* {owner_ref(owner)}\n"
    )


def current(repo):
    r = gh(f"repos/{ORG}/{repo}/contents/{PATH}", check=False)
    if r.returncode != 0:
        return None, None
    data = json.loads(r.stdout)
    import base64
    return base64.b64decode(data["content"]).decode("utf-8"), data["sha"]


def write(repo, body, sha):
    import base64
    payload = {
        "message": "CODEOWNERS fra Konvensjoner (solution-task-management#46) [skip ci]",
        "content": base64.b64encode(body.encode("utf-8")).decode("ascii"),
    }
    if sha:
        payload["sha"] = sha
    r = subprocess.run(["gh", "api", "-X", "PUT", f"repos/{ORG}/{repo}/contents/{PATH}", "--input", "-"],
                       input=json.dumps(payload), capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError(f"{repo}: {r.stderr.strip()}")


def main():
    apply = "--apply" in sys.argv
    owners = read_table()
    repos = org_repos()
    problems = 0
    for repo in sorted(repos - owners.keys()):
        print(f"MANGLER I TABELLEN: {repo}")
        problems += 1
    for repo in sorted(owners.keys() - repos):
        print(f"UKJENT REPO I TABELLEN: {repo}")
        problems += 1
    changed = 0
    for repo in sorted(owners.keys() & repos):
        owner = owners[repo]
        if not has_write(owner, repo):
            print(f"IKKE WRITE: {owner} på {repo} (linja ville blitt ignorert, hopper over)")
            problems += 1
            continue
        body = content(owner)
        old, sha = current(repo)
        if old == body:
            continue
        changed += 1
        print(f"{'skriver' if apply else 'ville skrevet'}: {repo} -> {owner_ref(owner)}"
              f"{'' if old is None else ' (erstatter eksisterende fil)'}")
        if apply:
            write(repo, body, sha)
    print(f"{len(owners)} repoer i tabellen, {changed} {'endret' if apply else 'å endre'}, {problems} avvik")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
