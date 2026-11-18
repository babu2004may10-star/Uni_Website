# Northbridge University Website — Progress

Last updated: 2026-11-18

## Project scope

A responsive, accessible single-page university website with academics, admissions, campus life, research, news, events, and contact information.

Northbridge University is a fictional institution created for this website concept. Program details, dates, statistics, names, and contact information are demonstration content rather than real-world claims.

## Completed

- [x] Established the site scope and content plan.
- [x] Created the `css/` and `js/` project folders.
- [x] Initialized this implementation log.
- [x] Built the semantic homepage with hero, quick links, about, programme explorer, admissions, campus life, research, news, events, visit form, and footer.
- [x] Added programme detail, news story, funding, research, and website-information dialogs.
- [x] Added a custom university favicon.
- [x] Added the complete visual design system, responsive layouts, and mobile breakpoints.
- [x] Added sticky-header state, accessible mobile navigation, and Escape/outside-click handling.
- [x] Added live programme search, level filters, school filtering, result counts, empty state, and filter reset.
- [x] Added programme, news, funding, research, and privacy dialogs with focus restoration.
- [x] Added custom visit-form validation, inline errors, success feedback, and body scroll locking.
- [x] Verified JavaScript syntax with `node --check`.
- [x] Replaced the one unavailable image and confirmed all remote photography returns HTTP 200.
- [x] Passed 34/34 browser checks covering navigation, filtering, dialogs, form validation, and horizontal overflow.
- [x] Passed automated WCAG 2.2 A/AA checks with zero violations on desktop, mobile, dialogs, privacy panel, form errors, and the open mobile menu.
- [x] Added `README.md` with setup instructions, feature summary, project structure, customisation guidance, accessibility notes, validation, and deployment steps.
- [x] Added `.gitignore` for local Git Credential Manager diagnostics.

## In progress

Nothing. The planned website is complete.

## Verification

- JavaScript syntax: passed.
- Browser behavior suite: 34/34 checks passed in Microsoft Edge.
- Accessibility: 0 automated WCAG 2.2 A/AA violations across six tested page states.
- Duplicate element IDs: none.
- Missing internal anchor targets: none.
- Links without destinations: none.
- Remote images: all tested URLs return HTTP 200.
- Horizontal overflow: none at 1440px or 390px.
- Font loading requires internet access; the design includes Georgia/Arial fallbacks.

## Next steps

- Optional production work: connect the visit form to a university CRM or form service, add a CMS for news and programme updates, replace demonstration biographies and statistics with verified institutional content, self-host approved photography and fonts, and run assistive-technology testing with real users.

## Change log

### 2026-11-17 — Project setup

- Added the project structure and implementation progress log.

### 2026-11-18 — Semantic page and content

- Added all planned content sections with in-page navigation and calls to action.
- Added an accessible programme directory with nine demonstration programmes and filtering hooks.
- Added admissions steps, campus gallery, research feature, news stories, and event listings.
- Added reusable modal dialogs for programme, news, funding, research, and privacy information.
- Added a visit-request form with validation hooks and privacy disclosure.
- Added a custom SVG favicon.

### 2026-11-18 — Visual design and responsive layout

- Added the university colour palette, editorial typography, spacing system, and reusable components.
- Styled the hero, programme directory, admissions timeline, campus gallery, research feature, news, events, contact form, footer, and dialogs.
- Added responsive layouts for tablet and mobile, including a horizontally scrollable campus gallery.
- Added reduced-motion, keyboard focus, selection, and print-independent interaction styles.

### 2026-11-18 — Interaction and accessibility behavior

- Added mobile navigation with expansion state, scroll locking, Escape support, and focus management.
- Added live programme filtering by search term, study level, and school, with announced result counts and a reset action.
- Added keyboard-accessible modal dialogs for programme details, news stories, research, and funding.
- Added the privacy and accessibility panel with focus trapping and focus restoration.
- Added inline visit-form validation, accessible error relationships, and demonstration success feedback.
- Added reduced-motion support and a sticky header state.

### 2026-11-18 — Validation and content corrections

- Corrected all automated colour-contrast findings, including reversed white text on the coral panels and footer text.
- Fixed brand accessible names, small contact-link touch targets, and mobile gallery keyboard access.
- Closed the programme dialog when its apply link navigates to admissions.
- Standardised contact and fee content to UK currency and phone formatting.
- Replaced one unavailable external image and confirmed every remaining remote image loads.
- Recorded final browser, link, image, and WCAG validation results.

### 2026-11-18 — Documentation

- Added a project README covering local use, features, file structure, content editing, imagery, forms, accessibility, validation, and deployment.
- Documented the fictional nature of the university and the lack of a project licence.
- Recorded the README and ignore-file additions in this progress log.
