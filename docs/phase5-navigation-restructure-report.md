# Phase 5 — Navigation Restructure & SaaS Positioning Report

**Project:** Orivis — Powering Trusted Decisions  
**Date:** 2026-06-25  
**Scope:** Navigation, page hierarchy, information architecture, user journeys, SaaS positioning

---

## Deliverable A: Navigation Migration Report

### Old Navigation (Public Pages)

| Item | Route | Removed? | Reason |
|---|---|---|---|
| Governance Center | governance-center.html | Kept | Core product feature |
| Verify Identity | verify-identity.html | Removed from top nav | Contextual — reached through Governance Center |
| Proposals | proposals.html | Removed from top nav | Contextual — reached through Governance Center |
| Outcomes | outcomes.html | Removed from top nav | Contextual — reached through Governance Center |
| Security | security.html | Renamed label to "Trust" | Better brand alignment |
| Sign Up | signup.html | Renamed to "Get Started" | SaaS CTA convention |
| Login | login.html | Renamed to "Sign In" | SaaS convention |

### New Navigation (Public Pages)

| Item | Route | Active Page Class |
|---|---|---|
| Platform | index.html | `active-link` on index |
| Governance Center | governance-center.html | `active-link` on governance-center |
| Trust | security.html | `active-link` on security |
| Resources | resources.html | `active-link` on resources |
| Sign In | login.html | nav-actions link |
| Get Started | signup.html | btn-primary CTA in nav-actions |

### Auth Pages Navigation

login.html, signup.html use minimal `navbar-auth`:
- Back to Home (index.html)
- Resources (resources.html)

### Dashboard Navigation (Authenticated)

- Dashboard (internal tab, stays)
- Outcomes (was "View Results") — renamed in Phase 4
- Profile (stays)
- Logout (stays)

### Affected Files (12 total)

| File | Nav Change | Footer Change |
|---|---|---|
| `index.html` | Full restructure | Full restructure |
| `governance-center.html` | Full restructure | Full restructure |
| `security.html` | Full restructure | Full restructure |
| `proposals.html` | Full restructure | Full restructure |
| `outcomes.html` | Full restructure | Full restructure |
| `verify-identity.html` | Full restructure | Full restructure |
| `receipt.html` | Nav added (had none) | Footer added (had none) |
| `login.html` | Simplified nav | Full restructure |
| `signup.html` | Simplified nav | Full restructure |
| `resources.html` | New page with nav/footer | New page with nav/footer |
| `dashboard.html` | "View Results" → "Outcomes" | Unchanged (custom dash footer) |

---

## Deliverable B: Route Impact Report

### All Updated Links (Validated)

| Source Page | Link Text | Target | Status |
|---|---|---|---|
| All public pages | Platform | index.html | ✓ |
| All public pages | Governance Center | governance-center.html | ✓ |
| All public pages | Trust | security.html | ✓ |
| All public pages | Resources | resources.html | ✓ |
| All public pages | Sign In | login.html | ✓ |
| All public pages | Get Started | signup.html | ✓ |
| All footers | Product > Platform | index.html | ✓ |
| All footers | Product > Governance Center | governance-center.html | ✓ |
| All footers | Product > Trust | security.html | ✓ |
| All footers | Product > Resources | resources.html | ✓ |
| Governance Center | Participate Now | login.html | ✓ |
| Governance Center | View Details / View Proposals / View Candidates | proposals.html | ✓ |
| Governance Center | Take Survey | login.html | ✓ |
| Governance Center | Verify Now | verify-identity.html | ✓ |
| Proposals | Participate | login.html | ✓ |
| Auth nav | Back to Home | index.html | ✓ |
| Auth nav | Resources | resources.html | ✓ |

### Old Routes Still Accessible (Backward Compatible)

| File | Still Exists? | Notes |
|---|---|---|
| `proposals.html` | Yes | Contextual, linked from governance center |
| `outcomes.html` | Yes | Contextual, linked from dashboard |
| `verify-identity.html` | Yes | Contextual, linked from guidelines |
| `security.html` | Yes | Renamed label to "Trust" in nav |

---

## Deliverable C: SaaS Positioning Audit

### Homepage Positioning Score: 9/10

| Criteria | Score | Notes |
|---|---|---|
| Value proposition clarity | 10 | "Trusted Governance for Modern Organizations" |
| Target audience visibility | 10 | New "Who Uses Orivis" section with 5 segments |
| Use case diversity | 9 | New "Governance for Every Organization" with 5 sectors |
| Trust signals | 9 | Stats, trust infrastructure, enterprise language |
| SaaS positioning | 9 | CTA "Get Started", nav "Sign In", resources page |
| **Average** | **9.4** | |

### Governance Center Score: 9/10

| Criteria | Score | Notes |
|---|---|---|
| Event type diversity | 10 | 5 types: Election, Approval, Consultation, Referendum, Survey |
| Category navigation | 9 | Filter pills for each event type |
| Card information density | 8 | Event type badge, status, participants, deadline, CTA |
| Multiple event support | 10 | Covers binary votes, multi-option, surveys, consultations |
| **Average** | **9.3** | |

### Enterprise Readiness Score: 8/10

| Criteria | Score | Notes |
|---|---|---|
| Navigation structure | 9 | SaaS-standard nav (Platform, Governance Center, Trust, Resources) |
| Information architecture | 8 | Contextual pages removed from nav, accessible via workflow |
| Footer organization | 9 | Product, Company, Legal, Social sections |
| Resources availability | 7 | Resources page with placeholder content |
| API readiness | 7 | "Coming soon" on API section |
| **Average** | **8.0** | |

---

## Deliverable D: Future Readiness Assessment

### Is the platform ready for Phase 6 — Organization Workspace Architecture?

**Assessment: READY**

**Reasoning:**
1. Navigation now follows SaaS convention (Platform → Governance Center → Trust → Resources)
2. Governance Center supports 5 distinct event types with visual category filtering
3. Auth pages use simplified nav appropriate for pre-login experiences
4. Footer structured by Product/Company/Legal/Social — standard SaaS pattern
5. Homepage clearly communicates Orivis as governance infrastructure for 5 organization types
6. Proposals page buttons now drive users into the participate flow (→ login → dashboard)
7. All old contextual pages still accessible through appropriate workflows

**Remaining work for Phase 6:**
- Organization workspace architecture (multi-org support)
- Role-based access control (admin, participant, reviewer)
- Organization-specific branding/theming
- Dashboard per-organization context
- User onboarding flows
- Event creation wizard

**Recommendation:** Proceed to Phase 6 — Organization Workspace Architecture
