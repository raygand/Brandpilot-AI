/**
 * Deterministic educational simulation. There is no model inference or external
 * market data here. Rates below are disclosed scenario assumptions, not forecasts.
 */
export const defaults = Object.freeze({
  price: 79, cost: 31, budget: 180000, stock: 6000,
  channel: 'balanced', discount: 15, evidence: 'interviews', leadTime: 30,
  selectedScenario: 'balanced', currentQuestion: 0, reflectionSubmitted: false,
  buyerAnswers: Object.freeze(['', '', '', '', '']),
  buyerScores: Object.freeze([null, null, null, null, null]),
  reflections: Object.freeze(['', '', ''])
});

export const inputLimits = Object.freeze({
  price: 1e9, cost: 1e9, budget: 1e12, stock: 1e9,
  discount: 60, leadTime: 365
});
const clamp = (value, min, max) => Math.max(min, Math.min(max, value));
const fields = ['price', 'cost', 'budget', 'stock', 'discount', 'leadTime'];
const rubricMax = Object.freeze({ clarity: 20, evidence: 30, economics: 25, channel: 15, risk: 10 });

export function freshState() {
  return { ...defaults, buyerAnswers: [...defaults.buyerAnswers],
    buyerScores: [...defaults.buyerScores], reflections: [...defaults.reflections] };
}

/** Accept a complete ASCII decimal, optionally with correctly grouped commas. */
export function parseNumeric(value) {
  if (typeof value === 'number') return Number.isFinite(value) ? value : NaN;
  if (typeof value !== 'string') return NaN;
  const text = value.trim();
  if (!/^-?(?:(?:\d+|\d{1,3}(?:,\d{3})+)(?:\.\d*)?|\.\d+)$/.test(text)) return NaN;
  const result = Number(text.replaceAll(',', ''));
  return Number.isFinite(result) ? result : NaN;
}

export function validateState(state) {
  if (!state || typeof state !== 'object') return [...fields, 'channel', 'evidence'];
  const errors = [];
  for (const field of fields) {
    const value = state[field];
    const minimum = ['price', 'budget'].includes(field) ? 0.01
      : ['stock', 'leadTime'].includes(field) ? 1 : 0;
    if (!Number.isFinite(value) || value < minimum || value > inputLimits[field]
      || (['stock', 'leadTime'].includes(field) && !Number.isInteger(value))) errors.push(field);
  }
  if (!['online', 'balanced', 'modern'].includes(state.channel)) errors.push('channel');
  if (!['idea', 'interviews', 'pilot'].includes(state.evidence)) errors.push('evidence');
  return errors;
}

function normalizedScore(score, answer) {
  if (!score || typeof score !== 'object' || answer.trim().length < 20) return null;
  const result = {};
  for (const [key, maximum] of Object.entries(rubricMax)) {
    if (!Number.isInteger(score[key]) || score[key] < 0 || score[key] > maximum) return null;
    result[key] = score[key];
  }
  result.total = Object.values(result).reduce((sum, value) => sum + value, 0);
  if (score.total !== result.total) return null;
  // A score from a different draft must never survive a restore.
  if (typeof score.answer === 'string' && score.answer !== answer.trim()) return null;
  return result;
}

export function normalizeState(saved) {
  const result = freshState();
  if (!saved || typeof saved !== 'object' || Array.isArray(saved)) return result;
  for (const field of fields) {
    const value = parseNumeric(saved[field]);
    const candidate = { ...result, [field]: value };
    if (!validateState(candidate).includes(field)) result[field] = value;
  }
  if (['online', 'balanced', 'modern'].includes(saved.channel)) result.channel = saved.channel;
  if (['idea', 'interviews', 'pilot'].includes(saved.evidence)) result.evidence = saved.evidence;
  if (['conservative', 'balanced', 'aggressive'].includes(saved.selectedScenario)) result.selectedScenario = saved.selectedScenario;
  if (Number.isInteger(saved.currentQuestion)) result.currentQuestion = clamp(saved.currentQuestion, 0, 4);
  for (const [field, length] of [['buyerAnswers', 5], ['reflections', 3]]) {
    if (Array.isArray(saved[field])) result[field] = Array.from({ length }, (_, i) =>
      typeof saved[field][i] === 'string' ? saved[field][i].slice(0, 10000) : '');
  }
  result.reflectionSubmitted = saved.reflectionSubmitted === true && result.reflections.every(answer => answer.trim().length > 0);
  if (Array.isArray(saved.buyerScores)) result.buyerScores = result.buyerAnswers.map((answer, i) => normalizedScore(saved.buyerScores[i], answer));
  return result;
}

