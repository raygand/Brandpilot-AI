import test from 'node:test';
import assert from 'node:assert/strict';
import { freshState, normalizeState, parseNumeric, validateState, calculateReadiness,
  calculateScenarios, evaluateBuyerAnswer } from '../core.js';

test('fresh sessions never share mutable answers, scores, or reflections', () => {
  const first = freshState(); const second = freshState();
  first.buyerAnswers[0] = 'draft'; first.reflections[0] = 'learning';
  assert.equal(second.buyerAnswers[0], ''); assert.equal(second.reflections[0], '');
});

test('restore retains all five answers/scores and three reflections', () => {
  const saved = freshState();
  saved.buyerAnswers = Array.from({ length: 5 }, (_, i) => `Because pilot data ${i + 1} shows retail profit, track weekly and stop below 10.`);
  saved.buyerScores = saved.buyerAnswers.map(evaluateBuyerAnswer);
  saved.reflections = ['เลือกทดสอบตลาด', 'ต้นทุนสูงกว่าคาด', 'ทดสอบราคาใหม่'];
  saved.currentQuestion = 4; saved.selectedScenario = 'conservative';
  assert.deepEqual(normalizeState(JSON.parse(JSON.stringify(saved))), saved);
});

test('corrupt stored fields reset independently without losing valid writing', () => {
  const restored = normalizeState({ price: '-12', cost: 'garbage', budget: '200,000',
    stock: 2.5, discount: 95, leadTime: null, evidence: 'made-up', channel: {},
    currentQuestion: 120, buyerAnswers: ['Valid draft', null], reflections: ['Keep me'],
    buyerScores: [{ total: 999 }], selectedScenario: 'missing' });
  assert.equal(restored.price, 79); assert.equal(restored.cost, 31);
  assert.equal(restored.budget, 200000); assert.equal(restored.stock, 6000);
  assert.equal(restored.currentQuestion, 4); assert.equal(restored.buyerAnswers[0], 'Valid draft');
  assert.equal(restored.reflections[0], 'Keep me');
  assert.deepEqual(restored.buyerScores, [null, null, null, null, null]);
  assert.deepEqual(validateState(restored), []);
  for (const invalid of [null, 0, 'string', [], true]) assert.deepEqual(normalizeState(invalid), freshState());
});

test('stored score cannot be negative, exceed its rubric, or contradict its total', () => {
  const answer = 'Because pilot evidence 10 shows profit in retail, monitor weekly and stop below 5.';
  const valid = evaluateBuyerAnswer(answer);
  for (const score of [{ ...valid, total: 0 }, { ...valid, risk: 11 }, { ...valid, clarity: -1 },
    { ...valid, evidence: '30' }, { ...valid, answer: 'old draft' }]) {
    assert.equal(normalizeState({ buyerAnswers: [answer], buyerScores: [score] }).buyerScores[0], null);
  }
});

test('numeric parsing accepts decimal and grouped input, never silently removes garbage', () => {
  for (const [input, expected] of [['180,000', 180000], [' 1,234.50 ', 1234.5], ['-.5', -.5], ['.25', .25], ['79.', 79], ['-12', -12], [79, 79]]) assert.equal(parseNumeric(input), expected);
  for (const input of ['', ' ', null, false, {}, [], 'abc', '1e3', '79 baht', '1,2', '1,00,000', '1.2.3', 'Infinity', Infinity, NaN]) assert.ok(Number.isNaN(parseNumeric(input)), String(input));
});

test('invalid numbers and fractional unit/day inputs are blocked before calculation', () => {
  const invalid = { ...freshState(), price: 0, cost: -1, budget: Infinity,
    stock: 2.5, discount: NaN, leadTime: 1.5 };
  assert.deepEqual(validateState(invalid), ['price', 'cost', 'budget', 'stock', 'discount', 'leadTime']);
  assert.throws(() => calculateReadiness(invalid), RangeError);
  assert.throws(() => calculateScenarios(invalid), RangeError);
  assert.ok(validateState({ ...freshState(), price: Number.MIN_VALUE }).includes('price'));
});

test('valid boundaries include free production cost and zero discount', () => {
  assert.deepEqual(validateState({ ...freshState(), cost: 0, discount: 0, stock: 1, leadTime: 365 }), []);
  assert.ok(validateState({ ...freshState(), discount: 60.001 }).includes('discount'));
  assert.ok(validateState({ ...freshState(), stock: 1e10 }).includes('stock'));
});

test('default readiness is 65 and confidence uses stable language-neutral keys', () => {
  const readiness = calculateReadiness(freshState());
  assert.equal(readiness.score, 65); assert.equal(readiness.confidence, 'medium');
  assert.equal(readiness.metrics.reduce((sum, item) => sum + item.max, 0), 100);
  assert.equal(calculateReadiness({ ...freshState(), evidence: 'idea' }).confidence, 'low');
  assert.equal(calculateReadiness({ ...freshState(), evidence: 'pilot' }).confidence, 'high');
});

