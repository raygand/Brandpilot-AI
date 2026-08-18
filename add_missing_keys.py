content = open('i18n.js').read()

# Add questionNavLabel to TH section (after buyerAverageText)
content = content.replace(
    "buyerAverageText: '{avg}/100 จาก {count} คำถาม',",
    "    buyerAverageText: '{avg}/100 จาก {count} คำถาม',\n    questionNavLabel: 'คำถาม {n}',"
)

# Add questionNavLabel to EN section
content = content.replace(
    "buyerAverageText: '{avg}/100 from {count} questions',",
    "    buyerAverageText: '{avg}/100 from {count} questions',\n    questionNavLabel: 'Question {n}',"
)

# Add questionNavLabel to ZH section
content = content.replace(
    "buyerAverageText: '{avg}/100 来自 {count} 个问题',",
    "    buyerAverageText: '{avg}/100 来自 {count} 个问题',\n    questionNavLabel: '问题 {n}',"
)

open('i18n.js', 'w').write(content)
print("Added questionNavLabel to all 3 languages")
