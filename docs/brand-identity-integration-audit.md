# Phase 3 — Brand Identity Integration Audit

**Orivis — Powering Trusted Decisions**

> Read-only analysis of remaining election language, visual branding, CSS architecture,
> and UX across all 10 pages. No code modifications made. This report informs the
> Phase 3 execution plan.

---

## Table of Contents

1. [Remaining Election Language Inventory](#1-remaining-election-language-inventory)
2. [Visual Branding Inventory](#2-visual-branding-inventory)
3. [Proposed Orivis Design System](#3-proposed-orivis-design-system)
4. [Hero Imagery Direction](#4-hero-imagery-direction)
5. [Dashboard UX Repositioning](#5-dashboard-ux-repositioning)
6. [Implementation Priority Order](#6-implementation-priority-order)

---

## 1. Remaining Election Language Inventory

This section catalogs every instance of election-specific, Nigeria-specific, or
democracy-specific language that still appears after Phase 1 and Phase 2 rebranding.

### 1.1 Page Titles

| File | Current Title | Issue |
|---|---|---|
| `election-center.html:6` | `Election Center \| Orivis` | "Election" is election-specific |
| `results.html:6` | `Results \| Orivis` | OK in context, but results are election-specific |

### 1.2 Navigation Labels (shared across all pages)

| Nav Label | Files | Issue |
|---|---|---|
| `Election Center` | `index.html:28`, `election-center.html:117`, `candidates.html:40`, `results.html:36`, `security.html:38`, `verify-pvc.html:28` | Election-specific label |

### 1.3 Election-Specific Terminology

**election-center.html:**
- `H1: "Election Center"` (line 147)
- Subtitle: `"Stay updated on all active, upcoming, and past elections..."` (line 148)
- Card types: `"Organization"`, `"Regional"` — OK as org types
- Card titles: `"Leadership Election 2026"`, `"Regional Election"`, `"Assembly Election"` (lines 158, 232, 262)
- Labels: `"Eligible Voters:"` x3 (lines 173, 247, 277) — "Voters" is election language
- Body text: `"Cast your vote for organizational leadership."` (line 175)
- Body text: `"Election for regional leadership."` (line 249)
- Body text: `"Representative elections across all districts..."` (line 279)
- Button: `"Vote Now"` (line 179)
- Modal title: `"Cast Your Vote"` (line 187)
- Section: `"Electoral Process"` (line 308)
- Text: `"Learn about how the blockchain ledger secures your vote..."` (line 309)
- Modal success: `"Vote Cast Successfully!"` (line 222)
- Modal success: `"Thank you for participating."` (line 223)

**dashboard.html:**
- Status bar: `"Election Status"` (line 78)
- Status bar: `"Total Votes Cast"` (line 90)
- Card title: `"Cast Your Vote: Leadership Election 2026"` (line 104)
- Party labels: `"Progressive Party (PP)"`, `"United Alliance (UA)"`, `"National Front (NF)"` (lines 114, 124, 134)
- "Live Results" pie chart labels: `"Candidate A"`, `"Candidate B"`, `"Others"` (lines 169-179)
- Chart legend colors: `#008751` (Nigeria green) (line 169)
- Detailed results chart: `"Candidate A (PP)"`, `"Candidate B (UA)"`, `"Candidate C (NF)"`, `"Others"` (line 382)
- State table retains Nigeria regions: `Lagos`, `Kano`, `Rivers`, `FCT Abuja`, `Kaduna` (lines 238-243)
- Profile view: `"Voting Center: Center 023, Ikeja"` (line 294)
- Profile view: `"Region: Lagos"` (line 286), `"District: Ikeja"` (line 290)
- Modal: `"Leadership Election"` (line 318)
- Modal: `"Irreversible Action — Once submitted, your vote is digitally signed..."` (lines 321-322)
- Success: `"Vote Cast Successfully!"` (line 584)
- Success: `"Your vote has been securely recorded on the blockchain ledger."` (line 584)

**candidates.html:**
- Header: `"Candidates"` (line 70)
- Subtitle: `"Explore the profiles of registered candidates for upcoming governance events."` (line 71) — OK, generic enough
- Party names: `"Progressive Party (PP)"`, `"United Alliance (UA)"`, `"National Front (NF)"` (lines 92, 105, 118)
- Bios reference: `"public servant"`, `"youth empowerment"`, `"national"` framing

**results.html:**
- H1: `"Live Election Results"` (line 66)
- Subtitle: `"Real-time, cryptographically verified governance results..."` (line 67) — hybrid, "governance results" is OK
- Chart subtitle: `"Leadership Election 2026"` (line 74)
- Chart subtitle: `"Total Votes Counted: 12,842,910 (15% of registered participants)"` (line 75)
- Bar chart: `"Candidate A (PP)"`, `"Candidate B (UA)"`, `"Candidate C (NF)"` (line 141)
- Data colors: `['#008751','#1f2937','#9ca3af','#e5e7eb']` — `#008751` is Nigeria green (line 145)
- State table: `Lagos`, `Kano`, `Rivers`, `FCT Abuja`, `Kaduna` (lines 97-119)
- Column header: `"State"` (line 90), `"Leading"` (line 91), `"Margin"` (line 92)

**receipt.html:**
- H1: `"Vote Successfully Cast"` (line 17)
- Subtitle: `"Your democratic choice has been securely recorded on the blockchain."` (line 18)
- Section: `"Voting Details"` (line 21)
- Label: `"Selected Candidate"` (line 23)
- Label: `"Political Party"` (line 27) — strong election language
- Label: `"Verification ID: ORIVIS-2026-X99-8821-B4"` (line 46) — contains "2026" election year
- Footer: `"This receipt serves as permanent proof of your vote."` (line 52)
- Footer: `"Your identity remains anonymous while your vote is publicly verifiable..."` (line 52)
- Brand: `"Orivis • Secure Governance Protocol v4.2.0"` (line 63) — OK

**auth.html:**
- Trust badge text: `"Your vote is anonymous and cannot be traced back to you."` (line 142) — election-specific
- Trust badge text: `"Every action is logged on the secure national ledger."` (line 149) — "national" implies government

**dashboard.html & election-center.html:**
- JavaScript countdown references: `new Date('2026-10-12T08:00:00')` — election date, also appears in JS (line 473 in dashboard, line 364 in election-center)

### 1.4 Nigeria-Specific Data

| Location | Data | Page |
|---|---|---|
| Profile | Phone `+234 803****890` | `dashboard.html:278` |
| Profile | `Region: Lagos`, `District: Ikeja` | `dashboard.html:286-290` |
| Profile | `Voting Center: Center 023, Ikeja` | `dashboard.html:294` |
| State table | `Lagos`, `Kano`, `Rivers`, `FCT Abuja`, `Kaduna` | `dashboard.html:238-243`, `results.html:97-119` |
| Registered | `93.4M` participants (Nigeria population scale) | `dashboard.html:87` |
| Total votes | `12.8M` | `dashboard.html:90` |

### 1.5 CSS Class Names with Election Themes

| Class Name | Purpose | Impact |
|---|---|---|
| `.election-grid` | Grid layout for event cards | Low (if renamed in CSS only) |
| `.election-card` | Individual event card | Low |
| `.state-table` | Results breakdown table | Low |
| `.candidate-card-large` | Candidate profile cards | Low |
| `.candidate-card` | Dashboard candidate selector | Low |
| `.candidate-photo` | Candidate photo placeholder | Low |
| `.candidate-name` | Candidate name text | Low |
| `.candidate-party` | Party affiliation label | Low |
| `.vote-actions` | Vote action buttons | Low |
| `.vote-modal` | Vote confirmation modal | Low |
| `.vote-warning` | Vote warning box | Low |
| `.voter-status` | Status display | Low |

These are cosmetic — they don't affect content but should be renamed for consistency.

---

## 2. Visual Branding Inventory

### 2.1 Current Color Palette

| Variable | Value | Purpose | Origin |
|---|---|---|---|
| `--primary-green` | `#008751` | Primary action color, links, accents | Nigeria national green |
| `--primary-green-hover` | `#00683e` | Button hover state | Derived |
| `--dark-bg` | `#111827` | Footer, dark sections | Design choice |
| `--text-main` | `#1f2937` | Body text | Gray-800 |
| `--text-muted` | `#6b7280` | Secondary text | Gray-500 |
| `--bg-light` | `#f9fafb` | Page background | Gray-50 |
| `--bg-white` | `#ffffff` | Card backgrounds | White |
| `--border-color` | `#e5e7eb` | Borders, dividers | Gray-200 |
| `--chart-green` | `#008751` | Chart primary color | Same as primary |
| `--chart-dark` | `#1f2937` | Chart secondary | Same as text-main |
| `--chart-gray` | `#9ca3af` | Chart tertiary | Gray-400 |
| `--chart-light-gray` | `#e5e7eb` | Chart quaternary | Gray-200 |

### 2.2 Color Usage Observations

- Green (`#008751`) is used for: primary buttons, links, active states, success indicators, chart colors, badge colors, icon accents, status indicators. The color is pervasive and single-source.
- No secondary brand color exists.
- No accent or highlight color exists.
- No semantic color system (success/error/warning/info) is standardized.
- Chart data colors are hardcoded hex values, not CSS variables.
- Green check-fill in modals uses `var(--primary-green)`.
- The green was chosen for Nigeria's flag — a brand association that no longer applies.

### 2.3 Typography

| Element | Size | Weight | Tracking |
|---|---|---|---|
| H1 | 3.5rem (56px) | 800 | -0.02em |
| H2 | 2.5rem (40px) | 700 | normal |
| H3 | 1.25rem (20px) | 600 | normal |
| Body | 1rem (16px) | 400 | normal |
| Small | 0.875rem (14px) | varies | normal |
| Nav | 0.875rem (14px) | 500 | normal |
| Status | 1.25rem (20px) | 700 | normal |

Font: Inter — modern, clean, well-suited for a governance tech platform.

### 2.4 Spacing (No System)

Values found across the codebase: `0.25rem`, `0.4rem`, `0.5rem`, `0.625rem`, `0.75rem`, `0.875rem`, `1rem`, `1.125rem`, `1.25rem`, `1.5rem`, `1.75rem`, `2rem`, `2.5rem`, `3rem`, `4rem`, `5rem`. No consistent scale — each value is chosen ad-hoc.

### 2.5 Component Visual Properties

| Component | Border Radius | Border | Shadow |
|---|---|---|---|
| Buttons | 6px | 1px | Hover: 0 4px 6px -1px rgba(0,135,81,0.2) |
| Cards (general) | 12px | 1px solid var(--border-color) | 0 1px 3px rgba(0,0,0,0.05) |
| Inputs | 6px | 1px solid var(--border-color) | None |
| PIN boxes | 10px | 2px solid var(--border-color) | None |
| OTP boxes | 6px | 1px solid var(--border-color) | None |
| Auth card | 12px | 1px solid var(--border-color) | 0 4px 6px rgba(0,0,0,0.05) |
| Modals | 16px | None | 0 20px 60px rgba(0,0,0,0.15) |
| Footer | None | Top border 1px | None |

### 2.6 CSS Architecture Assessment

**Strengths:**
- CSS variables present for core colors (limited adoption throughout)
- Responsive design covers 4 breakpoints
- Dark mode variables defined (commented out)
- AOS animation library integrated
- Print styles included

**Weaknesses:**
- 2076 lines in a single file — no modularization
- No spacing/typography design token system
- Color variables exist but other properties (border-radius, shadows, font sizes) are hardcoded
- Election-specific class names scattered throughout (`.election-card`, `.candidate-card`, `.vote-modal`, etc.)
- No CSS custom properties for layout values
- Dark mode commented out — many references to `[data-theme="dark"]` but theme toggle is removed from HTML
- Utility classes (`.mt-2`, `.mb-4`, `.text-sm`) are inconsistent and limited
- Duplicate style definitions between embedded `<style>` blocks and `index.css`
- Hero image background is hardcoded to `resources/homepage.png` — both in CSS (line 360) and inline dashboard styles (line 19)

### 2.7 Icon Usage

- Flaticon Uicons Regular Straight (`fi-rs-*`) is the only icon set
- Used for: stat icons, security features, form inputs, social proofs
- No custom SVG icons or logo mark
- The logo is built from CSS pseudo-elements (a diamond/cross pattern in `.logo-icon`)
- No favicon exists
- No SVG brand mark exists

### 2.8 Image Assets

- `resources/homepage.png` (~2 MB) — serves as both hero background and dashboard background
- No other image assets exist
- No illustrations, no icons, no data visualizations (charts are Chart.js canvas elements)

---

## 3. Proposed Orivis Design System

Based on the brand strategy (`docs/brand-strategy.md`), tagline **"Powering Trusted Decisions"**,
and the positioning as a premium governance technology platform.

### 3.1 Brand Personality

| Attribute | Manifestation |
|---|---|
| **Trustworthy** | Deep, stable colors; clean typography; generous whitespace |
| **Premium** | Refined color palette, subtle gradients, elevated shadows |
| **Modern** | Inter font, rounded corners, glassmorphism elements |
| **Secure** | Lock/s shield icons, status indicators, encryption badges |
| **Global** | Neutral color palette suitable for any organization type |

### 3.2 Recommended Color Palette

#### Primary: Deep Trust Blue

| Token | Value | Usage |
|---|---|---|
| `--color-primary` | `#1e3a5f` | Primary buttons, links, active states |
| `--color-primary-hover` | `#152d4a` | Button hover |
| `--color-primary-light` | `#e8edf4` | Light backgrounds, badge fills |

Rationale: Blue conveys trust, stability, enterprise-grade security. Replaces
the Nigeria-linked green with a globally appropriate governance color.

#### Secondary: Slate Gray

| Token | Value | Usage |
|---|---|---|
| `--color-secondary` | `#475569` | Secondary text, icons |
| `--color-secondary-light` | `#f1f5f9` | Card backgrounds, hover states |

#### Accent: Teal (for modern, growth-oriented feel)

| Token | Value | Usage |
|---|---|---|
| `--color-accent` | `#0d9488` | Success states, progress indicators |
| `--color-accent-light` | `#ccfbf1` | Success backgrounds |

#### Neutral Scale

| Token | Value | Usage |
|---|---|---|
| `--color-bg` | `#f8fafc` | Page background |
| `--color-surface` | `#ffffff` | Card, modal backgrounds |
| `--color-text` | `#0f172a` | Primary text |
| `--color-text-muted` | `#64748b` | Secondary text |
| `--color-border` | `#e2e8f0` | Borders, dividers |
| `--color-dark` | `#0f172a` | Footer, dark sections |

#### Semantic Colors

| Token | Value | Usage |
|---|---|---|
| `--color-success` | `#10b981` | Success badges, checkmarks |
| `--color-warning` | `#f59e0b` | Warnings, caution states |
| `--color-error` | `#ef4444` | Errors, validation |
| `--color-info` | `#3b82f6` | Info badges, tooltips |

#### Chart Data Colors

| Token | Value |
|---|---|
| `--chart-1` | `#1e3a5f` (Primary blue) |
| `--chart-2` | `#0d9488` (Teal accent) |
| `--chart-3` | `#94a3b8` (Slate) |
| `--chart-4` | `#cbd5e1` (Light slate) |
| `--chart-5` | `#f59e0b` (Amber) |

### 3.3 Typography Scale

| Token | Size | Weight | Line Height | Usage |
|---|---|---|---|---|
| `--text-xs` | `0.75rem` (12px) | varies | 1.5 | Badges, metadata |
| `--text-sm` | `0.875rem` (14px) | varies | 1.5 | Body, descriptions |
| `--text-base` | `1rem` (16px) | 400 | 1.5 | Default body |
| `--text-lg` | `1.125rem` (18px) | 400 | 1.5 | Larger body |
| `--text-xl` | `1.25rem` (20px) | 600 | 1.4 | H3, card titles |
| `--text-2xl` | `1.5rem` (24px) | 600 | 1.3 | Section headers |
| `--text-3xl` | `2rem` (32px) | 700 | 1.2 | H2 (mobile) |
| `--text-4xl` | `2.5rem` (40px) | 700 | 1.1 | H2 (desktop) |
| `--text-5xl` | `3rem` (48px) | 800 | 1 | H1 (mobile) |
| `--text-6xl` | `3.5rem` (56px) | 800 | 1 | H1 (desktop) |

Font Family: `'Inter', system-ui, -apple-system, sans-serif` (keep current)

### 3.4 Spacing Scale

| Token | Value |
|---|---|
| `--space-1` | `0.25rem` |
| `--space-2` | `0.5rem` |
| `--space-3` | `0.75rem` |
| `--space-4` | `1rem` |
| `--space-5` | `1.25rem` |
| `--space-6` | `1.5rem` |
| `--space-8` | `2rem` |
| `--space-10` | `2.5rem` |
| `--space-12` | `3rem` |
| `--space-16` | `4rem` |
| `--space-20` | `5rem` |

### 3.5 Border Radius

| Token | Value | Usage |
|---|---|---|
| `--radius-sm` | `4px` | Badges, small elements |
| `--radius-md` | `6px` | Buttons, inputs |
| `--radius-lg` | `8px` | Cards (compact) |
| `--radius-xl` | `12px` | Standard cards |
| `--radius-2xl` | `16px` | Modals, panels |
| `--radius-full` | `9999px` | Pills, badges |

### 3.6 Shadows

| Token | Value | Usage |
|---|---|---|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Subtle elements |
| `--shadow-md` | `0 1px 3px rgba(0,0,0,0.08)` | Standard cards |
| `--shadow-lg` | `0 4px 6px -1px rgba(0,0,0,0.1)` | Elevated cards |
| `--shadow-xl` | `0 10px 15px -3px rgba(0,0,0,0.1)` | Hover states |
| `--shadow-2xl` | `0 20px 60px rgba(0,0,0,0.15)` | Modals |

### 3.7 Component Styles

**Buttons (refined):**

| Property | `.btn-primary` | `.btn-secondary` | `.btn-outline` |
|---|---|---|---|
| Background | `var(--color-primary)` | `var(--color-surface)` | transparent |
| Text | white | `var(--color-text)` | `var(--color-text)` |
| Border | transparent | `var(--color-border)` | `var(--color-border)` |
| Hover bg | `var(--color-primary-hover)` | `var(--color-secondary-light)` | `var(--color-secondary-light)` |
| Hover shadow | `0 4px 6px -1px rgba(30,58,95,0.2)` | none | none |

**Cards:**

- Background: `var(--color-surface)`
- Border: `1px solid var(--color-border)`
- Border-radius: `var(--radius-xl)`
- Shadow: `var(--shadow-md)`
- Hover: translateY(-2px), shadow `var(--shadow-lg)`

**Inputs:**

- Background: `var(--color-surface)`
- Border: `1px solid var(--color-border)`
- Border-radius: `var(--radius-md)`
- Focus: `border-color var(--color-primary)`
- Padding: `var(--space-3) var(--space-4)`

**Navbar:**

- Keep glassmorphism (backdrop-filter blur)
- Background: `rgba(255,255,255,0.8)` 
- Border-bottom: `1px solid rgba(226,232,240,0.5)`
- Sticky top, z-index 100

**Modals:**

- Backdrop: `rgba(15,23,42,0.5)` (matches new dark color)
- Panel: white, rounded `var(--radius-2xl)`, shadow `var(--shadow-2xl)`
- Animation: scale-in

### 3.8 Logo / Favicon

**Priority: Create a favicon** (currently none exists)
- Simple geometric mark (SVG) based on the CSS diamond pattern
- 16×16, 32×32, 48×48 PNG and SVG formats
- Place in project root as `favicon.ico`

**Logo mark refinement:**
- Current CSS diamond/cross pattern in `.logo-icon` can be preserved
- Add SVG version as a proper image asset
- Color: `--color-primary` (#1e3a5f) for the logo mark

---

## 4. Hero Imagery Direction

### 4.1 Current State

- Hero background: `resources/homepage.png` (~2 MB, Nigeria-themed)
- Overlay: CSS gradient `rgba(249,250,251,0.95)` → `rgba(249,250,251,0.5)`
- Same image used for dashboard background

### 4.2 Recommended Direction

**Replace `resources/homepage.png` with an abstract, premium governance-themed image:**

| Criteria | Description |
|---|---|
| **Tone** | Clean, modern, abstract, professional |
| **Theme** | Digital governance, connected networks, secure infrastructure |
| **Colors** | Blue/navy/slate palette matching the new design system |
| **Type** | Abstract gradient or geometric pattern (not literal photography) |
| **Style** | Subtle, non-distracting, professional SaaS platform aesthetic |

**Options to explore:**
1. Abstract blue gradient with subtle grid/network overlay pattern
2. Dark navy with geometric wireframe shapes (dashboard/enterprise look)
3. Light slate with interconnected node/circle patterns
4. Professional gradient mesh in navy-teal spectrum

**Technical requirements:**
- Max 500 KB (compressed WebP preferred, PNG fallback)
- 1920×1080 minimum resolution
- Light enough that the gradient overlay remains readable

### 4.3 Alternative if no budget for custom imagery

Use a CSS-generated background pattern (e.g., subtle grid + gradient) to eliminate
the need for an image file entirely. This would reduce page load by ~2 MB and
improve performance. Example approach:

```css
.hero-with-image {
    background:
        radial-gradient(ellipse at 20% 50%, rgba(30,58,95,0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 50%, rgba(13,148,136,0.06) 0%, transparent 50%),
        linear-gradient(135deg, var(--color-bg) 0%, #eef2f7 100%);
}
```

---

## 5. Dashboard UX Repositioning

### 5.1 Current Problems

1. **Vote-centric language** — The dashboard frames everything around voting: "Cast Your Vote", "Election Status", "Total Votes Cast", "Vote Cast Successfully"
2. **Nigeria-specific data** — 93.4M registered participants, Nigeria state names, +234 phone format
3. **Political party framing** — "Progressive Party (PP)", "United Alliance (UA)" — positions the platform as exclusively for political elections
4. **Leadership Election 2026** — Hardcoded event name and date

### 5.2 Recommended UX Language Changes

| Current | Recommended | Location |
|---|---|---|
| `Election Status` | `Governance Status` | status-bar |
| `Total Votes Cast` | `Total Submissions` | status-bar |
| `Cast Your Vote: Leadership Election 2026` | `Active Governance Event 2026` | dash-card header |
| `Progressive Party (PP)` | `Proposal A (Team Alpha)` | candidate cards |
| `United Alliance (UA)` | `Proposal B (Team Beta)` | candidate cards |
| `National Front (NF)` | `Proposal C (Team Gamma)` | candidate cards |
| `Candidate A` ... `Candidate C` | `Proposal A` ... `Proposal C` | all locations |
| `Party` / `Political Party` | `Affiliation` / `Group` | all locations |
| `Vote` (as verb in UI) | `Submit` / `Cast Decision` | buttons |
| `Vote Cast Successfully!` | `Decision Submitted Successfully!` | success modals |
| `Your vote has been securely recorded...` | `Your submission has been securely recorded...` | modals |
| `Voting Center: Center 023, Ikeja` | `Verification Center: Center 023, Ikeja` | profile |
| `Leadership Election` | `Governance Vote` / `Decision Round` | dashboard modal |
| `Election` as event type | `Governance Event` | event cards |

### 5.3 Professional Profile Data Changes

| Current | Recommended |
|---|---|
| `Region: Lagos` | `Region: Lagos Region` (keep as example data) |
| `+234 803****890` | `+1 555****890` (neutral country code) |
| `93.4M Registered Participants` | `12.5K Registered Participants` (scale to org level) |
| `12.8M Total Votes Cast` | `8.4K Total Submissions` |

### 5.4 Results Page Changes

| Current | Recommended |
|---|---|
| `Live Election Results` | `Live Governance Results` |
| `Leadership Election 2026` | `Decision 2026` (more generic) |
| `Total Votes Counted: 12,842,910` | `Total Submissions: 12,842` |
| `(15% of registered participants)` | `(15% of registered participants)` |
| `State` column header | `Region` / `District` |
| Nigeria-specific rows | Generic region names |
| `Candidate A (PP)` in chart | `Proposal A (Team Alpha)` |

### 5.5 Dashboard Data Scale

Since this is a demo/static frontend, the data should reflect **organizational-scale**
numbers, not national-scale:

| Metric | Current (National) | Recommended (Org) |
|---|---|---|
| Registered Participants | 93.4M | 12.5K |
| Total Votes Cast | 12.8M | 8.4K |
| Total Votes Counted | 12,842,910 | 12,842 |
| Chart data (bars) | 5,393,000 / 4,880,000 / 2,054,000 / 515,910 | 5,393 / 4,880 / 2,054 / 515 |

### 5.6 Chart Color Updates

All chart colors currently reference `#008751` (Nigeria green). Replace with
new chart palette:

```javascript
// Current
backgroundColor: ['#008751', '#1f2937', '#9ca3af', '#e5e7eb']

// Recommended
backgroundColor: ['#1e3a5f', '#0d9488', '#94a3b8', '#cbd5e1']
```

---

## 6. Implementation Priority Order

### Phase 3A — Critical (Design System Foundation)

| # | Task | Files | Effort |
|---|---|---|---|
| 1 | Replace CSS variables with new color palette | `index.css` (lines 3-29) | Small |
| 2 | Update chart colors everywhere | `index.html`, `dashboard.html`, `results.html`, `scripts.js` | Medium |
| 3 | Replace hero background image (or remove and use CSS gradient) | `index.css` (line 360), `dashboard.html` (line 19) | Small |
| 4 | Update button hover shadow to match new primary | `index.css` (line 164) | Small |
| 5 | Add spacing/typography/border-radius CSS variables | `index.css` (add to `:root`) | Medium |
| 6 | Add favicon | New file + all HTML `<head>` sections | Small |

### Phase 3B — Important (Content Updates)

| # | Task | Files | Effort |
|---|---|---|---|
| 7 | Rename "Election Center" → "Governance Center" in all nav links | `index.html`, `election-center.html`, `candidates.html`, `results.html`, `security.html`, `verify-pvc.html` | Small |
| 8 | Rename page H1 and title for election-center.html | `election-center.html` | Small |
| 9 | Update all party labels → proposal/team labels | `dashboard.html`, `candidates.html`, `election-center.html`, `results.html` | Medium |
| 10 | Change "Political Party" → "Affiliation" | `receipt.html` | Small |
| 11 | Replace "Vote" language with "Submit"/"Decision" language | `dashboard.html`, `election-center.html`, `receipt.html` | Medium |
| 12 | Scale data from national to organizational | `dashboard.html`, `results.html` | Medium |
| 13 | Replace Nigeria phone + state data with neutral examples | `dashboard.html` | Small |
| 14 | Update receipt page: "Vote Successfully Cast" → "Decision Submitted" | `receipt.html` | Small |

### Phase 3C — Nice to Have (Code Quality)

| # | Task | Files | Effort |
|---|---|---|---|
| 15 | Rename election-specific CSS classes (`.election-card` → `.event-card`, etc.) | `index.css` + all HTML | Large |
| 16 | Extract inline `<style>` blocks from HTML into `index.css` | All HTML pages | Large |
| 17 | Re-enable and finalize dark mode theme | `index.css` | Medium |
| 18 | Create proper SVG logo asset | New file `resources/logo.svg` | Small |
| 19 | Replace Flaticon icons with custom SVG icons for key UI elements | Potentially large effort | Large |

### Phase 3 — Recommended Order of Execution

```
Phase 3A items 1-6  →  Phase 3B items 7-14  →  Phase 3C items 15-19
(CSS foundation)       (Content updates)        (Code quality)
```

Items 1-6 unblock everything else because the design system drives the visual
consistency of all subsequent changes. Items 7-14 deliver the most visible
brand impact. Items 15-19 are optional polish that can be deferred.

---

## Appendix: Complete CSS Variable Migration Map

When updating `index.css`, replace the `:root` block with the new design system:

```css
:root {
    /* Primary */
    --color-primary: #1e3a5f;
    --color-primary-hover: #152d4a;
    --color-primary-light: #e8edf4;

    /* Secondary */
    --color-secondary: #475569;
    --color-secondary-light: #f1f5f9;

    /* Accent */
    --color-accent: #0d9488;
    --color-accent-light: #ccfbf1;

    /* Neutral */
    --color-bg: #f8fafc;
    --color-surface: #ffffff;
    --color-text: #0f172a;
    --color-text-muted: #64748b;
    --color-border: #e2e8f0;
    --color-dark: #0f172a;

    /* Semantic */
    --color-success: #10b981;
    --color-warning: #f59e0b;
    --color-error: #ef4444;
    --color-info: #3b82f6;

    /* Chart colors */
    --chart-1: #1e3a5f;
    --chart-2: #0d9488;
    --chart-3: #94a3b8;
    --chart-4: #cbd5e1;
    --chart-5: #f59e0b;

    /* Typography */
    --font-family: 'Inter', system-ui, -apple-system, sans-serif;
    --text-xs: 0.75rem;
    --text-sm: 0.875rem;
    --text-base: 1rem;
    --text-lg: 1.125rem;
    --text-xl: 1.25rem;
    --text-2xl: 1.5rem;
    --text-3xl: 2rem;
    --text-4xl: 2.5rem;
    --text-5xl: 3rem;
    --text-6xl: 3.5rem;

    /* Spacing */
    --space-1: 0.25rem;
    --space-2: 0.5rem;
    --space-3: 0.75rem;
    --space-4: 1rem;
    --space-5: 1.25rem;
    --space-6: 1.5rem;
    --space-8: 2rem;
    --space-10: 2.5rem;
    --space-12: 3rem;
    --space-16: 4rem;
    --space-20: 5rem;

    /* Border Radius */
    --radius-sm: 4px;
    --radius-md: 6px;
    --radius-lg: 8px;
    --radius-xl: 12px;
    --radius-2xl: 16px;
    --radius-full: 9999px;

    /* Shadows */
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 1px 3px rgba(0,0,0,0.08);
    --shadow-lg: 0 4px 6px -1px rgba(0,0,0,0.1);
    --shadow-xl: 0 10px 15px -3px rgba(0,0,0,0.1);
    --shadow-2xl: 0 20px 60px rgba(0,0,0,0.15);

    /* Legacy aliases (for backward compatibility during migration) */
    --primary-green: var(--color-primary);
    --primary-green-hover: var(--color-primary-hover);
    --dark-bg: var(--color-dark);
    --text-main: var(--color-text);
    --text-muted: var(--color-text-muted);
    --bg-light: var(--color-bg);
    --bg-white: var(--color-surface);
    --border-color: var(--color-border);
}
```

Legacy aliases at the bottom allow a phased migration — existing code continues
to work while new code uses the new token names.
