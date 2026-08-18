import re

content = open('app.js').read()

# 1. Update import
content = content.replace(
    'import { setLanguage, t } from "./i18n.js";',
    'import { setLanguage, t, I18N, currentLang } from "./i18n.js";'
)

# 2. Replace hardcoded Thai strings in renderReadiness
content = content.replace(
    "$('#confidenceLabel').textContent = confidence;",
    "$('#confidenceLabel').textContent = t('confidenceValues.' + confidence);"
)
# Fix the status labels
content = content.replace(
    "const status = score >= 80 ? ['green', 'PILOT READY'] : score >= 65 ? ['aqua', 'CONTROLLED PILOT'] : score >= 50 ? ['amber', 'NEEDS VALIDATION'] : ['red', 'HIGH UNCERTAINTY'];",
    "const status = score >= 80 ? ['green', t('statusLabels.green')] : score >= 65 ? ['aqua', t('statusLabels.aqua')] : score >= 50 ? ['amber', t('statusLabels.amber')] : ['red', t('statusLabels.red')];"
)
# Fix priorityContent reference
content = content.replace(
    "const [title, copy] = priorityContent[weakest.key];",
    "const [title, copy] = priorityContent[t('nextBestTest')];"
)
# Fix metric bars labels
content = content.replace(
    "$('#metricBars').innerHTML = metrics.map(metric => `<div class=\"metric ${metric.key === weakest.key ? 'weak' : ''}\"><span>${metric.label}</span><b>${metric.score} / ${metric.max}</b><i style=\"--v:${(metric.score / metric.max) * 100}%\"></i></div>`).join('');",
    "$('#metricBars').innerHTML = metrics.map(metric => `<div class=\"metric ${metric.key === weakest.key ? 'weak' : ''}\"><span>${t('metricLabels.' + metric.key)}</span><b>${metric.score} / ${metric.max}</b><i style=\"--v:${(metric.score / metric.max) * 100}%\"></i></div>`).join('');"
)
# Fix warnings
content = content.replace(
    "if (grossMarginRate < .4) warnings.push(['margin', `Gross margin ${percent(grossMarginRate)} อาจไม่พอรองรับ GP และโปรโมชั่น`]);\n  else warnings.push(['good', `Gross margin ก่อนค่าช่องทาง ${percent(grossMarginRate)} มีพื้นที่ให้ทดสอบ`]);",
    "if (grossMarginRate < .4) warnings.push(['margin', t('warnings.marginBad', { percent: percent(grossMarginRate) })]);\n  else warnings.push(['good', t('warnings.marginGood', { percent: percent(grossMarginRate) })]);"
)
content = content.replace(
    "if (budgetPerUnit < 20) warnings.push(['budget', `งบต่อสต็อก ${money(budgetPerUnit)} ต่ำ ควรเลือก Pilot ที่แคบลง`]);",
    "if (budgetPerUnit < 20) warnings.push(['budget', t('warnings.budget', { money: money(budgetPerUnit) })]);"
)
content = content.replace(
    "if (state.leadTime > 45) warnings.push(['supply', `Lead time ${number(state.leadTime)} วัน เพิ่มความเสี่ยง Out-of-stock`]);",
    "if (state.leadTime > 45) warnings.push(['supply', t('warnings.supply', { days: number(state.leadTime) })]);"
)
content = content.replace(
    "if (state.discount > 25) warnings.push(['discount', `ส่วนลด ${state.discount}% กด Contribution ต่อหน่วยอย่างมีนัยสำคัญ`]);",
    "if (state.discount > 25) warnings.push(['discount', t('warnings.discount', { percent: state.discount })]);"
)

