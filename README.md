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
