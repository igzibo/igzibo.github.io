"""Screenshot-diff regression tests, guarding against layout regressions such
as an image overflowing its container.

Baselines are created automatically on first run (the test is skipped so you
can review the generated screenshot). Delete a file under tests/baselines/
to intentionally re-approve a visual change.
"""
from pathlib import Path

import pytest
from PIL import Image, ImageChops

from tests.pages import PAGES

BASELINE_DIR = Path(__file__).resolve().parent / "baselines"
DIFF_DIR = Path(__file__).resolve().parent / "__diffs__"
VIEWPORTS = {
    "mobile": {"width": 375, "height": 812},
    "tablet": {"width": 768, "height": 1024},
    "desktop": {"width": 1440, "height": 900},
}
MAX_DIFF_RATIO = 0.005  # fail once more than 0.5% of pixels differ from baseline


def _slug(path: str) -> str:
    return path.strip("/").replace("/", "_") or "home"


@pytest.mark.parametrize("viewport_name", VIEWPORTS)
@pytest.mark.parametrize("path", PAGES)
def test_visual_regression(page, base_url, path, viewport_name):
    viewport = VIEWPORTS[viewport_name]
    page.set_viewport_size(viewport)
    page.goto(f"{base_url}{path}", wait_until="networkidle")

    BASELINE_DIR.mkdir(parents=True, exist_ok=True)
    baseline_path = BASELINE_DIR / f"{_slug(path)}__{viewport_name}.png"
    actual_bytes = page.screenshot(full_page=True)

    if not baseline_path.exists():
        baseline_path.write_bytes(actual_bytes)
        pytest.skip(f"No baseline existed; created {baseline_path.name}. Re-run to compare.")

    DIFF_DIR.mkdir(parents=True, exist_ok=True)
    actual_path = DIFF_DIR / f"actual__{_slug(path)}__{viewport_name}.png"
    actual_path.write_bytes(actual_bytes)

    baseline_img = Image.open(baseline_path).convert("RGB")
    actual_img = Image.open(actual_path).convert("RGB")

    if baseline_img.size != actual_img.size:
        pytest.fail(f"{path} ({viewport_name}): size changed {baseline_img.size} -> {actual_img.size}")

    diff = ImageChops.difference(baseline_img, actual_img)
    diff_pixels = sum(1 for pixel in diff.getdata() if pixel != (0, 0, 0))
    total_pixels = baseline_img.width * baseline_img.height
    ratio = diff_pixels / total_pixels

    if ratio > MAX_DIFF_RATIO:
        diff_path = DIFF_DIR / f"diff__{_slug(path)}__{viewport_name}.png"
        diff.save(diff_path)
        pytest.fail(
            f"{path} ({viewport_name}): {ratio:.2%} of pixels differ from baseline "
            f"(threshold {MAX_DIFF_RATIO:.2%}). Diff saved to {diff_path}"
        )
    else:
        actual_path.unlink(missing_ok=True)
