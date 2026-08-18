"""
Complete rewrite of applyTranslations to properly handle all data-i18n keys
including nested keys (formLabels.price), array-based keys (nav, heroProof),
and special elements that need innerHTML instead of textContent.
"""

new_apply = '''// Apply all translations to DOM — data-i18n based (FULL COVERAGE)
window.applyTranslations = function applyTranslations() {
  const data = I18N[currentLang];

  // 1. Handle ALL data-i18n attributes with proper nested key resolution
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (!key) return;
    
    // Special handling for nav buttons (use array index)
    if (key === 'nav') {
      const navIdx = Array.from(el.closest('button.nav')?.parentElement?.querySelectorAll('button.nav') || []).indexOf(el.closest('button.nav'));
      if (data.nav && data.nav[navIdx] !== undefined) {
        el.textContent = data.nav[navIdx];
      }
      return;
    }
    
    // Special handling for heroProof items (use array index)
    if (key === 'heroProof') {
      const proofItems = document.querySelectorAll('.hero-proof span');
      const proofIdx = Array.from(proofItems).indexOf(el);
      if (data.heroProof && data.heroProof[proofIdx] !== undefined) {
        el.textContent = data.heroProof[proofIdx];
      }
      return;
    }

    // Resolve nested key (e.g., "formLabels.price" -> data.formLabels.price)
    const value = key.split('.').reduce((obj, k) => obj?.[k], data);
    if (value === undefined || value === null) return;
    
    if (typeof value === 'string') {
      // For textarea placeholders
      if (el.tagName === 'TEXTAREA') {
        el.placeholder = value;
        return;
      }
      // For input placeholders
      if (el.tagName === 'INPUT') {
        el.placeholder = value;
        return;
      }
      // If element has child elements (like <b>, <span>, <em> inside), update first text node
      const textNodes = Array.from(el.childNodes).filter(n => n.nodeType === 3);
      if (textNodes.length > 0) {
        textNodes[0].textContent = value;
      } else {
        el.textContent = value;
      }
    }
  });

  // 2. Handle elements that need innerHTML (preserve <br>, <em>, <b> tags)
  const innerHTMLMap = {
    'heroTitle': 'heroTitle',
    'reflectionTitle': 'reflectionTitle',
    'readinessTitle': 'readinessTitle',
    'scenarioTitle': 'scenarioTitle',
    'buyerTitle': 'buyerTitle',
    'roadmapTitle': 'roadmapTitle',
    'inputSubtitle': 'inputDesc',
    'productMeta': 'productMeta',
    'dialogTitle': 'dialogTitle',
  };
  for (const [elementId, dataKey] of Object.entries(innerHTMLMap)) {
    const el = document.getElementById(elementId);
    if (el && data[dataKey]) {
      el.innerHTML = data[dataKey];
    }
  }
  // Also handle elements with data-i18n that have innerHTML content
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    // Check if the original content had HTML tags (br, em, b)
    const value = key.split('.').reduce((obj, k) => obj?.[k], data);
    if (typeof value === 'string' && (value.includes('<br') || value.includes('<em') || value.includes('<b>'))) {
      el.innerHTML = value;
    }
  });

  // 3. Handle select options with nested keys
  document.querySelectorAll('select option[data-i18n]').forEach(opt => {
    const key = opt.getAttribute('data-i18n');
    const value = key.split('.').reduce((obj, k) => obj?.[k], data);
    if (typeof value === 'string') opt.textContent = value;
  });

  // 4. Handle special UI updates
  // WOW button with icon
  const wowBtn = document.getElementById('wowBtn');
  if (wowBtn && data.wowLabel) {
    wowBtn.innerHTML = `<i></i>${data.wowLabel}`;
  }
  // Case chip
  const caseChip = document.getElementById('caseChipLabel');
  if (caseChip && data.caseChip) caseChip.textContent = data.caseChip;
  // Mode label
  const modeLabel = document.getElementById('modeLabel');
  if (modeLabel && data.mode) modeLabel.textContent = data.mode;
  // Reset button
  const resetTop = document.getElementById('resetTop');
  if (resetTop && data.resetTop) resetTop.textContent = data.resetTop;
  // Hero start button (first .primary[data-next] = hero)
  const heroStart = document.querySelector('.hero .primary[data-next]') || document.querySelector('button.primary[data-next]');
  if (heroStart && data.heroStart) heroStart.textContent = data.heroStart;
  // Disclaimer
  document.querySelectorAll('.disclaimer').forEach(el => {
    if (data.disclaimer) el.textContent = data.disclaimer;
  });
  // Guardrail (has span inside)
  document.querySelectorAll('.guardrail').forEach(el => {
    if (data.guardrail) {
      const span = el.querySelector('span');
      if (span) {
        // Keep the span, update the text after it
        const textNode = Array.from(el.childNodes).find(n => n.nodeType === 3);
        if (textNode) textNode.textContent = ' ' + data.guardrail;
      } else {
        el.innerHTML = `<span>HUMAN-IN-THE-LOOP</span> ${data.guardrail}`;
      }
    }
  });
  // Dialog h3
  document.querySelectorAll('#reasonDialog h3').forEach(el => {
    if (data.dialogTitle) el.innerHTML = data.dialogTitle;
  });
  // Confidence value
  const confEl = document.getElementById('confidenceValue');
  if (confEl && data.confidenceValues?.medium) confEl.textContent = data.confidenceValues.medium;
};
'''

with open('i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the old applyTranslations function
start_idx = content.find('window.applyTranslations = function applyTranslations()')
end_idx = content.find('export { I18N')

if start_idx == -1:
    print("ERROR: Could not find applyTranslations")
    exit(1)

before = content[:start_idx]
after = content[end_idx:]
new_content = before + new_apply + after

with open('i18n.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("applyTranslations rewritten successfully")
