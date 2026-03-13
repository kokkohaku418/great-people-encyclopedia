#!/usr/bin/env python3
"""Orchestrator: run all people_ai batch scripts to generate 900 people."""

import subprocess
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

BATCHES = [
    'people_ai_math.py',
    'people_ai_chemistry.py',
    'people_ai_biology.py',
    'people_ai_philosophy.py',
    'people_ai_politics.py',
    'people_ai_literature.py',
    'people_ai_art.py',
    'people_ai_music.py',
    'people_ai_eng_astro.py',
]


def main():
    total = 0
    for batch in BATCHES:
        path = os.path.join(SCRIPT_DIR, batch)
        if not os.path.exists(path):
            print(f'WARNING: {batch} not found, skipping.')
            continue
        print(f'\n=== Running {batch} ===')
        result = subprocess.run([sys.executable, path], cwd=os.path.join(SCRIPT_DIR, '..', '..'))
        if result.returncode != 0:
            print(f'ERROR: {batch} failed with code {result.returncode}')
            sys.exit(1)

    # Count total
    people_dir = os.path.join(SCRIPT_DIR, '..', '..', 'data', 'people')
    count = len([f for f in os.listdir(people_dir) if f.endswith('.json')])
    print(f'\n=== DONE ===')
    print(f'Total people files: {count}')


if __name__ == '__main__':
    main()
