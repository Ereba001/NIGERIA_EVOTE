# Phase 1 Summary — Global Text Rebrand

> Completed: 2026-06-25
> Project: Orivis (formerly Nigeria E-Vote)

---

## Files Changed

| # | File | Changes |
|---|---|---|
| 1 | `index.html` | Title, meta description, hero content, nav label, stats labels, footer description, footer links, CTA text, trusted badge |
| 2 | `dashboard.html` | Title, logo text, 4 content references, email domain, 3 localStorage keys, locale, verification ID format, status bar, profile labels, vote modal, results section, footer |
| 3 | `login.html` | Title, logo text, heading, description, form labels |
| 4 | `auth.html` | Title, logo text, heading, step description, NIN label, phone placeholder, trust badge text, footer links |
| 5 | `candidates.html` | Title, logo text, nav label, page heading, filter options, footer description, footer logo, footer links |
| 6 | `election-center.html` | Title, logo text, nav label, page description, election card titles/descriptions, modal text, election types, filter options, NIN references, footer description, footer logo, footer links, guide card content |
| 7 | `receipt.html` | Title, verification ID value, footer logo, footer description, localStorage key |
| 8 | `results.html` | Title, logo text, nav label, page description, chart subtitle |
| 9 | `security.html` | Title, logo text, nav label, page description, 4 content references |
| 10 | `verify-pvc.html` | Title, logo text, nav label, page heading, description, form label, placeholder, footer description, footer logo, error message, success message |
| 11 | `scripts.js` | Chart dataset label ("Voter Registration" → "Participant Registration") |

**Total files modified: 11** (10 HTML + 1 JS)

---

## Branding Changes Made

### Brand Name Replacements

| Old | New | Locations |
|---|---|---|
| `Nigeria E-Vote` (page titles) | `Orivis` | All 10 HTML files |
| `E-VOTE NIGERIA` (header logo) | `Orivis` | `index.html`, `candidates.html`, `election-center.html`, `results.html`, `security.html`, `verify-pvc.html` |
| `NIGERIA E-VOTE` (header logo) | `Orivis` | `dashboard.html`, `login.html`, `auth.html` |
| `E-VOTE NG` (footer logo) | `Orivis` | `index.html`, `candidates.html`, `election-center.html`, `verify-pvc.html` |
| `E-VOTE SYSTEM` (receipt logo) | `Orivis` | `receipt.html` |

### Page Titles

| Page | Old Title | New Title |
|---|---|---|
| Home | "Nigeria E-Vote \| Home" | "Home \| Orivis" |
| Dashboard | "Dashboard \| Nigeria E-Vote" | "Dashboard \| Orivis" |
| Login | "Government Portal Login \| Nigeria E-Vote" | "Login \| Orivis" |
| Auth | "Secure Voter Authentication \| Nigeria E-Vote" | "Authentication \| Orivis" |
| Candidates | "Candidates \| Nigeria E-Vote" | "Candidates \| Orivis" |
| Election Center | "Election Center \| Nigeria E-Vote" | "Election Center \| Orivis" |
| Receipt | "Vote Receipt \| Nigeria E-Vote" | "Receipt \| Orivis" |
| Results | "Live Results \| Nigeria E-Vote" | "Results \| Orivis" |
| Security | "Security \| Nigeria E-Vote" | "Security \| Orivis" |
| Verify PVC | "Verify PVC \| Nigeria E-Vote" | "Identity Verification \| Orivis" |

### Hero Section (`index.html`)

- "Transparent Elections" → "Trusted Governance"
- "Nigerian citizen" → "organization"
- "sovereign-grade encryption" → "enterprise-grade encryption"
- "Register to Vote" → "Get Started"

### Navigation Labels

| Old Label | New Label | File(s) |
|---|---|---|
| Verify PVC | Verify Identity | All pages with nav (7 files) |

### Footer Descriptions

| Old | New |
|---|---|
| "The official digital voting infrastructure for the Federal Republic of Nigeria. Built for transparency, security, and the future of democracy." | "Orivis is a governance technology platform that enables transparent and trusted decision-making." |
| "The official digital voting infrastructure for the Federal Republic of Nigeria." | Same as above |

### Footer Links

| Old | New |
|---|---|
| Voter Education | Education |
| Electoral Acts | Governance Guides |
| Voter Guide | Participant Guide |
| Voter Guidelines | Participant Guidelines |
| Election Portal | Governance Portal |

### Elections → Governance Events

| Old | New |
|---|---|
| Presidential Election 2026 | Leadership Election 2026 |
| Lagos Gubernatorial | Regional Election |
| National Assembly | Assembly Election |
| President of the Federal Republic of Nigeria | organizational leadership |
| Nigeria First (party) | National Front |
| Federal (election type) | Organization |
| State (election type) | Regional |
| National election results | Governance results |
| National registration activity | Registration activity |

### Terminology Changes

