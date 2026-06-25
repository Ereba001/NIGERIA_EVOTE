# Phase 3 — Route & Content Migration Report

**Orivis — Powering Trusted Decisions**

---

## A. Route Migration Report

| Old Route | New Route | Files Updated |
|---|---|---|
| `election-center.html` | `governance-center.html` | `index.html`, `security.html`, `verify-identity.html`, `signup.html`, `governance-center.html`, `proposals.html`, `outcomes.html` |
| `verify-pvc.html` | `verify-identity.html` | `index.html`, `security.html`, `verify-identity.html`, `signup.html`, `governance-center.html`, `proposals.html`, `outcomes.html` |
| `candidates.html` | `proposals.html` | `index.html`, `security.html`, `verify-identity.html`, `signup.html`, `governance-center.html`, `proposals.html`, `outcomes.html` |
| `results.html` | `outcomes.html` | `index.html`, `security.html`, `verify-identity.html`, `signup.html`, `governance-center.html`, `proposals.html`, `outcomes.html` |
| `auth.html` | `signup.html` | `index.html`, `security.html`, `verify-identity.html`, `signup.html`, `governance-center.html`, `proposals.html`, `outcomes.html` |

All 5 old files deleted. All internal href references updated across 10 files.

---

## B. Content Migration Report

### dashboard.html

| Original | Replacement | Location |
|---|---|---|
| Election Status | Governance Status | status-bar |
| Total Votes Cast | Total Decisions Recorded | status-bar |
| Cast Your Vote: Leadership Election 2026 | Participate: Governance Event 2026 | card header |
| 93.4M | 12.5K | registered participants |
| 12.8M | 8.4K | total decisions |
| NOT YET CAST | NOT YET SUBMITTED | voter status |
| Every vote cast on the Orivis platform... | Every decision recorded on the Orivis platform... | verification text |
| Your Vote ID | Your Record ID | verification text |
| double-voting | duplicate entries | verification text |
| Confirm Selection | Confirm Choice | button |
| Submit Vote | Submit Decision | button |
| Candidate A / B / C | Option A / B / C | candidate cards, chart labels, modal, results table |
| Progressive Party (PP) | Option A | party label |
| United Alliance (UA) | Option B | party label |
| National Front (NF) | Option C | party label |
| Leadership Election 2026 | Governance Event 2026 | chart subtitle |
| Total Votes Counted: 12,842,910 | Total Decisions Recorded: 12,842 | chart subtitle |
| Chart data: [5393000, 4880000, 2054000, 515910] | [5393, 4880, 2054, 515] | chart data |
| Votes Cast | Decisions | chart label |
| Top Regions / States Breakdown | Top Regions Breakdown | table header |
| State | Region | table column |
| Lagos / Kano / Rivers / FCT Abuja / Kaduna | Northern / Southern / Eastern / Western / Central Region | table rows |
| Voting Center | Participation Center | profile |
| +234 803****890 | +1 555****890 | profile phone |
| Lagos | Central District | profile region |
| Ikeja | Downtown | profile district |
| Confirm Your Vote | Confirm Your Decision | modal title |
| Leadership Election | Governance Event | modal label |
| your vote is digitally signed | your decision is digitally signed | modal warning |
| Confirm and Submit | Confirm & Submit | modal button |
| Back to Selection | Back to Options | modal button |
| Leave Voting Session? | Leave Session? | logout modal |
| Vote Recorded | Decision Recorded | lock function |
| Select a candidate | Select an option | validation message |
| Vote Cast Successfully! | Decision Recorded! | success modal |
| Your vote has been securely recorded... | Your decision has been securely recorded... | success modal |

### receipt.html

| Original | Replacement | Location |
|---|---|---|
| Vote Successfully Cast | Decision Recorded | H1 |
| Your democratic choice has been securely recorded... | Your decision has been securely recorded... | subtitle |
| Voting Details | Participation Details | section header |
| Selected Candidate | Selected Option | row label |
| Political Party | Selected Option | row label |
| Candidate B | Option B | candidate display |
| This receipt serves as permanent proof of your vote. | This receipt serves as permanent proof of your decision. | notice |
| your vote is publicly verifiable via the national ledger | your decision is publicly verifiable via the ledger | notice |

### proposals.html (formerly candidates.html)

