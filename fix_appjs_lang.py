"""
Fix app.js to re-render dynamic content when language changes.
After setLanguage() and applyTranslations(), we need to also re-render
all the dynamic screens (scenarios, buyer, roadmap, etc.)
"""

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the language switcher setup to also re-render dynamic content
old_lang = """function setupLanguageSwitcher() {
  const langBtns = $$('.lang-btn');
  langBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const lang = btn.dataset.lang;
      setLanguage(lang);
      langBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });
}"""

new_lang = """function setupLanguageSwitcher() {
  const langBtns = $$('.lang-btn');
  langBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const lang = btn.dataset.lang;
      setLanguage(lang);
      // Re-render dynamic content after language change
      renderReadiness();
      renderScenarios();
      renderBuyer();
      renderRoadmap();
      renderReflectionSummary();
      langBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });
}"""

if old_lang in content:
    content = content.replace(old_lang, new_lang)
    print("Fixed language switcher in app.js — added re-render calls")
else:
    print("WARNING: Could not find exact match for language switcher")
    # Try to find it with slight variations
    import re
    # Find the function
    match = re.search(r'function setupLanguageSwitcher\(\)', content)
    if match:
        print("Found setupLanguageSwitcher at position", match.start())

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
