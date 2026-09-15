"""Run axe-core accessibility scans against key pages.

Flags color-contrast, missing labels, and other WCAG issues covered by
copilot-instructions.md's accessibility requirements.
"""
import pytest
from axe_playwright_python.sync_playwright import Axe

from tests.pages import PAGES

axe = Axe()


@pytest.mark.parametrize("path", PAGES)
def test_no_accessibility_violations(page, base_url, path):
    page.goto(f"{base_url}{path}", wait_until="networkidle")
    results = axe.run(page)
    assert results.violations_count == 0, results.generate_report()
