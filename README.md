# Book Mascots

[![MkDocs](https://img.shields.io/badge/Made%20with-MkDocs-526CFE?logo=materialformkdocs)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Material%20for%20MkDocs-526CFE?logo=materialformkdocs)](https://squidfunk.github.io/mkdocs-material/)
[![GitHub Pages](https://img.shields.io/badge/View%20on-GitHub%20Pages-blue?logo=github)](https://dmccreary.github.io/book-mascots/)
[![Built with Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-DA7857?logo=anthropic)](https://claude.ai/code)
[![Claude Skills](https://img.shields.io/badge/Uses-Claude%20Skills-DA7857?logo=anthropic)](https://github.com/dmccreary/claude-skills)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## View the Live Site

Browse the gallery at: [https://dmccreary.github.io/book-mascots/](https://dmccreary.github.io/book-mascots/)

## Overview

**Book Mascots** is a gallery of reusable cartoon mascot characters designed for use in intelligent textbooks and online courses. Each mascot is a small character with a fixed visual identity and a standard set of *poses* — neutral, welcome, thinking, tip, encouraging, warning, and celebration — that authors drop into chapters to add personality and consistent visual cues.

A mascot is not decoration. When used well, it does real instructional work: it reduces cognitive load by giving students a familiar visual landmark, signals tone shifts (a "warning" pose communicates *be careful here* faster than a paragraph), and gives a textbook a memorable identity that students recognize across slides, quizzes, chatbots, and social media.

This repository serves three purposes:

1. **A gallery** of finished mascots from existing textbook projects (Olli the Octopus for bioinformatics, Axiom the Owl for intelligent textbooks, Sparkle the Unicorn, and many more) that authors are free to reuse under CC BY-NC-SA 4.0.
2. **An idea catalog** of 50 candidate animals with subject-fit notes for authors who want to design a new mascot.
3. **A sync tool** — the `update-mascots` Claude skill — that scans sibling book projects under `~/Documents/ws/` and imports any new mascot directories into this gallery automatically.

## Site Status and Metrics

| Metric | Count |
|--------|-------|
| Mascots in gallery | 25 |
| Pose PNGs | 192 |
| Standard poses per mascot | 7 |
| Markdown files | 60 |
| Mascot ideas catalog | 50 animals |
| Total word count | ~43,000 |
| Claude skills | 1 (`update-mascots`) |

The gallery currently includes mascots for: bioinformatics, biology, blockchain, calculus, chemistry, circuits, cybersecurity, dementia, digital citizenship, ecology, economics, functions, genetics, infographics, intelligent textbooks, learning sciences, moss, personal finance, pre-calc, prompt engineering, quantum computing, statistics, theory of knowledge, token efficiency, and unicorns.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/dmccreary/book-mascots.git
cd book-mascots
```

### Install Dependencies

```bash
pip install mkdocs mkdocs-material
```

### Serve Locally

```bash
mkdocs serve
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

### Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

### Reusing a Mascot in Your Own Textbook

1. Browse the [Mascot Gallery](https://dmccreary.github.io/book-mascots/list-mascots/) and pick a character.
2. Copy the PNG poses from `docs/mascots/<slug>/` into your project's `docs/img/mascot/` (or equivalent) directory.
3. Reference the poses in your chapters using your textbook's admonition or callout style.
4. Provide attribution per the [CC BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/).

### Importing a New Mascot from a Sibling Project

If you have another textbook project under `~/Documents/ws/` with a `docs/img/mascot/` directory, the `update-mascots` skill will import it for you:

```bash
cd "$HOME/Documents/ws/book-mascots"
python3 skills/update-mascots/update_mascots.py
```

The script copies pose PNGs, generates a per-mascot index page, regenerates `docs/list-mascots.md`, and updates the `Mascots` nav section in `mkdocs.yml`. It is idempotent — re-running with no new siblings produces no changes.

## Repository Structure

```
book-mascots/
├── docs/                          # MkDocs source
│   ├── index.md                   # Site home page
│   ├── about.md                   # Why mascots matter, how we make them
│   ├── list-mascots.md            # Auto-generated gallery index
│   ├── mascot-ideas.md            # 50 candidate animals for new mascots
│   ├── mascot-image-quality.md    # Quality guidelines for pose images
│   ├── gender-neutral-names.md    # Naming guidance
│   ├── mascot-test.md             # Visual diagnostic page
│   ├── license.md                 # CC BY-NC-SA 4.0 details
│   ├── contact.md                 # Maintainer contact info
│   ├── css/                       # Theme overrides
│   ├── img/                       # Site-level images (logo, favicon)
│   └── mascots/                   # One directory per mascot
│       └── <slug>/
│           ├── index.md           # Per-mascot pose grid
│           ├── image-prompts.md   # Source AI image-generation prompts
│           ├── neutral.png        # Required: the canonical pose
│           └── *.png              # welcome, thinking, tip, encouraging,
│                                  #   warning, celebration, ...
├── skills/
│   └── update-mascots/            # Claude skill for syncing mascots
│       ├── SKILL.md               # Skill definition
│       └── update_mascots.py      # Worker script
├── mkdocs.yml                     # MkDocs configuration
└── README.md                      # This file
```

## Reporting Issues

Found a bug, broken link, missing pose, or have a suggestion?

[Open an issue on GitHub](https://github.com/dmccreary/book-mascots/issues)

When reporting, please include the mascot slug (e.g. `chemistry`), the pose name, and a description of the problem.

## License

This work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

**You are free to:**

- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material

**Under the following terms:**

- **Attribution** — Give appropriate credit and link back to this repository
- **NonCommercial** — You may not use the material for commercial purposes (no reselling)
- **ShareAlike** — Distribute your contributions under the same license

See [docs/license.md](docs/license.md) for the full license text.

## Acknowledgements

This project is built on top of an excellent open-source stack:

- **[MkDocs](https://www.mkdocs.org/)** — Static site generator for project documentation
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** — Theme used for the gallery
- **[GitHub Pages](https://pages.github.com/)** — Free hosting for the published site
- **[Claude Code](https://claude.ai/code)** by Anthropic — Used to author the `update-mascots` skill, the mascot ideas catalog, and much of the supporting copy

The mascot characters themselves are illustrated using a variety of AI image-generation tools, with each mascot's source prompts stored alongside its poses in `docs/mascots/<slug>/image-prompts.md` for reproducibility.

## Contact

**Dan McCreary**

- LinkedIn: [linkedin.com/in/danmccreary](https://www.linkedin.com/in/danmccreary/)
- GitHub: [@dmccreary](https://github.com/dmccreary)

Questions, mascot suggestions, or interested in contributing a new character? Open an issue or reach out on LinkedIn.
