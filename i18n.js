// BRANDPILOT AI — Internationalization (TH / EN / ZH)
const I18N = {
  th: {
    // Navigation
    nav: ['เริ่มต้น', 'ข้อมูล', 'คะแนน', 'ทางเลือก', 'Buyer', 'Roadmap', 'ทบทวน'],
    navAria: ['ภาพรวม', 'กรอกข้อมูล', 'ความพร้อม', 'สถานการณ์', 'ผู้ซื้อ', 'แผน 90 วัน', 'Reflection'],
    resetTop: 'เริ่มใหม่',
    mode: 'LEARNING MODE',
    caseChip: 'Simulation case',
    // Screen 0 — Hero
    heroEyebrow: 'DECISION SIMULATION LAB',
    heroTitle: 'ทดลองก่อนลงทุน<br/><em>เรียนรู้ก่อนเสี่ยงจริง</em>',
    heroLead: 'เปลี่ยนข้อมูลสินค้าให้เป็นสถานการณ์จำลอง เพื่อฝึกคิดเรื่องราคา ช่องทาง โปรโมชั่น สต็อก และการนำเสนอ Buyer อย่างมีหลักฐาน',
    heroStart: 'เริ่มจำลองสถานการณ์',
    reflectionQ1Placeholder: 'อธิบายเหตุผลและหลักฐานที่ใช้ตัดสินใจ...',
    reflectionPlaceholder: 'ระบุสิ่งที่ได้เรียนรู้จากตัวเลขหรือการทดลอง...',
    reflectionQ3Placeholder: 'กำหนดสมมติฐานหรือการทดสอบครั้งถัดไป...',

    reflectionQ2: '2. ผลลัพธ์ใดต่างจากที่คาด?',
    roadmapTitle: 'เปลี่ยนข้อสังเกตให้เป็นการทดลองที่ลงมือได้',
    buyerAnswerPlaceholder: 'พิมพ์คำตอบของคุณ โดยใช้ตัวเลขและเกณฑ์ตัดสินใจ...',
    buyerPrompt: 'ตอบด้วยปัญหาลูกค้า หลักฐาน และความแตกต่างที่ตรวจสอบได้',
    buyerQuestion: 'เหตุใดสินค้านี้จึงควรได้พื้นที่ขาย?',
    reflectionPromptText: 'จุดอ่อนข้อใดเปลี่ยนการตัดสินใจของคุณมากที่สุด?',
    assumptionText: 'คะแนนคำนวณจากข้อมูลที่ผู้ใช้กรอกและกติกาจำลอง ไม่ใช่คำรับรองความสำเร็จ',
    inputHint: 'ระบบจะแสดงสูตรและเตือนเมื่อข้อมูลยังไม่สมเหตุผล',
    guardrail: 'ระบบแสดงสมมติฐานและผลกระทบ ผู้ใช้เป็นผู้ตัดสินใจ',
    heroProof: ['ขั้นตอนตัดสินใจ', 'Scenario เปรียบเทียบ', 'แผนพร้อมลงมือ'],
    disclaimer: 'กรณีศึกษาและตัวเลขทั้งหมดเป็นข้อมูลสมมติสำหรับการเรียนรู้ ไม่ใช่คำแนะนำการลงทุน',
    // Screen 1 — Product Input
    inputEyebrow: 'STEP 01 · PRODUCT INPUT',
    inputTitle: 'เริ่มจากข้อมูลที่ตรวจสอบได้',
    inputDesc: 'แก้ไขข้อมูลเพื่อดูผลลัพธ์ใหม่ทันที<br/>ช่องที่มีเครื่องหมาย * จำเป็นต้องกรอก',
    productMeta: 'Ready-to-drink protein beverage<br/>330 mL · Protein 25 g',
    liveEconLabel: 'กำไรขั้นต้นก่อนค่าช่องทาง',
    liveMarginSuffix: 'ของราคาขาย',
    formLabels: { price: 'ราคาขายปลีก *', cost: 'ต้นทุนต่อหน่วย *', budget: 'งบเปิดตัว *', stock: 'สต็อกเริ่มต้น *', channel: 'ช่องทางที่สนใจ', discount: 'ส่วนลดสูงสุดที่รับได้ *', evidence: 'หลักฐานความต้องการลูกค้า', leadTime: 'Lead time การผลิต *' },
    formUnits: { price: 'บาท', cost: 'บาท', budget: 'บาท', stock: 'หน่วย', discount: '%', leadTime: 'วัน' },
    channelOptions: { online: 'Online Test', balanced: 'Online + Selected Retail', modern: 'Modern Trade Rollout' },
    evidenceOptions: { idea: 'มีเพียงสมมติฐาน', interviews: 'มีผลสัมภาษณ์ลูกค้า', pilot: 'มีข้อมูล Paid Pilot' },
    inputHint: 'ระบบจะแสดงสูตรและเตือนเมื่อข้อมูลยังไม่สมเหตุผล',
    inputHintWarning: 'คำเตือน: ต้นทุนสูงกว่าหรือเท่าราคาขาย',
    inputHintNormal: 'กำไรขั้นต้นก่อนค่าช่องทาง {money} ต่อหน่วย',
    analyzeBtn: 'วิเคราะห์ความพร้อม',
    backBtn: 'ย้อนกลับ',
    // Screen 2 — Readiness
    readinessEyebrow: 'STEP 02 · BRAND READINESS',
    readinessTitle: 'คะแนน <score> ชี้ว่าควรทดสอบอะไรต่อ',
    statusLabels: { green: 'PILOT READY', aqua: 'CONTROLLED PILOT', amber: 'NEEDS VALIDATION', red: 'HIGH UNCERTAINTY' },
    confidenceLabel: 'ความเชื่อมั่นของข้อมูล',
    confidenceValues: { high: 'สูง', medium: 'ปานกลาง', low: 'ต่ำ' },
    metricLabels: { demand: 'หลักฐานความต้องการลูกค้า', economics: 'เศรษฐศาสตร์ต่อหน่วย', channel: 'ความเหมาะสมของช่องทาง', supply: 'ความพร้อมด้านอุปทาน', marketing: 'แผนสนับสนุนตลาด', risk: 'ข้อมูล จริยธรรม และความเสี่ยง' },
    nextBestTest: 'NEXT BEST TEST',
    assumptionLabel: 'ASSUMPTION',
    assumptionText: 'คะแนนคำนวณจากข้อมูลที่ผู้ใช้กรอกและกติกาจำลอง ไม่ใช่คำรับรองความสำเร็จ',
    formulaToggleOpen: 'ดูวิธีคิดคะแนน',
    formulaToggleClose: 'ซ่อนวิธีคิดคะแนน',
    formulaDetails: 'Readiness Score = ผลรวม 6 มิติ: Demand 20, Economics 20, Channel 15, Supply 15, Marketing 15 และ Risk 15 คะแนน',
    reflectionPrompt: 'จุดอ่อนข้อใดเปลี่ยนการตัดสินใจของคุณมากที่สุด?',
    nextScenarios: 'เปรียบเทียบ 3 ทางเลือก',
    // Screen 3 — Scenarios
    scenarioEyebrow: 'STEP 03 · SCENARIO SIMULATOR',
    scenarioTitle: 'ยอดขายสูงขึ้น ไม่ได้แปลว่าความเสี่ยงต่ำลง',
    scenarioDesc: 'เปลี่ยนข้อมูลหน้าก่อนหน้าได้ตลอดเวลา<br/>หน่วย: บาท เว้นแต่ระบุเป็นอย่างอื่น',
    formulaText: 'Contribution/หน่วย = ราคาหลังส่วนลดและ GP − ต้นทุน − ค่าใช้จ่ายผันแปรช่องทาง',
    formulaNote: 'Simulation assumptions',
    decisionText: 'YOUR DECISION',
    decisionReasons: {
      conservative: 'ใช้เงินน้อยที่สุด เหมาะเมื่อหลักฐานยังจำกัดหรือ Unit Economics ยังเปราะบาง',
      balanced: 'สมดุลระหว่างการเรียนรู้ เงินลงทุน และการทดสอบร้านค้าจริง',
      aggressive: 'เหมาะเมื่อมี Paid Pilot หลักฐานสูง และ Contribution รองรับค่าใช้จ่ายช่องทางใหญ่'
    },
    whyRecommended: 'ดูเหตุผลแนะนำ',
    decisionRule: 'Decision rule',
    decisionRuleText: 'เลือกทางที่ Contribution เป็นบวกและลงทุนไม่เกินความเสียหายที่ยอมรับได้',
    decisionRuleDynamic: 'Contribution {money}/หน่วย · ตั้งเกณฑ์ Stop หากต่ำกว่า {money2}',
    decisionRuleNegative: 'Contribution ติดลบ ควรกลับไปปรับราคา ต้นทุน หรือโปรโมชั่น',
    nextBuyer: 'ซ้อมตอบ Buyer',
    scenarioSelect: 'เลือก Scenario นี้',
    scenarioSelected: 'เลือกแล้ว',
    scenarioKeys: { investment: 'เงินลงทุนจำลอง', units: 'ยอดขายสมมติ', contribution: 'Contribution / หน่วย', breakeven: 'Break-even', risk: 'ความเสี่ยงรวม' },
    breakevenLabel: 'ไม่ถึงจุดคุ้มทุน',
    // Screen 4 — Buyer
    buyerEyebrow: 'STEP 04 · VIRTUAL BUYER CHALLENGE',
    buyerTitle: 'คำตอบที่ดีต้องมีหลักฐาน ไม่ใช่เพียงความมั่นใจ',
    buyerAvatar: 'VIRTUAL BUYER',
    buyerResponse: 'YOUR RESPONSE',
    buyerPlaceholder: 'พิมพ์คำตอบของคุณ โดยใช้ตัวเลขและเกณฑ์ตัดสินใจ...',
    charCount: '{count} ตัวอักษร',
    evaluateBtn: 'ประเมินคำตอบ',
    strengthLabel: 'จุดแข็ง',
    improveLabel: 'ควรเพิ่ม',
    buyerStrengthDefault: 'พิมพ์คำตอบแล้วกดประเมิน',
    buyerImproveDefault: 'ระบบจะประเมินด้วย Rubric ที่เปิดเผยได้',
    rubricLabels: ['CLARITY', 'EVIDENCE', 'ECONOMICS', 'CHANNEL', 'RISK'],
    coachNote: 'Prototype note — การประเมินหน้านี้ใช้ Rubric-based evaluator ภายในเบราว์เซอร์ ไม่มีการส่งข้อความไปยังบริการภายนอก',
    buyerAverage: 'Buyer average',
    buyerAverageNone: 'ยังไม่มีคะแนน',
        buyerAverageText: '{avg}/100 จาก {count} คำถาม',
    questionNavLabel: 'คำถาม {n}',
    minCharsWarning: 'กรุณาอธิบายอย่างน้อย 20 ตัวอักษร เพื่อให้ Rubric ประเมินได้',
    rubricFeedback: {
      evidenceHigh: 'ใช้หลักฐานและตัวเลขช่วยให้ตรวจสอบคำตอบได้',
      evidenceLow: 'เพิ่มตัวเลขหรือหลักฐานจากการทดลอง',
      economicsHigh: 'เชื่อมคำตอบกับ Unit Economics',
      economicsLow: 'แสดงราคา ต้นทุน GP และ Contribution',
      riskHigh: 'มีเกณฑ์ควบคุมความเสี่ยง',
      riskLow: 'ระบุ Trigger สำหรับ Stop / Iterate / Scale',
      clarityLow: 'จัดคำตอบเป็น เหตุผล–หลักฐาน–การตัดสินใจ',
      strengthDefault: 'เริ่มตอบตรงคำถามแล้ว',
      improveDefault: 'คำตอบครบองค์ประกอบ ลองทำให้กระชับขึ้น'
    },
    nextRoadmap: 'สร้างแผน 90 วัน',
    // Screen 5 — Roadmap
    roadmapEyebrow: 'STEP 05 · 30–60–90 DAY ROADMAP',
    roadmapTitle: 'เปลี่ยนข้อสังเกตให้เป็นการทดลองที่ลงมือได้',
    roadmapKeys: { budget: 'งบจำลอง', contribution: 'Contribution เป้าหมาย', gate: 'จุดตัดสินใจ' },
    roadmapGatePositive: 'Pilot / Iterate / Stop',
    roadmapGateNegative: 'Fix Economics / Stop',
    roadmapDays: 'DAYS',
    effectuation: 'Effectuation — ลงทุนเท่าที่รับความเสียหายได้ และขยายเมื่อหลักฐานเพิ่มขึ้น',
    nextReflection: 'สะท้อนการเรียนรู้',
    // Screen 6 — Reflection
    reflectionEyebrow: 'STEP 06 · LEARNING REFLECTION',
    reflectionTitle: 'AI จบเมื่อผู้เรียน<br/>อธิบายเหตุผลได้',
    reflectionDesc: 'การสะท้อนผลเปลี่ยน "คำตอบจากระบบ" ให้เป็นความรู้ที่ผู้เรียนสร้างขึ้นเอง',
    kolb: ['EXPERIENCE', 'REFLECT', 'CONCEPTUALIZE', 'EXPERIMENT'],
    sessionLabel: 'SCENARIO',
    reflectionScore: 'Readiness {score}/100 · Contribution {money}/หน่วย',
    reflectionQ1: '1. คุณเลือกกลยุทธ์ใด และเพราะอะไร?',
    reflectionQ2: '2. ผลลัพธ์ใดต่างจากที่คาด?',
    reflectionQ3: '3. หากทดลองใหม่ จะเปลี่ยนอะไร?',
    reflectionP1: 'อธิบายเหตุผลและหลักฐานที่ใช้ตัดสินใจ',
    reflectionP2: 'ระบุสิ่งที่ได้เรียนรู้จากตัวเลขหรือ Scenario',
    reflectionP3: 'กำหนดสมมติฐานหรือการทดสอบครั้งถัดไป',
    saveReflection: 'บันทึก Reflection',
    downloadSummary: 'ดาวน์โหลดสรุป',
    completeLabel: 'LEARNING LOOP',
    completeText: 'ข้อมูลจะบันทึกเฉพาะในเบราว์เซอร์เครื่องนี้',
    reflectionSaved: 'REFLECTION SAVED',
    reflectionSavedText: 'บันทึกสำเร็จในเบราว์เซอร์เครื่องนี้',
    privacy: 'Privacy — Prototype นี้ไม่มี Backend และไม่ส่งข้อมูลออกจากอุปกรณ์',
    restartBtn: 'เริ่มรอบจำลองใหม่',
    // Dialog
    dialogEyebrow: 'RECOMMENDATION LOGIC',
    dialogTitle: 'เหตุผลที่ระบบแนะนำ Scenario นี้',
    dialogRecommended: '{label} เหมาะกับ Readiness {score}/100 และให้ Contribution {money}/หน่วย ภายใต้ความเสี่ยง {risk}. ระบบใช้หลักฐาน ความพร้อม และ Unit Economics ประกอบกัน แต่ผู้ใช้ยังเป็นผู้ตัดสินใจสุดท้าย',
    dialogAlternative: 'คุณเลือก {selected} ขณะที่ระบบแนะนำ {recommended}. ตัวเลือกของคุณให้ Contribution {money}/หน่วยและมีความเสี่ยง {risk}. ควรกำหนดเกณฑ์ Stop ให้ชัดเจนก่อนทดลอง',
    dialogClose: 'เข้าใจแล้ว',
    // Validation
    validation: {
      price: 'ราคาขายต้องมากกว่า 0',
      cost: 'ต้นทุนต้องไม่ติดลบ',
      budget: 'กรุณาระบุงบเปิดตัว',
      stock: 'กรุณาระบุสต็อกเริ่มต้น',
      discount: 'ส่วนลดควรอยู่ระหว่าง 0–60%',
      leadTime: 'Lead time ควรอยู่ระหว่าง 1–365 วัน'
    },
    resetConfirm: 'เริ่มรอบใหม่และล้างข้อมูลที่บันทึกไว้ในเบราว์เซอร์หรือไม่?',
    // Priority content
    priorities: {
      demand: ['พิสูจน์ความต้องการจริงก่อนเพิ่มสต็อก', 'สัมภาษณ์ลูกค้าเป้าหมายและทำ Paid Test เพื่อเก็บ Conversion กับอัตราซื้อซ้ำ'],
      economics: ['ปรับ Unit Economics ก่อนขยายช่องทาง', 'ทดสอบราคา ต้นทุน และโปรโมชั่นเพื่อให้ Contribution ต่อหน่วยยังเป็นบวก'],
      channel: ['ยืนยัน Channel–Product Fit', 'ทดลองกับช่องทางขนาดเล็ก วัด Sell-through และต้นทุนแฝงก่อนเข้าระบบใหญ่'],
      supply: ['ลดความเสี่ยงด้านสต็อกและ Lead time', 'ยืนยัน MOQ แผนเติมสินค้า และ Safety stock กับผู้ผลิตก่อนรับคำสั่งซื้อเพิ่ม'],
      marketing: ['สร้าง Demand Plan ที่วัดผลได้', 'จัดสรรงบตาม Funnel และกำหนด CAC, Conversion และจุดหยุดการใช้เงิน'],
      risk: ['กำหนด Guardrail ก่อนตัดสินใจ', 'ระบุสมมติฐาน แหล่งข้อมูล เจ้าของการตัดสินใจ และเกณฑ์ Stop / Iterate / Scale']
    },
    // Warnings
    warnings: {
      marginGood: 'Gross margin ก่อนค่าช่องทาง {percent} มีพื้นที่ให้ทดสอบ',
      marginBad: 'Gross margin {percent} อาจไม่พอรองรับ GP และโปรโมชั่น',
      budget: 'งบต่อสต็อก {money} ต่ำ ควรเลือก Pilot ที่แคบลง',
      supply: 'Lead time {days} วัน เพิ่มความเสี่ยง Out-of-stock',
      discount: 'ส่วนลด {percent}% กด Contribution ต่อหน่วยอย่างมีนัยสำคัญ'
    },
    // WOW
    wowLabel: '✨ WOW MODE',
    wowEyebrow: 'AI STRATEGY ENGINE',
    wowTitle: 'กำลังคำนวณกลยุทธ์...',
    wowSubtitle: 'วิเคราะห์ข้อมูลด้วย AI Simulation',
    wowFinal: 'กลยุทธ์ที่แนะนำ',
    wowScore: 'Readiness Score',
    wowReady: 'พร้อมใช้งาน!',
    wowComputing: 'กำลังคำนวณ...',
    wowClose: 'ปิด ✕',
    wowUnit: 'ต่อหน่วย',
    wowStrategy: 'กลยุทธ์: <b>{label}</b> — Contribution {money}/หน่วย',
    buyerQuestions: [
      { q: 'เหตุใดสินค้านี้จึงควรได้พื้นที่ขาย?', prompt: 'ตอบด้วยปัญหาลูกค้า หลักฐาน และความแตกต่างที่ตรวจสอบได้' },
      { q: 'หากจัดโปรโมชันตามแผน ธุรกิจยังมีกำไรหรือไม่?', prompt: 'อธิบายราคาสุทธิ ต้นทุน Contribution และจุดหยุดความเสี่ยง' },
      { q: 'จะทำให้สินค้าขายออกจากชั้นอย่างไร?', prompt: 'ระบุช่องทาง สื่อสนับสนุน KPI และความถี่ในการติดตาม' },
      { q: 'ถ้ายอดขายต่ำกว่าเป้า คุณจะจัดการสต็อกอย่างไร?', prompt: 'แสดง Trigger, Stock cover และแผน Iterate หรือ Stop' },
      { q: 'อีก 90 วัน Buyer ควรเห็นหลักฐานอะไร?', prompt: 'สรุปตัวเลข Go / No-go และผู้รับผิดชอบที่ชัดเจน' }
    ],
    roadmapTemplates: {
      conservative: [
        ['30', 'Discover', ['สัมภาษณ์ลูกค้าเป้าหมาย 12–15 คน', 'ทดสอบข้อความคุณค่า 2 แบบ', 'ยืนยันต้นทุนและ MOQ'], 'มี Problem–Solution Evidence'],
        ['60', 'Online Test', ['เปิดขายชุดเล็กใน Online', 'ทดสอบราคา 2 ระดับ', 'ติดตาม Conversion และซื้อซ้ำ'], 'ซื้อซ้ำ ≥ 20%'],
        ['90', 'Decide', ['สรุป CAC และ Contribution', 'แก้ Product / Offer', 'ตัดสินใจ Pilot หรือ Stop'], 'Evidence before retail']
      ],
      balanced: [
        ['30', 'Validate', ['สัมภาษณ์ลูกค้าเป้าหมาย 12 คน', 'ทดสอบราคาและ Promotion', 'ยืนยันต้นทุนและ MOQ'], 'ซื้อซ้ำ ≥ 25%'],
        ['60', 'Pilot', ['ขาย Online + ร้านคัดเลือก', 'ติดตามกำไรแยกช่องทาง', 'วัด Sell-through รายสัปดาห์'], 'Contribution ผ่านเกณฑ์'],
        ['90', 'Decide', ['ซ้อม Pitch กับ Virtual Buyer', 'สรุป Stock cover', 'ตัดสินใจ Scale / Iterate / Stop'], 'Evidence before scale']
      ],
      aggressive: [
        ['30', 'Retail Ready', ['ยืนยัน Forecast และ Service level', 'ล็อกแผนผลิตและ Safety stock', 'เตรียม Trade story'], 'Fill rate ≥ 95%'],
        ['60', 'Launch', ['เปิดตัวตาม Cluster ร้าน', 'ติดตาม Sell-through รายวัน', 'โยกงบตามประสิทธิภาพ'], 'On-shelf + Velocity'],
        ['90', 'Optimize', ['ทบทวน GP และ Promotion', 'ตัด SKU / Store ที่ไม่ผ่าน', 'ขยายเฉพาะ Cluster ที่ชนะ'], 'Profitable scale']
      ]
    },
    // Download
    downloadDisclaimer: 'Disclaimer: This prototype uses fictional data and simulation assumptions for learning only.'
  },
  en: {
    nav: ['Start', 'Input', 'Score', 'Options', 'Buyer', 'Roadmap', 'Review'],
    navAria: ['Overview', 'Product Input', 'Readiness', 'Scenarios', 'Buyer', '90-Day Plan', 'Reflection'],
    resetTop: 'Reset',
    mode: 'LEARNING MODE',
    caseChip: 'Simulation case',
    heroEyebrow: 'DECISION SIMULATION LAB',
    heroTitle: 'Test before invest<br/><em>Learn before you risk</em>',
    heroLead: 'Turn product data into simulated scenarios to practice thinking about pricing, channels, promotions, stock, and Buyer pitches with evidence',
    heroStart: 'Start Simulation',
    reflectionQ1Placeholder: 'Explain your reasoning and the evidence behind it...',
    reflectionPlaceholder: 'Note what you learned from the numbers or experiments...',
    reflectionQ3Placeholder: 'Define the next hypothesis or test...',

    buyerAnswerPlaceholder: 'Type your answer using numbers and decision criteria...',
    buyerPrompt: 'Answer with customer problems, evidence, and verifiable differentiation.',
    buyerQuestion: 'Why should this product get shelf space?',
    reflectionPromptText: 'Which weakness would most change your decision?',
    guardrail: 'System shows assumptions and impact — the user makes the final decision',
    heroProof: ['Decision steps', 'Scenarios compared', 'Ready-to-execute plan'],
    disclaimer: 'All case studies and figures are fictional data for learning purposes only. Not investment advice.',
    inputEyebrow: 'STEP 01 · PRODUCT INPUT',
    inputTitle: 'Start with verifiable data',
    inputDesc: 'Edit data to see results instantly<br/>Fields marked * are required',
    productMeta: 'Ready-to-drink protein beverage<br/>330 mL · Protein 25 g',
    liveEconLabel: 'Gross margin before channel costs',
    liveMarginSuffix: 'of retail price',
    formLabels: { price: 'Retail price *', cost: 'Unit cost *', budget: 'Launch budget *', stock: 'Opening stock *', channel: 'Target channel', discount: 'Max discount acceptable *', evidence: 'Customer demand evidence', leadTime: 'Production lead time *' },
    formUnits: { price: 'THB', cost: 'THB', budget: 'THB', stock: 'units', discount: '%', leadTime: 'days' },
    channelOptions: { online: 'Online Test', balanced: 'Online + Selected Retail', modern: 'Modern Trade Rollout' },
    evidenceOptions: { idea: 'Hypothesis only', interviews: 'Customer interviews', pilot: 'Paid pilot data' },
    inputHint: 'System shows formulas and warns when data seems unreasonable',
    inputHintWarning: 'Warning: Cost is higher than or equal to retail price',
    inputHintNormal: 'Gross margin before channel costs: {money} per unit',
    analyzeBtn: 'Analyze Readiness',
    backBtn: 'Back',
    readinessEyebrow: 'STEP 02 · BRAND READINESS',
    readinessTitle: 'A score of <score> shows what to test next',
    statusLabels: { green: 'PILOT READY', aqua: 'CONTROLLED PILOT', amber: 'NEEDS VALIDATION', red: 'HIGH UNCERTAINTY' },
    confidenceLabel: 'Data confidence',
    confidenceValues: { high: 'High', medium: 'Medium', low: 'Low' },
    metricLabels: { demand: 'Customer demand evidence', economics: 'Unit economics', channel: 'Channel fit', supply: 'Supply readiness', marketing: 'Marketing plan', risk: 'Data, ethics & risk' },
    nextBestTest: 'NEXT BEST TEST',
    assumptionLabel: 'ASSUMPTION',
    assumptionText: 'Score is calculated from user input and simulation rules — not a guarantee of success',
    formulaToggleOpen: 'Show scoring formula',
    formulaToggleClose: 'Hide scoring formula',
    formulaDetails: 'Readiness Score = sum of 6 dimensions: Demand 20, Economics 20, Channel 15, Supply 15, Marketing 15, and Risk 15 points',
    reflectionPrompt: 'Which weakness would most change your decision?',
    nextScenarios: 'Compare 3 options',
    scenarioEyebrow: 'STEP 03 · SCENARIO SIMULATOR',
    scenarioTitle: 'Higher sales don\'t mean lower risk',
    scenarioDesc: 'You can change previous data anytime<br/>Currency: THB unless noted',
    formulaText: 'Contribution/unit = Net price after discount & GP − cost − channel variable cost',
    formulaNote: 'Simulation assumptions',
    decisionText: 'YOUR DECISION',
    decisionReasons: {
      conservative: 'Lowest investment, best when evidence is limited or unit economics are fragile',
      balanced: 'Balance between learning, investment, and real retail testing',
      aggressive: 'Best with strong Paid Pilot evidence and Contribution that covers major channel costs'
    },
    whyRecommended: 'See recommendation logic',
    decisionRule: 'Decision rule',
    decisionRuleText: 'Choose the path where Contribution is positive and investment stays within acceptable loss',
    decisionRuleDynamic: 'Contribution {money}/unit · Set Stop criteria below {money2}',
    decisionRuleNegative: 'Negative Contribution — revisit pricing, cost, or promotion',
    nextBuyer: 'Practice Buyer Pitch',
    scenarioSelect: 'Select this scenario',
    scenarioSelected: 'Selected',
    scenarioKeys: { investment: 'Simulated investment', units: 'Projected units', contribution: 'Contribution / unit', breakeven: 'Break-even', risk: 'Overall risk' },
    breakevenLabel: 'Never breaks even',
    buyerEyebrow: 'STEP 04 · VIRTUAL BUYER CHALLENGE',
    buyerTitle: 'Good answers need evidence, not just confidence',
    buyerAvatar: 'VIRTUAL BUYER',
    buyerResponse: 'YOUR RESPONSE',
    buyerPlaceholder: 'Type your answer using numbers and decision criteria...',
    charCount: '{count} characters',
    evaluateBtn: 'Evaluate Answer',
    strengthLabel: 'Strengths',
    improveLabel: 'To improve',
    buyerStrengthDefault: 'Type your answer then evaluate',
    buyerImproveDefault: 'System evaluates with an open Rubric',
    rubricLabels: ['CLARITY', 'EVIDENCE', 'ECONOMICS', 'CHANNEL', 'RISK'],
    coachNote: 'Prototype note — This page uses a Rubric-based evaluator in the browser. No messages sent to external services.',
    buyerAverage: 'Buyer average',
    buyerAverageNone: 'No scores yet',
        buyerAverageText: '{avg}/100 from {count} questions',
    questionNavLabel: 'Question {n}',
    minCharsWarning: 'Please write at least 20 characters so the Rubric can evaluate.',
    rubricFeedback: {
      evidenceHigh: 'Uses data and evidence that can be verified',
      evidenceLow: 'Add numbers or evidence from experiments',
      economicsHigh: 'Connects answer to Unit Economics',
      economicsLow: 'Show price, cost, GP, and Contribution',
      riskHigh: 'Has risk control criteria',
      riskLow: 'Specify triggers for Stop / Iterate / Scale',
      clarityLow: 'Structure answer as Reason–Evidence–Decision',
      strengthDefault: 'Good start — answering directly',
      improveDefault: 'Complete answer — try making it more concise'
    },
    nextRoadmap: 'Build 90-Day Plan',
    roadmapEyebrow: 'STEP 05 · 30–60–90 DAY ROADMAP',
    roadmapTitle: 'Turn observations into actionable experiments',
    roadmapKeys: { budget: 'Simulated budget', contribution: 'Target Contribution', gate: 'Decision gate' },
    roadmapGatePositive: 'Pilot / Iterate / Stop',
    roadmapGateNegative: 'Fix Economics / Stop',
    roadmapDays: 'DAYS',
    effectuation: 'Effectuation — invest only what you can afford to lose, scale with evidence',
    nextReflection: 'Reflect on Learning',
    reflectionEyebrow: 'STEP 06 · LEARNING REFLECTION',
    reflectionTitle: 'AI ends when the learner<br/>can explain the why',
    reflectionDesc: 'Reflection turns "system answers" into knowledge the learner builds themselves',
    kolb: ['EXPERIENCE', 'REFLECT', 'CONCEPTUALIZE', 'EXPERIMENT'],
    sessionLabel: 'SCENARIO',
    reflectionScore: 'Readiness {score}/100 · Contribution {money}/unit',
    reflectionQ1: '1. Which strategy did you choose and why?',
    reflectionQ2: '2. What result surprised you?',
    reflectionQ3: '3. If you ran this again, what would you change?',
    reflectionP1: 'Explain your reasoning and the evidence used',
    reflectionP2: 'Note what you learned from the numbers or scenarios',
    reflectionP3: 'Define your next hypothesis or test',
    saveReflection: 'Save Reflection',
    downloadSummary: 'Download Summary',
    completeLabel: 'LEARNING LOOP',
    completeText: 'Data stored only in this browser',
    reflectionSaved: 'REFLECTION SAVED',
    reflectionSavedText: 'Saved successfully in this browser',
    privacy: 'Privacy — This prototype has no backend and sends no data outside the device',
    restartBtn: 'Start New Round',
    dialogEyebrow: 'RECOMMENDATION LOGIC',
    dialogTitle: 'Why the system recommends this scenario',
    dialogRecommended: '{label} fits Readiness {score}/100 and delivers Contribution {money}/unit at risk level {risk}. The system combines evidence, readiness, and unit economics — but the user makes the final decision.',
    dialogAlternative: 'You chose {selected} while the system recommends {recommended}. Your choice gives Contribution {money}/unit at risk level {risk}. Set clear Stop criteria before experimenting.',
    dialogClose: 'Got it',
    validation: {
      price: 'Retail price must be greater than 0',
      cost: 'Cost cannot be negative',
      budget: 'Please enter launch budget',
      stock: 'Please enter opening stock',
      discount: 'Discount should be between 0–60%',
      leadTime: 'Lead time should be between 1–365 days'
    },
    resetConfirm: 'Start a new round and clear saved browser data?',
    priorities: {
      demand: ['Prove real demand before adding stock', 'Interview target customers and run a Paid Test to collect Conversion and repeat purchase rates'],
      economics: ['Fix Unit Economics before expanding channels', 'Test price, cost, and promotions to keep Contribution per unit positive'],
      channel: ['Confirm Channel–Product Fit', 'Test on a small channel, measure Sell-through and hidden costs before going big'],
      supply: ['Reduce stock and lead time risk', 'Confirm MOQ, replenishment plans, and safety stock with supplier before accepting more orders'],
      marketing: ['Build a measurable Demand Plan', 'Allocate budget by Funnel and set CAC, Conversion, and spending stop points'],
      risk: ['Set guardrails before deciding', 'Identify assumptions, data sources, decision owners, and Stop / Iterate / Scale criteria']
    },
    warnings: {
      marginGood: 'Gross margin before channel costs at {percent} leaves room to test',
      marginBad: 'Gross margin at {percent} may not cover GP and promotions',
      budget: 'Budget per stock unit at {money} is low — choose a narrower pilot',
      supply: 'Lead time of {days} days increases Out-of-stock risk',
      discount: 'Discount of {percent}% significantly reduces per-unit Contribution'
    },
    wowLabel: '✨ WOW MODE',
    wowEyebrow: 'AI STRATEGY ENGINE',
    wowTitle: 'Computing strategy...',
    wowSubtitle: 'AI-powered simulation analysis',
    wowFinal: 'Recommended Strategy',
    wowScore: 'Readiness Score',
    wowReady: 'Ready!',
    wowComputing: 'Computing...',
    wowClose: 'Close ✕',
    wowUnit: 'per unit',
    wowStrategy: 'Strategy: <b>{label}</b> — Contribution {money}/unit',
    buyerQuestions: [
      { q: 'Why should this product get shelf space?', prompt: 'Answer with customer pain points, evidence, and verifiable differentiation' },
      { q: 'If we run the planned promotion, is the business still profitable?', prompt: 'Explain net price, cost, Contribution, and risk stop points' },
      { q: 'How will you drive product off the shelf?', prompt: 'Specify channels, media support, KPIs, and monitoring frequency' },
      { q: 'If sales fall below target, how will you manage stock?', prompt: 'Show Triggers, Stock cover, and Iterate or Stop plans' },
      { q: 'What evidence should the Buyer see in 90 days?', prompt: 'Summarize Go / No-go numbers and clearly assigned owners' }
    ],
    roadmapTemplates: {
      conservative: [
        ['30', 'Discover', ['Interview 12–15 target customers', 'Test 2 value messages', 'Confirm cost and MOQ'], 'Have Problem–Solution Evidence'],
        ['60', 'Online Test', ['Launch small online', 'Test 2 price levels', 'Track Conversion and repeat purchase'], 'Repeat ≥ 20%'],
        ['90', 'Decide', ['Summarize CAC and Contribution', 'Fix Product / Offer', 'Decide Pilot or Stop'], 'Evidence before retail']
      ],
      balanced: [
        ['30', 'Validate', ['Interview 12 target customers', 'Test price and Promotion', 'Confirm cost and MOQ'], 'Repeat ≥ 25%'],
        ['60', 'Pilot', ['Sell Online + selected retail', 'Track profit per channel', 'Measure weekly Sell-through'], 'Contribution passes criteria'],
        ['90', 'Decide', ['Rehearse pitch with Virtual Buyer', 'Summarize Stock cover', 'Decide Scale / Iterate / Stop'], 'Evidence before scale']
      ],
      aggressive: [
        ['30', 'Retail Ready', ['Confirm Forecast and Service level', 'Lock production plan and Safety stock', 'Prepare Trade story'], 'Fill rate ≥ 95%'],
        ['60', 'Launch', ['Launch by store cluster', 'Track daily Sell-through', 'Shift budget by performance'], 'On-shelf + Velocity'],
        ['90', 'Optimize', ['Review GP and Promotion', 'Cut non-performing SKU / Store', 'Expand only winning clusters'], 'Profitable scale']
      ]
    },
    downloadDisclaimer: 'Disclaimer: This prototype uses fictional data and simulation assumptions for learning only.'
  },
  zh: {
    nav: ['首页', '输入', '评分', '方案', '买家', '路线', '反思'],
    navAria: ['概览', '产品输入', '准备度', '情景模拟', '买家', '90天计划', '反思'],
    resetTop: '重置',
    mode: 'LEARNING MODE',
    caseChip: '模拟案例',
    heroEyebrow: 'DECISION SIMULATION LAB',
    heroTitle: '投资前先测试<br/><em>冒险前先学习</em>',
    heroLead: '将产品数据转化为模拟场景，练习有证据支撑的定价、渠道、促销、库存和买家提案思维',
    heroStart: '开始模拟',
    reflectionQ1Placeholder: '解释你的推理和证据...',
    reflectionPlaceholder: '记录你从数字或实验中学到的东西...',
    reflectionQ3Placeholder: '定义下一个假设或测试...',

    buyerAnswerPlaceholder: '用数字和决策标准输入你的答案...',
    buyerPrompt: '用客户问题、证据和可验证的差异化来回答',
    buyerQuestion: '为什么这个产品应该获得货架空间？',
    reflectionPromptText: '哪个弱点最会改变你的决定？',
    heroTitle: '投资前先测试<br/><em>冒险前先学习</em>',
    guardrail: '系统展示假设和影响 — 用户做最终决策',
    heroProof: ['决策步骤', '情景对比', '可执行计划'],
    disclaimer: '所有案例和数据均为学习用途的虚构数据，不构成投资建议。',
    inputEyebrow: 'STEP 01 · PRODUCT INPUT',
    inputTitle: '从可验证的数据开始',
    inputDesc: '随时修改数据查看新结果<br/>带 * 的字段为必填',
    productMeta: '即饮蛋白质饮料<br/>330 mL · 蛋白质 25g',
    liveEconLabel: '渠道费用前毛利',
    liveMarginSuffix: '占零售价',
    formLabels: { price: '零售价 *', cost: '单位成本 *', budget: '上市预算 *', stock: '初始库存 *', channel: '目标渠道', discount: '可接受最高折扣 *', evidence: '客户需求证据', leadTime: '生产周期 *' },
    formUnits: { price: '泰铢', cost: '泰铢', budget: '泰铢', stock: '件', discount: '%', leadTime: '天' },
    channelOptions: { online: '线上测试', balanced: '线上+精选零售', modern: '现代渠道铺货' },
    evidenceOptions: { idea: '仅有假设', interviews: '有客户访谈', pilot: '有付费试点数据' },
    inputHint: '系统会展示公式并在数据不合理时发出警告',
    inputHintWarning: '警告：成本高于或等于零售价',
    inputHintNormal: '渠道费用前毛利：{money}/件',
    analyzeBtn: '分析准备度',
    backBtn: '返回',
    readinessEyebrow: 'STEP 02 · BRAND READINESS',
    readinessTitle: '分数 <score> 显示下一步该测试什么',
    statusLabels: { green: 'PILOT READY', aqua: 'CONTROLLED PILOT', amber: 'NEEDS VALIDATION', red: 'HIGH UNCERTAINTY' },
    confidenceLabel: '数据置信度',
    confidenceValues: { high: '高', medium: '中', low: '低' },
    metricLabels: { demand: '客户需求证据', economics: '单位经济模型', channel: '渠道适配度', supply: '供应链准备度', marketing: '营销计划', risk: '数据、伦理与风险' },
    nextBestTest: '下一步最佳测试',
    assumptionLabel: 'ASSUMPTION',
    assumptionText: '分数基于用户输入和模拟规则计算 — 不是成功保证',
    formulaToggleOpen: '查看评分公式',
    formulaToggleClose: '隐藏评分公式',
    formulaDetails: 'Readiness Score = 6个维度之和：Demand 20, Economics 20, Channel 15, Supply 15, Marketing 15, Risk 15分',
    reflectionPrompt: '哪个弱点最可能改变你的决策？',
    nextScenarios: '对比3个方案',
    scenarioEyebrow: 'STEP 03 · SCENARIO SIMULATOR',
    scenarioTitle: '销量高不等于风险低',
    scenarioDesc: '可随时修改上一页数据<br/>单位：泰铢（另有注明除外）',
    formulaText: '单位贡献 = 折扣和GP后净价 − 成本 − 渠道可变费用',
    formulaNote: 'Simulation assumptions',
    decisionText: 'YOUR DECISION',
    decisionReasons: {
      conservative: '投资最少，适合证据有限或单位经济模型脆弱的情况',
      balanced: '在学习、投资和真实零售测试之间取得平衡',
      aggressive: '适合有强付费试点证据且贡献能覆盖大渠道成本的情况'
    },
    whyRecommended: '查看推荐理由',
    decisionRule: 'Decision rule',
    decisionRuleText: '选择贡献为正且投资不超过可接受损失的方案',
    decisionRuleDynamic: '贡献 {money}/件 · 低于 {money2} 时设置停止标准',
    decisionRuleNegative: '贡献为负 — 重新调整价格、成本或促销',
    nextBuyer: '练习买家提案',
    scenarioSelect: '选择此方案',
    scenarioSelected: '已选择',
    scenarioKeys: { investment: '模拟投资', units: '预测销量', contribution: '单位贡献', breakeven: '盈亏平衡', risk: '综合风险' },
    breakevenLabel: '无法盈亏平衡',
    buyerEyebrow: 'STEP 04 · VIRTUAL BUYER CHALLENGE',
    buyerTitle: '好的回答需要证据，不只是信心',
    buyerAvatar: 'VIRTUAL BUYER',
    buyerResponse: 'YOUR RESPONSE',
    buyerPlaceholder: '输入你的回答，使用数字和决策标准...',
    charCount: '{count} 字',
    evaluateBtn: '评估回答',
    strengthLabel: '优势',
    improveLabel: '改进点',
    buyerStrengthDefault: '输入回答后点击评估',
    buyerImproveDefault: '系统使用公开的Rubric评估',
    rubricLabels: ['清晰度', '证据', '经济模型', '渠道', '风险'],
    coachNote: '原型说明 — 此页使用浏览器内Rubric评估器，不向外部服务发送消息。',
    buyerAverage: '买家平均分',
    buyerAverageNone: '暂无评分',
    buyerAverageText: '{count}题平均 {avg}/100',
    minCharsWarning: '请至少写20个字，以便Rubric评估。',
    rubricFeedback: {
      evidenceHigh: '使用了可验证的数据和证据',
      evidenceLow: '增加实验数据或证据',
      economicsHigh: '将回答与单位经济模型关联',
      economicsLow: '展示价格、成本、GP和贡献',
      riskHigh: '有风险控制标准',
      riskLow: '明确Stop/Iterate/Scale的触发条件',
      clarityLow: '将回答组织为：原因–证据–决策',
      strengthDefault: '不错的开始 — 直接回答了问题',
      improveDefault: '回答完整 — 尝试更简洁'
    },
    nextRoadmap: '制定90天计划',
    roadmapEyebrow: 'STEP 05 · 30–60–90 DAY ROADMAP',
    roadmapTitle: '将观察转化为可执行的实验',
    roadmapKeys: { budget: '模拟预算', contribution: '目标贡献', gate: '决策关口' },
    roadmapGatePositive: '试点/迭代/停止',
    roadmapGateNegative: '修正经济模型/停止',
    roadmapDays: '天',
    effectuation: '效果推理 — 只投资能承受的损失，用证据扩大规模',
    nextReflection: '学习反思',
    reflectionEyebrow: 'STEP 06 · LEARNING REFLECTION',
    reflectionTitle: '当学习者能<br/>解释原因时AI才结束',
    reflectionDesc: '反思将"系统答案"转化为学习者自己构建的知识',
    kolb: ['体验', '反思', '概念化', '实验'],
    sessionLabel: 'SCENARIO',
    reflectionScore: '准备度 {score}/100 · 贡献 {money}/件',
    reflectionQ1: '1. 你选择了什么策略，为什么？',
    reflectionQ2: '2. 什么结果让你意外？',
    reflectionQ3: '3. 如果重来，你会改变什么？',
    reflectionP1: '解释你的推理和使用的证据',
    reflectionP2: '记录从数字或情景中学到了什么',
    reflectionP3: '定义下一个假设或测试',
    saveReflection: '保存反思',
    downloadSummary: '下载摘要',
    completeLabel: 'LEARNING LOOP',
    completeText: '数据仅存储在此浏览器中',
    reflectionSaved: '反思已保存',
    reflectionSavedText: '已成功保存到此浏览器',
    privacy: '隐私 — 此原型无后端，不向设备外发送数据',
    restartBtn: '开始新一轮',
    dialogEyebrow: 'RECOMMENDATION LOGIC',
    dialogTitle: '系统推荐此方案的原因',
    dialogRecommended: '{label} 适合准备度 {score}/100，贡献为 {money}/件，风险等级 {risk}。系统综合证据、准备度和单位经济模型 — 但用户做最终决策。',
    dialogAlternative: '你选择了 {selected}，而系统推荐 {recommended}。你的选择贡献为 {money}/件，风险等级 {risk}。实验前请设定明确的停止标准。',
    dialogClose: '明白了',
    validation: {
      price: '零售价必须大于0',
      cost: '成本不能为负',
      budget: '请输入上市预算',
      stock: '请输入初始库存',
      discount: '折扣应在0–60%之间',
      leadTime: '生产周期应在1–365天之间'
    },
    resetConfirm: '开始新一轮并清除浏览器中保存的数据？',
    priorities: {
      demand: ['增加库存前先证明真实需求', '访谈目标客户并进行付费测试，收集转化率和复购率'],
      economics: ['扩展渠道前先修正单位经济模型', '测试价格、成本和促销以确保单位贡献为正'],
      channel: ['确认渠道-产品适配', '在小渠道测试，测量动销率和隐性成本后再进入大系统'],
      supply: ['降低库存和周期风险', '在接受更多订单前与供应商确认MOQ、补货计划和安全库存'],
      marketing: ['建立可衡量的需求计划', '按漏斗分配预算，设定CAC、转化率和支出停止点'],
      risk: ['决策前设定护栏', '明确假设、数据来源、决策负责人和停止/迭代/扩大标准']
    },
    warnings: {
      marginGood: '渠道费用前毛利 {percent}，有测试空间',
      marginBad: '毛利 {percent} 可能不足以覆盖GP和促销',
      budget: '每件库存预算 {money} 偏低 — 选择更窄的试点',
      supply: '生产周期 {days} 天增加缺货风险',
      discount: '折扣 {percent}% 显著降低单位贡献'
    },
    wowLabel: '✨ WOW MODE',
    wowEyebrow: 'AI STRATEGY ENGINE',
    wowTitle: '正在计算策略...',
    wowSubtitle: 'AI驱动的模拟分析',
    wowFinal: '推荐策略',
    wowScore: '准备度分数',
    wowReady: '准备就绪！',
    wowComputing: '正在计算...',
    wowClose: '关闭 ✕',
    wowUnit: '每件',
    wowStrategy: '策略：<b>{label}</b> — 贡献 {money}/件',
    buyerQuestions: [
      { q: '为什么这个产品应该获得货架空间？', prompt: '用客户痛点、证据和可验证的差异化来回答' },
      { q: '如果按计划做促销，业务还能盈利吗？', prompt: '解释净价、成本、贡献和停止风险点' },
      { q: '如何让产品离开货架（卖出）？', prompt: '指定渠道、媒体支持、KPI和监测频率' },
      { q: '如果销量低于目标，你将如何管理库存？', prompt: '展示触发器、库存覆盖和迭代或停止计划' },
      { q: '90天后买家应该看到什么证据？', prompt: '总结Go/No-go数字和明确的责任人' }
    ],
    roadmapTemplates: {
      conservative: [
        ['30', 'Discover', ['访谈12–15名目标客户', '测试2个价值主张', '确认成本和MOQ'], '有Problem–Solution证据'],
        ['60', 'Online Test', ['小规模线上销售', '测试2个价格水平', '跟踪转化率和复购率'], '复购率 ≥ 20%'],
        ['90', 'Decide', ['总结CAC和贡献', '修正产品/报价', '决定试点或停止'], 'Evidence before retail']
      ],
      balanced: [
        ['30', 'Validate', ['访谈12名目标客户', '测试价格和促销', '确认成本和MOQ'], '复购率 ≥ 25%'],
        ['60', 'Pilot', ['线上+精选零售销售', '按渠道跟踪利润', '每周测量动销率'], '贡献通过标准'],
        ['90', 'Decide', ['与虚拟买家演练Pitch', '总结库存覆盖', '决定扩大/迭代/停止'], 'Evidence before scale']
      ],
      aggressive: [
        ['30', 'Retail Ready', ['确认预测和服务水平', '锁定生产计划和安全库存', '准备Trade story'], 'Fill rate ≥ 95%'],
        ['60', 'Launch', ['按门店集群上市', '每日跟踪动销率', '按表现调配预算'], 'On-shelf + Velocity'],
        ['90', 'Optimize', ['审查GP和促销', '淘汰不达标SKU/门店', '仅扩展获胜集群'], 'Profitable scale']
      ]
    },
    downloadDisclaimer: 'Disclaimer: This prototype uses fictional data and simulation assumptions for learning only.'
  }
};

