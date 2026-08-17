# Md. Mehenuf Hossain Bhuiyan — Portfolio

Personal portfolio site. Plain HTML, CSS, and JavaScript — no framework, no
build step, no `npm install`. That's deliberate: it means the site is free
to host anywhere and will still work in five years.

**Live:** https://mehenuf.github.io/ (once deployed — see [GUIDE.md](GUIDE.md))

**For everything — pushing to GitHub, hosting it live for free, and editing
every part of the site (text, photo, skills, adding a new project, colours,
fonts) — see [`GUIDE.md`](GUIDE.md). This file is just the map.**

```
.
├── index.html                       homepage — edit directly
├── projects/                        6 case studies — GENERATED, don't edit directly
│   ├── cifar10-classifier.html
│   ├── patient-care-operating-system.html
│   ├── credit-scoring-blockchain.html
│   ├── corn-leaf-xai.html
│   ├── perfume-store-rdbms.html
│   └── flood-alert-system.html
├── build_projects.py                generates everything in projects/ — edit THIS instead
├── assets/
│   ├── css/style.css                the entire design system
│   ├── js/main.js                   theme, reveals, timeline, lightbox
│   └── img/                         result charts pulled from my repos
├── .github/workflows/deploy.yml     GitHub Pages auto-deploy
├── .nojekyll                        tells Pages not to run Jekyll
└── GUIDE.md                         the full manual — start here
```

## The 30-second version

```bash
# Preview locally
python3 -m http.server 8000

# After editing build_projects.py, regenerate the project pages
python3 build_projects.py

# Ship it
git add . && git commit -m "..." && git push
```

Full detail on all of the above — including first-time GitHub setup,
Personal Access Tokens, enabling GitHub Pages, and a section-by-section
editing walkthrough — is in **[GUIDE.md](GUIDE.md)**.

---

© Md. Mehenuf Hossain Bhuiyan
