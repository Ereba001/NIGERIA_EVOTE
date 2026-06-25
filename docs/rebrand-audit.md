# Rebrand Audit Report

> Generated: 2026-06-25
> Project: E-Voting Frontend (Nigeria-specific)

---

## 1. Project Structure

```
PROJET/
├── .env                          # Empty environment variables file
├── .gitignore                    # Ignores .env, .tmp/, credentials.json, token.json
├── AGENT.md                      # Agent instructions (mirrored across CLAUDE.md, GEMINI.md, OPENCODE.md, AGENTS.md)
├── AGENTS.md                     # Master agent instructions (3-layer architecture: directives, orchestration, execution)
├── CLAUDE.md                     # Same as AGENTS.md (for Claude compatibility)
├── GEMINI.md                     # Same as AGENTS.md (for Gemini compatibility)
├── OPENCODE.md                   # Same as AGENTS.md (for OpenCode compatibility)
├── index.html                    # Home/Landing page (public)
├── dashboard.html                # Authenticated user dashboard (voting UI)
├── login.html                    # Login page (NIN + PIN authentication)
├── auth.html                     # Registration/sign-up page (multi-step: identity → OTP → PIN)
├── candidates.html               # Candidates listing page
├── election-center.html          # Election center (active/upcoming elections listings)
├── receipt.html                  # Post-vote receipt page (blockchain verification ID)
├── results.html                  # Live election results page
├── security.html                 # Security/trust information page
├── verify-pvc.html               # PVC (Permanent Voter's Card) verification page
├── index.css                     # Global stylesheet (57,920 bytes — all styles in one file)
├── scripts.js                    # Global JavaScript (Chart.js init, AOS init, counters, nav behavior, copy, receipt)
├── server.js                     # Simple Node.js HTTP static file server (port 3000)
├── vercel.json                   # Vercel deployment config (version 2, public, clean URLs)
│
├── directives/                   # SOPs in Markdown
│   ├── development_workflow.md   # SOP for development workflow
│   ├── frontend_style.md         # SOP for frontend style conventions
│   └── serve_frontend.md         # SOP for serving the frontend locally
│
├── execution/                    # Deterministic Python scripts
│   ├── analyze_css.py            # CSS analysis script
│   └── validate_html.py          # HTML validation script
│
├── resources/                    # Design assets
│   ├── homepage.png              # Homepage hero background image (~2 MB)
│   ├── wireframe1_merged (1).pdf # Wireframe PDF
│   ├── wireframe1_page-0003.jpg  # Wireframe image
│   ├── wireframe_page-0001.jpg   # Wireframe image
│   ├── wireframe_page-0002.jpg   # Wireframe image
│   ├── wireframe_page-0004.jpg   # Wireframe image
│   ├── wireframe_page-0005.jpg   # Wireframe image
│   └── wireframe_page-0006.jpg   # Wireframe image
│
├── .tmp/                         # Intermediate/temp files (gitignored)
│   └── mobile-responsiveness-audit.md  # Prior audit report
│
└── docs/                         # Documentation (newly created)
    └── rebrand-audit.md          # This file
```

---

## 2. Pages

### 2.1 Landing Page — `index.html`
| Property | Value |
|---|---|
| **Route** | `/` or `/index.html` |
| **Title** | `Nigeria E-Vote | Home` |
| **Purpose** | Public-facing landing page for the digital voting platform |
| **Main Sections** | Hero section, Trusted badge, Statistics grid (4 stat cards), Charts section (enrollment trends, regional distribution pie, security status), Footer |
| **Components Used** | `navbar`, `hero`, `trusted-badge`, `stats-grid` (4x `stat-card`), `charts-section` (`chart-card`, `trends-card`, `distribution-card`, `security-card`), `site-footer` |

### 2.2 Login Page — `login.html`
| Property | Value |
|---|---|
| **Route** | `/login.html` |
| **Title** | `Government Portal Login | Nigeria E-Vote` |
| **Purpose** | Voter authentication via NIN + 4-digit PIN |
| **Main Sections** | Header (navbar-auth), Portal card (NIN input, PIN input, verify button), Identity verification chart, Footer |
| **Components Used** | `navbar-auth`, `portal-card`, `portal-login-main`, `pin-inputs`, `portal-chart`, `auth-footer`, `auth-modal` (welcome modal) |

