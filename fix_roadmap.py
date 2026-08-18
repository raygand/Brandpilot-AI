content = open('app.js').read()

# Replace the broken roadmapTemplates const with a proper reference
old = """// roadmapTemplates moved to i18n.js
const roadmapTemplates = I18N[currentLang].roadmapTemplates || {
  conservative: [
    ...I18N[currentLang].roadmapTemplates.discover,
    ...I18N[currentLang].roadmapTemplates.discover,
    ...I18N[currentLang].roadmapTemplates.discover
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
};"""

new = """// roadmapTemplates moved to i18n.js
function getRoadmapTemplates() { return I18N[currentLang].roadmapTemplates; }"""

content = content.replace(old, new)

# Now fix renderRoadmap to use getRoadmapTemplates()
content = content.replace(
    "const roadmap = roadmapTemplates[selected.id];",
    "const roadmap = getRoadmapTemplates()[selected.id] || getRoadmapTemplates().balanced;"
)

open('app.js', 'w').write(content)
print("Fixed roadmapTemplates reference")
