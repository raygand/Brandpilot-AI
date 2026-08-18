content = open('app.js').read()

# Fix validation errors (lines 76-81)
content = content.replace(
    "if (state.price <= 0) errors.push('ราคาขายต้องมากกว่า 0');",
    "if (state.price <= 0) errors.push(t('validation.price'));"
)
content = content.replace(
    "if (state.cost < 0) errors.push('ต้นทุนต้องไม่ติดลบ');",
    "if (state.cost < 0) errors.push(t('validation.cost'));"
)
content = content.replace(
    "if (state.budget <= 0) errors.push('กรุณาระบุงบเปิดตัว');",
    "if (state.budget <= 0) errors.push(t('validation.budget'));"
)
content = content.replace(
    "if (state.stock <= 0) errors.push('กรุณาระบุสต็อกเริ่มต้น');",
    "if (state.stock <= 0) errors.push(t('validation.stock'));"
)
content = content.replace(
    "if (state.discount < 0 || state.discount > 60) errors.push('ส่วนลดควรอยู่ระหว่าง 0–60%');",
    "if (state.discount < 0 || state.discount > 60) errors.push(t('validation.discount'));"
)
content = content.replace(
    "if (state.leadTime < 1 || state.leadTime > 365) errors.push('Lead time ควรอยู่ระหว่าง 1–365 วัน');",
    "if (state.leadTime < 1 || state.leadTime > 365) errors.push(t('validation.leadTime'));"
)

# Fix metric bars labels (lines 98-103)
content = content.replace(
    "{ key: 'demand', label: 'หลักฐานความต้องการลูกค้า', score: demand, max: 20 },",
    "{ key: 'demand', label: t('metricLabels.demand'), score: demand, max: 20 },"
)
content = content.replace(
    "{ key: 'economics', label: 'เศรษฐศาสตร์ต่อหน่วย', score: economics, max: 20 },",
    "{ key: 'economics', label: t('metricLabels.economics'), score: economics, max: 20 },"
)
content = content.replace(
    "{ key: 'channel', label: 'ความเหมาะสมของช่องทาง', score: channel, max: 15 },",
    "{ key: 'channel', label: t('metricLabels.channel'), score: channel, max: 15 },"
)
content = content.replace(
    "{ key: 'supply', label: 'ความพร้อมด้านอุปทาน', score: supply, max: 15 },",
    "{ key: 'supply', label: t('metricLabels.supply'), score: supply, max: 15 },"
)
content = content.replace(
    "{ key: 'marketing', label: 'แผนสนับสนุนตลาด', score: marketing, max: 15 },",
    "{ key: 'marketing', label: t('metricLabels.marketing'), score: marketing, max: 15 },"
)
content = content.replace(
    "{ key: 'risk', label: 'ข้อมูล จริยธรรม และความเสี่ยง', score: risk, max: 15 }",
    "{ key: 'risk', label: t('metricLabels.risk'), score: risk, max: 15 }"
)

# Fix liveMargin (line 156)
content = content.replace(
    "$('#liveMargin').textContent = `${state.price ? ((gross / state.price) * 100).toFixed(1) : '0.0'}% ของราคาขาย`;",
    "$('#liveMargin').textContent = `${state.price ? ((gross / state.price) * 100).toFixed(1) : '0.0'}% ${t('liveMarginSuffix')}`;"
)

# Fix inputHint (line 158)
content = content.replace(
    "$('#inputHint').textContent = state.cost >= state.price ? 'คำเตือน: ต้นทุนสูงกว่าหรือเท่าราคาขาย' : `กำไรขั้นต้นก่อนค่าช่องทาง ${money(gross)} ต่อหน่วย`;",
    "$('#inputHint').textContent = state.cost >= state.price ? t('inputHintWarning') : t('inputHintNormal', { money: money(gross) });"
)

# Fix priorityContent (lines 162-167)
content = content.replace(
    "  demand: ['พิสูจน์ความต้องการจริงก่อนเพิ่มสต็อก', 'สัมภาษณ์ลูกค้าเป้าหมายและทำ Paid Test เพื่อเก็บ Conversion กับอัตราซื้อซ้ำ'],",
    "  demand: [t('priorityContent.demandTitle'), t('priorityContent.demandBody')],"
)
content = content.replace(
    "  economics: ['ปรับ Unit Economics ก่อนขยายช่องทาง', 'ทดสอบราคา ต้นทุน และโปรโมชั่นเพื่อให้ Contribution ต่อหน่วยยังเป็นบวก'],",
    "  economics: [t('priorityContent.economicsTitle'), t('priorityContent.economicsBody')],"
)
content = content.replace(
    "  channel: ['ยืนยัน Channel–Product Fit', 'ทดลองกับช่องทางขนาดเล็ก วัด Sell-through และต้นทุนแฝงก่อนเข้าระบบใหญ่'],",
    "  channel: [t('priorityContent.channelTitle'), t('priorityContent.channelBody')],"
)
content = content.replace(
    "  supply: ['ลดความเสี่ยงด้านสต็อกและ Lead time', 'ยืนยัน MOQ แผนเติมสินค้า และ Safety stock กับผู้ผลิตก่อนรับคำสั่งซื้อเพิ่ม'],",
    "  supply: [t('priorityContent.supplyTitle'), t('priorityContent.supplyBody')],"
)
content = content.replace(
    "  marketing: ['สร้าง Demand Plan ที่วัดผลได้', 'จัดสรรงบตาม Funnel และกำหนด CAC, Conversion และจุดหยุดการใช้เงิน'],",
    "  marketing: [t('priorityContent.marketingTitle'), t('priorityContent.marketingBody')],"
)
content = content.replace(
    "  risk: ['กำหนด Guardrail ก่อนตัดสินใจ', 'ระบุสมมติฐาน แหล่งข้อมูล เจ้าของการตัดสินใจ และเกณฑ์ Stop / Iterate / Scale']",
    "  risk: [t('priorityContent.riskTitle'), t('priorityContent.riskBody')]"
)

