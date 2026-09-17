#!/usr/bin/env python3
"""Generate the HTML policy pages from the markdown files under policies/.

For every subfolder of policies/ (e.g. security/) this script writes:

- policies/<subfolder>/<policy-name>.html  - one styled HTML page per policy document
- policies/<subfolder>/index.html         - the child page listing that category's policies

It also writes policies/index.html, the parent "Policies" page linking to each
child page.

Run with the project virtual environment:

    ../venvs/igzibo-github-io/Scripts/python scripts/build_policies.py
"""
import html
import re
from pathlib import Path

import markdown

REPO_ROOT = Path(__file__).resolve().parent.parent
POLICIES_DIR = REPO_ROOT / "policies"

# Subfolder -> child page display name (order preserved for the Policies page).
CATEGORIES = [
    ("client-services", "Client Services"),
    ("corporate", "Corporate"),
    ("governance", "Governance"),
    ("privacy", "Privacy"),
    ("recruiting", "Recruiting"),
    ("security", "Security"),
    ("website", "Website"),
]

HEADER = """  <!-- Header & Navigation -->
  <header>
    <div class="container">
      <nav class="nav">
        <a href="/" class="logo-text">IGZIBO</a>
        <ul class="nav-links">
          <li><a href="/">Home</a></li>
          <li><a href="/about/">About</a></li>
          <li><a href="/services/">Services</a></li>
          <li><a href="/team/">Team</a></li>
          <li class="nav-dropdown">
            <a href="/policies/">Policies</a>
            <ul class="nav-dropdown-menu">
              <li><a href="/policies/client-services/">Client Services</a></li>
              <li><a href="/policies/corporate/">Corporate</a></li>
              <li><a href="/policies/governance/">Governance</a></li>
              <li><a href="/policies/privacy/">Privacy</a></li>
              <li><a href="/policies/recruiting/">Recruiting</a></li>
              <li><a href="/policies/security/">Security</a></li>
              <li><a href="/policies/website/">Website</a></li>
            </ul>
          </li>
          <li><a href="https://calendly.com/igzibo-support" class="btn">Schedule Meeting</a></li>
        </ul>
      </nav>
    </div>
  </header>"""

CTA = """  <!-- CTA Section -->
  <section class="cta">
    <div class="container">
      <h2>Ready to Partner With Igzibo?</h2>
      <p>Let's discuss how our team can help you achieve your engineering and technology goals.</p>

      <div class="cta-links">
        <a href="/services/" class="btn btn-large">Explore Services</a>
        <a href="https://calendly.com/igzibo-support" class="btn-outline btn-large">Schedule a Call</a>
      </div>

      <p class="cta-contact">
        <strong>Phone:</strong> <a href="tel:+19712361374">971-236-1374</a> |
        <strong>Email:</strong> <a href="mailto:support@igzibo.com">support@igzibo.com</a>
      </p>
    </div>
  </section>"""

FOOTER = """  <!-- Footer -->
  <footer>
    <div class="container">
      <p><strong>IGZIBO | Engineering Solutions. Building What's Next.</strong></p>
      <p>Phone: <a href="tel:+19712361374">971-236-1374</a></p>
      <p>Calendly: <a href="https://calendly.com/igzibo-support">Schedule a Meeting</a></p>
      <p class="footer-copyright">&copy; 2024 Igzibo Engineering Solutions, Inc. All rights reserved.</p>
    </div>
  </footer>"""


def render_page(title, description, main_html):
    """Wrap page content in the shared site shell (head, header, footer)."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">
  <meta name="author" content="Igzibo Engineering Solutions">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:type" content="website">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body>
{HEADER}

  <main>

{main_html}

  </main>

{FOOTER}

  <script src="/assets/js/main.js"></script>
</body>
</html>
"""


def parse_policy(md_path):
    """Return (title, body_markdown) for a policy markdown file.

    The title is the document's first-level heading; it is removed from the
    body because the page template renders it as the page heading.
    """
    text = md_path.read_text(encoding="utf-8")
    match = re.search(r"^# (.+)$", text, flags=re.MULTILINE)
    if not match:
        raise ValueError(f"No level-1 heading found in {md_path}")
    title = match.group(1).strip()
    body = (text[: match.start()] + text[match.end() :]).lstrip("\n")
    return title, body


