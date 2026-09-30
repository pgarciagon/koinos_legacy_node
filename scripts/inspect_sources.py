#!/usr/bin/env python3
"""Save dependency manifests from the selected deployment tags and upstream heads."""
import json
import pathlib
import subprocess
ROOT = pathlib.Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'docs/inventory/evidence'
metadata = json.loads((EVIDENCE / 'upstream-metadata.json').read_text())
records = []
for repo in metadata['repositories']:
    path = ROOT / 'upstream' / repo['repository'].split('/')[1]
    refs = {'head': repo['head']}
    if repo['selected_commit']:
        refs['selected'] = repo['selected_commit']
    sources = {}
    for label, ref in refs.items():
        files = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', ref], cwd=path, text=True).splitlines()
        wanted = [f for f in files if f in ('Dockerfile', 'CMakeLists.txt', 'go.mod', 'go.sum', 'package.json', 'yarn.lock', '.gitmodules', '.circleci/config.yml') or f.endswith('KoinosPackages.cmake')]
        manifests = {f: subprocess.check_output(['git', 'show', ref + ':' + f], cwd=path, text=True) for f in wanted}
        modules = [line for line in subprocess.check_output(['git', 'ls-tree', '-r', ref], cwd=path, text=True).splitlines() if line.startswith('160000')]
        sources[label] = {'commit': ref, 'files': manifests, 'submodules': modules}
    records.append({'repository': repo['repository'], 'sources': sources})
(EVIDENCE / 'source-manifests.json').write_text(json.dumps(records, indent=2) + '\n')
for repo in records:
    s = repo['sources'].get('selected', repo['sources']['head'])
    print('\n' + repo['repository'])
    for name, body in s['files'].items():
        if name == '.circleci/config.yml':
            print(name + ': ' + str(len(body.splitlines())) + ' lines')
        elif name == 'go.mod':
            print(name + ':\n' + '\n'.join(l for l in body.splitlines() if '// indirect' not in l))
        elif name not in ('go.sum', 'yarn.lock'):
            print(name + ':\n' + body)
    print('submodules:', s['submodules'])
