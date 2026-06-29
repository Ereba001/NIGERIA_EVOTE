# Phase 7 — List of Updated Components

## Global Design System

| Component | Location | Changes |
|-----------|----------|---------|
| CSS Custom Properties | `index.css:3-80` | 40+ new design tokens (brand colors, semantics, spacing, radius, shadows, transitions) |
| Legacy Aliases | `index.css:41-42` | `--primary-green` / `--primary-green-hover` aliased to `--primary` / `--primary-hover` |
| Dark Mode Variables | `index.css:31-58` | Full dark palette redefined with blue-tinted colors |

## Core UI Components

| Component | CSS Class(es) | Changes |
|-----------|---------------|---------|
| Primary Button | `.btn-primary` | Background: `#008751` → `#1E3A5F`, Shadow: green → blue tint |
| Secondary Button | `.btn-secondary` | Unchanged (white/gray) |
| Outline Button | `.btn-outline` | Unchanged (border/gray) |
| Send OTP Button | `.btn-send-otp:hover` | Hover background: `#008751` → `#1E3A5F` |
| Badge Green | `.badge-green` | Background: `#def7ec` → `var(--badge-primary-bg)`, Color: `var(--primary-green)` → `var(--primary)` |
| Badge Blue | `.badge-blue` | Background: `#e1effe` → `var(--badge-secondary-bg)`, Color: `#1e40af` → `var(--badge-secondary-text)` |
| Badge Gray | `.badge-gray` | Background: `#f3f4f6` → `var(--badge-gray-bg)` |
| Text Green | `.text-green` | Color resolves via `--primary-green` alias → `#1E3A5F` |
| Checkmark | `.checkmark` | Color resolves via `--primary-green` alias → `#1E3A5F` |
| Nav Hover | `.nav-link:hover` | Background: `rgba(22,163,74,0.05)` → `var(--primary-light)` |

## Navigation

| Component | Files | Changes |
|-----------|-------|---------|
| Desktop nav link underline | `index.css` | `background: var(--primary-green)` → resolves to blue |
| Dashboard nav active | `index.css` | Text/border: green → blue |
| Nav link active (per-page) | HTML style blocks | Replaced `--primary-green` → `--primary` in 8 files |
| Nav user role badge | 4 admin files | Background `#def7ec` → `var(--badge-primary-bg)` |
| Org switcher focus ring | 4 admin files | Shadow: `rgba(0,135,81,0.15)` → `rgba(30,58,95,0.15)` |

## Cards

| Component | Files | Changes |
|-----------|-------|---------|
| Candidate card selected | `index.css` | Border/background: green → blue via alias + `var(--primary-light)` |
| Health card value/icon | `admin.html` | Color: `var(--primary-green)` → `var(--primary)` |
| Stat card | `index.css` | Unchanged (no green refs) |
| Chart card | `index.css` | Unchanged (no green refs) |

## Forms

| Component | Files | Changes |
|-----------|-------|---------|
| Input focus border | `index.css` | `var(--primary-green)` → resolves to blue |
| OTP box focus | `index.css` | `var(--primary-green)` → resolves to blue |
| PIN box caret/focus | `index.css` | `var(--primary-green)` → resolves to blue |
| Auth stepper active | `index.css` | `var(--primary-green)` → resolves to blue |
| Radio accent color | `governance-center.html` | `accent-color:var(--primary-green)` → `var(--primary)` |

## Tables

| Component | Files | Changes |
|-----------|-------|---------|
| State results table | `index.css` | Unchanged (no green refs) |
| Participant table | `admin-participants.html` | `#def7ec` → `var(--badge-primary-bg)` |

## Modals & Overlays

| Component | Files | Changes |
|-----------|-------|---------|
| Auth success icon | `index.css` | `var(--primary-green)` → resolves to blue |
| Auth modal icon | `index.css` | `var(--primary-green)` → resolves to blue |
| Confirm modal icon | `index.css` | `var(--primary-green)` → resolves to blue |
| Vote check badge | `index.css` | `var(--primary-green)` → resolves to blue |
| Vote modal spinner | `index.css` | `border-top-color: var(--primary-green)` → resolves to blue |
| Auth modal check fill | `index.css` | `fill: var(--primary-green)` → resolves to blue |
| Auth success modal icon | `index.css` | `background: var(--primary-green)` → resolves to blue |

## Status Indicators

| Component | Files | Changes |
|-----------|-------|---------|
| Status-optimal text | `index.css` | `var(--primary-green)` → resolves to blue |
| Identity success box | `index.css` | `#f0fdf4` / `#86efac` → success-blue tint |
| OTP feedback verified | `index.css` | `var(--primary-green)` → resolves to blue |
| Receipt success icon | `index.css` | `#def7ec` → `var(--badge-primary-bg)`, Color → `var(--primary)` |
| Receipt copy button | `index.css` | `var(--primary-green)` → resolves to blue |

## Admin-specific

| Component | Files | Changes |
|-----------|-------|---------|
| Activity feed dot | `admin.html` | `var(--primary-green)` → `var(--primary)` |
| Audit icon green | `admin-audit.html` | `var(--primary-green)` → `var(--primary)` |
| Lifecycle active dot | `admin-events.html` | `#22c55e` → `var(--success)` |
| Badge active | `admin-events.html` | `#def7ec` / `#008751` → `var(--badge-primary-bg)` / `var(--primary)` |
| Badge dot green | `admin-events.html` | `#008751` → `var(--primary)` |
| Status verified | `admin-participants.html` | `#def7ec` / `var(--primary-green)` → `var(--badge-primary-bg)` / `var(--primary)` |
| Action link resend | `admin-participants.html` | `var(--primary-green)` → `var(--primary)` |
| Danger zone button | `settings.html` | `var(--primary-green)` → `var(--primary)` |
| Form select accent | `settings.html` | `var(--primary-green)` → `var(--primary)` |
| Color option selected | `settings.html` | `var(--primary-green)` → `var(--primary)` |
| Nav-link-active | `settings.html` | `rgba(22,163,74,0.05)` → `var(--primary-light)` |

## Charts & Data Viz

| Component | File | Changes |
|-----------|------|---------|
| Enrollment line chart | `scripts.js` | `#008751` → `#1E3A5F` (border, points, fill) |
| Distribution pie chart | `scripts.js` | `#008751` → `#1E3A5F` (segment) |
| Live Results pie chart | `scripts.js` | `#008751` → `#1E3A5F`, `#2563eb` → `#3B82F6` |
| Dashboard outcomes chart | `dashboard.html` | `#008751` → `#1E3A5F` |
| Outcomes page chart | `outcomes.html` | `#008751` → `#1E3A5F` |

## Footer

| Component | Files | Changes |
|-----------|-------|---------|
| Footer | `index.css` | Unchanged (uses `--dark-bg`, no green refs) |

## Not Modified

- HTML structure (no tags added/removed/reordered)
- HTML class names (`.election-card`, `.candidate-card`, `.vote-modal`, `.badge-green`, `.text-green`, etc.)
- JavaScript logic (all Chart.js configs, localStorage, event handlers, DOM manipulation)
- CSS architecture (no selectors added/removed, no specificity changes)