# 3. Replace hardcoded strings in renderScenarios
content = content.replace(
    "<div class=\"key\"><span>เงินลงทุนจำลอง</span><strong>${money(item.investment)}</strong></div>",
    "<div class=\"key\"><span>${t('scenarioKeys.investment')}</span><strong>${money(item.investment)}</strong></div>"
)
content = content.replace(
    "<div class=\"key\"><span>ยอดขายสมมติ</span><strong>${number(item.units)} <small>units</small></strong></div>",
    "<div class=\"key\"><span>${t('scenarioKeys.units')}</span><strong>${number(item.units)} <small>units</small></strong></div>"
)
content = content.replace(
    "<div class=\"key ${contributionClass}\"><span>Contribution / หน่วย</span><strong>${money(item.contribution)}</strong></div>",
    "<div class=\"key ${contributionClass}\"><span>${t('scenarioKeys.contribution')}</span><strong>${money(item.contribution)}</strong></div>"
)
content = content.replace(
    "<div class=\"key\"><span>Break-even</span><strong>${Number.isFinite(item.breakEvenUnits) ? number(item.breakEvenUnits) : 'ไม่ถึงจุดคุ้มทุน'} <small>${Number.isFinite(item.breakEvenUnits) ? 'units' : ''}</small></strong></div>",
    "<div class=\"key\"><span>${t('scenarioKeys.breakeven')}</span><strong>${Number.isFinite(item.breakEvenUnits) ? number(item.breakEvenUnits) : t('breakevenLabel')} <small>${Number.isFinite(item.breakEvenUnits) ? 'units' : ''}</small></strong></div>"
)
content = content.replace(
    "<div class=\"risk ${item.risk.toLowerCase()}\"><i></i><span>ความเสี่ยงรวม</span><b>${item.risk}</b></div>",
    "<div class=\"risk ${item.risk.toLowerCase()}\"><i></i><span>${t('scenarioKeys.risk')}</span><b>${item.risk}</b></div>"
)
content = content.replace(
    "${selected ? 'เลือกแล้ว' : 'เลือก Scenario นี้'}",
    "${selected ? t('scenarioSelected') : t('scenarioSelect')}"
)
# Fix decisionReasons
content = content.replace(
    "const reasons = {\n    conservative: 'ใช้เงินน้อยที่สุด เหมาะเมื่อหลักฐานยังจำกัดหรือ Unit Economics ยังเปราะบาง',\n    balanced: 'สมดุลระหว่างการเรียนรู้ เงินลงทุน และการทดสอบร้านค้าจริง',\n    aggressive: 'เหมาะเมื่อมี Paid Pilot หลักฐานสูง และ Contribution รองรับค่าใช้จ่ายช่องทางใหญ่'\n  };",
    "const reasons = {\n    conservative: t('decisionReasons.conservative'),\n    balanced: t('decisionReasons.balanced'),\n    aggressive: t('decisionReasons.aggressive')\n  };"
)
# Fix decisionRule
content = content.replace(
    "$('#decisionRule').textContent = selected.contribution > 0 ? `Contribution ${money(selected.contribution)}/หน่วย · ตั้งเกณฑ์ Stop หากต่ำกว่า ${money(Math.max(8, selected.contribution * .75))}` : 'Contribution ติดลบ ควรกลับไปปรับราคา ต้นทุน หรือโปรโมชั่น';",
    "$('#decisionRule').textContent = selected.contribution > 0 ? t('decisionRuleDynamic', { money: money(selected.contribution), money2: money(Math.max(8, selected.contribution * .75)) }) : t('decisionRuleNegative');"
)

# 4. Replace buyerQuestions reference
content = content.replace(
    "const buyerQuestions = [",
    "// buyerQuestions moved to i18n.js\nconst buyerQuestions = I18N[currentLang].buyerQuestions || ["
)

# 5. Replace roadmapTemplates reference  
content = content.replace(
    "const roadmapTemplates = {",
    "// roadmapTemplates moved to i18n.js\nconst roadmapTemplates = I18N[currentLang].roadmapTemplates || {"
)

