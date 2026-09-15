"""Validate every HTML file against the W3C Nu Html Checker via html5validator.

Requires a Java runtime on PATH (html5validator bundles the checker as a .jar).
Skips automatically if Java isn't available rather than failing the whole suite.
"""
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

# html5validator has no __main__.py, so it must be invoked via its console
# script rather than `python -m html5validator`. Look next to the interpreter
# first (venv Scripts/bin dir), falling back to PATH.
HTML5VALIDATOR = shutil.which("html5validator", path=str(Path(sys.executable).parent)) or shutil.which(
    "html5validator"
)


@pytest.mark.skipif(shutil.which("java") is None, reason="html5validator requires Java on PATH")
@pytest.mark.skipif(HTML5VALIDATOR is None, reason="html5validator console script not found")
def test_html5validator():
    result = subprocess.run(
        [
            HTML5VALIDATOR,
            "--root",
            str(REPO_ROOT),
            "--ignore-re",
            r".*(node_modules|\.git).*",
        ],
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
    )
    assert result.returncode == 0, result.stdout + result.stderr
