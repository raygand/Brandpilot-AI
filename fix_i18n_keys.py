import re

with open('i18n.js', 'r') as f:
    content = f.read()

# New keys to add to ALL 3 languages
new_keys = {
    'heroTitle': 'heroTitle',
    'inputHint': 'inputHint',
    'assumptionText': 'assumptionText',
    'reflectionPromptText': 'reflectionPromptText',
    'buyerQuestion': 'buyerQuestion',
    'buyerPrompt': 'buyerPrompt',
    'buyerAnswerPlaceholder': 'buyerAnswerPlaceholder',
    'roadmapTitle': 'roadmapTitle',
    'reflectionQ2': 'reflectionQ2',
    'reflectionPlaceholder': 'reflectionPlaceholder',
}

# TH translations
th_additions = {
    'heroTitle': 'ทดลองก่อนลงทุน<br/><em>เรียนรู้ก่อนเสี่ยงจริง</em>',
    'inputHint': 'ระบบจะแสดงสูตรและเตือนเมื่อข้อมูลยังไม่สมเหตุผล',
    'assumptionText': 'คะแนนคำนวณจากข้อมูลที่ผู้ใช้กรอกและกติกาจำลอง ไม่ใช่คำรับรองความสำเร็จ',
    'reflectionPromptText': 'จุดอ่อนข้อใดเปลี่ยนการตัดสินใจของคุณมากที่สุด?',
    'buyerQuestion': 'เหตุใดสินค้านี้จึงควรได้พื้นที่ขาย?',
    'buyerPrompt': 'ตอบด้วยปัญหาลูกค้า หลักฐาน และความแตกต่างที่ตรวจสอบได้',
    'buyerAnswerPlaceholder': 'พิมพ์คำตอบของคุณ โดยใช้ตัวเลขและเกณฑ์ตัดสินใจ...',
    'roadmapTitle': 'เปลี่ยนข้อสังเกตให้เป็นการทดลองที่ลงมือได้',
    'reflectionQ2': '2. ผลลัพธ์ใดต่างจากที่คาด?',
    'reflectionPlaceholder': 'ระบุสิ่งที่ได้เรียนรู้จากตัวเลขหรือการทดลอง...',
}

# EN translations
en_additions = {
    'heroTitle': 'Test before invest<br/><em>Learn before you risk</em>',
    'inputHint': 'System shows formulas and warns when data seems unreasonable',
    'assumptionText': 'Score is calculated from user-inputted data and simulation rules. Not a guarantee of success.',
    'reflectionPromptText': 'Which weakness would most change your decision?',
    'buyerQuestion': 'Why should this product get shelf space?',
    'buyerPrompt': 'Answer with customer problems, evidence, and verifiable differentiation.',
    'buyerAnswerPlaceholder': 'Type your answer using numbers and decision criteria...',
    'roadmapTitle': 'Turn insights into actionable experiments',
    'reflectionQ2': '2. Which result differed from expectations?',
    'reflectionPlaceholder': 'Note what you learned from the numbers or experiments...',
}

# ZH translations
zh_additions = {
    'heroTitle': '投资前先测试<br/><em>冒险前先学习</em>',
    'inputHint': '系统展示公式并在数据不合理时发出警告',
    'assumptionText': '分数由用户输入数据和模拟规则计算，不是成功保证',
    'reflectionPromptText': '哪个弱点最会改变你的决定？',
    'buyerQuestion': '为什么这个产品应该获得货架空间？',
    'buyerPrompt': '用客户问题、证据和可验证的差异化来回答',
    'buyerAnswerPlaceholder': '用数字和决策标准输入你的答案...',
    'roadmapTitle': '把观察变成可执行的实验',
    'reflectionQ2': '2. 哪个结果与预期不同？',
    'reflectionPlaceholder': '记录你从数字或实验中学到的东西...',
}

# Function to insert keys after a specific existing key in a language block
def insert_after_key(content, lang, after_key, new_key, value):
    # Find the pattern for the language block
    # Look for the key in the specific language section
    pattern = rf'(    {re.escape(after_key)}: [^\n]*\n)'
    match = re.search(pattern, content)
    if match:
        insert_pos = match.end()
        new_line = f'    {new_key}: \'{value}\',\n'
        content = content[:insert_pos] + new_line + content[insert_pos:]
        return content, True
    return content, False

# For TH block: insert after 'heroStart' key
# For EN block: insert after 'heroStart' key  
# For ZH block: insert after 'heroStart' key

for key, th_val in th_additions.items():
    # Insert in TH section - find 'heroStart: ...' in TH section
    th_pattern = rf'(    heroStart: [^\n]*\n)'
    match = re.search(th_pattern, content)
    if match:
        pos = match.end()
        new_line = f'    {key}: \'{th_val}\',\n'
        # Check if key already exists
        if f'    {key}: ' not in content[:pos + 500]:
            content = content[:pos] + new_line + content[pos:]
            print(f"✅ TH: Added {key}")
        else:
            print(f"⏭️  TH: {key} already exists")

for key, en_val in en_additions.items():
    en_pattern = rf'(    heroStart: [^\n]*\n)'
    matches = list(re.finditer(en_pattern, content))
    # Use the second occurrence (EN section)
    if len(matches) >= 2:
        pos = matches[1].end()
        new_line = f'    {key}: \'{en_val}\',\n'
        # Check if key already exists in EN section
        en_section_start = matches[1].start()
        en_section_end = matches[1].start() + 20000  # rough estimate
        if f'    {key}: ' not in content[en_section_start:en_section_end]:
            content = content[:pos] + new_line + content[pos:]
            print(f"✅ EN: Added {key}")
        else:
            print(f"⏭️  EN: {key} already exists")

for key, zh_val in zh_additions.items():
    zh_pattern = rf'(    heroStart: [^\n]*\n)'
    matches = list(re.finditer(zh_pattern, content))
    # Use the third occurrence (ZH section)
    if len(matches) >= 3:
        pos = matches[2].end()
        new_line = f'    {key}: \'{zh_val}\',\n'
        # Check if key already exists in ZH section
        zh_section_start = matches[2].start()
        if f'    {key}: ' not in content[zh_section_start:zh_section_start + 20000]:
            content = content[:pos] + new_line + content[pos:]
            print(f"✅ ZH: Added {key}")
        else:
            print(f"⏭️  ZH: {key} already exists")

with open('i18n.js', 'w') as f:
    f.write(content)

print("\n✅ i18n.js updated successfully")
