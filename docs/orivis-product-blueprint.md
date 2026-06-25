# Orivis — Product Blueprint

> **Document Type:** Product Blueprint
> **Status:** Draft v1.0
> **Date:** 2026-06-25
> **Audience:** Investors, Project Supervisors, Developers, Designers

---

## 1. Product Overview

### 1.1 Elevator Pitch

Orivis is a governance technology platform that enables organizations — governments, universities, corporations, NGOs, and associations — to conduct transparent, verifiable, and secure decision-making processes. Every vote, approval, consultation, and referendum is cryptographically signed, immutably recorded, and publicly verifiable without compromising participant anonymity.

### 1.2 Mission

To enable organizations to conduct transparent, verifiable, and trusted decision-making processes through secure digital governance tools.

### 1.3 Vision

To become the global standard for trusted digital governance and decision-making.

### 1.4 Brand Promise

Every decision can be trusted.

### 1.5 Core Values

| Value | Description |
|---|---|
| **Transparency** | Every action is traceable and publicly verifiable |
| **Trust** | Cryptographic verification ensures integrity without intermediaries |
| **Accountability** | Immutable audit trails for all governance actions |
| **Neutrality** | Platform-agnostic, organization-owned, politically unaffiliated |
| **Accessibility** | Designed for participants of all technical skill levels |

### 1.6 Current State

The existing codebase is a single-tenant, election-only frontend application originally built for the Nigerian national election system. It contains 10 HTML pages, a global CSS stylesheet, shared JavaScript, and a static Node.js server. The rebrand from "Nigeria E-Vote" to "Orivis" is complete (Phase 1-2). This blueprint defines the target product architecture.

### 1.7 Target State

A multi-tenant, multi-event-type SaaS platform serving any organization that requires trusted governance infrastructure.

---

## 2. Target Customers

### 2.1 Customer Segments

| Segment | Use Cases | Decision Frequency | Scale |
|---|---|---|---|
| **Governments** | Public consultations, referendums, civic participation, parliamentary votes | Quarterly to annually | Millions of participants |
| **Universities** | Student elections, senate voting, faculty leadership selection | Semi-annually | Thousands to tens of thousands |
| **Corporations** | Board resolutions, shareholder voting, internal governance | Monthly to annually | Hundreds to thousands |
| **NGOs** | Member elections, policy approvals, leadership appointments | Annually | Hundreds to thousands |
| **Associations** | Council elections, bylaw changes, award selection | Annually | Hundreds |

### 2.2 Customer Personas

**Government Administrator — Fatima**
- Needs to run a national referendum with 50M+ eligible citizens
- Requires multi-factor identity verification (ID + biometric)
- Must produce auditable results within hours of close
- Concerned about security, fraud prevention, and public trust

**University Student Affairs Director — Dr. Chen**
- Runs annual student union elections across 12 faculties
- Needs campus-specific voter rolls and customizable ballot designs
- Wants real-time turnout monitoring
- Budget-constrained; needs affordable per-election pricing

**Corporate Board Secretary — James**
- Manages quarterly shareholder votes and annual director elections
- Requires share-weighted voting, quorum tracking, and proxy management
- Needs integration with existing shareholder registry
- Compliance reporting is mandatory

**NGO Executive Director — Amara**
- Runs member votes on policy positions and leadership selection
- Needs simple, accessible voting for members in remote areas
- Requires SMS-based verification for members without smartphones
- Budget is tight; needs a free or low-cost tier

**Association President — Miguel**
- Manages annual council elections for a 500-member professional body
- Needs nomination management, candidate statements, and secure ballots
- Wants a simple "set and forget" election workflow
- Values ease of use over advanced features

### 2.3 Market Differentiation

| Orivis | Traditional E-Voting | General Survey Tools |
|---|---|---|
| Multi-event-type (elections, approvals, consultations, referendums, surveys) | Single-purpose (elections only) | Single-purpose (surveys only) |
| Multi-tenant by design | Single-tenant per deployment | Multi-tenant but no governance features |
| Cryptographic audit trail | Varies (often opaque) | No audit trail |
| Identity verification tiers | Usually one-size-fits-all | Email-based only |
| Anonymous but verifiable | Often either anonymous OR verifiable | Usually anonymous |
| Organization-branded experience | Usually platform-branded | White-label at premium tier |