| Original | Replacement | Location |
|---|---|---|
| Page title: Candidates \| Orivis | Proposals \| Orivis | `<title>` |
| H1: Candidates | Proposals | page header |
| Explore the profiles of registered candidates... | Explore the proposals... | subtitle |
| Leadership Election 2026 | Governance Decision 2026 | filter option |
| Regional Election | Regional Decision | filter option |
| Assembly Election | Assembly Vote | filter option |
| Candidate A / B / C | Proposal A / B / C | card names |
| Progressive Party (PP) | Team Alpha | party label |
| United Alliance (UA) | Team Beta | party label |
| National Front (NF) | Team Gamma | party label |
| View Manifesto | View Details | button |

### governance-center.html (formerly election-center.html)

| Original | Replacement | Location |
|---|---|---|
| Page title: Election Center \| Orivis | Governance Center \| Orivis | `<title>` |
| H1: Election Center | Governance Center | page header |
| Nav: Election Center | Governance Center | nav link |
| ...past elections and governance events | ...past governance events | subtitle |
| Leadership Election 2026 | Governance Decision 2026 | event card |
| Eligible Voters: 93.4M | Eligible Participants: 12.5K | event detail |
| Cast your vote for organizational leadership | Participate in organizational decision-making | event description |
| View Candidates | View Proposals | button (x3) |
| Vote Now | Participate Now | button |
| Candidates / candidates | Proposals / proposals | modal + comments |
| Cast Your Vote | Submit Your Decision | modal title |
| Select your preferred candidate for the Leadership Election 2026 | Select your preferred option for the Governance Decision 2026 | modal text |
| Candidate A (PP) / People's Party | Option A / Team Alpha | option labels |
| Candidate B (UA) / Unity Alliance | Option B / Team Beta | option labels |
| Candidate C (NF) / National Front | Option C / Team Gamma | option labels |
| Submit Vote | Submit Decision | modal button |
| Vote Cast Successfully! | Decision Recorded! | success modal |
| Your vote has been securely recorded... | Your decision has been securely recorded... | success modal |
| Regional Election | Regional Decision | event card |
| Eligible Voters: 7.2M | Eligible Participants: 7.2K | event detail |
| Election for regional leadership | Regional decision | event description |
| Assembly Election | Assembly Vote | event card |
| Eligible Voters: 93.4M | Eligible Participants: 12.5K | event detail |
| Representative elections | Representative decisions | event description |
| Everything you need to know before casting your digital vote | Everything you need to know before participating | guidelines |
| Electoral Process | Governance Process | guide card |
| secures your vote, maintains anonymity, and prevents double-voting | secures your decision, maintains anonymity, and prevents duplicate entries | guide card |

### outcomes.html (formerly results.html)

| Original | Replacement | Location |
|---|---|---|
| Page title: Results \| Orivis | Outcomes \| Orivis | `<title>` |
| H1: Live Election Results | Live Governance Outcomes | page header |
| Leadership Election 2026 | Governance Decision 2026 | chart title |
| Total Votes Counted: 12,842,910 | Total Decisions Recorded: 12,842 | chart subtitle |
| Top Regions / States Breakdown | Top Regions Breakdown | table header |
| State | Region | table column |
| Lagos / Kano / Rivers / FCT Abuja / Kaduna | Northern / Southern / Eastern / Western / Central Region | table rows |
| Candidate A / B / C | Option A / B / C | table rows |
| Chart: Candidate A (PP) etc. | Chart: Option A etc. | chart labels |
| Votes Cast | Decisions | chart label |
| Chart data: [5393000, 4880000, 2054000, 515910] | [5393, 4880, 2054, 515] | chart data |

### security.html

| Original | Replacement | Location |
|---|---|---|
| Every vote cast on our platform... | Every decision recorded on our platform... | feature text |
| once a vote is recorded | once a decision is recorded | feature text |
| including election officials or system administrators | including system administrators | feature text |
| Zero-Knowledge Proofs guarantee your vote remains anonymous | Zero-Knowledge Proofs guarantee your decision remains anonymous | feature text |
| We eliminate double voting | We eliminate duplicate entries | feature text |

### index.html (homepage)

| Original | Replacement | Location |
|---|---|---|
| Every vote, approval, and consultation | Every decision, approval, and consultation | hero text |

### signup.html (formerly auth.html)

| Original | Replacement | Location |
|---|---|---|
| Your vote is anonymous and cannot be traced back to you | Your decision is anonymous and cannot be traced back to you | trust badge |
| Every action is logged on the secure national ledger | Every action is logged on the secure governance ledger | trust badge |
| +234 XXX XXX XXXX | +1 XXX XXX XXXX | phone placeholder |

### scripts.js (shared)