| Old | New |
|---|---|
| Voter Authentication | Participant Authentication |
| Secure Voter Authentication | Secure Participant Authentication |
| Voter Enrollment Trends | Participant Enrollment Trends |
| Registered Voters | Registered Participants |
| Biometric Verifications | Identity Verifications |
| Active Polls | Active Events |
| Voter ID | ID / Participant ID |
| Voter's ID | Participant ID |
| Voter Verification | Identity Verification |
| VERIFIED VOTER badge | VERIFIED PARTICIPANT |
| NIN (National Identification Number) | Participant ID |
| Voter ID (VIN) or NIN | Participant ID |
| PVC (Permanent Voter's Card) | Identity Verification / ID |
| PVC verified successfully | Identity verified successfully |
| State of Origin | Region |
| LGA | District |
| Polling Unit | Voting Center |
| NIN Linked | ID Linked |
| Biometric Match | Identity Match |
| National Identity Management Commission (NIMC) | trusted identity verification systems |
| cross-verify your PVC against your NIN | cross-verify your identity against your Participant ID |

### Receipt & Verification IDs

| Old | New |
|---|---|
| `NG-E-VOTE-2026-X99-8821-B4` | `ORIVIS-2026-X99-8821-B4` |
| `NG-E-VOTE-2026-` (generation format) | `ORIVIS-2026-` |
| "Federal Republic of Nigeria • Secure Voting Protocol v4.2.0" | "Orivis • Secure Governance Protocol v4.2.0" |

### Email Domain

| Old | New |
|---|---|
| `@e-vote.gov.ng` | `@orivis.io` |

### LocalStorage Keys

| Old Key | New Key | Used In |
|---|---|---|
| `nigeriaEVoteStatus` | `orivisVoteStatus` | `dashboard.html` (get/remove/set) |
| `nigeriaEVoteReceipt` | `orivisVoteReceipt` | `dashboard.html` (set), `receipt.html` (get) |

### Meta Description (`index.html`)

| Old | New |
|---|---|
| "Official Nigeria E-Vote portal for secure, transparent elections." | "Orivis — Powering Trusted Decisions. A governance technology platform for transparent, secure, and verifiable decision-making." |

### Chart Labels (`scripts.js`)

| Old | New |
|---|---|
| "Voter Registration (Millions)" | "Participant Registration (Millions)" |

### Dashboard Footer

| Old | New |
|---|---|
| "© 2026 Digital Election Division" | "© 2026 Orivis" |

### Auth Page Description

| Old | New |
|---|---|
| "access the 2026 General Election ballot" | "access the governance platform" |

---

## Items Intentionally Left Unchanged

1. **Page routes/filenames** (`verify-pvc.html`, `election-center.html`, `candidates.html`, `auth.html`, `dashboard.html`, `results.html`, `security.html`, `receipt.html`, `login.html`)

   *The instruction explicitly stated not to change page routes in Phase 1. These will be renamed in a future phase.*

2. **JavaScript variable names containing "pvc" / "nin"** (e.g., `pvcVinInput`, `pvcCheckBtn`, `portalNin`, `pvcIdentityResult`)

   *These are internal DOM element IDs and JS variables. Renaming them would break JavaScript functionality, which the instruction said not to modify. The visible labels and text they produce have been updated.*

3. **CSS file (`index.css`)**

   *No changes to CSS were made, as instructed. All branding changes were content-only.*

4. **Theme localStorage key (`evote-theme`)**

   *This key stores the user's dark/light mode preference, not branding identity. It was left unchanged to preserve user theme preferences across the rebrand.*

5. **Server file (`server.js`)**

   *No branding content in this file. It serves all files regardless of name.*

6. **Vercel config (`vercel.json`)**

   *No branding content in this file.*

7. **`en-US` locale in chart formatting**

   *Changed from `en-NG` (Nigeria English) to `en-US` as a neutral default locale.*

8. **State data in results tables** (Lagos, Kano, Rivers, FCT Abuja, Kaduna)

   *These are placeholder demo data in the state breakdown tables. They remain as-is since they serve as example data. If needed, these can be replaced with generic region names in a future phase.*

---

## Recommendations for Phase 2

1. **Rename page routes/files** — `verify-pvc.html` → `verify-identity.html`, `election-center.html` → `governance-center.html` or similar
2. **Update link references** across all files once routes are renamed
3. **Replace sample state data** in results tables with neutral regional labels
4. **Create a favicon** — currently the project has none
5. **Evaluate the logo** — currently CSS-only (green square with inner circle); may need a proper Orivis logo asset
6. **Review the hero background image** (`resources/homepage.png`) — still shows Nigeria-themed imagery; replace with neutral governance imagery
7. **Update the `server.js`** MIME types if new file extensions are introduced
8. **Demo identity data** — the test ID `1234567` returns "Banger Boys" profile which may need updating
9. **CSS variable references** — may contain legacy color naming tied to the old brand
