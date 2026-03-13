#!/usr/bin/env python3
"""Generate derived relationship graphs between people based on shared fields, countries, and eras."""

import json
import os
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, '..', '..')
PEOPLE_DIR = os.path.join(PROJECT_ROOT, 'data', 'people')
ERAS_DIR = os.path.join(PROJECT_ROOT, 'data', 'eras')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'generated', 'links', 'people')

MAX_ENTRIES = 20


def load_json_files(directory):
    """Load all JSON files from a directory, returning a list of parsed dicts."""
    results = []
    for filename in sorted(os.listdir(directory)):
        if not filename.endswith('.json'):
            continue
        path = os.path.join(directory, filename)
        with open(path, 'r', encoding='utf-8') as f:
            results.append(json.load(f))
    return results


def determine_era(birth_year, eras):
    """Determine which era a person belongs to based on birth_year."""
    for era in eras:
        if era['start_year'] <= birth_year < era['end_year']:
            return era['id']
    return None


def main():
    # Load all people
    people = load_json_files(PEOPLE_DIR)
    valid_ids = {p['id'] for p in people}
    print(f"Loaded {len(people)} people.")

    # Load all eras
    eras = load_json_files(ERAS_DIR)
    eras.sort(key=lambda e: e['start_year'])
    print(f"Loaded {len(eras)} eras.")

    # Build indexes: field -> set of person ids
    field_index = defaultdict(set)
    country_index = defaultdict(set)
    era_index = defaultdict(set)
    person_fields = {}
    person_countries = {}
    person_era = {}

    for p in people:
        pid = p['id']
        fields = p.get('fields', [])
        countries = p.get('countries', [])
        birth_year = p.get('birth_year')

        person_fields[pid] = fields
        person_countries[pid] = countries

        for field in fields:
            field_index[field].add(pid)

        for country in countries:
            country_index[country].add(pid)

        if birth_year is not None:
            era = determine_era(birth_year, eras)
            if era:
                era_index[era].add(pid)
                person_era[pid] = era

    # Generate output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    count = 0

    for p in people:
        pid = p['id']

        # same_field: people sharing at least one field
        same_field = set()
        for field in person_fields.get(pid, []):
            same_field |= field_index[field]
        same_field.discard(pid)

        # same_country: people sharing at least one country
        same_country = set()
        for country in person_countries.get(pid, []):
            same_country |= country_index[country]
        same_country.discard(pid)

        # same_era: people in the same era
        same_era = set()
        era = person_era.get(pid)
        if era:
            same_era = era_index[era].copy()
        same_era.discard(pid)

        # Filter to valid IDs, sort, and limit
        result = {
            "person": pid,
            "same_field": sorted(same_field & valid_ids)[:MAX_ENTRIES],
            "same_country": sorted(same_country & valid_ids)[:MAX_ENTRIES],
            "same_era": sorted(same_era & valid_ids)[:MAX_ENTRIES],
        }

        path = os.path.join(OUTPUT_DIR, f"{pid}.json")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
            f.write('\n')
        count += 1

    print(f"\nTotal: {count} relation files generated in generated/links/people/")


if __name__ == '__main__':
    main()
