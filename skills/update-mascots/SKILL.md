---
name: update-mascots
description: Scan sibling book/course projects under /Users/dan/Documents/ws/ for new mascot directories and import any not yet present in this book-mascots repo. Use this skill whenever the user says things like "update the mascots", "check for new mascots", "import mascots", "sync mascots from the other books", "are there any new mascots to bring in", or otherwise asks to refresh this gallery from sibling projects. Copies pose PNGs and the prompt file into docs/mascots/<slug>/, regenerates per-mascot index pages, rewrites docs/list-mascots.md, updates the Mascots nav section in mkdocs.yml, and prints a summary report (new mascots added, total count, anything skipped).
---

# update-mascots

This skill keeps the book-mascots gallery in sync with sibling book/course projects under `/Users/dan/Documents/ws/`. It is project-local and assumes it is being run from inside `/Users/dan/Documents/ws/book-mascots`.

## What it does

1. Lists existing mascots already in `docs/mascots/`.
2. Walks every sibling project in `/Users/dan/Documents/ws/` looking for a mascot directory (commonly `docs/img/mascot/`, `docs/mascots/`, or `docs/img/mascots/`) that has at least 3 standard pose PNGs and a `neutral.png` (or `*neutral.png`).
3. For each sibling not already in the gallery:
   - Creates `docs/mascots/<slug>/`
   - Copies every `*.png` from the source mascot dir
   - Copies the source prompt file to `docs/mascots/<slug>/image-prompts.md` (looking in priority order: `image-prompts.md`, `mascot-prompts.md`, `mascot-descriptions.md`, `README.md` in the mascot dir; `docs/prompts/*mascot*.md`; `docs/learning-graph/*mascot*guide*.md`)
   - Generates `docs/mascots/<slug>/index.md` (a Material `grid cards` block, one card per pose PNG)
4. Regenerates `docs/list-mascots.md` from scratch by scanning `docs/mascots/`. Each card has the linked book title, the neutral image, and the mascot's *character name* (e.g. "Olli the Octopus") extracted from its prompt file.
5. Rewrites the `Mascots:` section of `mkdocs.yml` so the nav lists every mascot alphabetically by display title. The rest of the file is left alone.
6. Prints a summary: how many new mascots were imported (with slugs), the new total count, and any sibling projects that had a mascot dir but were skipped (e.g. missing `neutral.png`, fewer than 3 poses).

## How to run it

Just run the bundled script from the project root:

```bash
cd /Users/dan/Documents/ws/book-mascots
python3 .claude/skills/update-mascots/update_mascots.py
```

The script is idempotent — running it when there are no new mascots produces no file changes and a "0 new mascots" report. Show the script's stdout to the user; it is the summary report.

## Why a script instead of inline steps

The work is purely mechanical (find files, copy, regenerate two derived files) and involves a name-extraction regex pass that's tedious to do step-by-step in a chat. A single script keeps the operation atomic and consistent every time.

## Name extraction (reference)

The script extracts each mascot's display name from its `image-prompts.md` using these rules in order:

1. Read the first `# H1` line. Split on em-dash / en-dash / " - " and keep the left side.
2. Strip leading `Mascot:`, `AI Image Generation Prompts for `, `Image Prompts for `, `Image Prompts of `.
3. Strip trailing ` Mascot Image Prompts`, ` Mascot`, ` Image Prompts`, ` AI Image…`.
4. If the result is empty or `Mascot Prompts`, fall back to a `**Name:**` or `**Name (Suggested):**` value found anywhere in the file.
5. Apply manual overrides for known edge cases: `cybersecurity → Sentinel the Fox`, `intelligent-textbooks → Axiom the Owl`, `pre-calc → Prema`.

If you need to add a new override (because a source file has an unusual structure), edit the `OVERRIDES` dict at the top of `update_mascots.py`.

## Files in this skill

- `SKILL.md` — this file
- `update_mascots.py` — the worker script
