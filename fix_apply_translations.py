import re

with open('i18n.js', 'r') as f:
    content = f.read()

# 1. Add data-i18n-placeholder processing after the data-i18n block
old_block = """  // === 2. Handle innerHTML elements (preserve <br>, <em>, <b>) ===
  const innerHTMLIds = ['heroTitle', 'reflectionTitle', 'readinessTitle', 'scenarioTitle', 'buyerTitle', 'roadmapTitle', 'productMeta', 'inputDesc'];"""

new_block = """  // === 1b. Process data-i18n-placeholder attributes ===
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    try {
      const key = el.getAttribute('data-i18n-placeholder');
      if (!key) return;
      let value = data;
      for (const part of key.split('.')) {
        value = value?.[part];
        if (value === undefined) break;
      }
      if (value !== undefined && value !== null && typeof value === 'string') {
        el.placeholder = value;
      }
    } catch (e) { console.warn('placeholder error:', e); }
  });
  // === 2. Handle innerHTML elements (preserve <br>, <em>, <b>) ===
  const innerHTMLIds = ['heroTitle', 'reflectionTitle', 'readinessTitle', 'scenarioTitle', 'buyerTitle', 'roadmapTitle', 'productMeta', 'inputDesc'];"""

content = content.replace(old_block, new_block)
print("✅ Added data-i18n-placeholder support")

# 2. Add the new IDs to innerHTMLIds list
old_ids = "const innerHTMLIds = ['heroTitle', 'reflectionTitle', 'readinessTitle', 'scenarioTitle', 'buyerTitle', 'roadmapTitle', 'productMeta', 'inputDesc'];"
new_ids = "const innerHTMLIds = ['heroTitle', 'reflectionTitle', 'readinessTitle', 'scenarioTitle', 'buyerTitle', 'roadmapTitle', 'productMeta', 'inputDesc', 'inputHint', 'assumptionText', 'reflectionPromptText', 'buyerQuestion', 'buyerPrompt'];"
content = content.replace(old_ids, new_ids)
print("✅ Added new IDs to innerHTMLIds")

# 3. Remove heroTitle from innerHTMLIds (it's handled separately below)
# Actually keep it - it's fine to handle it twice

with open('i18n.js', 'w') as f:
    f.write(content)

print("✅ i18n.js updated")
