#!/usr/bin/env python3
"""Static site generator for Great People Encyclopedia."""

import json
import os
import shutil
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, '..', '..')
PEOPLE_DIR = os.path.join(PROJECT_ROOT, 'data', 'people')
FIELDS_DIR = os.path.join(PROJECT_ROOT, 'data', 'fields')
COUNTRIES_DIR = os.path.join(PROJECT_ROOT, 'data', 'countries')
ERAS_DIR = os.path.join(PROJECT_ROOT, 'data', 'eras')
LINKS_DIR = os.path.join(PROJECT_ROOT, 'generated', 'links', 'people')
SITE_DIR = os.path.join(PROJECT_ROOT, 'site')

LANG = 'en'
# Base path for GitHub Pages deployment (e.g. '/great-people-encyclopedia/')
# Set to '/' for root deployment.
BASE_PATH = '/great-people-encyclopedia/'


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_json_dir(directory):
    """Load all JSON files from a directory, keyed by id."""
    result = {}
    for filename in sorted(os.listdir(directory)):
        if not filename.endswith('.json'):
            continue
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
            data = json.load(f)
            result[data['id']] = data
    return result


def t(obj, lang=LANG):
    """Extract text for a given language from an i18n object, with fallback to en."""
    if obj is None:
        return ''
    if isinstance(obj, str):
        return obj
    return obj.get(lang) or obj.get('en', '')


def esc(text):
    """Escape HTML special characters."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))


def write_page(path, content):
    """Write an HTML file, creating directories as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def page(title, body, breadcrumbs=None):
    """Wrap body content in a full HTML page."""
    bc = ''
    if breadcrumbs:
        parts = ['<nav>']
        for i, (label, href) in enumerate(breadcrumbs):
            if i > 0:
                parts.append(' &gt; ')
            if href:
                parts.append(f'<a href="{href}">{esc(label)}</a>')
            else:
                parts.append(esc(label))
        parts.append('</nav>')
        bc = ''.join(parts)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<base href="{BASE_PATH}">
<title>{esc(title)} - Great People Encyclopedia</title>
</head>
<body>
{bc}
{body}
</body>
</html>
'''


def person_page(title, body, breadcrumbs, person_id):
    """Wrap body content in a full HTML page with graph support for person pages."""
    bc = ''
    if breadcrumbs:
        parts = ['<nav>']
        for i, (label, href) in enumerate(breadcrumbs):
            if i > 0:
                parts.append(' &gt; ')
            if href:
                parts.append(f'<a href="{href}">{esc(label)}</a>')
            else:
                parts.append(esc(label))
        parts.append('</nav>')
        bc = ''.join(parts)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<base href="{BASE_PATH}">
<title>{esc(title)} - Great People Encyclopedia</title>
</head>
<body>
{bc}
{body}
<script src="https://unpkg.com/cytoscape@3.30.4/dist/cytoscape.min.js"></script>
<script src="assets/js/graph.js"></script>
</body>
</html>
'''


def person_link(pid, people):
    """Generate an <a> tag for a person."""
    if pid in people:
        name = esc(t(people[pid]['name']))
        return f'<a href="en/people/{pid}.html">{name}</a>'
    return esc(pid)


# ---------------------------------------------------------------------------
# Page generators
# ---------------------------------------------------------------------------

