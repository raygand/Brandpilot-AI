import re

with open('i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Get TH block to use as reference for missing keys
th_start = content.find('  th: {')
en_start = content.find('  en: {')
zh_start = content.find('  zh: {')
export_start = content.find('export {')

th_block = content[th_start:en_start]
en_block = content[en_start:zh_start]
zh_block = content[zh_start:export_start]

# Get TH keys
th_keys = re.findall(r'^    (\w+):', th_block, re.MULTILINE)
en_keys = re.findall(r'^    (\w+):', en_block, re.MULTILINE)
zh_keys = re.findall(r'^    (\w+):', zh_block, re.MULTILINE)

# Find keys in TH but not in EN
en_missing = [k for k in th_keys if k not in en_keys]
zh_missing = [k for k in th_keys if k not in zh_keys]

print(f"TH keys: {len(th_keys)}")
print(f"EN keys: {len(en_keys)}, Missing: {len(en_missing)}")
print(f"ZH keys: {len(zh_keys)}, Missing: {len(zh_missing)}")
print(f"\nEN missing keys: {en_missing}")
print(f"\nZH missing keys: {zh_missing}")
