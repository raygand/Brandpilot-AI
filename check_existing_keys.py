"""Check what keys actually exist in the i18n.js translations."""
import re

with open('i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all top-level keys in the TH block
th_start = content.find('th: {')
th_end = content.find('en: {')
th_block = content[th_start:th_end]

# Extract top-level keys (lines that start with 2 spaces + key + colon)
keys = re.findall(r'^  ([a-zA-Z_][a-zA-Z0-9_]*)\s*:', th_block, re.MULTILINE)
print(f"TH top-level keys ({len(keys)}):")
for k in sorted(set(keys)):
    print(f"  {k}")
