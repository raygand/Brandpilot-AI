"""
Fix language switcher to cover ALL text elements by adding data-i18n attributes
to index.html and updating i18n.js to handle them dynamically.
"""

# Step 1: Update index.html — add data-i18n attributes to all translatable text
# We'll do regex replacements on specific patterns

html_replacements = [
    # Hero section
    (r'<p class="eyebrow">DECISION SIMULATION LAB</p>', '<p class="eyebrow" data-i18n="heroEyebrow">DECISION SIMULATION LAB</p>'),
    # Nav labels
    (r'<button class="nav active" data-screen="0" aria-label="ภาพรวม" aria-current="step"><span>01</span><b>เริ่มต้น</b></button>',
     r'<button class="nav active" data-screen="0" aria-label="ภาพรวม" aria-current="step"><span>01</span><b data-i18n="nav0">เริ่มต้น</b></button>'),
    (r'<button class="nav" data-screen="1" aria-label="กรอกข้อมูล"><span>02</span><b>ข้อมูล</b></button>',
     r'<button class="nav" data-screen="1" aria-label="กรอกข้อมูล"><span>02</span><b data-i18n="nav1">ข้อมูล</b></button>'),
    (r'<button class="nav" data-screen="2" aria-label="ความพร้อม"><span>03</span><b>คะแนน</b></button>',
     r'<button class="nav" data-screen="2" aria-label="ความพร้อม"><span>03</span><b data-i18n="nav2">คะแนน</b></button>'),
    (r'<button class="nav" data-screen="3" aria-label="สถานการณ์"><span>04</span><b>ทางเลือก</b></button>',
     r'<button class="nav" data-screen="3" aria-label="สถานการณ์"><span>04</span><b data-i18n="nav3">ทางเลือก</b></button>'),
    (r'<button class="nav" data-screen="4" aria-label="ผู้ซื้อ"><span>05</span><b>Buyer</b></button>',
     r'<button class="nav" data-screen="4" aria-label="ผู้ซื้อ"><span>05</span><b data-i18n="nav4">Buyer</b></button>'),
    (r'<button class="nav" data-screen="5" aria-label="แผน 90 วัน"><span>06</span><b>Roadmap</b></button>',
     r'<button class="nav" data-screen="5" aria-label="แผน 90 วัน"><span>06</span><b data-i18n="nav5">Roadmap</b></button>'),
    (r'<button class="nav" data-screen="6" aria-label="Reflection"><span>07</span><b>ทบทวน</b></button>',
     r'<button class="nav" data-screen="6" aria-label="Reflection"><span>07</span><b data-i18n="nav6">ทบทวน</b></button>'),
    # Topbar
    (r'<span id="caseChipLabel">Simulation case</span>', '<span id="caseChipLabel" data-i18n="caseChipLabel">Simulation case</span>'),
    (r'<button class="ghost top-reset" id="resetTop" type="button">เริ่มใหม่</button>', '<button class="ghost top-reset" id="resetTop" type="button" data-i18n="resetTop">เริ่มใหม่</button>'),
    (r'<button class="wow-btn" id="wowBtn" type="button">✨ WOW</button>', '<button class="wow-btn" id="wowBtn" type="button" data-i18n="wowLabel">✨ WOW</button>'),
    (r'<div class="mode" id="modeLabel">LEARNING MODE</div>', '<div class="mode" id="modeLabel" data-i18n="modeLabel">LEARNING MODE</div>'),
    # Hero
    (r'<p class="lead">เปลี่ยนข้อมูลสินค้า', '<p class="lead" data-i18n="heroLead">เปลี่ยนข้อมูลสินค้า'),
    (r'<button class="primary" data-next type="button">เริ่มจำลองสถานการณ์</button>', '<button class="primary" data-next type="button" data-i18n="heroStart">เริ่มจำลองสถานการณ์</button>'),
    (r'<div class="guardrail"><span>HUMAN-IN-THE-LOOP</span> ระบบแสดงสมมติฐานและผลกระทบ', '<div class="guardrail" data-i18n="guardrail"><span>HUMAN-IN-THE-LOOP</span> ระบบแสดงสมมติฐานและผลกระทบ'),
    # Hero proof
    (r'<div><strong>7</strong><span>ขั้นตอนตัดสินใจ</span></div>', '<div><strong>7</strong><span data-i18n="heroProof0">ขั้นตอนตัดสินใจ</span></div>'),
    (r'<div><strong>3</strong><span>Scenario เปรียบเทียบ</span></div>', '<div><strong>3</strong><span data-i18n="heroProof1">Scenario เปรียบเทียบ</span></div>'),
    (r'<div><strong>1</strong><span>แผนพร้อมลงมือ</span></div>', '<div><strong>1</strong><span data-i18n="heroProof2">แผนพร้อมลงมือ</span></div>'),
    # Disclaimer
    (r'<div class="disclaimer">กรณีศึกษาและตัวเลขทั้งหมด', '<div class="disclaimer" data-i18n="disclaimer">กรณีศึกษาและตัวเลขทั้งหมด'),
    # Screen 1 title
    (r'<h2 id="inputTitle">เริ่มจากข้อมูลที่ตรวจสอบได้</h2>', '<h2 id="inputTitle" data-i18n="inputTitle">เริ่มจากข้อมูลที่ตรวจสอบได้</h2>'),
    (r'<p>แก้ไขข้อมูลเพื่อดูผลลัพธ์ใหม่ทันที<br/>ช่องที่มีเครื่องหมาย \* จำเป็นต้องกรอก</p>', '<p data-i18n="inputSubtitle">แก้ไขข้อมูลเพื่อดูผลลัพธ์ใหม่ทันที<br/>ช่องที่มีเครื่องหมาย * จำเป็นต้องกรอก</p>'),
    # Product meta
    (r'<p>Ready-to-drink protein beverage<br/>330 mL · Protein 25 g</p>', '<p data-i18n="productMeta">Ready-to-drink protein beverage<br/>330 mL · Protein 25 g</p>'),
    # Live economics
    (r'<span>กำไรขั้นต้นก่อนค่าช่องทาง</span>', '<span data-i18n="liveGrossLabel">กำไรขั้นต้นก่อนค่าช่องทาง</span>'),
    (r'<small id="liveMargin">60.8% ของราคาขาย</small>', '<small id="liveMargin" data-i18n="liveMarginSuffix">60.8% ของราคาขาย</small>'),
    # Form labels
    (r'<label for="price">ราคาขายปลีก \*</label>', '<label for="price" data-i18n="formLabelPrice">ราคาขายปลีก *</label>'),
    (r'<label for="cost">ต้นทุนต่อหน่วย \*</label>', '<label for="cost" data-i18n="formLabelCost">ต้นทุนต่อหน่วย *</label>'),
    (r'<label for="budget">งบเปิดตัว \*</label>', '<label for="budget" data-i18n="formLabelBudget">งบเปิดตัว *</label>'),
    (r'<label for="stock">สต็อกเริ่มต้น \*</label>', '<label for="stock" data-i18n="formLabelStock">สต็อกเริ่มต้น *</label>'),
    (r'<label for="channel">ช่องทางที่สนใจ</label>', '<label for="channel" data-i18n="formLabelChannel">ช่องทางที่สนใจ</label>'),
    (r'<label for="discount">ส่วนลดสูงสุดที่รับได้ \*</label>', '<label for="discount" data-i18n="formLabelDiscount">ส่วนลดสูงสุดที่รับได้ *</label>'),
    (r'<label for="evidence">หลักฐานความต้องการลูกค้า</label>', '<label for="evidence" data-i18n="formLabelEvidence">หลักฐานความต้องการลูกค้า</label>'),
    (r'<label for="leadTime">Lead time การผลิต \*</label>', '<label for="leadTime" data-i18n="formLabelLeadTime">Lead time การผลิต *</label>'),
    # Form units
    (r'<span id="priceUnit">บาท</span>', '<span id="priceUnit" data-i18n="unitBaht">บาท</span>'),
    (r'<span id="costUnit">บาท</span>', '<span id="costUnit" data-i18n="unitBaht">บาท</span>'),
    (r'<span id="budgetUnit">บาท</span>', '<span id="budgetUnit" data-i18n="unitBaht">บาท</span>'),
    (r'<span id="stockUnit">หน่วย</span>', '<span id="stockUnit" data-i18n="unitUnit">หน่วย</span>'),
    (r'<span id="discountUnit">%</span>', '<span id="discountUnit" data-i18n="unitPercent">%</span>'),
    (r'<span id="leadUnit">วัน</span>', '<span id="leadUnit" data-i18n="unitDay">วัน</span>'),
    # Select options
    (r'<option value="online">Online Test</option>', '<option value="online" data-i18n="selectOnline">Online Test</option>'),
    (r'<option value="balanced" selected>Online \+ Selected Retail</option>', '<option value="balanced" selected data-i18n="selectBalanced">Online + Selected Retail</option>'),
    (r'<option value="modern">Modern Trade Rollout</option>', '<option value="modern" data-i18n="selectModern">Modern Trade Rollout</option>'),
    # Evidence options
    (r'<option value="idea">มีเพียงสมมติฐาน</option>', '<option value="idea" data-i18n="evidenceIdea">มีเพียงสมมติฐาน</option>'),
    (r'<option value="interviews" selected>มีผลสัมภาษณ์ลูกค้า</option>', '<option value="interviews" selected data-i18n="evidenceInterviews">มีผลสัมภาษณ์ลูกค้า</option>'),
    (r'<option value="pilot">มีข้อมูล Paid Pilot</option>', '<option value="pilot" data-i18n="evidencePilot">มีข้อมูล Paid Pilot</option>'),
    # Input hint
    (r'<span id="inputHint">ระบบจะแสดงสูตรและเตือน</span>', '<span id="inputHint" data-i18n="inputHint">ระบบจะแสดงสูตรและเตือน</span>'),
    # Analyze button
    (r'<button class="primary" id="analyze" type="button">วิเคราะห์ความพร้อม</button>', '<button class="primary" id="analyze" type="button" data-i18n="analyzeBtn">วิเคราะห์ความพร้อม</button>'),
    # Back buttons (all of them)
    (r'<button class="ghost" data-back type="button">ย้อนกลับ</button>', '<button class="ghost" data-back type="button" data-i18n="backBtn">ย้อนกลับ</button>'),
    # Screen 2 readiness
    (r'<h2 id="readinessTitle">คะแนน <span id="scoreHeadline">64</span> ชี้ว่าควรทดสอบอะไรต่อ</h2>', '<h2 id="readinessTitle" data-i18n="readinessTitle">คะแนน <span id="scoreHeadline">64</span> ชี้ว่าควรทดสอบอะไรต่อ</h2>'),
    (r'<span>ความเชื่อมั่นของข้อมูล</span>', '<span data-i18n="confidenceLabel">ความเชื่อมั่นของข้อมูล</span>'),
    (r'<strong id="confidenceLabel">ปานกลาง</strong>', '<strong id="confidenceValue" data-i18n="confidenceValue">ปานกลาง</strong>'),
    (r'<h3 id="priorityTitle">พิสูจน์การซื้อซ้ำ<br/>ก่อนเพิ่มสต็อก</h3>', '<h3 id="priorityTitle" data-i18n="priorityTitle">พิสูจน์การซื้อซ้ำ<br/>ก่อนเพิ่มสต็อก</h3>'),
    (r'<p id="priorityCopy">ทดลองกับกลุ่มเป้าหมายขนาดเล็ก', '<p id="priorityCopy" data-i18n="priorityCopy">ทดลองกับกลุ่มเป้าหมายขนาดเล็ก'),
    (r'<b>คะแนนคำนวณจากข้อมูลที่ผู้ใช้กรอกและกติกาจำลอง</b>', '<b data-i18n="assumptionNote">คะแนนคำนวณจากข้อมูลที่ผู้ใช้กรอกและกติกาจำลอง</b>'),
    (r'<button class="formula-toggle" id="formulaToggle" type="button" aria-expanded="false">ดูวิธีคิดคะแนน</button>', '<button class="formula-toggle" id="formulaToggle" type="button" aria-expanded="false" data-i18n="formulaToggle">ดูวิธีคิดคะแนน</button>'),
    (r'<div class="formula-details" id="formulaDetails" hidden>Readiness Score', '<div class="formula-details" id="formulaDetails" hidden data-i18n="formulaDetails">Readiness Score'),
    # Reflection prompt in actionbar
    (r'<p><b>Reflection prompt</b> จุดอ่อนข้อใดเปลี่ยนการตัดสินใจ</p>', '<p><b>Reflection prompt</b> <span data-i18n="reflectionPrompt">จุดอ่อนข้อใดเปลี่ยนการตัดสินใจของคุณมากที่สุด?</span></p>'),
    # Next button screen 2
    (r'<button class="primary" data-next type="button">เปรียบเทียบ 3 ทางเลือก</button>', '<button class="primary" data-next type="button" data-i18n="nextScenarios">เปรียบเทียบ 3 ทางเลือก</button>'),
    # Screen 3 scenario
    (r'<h2 id="scenarioTitle">ยอดขายสูงขึ้น', '<h2 id="scenarioTitle" data-i18n="scenarioTitle">ยอดขายสูงขึ้น'),
    (r'<p>เปลี่ยนข้อมูลหน้าก่อนหน้าได้ตลอดเวลา<br/>หน่วย: บาท เว้นแต่ระบุเป็นอย่างอื่น</p>', '<p data-i18n="scenarioSubtitle">เปลี่ยนข้อมูลหน้าก่อนหน้าได้ตลอดเวลา<br/>หน่วย: บาท เว้นแต่ระบุเป็นอย่างอื่น</p>'),
    (r'<div class="formula"><b>สูตรหลัก</b><span>Contribution/หน่วย', '<div class="formula"><b data-i18n="formulaMainLabel">สูตรหลัก</b><span data-i18n="formulaMainText">Contribution/หน่วย'),
    (r'<em>Simulation assumptions</em></div>', '<em data-i18n="formulaAssumptions">Simulation assumptions</em></div>'),
    (r'<span>YOUR DECISION</span>', '<span data-i18n="yourDecision">YOUR DECISION</span>'),
    (r'<small id="decisionReason">สมดุลระหว่างการเรียนรู้', '<small id="decisionReason" data-i18n="decisionReason">สมดุลระหว่างการเรียนรู้'),
    (r'<button class="ghost" id="whyRecommended" type="button">ดูเหตุผลแนะนำ</button>', '<button class="ghost" id="whyRecommended" type="button" data-i18n="whyRecommended">ดูเหตุผลแนะนำ</button>'),
    (r'<p><b>Decision rule</b><span id="decisionRule">เลือกทางที่ Contribution', '<p><b>Decision rule</b><span id="decisionRule" data-i18n="decisionRule">เลือกทางที่ Contribution'),
    (r'<button class="primary" data-next type="button">ซ้อมตอบ Buyer</button>', '<button class="primary" data-next type="button" data-i18n="nextBuyer">ซ้อมตอบ Buyer</button>'),
    # Screen 4 buyer
    (r'<h2 id="buyerTitle">คำตอบที่ดีต้องมีหลักฐาน', '<h2 id="buyerTitle" data-i18n="buyerTitle">คำตอบที่ดีต้องมีหลักฐาน'),
    (r'<div class="round" id="roundLabel">QUESTION 1 / 5</div>', '<div class="round" id="roundLabel" data-i18n="roundLabel">QUESTION 1 / 5</div>'),
    (r'<label for="buyerAnswer">YOUR RESPONSE</label>', '<label for="buyerAnswer" data-i18n="yourResponse">YOUR RESPONSE</label>'),
    (r'<textarea id="buyerAnswer" placeholder="พิมพ์คำตอบของคุณ', '<textarea id="buyerAnswer" placeholder="พิมพ์คำตอบของคุณ'),
    (r'<small id="answerCount">0 ตัวอักษร</small>', '<small id="answerCount" data-i18n="charCount">0 ตัวอักษร</small>'),
    (r'<button class="evaluate" id="evaluate" type="button">ประเมินคำตอบ</button>', '<button class="evaluate" id="evaluate" type="button" data-i18n="evaluateBtn">ประเมินคำตอบ</button>'),
    (r'<span>/ 100</span>', '<span data-i18n="outOf100">/ 100</span>'),
    (r'<b>จุดแข็ง</b>', '<b data-i18n="strengthLabel">จุดแข็ง</b>'),
    (r'<b>ควรเพิ่ม</b>', '<b data-i18n="improveLabel">ควรเพิ่ม</b>'),
    (r'<p id="buyerStrength">พิมพ์คำตอบแล้วกดประเมิน</p>', '<p id="buyerStrength" data-i18n="buyerStrengthDefault">พิมพ์คำตอบแล้วกดประเมิน</p>'),
    (r'<p id="buyerImprove">ระบบจะประเมินด้วย Rubric', '<p id="buyerImprove" data-i18n="buyerImproveDefault">ระบบจะประเมินด้วย Rubric'),
    (r'<b>Prototype note</b> การประเมินหน้านี้', '<b>Prototype note</b> <span data-i18n="coachNote">การประเมินหน้านี้ใช้ Rubric-based evaluator ภายในเบราว์เซอร์ ไม่มีการส่งข้อความไปยังบริการภายนอก</span>'),
    (r'<p><b>Buyer average</b><span id="buyerAverage">ยังไม่มีคะแนน</span></p>', '<p><b>Buyer average</b><span id="buyerAverage" data-i18n="buyerAverageNone">ยังไม่มีคะแนน</span></p>'),
    (r'<button class="primary" data-next type="button">สร้างแผน 90 วัน</button>', '<button class="primary" data-next type="button" data-i18n="nextRoadmap">สร้างแผน 90 วัน</button>'),
    # Screen 5 roadmap
    (r'<h2 id="roadmapTitle">เปลี่ยนข้อสงเกต', '<h2 id="roadmapTitle" data-i18n="roadmapTitle">เปลี่ยนข้อสังเกต'),
    (r'<span>งบจำลอง</span>', '<span data-i18n="roadmapBudgetLabel">งบจำลอง</span>'),
    (r'<span>Contribution เป้าหมาย</span>', '<span data-i18n="roadmapContributionLabel">Contribution เป้าหมาย</span>'),
    (r'<span>จุดตัดสินใจ</span>', '<span data-i18n="roadmapGateLabel">จุดตัดสินใจ</span>'),
    (r'<p><b>Effectuation</b> ลงทุนเท่าที่รับความเสียหาย', '<p><b>Effectuation</b> <span data-i18n="effectuationNote">ลงทุนเท่าที่รับความเสียหายได้ และขยายเมื่อหลักฐานเพิ่มขึ้น</span></p>'),
    (r'<button class="primary" data-next type="button">สะท้อนการเรียนรู้</button>', '<button class="primary" data-next type="button" data-i18n="nextReflection">สะท้อนการเรียนรู้</button>'),
    # Screen 6 reflection
    (r'<h2 id="reflectionTitle">AI จบเมื่อผู้เรียน', '<h2 id="reflectionTitle" data-i18n="reflectionTitle">AI จบเมื่อผู้เรียน'),
    (r'<p>การสะท้อนผลเปลี่ยน', '<p data-i18n="reflectionSubtitle">การสะท้อนผลเปลี่ยน'),
    # Reflection form labels
    (r'<label for="reflection1">1. คุณเลือกกลยุทธ์ใด', '<label for="reflection1" data-i18n="reflectionQ1">1. คุณเลือกกลยุทธ์ใด'),
    (r'<label for="reflection2">2. ผลลัพธ์ใดต่างจากที่คาด?</label>', '<label for="reflection2" data-i18n="reflectionQ2">2. ผลลัพธ์ใดต่างจากที่คาด?</label>'),
    (r'<label for="reflection3">3. หากทดลองใหม่', '<label for="reflection3" data-i18n="reflectionQ3">3. หากทดลองใหม่'),
    (r'<textarea id="reflection1" placeholder="อธิบายเหตุผล', '<textarea id="reflection1" placeholder="อธิบายเหตุผล'),
    (r'<textarea id="reflection2" placeholder="ระบุสิ่งที่ได้เรียนรู้', '<textarea id="reflection2" placeholder="ระบุสิ่งที่ได้เรียนรู้'),
    (r'<textarea id="reflection3" placeholder="กำหนดสมมติฐาน', '<textarea id="reflection3" placeholder="กำหนดสมมติฐาน'),
    (r'<button class="primary" id="saveReflection" type="button">บันทึก Reflection</button>', '<button class="primary" id="saveReflection" type="button" data-i18n="saveReflectionBtn">บันทึก Reflection</button>'),
    (r'<button class="ghost" id="downloadSummary" type="button">ดาวน์โหลดสรุป</button>', '<button class="ghost" id="downloadSummary" type="button" data-i18n="downloadBtn">ดาวน์โหลดสรุป</button>'),
    (r'<span>ข้อมูลจะบันทึกเฉพาะในเบราว์เซอร์เครื่องนี้</span>', '<span data-i18n="completeNote">ข้อมูลจะบันทึกเฉพาะในเบราว์เซอร์เครื่องนี้</span>'),
    (r'<p><b>Privacy</b> Prototype นี้ไม่มี Backend', '<p><b>Privacy</b> <span data-i18n="privacyNote">Prototype นี้ไม่มี Backend และไม่ส่งข้อมูลออกจากอุปกรณ์</span></p>'),
    (r'<button class="primary" id="restart" type="button">เริ่มรอบจำลองใหม่</button>', '<button class="primary" id="restart" type="button" data-i18n="restartBtn">เริ่มรอบจำลองใหม่</button>'),
    # Dialog
    (r'<h3>เหตุผลที่ระบบแนะนำ Scenario นี้</h3>', '<h3 data-i18n="dialogTitle">เหตุผลที่ระบบแนะนำ Scenario นี้</h3>'),
    (r'<button class="primary" id="closeDialog" type="button">เข้าใจแล้ว</button>', '<button class="primary" id="closeDialog" type="button" data-i18n="dialogClose">เข้าใจแล้ว</button>'),
]

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
for pattern, replacement in html_replacements:
    html = re.sub(pattern, replacement, html, count=1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html updated with data-i18n attributes")