# Fix questionNav aria-label (line 255)
content = content.replace(
    "aria-label=\"คำถาม ${i + 1}\"",
    "aria-label=\"${t('questionNavLabel', { n: i + 1 })}\""
)

# Fix buyerAverage (line 266)
content = content.replace(
    "$('#buyerAverage').textContent = scored.length ? `${Math.round(scored.reduce((sum, result) => sum + result.total, 0) / scored.length)}/100 จาก ${scored.length} คำถาม` : 'ยังไม่มีคะแนน';",
    "$('#buyerAverage').textContent = scored.length ? t('buyerAverageText', { avg: Math.round(scored.reduce((sum, result) => sum + result.total, 0) / scored.length), count: scored.length }) : t('buyerAverageNone');"
)

# Fix buyerImprove (line 306)
content = content.replace(
    "$('#buyerImprove').textContent = 'ระบบจะประเมินด้วย Rubric ที่เปิดเผยได้';",
    "$('#buyerImprove').textContent = t('buyerImproveDefault');"
)

# Fix buyerQuestions fallback (lines 240-244)
content = content.replace(
    "  { q: 'เหตุใดสินค้านี้จึงควรได้พื้นที่ขาย?', prompt: 'ตอบด้วยปัญหาลูกค้า หลักฐาน และความแตกต่างที่ตรวจสอบได้' },",
    "  { q: t('buyerQuestions.0.q'), prompt: t('buyerQuestions.0.prompt') },"
)
content = content.replace(
    "  { q: 'หากจัดโปรโมชั่นตามแผน ธุรกิจยังมีกำไรหรือไม่?', prompt: 'อธิบายราคาสุทธิ ต้นทุน Contribution และจุดหยุดความเสี่ยง' },",
    "  { q: t('buyerQuestions.1.q'), prompt: t('buyerQuestions.1.prompt') },"
)
content = content.replace(
    "  { q: 'จะทำให้สินค้าขายออกจากชั้นอย่างไร?', prompt: 'ระบุช่องทาง สื่อสนับสนุน KPI และความถี่ในการติดตาม' },",
    "  { q: t('buyerQuestions.2.q'), prompt: t('buyerQuestions.2.prompt') },"
)
content = content.replace(
    "  { q: 'ถ้ายอดขายต่ำกว่าเป้า คุณจะจัดการสต็อกอย่างไร?', prompt: 'แสดง Trigger, Stock cover และแผน Iterate หรือ Stop' },",
    "  { q: t('buyerQuestions.3.q'), prompt: t('buyerQuestions.3.prompt') },"
)
content = content.replace(
    "  { q: 'อีก 90 วัน Buyer ควรเห็นหลักฐานอะไร?', prompt: 'สรุปตัวเลข Go / No-go และผู้รับผิดชอบที่ชัดเจน' }",
    "  { q: t('buyerQuestions.4.q'), prompt: t('buyerQuestions.4.prompt') }"
)

# Fix roadmapTemplates fallback (lines 317-329)
content = content.replace(
    "    ['30', 'Discover', ['สัมภาษณ์ลูกค้าเป้าหมาย 12–15 คน', 'ทดสอบข้อความคุณค่า 2 แบบ', 'ยืนยันต้นทุนและ MOQ'], 'มี Problem–Solution Evidence'],",
    "    ['30', t('roadmapKeys.discover'), [t('roadmapActions.0.0'), t('roadmapActions.0.1'), t('roadmapActions.0.2')], t('roadmapGates.0')],"
)
content = content.replace(
    "    ['60', 'Online Test', ['เปิดขายชุดเล็กใน Online', 'ทดสอบราคา 2 ระดับ', 'ติดตาม Conversion และซื้อซ้ำ'], 'ซื้อซ้ำ ≥ 20%'],",
    "    ['60', t('roadmapKeys.onlineTest'), [t('roadmapActions.1.0'), t('roadmapActions.1.1'), t('roadmapActions.1.2')], t('roadmapGates.1')],"
)
content = content.replace(
    "    ['90', 'Decide', ['สรุป CAC และ Contribution', 'แก้ Product / Offer', 'ตัดสินใจ Pilot หรือ Stop'], 'Evidence before retail']",
    "    ['90', t('roadmapKeys.decide'), [t('roadmapActions.2.0'), t('roadmapActions.2.1'), t('roadmapActions.2.2')], t('roadmapGates.2')]"
)

open('app.js', 'w').write(content)
print("Remaining Thai strings replaced with t() calls")
