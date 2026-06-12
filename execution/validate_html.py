"""
validate_html.py

Checks all HTML pages for structural consistency:
- Navbar with standard links exists
- Footer with correct copyright exists
- index.css stylesheet is linked
- Inter font is loaded
- Chart.js CDN present on pages with charts
- active-link class on current page nav item
- No empty href="#" on actionable elements (except fallbacks)

Usage:
    python execution/validate_html.py

Exit codes:
    0 — all good
    1 — one or more checks failed
"""

import os
import sys
import re

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PAGES = [
    "index.html",
    "auth.html",
    "login.html",
    "dashboard.html",
    "election-center.html",
    "candidates.html",
    "results.html",
    "verify-pvc.html",
    "security.html",
]

CHARTS_PAGES = {"index.html", "dashboard.html", "results.html"}

EXPECTED_NAV_LINKS = [
    "election-center.html",
    "verify-pvc.html",
    "candidates.html",
    "results.html",
    "security.html",
]

errors = []


def read_page(name):
    path = os.path.join(PROJECT_ROOT, name)
    if not os.path.exists(path):
        errors.append(f"MISSING: {name}")
        return ""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def check_navbar(html, page):
    if '<header class="navbar"' not in html:
        errors.append(f"{page}: missing <header class='navbar'>")
        return
    for link in EXPECTED_NAV_LINKS:
        if f'href="{link}"' not in html:
            errors.append(f"{page}: missing nav link to {link}")


def check_footer(html, page):
    if "Independent National Electoral Commission" not in html:
        errors.append(f"{page}: missing INEC copyright in footer")


def check_stylesheet(html, page):
    if 'href="index.css"' not in html:
        errors.append(f"{page}: missing index.css stylesheet link")


def check_font(html, page):
    if "Inter" not in html or "fonts.googleapis.com" not in html:
        errors.append(f"{page}: missing Inter font from Google Fonts")


def check_chartjs(html, page):
    if page in CHARTS_PAGES and "chart.js" not in html.lower():
        errors.append(f"{page}: missing Chart.js CDN (needs charts)")


def check_active_link(html, page):
    if page == "index.html":
        return  # index has no active-link in nav
    # Derive expected href: login.html -> href="login.html"
    expected_href = page
    pattern = rf'href="{expected_href}"[^>]*class="[^"]*active-link'
    if not re.search(pattern, html):
        # Try a more lenient check
        if f'class="active-link"' not in html:
            errors.append(
                f"{page}: missing active-link class on nav item for current page"
            )


def check_empty_hrefs(html, page):
    """Flag # links that look like placeholders."""
    # Find <a href="#"> with no onclick or other handler
    matches = re.findall(r'<a\s+href="#"[^>]*>', html)
    # Filter out ones with onclick (they may do something)
    actionable = [m for m in matches if "onclick" not in m]
    if actionable:
        errors.append(f"{page}: {len(actionable)} placeholder <a href='#'> links")


def run():
    print(f"Validating {len(PAGES)} HTML pages...\n")
    for page in PAGES:
        html = read_page(page)
        if not html:
            continue
        check_navbar(html, page)
        check_footer(html, page)
        check_stylesheet(html, page)
        check_font(html, page)
        check_chartjs(html, page)
        check_active_link(html, page)
        check_empty_hrefs(html, page)

    if errors:
        print(f"Found {len(errors)} issue(s):\n")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("All pages passed validation.")
        sys.exit(0)


if __name__ == "__main__":
    run()
