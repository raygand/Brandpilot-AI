content = open('app.js').read()

old = """// buyerQuestions moved to i18n.js
const buyerQuestions = I18N[currentLang].buyerQuestions || [
    I18N[currentLang].buyerQuestions[0],
    I18N[currentLang].buyerQuestions[1],
    I18N[currentLang].buyerQuestions[2],
    I18N[currentLang].buyerQuestions[3],
    I18N[currentLang].buyerQuestions[4]
];"""

new = """// buyerQuestions moved to i18n.js
function getBuyerQuestions() { return I18N[currentLang].buyerQuestions; }"""

content = content.replace(old, new)

# Fix all usages of buyerQuestions to use the function
content = content.replace("buyerQuestions.length", "getBuyerQuestions().length")
content = content.replace("buyerQuestions[index]", "getBuyerQuestions()[index]")
content = content.replace("buyerQuestions.map", "getBuyerQuestions().map")

open('app.js', 'w').write(content)
print("Fixed buyerQuestions reference")
