#!/usr/bin/env python3
"""Check generated pages, internal links, demo coverage, and source downloads."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.controls = []
        self.exchanges = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if 'aria-controls' in attrs:
            self.controls.extend(attrs['aria-controls'].split())
        if 'data-exchange' in attrs:
            self.exchanges += 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-path', default='/engineering-design-skills')
    parser.add_argument('--output', default='_site')
    args = parser.parse_args()
    output = (ROOT/args.output).resolve()
    base = '/' + args.base_path.strip('/') if args.base_path.strip('/') else ''
    pages = {}
    for path in output.rglob('*.html'):
        page = Page()
        page.feed(path.read_text())
        assert len(page.ids) == len(set(page.ids)), f'Duplicate IDs in {path}'
        assert set(page.controls) <= set(page.ids), f'Unresolved aria-controls in {path}'
        pages[path] = page
    demos = json.loads((ROOT/'site/demos.json').read_text())
    assert len(pages) == len(demos)+1, 'Missing or unexpected generated pages'
    for path, page in pages.items():
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            target = unquote(parsed.path)
            if not target:
                destination = path
            elif target.startswith('/'):
                assert target == base or target.startswith(base+'/'), f'Incorrect base path: {link}'
                destination = output/target[len(base):].lstrip('/')
            else:
                destination = path.parent/target
            if destination.is_dir():
                destination = destination/'index.html'
            assert destination.exists(), f'{path.relative_to(output)}: broken link {link}'
            assert destination.resolve().is_relative_to(output), f'Link escapes output: {link}'
            if parsed.fragment and destination.suffix == '.html':
                assert parsed.fragment in pages[destination].ids, f'Missing anchor: {link}'
    for demo in demos:
        slug = demo['slug']
        page = pages[output/'skills'/slug/'index.html']
        assert page.exchanges == len(demo['turns']), f'Demo exchanges missing for {slug}'
        for source in (ROOT/'skills'/slug).rglob('*'):
            if source.is_file():
                download = output/'downloads'/slug/source.relative_to(ROOT/'skills'/slug)
                assert download.read_bytes() == source.read_bytes(), f'Download changed: {download}'
    assert not list((output/'downloads').rglob('agents')), 'Host-specific configuration in downloads'
    print(f'Checked {len(pages)} pages: internal links, anchors, tab controls, demo exchanges, and exact source downloads.')


if __name__ == '__main__':
    main()