### 2.3 Registration Page — `auth.html`
| Property | Value |
|---|---|
| **Route** | `/auth.html` |
| **Title** | `Secure Voter Authentication | Nigeria E-Vote` |
| **Purpose** | Multi-step voter registration: (1) VIN/NIN + Phone → (2) OTP → (3) Security PIN |
| **Main Sections** | Header, Auth header, Stepper (3 steps), Auth form grid, Trust badges, Footer |
| **Components Used** | `navbar-auth`, `auth-stepper`, `auth-form-grid`, `auth-step` (x3), `auth-trust-badges` (x3), `auth-footer`, `auth-modal` (success modal) |

### 2.4 Dashboard — `dashboard.html`
| Property | Value |
|---|---|
| **Route** | `/dashboard.html` |
| **Title** | `Dashboard | Nigeria E-Vote` |
| **Purpose** | Authenticated voter dashboard with voting, results, and profile views |
| **Main Sections** | Status bar, Dashboard view (voting grid, transparency card, live results, verification), Results view (bar chart, state breakdown table), Profile view (voter details), Vote modal, Logout modal |
| **Components Used** | `navbar-dash`, `nav-user`, `status-bar`, `dash-card`, `candidates-grid`, `live-pie-container`, `verification-list`, `vote-modal`, `confirm-modal`, `auth-modal`, `dash-footer` |

### 2.5 Candidates Page — `candidates.html`
| Property | Value |
|---|---|
| **Route** | `/candidates.html` |
| **Title** | `Candidates | Nigeria E-Vote` |
| **Purpose** | Browse election candidates with profiles and manifestos |
| **Main Sections** | Page header, Filter bar (dropdown), Candidates grid (3 candidate cards), Footer |
| **Components Used** | `navbar`, `page-header`, `filter-bar`, `candidate-card-large` (x3), `site-footer` |

### 2.6 Election Center — `election-center.html`
| Property | Value |
|---|---|
| **Route** | `/election-center.html` |
| **Title** | `Election Center | Nigeria E-Vote` |
| **Purpose** | View active and upcoming elections with details |
| **Main Sections** | Page header, Election grid (3 election cards: Presidential, Lagos Gubernatorial, National Assembly), Vote modal (in-card), Success modal, Guidelines section (3 guide cards), Footer |
| **Components Used** | `navbar`, `page-header`, `election-card` (x3), `confirm-modal`, `auth-modal`, `guidelines-section`, `guide-card` (x3), `site-footer` |

### 2.7 Vote Receipt — `receipt.html`
| Property | Value |
|---|---|
| **Route** | `/receipt.html` |
| **Title** | `Vote Receipt | Nigeria E-Vote` |
| **Purpose** | Displays blockchain receipt after successful vote |
| **Main Sections** | Receipt card (success icon, vote details, transaction hash, verification ID, notice) |
| **Components Used** | `receipt-card`, `copy-field`, `receipt-brand`, `receipt-notice` |

### 2.8 Live Results — `results.html`
| Property | Value |
|---|---|
| **Route** | `/results.html` |
| **Title** | `Live Results | Nigeria E-Vote` |
| **Purpose** | Display live election results with bar chart and state breakdown |
| **Main Sections** | Page header, Results container (bar chart, state breakdown table), Footer |
| **Components Used** | `navbar`, `page-header`, `chart-box`, `state-results`, `state-table`, `site-footer` |

### 2.9 Security Page — `security.html`
| Property | Value |
|---|---|
| **Route** | `/security.html` |
| **Title** | `Security | Nigeria E-Vote` |
| **Purpose** | Explain platform security features (blockchain, identity gateway, cloud infra) |
| **Main Sections** | Page header, Security features (3 features: blockchain ledger, identity gateway, cloud infra), Certification banner, Footer |
| **Components Used** | `navbar`, `page-header`, `sec-feature` (x3), `cert-banner`, `site-footer` |

