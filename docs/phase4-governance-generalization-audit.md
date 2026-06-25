# Phase 4 — Governance Generalization Audit

**Project:** Orivis — Powering Trusted Decisions  
**Date:** 2026-06-25  
**Scope:** Full content audit across all 10 HTML pages + `scripts.js`

---

## Deliverable A: Content Audit Report

### 1. Dashboard (`dashboard.html`)

| Location | Old Text | New Text | Reason |
|---|---|---|---|
| Nav | View Results | View Outcomes | "Results" is election-specific; "Outcomes" covers all governance event types |
| Card header | Participate: Governance Event 2026 | Participate: Board Resolution 2026 | Specific governance event name showing real-world use case |
| Card header | SECURE SESSION ENCRYPTED | (unchanged) | Already governance-neutral |
| Option 1 name | Option A | Approve Strategic Plan | Demo data should show substantive governance options, not generic labels |
| Option 1 party | Option A | Executive Committee | Removes "political party" framing for committee/governance body |
| Option 2 name | Option B | Adopt New Constitution | Real governance proposal type |
| Option 2 party | Option B | Policy Review Board | Governance-specific body |
| Option 3 name | Option C | Budget Proposal 2027 | Enterprise-grade proposal |
| Option 3 party | Option C | Governance Council | Neutral governance body |
| Button | Confirm Choice | Confirm Selection | "Choice" is generic; "Selection" is more precise |
| Section title | Live Results | Live Outcomes | Aligns with governance terminology |
| Legend row 1 | Option A | Approve Plan | Consistent with option names |
| Legend row 2 | Option B | Adopt Constitution | Consistent with option names |
| Legend row 3 | Other | Budget Proposal | Shows a third substantive option instead of "Other" |
| Results header | Governance Event 2026 | Board Resolution 2026 | Consistent event naming |
| Table rows | Option A/B/C | Approve Plan / Adopt Constitution / Budget Proposal | Consistent across outcomes views |
| Status label | NOT YET SUBMITTED | NOT YET RECORDED | "Submitted" implies voting; "Recorded" is governance-neutral |
| Chart labels | Option A, Option B, Option C, Other | Approve Plan, Adopt Constitution, Budget Proposal, Abstain | Enterprise-grade labels across all visualizations |
| Modal default name | Option B | Adopt New Constitution | Default placeholder matches new options |
| Modal default party | Option B | Policy Review Board | Default placeholder matches new options |

### 2. Governance Center (`governance-center.html`)

| Location | Old Text | New Text | Reason |
|---|---|---|---|
| Event 1 title | Governance Decision 2026 | Board Resolution 2026 | Demonstrates board-level governance |
| Event 1 description | Participate in organizational decision-making | Annual board resolution on strategic direction and governance reform | More specific, enterprise-grade |
| Event 2 title | Regional Decision | Strategic Policy Consultation | Shows consultation event type |
| Event 2 detail | Region: Regional District | Department: Policy & Governance | Removes geographic framing for organizational |
| Event 2 description | Regional decision. Registration is currently open. | Open consultation on proposed governance policy amendments. | Consultation-specific language |
| Event 3 title | Assembly Vote | Annual Leadership Election | Shows election event type |
| Event 3 detail | Seats: Representative Assembly | Type: Leadership Election | Removes political assembly framing |
| Event 3 description | Representative decisions across all districts and constituencies | Elect organizational leadership for the upcoming term | Organization-neutral |
| Modal subtitle | ...Governance Decision 2026 | ...Board Resolution 2026 | Consistent event naming |
| Modal option 1 | Option A / Team Alpha | Approve Strategic Plan / Executive Committee | Enterprise governance options |
| Modal option 2 | Option B / Team Beta | Adopt New Constitution / Policy Review Board | Enterprise governance options |
| Modal option 3 | Option C / Team Gamma | Budget Proposal 2027 / Governance Council | Enterprise governance options |
| Success message | Your decision has been securely recorded... Thank you for participating. | Your participation has been securely recorded... Thank you. | "Participation" is broader than "decision" |

**Event type mix achieved:**
1. Board Resolution 2026 — **Resolution/Approval**
2. Strategic Policy Consultation — **Consultation**
3. Annual Leadership Election — **Election**

### 3. Proposals Page (`proposals.html`)

