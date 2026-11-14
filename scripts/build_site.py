#!/usr/bin/env python3
"""Build the static skill library and example chats for GitHub Pages."""
import argparse
import hashlib
from html import escape
import json
from pathlib import Path
import re
import shutil
from urllib.parse import quote
from zipfile import ZipFile, ZIP_DEFLATED

import markdown

from catalog import load_catalog

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/cmudrc/engineering-design-skills'
BASE = ''
REVISION = ''


def url(path=''):
    return BASE + '/' + path.lstrip('/')


def render(text):
    result = markdown.markdown(text, extensions=['tables', 'fenced_code', 'sane_lists'])
    return result.replace('<table>', '<div class="table-scroll"><table>').replace('</table>', '</table></div>')


def codex_install_url(slug):
    prompt = f'$skill-installer Install the skill from {REPO}/tree/main/skills/{slug}'
    return 'codex://new?prompt=' + quote(prompt, safe='')


def install_options(slug):
    command = f'npx skills add cmudrc/engineering-design-skills --skill {slug} -a claude-code'
    return f'''<div class="install-options"><nav class="install-actions" aria-label="Install skill"><a href="{escape(codex_install_url(slug), quote=True)}">Open in Codex ↗</a><a href="{url(f'downloads/{slug}.zip')}" download>Claude ZIP ↓</a></nav><details><summary>Install help</summary><p><strong>Codex:</strong> opens a prefilled install request. Send it to start installation.</p><p><strong>Claude:</strong> download the ZIP, then open <a href="https://claude.ai/customize/skills">Customize → Skills</a> and choose “Upload a skill.” Upload the ZIP and enable the skill.</p><p><strong>Claude Code:</strong> run this in your project (requires Node.js 22.20+):</p><pre><code>{escape(command)}</code></pre><p>For another coding agent, omit <code>-a claude-code</code> and choose your agent. Installation uses the current project by default; add <code>-g</code> for all projects.</p><p class="install-sources">Installation docs: <a href="https://learn.chatgpt.com/docs/reference/commands">Codex links</a> · <a href="https://support.claude.com/en/articles/12512180-use-skills-in-claude">Claude skills</a> · <a href="https://github.com/vercel-labs/skills">Skills CLI</a></p></details></div>'''


