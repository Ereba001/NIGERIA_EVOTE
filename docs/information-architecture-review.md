# Information Architecture Review

> Role: Senior Product Strategist
> Product: Orivis (Governance Technology Platform)
> Date: 2026-06-25

---

## 1. Current Structure

### Page Inventory

| # | Route | Title | Type | Auth Required |
|---|---|---|---|---|
| 1 | `index.html` | Home \| Orivis | Landing / Marketing | No |
| 2 | `auth.html` | Authentication \| Orivis | Registration (3-step) | No |
| 3 | `login.html` | Login \| Orivis | Login | No |
| 4 | `dashboard.html` | Dashboard \| Orivis | User Dashboard | Yes |
| 5 | `election-center.html` | Election Center \| Orivis | Event Listings | No |
| 6 | `candidates.html` | Candidates \| Orivis | Candidate Profiles | No |
| 7 | `results.html` | Results \| Orivis | Results Display | No |
| 8 | `security.html` | Security \| Orivis | Trust & Security | No |
| 9 | `verify-pvc.html` | Identity Verification \| Orivis | ID Check | No |
| 10 | `receipt.html` | Receipt \| Orivis | Post-action Confirmation | No (data from localStorage) |

### Current Navigation (Public Header)

```
[Orivis Logo]  |  Election Center  |  Verify Identity  |  Candidates  |  Results  |  Security  |  [Sign Up] [Login]
```

### Current Navigation (Authenticated Dashboard)

```
[Orivis Logo]  |  Dashboard  |  View Results  |  Profile  |  [Logout]
```

### Current Footer

```
Resources: Education, Governance Guides, Verification Guide, FAQ
Support: Help Center, Report Issue, Contact Support, Privacy Policy
Social: X, f, in
Legal: © 2026, Terms of Service, Data Protection Policy
```

---

## 2. Problems

### 2.1 Naming Mismatch with Brand Strategy

| Current Name | Brand Strategy Requirement | Gap |
|---|---|---|
| "Election Center" | Governance platform for votes, approvals, consultations | Too narrow. Excludes consultations, approvals, and other governance actions. |
| "Candidates" | Supports proposals, options, nominees, choices | Only covers one use case (candidate elections). Irrelevant for referendums, board resolutions, policy approvals. |
| "Results" | Decision outcomes across all event types | Implies electoral results only. Does not cover consultation findings, approval outcomes. |
| "Verify Identity" | Identity verification for participants | Functional label, but detached from the user journey. Should be part of participant onboarding. |
| "Security" | Trust infrastructure | Accurate but could be elevated to "Trust" to match brand values. |

### 2.2 Page Route / Filename Legacy

| Current File | Originates From | Problem |
|---|---|---|
| `verify-pvc.html` | "Permanent Voter's Card" — Nigeria INEC | Filename is still Nigeria-specific even though the title and content have been rebranded. |
| `election-center.html` | National election hub | "election" in the route contradicts the governance positioning. |

### 2.3 Missing Multi-Tenant Architecture

Orivis targets governments, universities, corporations, NGOs, and associations. The current IA assumes:

- **Single tenant**: One election, one set of candidates, one set of results
- **Single role**: All users are individual voters
- **Single event type**: Only elections (no consultations, approvals, referendums)

Missing pages/concepts:
- Organization onboarding / workspace creation
- Organization switcher
- Admin panel (event creation, participant management, audit logs)
- Event type selector (election, consultation, approval, referendum)
- Custom branding per organization

### 2.4 User Journey Gaps

**Current journey:**
```
Home → Sign Up → Login → View Events → Vote → Receipt
                                                      ↓
                                              View Results
```

**Missing journeys for target customers:**

| Customer | Missing Journey |
|---|---|
| Government | Create public consultation, verify citizen identities, publish outcomes |
| University | Set up student election, manage candidates, certify results |
| Corporation | Configure shareholder vote, set voting thresholds, audit trail |
| NGO | Member registration, policy approval workflow, quorum management |
| Association | Leadership nomination, ballot design, term management |

### 2.5 Content-Layout Tension

Several pages mix marketing content with authenticated functionality:

| Page | Problem |
|---|---|
| `election-center.html` | Public page with a voting modal embedded. Non-authenticated users can trigger a vote flow that redirects to login. This works but confuses the boundary between public browsing and authenticated actions. |
| `candidates.html` | Public page showing candidate cards. Works for elections, but what would this page show for a consultation or approval event? |
| `results.html` | Public results page. For enterprise governance, results are often private to participants. |
| `dashboard.html` | Combines voting, results viewing, and profile management. As Orivis adds more event types, this single dashboard will grow unwieldy. |

