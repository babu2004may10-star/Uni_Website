# Northbridge University Website — Progress

Last updated: 2026-11-18

## Project scope

A responsive, accessible university website delivered as both a Streamlit Python app and a static HTML/CSS/JavaScript site. It covers academics, admissions, campus life, research, news, events, and contact information.

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
- [x] Added a Streamlit version in `app.py` with six navigable sections and a custom responsive visual system.
- [x] Added live programme search, study-level and school filters, clearable results, programme dialogs, and news dialogs to the Streamlit app.
- [x] Added the admissions timeline, campus gallery, research feature, events, and validated visit form to the Streamlit app.
- [x] Added `requirements.txt`, Streamlit theme configuration, and local virtual-environment setup.
- [x] Passed 27/27 Streamlit browser checks and a zero-violation WCAG 2.2 A/AA audit across four app states.
- [x] Updated the README with Streamlit setup, customisation, validation, and deployment guidance.

## In progress

Nothing. Both the Streamlit app and static website are complete.

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

### 2026-11-18 — Streamlit application

- Installed Python 3.12 and Streamlit 1.51 in a local virtual environment.
- Created `app.py` as a native Streamlit version with custom HTML/CSS presentation.
- Added Discover, Study, Admissions, Campus life, Research & news, and Visit sections with button and radio navigation.
- Rebuilt programme search, level and school filters, result counts, clear-filters behavior, programme detail dialogs, and news story dialogs.
- Added the admissions image and deadline panel, expandable application steps and funding guidance, campus photo grid, research feature, and event list.
- Added a visit form with name, email, interest, consent, and message fields, plus accessible error and success feedback.
- Added Streamlit theme settings and `requirements.txt`.
- Added Python virtual environments, bytecode, and local Streamlit secrets to `.gitignore`.
- Verified all six sections, filtering, dialogs, the form, mobile layout, and absence of runtime errors with 27 browser checks.
- Fixed low-contrast labels and caption opacity found by automated accessibility testing.
- Updated the README to document both the Streamlit app and the original static site.
