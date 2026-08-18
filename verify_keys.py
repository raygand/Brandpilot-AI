"""Check if all data-i18n keys exist in I18N for all 3 languages."""
import re

# Extract all data-i18n keys from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

keys = set(re.findall(r'data-i18n="([^"]+)"', html))
print(f"Found {len(keys)} unique data-i18n keys in HTML")

# Extract all top-level keys from each language in i18n.js
with open('i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the I18N object
# Extract keys for each language
missing = {}
for lang in ['th', 'en', 'zh']:
    # Find the lang block
    lang_start = content.find(f"{lang}: {{")
    if lang_start == -1:
        missing[lang] = sorted(keys)
        continue
    
    # Get the block until the next language or end
    # Simple approach: extract all keys at the top level
    # Keys are like: key: 'value' or key: { ... }
    block = content[lang_start:content.find('export { I18N')]
    
    lang_missing = []
    for key in keys:
        # Check if key exists as a top-level key in this language block
        # Handle simple keys
        pattern = rf"^\s{{2}}{re.escape(key)}:"
        if re.search(pattern, block, re.MULTILINE):
            continue
        lang_missing.append(key)
    
    missing[lang] = lang_missing

for lang, keys_list in missing.items():
    if keys_list:
        print(f"\n{lang}: {len(keys_list)} missing keys:")
        for k in sorted(keys_list):
            print(f"  - {k}")
    else:
        print(f"\n{lang}: All keys found!")
