"""
Replace the applyTranslations function to use data-i18n attributes for ALL text elements.
This ensures every element with data-i18n="key" gets translated when language changes.
"""

new_apply = '''// Apply all translations to DOM — data-i18n based
window.applyTranslations = function applyTranslations() {
  const data = I18N[currentLang];

  // First: handle all data-i18n attributes (covers ALL static text)
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (!key) return;
    // Support dot notation for nested keys
    const value = key.split('.').reduce((obj, k) => obj?.[k], data);
    if (value !== undefined && value !== null) {
      if (typeof value === 'string') {
        // If element has child elements (like <b>, <span> inside), use textContent on first text node
        const textNodes = Array.from(el.childNodes).filter(n => n.nodeType === 3);
        if (textNodes.length > 0) {
          textNodes[0].textContent = value;
        } else {
          el.textContent = value;
        }
      }
    }
  });

  // Handle nav labels (they have data-i18n but also need array-based updates)
  const navData = ['nav0','nav1','nav2','nav3','nav4','nav5','nav6'];
  const navBtns = document.querySelectorAll('button.nav b');
  navBtns.forEach((el, i) => {
    const key = navData[i];
    if (key && data[key]) el.textContent = data[key];
  });

  // Handle select options with data-i18n
  document.querySelectorAll('select option[data-i18n]').forEach(opt => {
    const key = opt.getAttribute('data-i18n');
    if (key && data[key]) opt.textContent = data[key];
  });

  // Handle elements that need special treatment (innerHTML, aria-label, placeholder)
  if (data.heroTitle && document.getElementById('heroTitle')) {
    document.getElementById('heroTitle').innerHTML = data.heroTitle;
  }
  if (data.heroLead) {
    document.querySelectorAll('.lead').forEach(el => el.innerHTML = data.heroLead);
  }
  if (data.inputDesc) {
    document.querySelectorAll('p[data-i18n="inputSubtitle"]').forEach(el => el.innerHTML = data.inputDesc);
  }
  if (data.reflectionTitle && document.getElementById('reflectionTitle')) {
    document.getElementById('reflectionTitle').innerHTML = data.reflectionTitle;
  }
  if (data.productMeta) {
    document.querySelectorAll('p[data-i18n="productMeta"]').forEach(el => el.innerHTML = data.productMeta);
  }
  if (data.formulaDetails) {
    document.getElementById('formulaDetails').textContent = data.formulaDetails;
  }
  if (data.buyerStrengthDefault && document.getElementById('buyerStrength')) {
    document.getElementById('buyerStrength').textContent = data.buyerStrengthDefault;
  }
  if (data.buyerImproveDefault && document.getElementById('buyerImprove')) {
    document.getElementById('buyerImprove').textContent = data.buyerImproveDefault;
  }
  if (data.disclaimer) {
    document.querySelectorAll('.disclaimer').forEach(el => el.textContent = data.disclaimer);
  }
  if (data.guardrail) {
    document.querySelectorAll('.guardrail').forEach(el => {
      const span = el.querySelector('span');
      el.textContent = span ? data.guardrail : data.guardrail;
      // Re-add span if it was removed
      if (!el.querySelector('span') && data.guardrail.includes('HUMAN')) {
        el.innerHTML = `<span>HUMAN-IN-THE-LOOP</span> ${data.guardrail}`;
      }
    });
  }
  if (data.effectuationNote) {
    document.querySelectorAll('[data-i18n="effectuationNote"]').forEach(el => el.textContent = data.effectuationNote);
  }
  if (data.assumptionNote) {
    document.querySelectorAll('[data-i18n="assumptionNote"]').forEach(el => el.textContent = data.assumptionNote);
  }
  if (data.confidenceValue) {
    document.querySelectorAll('#confidenceValue').forEach(el => el.textContent = data.confidenceValue);
  }
  if (data.readinessTitle && document.getElementById('readinessTitle')) {
    document.getElementById('readinessTitle').innerHTML = data.readinessTitle;
  }
  if (data.scenarioTitle && document.getElementById('scenarioTitle')) {
    document.getElementById('scenarioTitle').innerHTML = data.scenarioTitle;
  }
  if (data.buyerTitle && document.getElementById('buyerTitle')) {
    document.getElementById('buyerTitle').innerHTML = data.buyerTitle;
  }
  if (data.roadmapTitle && document.getElementById('roadmapTitle')) {
    document.getElementById('roadmapTitle').innerHTML = data.roadmapTitle;
  }
  if (data.dialogTitle) {
    document.querySelectorAll('#reasonDialog h3').forEach(el => el.innerHTML = data.dialogTitle);
  }
  if (data.reflectionTitle && document.getElementById('reflectionTitle')) {
    document.getElementById('reflectionTitle').innerHTML = data.reflectionTitle;
  }

  // Handle dynamic content that app.js renders (scenario cards, roadmap, warnings, etc.)
  // These are handled by app.js when rendering, so we just trigger a re-render if needed
  // The key fix is that all STATIC text is now covered by data-i18n
};
'''

# Read the file
with open('i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the applyTranslations function
# It starts at "window.applyTranslations = function" and ends with "export { I18N"
import re

# Find the start of the function
start_idx = content.find('window.applyTranslations = function applyTranslations()')
# Find the end (the export statement)
end_idx = content.find('export { I18N')

if start_idx == -1:
    print("ERROR: Could not find applyTranslations function")
    exit(1)

# Extract everything before and after
before = content[:start_idx]
after = content[end_idx:]

# Build new content
new_content = before + new_apply + after

with open('i18n.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Fixed applyTranslations function (replaced {end_idx - start_idx} chars with {len(new_apply)} chars)")