test('hand-calculated default unit economics and required additional capital match', () => {
  const { scenarios, recommended } = calculateScenarios(freshState());
  const conservative = scenarios[0]; const balanced = scenarios[1]; const aggressive = scenarios[2];
  assert.ok(Math.abs(conservative.netPrice - 56.26775) < 1e-9);
  assert.ok(Math.abs(conservative.contribution - 22.26775) < 1e-9);
  assert.equal(conservative.units, 1998); assert.equal(conservative.breakEvenUnits, 8084);
  assert.equal(balanced.investment, 360000); assert.equal(balanced.cashGap, 180000);
  assert.equal(aggressive.inventoryGap, 9000); assert.equal(aggressive.cashGap, 639000);
  assert.equal(recommended, 'conservative');
  assert.ok(conservative.profitAfterInvestment < 0); // A learning pilot is not a claim of profit.
  assert.equal(conservative.risk, 'MEDIUM');
});

test('all scenario discounts respect the user maximum, including stress case and 60%', () => {
  for (const discount of [0, .5, 15, 45, 60]) {
    const { scenarios } = calculateScenarios({ ...freshState(), discount });
    for (const scenario of scenarios) {
      assert.ok(scenario.discountRate <= discount / 100);
      assert.ok(scenario.discountRate >= 0);
    }
    assert.equal(scenarios[1].discountRate, discount / 100);
    assert.equal(scenarios[2].discountRate, discount / 100);
  }
});

test('high readiness never recommends unfunded expansion or sales beyond opening inventory', () => {
  const state = { ...freshState(), price: 999, cost: 1, leadTime: 5, evidence: 'pilot', channel: 'online', budget: 1e6 };
  const readiness = calculateReadiness(state);
  assert.ok(readiness.score >= 80);
  const { scenarios, recommended } = calculateScenarios(state, readiness);
  const selected = scenarios.find(item => item.id === recommended);
  assert.ok(selected.withinBudget); assert.ok(selected.withinInventory); assert.ok(selected.viable);
  assert.equal(scenarios[1].withinBudget, false); assert.equal(scenarios[2].withinInventory, false);
});

test('no viable unit economics returns no recommendation, never a losing default', () => {
  const { scenarios, recommended } = calculateScenarios({ ...freshState(), price: 20, cost: 31 });
  assert.equal(recommended, null);
  for (const scenario of scenarios) {
    assert.equal(scenario.viable, false); assert.equal(scenario.risk, 'HIGH');
    assert.equal(scenario.breakEvenUnits, Infinity); assert.ok(scenario.contribution < 0);
  }
});

test('property sweep keeps readiness and financial outputs finite for supported inputs', () => {
  for (const price of [.01, 79, 1e9]) for (const cost of [0, 31, 1e9]) for (const discount of [0, 60]) {
    const state = { ...freshState(), price, cost, discount };
    const readiness = calculateReadiness(state);
    assert.ok(readiness.score >= 0 && readiness.score <= 100);
    for (const metric of readiness.metrics) assert.ok(metric.score >= 0 && metric.score <= metric.max);
    const result = calculateScenarios(state, readiness);
    for (const scenario of result.scenarios) {
      for (const field of ['netPrice', 'contribution', 'units', 'investment', 'projectedContribution', 'cashGap', 'inventoryGap', 'profitAfterInvestment']) assert.ok(Number.isFinite(scenario[field]), field);
      if (scenario.contribution > 0) assert.ok(scenario.breakEvenUnits > 0);
    }
    if (result.recommended) assert.ok(result.scenarios.find(item => item.id === result.recommended).viable);
  }
});

test('equivalent Thai, English and Chinese concept evidence receives the same rubric', () => {
  const answers = [
    'เพราะข้อมูลทดลอง 30 คนสนใจซื้อ กำไร 20 บาทต่อหน่วย ช่องทางร้านค้าปลีก ติดตามรายสัปดาห์ และหยุดหากยอดขายต่ำกว่า 10 หน่วย',
    'Because pilot data from 30 customers supports retail sales with profit of 20 baht, monitor weekly and stop below 10 units.',
    '因为试点数据有30位客户，零售渠道每件利润20泰铢，每周跟踪销量，低于10件就停止。'
  ];
  const scores = answers.map(evaluateBuyerAnswer);
  assert.deepEqual(scores[0], scores[1]); assert.deepEqual(scores[1], scores[2]);
  assert.equal(scores[0].total, 100);
});

test('rubric is bounded and empty responses are unscored', () => {
  assert.equal(evaluateBuyerAnswer('').total, 0);
  assert.equal(evaluateBuyerAnswer(null).total, 0);
  assert.ok(evaluateBuyerAnswer('We are the best product in the whole world.').total < 50);
  for (const answer of ['ก'.repeat(10000), '因为利润100元'.repeat(1000), '<img src=x onerror=alert(1)>']) {
    const score = evaluateBuyerAnswer(answer);
    assert.ok(score.total >= 0 && score.total <= 100);
    assert.equal(score.total, score.clarity + score.evidence + score.economics + score.channel + score.risk);
  }
});
