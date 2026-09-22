# BRANDPILOT AI logic audit

Reviewed original `app.js` (614 lines) and its `index.html` / `i18n.js` contracts on 2026-09-22. Line numbers below refer to that pre-repair source. This is a source audit, not evidence of browser testing.

## Findings and required behavior

| Priority | Original location | Finding | Required behavior |
| --- | --- | --- | --- |
| P0 | app.js 40–42 | Defaults were prepended to saved arrays and sliced to their original length, discarding every saved answer, score and reflection on reload. | Restore validated saved entries by index; preserve drafts and invalidate malformed scores. |
| P0 | app.js 7, 74–83, 138–150, 330–343, 398–403 | Invalid strings were silently stripped or coerced to zero; every recalculation ran before validation; direct navigation bypassed the input gate. | Parse complete numeric input; reject non-finite values and fractional stocks/days; prevent results, recommendations and export from using invalid inputs. |
| P1 | app.js 118 | Stress-case discount exceeded the user's declared maximum; a separate 45% cap also silently changed a valid 60% scenario. | Apply the user's maximum consistently and disclose the effective discount of each scenario. |
| P1 | app.js 122–135 | Recommendations ignored required capital and available inventory. Broad rollout required 4.55× budget and 2.5× inventory while still eligible for a recommendation. No safe “none” outcome existed when every scenario lost money per unit. | Show capital/inventory shortfalls; exclude unfunded or uncovered scenarios; return no recommendation when none has positive unit contribution. |
| P1 | app.js 123, 205–209 | Projected contribution was computed but total result after launch spending was never shown. A positive unit margin could be mistaken for total profit. | Show contribution less launch outlay separately; a pilot recommendation is not a profitability claim. |
| P1 | app.js 106, 177–178 | Confidence used Thai values as dictionary keys and wrote the translated result into the confidence label rather than its value. | Use stable high/medium/low keys and update `confidenceValue`. |
| P1 | app.js 412–427 | Editing or deleting an evaluated answer retained its previous score and average. | Clear the affected score immediately after a draft changes; evaluate the current draft only. |
| P1 | app.js 266–281 | Text-feature rubric lacked Chinese vocabulary and omitted common English economics/reason/evidence words. Length-heavy scoring favored longer scripts. | Use comparable Thai, English and Chinese concepts; explain that the heuristic does not verify factual truth or semantic answer quality. |
| P1 | app.js 49–50, 348; i18n.js 609–614 | Storage access was unguarded in saving/reset/language initialization. Browsers denying storage could prevent initialization or all interactions. | Keep the app usable in memory and explain failed persistence without pretending it saved. |
| P1 | app.js 601–610 | Browser-language detection ran after dynamic rendering and overrode the user's stored language. | Validate and respect saved language; initialize translations before dynamic render. |
| P1 | app.js 531–563 | AudioContext creation was unguarded and occurred before overlay close handlers. Unsupported audio could prevent cleanup. Audio contexts were never closed. | Sound must be optional; establish an immediately operable close route; clean up timers/contexts on every close. |
| P2 | app.js 566–583 | Language changes reset translated dynamic values without updating input hints, validation or formula open-state label; many scenario/rubric/export labels remained English. | Render all state-derived text in the active language without changing entered data, score or chosen scenario. |
| P2 | app.js 330–343, 449–452 | Navigation was memory-only, had no URL/history support or focus transfer; global arrow navigation also ran while a dialog was open. | Support shareable current step and browser back/forward; respect forms/dialogs; move focus to the active screen. |
| P2 | app.js 429–436 | Empty reflections could be marked complete, editing did not clear the saved badge, and unsaved reflections were lost on reload. | Distinguish saved draft from completed reflection and persist or clearly flag draft changes. |
| P2 | app.js 355–391 | Export was English-only and omitted channel, evidence, lead time, detailed scenarios, assumptions and buyer answers. Object URL was revoked immediately after clicking an unattached anchor. | Export the complete current session in the selected language; append the download element and revoke after the browser has started handling it. |
| P2 | app.js 464–564 | WOW presented a local deterministic rules engine as “AI-powered”, with nonessential motion/audio, no Escape close or reduced-motion path. | Identify rules-based simulation, preserve accurate current results, support dismissal/keyboard focus/reduced motion, and avoid overlapping runs. |

## Core repair verification

`core.js` contains the isolated deterministic model and validated state restoration. `node --test tests/core.test.mjs` passes 15 substantive tests covering:

- Independent default sessions and full draft/score/reflection persistence.
- Corrupt saved fields, score totals, bounds and stale draft metadata.
- Strict grouped numeric parsing; blank/garbage/non-finite input rejection.
- Valid financial and integer boundaries.
- Hand-calculated default readiness, net price, contribution, break-even units and shortfalls.
- Maximum discounts in every scenario, including 60%.
- Budget/inventory recommendation gates and no-viable-scenario outcome.
- A boundary sweep for bounded scores and finite monetary results.
- Equivalent Thai, English and Chinese rubric outcomes; empty and weak answers.

The original scenario investment multipliers (1×, 2×, 4.55× launch budget) and inventory multipliers (0.333×, 1×, 2.5×) are retained as disclosed assumptions. With one budget input, the latter two scenarios require additional capital and therefore cannot be automatically recommended. A funded pilot with positive unit contribution can still lose money after launch spending; that loss must remain visible.

Browser navigation, translated DOM, persistence-denied behavior, downloads, overlays, focus and responsive layout require separate integration/UI verification after the app adapter is repaired. These checks are not claimed by the core tests.
