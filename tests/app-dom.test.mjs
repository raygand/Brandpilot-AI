// DOM-level integration tests. Native browser layout, focus, files and dialogs
// are checked separately in the browser; these shims cover application state.
import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { parseHTML } from 'linkedom';

const {document,window}=parseHTML(await readFile(new URL('../index.html',import.meta.url),'utf8'));
Object.defineProperty(globalThis,'navigator',{value:{language:'en-US'},configurable:true});
globalThis.document=document;globalThis.window=window;
const saved=new Map([['brandpilot-lang','en']]);
globalThis.localStorage={getItem:key=>saved.get(key)||null,setItem:(key,value)=>saved.set(key,String(value)),removeItem:key=>saved.delete(key)};
globalThis.location={hash:''};
globalThis.history={pushState(_state,_title,hash){location.hash=hash;},replaceState(_state,_title,hash){location.hash=hash;}};
globalThis.addEventListener=window.addEventListener.bind(window);
globalThis.matchMedia=()=>({matches:true});
window.confirm=()=>true;
// Linkedom omits several native UI methods and select.value's setter.
Object.defineProperty(window.HTMLSelectElement.prototype,'value',{configurable:true,get(){return this.querySelector('option[selected]')?.value||this.querySelector('option')?.value||'';},set(value){for(const option of this.querySelectorAll('option')){if(option.value===String(value))option.setAttribute('selected','');else option.removeAttribute('selected');}}});
window.HTMLElement.prototype.showModal=function(){this.setAttribute('open','');};
window.HTMLElement.prototype.close=function(){this.removeAttribute('open');this.dispatchEvent(new window.Event('close'));};
const click=selector=>{const element=document.querySelector(selector);assert.ok(element,selector);element.click();};
const input=(id,value)=>{const element=document.getElementById(id);element.value=value;element.dispatchEvent(new window.Event('input',{bubbles:true}));};
const active=()=>document.querySelector('.screen.active');
await import('../app.js');
const {t,currentLang}=await import('../i18n.js');

// Run sequentially: each step exercises the state produced by the previous one.
test('application opens all seven screens in each language without losing score',()=>{
 const score=document.querySelector('#scoreHeadline');
 assert.match(score.textContent,/^\d+$/);
 for(const language of ['th','en','zh']){
  click(`.lang-btn[data-lang="${language}"]`);
  for(let page=0;page<7;page++){
   click(`.nav[data-screen="${page}"]`);
   assert.equal(active().dataset.screen,String(page));
   assert.equal(document.querySelectorAll('.screen:not([hidden])').length,1);
   assert.equal(document.querySelector('#scoreHeadline'),score);
   assert.match(score.textContent,/^\d+$/);
   assert.ok(!active().textContent.includes('<br/>'));
  }
 }
});

test('invalid data blocks analysis and valid edited values update it',()=>{
 input('price','not-a-number');click('.nav[data-screen="2"]');
 assert.equal(active().dataset.screen,'1');
 assert.equal(document.querySelector('#price').getAttribute('aria-invalid'),'true');
 assert.ok(document.querySelector('#formError').textContent);
 input('price','120');click('#analyze');
 assert.equal(active().dataset.screen,'2');
 assert.equal(document.querySelector('#price').getAttribute('aria-invalid'),'false');
 assert.equal(document.querySelector('#formError').textContent,'');
});

test('scenario choice, formula state and buyer answer survive a language change',()=>{
 click('#formulaToggle');assert.equal(document.querySelector('#formulaDetails').hidden,false);
 click('.nav[data-screen="3"]');click('[data-scenario="balanced"] .scenario-select');
 click('.nav[data-screen="4"]');click('[data-question="3"]');
 input('buyerAnswer','Because 30 pilot customers bought the product, price 120 cost 31 contribution 45, monitor retail sales weekly and stop below 10 units.');
 click('#evaluate');
 const score=document.querySelector('#buyerScore').textContent;
 assert.match(score,/^\d+$/);
 click('.lang-btn[data-lang="th"]');
 assert.equal(document.querySelector('#buyerAnswer').value.startsWith('Because 30'),true);
 assert.equal(document.querySelector('#buyerScore').textContent,score);
 assert.equal(document.querySelector('#roundLabel').textContent,t('questionProgress',{n:4,total:5}));
 assert.equal(document.querySelector('[data-scenario="balanced"] .scenario-select').getAttribute('aria-pressed'),'true');
 assert.equal(document.querySelector('#formulaToggle').getAttribute('aria-expanded'),'true');
 input('buyerAnswer','A changed answer requiring a fresh assessment.');
 assert.equal(document.querySelector('#buyerScore').textContent,'—');
 assert.equal(document.querySelector('#buyerImprove').textContent,t('answerChanged'));
});