---

## 3. User Roles

### 3.1 Role Hierarchy

```
Super Admin (Orivis Platform)
└── Organization Admin
    └── Event Manager
        ├── Participant
        └── Observer
```

### 3.2 Role Definitions

| Role | Privileges | Targets | Notes |
|---|---|---|---|
| **Super Admin** | Access all organizations, system configuration, billing management, platform-wide audit | Orivis internal team | Can impersonate org admins for support |
| **Organization Admin** | Create/edit/delete events, manage participants, view audit logs, configure org settings, manage billing | Customer organization owner | Full control over their organization workspace |
| **Event Manager** | Configure a single event, manage proposals/options, monitor participation, publish outcomes | Department heads, committee chairs | Scoped to one event at a time |
| **Participant** | View assigned events, verify identity, cast decision, view personal receipt, view outcomes | End users (voters, members, shareholders) | Cannot see who else participated or how they decided |
| **Observer** | View event status, participation metrics (not individual votes), final outcomes | Auditors, media, regulatory bodies | Read-only. May be public or restricted depending on event configuration |

### 3.3 Role Permissions Matrix

| Capability | Super Admin | Org Admin | Event Manager | Participant | Observer |
|---|---|---|---|---|---|
| Create organization | ✓ | — | — | — | — |
| Configure organization | ✓ | ✓ | — | — | — |
| Create event | ✓ | ✓ | ✓ | — | — |
| Configure event | ✓ | ✓ | ✓ | — | — |
| Manage proposals | ✓ | ✓ | ✓ | — | — |
| Manage participants | ✓ | ✓ | limited | — | — |
| Verify identity | — | — | — | ✓ | — |
| Cast decision | — | — | — | ✓ | — |
| View personal receipt | — | — | — | ✓ | — |
| View outcomes | ✓ | ✓ | ✓ | ✓ | ✓ |
| View audit log | ✓ | ✓ | ✓ | — | — |
| View participant list | ✓ | ✓ | ✓ | — | — |
| Export data | ✓ | ✓ | ✓ | — | — |
| Manage billing | ✓ | ✓ | — | — | — |
| Platform-wide settings | ✓ | — | — | — | — |

---

## 4. Event Types

### 4.1 Event Type Matrix

| Type | Use Case | Decision Options | UI Component | Verification Required |
|---|---|---|---|---|
| **Election** | Candidate selection, leadership vote | Multiple candidates, ranked choice, write-in | Candidate cards, ballot | Tier 2+ |
| **Approval** | Board resolution, policy adoption | Yes / No / Abstain, supermajority | Binary decision card | Tier 2+ |
| **Consultation** | Public feedback, community input | Open response, Likert scale, MCQs | Form builder, text input | Tier 1 |
| **Referendum** | Constitutional change, major policy | For / Against, voter information | Binary with information pamphlet | Tier 3+ |
| **Survey** | Sentiment analysis, pulse check | Multiple choice, rating scales | Question bank | Tier 1 (optional) |

### 4.2 Event Lifecycle

```
Draft → Scheduled → Open → Closed → Tallied → Published → Archived
  │         │           │        │         │          │
  │         │      Participants    │    Results     │
  │         │       can vote       │   final and    │
  │    Event is         │           │  verified      │
  │   visible but       │           │                │
  │    not open     ┌───┴───┐       │                │
  │                 │       │       │                │
  ▼                 ▼       ▼       ▼                ▼
```

### 4.3 Event Configuration Per Type

| Setting | Election | Approval | Consultation | Referendum | Survey |
|---|---|---|---|---|---|
| Ballot type | Single choice, ranked, STV | Yes/No/Abstain | Free text, Likert, MCQ | For/Against | MCQ, rating, text |
| Anonymous | ✓ | ✓ | optional | ✓ | optional |
| Verifiable receipts | ✓ | ✓ | — | ✓ | — |
| Quorum requirement | ✓ | ✓ | — | ✓ | — |
| Supermajority threshold | — | ✓ | — | ✓ | — |
| Proxy voting | optional | ✓ | — | — | — |
| Write-in candidates | ✓ | — | — | — | — |
| Voter information | Candidate profiles | Resolution text | Context document | Pamphlet | — |
| Results visibility | Public / Restricted | Public / Restricted | Public / Restricted | Public / Restricted | Restricted |
| Audit log | Full | Full | Full | Full | Basic |

