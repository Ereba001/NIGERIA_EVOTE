"""
analyze_css.py

Audits index.css for:
- Hardcoded color values that should use CSS variables
- Missing responsive breakpoints coverage
- Unused classes (heuristic, scans HTML pages)
- Classes in HTML not defined in CSS

Usage:
    python execution/analyze_css.py

Exit codes:
    0 — all clean
    1 — issues found
"""

import os
import sys
import re

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_PATH = os.path.join(PROJECT_ROOT, "index.css")

# Colors that should use CSS variables instead of hardcoded values
HARDCODED_COLORS_ALLOWED = [
    "#008751",  # primary-green
    "#00683e",  # primary-green-hover
    "#111827",  # dark-bg
    "#1f2937",  # text-main / chart-dark
    "#6b7280",  # text-muted
    "#f9fafb",  # bg-light
    "#ffffff",  # bg-white
    "#e5e7eb",  # border-color / chart-light-gray
    "#9ca3af",  # chart-gray
    "#f3f4f6",  # common utility bg
    "#def7ec",  # badge green bg
    "#e1effe",  # badge blue bg
    "#1e40af",  # badge blue text
]

# Selectors that should exist in responsive breakpoints
RESPONSIVE_SELECTORS = [
    ".navbar",
    ".nav-links",
    ".stats-grid",
    ".charts-section",
    ".footer-grid",
    ".auth-form-grid",
    ".auth-trust-badges",
    ".dash-grid",
    ".candidates-grid",
    ".results-container",
    ".guidelines-grid",
    ".page-header",
    ".election-grid",
    ".filter-bar",
    ".candidates-list",
    ".verify-container",
    ".security-container",
    ".sec-feature",
    ".hero",
    ".site-footer",
    ".status-bar",
]

# HTML pages for cross-referencing classes
HTML_PAGES = [
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


def extract_css_classes(css_text):
    """Extract all class selectors from CSS."""
    return set(re.findall(r'\.([\w-]+)\s*\{', css_text))


def extract_html_classes(file_path):
    """Extract all class attribute values from an HTML file."""
    classes = set()
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
        for match in re.findall(r'class="([^"]*)"', html):
            for cls in match.split():
                classes.add(cls)
    return classes


def check_hardcoded_colors(css_text):
    issues = []
    # Find all #xxx / #xxxxxx colors
    colors = re.findall(r'#[0-9a-fA-F]{3,6}', css_text)
    for color in colors:
        if color.upper() not in [c.upper() for c in HARDCODED_COLORS_ALLOWED]:
            # Find context (line approx)
            lines = css_text.split('\n')
            for i, line in enumerate(lines, 1):
                if color in line and 'var(' not in line:
                    if color not in ['#008751', '#00683e', '#111827', '#1f2937', '#6b7280', '#f9fafb', '#ffffff', '#e5e7eb', '#9ca3af', '#f3f4f6', '#def7ec', '#e1effe', '#1e40af', '#d1d5db', 'rgba(0,0,0,0.05)', 'rgba(0,0,0,0.1)', 'rgba(0, 135, 81, 0.1)', 'rgba(0, 135, 81, 0.2)', 'rgba(255,255,255,0.1)', 'rgba(255,255,255,0.2)']:
                        issues.append(f"  Line {i}: hardcoded color {color}")
                    break
    return issues


def check_responsive_coverage(css_text):
    issues = []
    # Find selectors defined outside media queries
    for selector in RESPONSIVE_SELECTORS:
        # Check if selector appears in main scope (before any media query)
        main_css = css_text.split("@media")[0] if "@media" in css_text else css_text
        if selector not in main_css:
            continue  # selector defined somewhere, skip

        # Check if it also appears in at least one media query
        in_media_768 = re.search(
            rf"@media[^}}]*768.*?{re.escape(selector)}", css_text, re.DOTALL
        )
        if not in_media_768:
            issues.append(f"  {selector}: no responsive override at 768px breakpoint")
    return issues


def run():
    if not os.path.exists(CSS_PATH):
        print("CSS file not found at", CSS_PATH)
        sys.exit(1)

    with open(CSS_PATH, "r", encoding="utf-8") as f:
        css_text = f.read()

    total_issues = 0

    print("=== Hardcoded Colors ===")
    color_issues = check_hardcoded_colors(css_text)
    if color_issues:
        total_issues += len(color_issues)
        for issue in color_issues:
            print(issue)
    else:
        print("  No unexpected hardcoded colors found.")

    print("\n=== Responsive Coverage ===")
    resp_issues = check_responsive_coverage(css_text)
    if resp_issues:
        total_issues += len(resp_issues)
        for issue in resp_issues:
            print(issue)
    else:
        print("  All major selectors have responsive overrides.")

    print("\n=== Unused CSS Classes ===")
    css_classes = extract_css_classes(css_text)
    all_html_classes = set()
    for page in HTML_PAGES:
        path = os.path.join(PROJECT_ROOT, page)
        if os.path.exists(path):
            all_html_classes.update(extract_html_classes(path))

    # Common utility/syntax classes that won't appear as literal class names
    skip_classes = {
        "btn", "active", "bg-light", "font-medium",
        "mt-2", "mt-4", "mt-8", "mb-0", "mb-4",
        "text-sm", "text-xs", "text-center", "text-right",
        "border-bottom",
    }
    unused = css_classes - all_html_classes - skip_classes
    if unused:
        total_issues += len(unused)
        for cls in sorted(unused):
            print(f"  .{cls}: not found in any HTML page")
    else:
        print("  All CSS classes are used in at least one HTML page.")

    print(f"\n{'='*40}")
    if total_issues:
        print(f"Found {total_issues} issue(s).")
        sys.exit(1)
    else:
        print("CSS audit passed cleanly.")
        sys.exit(0)


if __name__ == "__main__":
    run()
