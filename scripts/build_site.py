#!/usr/bin/env python3
"""Build the GitHub Pages showcase from repository skills and curated demos."""
import argparse
import hashlib
from html import escape
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlsplit

import markdown

ROOT = Path(__file__).resolve().parents[1]
REPO = 'https://github.com/cmudrc/engineering-design-skills'
BASE = ''
REVISION = ''


def url(path=''):
    return BASE + '/' + path.lstrip('/')


def render(text, slug=None):
    result = markdown.markdown(text, extensions=['tables', 'fenced_code', 'sane_lists'])
    if slug:
        def resource(match):
            target = match.group(1)
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith('#'):
                return match.group(0)
            return 'href="' + escape(url(f'downloads/{slug}/{target}'), quote=True) + '"'
        result = re.sub(r'href="([^"]+)"', resource, result)
    return result.replace('<table>', '<div class="table-scroll"><table>').replace('</table>', '</table></div>')


def document(path, slug):
    text = path.read_text(encoding='utf-8')
    if text.startswith('---\n'):
        text = text.split('---', 2)[2].lstrip()
    text = re.sub(r'^# [^\n]+\n', '', text, count=1).lstrip()
    result = render(text, slug)
    return re.sub(r'<(/?)h([1-5])([^>]*)>', lambda m: f'<{m[1]}h{int(m[2])+1}{m[3]}>', result)


def shell(title, body, path='', description='Engineering design methods, illustrated through conversations and artifacts.'):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · Engineering Design Skills</title>
<meta name="description" content="{escape(description, quote=True)}">
<meta name="theme-color" content="#f6f5ef">
<link rel="canonical" href="https://cmudrc.github.io{url(path)}">
<link rel="icon" type="image/svg+xml" href="{url('assets/favicon.svg')}">
<link rel="stylesheet" href="{url('assets/style.css')}?v={REVISION}">
<script src="{url('assets/site.js')}?v={REVISION}" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><div class="header-inner">
<a class="brand" href="{url()}"><span class="brand-mark" aria-hidden="true">d<span>↗</span></span><span>Engineering<br>Design Skills</span></a>
<nav aria-label="Main navigation"><a href="{url('#library')}">The library</a><a href="{url('#roadmap')}">Roadmap</a><a class="source-link" href="{REPO}">GitHub <span aria-hidden="true">↗</span></a></nav>
</div></header>
{body}
<footer class="site-footer"><div><a href="https://github.com/cmudrc">Design Research Collective</a><span>Carnegie Mellon University</span></div><p>Open methods. Reviewable artifacts. <a href="{REPO}/blob/main/LICENSE">MIT licensed.</a></p></footer>
</body></html>'''


def homepage(skills):
    rows = []
    for i, skill in enumerate(skills, 1):
        rows.append(f'''<a class="library-row" href="{url('skills/'+skill['slug']+'/')}">
<span class="row-number">0{i}</span><div><h3>{escape(skill['title'])}</h3><p>{escape(skill['short'])}</p></div><span class="row-output">{escape(skill['output'])}</span><span class="row-arrow" aria-hidden="true">↗</span></a>''')
    steps = ''.join(f'<a href="{url("skills/"+s["slug"]+"/")}"><span>0{i}</span>{label}<b aria-hidden="true">↗</b></a>' for i, (s, label) in enumerate(zip(skills, ['Guide the process', 'Compare the evidence', 'Generate alternatives', 'Formulate the problem']), 1))
    catalog = (ROOT/'docs/skill-catalog.md').read_text().split('## Planned methods', 1)[1]
    catalog = catalog.split('\n\nThe initial catalog', 1)[0].strip()
    roadmap = render(catalog)
    body = f'''<main id="main">