def render_document_page(category_slug, category_name, title, content_html):
    main = f"""  <section>
    <div class="container">
      <p><a href="/policies/{category_slug}/" class="policy-back-link">&larr; Back to {html.escape(category_name)} Policies</a></p>

      <article class="policy-document">
        <h1>{html.escape(title)}</h1>
        {content_html}
      </article>
    </div>
  </section>

{CTA}"""
    return render_page(
        f"{title} | Igzibo Policies",
        f"{title} - {category_name} policy document from Igzibo Engineering Solutions.",
        main,
    )


def render_category_page(category_slug, category_name, documents):
    cards = "\n        ".join(
        f'<div class="card">\n          <h3><a href="/policies/{category_slug}/{doc_slug}.html">{html.escape(doc_title)}</a></h3>\n        </div>'
        for doc_title, doc_slug in documents
    )
    main = f"""  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <div class="hero-grid">
        <div>
          <h1>{html.escape(category_name)} <span class="hero-tech">Policies</span></h1>
          <p>Igzibo Engineering Solutions {html.escape(category_name.lower())} policies, standards, and procedures.</p>

          <div class="hero-cta">
            <a href="/policies/" class="btn-outline btn-large">All Policies</a>
          </div>
        </div>
        <div>
          <div class="video-placeholder">
            <div>
              <h2>{html.escape(category_name)}</h2>
              <p>{len(documents)} policy document{"s" if len(documents) != 1 else ""}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Policy Documents -->
  <section>
    <div class="container">
      <div class="section-title">
        <h2>{html.escape(category_name)} Policies</h2>
        <p>Select a policy to view the full document.</p>
      </div>

      <div class="grid cards">
        {cards}
      </div>
    </div>
  </section>

{CTA}"""
    return render_page(
        f"{category_name} Policies | Igzibo",
        f"Igzibo Engineering Solutions {category_name.lower()} policies, standards, and procedures.",
        main,
    )


def render_policies_index(category_counts):
    cards = "\n        ".join(
        f'<div class="card">\n          <h3><a href="/policies/{slug}/">{html.escape(name)}</a></h3>\n          <p>{count} policy document{"s" if count != 1 else ""}</p>\n        </div>'
        for slug, name, count in category_counts
    )
    main = f"""  <!-- Hero Section -->
  <section class="hero">
    <div class="container">
      <div class="hero-grid">
        <div>
          <h1>Our <span class="hero-tech">Policies</span></h1>
          <p>The policies, standards, and procedures that govern how Igzibo Engineering Solutions works.</p>

          <div class="hero-cta">
            <a href="https://calendly.com/igzibo-support" class="btn-outline btn-large">Contact Us</a>
          </div>
        </div>
        <div>
          <div class="video-placeholder">
            <div>
              <h2>Governance</h2>
              <p>Clear standards for security, privacy, ethics, and delivery.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Policy Categories -->
  <section>
    <div class="container">
      <div class="section-title">
        <h2>Policy Categories</h2>
        <p>Select a category to browse its policy documents.</p>
      </div>

      <div class="grid cards">
        {cards}
      </div>
    </div>
  </section>

{CTA}"""
    return render_page(
        "Policies | Igzibo Engineering Solutions",
        "The policies, standards, and procedures that govern how Igzibo Engineering Solutions works.",
        main,
    )


def main():
    converter = markdown.Markdown(extensions=["tables", "sane_lists"])
    category_counts = []

    for category_slug, category_name in CATEGORIES:
        category_dir = POLICIES_DIR / category_slug
        documents = []

        for md_path in sorted(category_dir.glob("*.md")):
            title, body = parse_policy(md_path)
            converter.reset()
            content_html = converter.convert(body)
            doc_slug = md_path.stem
            out_path = category_dir / f"{doc_slug}.html"
            out_path.write_text(
                render_document_page(category_slug, category_name, title, content_html),
                encoding="utf-8",
            )
            documents.append((title, doc_slug))
            print(f"  wrote {out_path.relative_to(REPO_ROOT)}")

        index_path = category_dir / "index.html"
        index_path.write_text(
            render_category_page(category_slug, category_name, documents),
            encoding="utf-8",
        )
        print(f"  wrote {index_path.relative_to(REPO_ROOT)}")
        category_counts.append((category_slug, category_name, len(documents)))

    policies_index = POLICIES_DIR / "index.html"
    policies_index.write_text(render_policies_index(category_counts), encoding="utf-8")
    print(f"  wrote {policies_index.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
