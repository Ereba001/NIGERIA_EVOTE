# Frontend Style Guide & Conventions

## Goal
Maintain visual consistency across all pages.

## Design Tokens

### Colors
- `--primary-green: #008751` — Nigeria green, used for buttons, active states, accents
- `--primary-green-hover: #00683e`
- `--dark-bg: #111827` — footer background
- `--text-main: #1f2937` — body text
- `--text-muted: #6b7280` — secondary text
- `--bg-light: #f9fafb` — page background
- `--bg-white: #ffffff` — card background
- `--border-color: #e5e7eb`

### Chart colors (hardcoded in scripts.js)
- Green: `#008751`
- Dark slate: `#1f2937`
- Gray: `#9ca3af`
- Light gray: `#e5e7eb`

### Typography
- Font: Inter (Google Fonts), loaded via `<link>` in every page
- `h1`: 3.5rem / 800 weight
- `h2`: 2.5rem / 700 weight
- `h3`: 1.25rem / 600 weight
- Body: 1rem / 400 weight
- Small: 0.875rem
- Tiny: 0.75rem / 0.625rem

### Spacing
- Page max-width: 1200px, centered
- Navbar padding: 1.25rem 4rem (desktop)
- Card padding: 1.5rem
- Border radius: 6px (buttons), 12px (cards)
- Grid gap: 1.5rem

### Buttons
- `.btn-primary` — green background, white text
- `.btn-secondary` — white background, border, dark text
- `.btn-outline` — transparent, border only
- `.btn-large` — larger padding/font for CTAs
- `.btn-full` — width: 100%

### Badges
- `.badge-gray` — light gray bg, muted text
- `.badge-green` — green tint bg, green text (LIVE)
- `.badge-blue` — blue tint bg, blue text (SECURE)

## Page layout pattern
Every page follows:
1. `<header class="navbar">` — logo left, nav center, actions right
2. Main content area — varies per page
3. `<footer class="site-footer">` — dark bg, 4-column grid

## Active nav link
Add class `active-link` to the current page's nav `<a>` for a green highlight.

## Responsive breakpoints
- ≤1024px: tablet adjustments
- ≤768px: mobile stack layout
- ≤480px: small mobile spacing

## Scripts
- `scripts.js` — global JS, DOMContentLoaded listener, Chart.js charts
- Chart.js loaded from CDN: `https://cdn.jsdelivr.net/npm/chart.js`
- All form interactions and API calls (future) should go in scripts.js

## Rules
- Never add inline styles for layout — use index.css classes
- Never add duplicate nav/footer HTML — reuse the same structure across pages
- Chart data is currently hardcoded; replace with dynamic data when backend is added
