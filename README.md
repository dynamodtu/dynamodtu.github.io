# The DYNAMO website

This repository is the website of **DYNAMO, the Dynamic Biomedical Devices Group** at the Technical
University of Denmark (DTU): **https://dynamodtu.github.io**

This page explains how to keep the site up to date. You don't need to install anything or know how to
code: every routine change is editing a text file or uploading a file, right here on github.com. The site
updates itself about a minute after you save.

**Contents**

- [How editing works](#how-editing-works)
- [Where everything lives](#where-everything-lives)
- [Members](#members): add someone, M.S./B.S. students, someone leaves
- [News posts](#news-posts), including [announcing an open position](#announcing-an-open-position)
- [Publications](#publications)
- [Conferences (talks and posters)](#conferences-talks-and-posters)
- [Collaborator logos](#collaborator-logos)
- [Banner videos](#banner-videos)
- [The Welcome photo on the home page](#the-welcome-photo-on-the-home-page)
- [Research areas](#research-areas)
- [Menu, contact page and footer](#menu-contact-page-and-footer)
- [Image and video sizes](#image-and-video-sizes)
- [When something goes wrong](#when-something-goes-wrong)
- [Access to this repository](#access-to-this-repository)
- [Previewing on your own computer (optional)](#previewing-on-your-own-computer-optional)

---

## How editing works

You need to be signed in to GitHub with an account that has access to this repository
(see [Access](#access-to-this-repository)).

| To... | Do this |
|---|---|
| **Change a file** | Open the file, click the **pencil** icon (top right of the file), make your changes, then click **Commit changes...** and **Commit changes** again. |
| **Add a new text file** | Open the folder, click **Add file → Create new file**, type the file name, paste the content, commit. |
| **Upload a photo, logo or video** | Open the folder, click **Add file → Upload files**, drag the files in, commit. For a folder that doesn't exist yet (like `images/news/`), open the folder above it (`images/`) and drag in a folder from your computer with that name and the file inside. |
| **Delete a file** | Open the file, click the **...** menu (top right), **Delete file**, commit. |
| **Rename or move a file** | Edit the file (pencil) and change its name in the box at the top. Typing `folder/` in front of the name moves it. |

After you commit, the site rebuilds by itself. It's usually live within a minute or two. To follow it, open
the **Actions** tab: the newest *pages build and deployment* run turns green when it's live. Reload the site
with **Ctrl+F5** (or **Cmd+Shift+R** on a Mac) to skip your browser's old copy.

### The settings block at the top of a file

Most files start with a block of settings between two `---` lines, for example:

```yaml
---
name: Firstname Lastname
section: phd-students       # anything after a # is a note, ignored by the site
order: 1
---
```

A few rules keep it working:

- **Keep both `---` lines.**
- **Indent with spaces, never tabs**, and keep the indentation the same as the lines around it.
- **Put text in "quotes" if it contains a colon `:`**, a `#`, or starts with a special character, e.g.
  `title: "SERS: a new approach"`.
- **Dates are written `2026-10-14`** (year-month-day).
- Leave a setting empty (`photo:`) rather than deleting it if you might need it later.

Many files have notes (after `#`) explaining every setting. Read them: they are the manual.

---

## Where everything lives

| What | Where |
|---|---|
| People (one file each) | `_members/` (template: `_members/_template.md`) |
| M.S., B.S. and special course students | `_members/students.md` (one list, no file per student) |
| Member photos | `images/members/` |
| News posts | `_news/` |
| Papers | `_publications/` |
| Author names in papers | `_data/authors.yml` |
| Talks and posters | `_data/conferences.yml` |
| Collaborator logos | list: `_data/collaborators.yml`, files: `images/logos/` |
| Research areas | `_research/` |
| Banner videos and their still images | `files/videos/` and `images/hero/` |
| Home page (Welcome text and photo) | `_pages/home.html` |
| Other pages (Members, Research, News, Contact...) | `_pages/` |
| Menu | `_data/navigation.yml` |
| Site-wide settings (footer, member sections...) | `_config.yml` |

**Leave these alone unless you know what you're doing:** `_layouts/`, `_includes/`, `_sass/`, `assets/`
and most of `_config.yml`. They hold the site's design and code, not its content.

---

## Members

The Members page has these sections, in this order: **Principal Investigator**, **Postdoctoral
Researchers**, **Ph.D. Students**, **M.S. Students**, **B.S. Students**, **Special Course Students**,
**Alumni**.

### Add a postdoc or Ph.D. student

1. **Photo:** crop it to a **square**, about **480 × 480 pixels**, as a `.jpg`, showing head and shoulders
   (Windows Photos: *Edit → Crop → Aspect ratio: Square*). Upload it to `images/members/` named
   `firstname-lastname.jpg` (lowercase, no spaces).
2. **Their file:** open `_members/_template.md`, copy everything, then create a new file
   `_members/firstname-lastname.md` and paste. Files starting with `_` are not shown on the site, so the
   template itself stays hidden. Fill it in, for example:

   ```yaml
   ---
   name: Firstname Lastname
   section: phd-students       # postdocs | phd-students | alumni
   order: 4                    # position within the section, lower comes first
   role: Ph.D. Student
   co_supervised:              # true if Tijana is co-supervisor
   main_supervisor:            # with co_supervised, e.g. "Prof. Anja Boisen"
   photo: /images/members/firstname-lastname.jpg
   research: "Oral drug delivery"
   email: firstname.lastname@dtu.dk
   scholar:
   orcid:
   linkedin:
   website:
   ---
   ```

   Without a photo, their initials are shown in a circle instead.

   Don't add an `author_key:` line: only Tijana's name is shown in bold in author lists, and her file is
   the only one that has it (see [Publications](#publications)).

### Add M.S., B.S. or special course students

These students don't get their own file. Open `_members/students.md` and add one line under the right
list (`masters`, `bachelors` or `special-course`), indented like the others:

```yaml
masters:
  - Sylvia Atladottir
  - New Student Name
```

They're shown in exactly this order. The file's notes explain the optional extras (a project title, a
link, or a surname of more than one word).

### Someone leaves

- **Postdoc or Ph.D. student:** in their file in `_members/`, change `section:` to `alumni`. You can update
  `role:` too, e.g. `role: "Ph.D. 2027, now at Novo Nordisk"`.
- **M.S., B.S. or special course student:** delete their line from `_members/students.md`.
- **Removing someone completely:** delete their file in `_members/` (and their photo).

### The PI profile

Tijana's profile is `_members/prof-tijana-miseljic.md`, including the Education / Work experience /
Awards rows under her card. Each row is a `year` and a `text`; the notes in the file show how to add one.

---

## News posts

Each post is one file in `_news/`. The newest four are shown on the home page, and all of them on the
News page, newest first. Each post also gets its own page.

1. Create a file in `_news/` named `YYYY-MM-DD-short-title.md`, e.g. `2027-03-02-new-grant.md`.
2. Paste this and fill it in:

   ```markdown
   ---
   title: "DYNAMO receives a new grant"
   date: 2027-03-02
   image:            # optional photo at the top, e.g. /images/news/2027-03-02-grant.jpg
   ---

   The text of the post. Leave an empty line between paragraphs.
   You can make a [link](https://www.dtu.dk) and write **bold** text.
   ```

3. For a photo, upload it to `images/news/` and put its address after `image:`.

The address of the post is `/news/` plus the file name without `.md`, so pick a short, clear name.

### Announcing an open position

Official DTU positions (Ph.D., postdoc) are applied for through DTU's job portal; the website announces
them and links there.

1. **A news post** with the announcement, e.g. `_news/2026-10-18-hiring-postdoc.md`: a short title
   ("We're hiring a Postdoc": the home page shows titles on one line), the deadline and the link to the
   DTU job ad at the top, then the project, tasks, requirements and how to apply. Copy one of the
   existing hiring posts and change it.
2. **The Contact page** (where the home page's *Join us* button leads): in `_pages/contact.html`, the
   `intro:` text under `applications:` names the open positions with links to their posts, e.g.
   `**[Postdoc](/news/2026-10-18-hiring-postdoc/)** (apply by 26 October 2026)`.
3. **After the deadline:** take the positions out of the Contact page `intro:`, and either delete the news
   post or add a line at its top: `**This position has been filled.**`

To show an e-mail address in a post without exposing it to spam robots, write
`{% include email-link.html address="name@dtu.dk" show=true %}` instead of the address.

---

## Publications

Each paper is one file in `_publications/`. The Publications page lists them newest first, grouped by
year; the newest three are also on the home page.

1. Create a file named `YYYY-MM-DD-short-name.md` (the publication date), e.g.
   `2027-01-15-magnetic-micromotors.md`.
2. Paste this and fill it in:

   ```yaml
   ---
   title: "Full title of the paper"
   authors:
     - key: tijana              # a person from _data/authors.yml
     - first: "Jane"            # anyone else: write the name out
       last1: "Doe"
     - key: anja
   category: journals          # journals | reviews
   date: 2027-01-15
   venue: "Advanced Functional Materials"
   short: "Adv Funct Mater"
   volume: '37'
   issue: '3'
   pages: '2412345'
   paperurl: https://doi.org/10.1002/adfm.2412345
   ---
   ```

- **Tijana in bold:** list her as `- key: tijana` and her name is shown in **bold** automatically. Only she
  is bold: her member file is the only one with `author_key: tijana`, and other members shouldn't get
  one. A person who appears in many papers can get a short key in `_data/authors.yml` (written like the
  ones there) to save typing; everyone else can be written out with `first:` and `last1:`
  (optionally `middle:` and a second surname `last2:`). The notes at the top of `_data/authors.yml` explain
  the options.
- **Not out yet:** add `status: "In press"` (or "Accepted") and it's shown instead of the year.
- **Cover feature:** add `cover: true` (and optionally `cover_url:` with a link to the cover) to show a
  "Cover Feature" label.
- **Reviews** use `category: reviews` and are listed together with the journal articles.
- Some papers have extra fields (`summary`, `abstract`, `tags`, `thumbnail`...). They come from the format
  this site shares with a personal site; they're optional and you can leave them out.

---

## Conferences (talks and posters)

Talks, posters and other conference contributions are all in one file: `_data/conferences.yml`. Add an
entry at the bottom (any order; the page sorts them newest first):

```yaml
- date: 2027-06-15
  type: Talk                        # Talk | Poster | Invited talk | Keynote | Workshop ...
  title: "Title of the contribution"
  presenters: "**T. Maric**, J. Doe"   # Tijana in **bold**, as in the paper lists
  event: "Name of the conference 2027"
  location: "Copenhagen, Denmark"
  url: https://example.org          # optional link (abstract, programme...)
  pdf: /files/posters/file.pdf      # optional: upload the poster to files/posters/
```

**The file starts with two example entries marked `sample: true`.** Delete those once the first real
entries are in.

---

## Collaborator logos

The home page ends with a strip of collaborator logos, in centred rows.

1. **Logo file:** preferably **SVG**; otherwise a **PNG with a transparent background**, about 600–800
   pixels wide. **EPS, PDF and Word files don't work in browsers**: ask for an SVG or PNG instead. Crop away
   any empty space around the logo, or it will look too small. Upload it to `images/logos/` with a short
   lowercase name, e.g. `novo-nordisk.svg`.
2. **Add it to the list** in `_data/collaborators.yml`, in the position you want:

   ```yaml
   - name: "Novo Nordisk"
     logo: /images/logos/novo-nordisk.svg
     width: 300
     height: 100
   ```

`width` and `height` are the logo file's own size. With them, every logo is sized to look equally big
whatever its shape. To find them: for a PNG, right-click the file on your computer, **Properties →
Details**; for an SVG, open it (it's text) and look for `viewBox="0 0 300 100"` near the top: the last two
numbers. Without them the logo is simply shown 48 pixels tall.

---

## Banner videos

The banner at the top of Home, Members, Research and Publications plays a short muted video on a loop,
behind the page title. Pages under a section use their section's video: the research areas use the
Research video, Conferences uses the Publications video, and news posts would use a News video.
Visitors can stop it with the small pause icon in the banner's bottom right corner; their browser
remembers that, so the videos stay paused on the next pages too.

**The video:**

- shaped **4:1** (four times as wide as tall), e.g. **1920 × 480** or 2880 × 720
- **MP4**, **no sound** (it always plays muted, so remove the sound track to save space), **under ~3 MB**
- **3–15 seconds** that loop smoothly (the end flows back into the start)
- keep the interesting part **in the middle and right**: the left side is under a dark blue tint that
  keeps the title readable, and the edges are cut off on some screens

**The still image:** a `.jpg` of the video's **first frame**, at the same 4:1 shape. It's shown while the
video loads, so the banner doesn't flash plain blue first. It's optional but recommended.

**To change or add one:**

1. Upload the video to `files/videos/` and the still image to `images/hero/`. Uploading a file with the
   same name as an existing one replaces it.
2. In the page's file in `_pages/`, set them under `hero:` at the top:

   ```yaml
   hero:
     video: /files/videos/news.mp4
     poster: /images/hero/news.jpg
   ```

   On a page that currently says `hero: true` (News, Conferences, Contact), replace that line with the
   block above. Any page can also use a still photo only: `image: /images/hero/photo.jpg`.

---

## The Welcome photo on the home page

The Welcome section has a "Photo coming soon" box until a photo is set.

1. Upload a **landscape** photo, about **1600 pixels wide**, to a new folder `images/home/`, e.g.
   `images/home/welcome.jpg`. The photo is cropped around its centre to fit (4:3 next to the text on wide
   screens, 16:9 above the text on smaller ones), so keep people away from the edges.
2. In `_pages/home.html`, at the top, fill in:

   ```yaml
   welcome_photo: /images/home/welcome.jpg
   welcome_photo_alt: "The DYNAMO group in the lab"    # a short description, for screen readers
   ```

The Welcome text itself is further down in the same file, as normal text between `<p>` and `</p>`.

---

## Research areas

Each research area is a file in `_research/`: it becomes a card on the Research page and a page of its
own. To add one:

1. Copy an existing file, e.g. `_research/sers-sensing.md`, to a new file in `_research/` with a short
   name (the name becomes its address: `/research/<name>/`).
2. Change `title`, `label` (the small grey category), `order` (position among the areas), `summary` (the
   text on the card) and the text below the settings.
3. `icon:` picks the drawing on the card. There are four: `skin`, `nose`, `gut`, `sers`. New drawings
   need code changes (`_includes/research-icon.html`).
4. Add it to the Research sub-menu in `_data/navigation.yml` (see below).

---

## Menu, contact page and footer

- **Menu** (sidebar): `_data/navigation.yml`. Each entry is a `title` and a `url`; `children` makes a
  sub-menu. Removing an entry hides it from the menu but doesn't delete the page.
- **Contact page**: everything on it (address, map, open positions, who to email) is in the settings at
  the top of `_pages/contact.html`, with notes.
- **Footer** text and logos: the `footer:` section near the top of `_config.yml`.

---

## Image and video sizes

| What | Shape | Size | Format | Folder |
|---|---|---|---|---|
| Member photo | square | ~480 × 480 | JPG | `images/members/` |
| Collaborator logo | any, empty space cropped away | 600–800 wide if PNG | SVG, or PNG with transparent background | `images/logos/` |
| Banner video | 4:1 | 1920 × 480 or larger, under ~3 MB | MP4, no sound | `files/videos/` |
| Banner still image | 4:1 | same as the video | JPG | `images/hero/` |
| Welcome photo | landscape | ~1600 wide | JPG | `images/home/` |
| News photo | landscape | ~1600 wide | JPG | `images/news/` |

Keep photos under about 500 KB. A phone photo straight from the camera is often 3–5 MB, which makes the
site slow: shrink it first (Windows Photos: *... → Resize image*).

File names: lowercase, words separated by `-`, no spaces or special letters (`marco-tjakra.jpg`, not
`Marco Tjakra (1).JPG`). Addresses on the site are case-sensitive: `Photo.jpg` and `photo.jpg` are different.

---

## When something goes wrong

- **The site didn't change.** Wait two minutes, then reload with **Ctrl+F5**. Check the **Actions** tab:
  a yellow dot means it's still building.
- **The build failed** (red ✗ in the **Actions** tab). Don't panic: the site keeps showing the previous
  version. Open the failed run to see the message; it usually names the file and line. Most failures are a
  typo in the settings block: a missing quote, a tab instead of spaces, a missing `---`, or a `:` in text
  without quotes.
- **A photo or logo doesn't show.** Check that the address in the file matches the uploaded file exactly,
  including capital letters and the extension (`.jpg` vs `.jpeg` vs `.JPG`).
- **Undo a change.** Open the file, click **History**, open the version from before the change, copy its
  content (the **Raw** button shows it as plain text), then edit the current file, paste, and commit.
  Nothing is ever lost: every earlier version is kept.

---

## Access to this repository

The site belongs to the **dynamodtu** GitHub account (e-mail: dynamo.dtu@gmail.com). Its password and
two-factor recovery codes should be held by the group leader, so the site never depends on one student.

To let someone edit the site, the account owner adds their own GitHub account under **Settings →
Collaborators → Add people**. Don't share the dynamodtu password with students; remove people from
Collaborators when they leave.

---

## Previewing on your own computer (optional)

For bigger changes (new pages, design) you can run the site on your own computer and see changes before
they go live. You need [Ruby](https://www.ruby-lang.org/en/downloads/) with Bundler; then, in this folder:

```bash
bundle install
bundle exec jekyll serve --livereload
```

and open http://localhost:4000. It updates as you save files, except `_config.yml`: after changing that,
stop it (Ctrl+C) and start it again. On Windows, make sure the old one has really stopped: an old server
can keep answering on port 4000 with an outdated site.

`AGENTS.md` describes how this site is built, for AI coding assistants (Claude Code, Copilot...) and for
anyone changing the design or code.

---

Built on the [Academic Pages](https://github.com/academicpages/academicpages.github.io) template
(MIT License, see `LICENSE`), itself based on the Minimal Mistakes Jekyll theme by Michael Rose.