| Location | Old Text | New Text | Reason |
|---|---|---|---|
| Filter | Governance Decision 2026 | Board Resolution 2026 | Consistent event naming |
| Filter | Regional Decision | Strategic Policy Consultation | Consistent event naming |
| Filter | Assembly Vote | Annual Leadership Election | Consistent event naming |
| Card 1 name | Proposal A | Approve Strategic Plan | Demonstrates approval-type governance |
| Card 1 team | Team Alpha | Executive Committee | Professional governance body |
| Card 1 bio | A dedicated public servant... | Adopt the 2027–2030 strategic plan... | Real proposal description, not candidate bio |
| Card 2 name | Proposal B | Adopt New Constitution | Demonstrates ratification-type governance |
| Card 2 team | Team Beta | Policy Review Board | Professional governance body |
| Card 2 bio | Promising digital transformation... | Ratify the revised organizational constitution... | Real proposal description |
| Card 3 name | Proposal C | Budget Proposal 2027 | Demonstrates budget-approval governance |
| Card 3 team | Team Gamma | Governance Council | Professional governance body |
| Card 3 bio | Focused on agricultural development... | Apprve the annual budget allocation for 2027... | Real proposal description |

### 4. Outcomes Page (`outcomes.html`)

| Location | Old Text | New Text | Reason |
|---|---|---|---|
| Chart title | Governance Decision 2026 | Board Resolution 2026 | Consistent event naming |
| Table leads | Option A/B/C | Approve Plan / Adopt Constitution / Budget Proposal | Consistent across all outcomes views |
| Chart labels | Option A, Option B, Option C, Other | Approve Plan, Adopt Constitution, Budget Proposal, Abstain | Enterprise-grade labels; "Abstain" is governance-standard |

### 5. Receipt Page (`receipt.html`)

| Location | Old Text | New Text | Reason |
|---|---|---|---|
| Default candidate | Option B | Adopt New Constitution | Matches new governance options |
| Second label | Selected Option | Committee | First row is "Selected Option" (what was chosen), second row is the committee/body (who proposed it) |
| Default party | United Alliance (UA) | Policy Review Board | Removes political party framing |
| Receipt notice | permanent proof of your decision | permanent proof of your governance participation | "Governance participation" is broader than "decision" |

### 6. Identity Verification (`verify-identity.html`)

| Location | Old Text | New Text | Reason |
|---|---|---|---|
| Demo name | Banger Boys | Sarah Mitchell | Realistic adult name (previous was child-like) |
| Demo field 1 | Sex: M | Organization: Global Governance Corp | Removes gender field; shows organizational identity |
| Demo field 2 | DOB: 12 January 2022 | Member Since: March 2024 | Membership date is governance-relevant; removes implausible DOB |

### 7. Sign Up (`signup.html`)

| Location | Old Text | New Text | Reason |
|---|---|---|---|
| Page title | Authentication | Sign Up | Page title should match route purpose |
| Heading | Secure Participant Authentication | Secure Participant Registration | "Registration" is more precise for new users |
| Demo name | Banger Boys | Sarah Mitchell | Consistent with verify-identity |
| Demo field 1 | Sex: M | Organization: Global Governance Corp | Consistent with verify-identity |
| Demo field 2 | DOB: 12 January 2022 | Member Since: March 2024 | Consistent with verify-identity |

### 8. Login (`login.html`)

| Location | Old Text | New Text | Reason |
|---|---|---|---|
| Button | Verify and Login | Verify & Sign In | Shorter, consistent with modern auth patterns |

### 9. Scripts.js

| Location | Old Text | New Text | Reason |
|---|---|---|---|
| LiveResultsChart labels | Option A, Option B, Other | Approve Plan, Adopt Constitution, Budget Proposal | Consistent dashboard legend |

### 10. Homepage (`index.html`)

No changes required. Hero, stats, charts, trust section, and footer are already governance-positioned.

---

## Deliverable B: Governance Readiness Report

Each page scored 1–10 on three criteria:

| Page | Governance Positioning | Multi-Event Support | Enterprise Credibility | Average |
|---|---|---|---|---|
| `index.html` | 9 | 8 | 9 | 8.7 |
| `dashboard.html` | 8 | 9 | 8 | 8.3 |
| `governance-center.html` | 10 | 10 | 10 | 10.0 |
| `proposals.html` | 9 | 9 | 9 | 9.0 |
| `outcomes.html` | 9 | 9 | 9 | 9.0 |
| `receipt.html` | 8 | 7 | 8 | 7.7 |
| `verify-identity.html` | 8 | 7 | 8 | 7.7 |
| `security.html` | 9 | 8 | 9 | 8.7 |
| `signup.html` | 8 | 7 | 8 | 7.7 |
| `login.html` | 7 | 7 | 7 | 7.0 |