### 2.6 No Navigation Hierarchy

The current nav has flat 5 links with no grouping. As the product grows:

- There is no distinction between "browse" and "manage"
- There is no account/settings entry point (except hidden in dashboard profile)
- No organization context
- No indication of active event vs. event library

---

## 3. Recommended Structure

### 3.1 Page Inventory — Target State

| Keep | Rename | Merge | New (Future) |
|---|---|---|---|
| `index.html` (Home) | `election-center.html` → `governance-center.html` | `auth.html` + `verify-pvc.html` → `signup.html` (unified onboarding) | `console.html` (organization dashboard) |
| `login.html` (Login) | `candidates.html` → `participants.html` or `proposals.html` | | `admin-events.html` (event management) |
| `dashboard.html` (Dashboard) | `results.html` → `outcomes.html` | | `admin-participants.html` (participant management) |
| `security.html` (Security/Trust) | `verify-pvc.html` → `verify-identity.html` | | `admin-audit.html` (audit logs) |
| `receipt.html` (Confirmation) | `auth.html` → `signup.html` | | `settings.html` (account & org settings) |
| | `security.html` → `trust.html` (optional) | | `pricing.html` (plans for SaaS) |
| | | | `resources.html` (docs, guides, API) |

### 3.2 Page Descriptions — Target State

| Route | Title | Purpose |
|---|---|---|
| `/` | Home \| Orivis | Marketing landing (unchanged) |
| `/login` | Login \| Orivis | Participant authentication (unchanged) |
| `/signup` | Sign Up \| Orivis | Unified onboarding: identity verification + registration (merge auth + verify-identity) |
| `/dashboard` | Dashboard \| Orivis | Authenticated participant hub (enhanced) |
| `/console` | Console \| Organization Name | Organization admin workspace (new) |
| `/governance-center` | Governance Center \| Orivis | Browse active and past events (renamed) |
| `/proposals` | Proposals \| Orivis | View participants, options, or proposals for an event (renamed) |
| `/outcomes` | Outcomes \| Orivis | Verified results and decisions (renamed) |
| `/trust` | Trust \| Orivis | Security, transparency, verification infrastructure (renamed from security) |
| `/receipt` | Receipt \| Orivis | Post-action confirmation receipt |
| `/settings` | Settings \| Orivis | Account and organization preferences (new) |

---

## 4. Navigation Recommendations

### 4.1 Public Navigation (Unauthenticated)

```
[Orivis Logo]  |  Platform  |  Governance Center  |  Trust  |  Resources  |  [Sign In] [Get Started]
```

| Label | Route | Rationale |
|---|---|---|
| Platform | `/` (with hero anchor) | All-in-one landing for what Orivis is |
| Governance Center | `/governance-center` | Browse active governance events |
| Trust | `/trust` | Security, verification, infrastructure |
| Resources | `/resources` | Documentation, guides, API, whitepapers |
| Sign In | `/login` | Existing participant login |
| Get Started | `/signup` | CTA for new participants and organizations |

**Removed from public nav:**
- "Verify Identity" — moved into the onboarding flow (part of signup)
- "Candidates" — renamed to "Proposals" and becomes event-contextual (shown within an event, not as top-level nav)
- "Results" — renamed to "Outcomes", shown within event context

### 4.2 Authenticated Navigation (Participant)

```
[Orivis Logo] [Organization Switcher ▼]  |  Dashboard  |  Governance Center  |  [Profile ▼]  [Notifications]
```

| Label | Route | Rationale |
|---|---|---|
| Dashboard | `/dashboard` | Personal hub: my events, my votes, my status |
| Governance Center | `/governance-center` | Browse and filter all accessible events |
| Profile dropdown | `/settings` | Account settings, notifications, logout |

### 4.3 Authenticated Navigation (Admin)

```
[Orivis Logo] [Organization Name ▼]  |  Console  |  Events  |  Participants  |  Audit  |  [Settings ▼]
```

| Label | Route | Rationale |
|---|---|---|
| Console | `/console` | Org-level overview dashboard (stats, active events, health) |
| Events | `/admin-events` | Create, manage, close governance events |
| Participants | `/admin-participants` | Manage participant roster, roles, verification status |
| Audit | `/admin-audit` | Immutable audit log, transparency reports |
| Settings | `/settings` | Org profile, branding, security policies, billing |

