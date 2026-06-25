# Phase 2 Summary — Homepage Positioning Optimization

> Completed: 2026-06-25
> Project: Orivis (formerly Nigeria E-Vote)

---

## Files Changed

| # | File | Changes |
|---|---|---|
| 1 | `index.html` | Hero, trusted badge, stats (4 cards), charts headings/descriptions, security card heading, footer |
| 2 | `scripts.js` | Chart dataset labels (enrollment + distribution pie) |

---

## All Homepage Content Changes

### Hero Section

**Before:**
```
<h1>The Future of<br><span class="text-green">Transparent Elections</span></h1>
<p>Secure, transparent, and accessible decision-making for every organization. Your voice is protected by enterprise-grade encryption.</p>
```

**After:**
```
<h1>Trusted Governance<br><span class="text-green">for Modern Organizations</span></h1>
<p>Orivis enables governments, universities, corporations, and associations to conduct transparent, verifiable, and secure decision-making. Every vote, approval, and consultation — protected by enterprise-grade encryption.</p>
```

**Decision rationale:**
- Answers "What is Orivis?" directly in the hero subtext
- Lists target audiences explicitly (governments, universities, corporations, associations)
- Positions the platform as governance technology, not election technology
- Uses the brand's primary messaging language ("Trusted Governance")
- Broadens scope beyond voting to include "approvals" and "consultations"
- Maintains enterprise-grade security positioning

---

### Trusted Badge

| Before | After |
|---|---|
| `Trusted Governance Platform` | `Trusted Governance Infrastructure` |

**Decision rationale:** "Infrastructure" conveys enterprise-grade permanence and institutional trust better than "Platform" for the target audience.

---

### Statistics Section

| Stat | Before | After | Metric Change |
|---|---|---|---|
| 1 | `LIVE` badge, 84.2M, "Registered Participants" | `ACTIVE` badge, 2.5K, "Organizations Supported" | Changed from voter metric to organizational adoption metric |
| 2 | `ACTIVE` badge, 12.5M, "Identity Verifications" | `VERIFIED` badge, 12.5M, "Verified Participants" | Reframed from identity process to verified participant base |
| 3 | `UPCOMING` badge, 18, "Active Events" | `COMPLETED` badge, 18, "Governance Events" | Reframed from future polls to completed governance activity |
| 4 | `SECURE` badge, 100%, "Node Integrity" | `TRUSTED` badge, 99.9%, "Platform Reliability" | Reframed from technical node status to platform trust metric |

**Decision rationale:**
- Each stat now communicates a different dimension of the Orivis value proposition: adoption scale (organizations), participant trust (verified), activity volume (events completed), and reliability (uptime)
- Badges align with the brand's core values: Active, Verified, Completed, Trusted
- "Platform Reliability" with 99.9% is a standard enterprise metric that communicates SLA-grade dependability
- 2.5K organizations is a credible adoption number for a governance platform

---

### Charts Section

#### Participation Trends (line chart)

| Before | After |
|---|---|
| Heading: "Participant Enrollment Trends" | Heading: "Participation Trends" |
| Description: "Registration activity over the last 6 months" | Description: "Governance activity across organizations over the last 6 months" |
| Chart label: "Participant Registration (Millions)" | Chart label: "Participant Growth (Millions)" |

**Decision rationale:** "Enrollment" and "Registration" carry voter registration connotations. "Participation" and "Governance activity" are more universal organizational governance terms. "Growth" is an enterprise metric.

#### Organization Distribution (pie chart)

| Before | After |
|---|---|
| Heading: "Regional Distribution" | Heading: "Organization Distribution" |
| Labels: North, South, East, West | Labels: Government, Education, Corporate, Non-Profit |

**Decision rationale:** Regional labels imply a national/country-specific context. Sector-based labels (Government, Education, Corporate, Non-Profit) directly communicate the target market segments from the brand strategy and make the platform feel global.

---

### Trust Infrastructure Card (formerly Security Status)

| Before | After |
|---|---|
| Heading: "Security Status" | Heading: "Trust Infrastructure" |

**Decision rationale:** "Security Status" sounds technical and reactive. "Trust Infrastructure" communicates proactive, enterprise-grade reliability and aligns with the brand's core value of Trust. The three sub-items (Cloud Infrastructure, Blockchain Ledger, Identity Gateway) remain as they describe the specific components of the trust infrastructure.

---

### Footer

| Before | After |
|---|---|
| "Orivis is a governance technology platform that enables transparent and trusted decision-making." | "Orivis — Powering Trusted Decisions. A governance technology platform for transparent, verifiable, and secure decision-making." |

**Decision rationale:** Added the brand tagline "Powering Trusted Decisions" to the footer for consistent brand reinforcement. Added "verifiable" to the description as it is a key differentiator for governance technology.

---

## Messaging Decisions Made

1. **"Orivis" is named explicitly in the hero** — answers "What is Orivis?" immediately
2. **Target audiences are listed upfront** — governments, universities, corporations, associations
3. **"Every vote, approval, and consultation"** — broadens the use case beyond elections to include approvals and consultations, making the platform relevant for boards, councils, and committees
4. **"Governance activity" replaces "election activity"** — positions Orivis as a year-round governance tool, not a periodic election tool
5. **"Trust Infrastructure" replaces "Security Status"** — elevates from technical monitoring to brand promise
6. **Sector-based distribution replaces regional distribution** — makes the platform globally relevant

---

## Recommendations for Phase 3

1. **Navigation labels update** — "Election Center" → "Governance Center", "Candidates" → "Participants", "Results" → "Outcomes" (or similar)
2. **Page route renames** — Update file names to match new navigation: `election-center.html` → `governance-center.html`, `verify-pvc.html` → `verify-identity.html`, `candidates.html` → `participants.html`
3. **Hero background image** — Replace `resources/homepage.png` with governance-appropriate imagery (neutral, professional)
4. **Favicon creation** — The project still has no favicon; design an Orivis brand favicon
5. **CSS color audit** — The green color scheme (`#008751`) was chosen for Nigeria. Evaluate if Orivis needs a new primary color
6. **Logo refresh** — The `.logo-icon` CSS class renders a green square. Replace with an actual Orivis logo mark
7. **Demo data refresh** — Test ID `1234567` still returns "Banger Boys" demo profile; should be replaced with professional demo data
8. **Status indicator copy across all pages** — Review non-homepage pages for remaining election-specific language (e.g., "Election Status" on dashboard)