<section class="home-hero page-width">
<div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span> A working library from the Design Research Collective</p>
<h1>Engineering design,<br><em>made explicit.</em></h1>
<p class="hero-description">Methods for agents that design physical products and engineered systems. Explore the reasoning, inspect the artifacts, and see what comes next.</p>
<div class="hero-actions"><a class="button primary" href="{url('skills/engineering-design-process/')}">Walk through a demo <span aria-hidden="true">↗</span></a><a class="text-link" href="#library">Explore the skills <span aria-hidden="true">↓</span></a></div>
<p class="hero-meta"><span>04 draft skills</span><span>23 planned methods</span><span>Platform neutral</span></p></div>
<aside class="process-map" aria-label="The connected demo"><div class="map-topline"><span>ONE DESIGN PROBLEM</span><span class="tiny-tag">4 SKILLS</span></div><div class="case-icon" aria-hidden="true"><span class="case-handle"></span><span class="case-lid"></span><span class="case-body"></span><span class="case-line"></span></div><h2>A lighter way<br>to keep things cold.</h2><p>Follow a portable container from an open brief to a mathematical formulation.</p><div class="map-steps">{steps}</div><div class="map-footnote">Illustrative conversations · synthetic data</div></aside>
</section>
<section class="library-section page-width" id="library"><div class="section-heading"><div><p class="eyebrow">THE CURRENT LIBRARY</p><h2>Four methods. Four ways forward.</h2></div><p>Each skill pairs a step-through conversation with its instructions, a reusable template, and a worked example.</p></div><div class="library-list">{''.join(rows)}</div></section>
<section class="evidence-section page-width"><span class="section-index">WHY THE DETAILS MATTER</span><div><h2>A promising number<br>needs a common basis.</h2><p>In the benchmark demo, one container claims ten hours of cooling. Different test conditions and an incomplete mass boundary make that claim unsuitable for a direct ranking.</p><a class="text-link" href="{url('skills/technical-benchmarking/')}">See how the skill handles it <span aria-hidden="true">↗</span></a></div><div class="benchmark-preview"><div class="preview-label">SYNTHETIC REFERENCE DATA</div><div class="preview-row"><b>A</b><span>6 h <small>at 30 °C</small></span><span class="data-tag">Comparable</span></div><div class="preview-row"><b>B</b><span>5 h <small>at 30 °C</small></span><span class="data-tag">Comparable</span></div><div class="preview-row uncertain"><b>C</b><span>10 h <small>at 20 °C</small></span><span class="data-tag">Needs context</span></div></div></section>
<section class="roadmap-section page-width" id="roadmap"><div class="section-heading"><div><p class="eyebrow">GROWING THE LIBRARY</p><h2>The rest of the design toolbox.</h2></div><p>Needs and requirements, analogy, concept selection, robust design, and more. Every planned method has an implementation issue.</p></div><details class="roadmap-details"><summary>Explore the 23 planned methods <span aria-hidden="true">+</span></summary>{roadmap}</details><p class="draft-note">These skills are initial drafts. The demos illustrate their intended behavior using authored conversations and synthetic inputs; they are not controlled agent-performance evaluations.</p></section>
</main>'''
    return shell('Engineering design, made explicit', body)


def explorer():
    return '''<section class="model-explorer" aria-labelledby="model-title"><div class="explorer-heading"><div><p class="eyebrow">TRY THE FORMULATION</p><h2 id="model-title">Change a variable. Inspect the constraint.</h2></div><span class="tiny-tag">TOY MODEL</span></div>
<p>Adjust insulation thickness and ice mass for the fixed foam-and-ice architecture. This evaluates trial designs without searching for an optimum.</p>
<div class="model-grid"><div class="model-inputs"><label for="thickness">Insulation thickness <output id="thickness-label" for="thickness">30 mm</output></label><input id="thickness" type="range" min="10" max="60" step="1" value="30"><label for="ice">Ice mass <output id="ice-label" for="ice">0.55 kg</output></label><input id="ice" type="range" min="0.2" max="1" step="0.01" value="0.55"><button class="text-button" type="button" data-model-reset>Reset trial design ↺</button></div>
<div class="model-results" aria-live="polite" aria-atomic="true"><div><span>Ready-to-load mass</span><strong id="result-mass">1.175 kg</strong><small>Requirement: ≤ 1.5 kg</small></div><div><span>Six-hour energy margin</span><strong id="result-energy">+10.9 kJ</strong><small>Requirement: ≥ 0 kJ</small></div><p id="result-status" class="model-status pass">Passes modeled constraints</p></div></div>
<details class="model-assumptions"><summary>Model assumptions and the missing temperature relationship</summary><p>Mass = 0.4 + 7.5t + m [kg]. Heat leak = 0.225/t + 0.5 [W]. Energy margin = 334000m − 21600 × heat leak [J], with t in meters and m in kilograms. All parameter values are synthetic.</p><p>The model assumes a fixed effective area, a constant 30 K temperature difference, and latent cooling capacity. It omits transient payload temperature, openings, geometry changes, and material variation. Passing the energy screen does not establish the original 10 °C payload-temperature requirement.</p></details></section>'''


def skillpage(skill, skills):
    slug = skill['slug']
    directory = ROOT/'skills'/slug
    index = skills.index(skill)
    resource = {
        'instructions': ('Skill instructions', directory/'SKILL.md', 'SKILL.md'),
        'template': ('Output template', next((directory/'assets').glob('*.md')), ''),
        'example': ('Worked example', directory/'references/worked-example.md', 'references/worked-example.md'),
    }
    resource['template'] = (resource['template'][0], resource['template'][1], str(resource['template'][1].relative_to(directory)))
    tabs = [('demo', 'Demo interaction'), ('instructions', 'Instructions'), ('template', 'Template'), ('example', 'Worked example')]
    tabhtml = ''.join(f'<button type="button" role="tab" id="tab-{key}" aria-controls="panel-{key}" aria-selected="{str(key=="demo").lower()}" tabindex="{0 if key=="demo" else -1}" data-tab="{key}">{label}</button>' for key,label in tabs)
    exchanges = []
    for i, turn in enumerate(skill['turns']):
        exchanges.append(f'''<article class="exchange" data-exchange="{i}"{' hidden' if i else ''}><div class="message user-message"><div class="message-role">DESIGNER <span>0{i+1}</span></div><p>{escape(turn['user'])}</p></div><div class="message assistant-message"><div class="message-role"><span class="agent-icon" aria-hidden="true">↳</span> AGENT <span>USING THIS SKILL</span></div><div class="prose">{render(turn['assistant'])}</div></div></article>''')
    panels = []
    for key,(title,path,relative) in resource.items():
        panels.append(f'<section class="skill-panel source-panel" id="panel-{key}" role="tabpanel" aria-labelledby="tab-{key}" hidden><div class="document-topline"><h2>{title}</h2><a href="{url(f"downloads/{slug}/{relative}")}" download>Download Markdown ↓</a></div><div class="prose">{document(path,slug)}</div></section>')
    nextskill = skills[(index+1)%len(skills)]
    body = f'''<main id="main" class="skill-main page-width"><div class="breadcrumbs"><a href="{url('#library')}">The library</a><span aria-hidden="true">/</span><span>{escape(skill['title'])}</span></div>