### 4.4 Footer Navigation

Retain current structure but add:

```
Product: Platform, Governance Center, Trust, Pricing
Resources: Documentation, API Reference, Integration Guides, FAQ
Company: About, Contact, Careers, Press
Legal: Privacy, Terms, Data Processing, Cookie Policy
Social: X, LinkedIn, GitHub, YouTube
```

---

## 5. User Journey Mapping

### 5.1 Government — Public Consultation

```
Home → Governance Center → Select "Public Consultation" → View Proposal → 
Verify Identity → Submit Feedback → Receipt → Monitor Outcomes
```

### 5.2 University — Student Election

```
Home → Sign Up (org: University) → Dashboard → 
Admin: Create Election → Add Candidates → Set Timeline → 
Student: Browse → Verify → Vote → View Live Outcomes
```

### 5.3 Corporation — Board Resolution

```
Home → Sign In → Dashboard → Select "Board Resolution" →
Review Proposal → Cast Decision → Receipt →
Audit Trail Available
```

### 5.4 NGO — Policy Approval

```
Home → Governance Center → Browse "Policy Vote" →
Review Document → Approve/Reject/Abstain →
Receipt → Track Outcome
```

### 5.5 Association — Leadership Vote

```
Home → Sign In → Governance Center → "Annual Elections" →
View Participants → Vote → Receipt →
Attend Virtual AGM → Final Results
```

---

## 6. Pages That Should Remain Unchanged

| Page | Rationale |
|---|---|
| `index.html` | Already optimized in Phase 2. Serves as the public face of Orivis. Only needs navigation link updates to point to renamed pages. |
| `login.html` | Authentication pattern is standard. No fundamental change needed beyond route update. |
| `dashboard.html` | Core authenticated experience. The internal tab structure (Dashboard, View Results, Profile) works but labels and scope should expand in Phase 4 to accommodate multiple event types. |
| `receipt.html` | Post-action confirmation is essential. Content still uses vote-specific language that should be generalized (see Phase 4). |

---

## 7. Pages That Should Be Renamed

