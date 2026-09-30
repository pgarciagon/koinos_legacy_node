#!/usr/bin/env python3
"""Collect public upstream source and release metadata without starting containers."""
import concurrent.futures
import datetime
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
UPSTREAM = ROOT / 'upstream'
EVIDENCE = ROOT / 'docs/inventory/evidence'


def run(*args, cwd=None):
    p = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.returncode:
        raise RuntimeError(p.stderr.strip())
    return p.stdout


def api(path):
    return json.loads(run('gh', 'api', path))


def collect(name, version):
    repo = 'koinos/' + name
    dest = UPSTREAM / name
    if not dest.exists():
        run('git', 'clone', '--depth', '1', 'https://github.com/' + repo + '.git', str(dest))
    # Refresh only a clean source reference checkout; never reset local changes.
    if run('git', 'status', '--porcelain', cwd=dest).strip():
        raise RuntimeError('Reference checkout has local changes: ' + str(dest))
    meta = api('repos/' + repo)
    run('git', 'fetch', '--depth', '1', 'origin', meta['default_branch'], cwd=dest)
    head = run('git', 'rev-parse', 'FETCH_HEAD', cwd=dest).strip()
    run('git', 'checkout', '--detach', head, cwd=dest)
    pinned = None
    if version:
        run('git', 'fetch', '--depth', '1', 'origin', 'refs/tags/' + version + ':refs/tags/' + version, cwd=dest)
        pinned = run('git', 'rev-parse', version + '^{commit}', cwd=dest).strip()
    releases = api('repos/' + repo + '/releases?per_page=10')
    tags = api('repos/' + repo + '/tags?per_page=15')
    issues = api('repos/' + repo + '/issues?state=open&per_page=100')
    return {
        'repository': repo, 'url': meta['html_url'], 'default_branch': meta['default_branch'],
        'head': head, 'head_date': run('git', 'show', '-s', '--format=%cI', head, cwd=dest).strip(),
        'archived': meta['archived'], 'pushed_at': meta['pushed_at'],
        'selected_tag': version, 'selected_commit': pinned,
        'releases': [{k: r.get(k) for k in ('tag_name', 'published_at', 'prerelease', 'draft', 'html_url')} for r in releases],
        'tags': [{'name': t['name'], 'commit': t['commit']['sha']} for t in tags],
        'open_items': [{'number': i['number'], 'title': i['title'], 'url': i['html_url'], 'is_pr': 'pull_request' in i} for i in issues],
    }


def main():
    UPSTREAM.mkdir(exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    # Refresh the integrator first so service tags come from the same snapshot.
    integrator = collect('koinos', None)
    versions = {}
    for line in (UPSTREAM / 'koinos/env.example').read_text().splitlines():
        if '_TAG=' in line and not line.startswith('#'):
            key, value = line.split('=', 1)
            versions['koinos-' + key[:-4].lower().replace('_', '-')] = value
    records, errors = [integrator], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(collect, name, tag): name for name, tag in versions.items()}
        for f in concurrent.futures.as_completed(futures):
            name = futures[f]
            try:
                record = f.result()
                records.append(record)
                print(name + ': ' + record['head'][:12], flush=True)
            except Exception as e:
                errors.append({'repository': name, 'error': str(e)})
                print(name + ': ERROR ' + str(e), flush=True)
    result = {'collected_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'scope': 'Public upstream source; no running-node inspection',
              'repositories': sorted(records, key=lambda r: r['repository']), 'errors': errors}
    (EVIDENCE / 'upstream-metadata.json').write_text(json.dumps(result, indent=2) + '\n')
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