| Original | Replacement | Location |
|---|---|---|
| Chart labels: Candidate A, Candidate B, Others | Option A, Option B, Other | liveResultsChart |

---

## C. Validation Report

### Files Modified

| File | Status |
|---|---|
| `index.html` | ✅ Updated (nav, hero text) |
| `dashboard.html` | ✅ Updated (status bar, cards, chart, profile, modal) |
| `login.html` | ✅ No changes needed |
| `security.html` | ✅ Updated (feature text) |
| `receipt.html` | ✅ Updated (headers, labels, notice) |
| `signup.html` (was auth.html) | ✅ Updated (trust badges, phone placeholder) |
| `verify-identity.html` (was verify-pvc.html) | ✅ Updated (nav only, JS vars preserved) |
| `governance-center.html` (was election-center.html) | ✅ Updated (all election content replaced) |
| `proposals.html` (was candidates.html) | ✅ Updated (all candidate content replaced) |
| `outcomes.html` (was results.html) | ✅ Updated (all results content replaced) |
| `scripts.js` | ✅ Updated (chart labels) |

**Total files modified: 10**

### Broken Links

- **Found: 0** — All internal href references validated. All new route files exist.

### Old Files Deleted

| File | Status |
|---|---|
| `auth.html` | ✅ Deleted |
| `candidates.html` | ✅ Deleted |
| `election-center.html` | ✅ Deleted |
| `results.html` | ✅ Deleted |
| `verify-pvc.html` | ✅ Deleted |

### Remaining Legacy References (Intentional)

These references are preserved per the "do not change CSS architecture" and "do not change JavaScript functionality" constraints:

| Location | Reference | Reason |
|---|---|---|
| `dashboard.html` (CSS classes) | `.vote-actions`, `.vote-modal`, `.vote-warning`, `.vote-check`, `.candidate-card`, `.candidates-grid`, `.candidate-photo` | CSS architecture — not to be changed |
| `dashboard.html` (JS/HTML IDs) | `voteModal`, `submitVoteBtn`, `voterStatus`, `confirmSelectionBtn`, `backToSelectionBtn` | JavaScript functionality — IDs referenced by JS |
| `dashboard.html` (JS variables) | `candidateRadios`, `candidateCards`, `lockVoteUI`, `party`, `orivisVoteStatus`, `orivisVoteReceipt` | JavaScript functionality — internal variables |
| `dashboard.html` (JS element IDs) | `dashVoteSpinner`, `dashVoteCheck` | JavaScript functionality — spinner IDs |
| `governance-center.html` (CSS classes) | `.election-grid`, `.election-card`, `.voteModal`, `.voteSubmit`, etc. | CSS architecture — not to be changed |
| `governance-center.html` (JS IDs) | `voteModal`, `voteCancel`, `voteSubmit`, `voteSuccessModal`, `voteSpinner`, `voteCheck` | JavaScript functionality |
| `governance-center.html` (JS) | `voteBtn`, `voteCandidate` radio names, `candidateOptions` | JavaScript functionality |
| `proposals.html` (CSS classes) | `.candidates-list`, `.candidate-card-large`, `.cand-header`, `.cand-photo`, `.cand-name`, `.cand-party`, `.cand-bio` | CSS architecture — inline `<style>` block |
| `verify-identity.html` (JS) | `pvcVinInput`, `pvcCheckBtn`, `pvcBtnText`, `pvcIdentityResult` | JavaScript functionality — element IDs |
| `login.html` (JS) | `portalNin`, `ninValue` | JavaScript functionality — internal variables |
| `index.css` | `.election-card`, `.election-grid`, `.vote-modal__election`, etc. | CSS architecture — not to be changed |
| `scripts.js` (commented out) | `STORAGE_KEY = 'evote-theme'` | Commented-out code block |
| `receipt.html` (JS) | `orivisVoteReceipt` | localStorage key — data persistence |

### Navigation Paths Verified

- Homepage → Governance Center: ✅
- Homepage → Verify Identity: ✅
- Homepage → Proposals: ✅
- Homepage → Outcomes: ✅
- Homepage → Security: ✅
- Homepage → Sign Up: ✅
- Homepage → Login: ✅
- Governance Center → Proposals: ✅
- Governance Center → Verify Identity: ✅
- Governance Center → Login/Sign Up: ✅
- All footer links: ✅
- Login → Dashboard: ✅
- Dashboard → Receipt: ✅
- Sign Up → Login: ✅
- Verify Identity → Sign Up: ✅

### Confirmation

All routes, buttons, redirects, and navigation paths verified and functioning correctly.
