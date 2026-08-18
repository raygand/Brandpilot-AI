import re

with open('index.html', 'r') as f:
    html = f.read()

# Fix all missing data-i18n attributes
replacements = [
    # Line 45: heroTitle
    ('<h1 id="heroTitle">ทดลองก่อนลงทุน<br/><em>เรียนรู้ก่อนเสี่ยงจริง</em></h1>',
     '<h1 id="heroTitle" data-i18n="heroTitle">ทดลองก่อนลงทุน<br/><em>เรียนรู้ก่อนเสี่ยงจริง</em></h1>'),
    
    # Line 87: inputHint
    ('<span id="inputHint">ระบบจะแสดงสูตรและเตือนเมื่อข้อมูลยังไม่สมเหตุผล',
     '<span id="inputHint" data-i18n="inputHint">ระบบจะแสดงสูตรและเตือนเมื่อข้อมูลยังไม่สมเหตุผล'),
    
    # Line 105: assumption text
    ('<b>คะแนนคำนวณจากข้อมูลที่ผู้ใช้กรอกและกติกาจำลอง ไม่ใช่คำรับรองความสำเร็จ',
     '<b data-i18n="assumptionText">คะแนนคำนวณจากข้อมูลที่ผู้ใช้กรอกและกติกาจำลอง ไม่ใช่คำรับรองความสำเร็จ'),
    
    # Line 111: reflection prompt text
    ('<p><b>Reflection prompt</b> จุดอ่อนข้อใดเปลี่ยนการตัดสินใจของคุณมากที่สุด?</p>',
     '<p><b>Reflection prompt</b> <span data-i18n="reflectionPromptText">จุดอ่อนข้อใดเปลี่ยนการตัดสินใจของคุณมากที่สุด?</span></p>'),
    
    # Line 133: buyerQuestion
    ('<h3 id="buyerQuestion">เหตุใดสินค้านี้จึงควรได้พื้นที่ขาย?</h3>',
     '<h3 id="buyerQuestion" data-i18n="buyerQuestion">เหตุใดสินค้านี้จึงควรได้พื้นที่ขาย?</h3>'),
    
    # Line 134: buyerPrompt
    ('<p id="buyerPrompt">ตอบด้วยปัญหาลูกค้า หลักฐาน และความแตกต่างที่ตรวจสอบได้</p>',
     '<p id="buyerPrompt" data-i18n="buyerPrompt">ตอบด้วยปัญหาลูกค้า หลักฐาน และความแตกต่างที่ตรวจสอบได้</p>'),
    
    # Line 139: buyerAnswer placeholder
    ('<textarea id="buyerAnswer" placeholder="พิมพ์คำตอบของคุณ โดยใช้ตัวเลขและเกณฑ์ตัดสินใจ...">',
     '<textarea id="buyerAnswer" data-i18n-placeholder="buyerAnswerPlaceholder" placeholder="พิมพ์คำตอบของคุณ โดยใช้ตัวเลขและเกณฑ์ตัดสินใจ...">'),
    
    # Line 154: roadmapTitle
    ('<h2 id="roadmapTitle">เปลี่ยนข้อสังเกตให้เป็นการทดลองที่ลงมือได้',
     '<h2 id="roadmapTitle" data-i18n="roadmapTitle">เปลี่ยนข้อสังเกตให้เป็นการทดลองที่ลงมือได้'),
    
    # Line 167: reflectionQ2
    ('<label for="reflection2">2. ผลลัพธ์ใดต่างจากที่คาด?</label>',
     '<label for="reflection2" data-i18n="reflectionQ2">2. ผลลัพธ์ใดต่างจากที่คาด?</label>'),
    
    # Line 167: reflection2 placeholder
    ('<textarea id="reflection2" placeholder="ระบุสิ่งที่ได้เรียนรู้จากตัวเลขหรือ',
     '<textarea id="reflection2" data-i18n-placeholder="reflectionPlaceholder" placeholder="ระบุสิ่งที่ได้เรียนรู้จากตัวเลขหรือ'),
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        count += 1
        print(f"✅ Replaced: {old[:60]}...")
    else:
        print(f"❌ NOT FOUND: {old[:60]}...")

print(f"\nTotal replacements: {count}/{len(replacements)}")

with open('index.html', 'w') as f:
    f.write(html)

print("index.html updated successfully")
