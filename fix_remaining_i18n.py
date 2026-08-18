import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix 1: Remove duplicate text after span elements (lines 148, 159, 173)
# Line 148: remove "ใช้ Rubric-based evaluator ภายในเบราว์เซอร์ ไม่มีการส่งข้อความไปยังบริการภายนอก" after </span>
html = html.replace(
    '<span data-i18n="coachNote">การประเมินหน้านี้ใช้ Rubric-based evaluator ภายในเบราว์เซอร์ ไม่มีการส่งข้อความไปยังบริการภายนอก</span>ใช้ Rubric-based evaluator ภายในเบราว์เซอร์ ไม่มีการส่งข้อความไปยังบริการภายนอก',
    '<span data-i18n="coachNote">การประเมินหน้านี้ใช้ Rubric-based evaluator ภายในเบราว์เซอร์ ไม่มีการส่งข้อความไปยังบริการภายนอก</span>'
)

# Line 159: remove "ได้ และขยายเมื่อหลักฐานเพิ่มขึ้น" after </span>
html = html.replace(
    '<span data-i18n="effectuation">ลงทุนเท่าที่รับความเสียหายได้ และขยายเมื่อหลักฐานเพิ่มขึ้น</span></p>ได้ และขยายเมื่อหลักฐานเพิ่มขึ้น</p>',
    '<span data-i18n="effectuation">ลงทุนเท่าที่รับความเสียหายได้ และขยายเมื่อหลักฐานเพิ่มขึ้น</span></p>'
)

# Line 173: remove "และไม่ส่งข้อมูลออกจากอุปกรณ์" after </span>
html = html.replace(
    '<span data-i18n="privacy">Prototype นี้ไม่มี Backend และไม่ส่งข้อมูลออกจากอุปกรณ์</span></p> และไม่ส่งข้อมูลออกจากอุปกรณ์</p>',
    '<span data-i18n="privacy">Prototype นี้ไม่มี Backend และไม่ส่งข้อมูลออกจากอุปกรณ์</span></p>'
)

# Fix 2: Add data-i18n-placeholder to reflection1 and reflection3 textareas
html = html.replace(
    '<textarea id="reflection1" placeholder="อธิบายเหตุผลและหลักฐานที่ใช้ตัดสินใจ">',
    '<textarea id="reflection1" data-i18n-placeholder="reflectionQ1Placeholder" placeholder="อธิบายเหตุผลและหลักฐานที่ใช้ตัดสินใจ">'
)
html = html.replace(
    '<textarea id="reflection3" placeholder="กำหนดสมมติฐานหรือการทดสอบครั้งถัดไป">',
    '<textarea id="reflection3" data-i18n-placeholder="reflectionQ3Placeholder" placeholder="กำหนดสมมติฐานหรือการทดสอบครั้งถัดไป">'
)

# Also fix the buyerAnswer textarea placeholder to use data-i18n properly
# (it already has data-i18n-placeholder, so this should work)

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Fixed duplicate text and added missing data-i18n-placeholder attributes")

# Now add the missing translation keys to i18n.js
with open('i18n.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add reflectionQ1Placeholder and reflectionQ3Placeholder to TH
js = js.replace(
    "reflectionPlaceholder: 'ระบุสิ่งที่ได้เรียนรู้จากตัวเลขหรือการทดลอง...',",
    "reflectionQ1Placeholder: 'อธิบายเหตุผลและหลักฐานที่ใช้ตัดสินใจ...',\n    reflectionPlaceholder: 'ระบุสิ่งที่ได้เรียนรู้จากตัวเลขหรือการทดลอง...',\n    reflectionQ3Placeholder: 'กำหนดสมมติฐานหรือการทดสอบครั้งถัดไป...',\n"
)

# Add to EN
js = js.replace(
    "reflectionPlaceholder: 'Note what you learned from the numbers or experiments...',",
    "reflectionQ1Placeholder: 'Explain your reasoning and the evidence behind it...',\n    reflectionPlaceholder: 'Note what you learned from the numbers or experiments...',\n    reflectionQ3Placeholder: 'Define the next hypothesis or test...',\n"
)

# Add to ZH
js = js.replace(
    "reflectionPlaceholder: '记录你从数字或实验中学到的东西...',",
    "reflectionQ1Placeholder: '解释你的推理和证据...',\n    reflectionPlaceholder: '记录你从数字或实验中学到的东西...',\n    reflectionQ3Placeholder: '定义下一个假设或测试...',\n"
)

# Add to the second TH block (if there's a zh2 or en2)
# Check if there are more blocks
if "reflectionPlaceholder" in js:
    # Count occurrences
    count = js.count("reflectionPlaceholder")
    print(f"reflectionPlaceholder appears {count} times")
    if count == 3:
        # Only TH, EN, ZH - good
        pass
    elif count > 3:
        # There might be duplicate language blocks
        print("⚠️ Warning: More than 3 language blocks found")

with open('i18n.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("✅ Added missing translation keys to i18n.js")

# Verify syntax
import subprocess
result = subprocess.run(['node', '--check', 'i18n.js'], capture_output=True, text=True)
if result.returncode == 0:
    print("✅ i18n.js syntax OK")
else:
    print(f"❌ i18n.js syntax error: {result.stderr}")

result = subprocess.run(['node', '--check', 'index.html'], capture_output=True, text=True)
# HTML can't be checked with node --check, that's fine