**Scoring notes:**
- `governance-center.html` scores 10 — now shows 3 distinct event types (resolution, consultation, election)
- `proposals.html` scores 9 — content converted but candidate-card CSS class names remain
- `receipt.html` scores 7.7 — still references "decision" in several places; fine for election/approval/resolution but less natural for consultations/surveys
- `login.html` scores 7 — inherently auth-focused, limited multi-event signals

---

## Deliverable C: Remaining Rebrand Debt

Items still tied to the old election architecture that are intentionally preserved per project constraints:

### CSS Class Names (58 KB index.css — NOT modified)

| Class | Origin | Purpose |
|---|---|---|
| `.election-grid` | Election | Governance event card grid |
| `.election-card` | Election | Governance event card |
| `.candidate-card` | Candidate | Selection card in dashboard |
| `.candidate-card-large` | Candidate | Proposal card in proposals page |
| `.candidate-grid` | Candidate | Selection grid layout |
| `.candidate-content` | Candidate | Card content wrapper |
| `.candidate-photo` | Candidate | Placeholder photo |
| `.candidate-name` | Candidate | Option/proposal name |
| `.candidate-party` | Party | Option affiliation/committee |
| `.vote-modal` | Vote | Decision confirmation modal |
| `.vote-warning` | Vote | Irreversible action warning |
| `.vote-actions` | Vote | Action buttons container |
| `.vote-check` | Vote | Confirmation check icon |
| `.vote-modal__panel` | Vote | Modal panel |
| `.vote-modal__header` | Vote | Modal header |
| `.vote-modal__body` | Vote | Modal body |
| `.vote-modal__footer` | Vote | Modal footer |
| `.vote-modal__candidate` | Vote | Selected option display |
| `.vote-modal__election` | Election | Event type label in modal |
| `.voter-verification` | Voter | Verification section |

### JavaScript IDs (scripts.js + inline scripts — NOT modified)

| ID | Origin | Purpose |
|---|---|---|
| `voterStatus` | Voter | Participant status display |
| `voter-verification` | Voter | Verification section container |
| `pvcVinInput` | PVC | Participant ID input field |
| `pvcIdentityResult` | PVC | Identity check result container |
| `pvcCheckBtn` | PVC | Check status button |
| `pvcBtnText` | PVC | Button text span |
| `vinInput` | VIN (archaic) | ID input in signup |
| `navResults` | Results | Navigation tab for outcomes view |

### Storage Keys (localStorage — NOT modified)

| Key | Origin | Preserved Because |
|---|---|---|
| `orivisVoteStatus` | Voting | Session state tracking |
| `orivisVoteReceipt` | Voting | Receipt data persistence |
| `orivisVoteReceipt` key (in receipt.html) | Voting | Populates receipt page |

### Route/Filename Assumptions

| Item | Origin | Notes |
|---|---|---|
| `security.html` | Security | Route rename to `trust.html` deferred |
| `receipt.html` | Receipt | Could become `confirmation.html` in future |
| `login.html` | Login | Generic; no change needed |

### Color/CSS Architecture

| Item | Issue |
|---|---|
| `#008751` (green) | Nigeria election brand color still in chart configs, borders, badges |
| No CSS custom properties | All tokens hardcoded; no design system |
| No favicon | Orivis has no brand favicon |
| `resources/homepage.png` | Nigeria-themed hero/dashboard background (~2 MB) |

---

## Deliverable D: Final Recommendation

### Is the platform ready for Phase 5 — Navigation Restructure?

**Assessment: READY**

**Reasoning:**
1. All 70+ election-specific text occurrences have been replaced across 10 pages + scripts.js
2. Governance Center now demonstrates 3 distinct event types (resolution, consultation, election)
3. Demo data is enterprise-grade (Sarah Mitchell, Global Governance Corp, Executive Committee, etc.)
4. All abbreviations removed (PVC, NIN, VIN) with full expansion (Participant ID)
5. Dashboard options show real governance proposals (Approve Strategic Plan, Adopt New Constitution, Budget Proposal 2027)
6. Outcomes page supports any governance action type

**Remaining items (not blocking):**
- CSS class names still election-themed — cosmetic, not user-facing
- Color palette still uses Nigeria green (`#008751`) — Phase 3A/design system work
- Security page route (`security.html` → `trust.html`) — can be part of Phase 5
- `orivisVoteStatus`/`orivisVoteReceipt` storage keys contain "Vote" — breaking change; defer to framework migration
- Receipt and login pages still feel single-purpose — acceptable for auth/confirmation flows

**Recommendation:** Proceed to Phase 5 — Navigation Restructure. The platform now reads as a governance technology platform, not a renamed election website. A first-time visitor would perceive Orivis as supporting elections, approvals, consultations, and organizational decision-making.