# 6. Fix renderBuyerScore
content = content.replace(
    "if (score.evidence >= 22) strengths.push('ใช้หลักฐานและตัวเลขช่วยให้ตรวจสอบคำตอบได้'); else improvements.push('เพิ่มตัวเลขหรือหลักฐานจากการทดลอง');",
    "if (score.evidence >= 22) strengths.push(t('rubricFeedback.evidenceHigh')); else improvements.push(t('rubricFeedback.evidenceLow'));"
)
content = content.replace(
    "if (score.economics >= 18) strengths.push('เชื่อมคำตอบกับ Unit Economics'); else improvements.push('แสดงราคา ต้นทุน GP และ Contribution');",
    "if (score.economics >= 18) strengths.push(t('rubricFeedback.economicsHigh')); else improvements.push(t('rubricFeedback.economicsLow'));"
)
content = content.replace(
    "if (score.risk >= 7) strengths.push('มีเกณฑ์ควบคุมความเสี่ยง'); else improvements.push('ระบุ Trigger สำหรับ Stop / Iterate / Scale');",
    "if (score.risk >= 7) strengths.push(t('rubricFeedback.riskHigh')); else improvements.push(t('rubricFeedback.riskLow'));"
)
content = content.replace(
    "if (score.clarity < 14) improvements.push('จัดคำตอบเป็น เหตุผล–หลักฐาน–การตัดสินใจ');",
    "if (score.clarity < 14) improvements.push(t('rubricFeedback.clarityLow'));"
)
content = content.replace(
    "$('#buyerStrength').textContent = strengths.length ? strengths.join(' · ') : 'เริ่มตอบตรงคำถามแล้ว';",
    "$('#buyerStrength').textContent = strengths.length ? strengths.join(' · ') : t('buyerStrengthDefault');"
)
content = content.replace(
    "$('#buyerImprove').textContent = improvements.length ? improvements.join(' · ') : 'คำตอบครบองค์ประกอบ ลองทำให้กระชับขึ้น';",
    "$('#buyerImprove').textContent = improvements.length ? improvements.join(' · ') : t('buyerImproveDefault');"
)

# 7. Fix resetBuyerFeedback
content = content.replace(
    "$('#buyerStrength').textContent = 'พิมพ์คำตอบแล้วกดประเมิน';",
    "$('#buyerStrength').textContent = t('buyerStrengthDefault');"
)
content = content.replace(
    "$('#buyerImprove').textContent = 'ระบบจะประเมินด้วย Rubric ที่เผยแพร่ได้';",
    "$('#buyerImprove').textContent = t('buyerImproveDefault');"
)

# 8. Fix updateAnswerCount
content = content.replace(
    "$('#answerCount').textContent = `${$('#buyerAnswer').value.length} ตัวอักษร`;",
    "$('#answerCount').textContent = t('charCount', { count: $('#buyerAnswer').value.length });"
)

# 9. Fix evaluate min chars warning
content = content.replace(
    "$('#buyerImprove').textContent = 'กรุณาอธิบายอย่างน้อย 20 ตัวอักษร เพื่อให้ Rubric ประเมินได้';",
    "$('#buyerImprove').textContent = t('minCharsWarning');"
)

# 10. Fix renderRoadmap
content = content.replace(
    "$('#roadmapContribution').textContent = `${money(selected.contribution)}/หน่วย`;",
    "$('#roadmapContribution').textContent = `${money(selected.contribution)}/${t('wowUnit')}`;"
)
content = content.replace(
    "$('#roadmapGate').textContent = selected.contribution > 0 ? 'Pilot / Iterate / Stop' : 'Fix Economics / Stop';",
    "$('#roadmapGate').textContent = selected.contribution > 0 ? t('roadmapGatePositive') : t('roadmapGateNegative');"
)

# 11. Fix renderReflectionSummary
content = content.replace(
    "$('#reflectionScore').textContent = `Readiness ${analysis.readiness.score}/100 · Contribution ${money(selected.contribution)}/หน่วย`;",
    "$('#reflectionScore').textContent = t('reflectionScore', { score: analysis.readiness.score, money: money(selected.contribution) });"
)

# 12. Fix saveReflection
content = content.replace(
    "$('b', complete).textContent = 'REFLECTION SAVED';",
    "$('b', complete).textContent = t('reflectionSaved');"
)
content = content.replace(
    "$('span', complete).textContent = 'บันทึกสำเร็จในเบราว์เซอร์เครื่องนี้';",
    "$('span', complete).textContent = t('reflectionSavedText');"
)