// Language management
let currentLang = localStorage.getItem('brandpilot-lang') || 'th';

function setLanguage(lang) {
  if (!I18N[lang]) return;
  currentLang = lang;
  localStorage.setItem('brandpilot-lang', lang);
  document.documentElement.lang = lang;
  if (typeof window.applyTranslations === 'function') window.applyTranslations();
}

function t(key, replacements = {}) {
  const value = key.split('.').reduce((obj, k) => obj?.[k], I18N[currentLang]);
  if (value === undefined) return key;
  let result = typeof value === 'string' ? value : value;
  for (const [k, v] of Object.entries(replacements)) {
    result = result.replace(new RegExp(`\\{${k}\\}`, 'g'), v);
  }
  return result;
}


// Apply all translations to DOM
window.applyTranslations = function applyTranslations() {
  const data = I18N[currentLang];
  if (!data) return;

  // Helper: safely update text content
  function setText(el, value) {
    if (!el || value === undefined || value === null) return;
    if (typeof value !== 'string') return;
    // If value contains HTML tags, use innerHTML
    if (value.includes('<') && value.includes('>')) {
      el.innerHTML = value;
    } else {
      el.textContent = value;
    }
  }

  // === 1. Process ALL data-i18n attributes ===
  document.querySelectorAll('[data-i18n]').forEach(el => {
    try {
      const key = el.getAttribute('data-i18n');
      if (!key) return;

      // Special: nav array (multiple buttons share same key)
      if (key === 'nav') {
        const allNav = Array.from(document.querySelectorAll('button.nav b[data-i18n="nav"]'));
        const idx = allNav.indexOf(el);
        if (idx >= 0 && Array.isArray(data.nav) && data.nav[idx]) {
          el.textContent = data.nav[idx];
        }
        return;
      }

      // Special: heroProof array
      if (key === 'heroProof') {
        const allProof = Array.from(document.querySelectorAll('.hero-proof span[data-i18n="heroProof"]'));
        const idx = allProof.indexOf(el);
        if (idx >= 0 && Array.isArray(data.heroProof) && data.heroProof[idx]) {
          el.textContent = data.heroProof[idx];
        }
        return;
      }

      // Resolve nested key
      let value = data;
      for (const part of key.split('.')) {
        value = value?.[part];
        if (value === undefined) break;
      }
      if (value === undefined || value === null) return;

      // Handle based on element type
      if (el.tagName === 'TEXTAREA' || (el.tagName === 'INPUT' && !['button','submit','reset'].includes(el.type))) {
        el.placeholder = value;
      } else if (el.tagName === 'OPTION') {
        el.textContent = value;
      } else if (typeof value === 'string') {
        setText(el, value);
      }
    } catch (e) {
      console.warn('i18n error for element:', e);
    }
  });

  // === 1b. Process data-i18n-placeholder attributes ===
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    try {
      const key = el.getAttribute('data-i18n-placeholder');
      if (!key) return;
      let value = data;
      for (const part of key.split('.')) {
        value = value?.[part];
        if (value === undefined) break;
      }
      if (value !== undefined && value !== null && typeof value === 'string') {
        el.placeholder = value;
      }
    } catch (e) { console.warn('placeholder error:', e); }
  });
  // === 2. Handle innerHTML elements (preserve <br>, <em>, <b>) ===
  const innerHTMLIds = ['heroTitle', 'reflectionTitle', 'readinessTitle', 'scenarioTitle', 'buyerTitle', 'roadmapTitle', 'productMeta', 'inputDesc', 'inputHint', 'assumptionText', 'reflectionPromptText', 'buyerQuestion', 'buyerPrompt'];
  innerHTMLIds.forEach(id => {
    const el = document.getElementById(id);
    if (el && data[id]) {
      try { el.innerHTML = data[id]; } catch(e) { console.warn('innerHTML error:', id, e); }
    }
  });

  // === 3. Special UI elements ===
  const wowBtn = document.getElementById('wowBtn');
  if (wowBtn && data.wowLabel) {
    try { wowBtn.innerHTML = '<i></i>' + data.wowLabel; } catch(e) {}
  }

  const caseChip = document.getElementById('caseChipLabel');
  if (caseChip && data.caseChip) {
    try { caseChip.textContent = data.caseChip; } catch(e) {}
  }

  const modeLabel = document.getElementById('modeLabel');
  if (modeLabel && data.mode) {
    try { modeLabel.textContent = data.mode; } catch(e) {}
  }

  const resetTop = document.getElementById('resetTop');
  if (resetTop && data.resetTop) {
    try { resetTop.textContent = data.resetTop; } catch(e) {}
  }

  // Hero start button
  const heroStart = document.querySelector('.hero .primary[data-next]') || document.querySelector('button.primary[data-next]');
  if (heroStart && data.heroStart) {
    try { heroStart.textContent = data.heroStart; } catch(e) {}
  }

  // Disclaimer
  document.querySelectorAll('.disclaimer').forEach(el => {
    if (data.disclaimer) { try { el.textContent = data.disclaimer; } catch(e) {} }
  });

  // Guardrail
  document.querySelectorAll('.guardrail').forEach(el => {
    if (data.guardrail) {
      try {
        const span = el.querySelector('span');
        if (span) {
          const textNode = Array.from(el.childNodes).find(n => n.nodeType === 3);
          if (textNode) textNode.textContent = ' ' + data.guardrail;
        } else {
          el.innerHTML = '<span>HUMAN-IN-THE-LOOP</span> ' + data.guardrail;
        }
      } catch(e) {}
    }
  });

  // Confidence value
  const confEl = document.getElementById('confidenceValue');
  if (confEl && data.confidenceValues?.medium) {
    try { confEl.textContent = data.confidenceValues.medium; } catch(e) {}
  }

  // Nav aria-labels
  const navBtns = document.querySelectorAll('button.nav');
  if (data.navAria && navBtns.length) {
    navBtns.forEach((el, i) => {
      if (data.navAria[i]) {
        try { el.setAttribute('aria-label', data.navAria[i]); } catch(e) {}
      }
    });
  }
};

export { I18N, currentLang, setLanguage, t };