<div class="skill-layout"><aside class="skill-sidebar"><p class="eyebrow">{escape(skill['eyebrow'])}</p><h1>{escape(skill['title'])}</h1><p class="skill-description">{escape(skill['description'])}</p><span class="draft-label">DRAFT SKILL</span><dl class="skill-facts"><dt>What it makes</dt><dd>{escape(skill['output'])}</dd><dt>What it needs</dt><dd>{escape(skill['inputs'])}</dd><dt>The critical check</dt><dd>{escape(skill['check'])}</dd></dl><a class="text-link" href="{REPO}/tree/main/skills/{slug}">View skill source ↗</a><div class="next-skill"><span>NEXT IN THE WALKTHROUGH</span><a href="{url('skills/'+nextskill['slug']+'/')}">{escape(nextskill['title'])} ↗</a></div></aside>
<div class="skill-workbench"><div class="skill-tabs" role="tablist" aria-label="Explore this skill">{tabhtml}</div><section class="skill-panel" id="panel-demo" role="tabpanel" aria-labelledby="tab-demo"><div class="demo-intro"><span class="demo-label"><span class="status-dot"></span> CURATED CONVERSATION</span><p>A portable insulated container · synthetic inputs</p></div><div class="conversation">{''.join(exchanges)}</div><div class="demo-controls"><div><button class="button secondary" type="button" data-demo-back disabled>← Back</button><button class="button primary" type="button" data-demo-next>Next exchange →</button></div><span class="demo-progress" role="status" aria-live="polite">Exchange 1 of {len(exchanges)}</span><div><button class="text-button" type="button" data-demo-all>Read all</button><button class="text-button" type="button" data-demo-reset>Replay ↺</button></div></div><p class="demo-disclosure">This authored conversation demonstrates the method. It is not a live model run or evidence of agent effectiveness.</p>{explorer() if skill.get('explorer') else ''}</section>{''.join(panels)}<noscript><style>.exchange[hidden],.skill-panel[hidden]{{display:block!important}}.demo-controls,.skill-tabs{{display:none}}</style><p>JavaScript is disabled. All conversation exchanges and source materials are shown below. The model explorer requires JavaScript.</p></noscript></div></div></main>'''
    return shell(skill['title'], body, 'skills/'+slug+'/', skill['description'])


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
    actual={p.parent.name for p in (ROOT/'skills').glob('*/SKILL.md')}
    if {s['slug'] for s in skills} != actual or len(skills) != len(actual):
        raise ValueError('Each implemented skill must have exactly one demo')
    REVISION=hashlib.sha256(b''.join((ROOT/'site'/p).read_bytes() for p in ['style.css','site.js'])).hexdigest()[:12]
    assets=output/'assets'
    assets.mkdir()
    for filename in ['style.css','site.js','favicon.svg']:
        shutil.copyfile(ROOT/'site'/filename, assets/filename)
    (output/'index.html').write_text(homepage(skills),encoding='utf-8')
    for skill in skills:
        slug=skill['slug']
        if not skill['turns'] or any(not t.get('user') or not t.get('assistant') for t in skill['turns']):
            raise ValueError(f'{slug}: demo exchanges need both roles')
        page=output/'skills'/slug
        page.mkdir(parents=True)
        (page/'index.html').write_text(skillpage(skill,skills),encoding='utf-8')
        shutil.copytree(ROOT/'skills'/slug, output/'downloads'/slug)
    print(f'Built {len(skills)+1} pages with {sum(len(s["turns"]) for s in skills)} demo exchanges at {output}; base path {BASE or "/"}.')


if __name__ == '__main__':
    main()
