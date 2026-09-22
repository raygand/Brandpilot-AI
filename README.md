# BRANDPILOT AI

Interactive brand strategy learning prototype for product readiness, scenario planning, Virtual Buyer practice, and 30–60–90 day action planning.

## What the prototype does

- Calculates a Brand Readiness Score from eight editable product inputs.
- Recalculates three go-to-market scenarios and Unit Economics in real time.
- Lets the learner select a scenario and see a connected 90-day roadmap.
- Scores five Virtual Buyer answers with a transparent, browser-based rubric.
- Saves Reflection responses locally and exports a plain-text session summary.
- Works on desktop, tablet, and mobile without a backend.

## Academic and privacy note

DR.MUSCLE, all financial figures, formulas, thresholds, and scenario outputs are fictional simulation assumptions for learning. They are not market facts, financial advice, or a guarantee of commercial success.

The prototype stores progress only in the current browser via `localStorage`. It does not transmit user input to an external service.

## Run locally

```bash
npm install
npm run dev
```

## Production build

```bash
npm run build
```

The static build is generated in `dist/` and deployed automatically to GitHub Pages from the `main` branch.

## September 2026 functional repair

- Thai, English and Simplified Chinese cover navigation, static/dynamic results, validation, dialogs, and exported summaries. A saved language takes precedence over browser language.
- Seven routes support browser Back/Forward and direct hash links. Only the active screen is exposed to keyboard focus.
- Invalid numbers block analysis. Valid edits recalculate readiness, three scenarios, and the selected roadmap.
- Five buyer answers, scores, reflections and selection survive reloads. Editing an answer invalidates its previous score. Local storage failures show a message and leave in-memory use available.
- Financial comparison discloses GP, effective discounts, variable channel costs, launch-outlay and sales multipliers. Discounts respect the entered maximum. Extra launch budget and stock are shown; unfunded choices are not recommended. Positive unit contribution does not imply overall launch profit.
- The strategy recap is a closeable native dialog and respects reduced motion; it displays existing calculated results, not generative AI inference.
- `npm test` runs 29 calculation, persistence, translation, and application DOM regression cases before Pages deployment. Browser QA evidence and limits are recorded in `docs/qa/release-2026-09-22.md`.
