"""Verify every internal href/src in the site resolves to a real file on disk.

Catches missing images, dead profile links, and typo'd asset paths before they
reach GitHub Pages.
"""
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

REPO_ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git"}
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel"}


def _iter_html_files():
    for path in REPO_ROOT.rglob("*.html"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def _strip_fragment_and_query(ref: str) -> str:
    return ref.split("#")[0].split("?")[0]


def _resolve_absolute_site_path(ref: str) -> Path:
    """Resolve a site-absolute path (e.g. /assets/css/styles.css) to a repo file."""
    if ref.endswith("/"):
        ref += "index.html"
    return REPO_ROOT / ref.lstrip("/")


def test_internal_links_and_assets_resolve():
    broken = []
    for html_file in _iter_html_files():
        soup = BeautifulSoup(html_file.read_text(encoding="utf-8"), "html.parser")
        refs = [tag.get("href") for tag in soup.find_all(["a", "link"])]
        refs += [tag.get("src") for tag in soup.find_all(["img", "script"])]

        for raw_ref in filter(None, refs):
            ref = _strip_fragment_and_query(raw_ref)
            if not ref or ref.startswith("//"):
                continue
            if urlparse(ref).scheme in EXTERNAL_SCHEMES:
                continue

            if ref.startswith("/"):
                target = _resolve_absolute_site_path(ref)
            else:
                target = (html_file.parent / ref).resolve()

            if not target.exists():
                broken.append(f"{html_file.relative_to(REPO_ROOT)} -> {raw_ref}")

    assert not broken, "Broken internal references found:\n" + "\n".join(broken)
