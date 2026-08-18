"""
Map data-i18n attributes in index.html to the EXISTING keys in i18n.js.
The translations already exist — we just need to use the correct key names.
"""

# Mapping: my_data_i18n_key -> existing_i18n_key
key_mapping = {
    # Nav
    'nav0': 'nav',  # handled by array
    'nav1': 'nav',
    'nav2': 'nav',
    'nav3': 'nav',
    'nav4': 'nav',
    'nav5': 'nav',
    'nav6': 'nav',
    # Topbar
    'caseChipLabel': 'caseChip',
    'modeLabel': 'mode',
    'resetTop': 'resetTop',
    'wowLabel': 'wowLabel',
    # Hero
    'heroEyebrow': 'heroEyebrow',
    'heroLead': 'heroLead',
    'heroStart': 'heroStart',
    'guardrail': 'guardrail',
    'heroProof0': 'heroProof',  # handled by array
    'heroProof1': 'heroProof',
    'heroProof2': 'heroProof',
    'disclaimer': 'disclaimer',
    # Screen 1
    'inputTitle': 'inputTitle',
    'inputSubtitle': 'inputDesc',
    'productMeta': 'productMeta',
    'liveGrossLabel': 'liveEconLabel',
    'liveMarginSuffix': 'liveMarginSuffix',
    'formLabelPrice': 'formLabels.price',
    'formLabelCost': 'formLabels.cost',
    'formLabelBudget': 'formLabels.budget',
    'formLabelStock': 'formLabels.stock',
    'formLabelChannel': 'formLabels.channel',
    'formLabelDiscount': 'formLabels.discount',
    'formLabelEvidence': 'formLabels.evidence',
    'formLabelLeadTime': 'formLabels.leadTime',
    'unitBaht': 'formUnits.price',  # all units use same key per type
    'unitUnit': 'formUnits.stock',
    'unitPercent': 'formUnits.discount',
    'unitDay': 'formUnits.leadTime',
    'selectOnline': 'channelOptions.online',
    'selectBalanced': 'channelOptions.balanced',
    'selectModern': 'channelOptions.modern',
    'evidenceIdea': 'evidenceOptions.idea',
    'evidenceInterviews': 'evidenceOptions.interviews',
    'evidencePilot': 'evidenceOptions.pilot',
    'inputHint': 'inputHint',
    'analyzeBtn': 'analyzeBtn',
    'backBtn': 'backBtn',
    # Screen 2
    'readinessTitle': 'readinessTitle',
    'confidenceLabel': 'confidenceLabel',
    'confidenceValue': 'confidenceValues.medium',
    'priorityTitle': 'nextBestTest',
    'priorityCopy': 'priorities.demand',
    'assumptionNote': 'assumptionText',
    'formulaToggle': 'formulaToggleOpen',
    'formulaDetails': 'formulaDetails',
    'reflectionPrompt': 'reflectionPrompt',
    'nextScenarios': 'nextScenarios',
    # Screen 3
    'scenarioTitle': 'scenarioTitle',
    'scenarioSubtitle': 'scenarioDesc',
    'formulaMainLabel': 'formulaText',
    'formulaMainText': 'formulaText',
    'formulaAssumptions': 'formulaNote',
    'yourDecision': 'decisionText',
    'decisionReason': 'decisionReasons.balanced',
    'whyRecommended': 'whyRecommended',
    'decisionRule': 'decisionRuleText',
    'nextBuyer': 'nextBuyer',
    # Screen 4
    'buyerTitle': 'buyerTitle',
    'roundLabel': 'questionNavLabel',
    'yourResponse': 'buyerResponse',
    'buyerPlaceholder': 'buyerPlaceholder',
    'charCount': 'charCount',
    'evaluateBtn': 'evaluateBtn',
    'outOf100': 'charCount',
    'strengthLabel': 'strengthLabel',
    'improveLabel': 'improveLabel',
    'buyerStrengthDefault': 'buyerStrengthDefault',
    'buyerImproveDefault': 'buyerImproveDefault',
    'coachNote': 'coachNote',
    'buyerAverageNone': 'buyerAverageNone',
    'nextRoadmap': 'nextRoadmap',
    # Screen 5
    'roadmapTitle': 'roadmapTitle',
    'roadmapBudgetLabel': 'roadmapKeys.budget',
    'roadmapContributionLabel': 'roadmapKeys.contribution',
    'roadmapGateLabel': 'roadmapKeys.gate',
    'effectuationNote': 'effectuation',
    'nextReflection': 'nextReflection',
    # Screen 6
    'reflectionTitle': 'reflectionTitle',
    'reflectionSubtitle': 'reflectionDesc',
    'reflectionQ1': 'reflectionQ1',
    'reflectionQ2': 'reflectionQ2',
    'reflectionQ3': 'reflectionQ3',
    'saveReflectionBtn': 'saveReflection',
    'downloadBtn': 'downloadSummary',
    'completeNote': 'completeText',
    'privacyNote': 'privacy',
    'restartBtn': 'restartBtn',
    # Dialog
    'dialogTitle': 'dialogTitle',
    'dialogClose': 'dialogClose',
}

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace data-i18n values with correct keys
for old_key, new_key in key_mapping.items():
    html = html.replace(f'data-i18n="{old_key}"', f'data-i18n="{new_key}"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed data-i18n keys in index.html to match existing i18n.js keys")

# Verify
import re
keys_in_html = set(re.findall(r'data-i18n="([^"]+)"', html))
print(f"\nUnique data-i18n keys in HTML: {len(keys_in_html)}")