### 2.10 Verify PVC — `verify-pvc.html`
| Property | Value |
|---|---|
| **Route** | `/verify-pvc.html` |
| **Title** | `Verify PVC | Nigeria E-Vote` |
| **Purpose** | Check PVC validity by entering VIN/NIN |
| **Main Sections** | Page header, Verification form (VIN/NIN input, result display), Footer |
| **Components Used** | `navbar`, `page-header`, `verify-container`, `identity-result`, `site-footer` |

---

## 3. Branding Audit — Nigeria-Specific Content

### 3.1 `index.html`

| Line | Text |
|---|---|
| 6 | `<title>Nigeria E-Vote | Home</title>` |
| 9 | `content="Official Nigeria E-Vote portal for secure, transparent elections."` |
| 25 | `<span class="logo-text">E-VOTE <strong>NIGERIA</strong></span>` |
| 29 | `<a href="verify-pvc.html">Verify PVC</a>` |
| 65 | `Nigerian citizen. Your vote is your voice, protected by` |
| 203 | `<span class="logo-text">E-VOTE NG</span>` |
| 207 | `Federal Republic of Nigeria. Built for transparency,` |

### 3.2 `dashboard.html`

| Line | Text |
|---|---|
| 6 | `<title>Dashboard | Nigeria E-Vote</title>` |
| 42 | `<span class="logo-text">NIGERIA <strong>E-VOTE</strong></span>` |
| 152 | `Every vote cast on the <strong>Nigeria E-Vote</strong> platform is cryptographically signed...` |
| 282 | `<span class="profile-value">c********@e-vote.gov.ng</span>` |
| 454 | `localStorage.removeItem('nigeriaEVoteStatus');` |
| 522 | `verificationId: 'NG-E-VOTE-2026-' + selected + '-' + ...` |
| 526 | `if (localStorage.getItem('nigeriaEVoteStatus') === 'cast') {` |
| 573 | `localStorage.setItem('nigeriaEVoteReceipt', JSON.stringify(receipt));` |
| 574 | `localStorage.setItem('nigeriaEVoteStatus', 'cast');` |

### 3.3 `login.html`

| Line | Text |
|---|---|
| 6 | `<title>Government Portal Login | Nigeria E-Vote</title>` |
| 18 | `<span class="logo-text">NIGERIA <strong>E-VOTE</strong></span>` |

### 3.4 `auth.html`

| Line | Text |
|---|---|
| 6 | `<title>Secure Voter Authentication | Nigeria E-Vote</title>` |
| 17 | `<span class="logo-text">NIGERIA <strong>E-VOTE</strong></span>` |
| 134 | `<p>Linked to your PVC biometric data for maximum security.</p>` |

### 3.5 `candidates.html`

| Line | Text |
|---|---|
| 6 | `<title>Candidates | Nigeria E-Vote</title>` |
| 37 | `<span class="logo-text">E-VOTE <strong>NIGERIA</strong></span>` |
| 41 | `<a href="verify-pvc.html">Verify PVC</a>` |
| 131 | `<span class="logo-text">E-VOTE NG</span>` |
| 133 | `<p class="footer-desc">The official digital voting infrastructure for the Federal Republic of Nigeria.</p>` |
| 140 | `<li><a href="verify-pvc.html">Verification Guide</a></li>` |

### 3.6 `election-center.html`

| Line | Text |
|---|---|
| 6 | `<title>Election Center | Nigeria E-Vote</title>` |
| 114 | `<span class="logo-text">E-VOTE <strong>NIGERIA</strong></span>` |
| 118 | `<a href="verify-pvc.html">Verify PVC</a>` |
| 148 | `Stay updated on all active, upcoming, and past elections across the Federal Republic of Nigeria.` |
| 175 | `Cast your vote for the next President of the Federal Republic of Nigeria.` |
| 200 | `<span><strong>Candidate C (NF)</strong><br><span class="text-sm text-gray">Nigeria First</span></span>` |
| 296 | `<h3>Verify Your PVC</h3>` |
| 297 | `Ensure your Permanent Voter's Card (PVC) is linked to your National Identification Number (NIN)` |
| 298 | `<a href="verify-pvc.html" class="text-green font-medium">Verify Now` |
| 322 | `<span class="logo-text">E-VOTE NG</span>` |
| 324 | `The official digital voting infrastructure for the Federal Republic of Nigeria...` |
| 331 | `<li><a href="verify-pvc.html">Verification Guide</a></li>` |

