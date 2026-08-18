content = open('i18n.js').read()
lines = content.split('\n')

# TH buyerQuestions content to insert after line 171 (wowReady: 'พร้อมใช้งาน!',)
th_extra = """    wowComputing: 'กำลังคำนวณ...',
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
    },"""

# EN content
en_extra = """    wowComputing: 'Computing...',
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
    },"""

# ZH content
zh_extra = """    wowComputing: '正在计算...',
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
    },"""

# Insert after wowReady lines
# Line 171 (0-indexed: 170) for TH
lines[170] = lines[170] + '\n' + th_extra

# Line 330 (0-indexed: 329) for EN - but after TH insertion it shifted
# We need to recalculate. TH was 1 line → now 1 + ~42 lines. 
# Better approach: find wowReady lines by content
new_lines = []
for i, line in enumerate(lines):
    new_lines.append(line)
    stripped = line.strip()
    if stripped == "wowReady: 'พร้อมใช้งาน!',":
        for extra_line in th_extra.split('\n'):
            new_lines.append(extra_line)
    elif stripped == "wowReady: 'Ready!',":
        for extra_line in en_extra.split('\n'):
            new_lines.append(extra_line)
    elif stripped == "wowReady: '准备就绪！',":
        for extra_line in zh_extra.split('\n'):
            new_lines.append(extra_line)

content = '\n'.join(new_lines)

# Fix setLanguage to not crash
content = content.replace(
    "  applyTranslations();",
    "  if (typeof window.applyTranslations === 'function') window.applyTranslations();"
)

open('i18n.js', 'w').write(content)
print(f"i18n.js fixed. Lines: {len(content.split(chr(10)))}")
