#!/usr/bin/env python3
"""Generate a minimal search index JSON for client-side search."""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, '..', '..')
PEOPLE_DIR = os.path.join(PROJECT_ROOT, 'data', 'people')
OUTPUT_PATH = os.path.join(PROJECT_ROOT, 'site', 'search.json')

LANG = 'en'


def t(obj):
    if obj is None:
        return ''
    if isinstance(obj, str):
        return obj
    return obj.get(LANG) or obj.get('en', '')


def main():
    entries = []
    for filename in sorted(os.listdir(PEOPLE_DIR)):
        if not filename.endswith('.json'):
            continue
        with open(os.path.join(PEOPLE_DIR, filename), 'r', encoding='utf-8') as f:
            p = json.load(f)
        entries.append({
            "id": p["id"],
            "name": t(p.get("name")),
            "fields": p.get("fields", []),
            "countries": p.get("countries", []),
            "birth_year": p.get("birth_year"),
            "death_year": p.get("death_year"),
            "overview": t(p.get("overview")),
        })

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f"Generated {OUTPUT_PATH} with {len(entries)} entries.")


if __name__ == '__main__':
    main()
