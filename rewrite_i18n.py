import re

# Read current i18n.js
with open('i18n.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the applyTranslations function and replace it entirely
# The function starts at the line with "window.applyTranslations = function applyTranslations()"
# and ends before "export { I18N, currentLang, setLanguage, t };"

new_apply = '''window.applyTranslations = function applyTranslations() {
  const data = I18N[currentLang];
  if (!data) return;

  // Helper: safely update text content
  function setText(el, value) {
    if (!el || value === undefined || value === null) return;
    if (typeof value !== 'string') return;
    // If value contains HTML tags, use innerHTML
    if (value.includes('<') && value.includes('>')) {
      el.innerHTML = value;
    } else {
      el.textContent = value;
    }
  }

  // === 1. Process ALL data-i18n attributes ===
  document.querySelectorAll('[data-i18n]').forEach(el => {
    try {
      const key = el.getAttribute('data-i18n');
      if (!key) return;

      // Special: nav array (multiple buttons share same key)
      if (key === 'nav') {
        const allNav = Array.from(document.querySelectorAll('button.nav b[data-i18n="nav"]'));
        const idx = allNav.indexOf(el);
        if (idx >= 0 && Array.isArray(data.nav) && data.nav[idx]) {
          el.textContent = data.nav[idx];
        }
        return;
      }

      // Special: heroProof array
      if (key === 'heroProof') {
        const allProof = Array.from(document.querySelectorAll('.hero-proof span[data-i18n="heroProof"]'));
        const idx = allProof.indexOf(el);
        if (idx >= 0 && Array.isArray(data.heroProof) && data.heroProof[idx]) {
          el.textContent = data.heroProof[idx];
        }
        return;
      }

      // Resolve nested key
      let value = data;
      for (const part of key.split('.')) {
        value = value?.[part];
        if (value === undefined) break;
      }
      if (value === undefined || value === null) return;

      // Handle based on element type
      if (el.tagName === 'TEXTAREA' || (el.tagName === 'INPUT' && !['button','submit','reset'].includes(el.type))) {
        el.placeholder = value;
      } else if (el.tagName === 'OPTION') {
        el.textContent = value;
      } else if (typeof value === 'string') {
        setText(el, value);
      }
    } catch (e) {
      console.warn('i18n error for element:', e);
    }
  });

  // === 2. Handle innerHTML elements (preserve <br>, <em>, <b>) ===
  const innerHTMLIds = ['heroTitle', 'reflectionTitle', 'readinessTitle', 'scenarioTitle', 'buyerTitle', 'roadmapTitle', 'productMeta', 'inputDesc'];
  innerHTMLIds.forEach(id => {
    const el = document.getElementById(id);
    if (el && data[id]) {
      try { el.innerHTML = data[id]; } catch(e) { console.warn('innerHTML error:', id, e); }
    }
  });

  // === 3. Special UI elements ===
  const wowBtn = document.getElementById('wowBtn');
  if (wowBtn && data.wowLabel) {
    try { wowBtn.innerHTML = '<i></i>' + data.wowLabel; } catch(e) {}
  }

  const caseChip = document.getElementById('caseChipLabel');
  if (caseChip && data.caseChip) {
    try { caseChip.textContent = data.caseChip; } catch(e) {}
  }

  const modeLabel = document.getElementById('modeLabel');
  if (modeLabel && data.mode) {
    try { modeLabel.textContent = data.mode; } catch(e) {}
  }

  const resetTop = document.getElementById('resetTop');
  if (resetTop && data.resetTop) {
    try { resetTop.textContent = data.resetTop; } catch(e) {}
  }

  // Hero start button
  const heroStart = document.querySelector('.hero .primary[data-next]') || document.querySelector('button.primary[data-next]');
  if (heroStart && data.heroStart) {
    try { heroStart.textContent = data.heroStart; } catch(e) {}
  }

  // Disclaimer
  document.querySelectorAll('.disclaimer').forEach(el => {
    if (data.disclaimer) { try { el.textContent = data.disclaimer; } catch(e) {} }
  });

  // Guardrail
  document.querySelectorAll('.guardrail').forEach(el => {
    if (data.guardrail) {
      try {
        const span = el.querySelector('span');
        if (span) {
          const textNode = Array.from(el.childNodes).find(n => n.nodeType === 3);
          if (textNode) textNode.textContent = ' ' + data.guardrail;
        } else {
          el.innerHTML = '<span>HUMAN-IN-THE-LOOP</span> ' + data.guardrail;
        }
      } catch(e) {}
    }
  });

  // Confidence value
  const confEl = document.getElementById('confidenceValue');
  if (confEl && data.confidenceValues?.medium) {
    try { confEl.textContent = data.confidenceValues.medium; } catch(e) {}
  }

  // Nav aria-labels
  const navBtns = document.querySelectorAll('button.nav');
  if (data.navAria && navBtns.length) {
    navBtns.forEach((el, i) => {
      if (data.navAria[i]) {
        try { el.setAttribute('aria-label', data.navAria[i]); } catch(e) {}
      }
    });
  }
};'''

# Find the old applyTranslations function and replace it
pattern = r'// Apply all translations to DOM[^\n]*\n(?:// Apply all translations to DOM[^\n]*\n)?window\.applyTranslations = function applyTranslations\(\) \{.*?\n\};'
match = re.search(pattern, content, re.DOTALL)

if match:
    content = content[:match.start()] + new_apply + '\n' + content[match.end():]
    print("✅ Replaced applyTranslations function")
else:
    print("❌ Could not find applyTranslations function to replace")
    # Try a broader pattern
    pattern2 = r'window\.applyTranslations = function applyTranslations\(\) \{.*?\n\};'
    match2 = re.search(pattern2, content, re.DOTALL)
    if match2:
        content = content[:match2.start()] + new_apply + '\n' + content[match2.end():]
        print("✅ Replaced applyTranslations (broader pattern)")
    else:
        print("❌ Still couldn't find it")

with open('i18n.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! i18n.js updated.")