def generate_person_page(person, people, fields, countries, links):
    pid = person['id']
    name = t(person['name'])

    sections = []

    # Overview
    overview = t(person.get('overview'))
    if overview:
        sections.append(f'<section>\n<h2>Overview</h2>\n<p>{esc(overview)}</p>\n</section>')

    # Early Life
    early_life = t(person.get('early_life'))
    if early_life:
        sections.append(f'<section>\n<h2>Early Life</h2>\n<p>{esc(early_life)}</p>\n</section>')

    # Impact
    impact = t(person.get('impact'))
    if impact:
        sections.append(f'<section>\n<h2>Impact</h2>\n<p>{esc(impact)}</p>\n</section>')

    # Relation Graph
    graph_html = f'''<section>
<h2>Relation Graph</h2>
<div id="relation-graph" data-person="{pid}" style="width:100%;height:450px;border:1px solid #ddd;border-radius:8px;background:#fafafa;"></div>
<div id="graph-legend" style="margin-top:8px;font-size:13px;color:#555;"></div>
</section>'''
    sections.append(graph_html)

    # Timeline
    timeline = person.get('timeline', [])
    if timeline:
        items = []
        for entry in timeline:
            year = entry.get('year', '')
            event = t(entry.get('event'))
            if event:
                items.append(f'<li><strong>{year}</strong> — {esc(event)}</li>')
        if items:
            sections.append('<section>\n<h2>Timeline</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    # Related People (deduplicated from all relation types, up to 6)
    link_data = links.get(pid, {})
    related_seen = set()
    related_ids = []
    for key in ('same_field', 'same_country', 'same_era'):
        for rid in link_data.get(key, []):
            if rid not in related_seen:
                related_seen.add(rid)
                related_ids.append(rid)
                if len(related_ids) >= 6:
                    break
        if len(related_ids) >= 6:
            break
    if related_ids:
        items = [f'<li>{person_link(rid, people)}</li>' for rid in related_ids]
        sections.append('<section>\n<h2>Related People</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    # Famous Works
    works = person.get('famous_works', [])
    if works:
        items = []
        for w in works:
            title = t(w.get('title'))
            year = w.get('year', '')
            desc = t(w.get('description'))
            line = f'<strong>{esc(title)}</strong> ({year})'
            if desc:
                line += f' — {esc(desc)}'
            items.append(f'<li>{line}</li>')
        if items:
            sections.append('<section>\n<h2>Famous Works</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    # Quotes
    quotes = person.get('quotes', [])
    if quotes:
        items = []
        for q in quotes:
            text = t(q.get('text'))
            source = q.get('source', '')
            if text:
                cite = f' <cite>— {esc(source)}</cite>' if source else ''
                items.append(f'<li><blockquote>&ldquo;{esc(text)}&rdquo;{cite}</blockquote></li>')
        if items:
            sections.append('<section>\n<h2>Quotes</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    # Metadata
    meta_items = []
    birth = person.get('birth_year')
    death = person.get('death_year')
    if birth is not None:
        life = f'{birth}'
        if death is not None:
            life += f' – {death}'
        else:
            life += ' – present'
        meta_items.append(f'<li><strong>Lifespan:</strong> {life}</li>')

    person_fields = person.get('fields', [])
    if person_fields:
        field_links = []
        for fid in person_fields:
            fname = esc(t(fields[fid]['name'])) if fid in fields else esc(fid)
            field_links.append(f'<a href="en/fields/{fid}.html">{fname}</a>')
        meta_items.append(f'<li><strong>Fields:</strong> {", ".join(field_links)}</li>')

    person_countries = person.get('countries', [])
    if person_countries:
        country_links = []
        for cid in person_countries:
            cname = esc(t(countries[cid]['name'])) if cid in countries else esc(cid)
            country_links.append(f'<a href="en/countries/{cid}.html">{cname}</a>')
        meta_items.append(f'<li><strong>Countries:</strong> {", ".join(country_links)}</li>')

    if meta_items:
        sections.insert(0, '<section>\n<ul>\n' + '\n'.join(meta_items) + '\n</ul>\n</section>')

    # Derived links
    link_data = links.get(pid, {})
    for key, label in [('same_field', 'Same Field'), ('same_country', 'Same Country'), ('same_era', 'Same Era')]:
        ids = link_data.get(key, [])
        if ids:
            items = [f'<li>{person_link(rid, people)}</li>' for rid in ids]
            sections.append(f'<section>\n<h2>{label}</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    body = f'<h1>{esc(name)}</h1>\n' + '\n\n'.join(sections)
    breadcrumbs = [('Home', 'index.html'), ('People', 'en/people/'), (name, None)]
    return person_page(name, body, breadcrumbs, pid)


def generate_field_page(field, people_by_field, people):
    fid = field['id']
    name = t(field['name'])
    desc = t(field.get('description'))

    sections = []
    if desc:
        sections.append(f'<section>\n<h2>Description</h2>\n<p>{esc(desc)}</p>\n</section>')

    pids = people_by_field.get(fid, [])
    if pids:
        items = [f'<li>{person_link(pid, people)}</li>' for pid in pids]
        sections.append(f'<section>\n<h2>People ({len(pids)})</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    body = f'<h1>{esc(name)}</h1>\n' + '\n\n'.join(sections)
    breadcrumbs = [('Home', 'index.html'), ('Fields', 'en/fields/'), (name, None)]
    return page(name, body, breadcrumbs)


def generate_country_page(country, people_by_country, people):
    cid = country['id']
    name = t(country['name'])
    desc = t(country.get('description'))

    sections = []
    if desc:
        sections.append(f'<section>\n<h2>Description</h2>\n<p>{esc(desc)}</p>\n</section>')

    pids = people_by_country.get(cid, [])
    if pids:
        items = [f'<li>{person_link(pid, people)}</li>' for pid in pids]
        sections.append(f'<section>\n<h2>People ({len(pids)})</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    body = f'<h1>{esc(name)}</h1>\n' + '\n\n'.join(sections)
    breadcrumbs = [('Home', 'index.html'), ('Countries', 'en/countries/'), (name, None)]
    return page(name, body, breadcrumbs)


def generate_era_page(era, people_by_era, people):
    eid = era['id']
    name = t(era['name'])
    desc = t(era.get('description'))
    start = era.get('start_year', '')
    end = era.get('end_year', '')

    sections = []
    sections.append(f'<section>\n<p><strong>{start} – {end}</strong></p>\n</section>')
    if desc:
        sections.append(f'<section>\n<h2>Description</h2>\n<p>{esc(desc)}</p>\n</section>')

    pids = people_by_era.get(eid, [])
    if pids:
        items = [f'<li>{person_link(pid, people)}</li>' for pid in pids]
        sections.append(f'<section>\n<h2>People ({len(pids)})</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    body = f'<h1>{esc(name)}</h1>\n' + '\n\n'.join(sections)
    breadcrumbs = [('Home', 'index.html'), ('Eras', 'en/eras/'), (name, None)]
    return page(name, body, breadcrumbs)


def generate_people_index(people):
    """Generate /en/people/index.html listing all people."""
    items = []
    for pid in sorted(people.keys()):
        name = esc(t(people[pid]['name']))
        items.append(f'<li><a href="./{pid}.html">{name}</a></li>')
    body = f'<h1>People ({len(items)})</h1>\n<ul>\n' + '\n'.join(items) + '\n</ul>'
    breadcrumbs = [('Home', 'index.html'), ('People', None)]
    return page(f'People ({len(items)})', body, breadcrumbs)


def generate_index(people, fields, countries, eras):
    # Build label maps for JS
    field_labels = {fid: t(f['name']) for fid, f in fields.items()}
    country_labels = {cid: t(c['name']) for cid, c in countries.items()}

    field_json = json.dumps(field_labels, ensure_ascii=False)
    country_json = json.dumps(country_labels, ensure_ascii=False)

    sections = []

    # Filter app (JS-powered)
    sections.append(f'''<script id="field-labels" type="application/json">{field_json}</script>
<script id="country-labels" type="application/json">{country_json}</script>
<section>
<h2>People ({len(people)})</h2>
<div id="people-filter-app"><noscript>
<ul>
''' + '\n'.join(f'<li>{person_link(pid, people)}</li>' for pid in sorted(people.keys())) + '''
</ul>
</noscript></div>
</section>''')

    # Fields
    items = []
    for fid in sorted(fields.keys()):
        name = esc(t(fields[fid]['name']))
        items.append(f'<li><a href="en/fields/{fid}.html">{name}</a></li>')
    sections.append(f'<section>\n<h2>Fields ({len(items)})</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    # Countries
    items = []
    for cid in sorted(countries.keys()):
        name = esc(t(countries[cid]['name']))
        items.append(f'<li><a href="en/countries/{cid}.html">{name}</a></li>')
    sections.append(f'<section>\n<h2>Countries ({len(items)})</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    # Eras
    items = []
    for eid, era in sorted(eras.items(), key=lambda x: x[1].get('start_year', 0)):
        name = esc(t(era['name']))
        items.append(f'<li><a href="en/eras/{eid}.html">{name}</a></li>')
    sections.append(f'<section>\n<h2>Eras ({len(items)})</h2>\n<ul>\n' + '\n'.join(items) + '\n</ul>\n</section>')

    nav_links = '<p style="margin-bottom:16px;"><a href="timeline.html">Timeline</a> | <a href="map.html">World Map</a> | <a href="search.html">Search</a> | <a href="random.html">Random Person</a></p>'
    body = '<h1>Great People Encyclopedia</h1>\n' + nav_links + '\n\n'.join(sections)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<base href="{BASE_PATH}">
<title>Great People Encyclopedia</title>
</head>
<body>
{body}
<script src="assets/js/filter.js"></script>
</body>
</html>
'''


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # 1. Load all data
    people = load_json_dir(PEOPLE_DIR)
    fields = load_json_dir(FIELDS_DIR)
    countries = load_json_dir(COUNTRIES_DIR)
    eras = load_json_dir(ERAS_DIR)

    links = {}
    if os.path.isdir(LINKS_DIR):
        for filename in os.listdir(LINKS_DIR):
            if not filename.endswith('.json'):
                continue
            with open(os.path.join(LINKS_DIR, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                links[data['person']] = data

    print(f"Loaded: {len(people)} people, {len(fields)} fields, {len(countries)} countries, {len(eras)} eras, {len(links)} link files")

    # 2. Build lookup tables
    eras_sorted = sorted(eras.values(), key=lambda e: e['start_year'])

    people_by_field = defaultdict(list)
    people_by_country = defaultdict(list)
    people_by_era = defaultdict(list)

    for pid, p in sorted(people.items()):
        for fid in p.get('fields', []):
            people_by_field[fid].append(pid)
        for cid in p.get('countries', []):
            people_by_country[cid].append(pid)
        birth = p.get('birth_year')
        if birth is not None:
            for era in eras_sorted:
                if era['start_year'] <= birth < era['end_year']:
                    people_by_era[era['id']].append(pid)
                    break

    # 3. Generate people pages
    count_people = 0
    for pid, p in sorted(people.items()):
        html = generate_person_page(p, people, fields, countries, links)
        write_page(os.path.join(SITE_DIR, 'en', 'people', f'{pid}.html'), html)
        count_people += 1
    print(f"Generated {count_people} people pages")

    # 3b. Generate people index page
    html = generate_people_index(people)
    write_page(os.path.join(SITE_DIR, 'en', 'people', 'index.html'), html)
    print("Generated en/people/index.html")

    # 4. Generate field pages
    count_fields = 0
    for fid, f in sorted(fields.items()):
        html = generate_field_page(f, people_by_field, people)
        write_page(os.path.join(SITE_DIR, 'en', 'fields', f'{fid}.html'), html)
        count_fields += 1
    print(f"Generated {count_fields} field pages")

    # 5. Generate country pages
    count_countries = 0
    for cid, c in sorted(countries.items()):
        html = generate_country_page(c, people_by_country, people)
        write_page(os.path.join(SITE_DIR, 'en', 'countries', f'{cid}.html'), html)
        count_countries += 1
    print(f"Generated {count_countries} country pages")

    # 6. Generate era pages
    count_eras = 0
    for eid, e in sorted(eras.items()):
        html = generate_era_page(e, people_by_era, people)
        write_page(os.path.join(SITE_DIR, 'en', 'eras', f'{eid}.html'), html)
        count_eras += 1
    print(f"Generated {count_eras} era pages")

    # 7. Copy relation files to site for client-side access
    site_links_dir = os.path.join(SITE_DIR, 'generated', 'links', 'people')
    if os.path.isdir(LINKS_DIR):
        os.makedirs(site_links_dir, exist_ok=True)
        for filename in os.listdir(LINKS_DIR):
            if filename.endswith('.json'):
                shutil.copy2(os.path.join(LINKS_DIR, filename),
                             os.path.join(site_links_dir, filename))
        print(f"Copied {len(os.listdir(site_links_dir))} relation files to site/")

    # 8. Generate index page
    html = generate_index(people, fields, countries, eras)
    write_page(os.path.join(SITE_DIR, 'index.html'), html)
    print("Generated index.html")

    total = count_people + count_fields + count_countries + count_eras + 1
    print(f"\nTotal: {total} pages generated in site/")


if __name__ == '__main__':
    main()