---

## 5. Core Modules

### 5.1 Module Map

```
┌─────────────────────────────────────────────────────────────┐
│                        PUBLIC LAYER                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │  Home    │  │Governance│  │  Trust   │  │Resources │    │
│  │ (Landing)│  │  Center  │  │(Security)│  │  (Docs)  │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
├─────────────────────────────────────────────────────────────┤
│                     AUTHENTICATION LAYER                     │
│  ┌──────────┐  ┌──────────┐  ┌────────────────────────┐    │
│  │  Login   │  │  Sign Up │  │  Identity Verification │    │
│  │          │  │ (Merge)  │  │  (Tiers 1-4)           │    │
│  └──────────┘  └──────────┘  └────────────────────────┘    │
├─────────────────────────────────────────────────────────────┤
│                    PARTICIPANT LAYER                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │Dashboard │  │  Events  │  │ Outcomes │  │  Profile │    │
│  │ (My Hub) │  │ (Active) │  │ (Results)│  │(Settings)│    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
├─────────────────────────────────────────────────────────────┤
│                      ADMIN LAYER                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ Console  │  │  Events  │  │Particip. │  │  Audit   │    │
│  │   (Org)  │  │ (Manage) │  │ (Manage) │  │  (Logs)  │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
├─────────────────────────────────────────────────────────────┤
│                      INFRASTRUCTURE LAYER                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │   Auth   │  │   API    │  │ Block-   │  │  Audit   │    │
│  │  Service │  │  Gateway │  │ chain    │  │  Store   │    │
│  │          │  │          │  │ Ledger   │  │          │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 Module Specification

#### 5.2.1 Authentication

| Feature | Description | Current | Target |
|---|---|---|---|
| Sign Up | Multi-step identity verification | `auth.html` (standalone) | Unified `signup.html` |
| Login | Participant authentication | `login.html` | `login.html` (enhanced) |
| OTP | One-time password verification | SMS-based | SMS + Email + TOTP app |
| SSO | Single sign-on | Not supported | SAML, OAuth, Azure AD, Google |
| Session Management | Token-based session | localStorage simulation | JWT with refresh tokens |
| MFA | Multi-factor authentication | Not supported | TOTP, SMS backup, hardware key |

#### 5.2.2 Identity Verification

| Tier | Method | Use Case | Status |
|---|---|---|---|
| 1 | Email + OTP | Surveys, low-stakes consultations | New |
| 2 | ID + Phone + OTP | Elections, approvals | Refactor of current flow |
| 3 | ID + OTP + Biometric | Government elections, high-stakes referendums | New |
| 4 | Multi-party cryptographic | Sovereign-grade constitutional events | New |

#### 5.2.3 Governance Center

| Feature | Description | Current | Target |
|---|---|---|---|
| Event listing | Browse active, upcoming, past events | `election-center.html` | `governance-center.html` |
| Event filtering | Filter by type, date, status, organization | Dropdown only | Rich filter panel |
| Event detail | View event info, proposals, timeline | Inline card | Dedicated event detail page |
| Event types | Election, approval, consultation, referendum, survey | Elections only | All 5 types |
| Multi-tenant | Per-organization event views | Single tenant | Organization-scoped |

#### 5.2.4 Participants (Proposals)

| Feature | Description | Current | Target |
|---|---|---|---|
| View proposals | Browse candidates/options/resolutions | `candidates.html` | Dynamic per event type |
| Proposal profiles | Candidate bio, party, manifesto | Static cards | Rich profiles with media |
| Event-contextual rendering | Different UI per event type | Election only | Election: candidates; Approval: resolution text; Consultation: questions |
| Search and filter | Find proposals by name, party, position | Not supported | Full-text search + category filter |

#### 5.2.5 Outcomes (Results)

| Feature | Description | Current | Target |
|---|---|---|---|
| Result display | Bar chart + state breakdown | `results.html` | Dynamic per event type |
| Live results | Real-time tallies during voting | Implemented via Chart.js | Real-time via WebSocket |
| Result verification | Cryptographic verification | Receipt-based | Public verification portal |
| Export | Download results | Not supported | PDF, CSV, JSON |
| Privacy control | Public vs. restricted | Public only | Configurable per event |

#### 5.2.6 Trust (Security)

| Feature | Description | Current | Target |
|---|---|---|---|
| Security information | Platform security features | `security.html` | `trust.html` (expanded) |
| Infrastructure status | Cloud, blockchain, identity gateway | Static indicators | Live status dashboard |
| Audit certifications | Security audit reports | Static | Downloadable reports |
| Verification portal | Public vote/receipt verification | Not supported | Dedicated verification tool |

#### 5.2.7 Audit Logs

| Feature | Description | Priority |
|---|---|---|
| Event audit trail | All actions on an event (create, modify, close) | High |
| Participant audit | Who verified, when, and at what level | High |
| Vote audit (aggregate) | Total votes, timing, verification counts | High |
| Vote audit (individual) | Per-vote cryptographic receipt | High |
| System audit | Platform-level admin actions | Medium |
| Export | Full audit log export in JSON/CSV | Medium |

---

## 6. Future Modules

### 6.1 Organization Management

| Feature | Description | Priority |
|---|---|---|
| Multi-tenant workspaces | Each organization gets an isolated workspace | P0 |
| Organization onboarding | Guided setup wizard for new orgs | P0 |
| Organization switcher | Switch between orgs (for consultants, admins of multiple orgs) | P1 |
| Custom branding | Org logo, colors, domain (white-label) | P1 |
| Team management | Invite team members with role assignment | P1 |
| Activity log | Per-org activity timeline | P2 |

### 6.2 Billing

| Feature | Description | Priority |
|---|---|---|
| Subscription tiers | Free, Professional, Enterprise, Sovereign | P1 |
| Usage-based billing | Per-event, per-participant pricing | P1 |
| Invoice generation | Automated monthly invoicing | P2 |
| Payment processing | Credit card, wire transfer, ACH | P2 |
| Tax handling | VAT, GST, sales tax per region | P3 |

### 6.3 Notifications

| Feature | Description | Priority |
|---|---|---|
| Email notifications | Event invitations, reminders, confirmations | P0 |
| SMS notifications | OTP delivery, urgent reminders | P1 |
| In-app notifications | Notification center within dashboard | P1 |
| Push notifications | Mobile app notifications | P2 |
| Webhook delivery | Programmatic notification for integrations | P2 |
| Notification preferences | Per-user notification settings | P1 |

### 6.4 API Access

| Feature | Description | Priority |
|---|---|---|
| REST API | Full CRUD for events, participants, outcomes | P1 |
| API keys | Per-organization API key management | P1 |
| Rate limiting | Fair usage enforcement | P1 |
| Webhooks | Event-driven callbacks for integrations | P2 |
| SDKs | JavaScript, Python, .NET client libraries | P2 |
| API documentation | OpenAPI/Swagger specification | P1 |

### 6.5 Integrations

| Integration | Description | Priority |
|---|---|---|
| SSO providers | Azure AD, Google Workspace, Okta, OneLogin | P1 |
| Identity providers | National ID systems, university directories, corporate LDAP | P1 |
| HR systems | Workday, BambooHR for employee eligibility | P2 |
| CRM | Salesforce, HubSpot for member management | P2 |
| Analytics | Google Analytics, Mixpanel, Amplitude | P2 |
| Data export | S3, BigQuery, Snowflake | P3 |

---

## 7. Navigation Architecture

### 7.1 Navigation by User State

```
UNAUTHENTICATED
┌──────────────────────────────────────────────────────────┐
│ [Orivis Logo]  Platform │ Governance Center │ Trust │    │
│ Resources │ [Sign In] [Get Started]                      │
└──────────────────────────────────────────────────────────┘

