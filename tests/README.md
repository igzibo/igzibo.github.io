# Regression Tests

Static-site regression suite: broken links/assets, HTML validity, accessibility
(axe-core), and visual regression (screenshot diffing).

## Setup (one-time)

Using the project virtual environment:

```powershell
C:\Users\ryans\code\venvs\igzibo-github-io\Scripts\python.exe -m pip install -r requirements-dev.txt
C:\Users\ryans\code\venvs\igzibo-github-io\Scripts\python.exe -m playwright install chromium
```

## Run all tests

```powershell
C:\Users\ryans\code\venvs\igzibo-github-io\Scripts\python.exe -m pytest -v
```

## Test suites

- `test_links.py` — confirms every internal `href`/`src` resolves to a real file.
- `test_html_validity.py` — runs the W3C Nu Html Checker (skipped automatically if Java isn't on PATH).
- `test_accessibility.py` — runs axe-core against each page in `pages.py`.
- `test_visual_regression.py` — screenshots each page at mobile/tablet/desktop widths and diffs against `tests/baselines/`.
  - First run auto-creates baselines (tests are skipped so you can review the screenshot).
  - To intentionally approve a visual change, delete the corresponding file under `tests/baselines/` and re-run.
  - Failing diffs are written to `tests/__diffs__/` (gitignored) for inspection.

## Adding a new page

Add its path to the `PAGES` list in `tests/pages.py` — it will automatically be covered by both the accessibility and visual regression suites.

## Known pre-existing findings (not caused by these tests)

Running the suite today surfaced real, pre-existing accessibility issues that predate this test suite:
- `color-contrast`: the `--accent` teal (`#06B6D4`) fails WCAG AA contrast on white/light backgrounds in several places (nav links, buttons, inline text links).
- `landmark-one-main` / `region`: pages don't wrap their primary content in a `<main>` landmark.

These were not introduced by adding the tests and are left for a separate, deliberate fix.
