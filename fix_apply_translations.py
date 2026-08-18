content = open('i18n.js').read()

# Fix key name mismatches
content = content.replace(
    "guardrail.textContent = data.heroGuardrail || '';",
    "guardrail.textContent = data.guardrail || '';"
)
content = content.replace(
    "proofItems.forEach((el, i) => { if (data.heroProof && data.heroProof[i]) el.textContent = data.heroProof[i]; });",
    "proofItems.forEach((el, i) => { if (data.heroProof && data.heroProof[i]) el.textContent = data.heroProof[i]; });"
)

# Also need to add I18N and currentLang references - they're in module scope
# The function uses I18N and currentLang which are module-scoped vars, so that's fine
# But we need to make sure setLanguage calls applyTranslations correctly

open('i18n.js', 'w').write(content)
print("Fixed applyTranslations key references")