# 13. Fix dialog
content = content.replace(
    "$('#reasonDialogCopy').textContent = selected.id === analysis.recommended\n      ? `${selected.label} เหมาะกับ Readiness ${analysis.readiness.score}/100 และให้ Contribution ${money(selected.contribution)}/หน่วย ภายใต้ความเสี่ยง ${selected.risk}. ระบบใช้หลักฐาน ความพร้อม และ Unit Economics ประกอบกัน แต่ผู้ใช้ยังเป็นผู้ตัดสินใจสุดท้าย`\n      : `คุณเลือก ${selected.label} ขณะที่ระบบแนะนำ ${recommended.label}. ตัวเลือกของคุณให้ Contribution ${money(selected.contribution)}/หน่วยและมีความเสี่ยง ${selected.risk}. ควรกำหนดเกณฑ์ Stop ให้ชัดเจนก่อนทดลอง`;",
    "$('#reasonDialogCopy').textContent = selected.id === analysis.recommended\n      ? t('dialogRecommended', { label: selected.label, score: analysis.readiness.score, money: money(selected.contribution), risk: selected.risk })\n      : t('dialogAlternative', { selected: selected.label, recommended: recommended.label, money: money(selected.contribution), risk: selected.risk });"
)

# 14. Fix formulaToggle
content = content.replace(
    "event.currentTarget.textContent = open ? 'ซ่อนวิธีคิดคะแนน' : 'ดูวิธีคิดคะแนน';",
    "event.currentTarget.textContent = open ? t('formulaToggleClose') : t('formulaToggleOpen');"
)

# 15. Fix resetSimulation confirm
content = content.replace(
    "const confirmed = window.confirm('เริ่มรอบใหม่และล้างข้อมูลที่บันทึกไว้ในเบราว์เซอร์หรือไม่?');",
    "const confirmed = window.confirm(t('resetConfirm'));"
)

# 16. Fix WOW overlay - replace hardcoded Thai strings
content = content.replace(
    "<p class=\"wow-eyebrow\">AI STRATEGY ENGINE</p>",
    "<p class=\"wow-eyebrow\" id=\"wowEyebrowText\">AI STRATEGY ENGINE</p>"
)
content = content.replace(
    "<h2 class=\"wow-title\" id=\"wowTitleText\">กำลังคำนวณยุทธศาสตร์...</h2>",
    "<h2 class=\"wow-title\" id=\"wowTitleText\">${t('wowTitle')}</h2>"
)
content = content.replace(
    "<p class=\"wow-subtitle\">วิเคราะห์ข้อมูลด้วย AI Simulation</p>",
    "<p class=\"wow-subtitle\">${t('wowSubtitle')}</p>"
)
content = content.replace(
    "<p class=\"wow-score-label\">READINESS SCORE</p>",
    "<p class=\"wow-score-label\">${t('wowScore')}</p>"
)
content = content.replace(
    "<button class=\"wow-close\" id=\"wowCloseBtn\" disabled>กำลังคำนวณ...</button>",
    "<button class=\"wow-close\" id=\"wowCloseBtn\" disabled>${t('wowComputing')}</button>"
)
content = content.replace(
    "กลยุทธ์ที่แนะนำ: <b>Balanced Pilot</b> — Contribution ฿0/หน่วย",
    "${t('wowFinal')}: <b>Balanced Pilot</b>"
)

# Fix the wowStrategy text that uses analysis
content = content.replace(
    "const wowStrategy = analysis \n      ? `ยุทธศาสตร์: <b>${analysis.scenarios.find(s => s.id === analysis.recommended)?.label || 'Balanced Pilot'}</b> — Contribution ${analysis.scenarios.find(s => s.id === analysis.recommended)?.contribution || '฿0'}/หน่วย`\n      : `ยุทธศาสตร์: <b>Balanced Pilot</b>`;",
    "const wowStrategy = analysis \n      ? t('wowStrategy', { label: analysis.scenarios.find(s => s.id === analysis.recommended)?.label || 'Balanced Pilot', money: money(analysis.scenarios.find(s => s.id === analysis.recommended)?.contribution || 0) })\n      : t('wowFinal') + ': <b>Balanced Pilot</b>';"
)

# Fix closeBtn
content = content.replace(
    "closeBtn.textContent = 'ปิด ✕';",
    "closeBtn.textContent = t('wowClose');"
)

open('app.js', 'w').write(content)
print(f"app.js fixed. Lines: {len(content.split(chr(10)))}")