function requireValid(state) {
  const invalid = validateState(state);
  if (invalid.length) throw new RangeError(`Invalid simulation fields: ${invalid.join(', ')}`);
}

export function calculateReadiness(state) {
  requireValid(state);
  const grossMarginRate = (state.price - state.cost) / state.price;
  const budgetPerUnit = state.budget / state.stock;
  const demand = { idea: 6, interviews: 11, pilot: 18 }[state.evidence];
  const economics = clamp(Math.round(grossMarginRate * 23), 0, 20);
  const channelBase = { online: 12, balanced: 10, modern: 7 }[state.channel];
  const channelBudgetBoost = budgetPerUnit >= 40 ? 3 : budgetPerUnit >= 25 ? 1 : 0;
  const channel = clamp(channelBase + channelBudgetBoost, 0, 15);
  const supply = state.leadTime <= 21 ? 14 : state.leadTime <= 30 ? 11 : state.leadTime <= 45 ? 8 : 5;
  const marketing = clamp(Math.round(budgetPerUnit / 3.3), 3, 15);
  const risk = clamp(9 + (state.evidence === 'pilot' ? 3 : 0) - (state.discount > 25 ? 2 : 0) - (state.cost >= state.price ? 4 : 0), 2, 15);
  const metrics = [
    { key: 'demand', score: demand, max: 20 }, { key: 'economics', score: economics, max: 20 },
    { key: 'channel', score: channel, max: 15 }, { key: 'supply', score: supply, max: 15 },
    { key: 'marketing', score: marketing, max: 15 }, { key: 'risk', score: risk, max: 15 }
  ];
  return { score: metrics.reduce((sum, item) => sum + item.score, 0), metrics,
    grossMarginRate, budgetPerUnit, confidence: { idea: 'low', interviews: 'medium', pilot: 'high' }[state.evidence] };
}

export const scenarioConfigs = Object.freeze([
  Object.freeze({ id: 'conservative', number: '01', name: 'CONSERVATIVE', label: 'Online Test', subtitle: 'Online test first', gp: .23, variable: 3, discountFactor: .5, unitsFactor: .333, investmentFactor: 1 }),
  Object.freeze({ id: 'balanced', number: '02', name: 'BALANCED', label: 'Balanced Pilot', subtitle: 'Online + selected retail', gp: .22, variable: 4, discountFactor: 1, unitsFactor: 1, investmentFactor: 2 }),
  Object.freeze({ id: 'aggressive', number: '03', name: 'AGGRESSIVE', label: 'Modern Trade Rollout', subtitle: 'Broad retail rollout', gp: .35, variable: 6, discountFactor: 1.34, unitsFactor: 2.5, investmentFactor: 4.55 })
]);

export function calculateScenarios(state, readiness = calculateReadiness(state)) {
  requireValid(state);
  const scenarios = scenarioConfigs.map(config => {
    // The user's maximum discount is a hard constraint, including the stress case.
    const discountRate = Math.min(state.discount / 100, (state.discount / 100) * config.discountFactor);
    const netPrice = state.price * (1 - discountRate) * (1 - config.gp);
    const contribution = netPrice - state.cost - config.variable;
    const units = Math.max(1, Math.round(state.stock * config.unitsFactor));
    // Fixed launch outlay is additional to per-unit production/channel costs.
    const investment = state.budget * config.investmentFactor;
    const projectedContribution = contribution * units;
    const breakEvenUnits = contribution > 0 ? Math.ceil(investment / contribution) : Infinity;
    const cashGap = Math.max(0, investment - state.budget);
    const inventoryGap = Math.max(0, units - state.stock);
    const withinBudget = cashGap === 0;
    const withinInventory = inventoryGap === 0;
    const profitAfterInvestment = projectedContribution - investment;
    // Viable means a funded unit-economics pilot, not guaranteed profit or demand.
    const viable = contribution > 0 && withinBudget && withinInventory;
    let risk = config.id === 'conservative' && contribution > 0 ? 'LOW' : 'MEDIUM';
    if (profitAfterInvestment < 0 || state.evidence !== 'pilot') risk = 'MEDIUM';
    if (config.id === 'aggressive' || contribution <= 8 || !withinBudget || !withinInventory) risk = 'HIGH';
    return { ...config, discountRate, netPrice, contribution, units, investment,
      projectedContribution, breakEvenUnits, risk, cashGap, inventoryGap,
      profitAfterInvestment, withinBudget, withinInventory, viable };
  });
  const preferred = readiness.score >= 80 && state.evidence === 'pilot'
    ? ['aggressive', 'balanced', 'conservative']
    : readiness.score >= 52 ? ['balanced', 'conservative'] : ['conservative'];
  const recommended = preferred.find(id => {
    const scenario = scenarios.find(item => item.id === id);
    return scenario.viable && (id === 'conservative' || scenario.contribution >= (id === 'aggressive' ? 12 : 10));
  }) || null;
  return { scenarios, recommended };
}

