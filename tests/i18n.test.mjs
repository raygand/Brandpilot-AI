import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { parseHTML } from 'linkedom';

const html = await readFile(new URL('../index.html', import.meta.url), 'utf8');
const application = await readFile(new URL('../app.js', import.meta.url), 'utf8');
const storage = new Map([['brandpilot-lang', 'zh']]);
Object.defineProperty(globalThis, 'navigator', {value:{language:'en-US'}, configurable:true});
globalThis.localStorage = {getItem:key=>storage.get(key)??null,setItem:(key,value)=>storage.set(key,String(value))};
const i18n = await import('../i18n.js');

function freshDocument() {
  const {document, window} = parseHTML(html);
  globalThis.document = document;
  globalThis.window = window;
  return document;
}
function leaves(value, prefix='') {
  return Object.entries(value).flatMap(([key,item])=>item&&typeof item==='object'?leaves(item,`${prefix}${key}.`):[`${prefix}${key}`]).sort();
}
function get(value, path) { return path.split('.').reduce((object,key)=>object?.[key],value); }

test('a saved language takes precedence over browser language', () => {
  assert.equal(i18n.currentLang, 'zh');
});

test('all three dictionaries have identical keys, nonempty values and matching replacement tokens', () => {
  const expected = leaves(i18n.I18N.th);
  for(const language of ['th','en','zh']) {
    assert.deepEqual(leaves(i18n.I18N[language]), expected, language);
    for(const path of expected) {
      const translated = get(i18n.I18N[language],path);
      assert.equal(typeof translated,'string',`${language}.${path}`);
      assert.ok(translated.trim(), `${language}.${path} empty`);
      const tokens = text=>[...text.matchAll(/\{([^{}]+)\}/g)].map(match=>match[1]).sort();
      assert.deepEqual(tokens(translated),tokens(get(i18n.I18N.th,path)),`${language}.${path} replacements`);
    }
  }
});

test('all literal app lookups and HTML translation attributes resolve in every language', () => {
  const document = freshDocument();
  const keys = new Set([...application.matchAll(/\bt\(\s*['"]([^'"]+)['"]/g)].map(match=>match[1]));
  for(const element of document.querySelectorAll('*')) for(const attribute of element.attributes) {
    if(attribute.name === 'data-i18n' || attribute.name.startsWith('data-i18n-')) keys.add(attribute.value);
  }
  for(const language of ['th','en','zh']) for(const key of keys) {
    assert.notEqual(get(i18n.I18N[language], key), undefined,`${language}.${key} missing`);
  }
});

test('30 language switches preserve live score node, drafts, selected inputs and dynamic result values', () => {
  const document = freshDocument();
  const score = document.querySelector('#scoreHeadline');
  score.textContent = '83';
  const answer = document.querySelector('#buyerAnswer');
  answer.value = 'My buyer evidence 123';
  document.querySelector('#reflection1').value = 'สมมติฐานและเหตุผล';
  document.querySelector('#price').value = '92.5';
  const live = document.querySelector('#confidenceValue');
  live.textContent = 'LIVE VALUE';
  // Regression: old releases annotated app-rendered values as static translations.
  live.setAttribute('data-i18n','confidenceValues.medium');
  document.querySelector('#buyerQuestion').textContent = 'ACTIVE QUESTION 4';
  document.querySelector('#buyerQuestion').setAttribute('data-i18n','buyerQuestion');
  for(let iteration=0;iteration<10;iteration++) for(const language of ['th','en','zh']) {
    assert.equal(i18n.setLanguage(language),true);
    assert.equal(document.querySelector('#scoreHeadline'),score);
    assert.equal(score.textContent,'83');
    assert.equal(answer.value,'My buyer evidence 123');
    assert.equal(document.querySelector('#reflection1').value,'สมมติฐานและเหตุผล');
    assert.equal(document.querySelector('#price').value,'92.5');
    assert.equal(live.textContent,'LIVE VALUE');
    assert.equal(document.querySelector('#buyerQuestion').textContent,'ACTIVE QUESTION 4');
    assert.equal(document.querySelectorAll('#scoreHeadline').length,1);
    assert.equal(document.querySelector('score'),null);
    assert.equal(document.querySelector('.rail nav').getAttribute('aria-label'),i18n.t('railLabel'));
    assert.equal(document.querySelector('.lang-btn[aria-pressed="true"]').dataset.lang,language);
    assert.equal(document.querySelector('button.nav').getAttribute('aria-label'),i18n.t('navAria')[0]);
  }
});

test('rich descriptions render line breaks, nested guardrail survives, and expanded formula stays expanded', () => {
  const document = freshDocument();
  const formula = document.querySelector('#formulaToggle');
  formula.setAttribute('aria-expanded','true');
  document.querySelector('#formulaDetails').hidden=false;
  for(const language of ['th','en','zh']) {
    i18n.setLanguage(language);
    for(const key of ['heroTitle','inputDesc','productMeta','reflectionTitle','scenarioDesc']) {
      const element=document.querySelector(`[data-i18n="${key}"]`);
      assert.ok(element.querySelector('br'),`${language}.${key}`);
      assert.ok(!element.textContent.includes('<br'),`${language}.${key} literal markup`);
    }
    assert.equal(document.querySelectorAll('.guardrail-label').length,1);
    assert.equal(document.querySelector('.guardrail-copy').textContent,i18n.t('guardrail'));
    assert.equal(formula.textContent,i18n.t('formulaToggleClose'));
    assert.equal(document.querySelector('#formulaDetails').hidden,false);
  }
});

test('locale normalization and literal replacement are safe', () => {
  freshDocument();
  assert.equal(i18n.setLanguage('zh-CN'),true);
  assert.equal(i18n.currentLang,'zh');
  assert.equal(document.documentElement.lang,'zh-Hans');
  assert.equal(i18n.setLanguage('xx'),false);
  assert.equal(i18n.currentLang,'zh');
  i18n.setLanguage('en');
  assert.equal(i18n.t('questionNavLabel',{n:'$& $$ <value>'}),'Question $& $$ <value>');
  assert.equal(i18n.t('rubricLabels',{unused:'ignored'}).clarity,'CLARITY');
  assert.equal(i18n.t('priorities.demand',{unused:1}).length,2);
});

test('blocked storage does not prevent language changes or translations', () => {
  freshDocument();
  const previous=globalThis.localStorage;
  globalThis.localStorage={getItem(){throw Error('blocked');},setItem(){throw Error('blocked');}};
  assert.doesNotThrow(()=>i18n.setLanguage('th'));
  assert.equal(i18n.currentLang,'th');
  assert.equal(document.querySelector('[data-i18n="heroStart"]').textContent,i18n.t('heroStart'));
  globalThis.localStorage=previous;
});
