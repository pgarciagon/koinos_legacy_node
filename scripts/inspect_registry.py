#!/usr/bin/env python3
"""Inspect anonymous Docker Hub manifests/configs; never pull image layers."""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import urllib.parse
import urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / 'docs/inventory/evidence'
ACCEPT = ', '.join(['application/vnd.oci.image.index.v1+json', 'application/vnd.docker.distribution.manifest.list.v2+json', 'application/vnd.oci.image.manifest.v1+json', 'application/vnd.docker.distribution.manifest.v2+json'])


def fetch(url, headers=None):
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers or {}), timeout=30) as response:
        body = response.read()
        return json.loads(body), dict(response.headers), body


def inspect(image):
    repo, tag = image.rsplit(':', 1)
    if '/' not in repo:
        repo = 'library/' + repo
    token = fetch('https://auth.docker.io/token?' + urllib.parse.urlencode({'service': 'registry.docker.io', 'scope': 'repository:' + repo + ':pull'}))[0]['token']
    headers = {'Authorization': 'Bearer ' + token, 'Accept': ACCEPT}
    base = 'https://registry-1.docker.io/v2/' + repo
    manifest, response_headers, raw = fetch(base + '/manifests/' + tag, headers)
    digest = next((v for k, v in response_headers.items() if k.lower() == 'docker-content-digest'), 'sha256:' + hashlib.sha256(raw).hexdigest())
    if 'manifests' in manifest:
        entries = [{'digest': m['digest'], 'platform': m.get('platform', {})} for m in manifest['manifests']]
    else:
        entries = [{'digest': digest}]
    configs = []
    for entry in entries:
        platform = entry.get('platform', {})
        if platform.get('os') == 'unknown':
            continue
        # Configuration blobs are tiny metadata documents, not filesystem layers.
        m = manifest if entry['digest'] == digest else fetch(base + '/manifests/' + entry['digest'], headers)[0]
        config = fetch(base + '/blobs/' + m['config']['digest'], headers)[0]
        env = config.get('config', {}).get('Env', [])
        configs.append({'manifest_digest': entry['digest'], 'os': config.get('os'), 'architecture': config.get('architecture'),
                        'variant': platform.get('variant'), 'created': config.get('created'),
                        'labels': config.get('config', {}).get('Labels'),
                        'version_environment': [e for e in env if e.startswith(('RABBITMQ_VERSION=', 'ERLANG_VERSION=', 'NODE_VERSION='))]})
    return {'image': image, 'digest': digest, 'media_type': manifest.get('mediaType'), 'manifests': entries, 'configs': configs}


def main():
    compose = json.loads((EVIDENCE / 'compose-all.json').read_text())
    images = [s['image'] for s in compose['services'].values()]
    results, errors = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        pending = {pool.submit(inspect, image): image for image in images}
        for future in concurrent.futures.as_completed(pending):
            image = pending[future]
            try:
                result = future.result()
                results.append(result)
                print(image + ': ' + str([(c['os'], c['architecture']) for c in result['configs']]), flush=True)
            except Exception as e:
                errors.append({'image': image, 'error': str(e)})
                print(image + ': ERROR ' + str(e), flush=True)
    (EVIDENCE / 'docker-registry.json').write_text(json.dumps({'collected_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'images': sorted(results, key=lambda r: r['image']), 'errors': errors}, indent=2) + '\n')
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