/** Text-feature rubric, not semantic AI grading or verification of any claim. */
export function evaluateBuyerAnswer(answer) {
  // NFC preserves Thai sara am (ำ); NFKC decomposes it and breaks Thai keywords.
  const text = typeof answer === 'string' ? answer.trim().normalize('NFC') : '';
  if (!text) return { clarity: 0, evidence: 0, economics: 0, channel: 0, risk: 0, total: 0 };
  const hasNumber = /\p{Nd}/u.test(text);
  const hasReason = /(เพราะ|ดังนั้น|เนื่องจาก|เพื่อให้|because|therefore|so that|since|因为|因此|所以|由于|为了)/iu.test(text);
  const evidenceWords = /(ข้อมูล|หลักฐาน|ทดลอง|สัมภาษณ์|ซื้อซ้ำ|data|evidence|interview|repeat purchase|conversion|sell.through|pilot|test|数据|证据|试验|测试|访谈|复购|转化|试点)/iu.test(text);
  const economicWords = /(ราคา|ต้นทุน|กำไร|ส่วนลด|โปรโมชั่น|บาท|คุ้มทุน|price|cost|profit|contribution|margin|\bgp\b|discount|promotion|baht|break.even|价格|成本|利润|贡献|毛利|折扣|促销|泰铢|盈亏平衡)/iu.test(text);
  const profitWords = /(contribution|profit|break.even|กำไร|คุ้มทุน|利润|贡献|盈亏平衡)/iu.test(text);
  const channelWords = /(online|retail|modern trade|ร้าน|สาขา|buyer|ช่องทาง|ชั้นวาง|sell.through|ออนไลน์|ค้าปลีก|零售|线上|买手|渠道|货架|门店)/iu.test(text);
  const monitorWords = /(รายสัปดาห์|ติดตาม|วัดผล|ยอดขาย|kpi|sales|weekly|monitor|track|conversion|stock cover|每周|跟踪|监测|衡量|销量|转化|库存覆盖)/iu.test(text);
  const riskWords = /(หยุด|เกณฑ์|ความเสี่ยง|ทบทวน|ต่ำกว่า|สูงกว่า|stop|iterate|scale|trigger|review|risk|threshold|below|above|停止|门槛|风险|迭代|扩大|触发|复盘|低于|高于)/iu.test(text);
  const conceptCount = [evidenceWords, economicWords, channelWords, monitorWords, riskWords].filter(Boolean).length;
  // Concepts carry the weight; equivalent Chinese text is not penalized for brevity.
  const clarity = clamp(6 + Math.min(6, conceptCount * 2) + (hasReason ? 4 : 0) + (text.length >= 20 ? 4 : 0), 0, 20);
  const evidence = clamp((hasNumber ? 14 : 4) + (evidenceWords ? 12 : 3) + (evidenceWords && hasReason ? 4 : 0), 0, 30);
  const economics = clamp((economicWords ? 14 : 4) + (hasNumber ? 8 : 2) + (profitWords ? 3 : 0), 0, 25);
  const channel = clamp((channelWords ? 8 : 2) + (monitorWords ? 7 : 2), 0, 15);
  const risk = clamp((riskWords ? 6 : 1) + (hasNumber ? 4 : 1), 0, 10);
  return { clarity, evidence, economics, channel, risk, total: clarity + evidence + economics + channel + risk };
}
