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
        self.scripts = 0
        self.exchanges = 0
        self.hidden_exchanges = 0
        self.chat_windows = 0
        self.demo_controls = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
        if tag == 'script':
            self.scripts += 1
        if 'data-exchange' in attrs:
            self.exchanges += 1
            self.hidden_exchanges += 'hidden' in attrs
        if attrs.get('class') == 'conversation':
            assert attrs.get('role') == 'region' and attrs.get('aria-label'), 'Chat window needs an accessible name'
            assert attrs.get('tabindex') == '0', 'Chat window must support keyboard scrolling'
            self.chat_windows += 1
        if any(key.startswith('data-demo-') or key == 'data-model-reset' for key in attrs):
            self.demo_controls += 1
        if tag == 'input' and attrs.get('type') == 'range':
            self.demo_controls += 1


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
        assert page.scripts == 0, f'Expected static pages without JavaScript: {path}'
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
        assert page.hidden_exchanges == 0, f'Chat exchanges hidden for {slug}'
        assert page.chat_windows == 1, f'Expected one accessible chat window for {slug}'
        assert page.demo_controls == 0, f'Interactive demo controls remain for {slug}'
        for source in (ROOT/'skills'/slug).rglob('*'):
            if source.is_file():
                download = output/'downloads'/slug/source.relative_to(ROOT/'skills'/slug)
                assert download.read_bytes() == source.read_bytes(), f'Download changed: {download}'
    assert not list((output/'downloads').rglob('agents')), 'Host-specific configuration in downloads'
    print(f'Checked {len(pages)} pages: internal links, anchors, complete static accessible chats, and exact source downloads.')


if __name__ == '__main__':
    main()
