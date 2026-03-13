"""Shared helper for people_ai batch scripts."""
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, '..', '..')
PEOPLE_DIR = os.path.join(PROJECT_ROOT, 'data', 'people')
LANGS = ["en", "es", "pt", "fr", "de", "zh", "hi", "ar", "id", "ja"]


def i18n(en="", ja=""):
    d = {lang: "" for lang in LANGS}
    d["en"] = en
    if ja:
        d["ja"] = ja
    return d


def person(id, name_en, name_ja, birth, death, countries, fields,
           overview, early_life, impact, timeline, works, quotes, relations=None):
    return {
        "id": id,
        "name": i18n(name_en, name_ja),
        "birth_year": birth,
        "death_year": death,
        "countries": countries,
        "fields": fields,
        "overview": i18n(overview),
        "early_life": i18n(early_life),
        "impact": i18n(impact),
        "timeline": [
            {"year": y, "event": i18n(e)} for y, e in timeline
        ],
        "famous_works": [
            {"title": i18n(t), "year": y, "description": i18n(d)}
            for t, y, d in works
        ],
        "quotes": [
            {"text": i18n(t), "source": s} for t, s in quotes
        ],
        "relations": relations or []
    }


def write_people(people_list):
    os.makedirs(PEOPLE_DIR, exist_ok=True)
    count = 0
    skipped = 0
    for p in people_list:
        path = os.path.join(PEOPLE_DIR, f"{p['id']}.json")
        if os.path.exists(path):
            skipped += 1
            continue
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(p, f, ensure_ascii=False, indent=2)
            f.write('\n')
        count += 1
    print(f"Created {count} files, skipped {skipped} existing.")
    return count
