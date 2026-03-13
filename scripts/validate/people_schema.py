#!/usr/bin/env python3
"""Validate all people JSON files against the required schema."""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, '..', '..')
PEOPLE_DIR = os.path.join(PROJECT_ROOT, 'data', 'people')

REQUIRED_FIELDS = [
    'id', 'name', 'birth_year', 'death_year', 'countries', 'fields',
    'overview', 'early_life', 'impact', 'timeline', 'famous_works',
    'quotes', 'relations'
]

LANGS = ['en', 'es', 'pt', 'fr', 'de', 'zh', 'hi', 'ar', 'id', 'ja']

I18N_FIELDS = ['name', 'overview', 'early_life', 'impact']


def validate_person(filepath):
    errors = []
    filename = os.path.basename(filepath)
    expected_id = filename.replace('.json', '')

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return [f'{filename}: invalid JSON - {e}']

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f'{filename}: missing required field "{field}"')

    # Check id matches filename
    if data.get('id') != expected_id:
        errors.append(f'{filename}: id "{data.get("id")}" does not match filename "{expected_id}"')

    # Check i18n fields have all 10 languages
    for field in I18N_FIELDS:
        if field not in data:
            continue
        obj = data[field]
        if not isinstance(obj, dict):
            errors.append(f'{filename}: "{field}" must be an i18n object')
            continue
        for lang in LANGS:
            if lang not in obj:
                errors.append(f'{filename}: "{field}" missing language "{lang}"')

    # Check name has all languages in name
    if 'name' in data and isinstance(data['name'], dict):
        for lang in LANGS:
            if lang not in data['name']:
                errors.append(f'{filename}: "name" missing language "{lang}"')

    # Check arrays
    for field in ['countries', 'fields', 'timeline', 'famous_works', 'quotes', 'relations']:
        if field in data and not isinstance(data[field], list):
            errors.append(f'{filename}: "{field}" must be a list')

    return errors


def main():
    if not os.path.isdir(PEOPLE_DIR):
        print(f'Error: {PEOPLE_DIR} does not exist')
        sys.exit(1)

    all_errors = []
    count = 0

    for filename in sorted(os.listdir(PEOPLE_DIR)):
        if not filename.endswith('.json'):
            continue
        count += 1
        filepath = os.path.join(PEOPLE_DIR, filename)
        errors = validate_person(filepath)
        all_errors.extend(errors)

    print(f'Validated {count} people files.')
    print(f'Errors: {len(all_errors)}')

    if all_errors:
        for e in all_errors[:50]:
            print(f'  - {e}')
        if len(all_errors) > 50:
            print(f'  ... and {len(all_errors) - 50} more errors')
        sys.exit(1)
    else:
        print('All files valid!')


if __name__ == '__main__':
    main()