### 3.7 `receipt.html`

| Line | Text |
|---|---|
| 6 | `<title>Vote Receipt | Nigeria E-Vote</title>` |
| 46 | `<input id="verificationId" type="text" readonly value="NG-E-VOTE-2026-X99-8821-B4">` |
| 61 | `<span class="logo-text">E-VOTE SYSTEM</span>` |
| 63 | `<p>Federal Republic of Nigeria • Secure Voting Protocol v4.2.0</p>` |
| 71 | `var raw = localStorage.getItem('nigeriaEVoteReceipt');` |

### 3.8 `results.html`

| Line | Text |
|---|---|
| 6 | `<title>Live Results | Nigeria E-Vote</title>` |
| 33 | `<span class="logo-text">E-VOTE <strong>NIGERIA</strong></span>` |
| 37 | `<a href="verify-pvc.html">Verify PVC</a>` |

### 3.9 `security.html`

| Line | Text |
|---|---|
| 6 | `<title>Security | Nigeria E-Vote</title>` |
| 35 | `<span class="logo-text">E-VOTE <strong>NIGERIA</strong></span>` |
| 39 | `<a href="verify-pvc.html">Verify PVC</a>` |
| 69 | `Learn how the Nigeria E-Vote platform uses advanced cryptographic protocols...` |
| 81 | `Distributed nodes across Nigeria validate integrity continuously.` |
| 90 | `...linking the platform directly to the National Identity Management Commission (NIMC) database, we cross-verify your PVC against your NIN.` |

### 3.10 `verify-pvc.html`

| Line | Text |
|---|---|
| 6 | `<title>Verify PVC | Nigeria E-Vote</title>` |
| 25 | `<span class="logo-text">E-VOTE <strong>NIGERIA</strong></span>` |
| 29 | `<a href="verify-pvc.html" class="active-link">Verify PVC</a>` |
| 85 | `<p class="footer-desc">The official digital voting infrastructure for the Federal Republic of Nigeria.</p>` |

### 3.11 `scripts.js`

| Line | Text |
|---|---|
| — | `localStorage` keys: `'nigeriaEVoteStatus'`, `'nigeriaEVoteReceipt'`, `'evote-theme'` |
| — | Verification ID format: `'NG-E-VOTE-2026-'` |
| — | Locale: `'en-NG'` (Nigeria English) |

### 3.12 Summary of Key Branding Terms