test('reflection validates completeness, saves three answers and survives language switch',()=>{
 click('.nav[data-screen="6"]');click('#saveReflection');
 assert.equal(document.querySelector('#appStatus').textContent,t('reflectionRequired'));
 input('reflection1','ทดสอบออนไลน์เพราะใช้เงินน้อยและมีหลักฐาน');
 input('reflection2','กำไรหลังหักค่าช่องทางต่ำกว่าที่คาด');
 input('reflection3','จะทดสอบราคาใหม่และติดตามการซื้อซ้ำ');
 click('#saveReflection');
 assert.equal(document.querySelector('#completeState').classList.contains('saved'),true);
 click('.lang-btn[data-lang="zh"]');
 assert.equal(document.querySelector('#completeState b').textContent,t('reflectionSaved'));
 const persisted=JSON.parse(saved.get('brandpilot-ai-prototype-v2'));
 assert.equal(persisted.reflections.length,3);
 assert.equal(persisted.reflections[1],'กำไรหลังหักค่าช่องทางต่ำกว่าที่คาด');
});

test('recommendation and strategy dialogs open and close, reset clears round data',()=>{
 click('.nav[data-screen="3"]');click('#whyRecommended');
 assert.equal(document.querySelector('#reasonDialog').hasAttribute('open'),true);
 click('#closeDialog');assert.equal(document.querySelector('#reasonDialog').hasAttribute('open'),false);
 click('#wowBtn');assert.ok(document.querySelector('.wow-overlay[open]'));
 click('#wowCloseBtn');assert.equal(document.querySelector('.wow-overlay'),null);
 click('#resetTop');assert.equal(document.querySelector('#resetDialog').hasAttribute('open'),true);click('#cancelReset');assert.equal(document.querySelector('#resetDialog').hasAttribute('open'),false);click('#resetTop');click('#confirmReset');
 assert.equal(active().dataset.screen,'0');
 assert.equal(document.querySelector('#price').value,'79');
 assert.equal(document.querySelector('#buyerAnswer').value,'');
 assert.equal(document.querySelector('#reflection1').value,'');
});

test('summary exports contain localized headings and current drafts in every language',async()=>{
 const nativeCreate=URL.createObjectURL,nativeRevoke=URL.revokeObjectURL,nativeTimeout=globalThis.setTimeout;
 const blobs=[];
 URL.createObjectURL=blob=>{blobs.push(blob);return `blob:test-${blobs.length}`;};
 URL.revokeObjectURL=()=>{};
 globalThis.setTimeout=(fn,delay,...args)=>{const timer=nativeTimeout(fn,delay,...args);timer.unref?.();return timer;};
 try{
  input('reflection1','Export must include this exact draft: 中文 ภาษาไทย & evidence 123.');
  for(const language of ['th','en','zh']){
   click(`.lang-btn[data-lang="${language}"]`);click('.nav[data-screen="6"]');click('#downloadSummary');
   const text=await blobs.at(-1).text();
   for(const key of ['title','input','decision','readiness','questions','roadmap','reflection']) assert.ok(text.includes(t(`exportLabels.${key}`)),`${language}.${key}`);
   assert.ok(text.includes('Export must include this exact draft: 中文 ภาษาไทย & evidence 123.'));
   assert.ok(!/exportLabels\.|\{(?:n|score|money|count|avg)\}/.test(text));
   assert.equal(blobs.at(-1).type,'text/plain;charset=utf-8');
  }
  assert.equal(blobs.length,3);
 }finally{URL.createObjectURL=nativeCreate;URL.revokeObjectURL=nativeRevoke;globalThis.setTimeout=nativeTimeout;}
});

test('blocked storage reports the limitation while navigation and language changes still work',()=>{
 const working=globalThis.localStorage;
 globalThis.localStorage={getItem(){throw Error('blocked');},setItem(){throw Error('blocked');},removeItem(){throw Error('blocked');}};
 try{
  input('price','85');click('.nav[data-screen="2"]');
  assert.equal(active().dataset.screen,'2');
  assert.equal(document.querySelector('#appStatus').textContent,t('storageUnavailable'));
  click('.lang-btn[data-lang="en"]');click('.nav[data-screen="6"]');
  assert.equal(document.querySelector('#completeState span').textContent,t('storageUnavailable'));
 }finally{globalThis.localStorage=working;}
});
