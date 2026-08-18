import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Wrap render calls in try-catch in setupLanguageSwitcher
old_switcher = '''function setupLanguageSwitcher() {
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
}'''

new_switcher = '''function setupLanguageSwitcher() {
  const langBtns = $$('.lang-btn');
  langBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const lang = btn.dataset.lang;
      setLanguage(lang);
      // Re-render dynamic content after language change (only if data exists)
      if (analysis) {
        try { renderReadiness(); } catch(e) { console.warn('renderReadiness i18n error:', e); }
        try { renderScenarios(); } catch(e) { console.warn('renderScenarios i18n error:', e); }
        try { renderBuyer(); } catch(e) { console.warn('renderBuyer i18n error:', e); }
        try { renderRoadmap(); } catch(e) { console.warn('renderRoadmap i18n error:', e); }
        try { renderReflectionSummary(); } catch(e) { console.warn('renderReflectionSummary i18n error:', e); }
      }
      langBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });
}'''

if old_switcher in content:
    content = content.replace(old_switcher, new_switcher)
    print("✅ Fixed setupLanguageSwitcher")
else:
    print("❌ Could not find exact match for setupLanguageSwitcher")
    # Try to find and replace with a more flexible approach
    # Find the function and replace it
    pattern = r'function setupLanguageSwitcher\(\) \{.*?\n\}'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_switcher + content[match.end():]
        print("✅ Fixed setupLanguageSwitcher (regex)")
    else:
        print("❌ Could not find setupLanguageSwitcher at all")

# Fix 2: Make priorityContent dynamic
old_priority = '''const priorityContent = {
  demand: [t('priorities.demand')[0], t('priorities.demand')[1]],
  economics: [t('priorities.economics')[0], t('priorities.economics')[1]],
  channel: [t('priorities.channel')[0], t('priorities.channel')[1]],
  supply: [t('priorities.supply')[0], t('priorities.supply')[1]],
  marketing: [t('priorities.marketing')[0], t('priorities.marketing')[1]],
  risk: [t('priorities.risk')[0], t('priorities.risk')[1]]
};'''

new_priority = '''function getPriorityContent() {
  return {
    demand: t('priorities.demand'),
    economics: t('priorities.economics'),
    channel: t('priorities.channel'),
    supply: t('priorities.supply'),
    marketing: t('priorities.marketing'),
    risk: t('priorities.risk')
  };
}'''

if old_priority in content:
    content = content.replace(old_priority, new_priority)
    print("✅ Fixed priorityContent")
else:
    print("❌ Could not find exact match for priorityContent")
    # Try regex
    pattern = r'const priorityContent = \{.*?\n\};'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_priority + content[match.end():]
        print("✅ Fixed priorityContent (regex)")
    else:
        print("❌ Could not find priorityContent at all")

# Fix 3: Update renderReadiness to use getPriorityContent() instead of priorityContent
if 'const [title, copy] = priorityContent[weakest.key];' in content:
    content = content.replace(
        'const [title, copy] = priorityContent[weakest.key];',
        'const [title, copy] = getPriorityContent()[weakest.key] || ["", ""];'
    )
    print("✅ Fixed renderReadiness priorityContent reference")

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
