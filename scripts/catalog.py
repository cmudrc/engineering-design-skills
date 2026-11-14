#!/usr/bin/env python3
"""Load the phase catalog and generate its human-readable reference."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/cmudrc/engineering-design-skills'


def load_catalog():
    data = json.loads((ROOT/'catalog.json').read_text())
    phases = data['phases']
    assert [phase['id'] for phase in phases] == list(range(6)), 'The framework must contain phases 0–5'
    assert [p['name'] for p in phases] == ['Planning','Concept Development','System-Level Design','Detail Design','Testing and Refinement','Production Ramp-Up'], 'Unexpected phase names'
    slugs = set()
    for entry in data['skills']:
        slug = entry['slug']
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug) and slug not in slugs, f'Invalid or duplicate skill: {slug}'
        slugs.add(slug)
        membership = entry['phases']
        assert membership and all(type(p) is int and 0 <= p <= 5 for p in membership), f'Invalid phase membership: {slug}'
        assert membership == sorted(set(membership)), f'Unsorted or duplicate membership: {slug}'
        assert entry['status'] in ('draft','planned'), f'Invalid status: {slug}'
        if entry['status'] == 'draft':
            assert (ROOT/'skills'/slug/'SKILL.md').is_file(), f'Missing draft skill: {slug}'
        else:
            assert type(entry.get('issue')) is int and entry['issue'] > 0, f'Missing planned-skill issue: {slug}'
    drafts = {e['slug'] for e in data['skills'] if e['status'] == 'draft'}
    assert drafts == {p.parent.name for p in (ROOT/'skills').glob('*/SKILL.md')}, 'Catalog and implemented skills differ'
    return data


def render_catalog(data):
    rows = ['# Skill catalog','','The library uses Ulrich and Eppinger’s six product-development phases. Skills have many-to-many membership: a method can support several phases, with a different decision and evidence standard in each. Membership is guidance rather than a restriction.','','`catalog.json` is the source of truth. Regenerate this reference with `python3 scripts/catalog.py`.','','## Phase framework','','| Phase | Focus | Typical output |','|---|---|---|']
    for phase in data['phases']:
        rows.append(f"| {phase['id']}: {phase['name']} | {phase['purpose']} | {phase['output']} |")
    rows += ['', '## Draft implementations','','| Skill | Phases |','|---|---|']
    for entry in data['skills']:
        if entry['status']=='draft':
            membership=', '.join(map(str,entry['phases']))
            rows.append(f"| [{entry['name']}](../skills/{entry['slug']}/SKILL.md) | {membership} |")
    rows += ['', '## Planned methods','','| Skill | Phases | Implementation issue |','|---|---|---|']
    for entry in data['skills']:
        if entry['status']=='planned':
            membership=', '.join(map(str,entry['phases']))
            rows.append(f"| {entry['name']} | {membership} | [#{entry['issue']}]({REPO}/issues/{entry['issue']}) |")
    rows += ['', '## Interpreting the phases','','Concept testing belongs in Phase 1. Phase 4 evaluates more developed product versions; prototyping, benchmarking, and other methods can still be used earlier. A small prototype or an optimization model does not by itself establish that a project has reached a later phase.','','The process skill spans all phases. The current implementations emphasize concept and analytical design; production-specific coverage is still planned.','','## Source','','Karl T. Ulrich and Steven D. Eppinger (2016), *Product Design and Development*, 6th edition, McGraw-Hill Education. Chapter 2, pp. 13–16, Exhibits 2-2 and 2-3; Exhibit 1-4, p. 9. Phase names follow this framework. The summaries and individual agent-skill memberships are this library’s interpretation.','']
    return '\n'.join(rows)


if __name__ == '__main__':
    text = render_catalog(load_catalog())
    target = ROOT/'docs/skill-catalog.md'
    if '--check' in sys.argv:
        if target.read_text() != text:
            raise SystemExit('Skill catalog docs are stale; run python3 scripts/catalog.py')
        print('Phase catalog and generated documentation agree.')
    else:
        target.write_text(text)
        print('Updated docs/skill-catalog.md from catalog.json.')