def shell(title, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="AI skills for engineering design, with example conversations and reusable resources.">
<link rel="icon" type="image/svg+xml" href="{url('assets/favicon.svg')}">
<link rel="stylesheet" href="{url('assets/style.css')}?v={REVISION}">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header><a href="{url()}">Design Research Collective</a><a href="{REPO}">GitHub ↗</a></header>
{body}
<footer><a href="{REPO}/issues">Planned skills</a><a href="{REPO}/blob/main/LICENSE">MIT license</a></footer>
</body></html>'''


def homepage(skills, catalog):
    phase_sections = []
    for phase in catalog['phases']:
        members = [s for s in catalog['skills'] if s['status']=='draft' and s['slug']!='engineering-design-process' and phase['id'] in s['phases']]
        links = ''.join(f'<li><a href="{url("skills/"+s["slug"]+"/")}">{escape(s["name"])} <span aria-hidden="true">↗</span></a></li>' for s in members)
        if not links:
            links = '<li class="no-draft">No draft method yet.</li>'
        planned = sum(s['status']=='planned' and phase['id'] in s['phases'] for s in catalog['skills'])
        issue_url = REPO+'/issues?q=is%3Aopen%20label%3A%22phase%3A'+str(phase['id'])+'%22'
        phase_sections.append(f'<section class="phase-block" id="phase-{phase["id"]}"><h2><span>Phase {phase["id"]}</span>{escape(phase["name"])}</h2><ul>{links}</ul><a class="planned-link" href="{issue_url}">{planned} planned methods ↗</a></section>')
    body = f'''<main id="main" class="home"><h1>AI Skills for<br>Engineering Design</h1><p class="intro">Ulrich &amp; Eppinger’s six phases. Skills can belong to more than one.</p><a class="process-link" href="{url('skills/engineering-design-process/')}"><span>Engineering design process</span><small>All phases · 0–5</small><b aria-hidden="true">↗</b></a><div class="phase-grid">{''.join(phase_sections)}</div><p class="framework-note">Based on <em>Product Design and Development</em>, 6th edition. <a href="{REPO}/blob/main/docs/skill-catalog.md">Phase mapping ↗</a></p></main>'''
    return shell('AI Skills for Engineering Design', body)


def skillpage(skill, catalog):
    slug = skill['slug']
    directory = ROOT/'skills'/slug
    template = next((directory/'assets').glob('*.md'))
    template_path = str(template.relative_to(directory))
    membership = next(s['phases'] for s in catalog['skills'] if s['slug']==slug)
    if len(membership)==6:
        phase_links = '<a href="'+url('#phase-0')+'">All phases · 0–5</a>'
    else:
        phase_links = ' '.join(f'<a href="{url("#phase-"+str(i))}" title="{escape(catalog["phases"][i]["name"], quote=True)}" aria-label="Phase {i}: {escape(catalog["phases"][i]["name"], quote=True)}">{i}</a>' for i in membership)
    exchanges = []
    for i, turn in enumerate(skill['turns']):
        exchanges.append(f'''<article class="exchange" data-exchange="{i}"><div class="message user-message"><div class="speaker"><span class="avatar" aria-hidden="true">Y</span><span>You</span></div><div class="bubble"><p>{escape(turn['user'])}</p></div></div><div class="message assistant-message"><div class="speaker"><span class="avatar" aria-hidden="true">AI</span><span>Agent</span></div><div class="bubble prose">{render(turn['assistant'])}</div></div></article>''')
    body = f'''<main id="main" class="skill-page"><a class="back" href="{url()}">← All skills</a><h1>{escape(skill['title'])}</h1><p class="intro">{escape(skill['short'])}</p><div class="phase-membership"><span>Phases</span>{phase_links}</div>{install_options(slug)}<nav class="resources" aria-label="Skill resources"><a href="{REPO}/blob/main/skills/{slug}/SKILL.md">Instructions ↗</a><a href="{url(f'downloads/{slug}/{template_path}')}" download>Template ↓</a><a href="{REPO}/blob/main/skills/{slug}/references/worked-example.md">Worked example ↗</a></nav><div class="chat-window"><div class="chat-header"><span class="chat-title"><span class="chat-mark" aria-hidden="true">↳</span> Example chat</span><span>Illustrative · synthetic data</span></div><div class="conversation" role="region" aria-label="Example chat: {escape(skill['title'], quote=True)}" tabindex="0">{''.join(exchanges)}</div></div></main>'''
    return shell(skill['title']+' · AI Skills for Engineering Design', body)


def main():
    global BASE, REVISION
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-path', default='/engineering-design-skills')
    parser.add_argument('--output', default='_site')
    args=parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9/_-]*', args.base_path):
        parser.error('base path must contain URL path characters only')
    BASE='/' + args.base_path.strip('/') if args.base_path.strip('/') else ''
    output=(ROOT/args.output).resolve()
    if output == ROOT or not output.is_relative_to(ROOT):
        parser.error('output must be a generated subdirectory of the repository')
    if output.exists():
        if not (output/'.site-output').is_file():
            parser.error('refusing to replace an unmarked output directory')
        shutil.rmtree(output)
    output.mkdir(parents=True)
    (output/'.site-output').write_text('Generated by scripts/build_site.py\n')
    (output/'.nojekyll').touch()
    skills=json.loads((ROOT/'site/demos.json').read_text())
    catalog=load_catalog()
    actual={p.parent.name for p in (ROOT/'skills').glob('*/SKILL.md')}
    if {s['slug'] for s in skills} != actual or len(skills) != len(actual):
        raise ValueError('Each implemented skill must have exactly one demo')
    REVISION=hashlib.sha256((ROOT/'site/style.css').read_bytes()).hexdigest()[:12]
    assets=output/'assets'
    assets.mkdir()
    for filename in ['style.css','favicon.svg']:
        shutil.copyfile(ROOT/'site'/filename, assets/filename)
    (output/'index.html').write_text(homepage(skills, catalog),encoding='utf-8')
    for skill in skills:
        slug=skill['slug']
        if not skill['turns'] or any(not t.get('user') or not t.get('assistant') for t in skill['turns']):
            raise ValueError(f'{slug}: demo exchanges need both roles')
        page=output/'skills'/slug
        page.mkdir(parents=True)
        (page/'index.html').write_text(skillpage(skill,catalog),encoding='utf-8')
        shutil.copytree(ROOT/'skills'/slug, output/'downloads'/slug)
        with ZipFile(output/'downloads'/f'{slug}.zip', 'w', ZIP_DEFLATED) as archive:
            for source in sorted((ROOT/'skills'/slug).rglob('*')):
                if source.is_file():
                    archive.write(source, Path(slug)/source.relative_to(ROOT/'skills'/slug))
            archive.write(ROOT/'LICENSE', f'{slug}/LICENSE')
    print(f'Built {len(skills)+1} static pages with {sum(len(s["turns"]) for s in skills)} chat exchanges at {output}.')


if __name__ == '__main__':
    main()