| Term | Occurrences |
|---|---|
| `Nigeria` | 20+ (titles, logos, page descriptions, localStorage keys, NIMC reference) |
| `E-Vote` / `E-VOTE` | 20+ (brand name in logo, titles, localStorage keys, verification IDs) |
| `Federal Republic of Nigeria` | 5 (footer descriptions, election-center, receipt) |
| `Nigerian` | 2 (hero text, results page) |
| `PVC` (Permanent Voter's Card) | 10+ (page title, nav links, section headers, descriptions) |
| `Verify PVC` | 7 (nav items across all pages) |
| `E-VOTE NG` | 4 (footer logos) |
| `NG-E-VOTE-2026` | 2 (verification ID format) |
| `e-vote.gov.ng` | 1 (email domain) |
| `Nigeria First` | 1 (political party name in election-center) |
| `National Identity Management Commission (NIMC)` | 1 (security page) |
| `NIN` | 5+ (National Identification Number references) |
| `en-NG` locale | 1 (date formatting in dashboard) |
| `Lagos`, `Kano`, `Rivers`, `FCT Abuja`, `Kaduna` | State names in results tables |

---

## 4. Navigation Audit

### 4.1 Header Navigation (Public Pages)

Present on: `index.html`, `candidates.html`, `election-center.html`, `results.html`, `security.html`, `verify-pvc.html`

| Order | Label | Link | Notes |
|---|---|---|---|
| Logo | `E-VOTE NIGERIA` | `index.html` | Brand logo linking to home |
| 1 | Election Center | `election-center.html` | |
| 2 | Verify PVC | `verify-pvc.html` | |
| 3 | Candidates | `candidates.html` | |
| 4 | Results | `results.html` | |
| 5 | Security | `security.html` | |
| — | Sign Up | `auth.html` | `.nav-login` class |
| — | Login | `login.html` | `.btn-primary` class |

### 4.2 Header Navigation (Authenticated — Dashboard)

Present on: `dashboard.html`

| Order | Label | Link | Notes |
|---|---|---|---|
| Logo | `NIGERIA E-VOTE` | `dashboard.html` | |
| 1 | Dashboard | `#` (JS toggle) | `#dashboardView` |
| 2 | View Results | `#` (JS toggle) | `#resultsView` |
| 3 | Profile | `#` (JS toggle) | `#profileView` |
| — | Logout | `#` (JS modal) | `logoutBtn` |

### 4.3 Header Navigation (Auth Pages)

Present on: `login.html`, `auth.html`

| Order | Label | Link | Notes |
|---|---|---|---|
| Logo | `NIGERIA E-VOTE` | `index.html` | |
| 1 | Back to Home | `index.html` | |
| 2 | Help Center | `#` | |

### 4.4 Footer Navigation

Present on: `index.html`, `candidates.html`, `election-center.html`, `verify-pvc.html`
Abbreviated on: `results.html`, `security.html`, `dashboard.html`

**Full Footer (index, candidates, election-center, verify-pvc):**

| Section | Links |
|---|---|
| **Brand** | Logo: `E-VOTE NG`, Description (references Federal Republic of Nigeria) |
| **Resources** | Voter Education, Electoral Acts, Verification Guide (`verify-pvc.html`), FAQ |
| **Support** | Help Center, Report Issue, Contact Support, Privacy Policy |
| **Social** | 𝕏, f, in |
| **Bottom** | © 2026, Terms of Service, Data Protection Policy |

**Abbreviated Footer (results.html, security.html):**
- `© 2026 All Rights Reserved.` only

**Dashboard Footer (dashboard.html):**
- `© 2026 Digital Election Division`
- Privacy Policy, Terms of Use, Help Desk, Security Audit Report

**Auth Footer (login.html, auth.html):**
- Support Center, Privacy Policy, Voter Guide/Guide/Voter Guidelines, Accessibility/Election Portal

### 4.5 Mobile Navigation

No dedicated mobile menu (hamburger/drawer) was found. The `scripts.js` contains logic to hide the navbar when the footer enters viewport on mobile (`window.innerWidth <= 768`), but there is no responsive hamburger menu implementation. The nav links are displayed inline and rely on CSS overflow behavior.

---

## 5. Content Audit

### 5.1 Hero Sections

| Page | Description |
|---|---|
| `index.html` | Full hero with image background (`resources/homepage.png`). Title: "The Future of Transparent Elections". Subtitle about "Secure, blockchain-verified... for every Nigerian citizen". CTA: "Register to Vote" and "How it Works". |

### 5.2 Feature Sections

| Page | Description |
|---|---|
| `index.html` | Trusted badge ("Official Digital Election Infrastructure"), Security Status card (Cloud, Blockchain, Identity Gateway statuses) |
| `auth.html` | Trust badges (Biometric Sync, Privacy First, Audit Trail) with descriptions |
| `election-center.html` | Guidelines section (Verify PVC, OTP Authentication, Electoral Process) with 3 guide cards |
| `security.html` | 3 security features (Immutable Blockchain Ledger, Multi-Factor Identity Gateway, Military-Grade Cloud Infrastructure) |
| `dashboard.html` | Blockchain verification description and voter verification status list |

### 5.3 Statistics Sections

| Page | Description |
|---|---|
| `index.html` | Stats grid with 4 animated counters: Registered Voters (84.2M), Biometric Verifications (12.5M), Active Polls (18), Node Integrity (100%) |
| `dashboard.html` | Status bar: Election Status (ACTIVE), Countdown timer, Registered Voters (93.4M), Total Votes Cast (12.8M), Your Status |

### 5.4 CTA Sections

| Page | CTA |
|---|---|
| `index.html` | "Register to Vote" (→ `auth.html`), "How it Works" (→ `#`) |
| `index.html` | "View Security Audit" button |
| `security.html` | "Download Technical Whitepaper" button |
| `receipt.html` | "Proceed Back to Dashboard" (→ `dashboard.html`), "Download Receipt (PDF)" |
| `verify-pvc.html` | "Check Status" → "Proceed to Sign Up" (→ `auth.html`) |
| `election-center.html` | "View Candidates" (→ `candidates.html`), "Vote Now" (→ `login.html`) |

---

## 6. Asset Audit

### 6.1 Logos

| Asset | Location | Description |
|---|---|---|
| `.logo-icon` | CSS class in `index.css` (all pages) | Green square icon (styled via CSS — 40×40px `border-radius: 10px` with `#008751` background and inner circle) |
| Brand text "E-VOTE NIGERIA" | Header of all public pages | Text-based brand |
| Brand text "NIGERIA E-VOTE" | Header of `dashboard.html`, `login.html`, `auth.html` | Text-based brand |
| Brand text "E-VOTE NG" | Footer of `index.html`, `candidates.html`, `election-center.html`, `verify-pvc.html` | Text-based brand |
| Brand text "E-VOTE SYSTEM" | `receipt.html`, line 61 | Text-based brand footer variant |

### 6.2 Icons

| Source | Usage |
|---|---|
| Flaticon UIcons (`uicons-regular-straight`) | All pages — various icons (`fi-rs-*` classes for users, chart, lock, envelope, badge, shield, etc.) |
| CSS-based social icons | Footer: 𝕏 (X/Twitter), f (Facebook), in (LinkedIn) — plain text characters |
| Inline SVG | Check/circle animations in modals (`auth-modal__check`, `confirm-modal`) |

### 6.3 Images

| File | Location | Size | Usage |
|---|---|---|---|
| `resources/homepage.png` | Referenced in `index.html` and `dashboard.html` | ~2 MB | Hero background image (homepage) and dashboard background |

### 6.4 Favicons

| Status | Details |
|---|---|
| **Not found** | No favicon or apple-touch-icon is defined in any HTML file. No favicon files exist in the project. |

---

## 7. Summary of Rebranding Requirements

To rebrand this project away from Nigeria-specific theming:

1. **Site title changes** across all 10 HTML files (e.g., "Nigeria E-Vote" → new brand name)
2. **Logo text changes** in all headers and footers (E-VOTE NIGERIA, NIGERIA E-VOTE, E-VOTE NG, E-VOTE SYSTEM)
3. **Hero content** rewrite (`index.html` — remove "Nigerian citizen" references)
4. **Footer descriptions** in 4+ files (remove "Federal Republic of Nigeria")
5. **LocalStorage keys** in `dashboard.html` (`nigeriaEVoteStatus`, `nigeriaEVoteReceipt`)
6. **Verification ID format** in `dashboard.html` (`NG-E-VOTE-2026-`)
7. **Email domain** in `dashboard.html` (`@e-vote.gov.ng`)
8. **Locale** in `dashboard.html` (`en-NG` → appropriate locale)
9. **State names** in `dashboard.html` and `results.html` (Lagos, Kano, Rivers, FCT Abuja, Kaduna)
10. **Party name** in `election-center.html` ("Nigeria First" party)
11. **NIMC reference** in `security.html` (National Identity Management Commission)
12. **NIN/PVC concept** across multiple pages — decide whether to keep or replace the voter ID concepts
13. **Page URLs** like `verify-pvc.html` may need renaming
14. **Favicon** needs to be created (currently absent)
