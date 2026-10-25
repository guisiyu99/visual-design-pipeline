#!/usr/bin/env python3
"""Validate required project files and stage artifacts for the Skill."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'SKILL.md', 'README.md', 'docs/工作流.md',
    'templates/brief.md', 'templates/page-map.md',
    'templates/reference-board.md', 'templates/design-spec.md',
    'templates/visual-validation.md', 'templates/review-report.md',
    'templates/design.md', 'templates/lessons.md',
]
missing = [name for name in REQUIRED if not (ROOT / name).is_file()]
header = (ROOT / 'SKILL.md').read_text(encoding='utf-8') if (ROOT / 'SKILL.md').exists() else ''
if not header.startswith('---\n') or 'name: visual-design-pipeline' not in header:
    missing.append('SKILL.md frontmatter')
if missing:
    print('Validation failed:', ', '.join(missing))
    sys.exit(1)
print(f'Validated {len(REQUIRED)} required files and Skill metadata.')
