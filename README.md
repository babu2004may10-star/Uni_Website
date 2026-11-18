# Northbridge University

A responsive university website concept built with semantic HTML, modern CSS, and dependency-free JavaScript.

Northbridge University is a fictional institution. All programmes, people, statistics, dates, fees, events, and contact details are demonstration content rather than real-world claims.

## Highlights

- Editorial, photography-led responsive design for desktop, tablet, and mobile
- Accessible navigation with a keyboard-friendly mobile menu
- Live programme search and filtering by study level and school
- Programme detail dialogs with entry requirements and career pathways
- Admissions timeline, campus gallery, research feature, news, and events
- Modal content for news stories, research, fees, and funding
- Visit-request form with inline validation and accessible feedback
- Reduced-motion support, visible focus states, and WCAG 2.2 AA styling
- No frameworks, build step, or runtime dependencies

## Run locally

The site is entirely static. Open `index.html` directly in a browser, or serve the project locally:

```sh
npx serve .
```

Then open the local URL printed by the command.

For the best experience, use a current version of Chrome, Edge, Firefox, or Safari with internet access. Remote photography is loaded from Unsplash and fonts are loaded from Google Fonts; local fallback fonts are included.

## Project structure

```text
.
├── assets/
│   └── favicon.svg
├── css/
│   └── styles.css
├── js/
│   └── main.js
├── .gitignore
├── index.html
├── progress.md
└── README.md
```

## Customisation

### Brand and design tokens

Colours, typography, spacing, shadows, and container width are defined as CSS custom properties at the top of `css/styles.css`.

```css
:root {
  --ink: #17332f;
  --coral-deep: #b8432a;
  --cream: #f3efe5;
  --serif: "Fraunces", Georgia, serif;
  --sans: "Manrope", "Helvetica Neue", Arial, sans-serif;
}
```

### Programmes

Programme cards live in `index.html`. Each card carries the filter and dialog data as attributes:

```html
<article
  class="programme-card"
  data-level="undergraduate"
  data-school="School of Science &amp; Engineering"
  data-title="Environmental Science BSc"
  data-type="BSc · 3 years"
  data-description="..."
  data-careers="..."
  data-requirements="...">
```

Update the relative filter values consistently when adding or removing a programme.

### News stories

News dialog content is stored in the `stories` object in `js/main.js`. Each trigger references a matching key through `data-story-key`.

### Imagery

Images use Unsplash URLs with size and crop parameters. Replace them with locally hosted, appropriately licensed photography before production use. Update the hero preload and Open Graph metadata in `index.html` when changing the main image.

### Forms

The visit form currently demonstrates validation and success feedback only. It does not transmit or store data. Connect the `submit` handler in `js/main.js` to a form service or university CRM before launch, and update the privacy disclosure accordingly.

## Accessibility

The site includes:

- A skip link and semantic landmarks
- Keyboard-operable menus, dialogs, filters, and form controls
- Visible focus styles and `Escape` handling for overlays
- Meaningful alternative text and labelled form fields
- Screen-reader result announcements for programme filtering
- Respect for `prefers-reduced-motion`

Automated WCAG 2.2 A/AA testing reported zero violations across the homepage, programme dialog, privacy panel, form-error state, mobile layout, and open mobile menu. Automated checks do not replace testing with assistive technology users.

## Validation performed

- `node --check js/main.js`
- 34 browser checks covering navigation, filtering, dialogs, form validation, and horizontal overflow
- Automated accessibility audit with axe-core against WCAG 2.2 A/AA
- Internal anchor and duplicate-ID checks
- Remote image availability checks

## Deployment

This is a static site and can be hosted on GitHub Pages, Netlify, Cloudflare Pages, or any static web host.

### GitHub Pages

1. Open the repository's **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Select the `main` branch and the repository root, then save.
4. GitHub will publish the site at the Pages URL shown in that panel.

All asset paths are relative, so the site works from a repository subpath without configuration.

## Project status

See [progress.md](progress.md) for the implemented features, change history, verification results, and suggested production next steps.

## Licence

No licence has been added. Add an appropriate licence before redistributing or reusing the project outside its intended demonstration context.