AUTHENTICATED (PARTICIPANT)
┌──────────────────────────────────────────────────────────┐
│ [Orivis Logo] [Org ▼]  Dashboard │ Governance Center │   │
│ [🔔] [👤 Profile ▼]                                      │
└──────────────────────────────────────────────────────────┘

AUTHENTICATED (ADMIN)
┌──────────────────────────────────────────────────────────┐
│ [Orivis Logo] [Organization Name ▼]                      │
│ Console │ Events │ Participants │ Audit │ [⚙️ Settings ▼] │
└──────────────────────────────────────────────────────────┘
```

### 7.2 Navigation Route Map

| Label | Route | Access | Notes |
|---|---|---|---|
| Platform (Home) | `/` | Public | Marketing landing |
| Governance Center | `/governance-center` | Public + Auth | Browse events |
| Trust | `/trust` | Public | Security & verification |
| Resources | `/resources` | Public | Documentation |
| Sign In | `/login` | Public | Authentication |
| Get Started | `/signup` | Public | Registration |
| Dashboard | `/dashboard` | Auth (Participant) | Personal hub |
| Outcomes | `/outcomes` | Public or Auth | Per event |
| Receipt | `/receipt` | Auth | Post-action confirmation |
| Console | `/console` | Auth (Admin) | Org overview |
| Admin Events | `/admin/events` | Auth (Admin) | Event management |
| Admin Participants | `/admin/participants` | Auth (Admin) | Participant management |
| Admin Audit | `/admin/audit` | Auth (Admin) | Audit logs |
| Settings | `/settings` | Auth | Account & org settings |

### 7.3 Footer Architecture

```
┌──────────────────────────────────────────────────────────┐
│ PRODUCT                        │ COMPANY                 │
│ Platform                       │ About                   │
│ Governance Center              │ Contact                 │
│ Trust                          │ Careers                 │
│ Pricing                        │ Press Kit               │
│                                │                         │
│ RESOURCES                      │ LEGAL                   │
│ Documentation                  │ Privacy Policy          │
│ API Reference                  │ Terms of Service        │
│ Integration Guides             │ Data Processing         │
│ FAQ                            │ Cookie Policy           │
│                                │                         │
│              SOCIAL: X │ LinkedIn │ GitHub │ YouTube      │
│              © 2026 Orivis. All rights reserved.         │
└──────────────────────────────────────────────────────────┘
```

---

## 8. Dashboard Architecture

### 8.1 Participant Dashboard

```
┌──────────────────────────────────────────────────────────┐
│ Orivis Dashboard                                         │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ Welcome back, [Name]                       [Org Name]│ │
│ │                                                      │ │
│ │ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                │ │
│ │ │Active│ │Pending│ │Completed│ │Verified│           │ │
│ │ │ 3    │ │ 2    │ │ 12     │ │ Yes    │           │ │
│ │ └──────┘ └──────┘ └──────┘ └──────┘                │ │
│ └──────────────────────────────────────────────────────┘ │
│                                                          │
│ Active Events                    [View All →]            │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ Leadership Election 2026           ⏰ 2d 14h left    │ │
│ │ ████████████████░░░░░░░░  65% turnout               │ │
│ │ [Review Candidates] [Cast Vote]                     │ │
│ ├──────────────────────────────────────────────────────┤ │
│ │ Board Resolution Q3                  ⏰ 7d left      │ │
│ │ ██████░░░░░░░░░░░░░░░░  30% turnout                 │ │
│ │ [Review Resolution] [Cast Decision]                 │ │
│ └──────────────────────────────────────────────────────┘ │
│                                                          │
│ Recent Outcomes                                          │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ Student Council Election — Results Published 2h ago  │ │
│ │ Policy Vote #42 — Passed (78% approval) 1d ago       │ │
│ └──────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

