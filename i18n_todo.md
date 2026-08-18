# i18n Bug Fix — BrandPilot AI

## Problem
The `applyTranslations` function in i18n.js only covers SOME text elements. Many hardcoded Thai texts in index.html are NOT covered by any translation key.

## Missing Translation Keys (from index.html)

### Hero (screen 0)
- heroTitle: "ทดลองก่อนลงทุน" + em "เรียนรู้ก่อนเสี่ยงจริง"
- heroLead: "เปลี่ยนข้อมูลสินค้าให้เป็นสถานการณ์จำลอง เพื่อฝึกคิดเรื่องราคา ช่องทาง โปรโมชั่น สต็อก และการนำเสนอ Buyer อย่างมีหลักฐาน"
- heroStart: "เริ่มจำลองสถานการณ์"
- guardrail: "ระบบแสดงสมมติฐานและผลกระทบ ผู้ใช้เป็นผู้ตัดสินใจ"
- heroProof: ["ขั้นตอนตัดสินใจ", "Scenario เปรียบเทียบ", "แผนพร้อมลงมือ"]
- disclaimer: "กรณีศึกษาและตัวเลขทั้งหมดเป็นข้อมูลสมมติสำหรับการเรียนรู้ ไม่ใช่คำแนะนำการลงทุน"

### Screen 1 (Input)
- inputTitle: "เริ่มจากข้อมูลที่ตรวจสอบได้"
- inputSubtitle: "แก้ไขข้อมูลเพื่อดูผลลัพธ์ใหม่ทันที" + "ช่องที่มีเครื่องหมาย * จำเป็นต้องกรอก"
- productMeta: "Ready-to-drink protein beverage" / "330 mL · Protein 25 g"
- liveGrossLabel: "กำไรขั้นต้นก่อนค่าช่องทาง"
- liveMarginSuffix: "ของราคาขาย"
- formLabels: price="ราคาขายปลีก *", cost="ต้นทุนต่อหน่วย *", budget="งบเปิดตัว *", stock="สต็อกเริ่มต้น *", channel="ช่องทางที่สนใจ", discount="ส่วนลดโปรโมชั่น *", evidence="หลักฐานความต้องการ", leadTime="Lead Time สินค้า *"
- selectOptions: "Online Test", "Online + Selected Retail", "Modern Trade Rollout"
- inputHint: "หน่วย: บาท เว้นแต่ระบุเป็นอย่างอื่น"
- analyzeBtn: "วิเคราะห์ความพร้อม"

### Screen 2 (Readiness)
- readinessTitle: "คะแนน...ชี้ว่าควรทดสอบอะไรต่อ" (need to see exact)
- formulaToggle: "ดูวิธีคิดคะแนน"
- formulaContent: "Readiness Score = ผลรวม 6 มิติ..."
- confidenceLabel: "ความเชื่อมั่นของข้อมูล"
- confidenceValue: "ปานกลาง"
- evidenceLabels: "พิสูจน์การซื้อซ้ำ" / "ก่อนเพิ่มสต็อก"
- evidenceTips: "ทดลองกับกลุ่มเป้าหมายขนาดเล็ก..."
- disclaimer2: "คะแนนคำนวณจากข้อมูลที่ผู้ใช้กรอก..."
- formulaLink: "สูตรหลัก"
- formulaFormula: "Contribution/หน่วย = ..."

### Screen 3 (Scenario)
- scenarioTitle: "เปรียบเทียบ 3 ทางเลือก" (need exact)
- scenarioSubtitle: "ยอดขายสูงขึ้น ไม่ได้แปลว่าความเสี่ยงต่ำลง" + "เปลี่ยนข้อมูลหน้าก่อนหน้าได้ตลอดเวลา"
- scenarioKeys: investment="การลงทุน", units="หน่วย", contribution="Contribution", breakeven="จุดคุ้มทุน", risk="ความเสี่ยง"
- scenarioSelected/Select: "เลือกแล้ว" / "เลือก"
- decisionText: "ทางเลือกที่แนะนำ"
- decisionReasons: conservative/balanced/aggressive
- decisionRuleDynamic/Negative
- dialogTitle: "เหตุผลที่ระบบแนะนำ Scenario นี้"
- dialogCopy: "เลือกทางที่ Contribution เป็นบวก..."
- dialogClose: "เข้าใจแล้ว"

### Screen 4 (Buyer)
- buyerTitle: "ซ้อมตอบ Buyer"
- buyerSubtitle: "คำตอบที่ดีต้องมีหลักฐาน..."
- buyerQuestions: q, prompt (5 questions)
- buyerPromptLabel: "เหตุใดสินค้านี้จึงควรได้พื้นที่ขาย?" / "ตอบด้วยปัญหาลูกค้า..."
- charCount: "N ตัวอักษร"
- evaluateBtn: "ประเมินคำตอบ"
- rubricLabels: "จุดแข็ง" / "ควรเพิ่ม"
- buyerStrengthDefault: "พิมพ์คำตอบแล้วกดประเมิน"
- buyerImproveDefault: "ระบบจะประเมินด้วย Rubric..."
- privacyNote: "การประเมินหน้านี้ใช้ Rubric-based evaluator..."
- buyerAverageNone: "ยังไม่มีคะแนน"
- buyerAverageText: "คะแนนเฉลี่ย N/100 จาก N คำตอบ"
- roadmapBtn: "สร้างแผน 90 วัน"

### Screen 5 (Roadmap)
- roadmapTitle: "เปลี่ยนข้อสังเกตให้เป็นการทดลองที่ลงมือได้"
- roadmapLabels: "งบจำลอง" / "Contribution เป้าหมาย" / "จุดตัดสินใจ"
- effectuationNote: "ลงทุนเท่าที่รับความเสียหายได้..."
- reflectionBtn: "สะท้อนการเรียนรู้"

### Screen 6 (Reflection)
- reflectionTitle: "AI จบเมื่อผู้เรียน" + "อธิบายเหตุผลได้"
- reflectionSubtitle: "การสะท้อนผลเปลี่ยน..."
- reflectionQuestions: 3 labels
- reflectionPlaceholders: 3 placeholders
- saveReflectionBtn: "บันทึก Reflection"
- downloadBtn: "ดาวน์โหลดสรุป"
- completeNote: "ข้อมูลจะบันทึกเฉพาะในเบราว์เซอร์เครื่องนี้"
- privacyNote: "Prototype นี้ไม่มี Backend..."
- restartBtn: "เริ่มรอบจำลองใหม่"

### Dialog
- dialogTitle: "เหตุผลที่ระบบแนะนำ Scenario นี้"
- dialogClose: "เข้าใจแล้ว"

### Nav
- nav labels: 7 items (already in i18n)
- navAria labels

## Solution Approach
1. Add `data-i18n` attributes to ALL translatable elements in index.html
2. Update i18n.js to scan for `data-i18n` attributes and apply translations to ALL of them
3. Also handle `placeholder` attributes for textareas
4. Also handle `aria-label` attributes