| Current File | New File | Priority | Rationale |
|---|---|---|---|
| `election-center.html` | `governance-center.html` | High | "Election" contradicts brand positioning. "Governance Center" covers elections, consultations, approvals, referendums. |
| `verify-pvc.html` | `verify-identity.html` | High | Filename still references "PVC" (Permanent Voter's Card). Content already rebranded; file name must follow. |
| `candidates.html` | `proposals.html` | Medium | "Candidates" only fits elections. "Proposals" covers candidates, policy options, referendum choices, resolution options. |
| `results.html` | `outcomes.html` | Medium | "Results" implies electoral winners/losers. "Outcomes" is neutral and fits all governance event types. |
| `auth.html` | `signup.html` | Medium | "Auth" is developer jargon. "Sign Up" is user-friendly. Should merge with identity verification. |
| `security.html` | `trust.html` | Low | "Security" is functional. "Trust" aligns with brand value. Optional — "Security" is also acceptable for enterprise buyers. |

---

## 8. Pages That Should Be Merged

| Pages to Merge | New Page | Rationale |
|---|---|---|
| `auth.html` + `verify-pvc.html` | `signup.html` | Both handle identity verification and registration. Currently, the flow is: verify PVC → proceed to auth. A single streamlined onboarding page reduces friction. The verify-pvc standalone page can redirect to signup. |

---

## 9. Pages That Are Missing

| Missing Page | Priority | Purpose |
|---|---|---|
| Organization dashboard (`/console`) | High | Admin needs a bird's-eye view of their organization's governance activity. Current dashboard is participant-only. |
| Event management (`/admin/events`) | High | Create, configure, and manage governance events. Each event type (election, consultation, approval, referendum) needs different settings. |
| Participant management (`/admin/participants`) | High | Manage who can participate, their verification status, roles, and eligibility. |
| Audit log (`/admin/audit`) | Medium | Immutable record of all governance actions. Essential for the "verifiable" brand promise. |
| Account settings (`/settings`) | Medium | Profile, security preferences, notification settings, organization preferences. |
| Organization creation (`/onboard`) | Medium | First-run wizard for new organizations to set up their workspace. |
| Notifications | Medium | In-app notification center for event invitations, reminders, outcome alerts. |
| Documentation / Resources (`/resources`) | Low | Knowledge base, integration guides, whitepapers, API docs. |
| Pricing (`/pricing`) | Low | SaaS pricing page for the future commercial product. |

---

## 10. Pages That No Longer Fit the Orivis Vision

None of the existing pages fundamentally need removal. However, some require significant content repositioning:

| Page | Issue | Recommendation |
|---|---|---|
| `receipt.html` | Entirely vote-focused: "Vote Successfully Cast", "Your democratic choice", "Political Party", "Voting Details" | Generalize to "Decision Recorded", "Your participation has been securely recorded", "Option Selected", "Participation Details". The receipt concept is sound; the language needs broadening. |
| `dashboard.html` | "Election Status", "Total Votes Cast", "NOT YET CAST", "Leadership Election" | Generalize status terminology. Replace "Cast Your Vote" with "Your Active Events" or "Pending Decisions". The tab system (Dashboard/Results/Profile) should accommodate multiple event types. |
| `candidates.html` | Page assumes electoral candidates with political parties | For governance events, this page should render differently based on event type: candidates for elections, options for referendums, proposals for approvals, questions for consultations. The card UI is reusable; the data model needs generalization. |

---

## 11. Future SaaS Expansion Opportunities

### 11.1 Multi-Tenant Architecture

```
/organization/:slug
  /dashboard
  /events
  /events/:id
  /participants
  /audit
  /settings
  /billing
```

### 11.2 Event-Type System

Orivis should support these event types out of the box, each with its own specialized UI:

| Event Type | Use Cases | Display Component |
|---|---|---|
| **Election** | Candidate selection, leadership vote | Candidate cards, ranked choice, single transferable vote |
| **Approval** | Board resolution, policy adoption | Yes/No/Abstain, supermajority thresholds |
| **Consultation** | Public feedback, community input | Open response, Likert scale, multiple choice |
| **Referendum** | Constitutional change, major policy | Binary choice, voter information pamphlets |
| **Survey** | Sentiment analysis, pulse check | Question bank, anonymous response |

### 11.3 Verification Tiers

```
Level 1: Email + OTP (low stakes — internal surveys)
Level 2: ID + OTP (medium stakes — member elections)
Level 3: ID + OTP + Biometric (high stakes — government elections)
Level 4: Multi-party cryptographic (sovereign-grade — constitutional referendums)
```

### 11.4 API & Integration Layer

- REST API for event creation, participant management, outcome retrieval
- Webhook notifications for event milestones
- SSO integration (SAML, OAuth, Azure AD, Google Workspace)
- Data export (CSV, JSON, PDF audit reports)

### 11.5 Commercial Models

| Tier | Features | Target |
|---|---|---|
| **Free** | 1 organization, 3 events/year, 100 participants | Small associations, student groups |
| **Professional** | 1 organization, unlimited events, 10K participants, audit logs | Universities, NGOs, mid-size corporations |
| **Enterprise** | Multiple orgs, custom verification, API access, SLA, dedicated support | Governments, large corporations, multinationals |
| **Sovereign** | On-premise deployment, air-gapped, custom security audit | National governments, defense, intelligence |

---

## 12. Implementation Priority

| Phase | Focus | Pages Affected |
|---|---|---|
| **Phase 3.5** (immediate) | Rename page routes + update all internal links | `verify-pvc.html`, `election-center.html` + all 10 files linking to them |
| **Phase 4** | Content generalization across all pages | `receipt.html` (vote-specific language), `dashboard.html` (election status), `candidates.html` (political framing) |
| **Phase 5** | Navigation restructure | All templates (header nav partial) |
| **Phase 6** | Merge auth + verify into unified signup | `auth.html`, `verify-pvc.html` |
| **Phase 7** | Admin console (new pages) | Console, event management, participant management |
| **Phase 8** | Multi-tenant architecture | Organization context throughout |

---

## 13. Summary

| Category | Count |
|---|---|
| Pages to keep unchanged | 3 (index, login, receipt) |
| Pages to rename | 6 (election-center, verify-pvc, candidates, results, auth, security) |
| Pages to merge | 2 (auth + verify-pvc → signup) |
| Pages missing (high priority) | 4 (org console, event management, participant mgmt, settings) |
| Pages missing (medium priority) | 4 (audit log, onboarding, notifications, resources) |
| Pages missing (low priority) | 1 (pricing) |
| Pages to remove | 0 |
