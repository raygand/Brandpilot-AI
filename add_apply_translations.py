# Read current file
content = open('i18n.js').read()

# Add applyTranslations function before the export line
apply_fn = """
// Apply all translations to DOM
window.applyTranslations = function applyTranslations() {
  const data = I18N[currentLang];
  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  // Nav labels
  $$('.nav b').forEach((el, i) => { if (data.nav && data.nav[i]) el.textContent = data.nav[i]; });

  // Topbar
  if ($('#caseChipLabel')) $('#caseChipLabel').textContent = data.caseChipLabel || '';
  if ($('#modeLabel')) $('#modeLabel').textContent = data.modeLabel || '';
  if ($('#resetTop')) $('#resetTop').textContent = data.resetTop || '';
  if ($('#wowBtn')) {
    $('#wowBtn').innerHTML = `<i></i>${data.wowLabel || '✨ WOW MODE'}`;
  }

  // Hero
  if ($('#heroTitle')) $('#heroTitle').textContent = data.heroTitle || '';
  const lead = $('.lead');
  if (lead) lead.innerHTML = data.heroLead || '';
  const guardrail = $('.guardrail');
  if (guardrail) guardrail.textContent = data.heroGuardrail || '';
  // Hero proof items
  const proofItems = $$('.hero-proof span');
  if (data.heroProof && proofItems.length) {
    proofItems.forEach((el, i) => { if (data.heroProof[i]) el.textContent = data.heroProof[i]; });
  }
  // Hero start button
  const startBtn = $('.primary[data-next]');
  if (startBtn) startBtn.textContent = data.heroStart || '';

  // Input screen
  if ($('#inputTitle')) $('#inputTitle').textContent = data.inputTitle || '';
  // Form labels
  Object.entries(data.formLabels || {}).forEach(([key, label]) => {
    const el = $(`#label_${key}`) || $(`label[for="${key}"]`);
    if (el) el.textContent = label;
  });
  // Form units
  Object.entries(data.formUnits || {}).forEach(([key, unit]) => {
    const el = $(`#unit_${key}`);
    if (el) el.textContent = unit;
  });
  // Select options
  $$('.form-select option').forEach(opt => {
    const idx = parseInt(opt.value) - 1;
    if (data.selectOptions && data.selectOptions[idx]) opt.textContent = data.selectOptions[idx];
  });
  if ($('#inputHint')) $('#inputHint').textContent = data.inputHint || '';
  if ($('#analyze')) $('#analyze').textContent = data.analyzeBtn || '';

  // Readiness screen
  if ($('#readinessTitle')) $('#readinessTitle').textContent = data.readinessTitle || '';
  if ($('#formulaToggle')) $('#formulaToggle').textContent = data.formulaToggleOpen || '';
  if ($('#confidenceLabel span')) $('#confidenceLabel span').textContent = data.confidence || '';

  // Scenario screen
  if ($('#scenarioTitle')) $('#scenarioTitle').textContent = data.scenarioTitle || '';

  // Buyer screen
  if ($('#buyerTitle')) $('#buyerTitle').textContent = data.buyerTitle || '';
  if ($('#buyerAnswer')) {
    const q = data.buyerQuestions?.[0];
    if (q) $('#buyerAnswer').placeholder = q.prompt || '';
  }
  if ($('#evaluate')) $('#evaluate').textContent = data.evaluateBtn || '';

  // Roadmap screen
  if ($('#roadmapTitle')) $('#roadmapTitle').textContent = data.roadmapTitle || '';

  // Reflection screen
  if ($('#reflectionTitle')) $('#reflectionTitle').textContent = data.reflectionTitle || '';
  // Reflection labels
  const reflLabels = $$('.reflection-label, .reflection-item label');
  if (data.reflectionLabels) {
    reflLabels.forEach((el, i) => { if (data.reflectionLabels[i]) el.textContent = data.reflectionLabels[i]; });
  }
  // Reflection placeholders
  const reflInputs = $$('.reflection-item textarea, .reflection-item input');
  if (data.reflectionPlaceholders) {
    reflInputs.forEach((el, i) => { if (data.reflectionPlaceholders[i]) el.placeholder = data.reflectionPlaceholders[i]; });
  }
  if ($('#saveReflection')) $('#saveReflection').textContent = data.saveReflectionBtn || '';
  if ($('#downloadSummary')) $('#downloadSummary').textContent = data.downloadBtn || '';
  if ($('#restart')) $('#restart').textContent = data.restartBtn || '';

  // Dialog
  if ($('#reasonDialog h3')) $('#reasonDialog h3').textContent = data.dialogTitle || '';
  if ($('#closeDialog')) $('#closeDialog').textContent = data.dialogClose || '';
};
"""

# Insert before the export line
content = content.replace(
    "export { I18N, currentLang, setLanguage, t };",
    apply_fn + "\nexport { I18N, currentLang, setLanguage, t };"
)

open('i18n.js', 'w').write(content)
print(f"applyTranslations added. Total lines: {len(content.split(chr(10)))}")