### 8.2 Dashboard Components

| Widget | Description | Data Source |
|---|---|---|
| Welcome header | User name, org name, quick status | User profile, org context |
| Summary cards | Active events, pending decisions, completed, verification status | Events service |
| Active events list | Events requiring action with progress bars | Events service |
| Recent outcomes | Recently published event results | Outcomes service |
| Quick actions | "Cast Vote", "View Profile", "Settings" | Navigation |
| Notifications | Recent alerts, invitations | Notifications service |

### 8.3 Dashboard States

| State | Display |
|---|---|
| **Empty** (new user, no events) | Hero illustration + "You have no active events. Join an organization to get started." + CTA to browse Governance Center |
| **Active** (has pending events) | Full dashboard with active events, progress, and CTAs |
| **All completed** (voted on everything) | Summary view + "All decisions cast. Check back for new events or view past outcomes." |
| **Error** (service disruption) | Status message + retry button |

---

## 9. Admin Console Architecture

### 9.1 Console Layout

```
┌──────────────────────────────────────────────────────────┐
│ Console — [Organization Name]                            │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 🔴 Active Events: 3    📊 Avg Turnout: 58%          │ │
│ │ ✅ Completed: 18       🎯 Avg Approval: 72%         │ │
│ │ 👥 Participants: 2,450 🔐 Verified: 94%             │ │
│ └──────────────────────────────────────────────────────┘ │
│                                                          │
│ Quick Actions                    [Create Event +]        │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│ │  Create  │ │  Manage  │ │  Export  │ │  View   │    │
│ │ Election │ │Participants│ │  Audit  │ │ Reports │    │
│ └──────────┘ └──────────┘ └──────────┘ └──────────┘    │
│                                                          │
│ Recent Activity                                          │
│ ┌──────────────────────────────────────────────────────┐ │
│ │ 🟢 Oct 25 — Leadership Election closed — 12,842 votes│ │
│ │ 🟡 Oct 24 — 450 new participants verified            │ │
│ │ 🟢 Oct 20 — Board Resolution #47 passed              │ │
│ └──────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

### 9.2 Admin Sub-Pages

| Page | Route | Purpose |
|---|---|---|
| Console Overview | `/console` | Org-level KPIs, recent activity, quick actions |
| Event List | `/admin/events` | All events with status, dates, turnout |
| Event Create | `/admin/events/new` | Multi-step event creation wizard |
| Event Edit | `/admin/events/:id` | Event configuration, timeline, proposals |
| Participant List | `/admin/participants` | Participant roster with verification status |
| Participant Import | `/admin/participants/import` | CSV/API bulk import |
| Participant Detail | `/admin/participants/:id` | Individual participant record |
| Audit Log | `/admin/audit` | Immutable activity log with filters |
| Org Settings | `/settings/organization` | Org profile, branding, security policies |
| Billing | `/settings/billing` | Plan, invoices, payment method |
| Team | `/settings/team` | Team member management and roles |

### 9.3 Event Creation Wizard

```
Step 1: Event Type     →  [Election] [Approval] [Consultation] [Referendum] [Survey]
Step 2: Configuration  →  Title, description, dates, verification tier, quorum, thresholds
Step 3: Proposals      →  Add candidates (election), resolution text (approval), questions (consultation)
Step 4: Participants   →  Define eligibility (all, specific list, CSV upload, API sync)
Step 5: Review         →  Summary + test vote + publish
```

---

## 10. SaaS Roadmap

### 10.1 Phase Overview

```
Phase 1-2 ✅  Rebrand (Complete)
Phase 3.5    🔄  Route Renaming (Current)
Phase 4      📋  Content Generalization
Phase 5      📋  Navigation Restructure
Phase 6      📋  Unified Signup
Phase 7      📋  Admin Console (MVP)
Phase 8      📋  Multi-Tenant Architecture
Phase 9      📋  Event Type Expansion
Phase 10     📋  API & Integrations
Phase 11     📋  Billing & Commercial Launch
```

### 10.2 Detailed Roadmap

| Phase | Timeline | Focus | Deliverables |
|---|---|---|---|
| **1-2** | Complete | Global rebrand + homepage optimization | Brand replacement, hero rewrite, stat modernization |
| **3.5** | Week 1 | Route renaming | Rename `verify-pvc.html` → `verify-identity.html`, `election-center.html` → `governance-center.html`. Update all internal links across 10 files. |
| **4** | Week 2 | Content generalization | Generalize `receipt.html` (remove "Vote Successfully Cast", "Political Party", "Your democratic choice"). Generalize `dashboard.html` status labels. Generalize `candidates.html` to support multiple event types. |
| **5** | Week 3 | Navigation restructure | Implement new header nav per user role (public, participant, admin). Add profile dropdown, org switcher. |
| **6** | Week 4 | Unified signup | Merge `auth.html` + `verify-pvc.html` → `signup.html`. Streamlined onboarding flow. |
| **7** | Month 2 | Admin console | Build org console (`console.html`), event management (`admin/events.html`), participant management (`admin/participants.html`). |
| **8** | Month 3 | Multi-tenant architecture | Backend: org-scoped data models, routing, authentication. Frontend: org context, switcher, isolated data. |
| **9** | Month 4 | Event type expansion | Approval, consultation, referendum, survey UI components. Dynamic event rendering. |
| **10** | Month 5 | API & integrations | REST API, webhooks, SSO, identity provider integrations, SDKs. |
| **11** | Month 6 | Commercial launch | Billing system, tiered pricing, public pricing page, marketing site. |

---

## 11. MVP Scope

### 11.1 MVP Definition

The MVP targets a single-organization deployment with one event type (elections) and the core participant flow. It is the minimum viable version of Orivis that can be demonstrated to investors and used by early adopter organizations.

### 11.2 MVP Pages (Refactored from Existing)

| Route | Title | Source | Changes Required |
|---|---|---|---|
| `/` | Home \| Orivis | `index.html` | Minimal (Phase 2 complete) |
| `/login` | Login \| Orivis | `login.html` | Route update only |
| `/signup` | Sign Up \| Orivis | `auth.html` (renamed) | Route update, merge verify flow |
| `/dashboard` | Dashboard \| Orivis | `dashboard.html` | Generalize status labels |
| `/governance-center` | Governance Center \| Orivis | `election-center.html` (renamed) | Rename route + update links |
| `/proposals` | Proposals \| Orivis | `candidates.html` (renamed) | Rename route + generalize content |
| `/outcomes` | Outcomes \| Orivis | `results.html` (renamed) | Rename route |
| `/trust` | Trust \| Orivis | `security.html` (renamed) | Rename route |
| `/receipt` | Receipt \| Orivis | `receipt.html` | Generalize vote-specific content |
| `/settings` | Settings \| Orivis | New | Profile, notifications, logout |

### 11.3 MVP Features

| Category | Feature | Priority |
|---|---|---|
| **Authentication** | Email/ID + OTP signup | P0 |
| **Authentication** | Participant login | P0 |
| **Authentication** | Session management (JWT) | P0 |
| **Events** | Browse active events | P0 |
| **Events** | View event details + timeline | P0 |
| **Decision** | Cast vote/approval (single choice) | P0 |
| **Decision** | Confirmation receipt | P0 |
| **Results** | View outcomes (bar chart + breakdown) | P0 |
| **Results** | Cryptographic receipt verification | P0 |
| **Identity** | ID + phone verification | P0 |
| **Identity** | OTP delivery (SMS) | P0 |
| **Admin** | Basic org console (overview stats) | P1 |
| **Admin** | Create election event | P1 |
| **Admin** | Add candidates/manual | P1 |
| **Admin** | View participant list | P1 |
| **Admin** | Publish results | P1 |

### 11.4 MVP Exclusions (Post-MVP)

| Feature | Rationale |
|---|---|
| Multi-tenant architecture | Org scoping adds complexity. MVP is single-org. |
| Event types beyond elections | Approval, consultation, referendum, survey are Phase 9 |
| SSO / identity provider integration | Engineering effort high; OTP is sufficient for early adopters |
| API access | Developer audience is post-MVP |
| Billing | MVP is free for early adopters |
| Mobile app | Responsive web app is sufficient |
| Advanced ballot types (ranked, STV) | Single choice only for MVP |
| White-label / custom branding | Fixed Orivis branding for MVP |

### 11.5 MVP Architecture Decision Records

| Decision | Choice | Rationale |
|---|---|---|
| **Framework** | Vanilla HTML/CSS/JS → Next.js or React | Current codebase is static. Requires framework migration for dynamic features. |
| **Backend** | New Node.js/Express or Python/FastAPI | Existing `server.js` is a static file server. Needs API layer. |
| **Database** | PostgreSQL | Relational model for orgs, events, participants, votes. Audit-friendly. |
| **Auth** | JWT + bcrypt | Stateless, scalable. No session store required. |
| **Hosting** | Vercel (frontend) + Railway/Render (backend) | Aligns with current Vercel deployment. |
| **CSS approach** | Tailwind CSS or CSS Modules | Current monolithic CSS is 58KB. Component-based approach needed for maintainability. |

---

## 12. Post-MVP Scope

### 12.1 Near-Term (Months 3-6)

| Feature | Value |
|---|---|
| Multi-tenant org workspaces | Enables B2B sales to multiple organizations |
| Approval event type | Opens corporate board resolution market |
| Consultation event type | Opens government public consultation market |
| Referendum event type | Opens high-stakes government market |
| Survey event type | Low-friction entry point for new customers |
| Admin event creation wizard | Reduces time-to-first-event for org admins |
| Participant CSV import | Makes onboarding large orgs practical |
| Audit log UI | Fulfills the "verifiable" brand promise |
| Email notifications | Improves participant engagement and completion rates |

### 12.2 Mid-Term (Months 6-12)

| Feature | Value |
|---|---|
| REST API | Enables custom integrations and platform play |
| SSO / identity provider integration | Required for enterprise procurement |
| White-label / custom domain | Enables reseller and enterprise channels |
| Billing system | Revenue generation |
| Mobile responsive enhancement | Improves accessibility in emerging markets |
| Advanced ballot types (ranked, STV) | Differentiator vs. competitors |
| Proxy voting | Required for corporate shareholder votes |
| Quorum management | Required for associations and boards |

### 12.3 Long-Term (Year 2+)

| Feature | Value |
|---|---|
| Mobile native apps | Higher engagement, biometric auth |
| Offline voting capability | Critical for emerging markets with unreliable connectivity |
| AI-powered anomaly detection | Fraud detection, unusual voting pattern alerts |
| Multi-language support | Required for international markets |
| On-premise deployment option | Required for sovereign government customers |
| Marketplace / plugin system | Platform ecosystem play |
| Integration marketplace | Salesforce, Workday, Slack, Teams connectors |
| Decentralized identity (DID) | Future-proofing for self-sovereign identity standards |

---

## Appendix A: Current vs. Target Architecture

| Dimension | Current | Target (MVP) | Target (Post-MVP) |
|---|---|---|---|
| **Tenancy** | Single-tenant | Single-tenant with org concept | Multi-tenant |
| **Event types** | Elections only | Elections | 5 event types |
| **User roles** | 1 (voter) | 3 (participant, event manager, org admin) | 5 roles |
| **Pages** | 10 | 11 (refactored) | 20+ |
| **Framework** | Static HTML/CSS/JS | React/Next.js | Same |
| **Backend** | None (static server) | Node.js + PostgreSQL | Same + message queue |
| **Identity** | Hardcoded test flow | OTP + verification tiers | SSO + biometric |
| **API** | None | Internal REST API | Public REST API + SDKs |
| **Deployment** | Vercel (static) | Vercel + cloud backend | Multi-region, on-prem option |

---

## Appendix B: Glossary

| Term | Definition |
|---|---|
| **Orivis** | Governance technology platform (brand name) |
| **Governance Event** | Any structured decision-making process (election, approval, consultation, referendum, survey) |
| **Participant** | An individual authorized to participate in a governance event |
| **Proposal** | An option presented to participants (candidate, resolution, question, choice) |
| **Outcome** | The verified result of a governance event |
| **Receipt** | Cryptographic proof of participation, verifiable without revealing decision |
| **Verification Tier** | Level of identity assurance required for an event (1-4) |
| **Trust Infrastructure** | The combined security, blockchain, and identity systems underpinning Orivis |
| **Organization** | A customer entity (government, university, corporation, NGO, association) |
| **Console** | Administrative dashboard for managing an organization's Orivis workspace |
| **Audit Log** | Immutable, timestamped record of all governance actions |
| **Single Transferable Vote (STV)** | Ranked-choice voting system for multi-seat elections |
| **Quorum** | Minimum number of participants required for a valid decision |
| **Supermajority** | Threshold higher than simple majority (e.g., 2/3, 75%) |

---

*This blueprint is a living document. It should be reviewed and updated as the product evolves through each implementation phase.*
