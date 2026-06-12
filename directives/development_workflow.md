# Development Workflow

## Goal
Standard process for adding features or fixing bugs on the Nigeria E-Vote frontend.

## Process

### 1. Understand the current state
- Read the relevant HTML file and its inline `<style>` block
- Check `index.css` for shared styles and responsive breakpoints
- Check `scripts.js` for any related JS logic
- Check `directives/` for existing SOPs

### 2. Check for execution scripts
Before manually doing repetitive work, check `execution/`:
- `validate_html.py` — check HTML structure
- `analyze_css.py` — audit CSS for issues

### 3. Make changes
- Follow the style guide (`directives/frontend_style.md`)
- Keep UI consistent with existing pages
- Add responsive support at all 3 breakpoints (1024px, 768px, 480px)

### 4. Self-anneal on errors
If something breaks:
1. Read the error
2. Fix the root cause
3. Run validation scripts again
4. Update the relevant directive with what was learned

### 5. Update directives
If you discover a new pattern, constraint, or edge case, update the relevant directive.

## Adding a new page
1. Create `.html` file with the standard navbar/body/footer structure
2. Add page-specific styles in an inline `<style>` block (not in index.css)
3. Add `active-link` class to the nav link
4. Add responsive support at all breakpoints
5. Update `directives/serve_frontend.md` if the page is in the navigation

## Adding interactivity
- All JS goes in `scripts.js` inside the `DOMContentLoaded` listener
- If the logic is complex, extract into a named function
- Chart.js charts use `<canvas>` with an `id` attribute
- Form validation is client-side only (no backend yet)
