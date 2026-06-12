# Serve Frontend Locally

## Goal
Start a local HTTP server to preview the Nigeria E-Vote frontend.

## Tools / Scripts
- `node server.js` (root of project)

## How to run
```bash
node server.js
```
Opens at `http://localhost:3000`.

If `server.js` doesn't exist, use Node's built-in http module or Python's http.server.

## File structure
All pages are flat HTML files in the project root:
- `index.html` — landing page
- `auth.html` — registration
- `login.html` — sign in
- `dashboard.html` — voter dashboard
- `election-center.html` — election listings
- `candidates.html` — candidate profiles
- `results.html` — live results
- `verify-pvc.html` — PVC verification
- `security.html` — security info
- `index.css` — global stylesheet
- `scripts.js` — global JS (Chart.js + interactions)

## Edge cases
- Refresh on any route other than `/` must default to serving the matching `.html` file
- If a `.html` file is missing, return 404
- No backend — this is a static frontend only
