"""Check what keys exist in i18n.js"""
import re

with open('i18n.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_th = False
th_keys = set()
for i, line in enumerate(lines):
    stripped = line.strip()
    if stripped == 'th: {':
        in_th = True
        continue
    if in_th and stripped.startswith('en:'):
        break
    if in_th:
        # Look for pattern: key: 'value' or key: { or key: [
        m = re.match(r'^\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*:', line)
        if m:
            th_keys.add(m.group(1))

print(f"TH keys ({len(th_keys)}):")
for k in sorted(th_keys):
    print(f"  {k}")
