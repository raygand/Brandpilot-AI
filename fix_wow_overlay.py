content = open('app.js').read()

# Fix WOW overlay hardcoded strings
content = content.replace(
    "<h2 class=\"wow-title\" id=\"wowTitleText\">กำลังคำนวณกลยุทธ์...</h2>",
    "<h2 class=\"wow-title\" id=\"wowTitleText\">${t('wowTitle')}</h2>"
)
content = content.replace(
    "<p class=\"wow-subtitle\" id=\"wowSubtitleText\">วิเคราะห์ข้อมูลด้วย AI Simulation</p>",
    "<p class=\"wow-subtitle\" id=\"wowSubtitleText\">${t('wowSubtitle')}</p>"
)
content = content.replace(
    "<p class=\"wow-score-label\" id=\"wowScoreLabel\">READINESS SCORE</p>",
    "<p class=\"wow-score-label\" id=\"wowScoreLabel\">${t('wowScore')}</p>"
)
content = content.replace(
    "<button class=\"wow-close\" id=\"wowCloseBtn\" disabled>รอผลการคำนวณ...</button>",
    "<button class=\"wow-close\" id=\"wowCloseBtn\" disabled>${t('wowComputing')}</button>"
)

# Fix strategyText
content = content.replace(
    "const strategyText = analysis \n    ? `กลยุทธ์ที่แนะนำ: <b>${analysis.scenarios.find(s => s.id === analysis.recommended)?.label || 'Balanced Pilot'}</b> — Contribution ${analysis.scenarios.find(s => s.id === analysis.recommended)?.contribution || '฿0'}/หน่วย`\n    : 'กลยุทธ์ที่แนะนำ: <b>Balanced Pilot</b> — ทดสอบช่องทางเล็กก่อนขยาย';",
    "const strategyText = analysis \n    ? t('wowStrategy', { label: analysis.scenarios.find(s => s.id === analysis.recommended)?.label || 'Balanced Pilot', money: money(analysis.scenarios.find(s => s.id === analysis.recommended)?.contribution || 0) })\n    : t('wowFinal') + ': <b>Balanced Pilot</b>';"
)

open('app.js', 'w').write(content)
print("WOW overlay fixed")
