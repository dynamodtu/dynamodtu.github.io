# Notes for coding agents (and anyone changing the code)

This is the website of DYNAMO, the Dynamic Biomedical Devices Group at DTU: https://dynamodtu.com.
It is a Jekyll site built by GitHub Pages from the `master` branch, started from the Academic Pages
template (v0.9.x) and heavily customised. It is **not** a fork to send pull requests back to.

## Who edits it

Group members, usually students, who edit content on github.com with no local setup. **`README.md` is their
manual**: step-by-step recipes for every routine change. If you change how content is entered (a field, a
file, a folder, an image size), update the matching README section in the same change.

Keep content editable without code: content goes in data files and front matter, with a `#` note on each
setting explaining it (see `_data/collaborators.yml`, `_members/_template.md`). Match that comment style.

## Where things are

- **Content:** `_members/` (one file per person; M.S./B.S./special course students all in
  `_members/students.md`), `_news/`, `_publications/`, `_research/`, `_data/` (`authors.yml`,
  `collaborators.yml`, `conferences.yml`, `navigation.yml`), pages in `_pages/`.
- **DYNAMO's own design and code** (the rest is mostly the template's):
  - `_sass/_dynamo.scss`: all of the site's own styles. Colours are the `$dyn-*` variables at its top
    (navy `$dyn-primary`, yellow `$dyn-accent`); breakpoints are the theme's `$small` 600px, `$medium`
    768px, `$large` 925px (sidebar becomes a top bar below it), `$x-large` 1280px.
  - `_sass/_dyn-publications.scss`: the Publications page.
  - `_includes/dyn-*.html` (banner, sidebar, footer), `member-name.html`, `news-list.html`,
    `research-cards.html`, `research-icon.html`; layouts `research-area.html`, `news-post.html`.
  - `assets/js/dyn-*.js`: the site's scripts.
- **Images:** `images/members/` (square photos), `images/logos/` (all logos, including the site's own),
  `images/hero/` (banner stills); videos in `files/videos/`.
- `_site/` is the generated output: never edit it.

## How some things work

- **Banner** (`_includes/dyn-hero.html`): shown when a page has `hero:` in its front matter (`hero: true`
  for a plain one). `hero.video` plays a muted loop, `hero.poster` is shown while it loads. The video plays
  for everyone, also with reduced motion (the group chose this); instead, a pause button in its corner
  (`assets/js/dyn-hero.js`) stops it, and the choice is kept in localStorage for the next pages. A page
  without its own video/image uses its section's: the menu item whose
  `children` link to it in `_data/navigation.yml`, else the page at the first segment of its URL.
- **Members page** sections come from `member_sections` in `_config.yml`; each member file names its
  `section:`. Authors in publication lists are bold when their key is a member's `author_key:`; by the
  group's choice only the PI's file has one, so only Tijana is bold. Don't add `author_key` to others.
- **Publications**: authors are keys from `_data/authors.yml` or written out (`first`, `last1`...).
  `cover_image` feeds the covers column and `thumbnail` the (switched-off) thumbnails; `summary`,
  `abstract` and `tags` are not shown, and leaving them out is fine. `publications` has `output: false`
  (no page per paper).
- **Collaborator logos** are sized by area: `width`/`height` in `_data/collaborators.yml` feed CSS
  variables, and the height is `sqrt(area × h / w)`, so wide and tall logos look equally big.

## Rules

- **No inline `<script>` in pages or includes.** Pages go through the `compress` layout, which is off in
  local development but on for the live build; it joins lines, so a `//` comment silently breaks the rest of
  an inline script on the live site only. Put scripts in `assets/js/` files.
- **Check phone width** (390px) as well as desktop: no horizontal scrolling. Grid columns need
  `minmax(0, 1fr)`, not `1fr`, when they contain one-line (`nowrap`) text.
- **Respect `prefers-reduced-motion`** for new animations (the banner video is the one deliberate exception,
  with its pause button instead).
- **Logos**: SVG, or PNG with a transparent background; crop the empty space around them; browsers can't
  show EPS. Keep files small (a logo over ~100 KB usually needs fixing).
- **Preview locally** with `bundle exec jekyll serve --livereload` (http://localhost:4000). `_config.yml`
  changes need a restart; on Windows, stop the old `ruby.exe` too, or a stale server keeps answering on
  port 4000.
- **Don't commit or push unless asked**: pushing to `master` publishes the site within a minute.
