# Northbridge University

A responsive university website concept available in two forms:

- **Streamlit app** (`app.py`) — the Python version to run and deploy with Streamlit.
- **Static website** (`index.html`) — the original framework-free HTML, CSS, and JavaScript version.

Northbridge University is a fictional institution. All programmes, people, statistics, dates, fees, events, and contact details are demonstration content rather than real-world claims.

## Streamlit highlights

- Six navigable sections: Discover, Study, Admissions, Campus life, Research & news, and Visit
- Live programme search with study-level and school filters
- Programme detail dialogs with entry requirements and career pathways
- Admissions timeline, campus gallery, research feature, news, and events
- News story dialogs
- Visit-request form with inline validation and success feedback
- Custom editorial styling built on Streamlit's native widgets
- Responsive layout for desktop, tablet, and mobile
- Demonstration content clearly labelled as fictional

## Run the Streamlit app

### Prerequisites

- Python 3.10 or newer
- Internet access for remote photography and fonts

### Setup

```sh
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```sh
# macOS or Linux
source .venv/bin/activate
```

Install dependencies and start the app:

```sh
pip install -r requirements.txt
streamlit run app.py
```

Open the local URL printed by Streamlit, usually <http://localhost:8501>.

The app reads visual settings from `.streamlit/config.toml`; no secrets or environment variables are required.

## Run the static website

Open `index.html` directly in a browser, or serve it locally:

```sh
npx serve .
```

Remote photography is loaded from Unsplash and fonts from Google Fonts. Local fallback fonts are included.

## Project structure

```text
.
├── .streamlit/
│   └── config.toml
├── assets/
│   └── favicon.svg
├── css/
│   └── styles.css
├── js/
│   └── main.js
├── .gitignore
├── app.py
├── index.html
├── progress.md
├── README.md
└── requirements.txt
```

## Customisation

### Streamlit app

#### Programmes

Programmes are defined in the `PROGRAMMES` list near the top of `app.py`. Each entry provides the filterable metadata, summary, and dialog content:

```python
{
    "title": "Environmental Science",
    "level": "Undergraduate",
    "school": "Science & Engineering",
    "award": "BSc · 3 years",
    "summary": "Read the planet. Design a more resilient future.",
    "description": "...",
    "careers": "...",
    "requirements": "...",
    "number": "03",
}
```

Add an entry to `PROGRAMMES` and it appears in the directory automatically. Keep `level` values consistent with the filter options.

#### News stories

Stories live in the `STORIES` list in `app.py`. Each dialog reads its content from the selected story.

#### Brand, colours, and typography

The interface styles are in the CSS block passed to `st.markdown` in `app.py`. Theme values are also set in `.streamlit/config.toml`. Update both when changing the primary colours, font-family stack, or page background.

The design uses Fraunces for display headings and Manrope for body text, with local fallback fonts.

#### Visit form

The form validates name, email, interest, and consent, then displays demonstration success feedback. It does not transmit or persist data. Connect the `submitted` branch in `render_visit()` to a CRM, email service, or database before launch, and update the privacy wording.

### Static website

- Brand and design tokens: CSS custom properties at the top of `css/styles.css`.
- Programmes: programme cards in `index.html`, with filter and dialog data stored as attributes.
- News stories: the `stories` object in `js/main.js`.
- Images: replace remote Unsplash URLs with approved, locally hosted photography.
- Forms: the static form only simulates submission; connect it to a backend service before launch.

## Accessibility

Both versions include semantic headings, labelled controls, visible focus styles, keyboard-operable dialogs, and responsive layouts. The static version adds a skip link and screen-reader-announced programme results.

Automated testing of the Streamlit app reported zero WCAG 2.2 A/AA violations across Discover desktop, Study, the programme dialog, and mobile Discover. Automated checks do not replace testing with assistive-technology users.

## Validation performed

Streamlit app:

- Python syntax compiled successfully
- 27 browser checks covering all six sections, programme filtering, dialogs, form validation, responsive overflow, and runtime errors
- Automated accessibility audit with axe-core against WCAG 2.2 A/AA

Static website:

- `node --check js/main.js`
- 34 browser checks covering navigation, filtering, dialogs, form validation, and horizontal overflow
- Automated accessibility audit with axe-core against WCAG 2.2 A/AA
- Internal anchor, duplicate-ID, remote-image, and link checks

## Deployment

### Streamlit Community Cloud

1. Push the repository to GitHub.
2. Sign in at <https://share.streamlit.io>.
3. Choose **New app**, select the repository and branch, and set the main file to `app.py`.
4. Deploy. Streamlit installs dependencies from `requirements.txt`.

No secrets are required for the current demonstration app.

### Other hosts

The Streamlit app can run on any Python host that supports long-lived web processes, such as a container platform or virtual machine:

```sh
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
```

The static version can be hosted on GitHub Pages, Netlify, Cloudflare Pages, or any static web host. All asset paths are relative, so it works from a repository subpath.

## Project status

See [progress.md](progress.md) for implemented features, change history, verification results, and suggested production next steps.

## Licence

No licence has been added. Add an appropriate licence before redistributing or reusing the project outside its intended demonstration context.
