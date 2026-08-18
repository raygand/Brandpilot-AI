content = open('app.js').read()

# Fix priorityContent references to use priorities (which is an array object in i18n)
for key in ['demand', 'economics', 'channel', 'supply', 'marketing', 'risk']:
    content = content.replace(
        f"t('priorityContent.{key}Title')",
        f"t('priorities.{key}')[0]"
    )
    content = content.replace(
        f"t('priorityContent.{key}Body')",
        f"t('priorities.{key}')[1]"
    )

# Fix buyerQuestions to use I18N[currentLang] directly (it's an array)
content = content.replace(
    "{ q: t('buyerQuestions.0.q'), prompt: t('buyerQuestions.0.prompt') },",
    "  I18N[currentLang].buyerQuestions[0],"
)
content = content.replace(
    "{ q: t('buyerQuestions.1.q'), prompt: t('buyerQuestions.1.prompt') },",
    "  I18N[currentLang].buyerQuestions[1],"
)
content = content.replace(
    "{ q: t('buyerQuestions.2.q'), prompt: t('buyerQuestions.2.prompt') },",
    "  I18N[currentLang].buyerQuestions[2],"
)
content = content.replace(
    "{ q: t('buyerQuestions.3.q'), prompt: t('buyerQuestions.3.prompt') },",
    "  I18N[currentLang].buyerQuestions[3],"
)
content = content.replace(
    "{ q: t('buyerQuestions.4.q'), prompt: t('buyerQuestions.4.prompt') }",
    "  I18N[currentLang].buyerQuestions[4]"
)

# Fix roadmapTemplates references to use I18N[currentLang] directly
# Replace the t('roadmapKeys.*') and t('roadmapActions.*') and t('roadmapGates.*') patterns
content = content.replace(
    "    ['30', t('roadmapKeys.discover'), [t('roadmapActions.0.0'), t('roadmapActions.0.1'), t('roadmapActions.0.2')], t('roadmapGates.0')],",
    "    ...I18N[currentLang].roadmapTemplates.discover,"
)
content = content.replace(
    "    ['60', t('roadmapKeys.onlineTest'), [t('roadmapActions.1.0'), t('roadmapActions.1.1'), t('roadmapActions.1.2')], t('roadmapGates.1')],",
    "    ...I18N[currentLang].roadmapTemplates.discover,"
)
content = content.replace(
    "    ['90', t('roadmapKeys.decide'), [t('roadmapActions.2.0'), t('roadmapActions.2.1'), t('roadmapActions.2.2')], t('roadmapGates.2')]",
    "    ...I18N[currentLang].roadmapTemplates.discover"
)

open('app.js', 'w').write(content)
print("Fixed references")
