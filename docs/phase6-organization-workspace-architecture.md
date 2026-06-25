# Phase 6 — Organization Workspace Architecture Report

**Project:** Orivis — Powering Trusted Decisions  
**Date:** 2026-06-25  
**Scope:** Organization workspace, admin console, participant management, event lifecycle, audit trail

---

## Deliverable A: Organization Architecture Report

### Core Entities

| Entity | Description | Owned By |
|---|---|---|
| **Organization** | A tenant (government, university, corporation, association, NGO) | Self |
| **User** | A person with login credentials | Organization |
| **Membership** | Links a User to an Organization with a Role | Organization + User |
| **GovernanceEvent** | An election, approval, consultation, referendum, or survey | Organization |
| **Proposal** | An option within a GovernanceEvent (candidate, policy, question) | GovernanceEvent |
| **Decision** | A participant's submission (vote, response, selection) | Participant + GovernanceEvent |
| **Outcome** | The published result of a GovernanceEvent | GovernanceEvent |
| **AuditEntry** | An immutable log record of any governance action | Organization |
| **Notification** | An alert sent to participants (future) | Organization |
| **Verification** | Identity verification record for a participant | Organization |

### Ownership Model

```
Organization
├── Participants (Users with Memberships)
│   ├── Roles: Owner, Administrator, Moderator, Participant
│   └── Statuses: Verified, Pending, Suspended, Inactive
├── GovernanceEvents
│   ├── Lifecycle: Draft → Review → Published → Active → Closed → Outcome Published → Archived
│   └── Types: Election, Approval, Consultation, Referendum, Survey
├── Proposals (belong to Events)
├── Decisions (belong to Participants + Events)
├── Outcomes (belong to Events)
└── AuditEntries (immutable, belong to Organization)
```

### Relationships

- Organization **has_many** Memberships
- Membership **belongs_to** Organization, **belongs_to** User (through email/ID)
- Membership **has_one** Role
- Organization **has_many** GovernanceEvents
- GovernanceEvent **has_many** Proposals
- GovernanceEvent **has_many** Decisions
- GovernanceEvent **has_one** Outcome
- Organization **has_many** AuditEntries
- User **has_many** Memberships (future: multi-tenant)
- Participant (via Membership) **has_many** Decisions (one per event)

---

## Deliverable B: Workspace Navigation Report

### Participant Navigation (dashboard.html)

```
Orivis Logo  [Organization ▼]  Dashboard | Governance Center | Outcomes | Profile  [Settings] [Logout]
```

- Org switcher dropdown (UI only, no backend)
- Internal toggle tabs: Dashboard, Outcomes, Profile (JS-driven same-page views)
- Governance Center links to external page
- Settings links to settings.html
- "Switch to Admin" link in user ID area → console.html

### Administrator Navigation (console.html + admin pages)

```
Orivis Logo  [Organization ▼]  Console | Events | Participants | Audit  [Admin User | Org Admin] [Settings] [Sign Out]
```

- Console → console.html (workspace dashboard)
- Events → admin-events.html (event CRUD with lifecycle)
- Participants → admin-participants.html (participant management)
- Audit → admin-audit.html (immutable audit trail)
- Settings → settings.html (organization settings)
- Sign Out → index.html

### Public Navigation (unauthenticated)

```
Orivis Logo  Platform | Governance Center | Trust | Resources  [Sign In] [Get Started]
```

Unchanged from Phase 5.

---

## Deliverable C: New Page Inventory

| Route | File | Purpose | Future Functionality |
|---|---|---|---|
| /console | `console.html` | Workspace dashboard with governance health, recent activity, upcoming deadlines | Real-time stats, multi-org dashboard, widgets |
| /admin/events | `admin-events.html` | Event lifecycle management with create/edit/publish/archive | Actual CRUD, event templates, workflow automation |
| /admin/participants | `admin-participants.html` | Participant management with invite/verify/remove/role assignment | Bulk invite, SSO, role-based access control |
| /admin/audit | `admin-audit.html` | Immutable audit trail of all governance activity | Search, filters, export, real-time streaming |
| /settings | `settings.html` | Organization profile, branding, security, notifications | Actual save functionality, custom domain, SSO config |

### Page Details

**console.html** (Organization Workspace Dashboard)
- Governance Health: 4 stat cards (Active Events, Participation Rate, Verified Participants, Pending Decisions)
- Recent Activity: Timeline feed with 5 entries
- Upcoming Deadlines: 3 upcoming event dates
- Admin nav with org switcher

**admin-events.html** (Event Management)
- 5 event cards with lifecycle bar (Draft → Review → Published → Active → Closed → Archived)
- Status badges per event (Draft, Review, Published, Active)
- Contextual action buttons (Edit, Publish, Archive, View Results)
- Create Event button (placeholder)

**admin-participants.html** (Participant Management)
- 3 stat cards (Total, Verified, Pending)
- Full participant table with 6 sample rows
- Status badges (Verified, Pending, Suspended)
- Role column, Action buttons
- Invite button (placeholder)

**admin-audit.html** (Audit Trail)
- 9 audit entries in vertical timeline
- Color-coded icons by action type (green: verification/decision, blue: events, purple: outcomes)
- Timestamps, action names, descriptions

**settings.html** (Organization Settings)
- 4 config cards: Organization Profile, Branding, Security, Notifications
- All fields display-only with "Coming soon" badges
- Readonly inputs, disabled toggles, color swatch

---

## Deliverable D: Multi-Tenant Readiness Assessment

### Is Orivis ready for Phase 7 — SaaS Data Architecture?

**Assessment: READY**

**Reasoning:**

1. **Organization model is scaffolded** — All new pages reference organizations via the switcher dropdown
2. **Workspace roles are defined** — Owner, Administrator, Moderator, Participant with clear separation
3. **Event lifecycle is implemented** — All 7 stages (Draft → Review → Published → Active → Closed → Outcome Published → Archived) are visually represented
4. **Audit trail exists** — Immutable audit entries demonstrate transparency expectations
5. **Admin/participant separation** — Dashboard.html serves participants, console.html serves administrators, with "Switch to Admin" bridge
6. **5 event types supported** — Election, Approval, Consultation, Referendum, Survey on the governance center
7. **Entity relationships documented** — All future database relationships defined

### Remaining for Phase 7

| Item | Status |
|---|---|
| Actual backend database | Not started |
| Authentication & sessions | Not started |
| Multi-tenant data isolation | Not started |
| Real RBAC enforcement | Not started |
| API endpoints | Not started |
| Billing/subscriptions | Deferred to later phase |
| User registration flow | Placeholder only |

**Recommendation:** Proceed to Phase 7 — SaaS Data Architecture (backend: database schema, API layer, authentication).
