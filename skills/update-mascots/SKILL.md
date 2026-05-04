---
name: update-mascots
description: Scan sibling book/course projects under /Users/dan/Documents/ws/ for new mascot directories and import any not yet present in this book-mascots repo. Use this skill whenever the user says things like "update the mascots", "check for new mascots", "import mascots", "sync mascots from the other books", "are there any new mascots to bring in", or otherwise asks to refresh this gallery from sibling projects. Copies pose PNGs and the prompt file into docs/mascots/<slug>/, regenerates per-mascot index pages, rewrites docs/list-mascots.md, updates the Mascots nav section in mkdocs.yml, and prints a summary report (new mascots added, total count, anything skipped).
---

# update-mascots

This skill keeps the book-mascots gallery in sync with sibling book/course projects under `$HOME/Documents/ws/`. It is project-local and assumes it is being run from inside `$HOME/Documents/ws/book-mascots`.

## What it does

1. Lists existing mascots already in `docs/mascots/`.
2. Walks every sibling project in `/Users/dan/Documents/ws/` looking for a mascot directory (commonly `docs/img/mascot/`, `docs/mascots/`, or `docs/img/mascots/`) that has at least 3 standard pose PNGs and a `neutral.png` (or `*neutral.png`).
3. For each sibling not already in the gallery:
   - Creates `docs/mascots/<slug>/`
   - Copies every `*.png` from the source mascot dir
   - Copies the source prompt file to `docs/mascots/<slug>/image-prompts.md` (looking in priority order: `image-prompts.md`, `mascot-prompts.md`, `mascot-descriptions.md`, `README.md` in the mascot dir; `docs/prompts/*mascot*.md`; `docs/learning-graph/*mascot*guide*.md`)
   - Generates `docs/mascots/<slug>/index.md` (a Material `grid cards` block, one card per pose PNG, emitted in canonical pose order — see *Pose ordering* below) — the page initially has only the title, the boilerplate "All poses for the **X** mascot." line, and the gallery; the **descriptive intro paragraph is added in step 4** below.
4. **Author a detailed intro paragraph for each newly-imported mascot.** This step is a manual follow-up the agent (Claude) performs after the script finishes — the script cannot produce it because it requires subject-domain judgment (species symbolism, name etymology, biology metaphors, pedagogical fit). For every slug returned by the import step, edit `docs/mascots/<slug>/index.md` and insert a 4–6 sentence paragraph immediately after the `# Title` heading and before the `All poses for the **X** mascot.` line. See the **Intro paragraph pattern** section below for the required structure.
5. Regenerates `docs/list-mascots.md` from scratch by scanning `docs/mascots/`. Each card has the linked book title, the neutral image, and the mascot's *character name* (e.g. "Olli the Octopus") extracted from its prompt file.
6. Rewrites the `Mascots:` section of `mkdocs.yml` so the nav lists every mascot alphabetically by display title. The rest of the file is left alone.
7. Prints a summary: how many new mascots were imported (with slugs), the new total count, and any sibling projects that had a mascot dir but were skipped (e.g. missing `neutral.png`, fewer than 3 poses).

## How to run it

Just run the bundled script from the project root:

```bash
cd "$HOME/Documents/ws/book-mascots"
python3 skills/update-mascots/update_mascots.py
```

The script is idempotent — running it when there are no new mascots produces no file changes and a "0 new mascots" report. Show the script's stdout to the user; it is the summary report.

**Then, for each new slug listed in the report, write the intro paragraph** by editing the freshly-generated `docs/mascots/<slug>/index.md` (see the *Intro paragraph pattern* section below). Skipping this step ships index pages that read as bare image galleries and undercuts the project's premise that effective mascots are subject-coupled, not just cute.

## Intro paragraph pattern

Each per-mascot `index.md` page must open with a 4–6 sentence descriptive paragraph that establishes who the mascot is, where the textbook lives, why this species and name were chosen, and why the choice works pedagogically. The paragraph sits between the `# Title` heading and the `All poses for the **X** mascot.` line.

### Required structure (in order)

1. **First sentence — identification + textbook link.** Open with the bold mascot character name, then state which textbook it is the mascot for, with the textbook title as a hyperlink to its published GitHub Pages URL. Read the sibling project's `mkdocs.yml` to get both the `site_name` (display title) and `site_url`.
2. **Second sentence — species / symbol facts.** State the load-bearing facts about the species, profession, or symbol that make it a fit for the discipline (e.g., octopuses' distributed nervous system; bees' waggle dance; tortoises as long-lived "deep time" animals; foxes as canonical vigilance symbols). These facts must be *real* — not flattery — and must connect to a core idea in the curriculum.
3. **Third sentence — name etymology, when relevant.** If the character's name carries meaning (Greek root, scientist's surname, pun, alliteration), unpack it briefly. Many of the strongest mascots in the gallery have two layers of symbolism: species *and* name (Axiom the Owl, Fermi the Ferret, Iris the Hummingbird, Chronos the Tortoise).
4. **Fourth sentence — why this mascot was chosen.** State the pedagogical intent explicitly: what mental model the mascot installs, what disciplinary virtue it models, what concept becomes free-of-charge for a student who internalizes the character.
5. **Fifth sentence — why the choice is good (or strong / exceptional).** Close with an evaluative sentence that situates the mascot on the good / better / best gradient described in `docs/mascot-effectivness.md`. Mascots whose name *and* species both encode load-bearing concepts are the strongest; mascots that decorate without symbolizing are the weakest.

### Source material

- **Species symbolism and name etymology:** rely on general knowledge; do not invent biological facts. If unsure, state the metaphor in terms the source prompt file already establishes (the source `image-prompts.md` often spells out the rationale).
- **Textbook URL:** read it from the sibling project's `mkdocs.yml` `site_url:` line. Strip surrounding quotes. If the sibling project has no published `site_url`, write a single sentence in the paragraph noting the textbook is in development and skip the link.
- **Tone:** match the rest of the gallery — confident, specific, and grounded. Avoid marketing language. Avoid adjectives like *adorable*, *cute*, *fun*. The whole project's premise is that pedagogical agents earn their keep through subject-coupling, not cuteness.

### Concrete examples

Open any of the recently-added mascot pages for a working template:

- `docs/mascots/ancient-history/index.md` — Chronos the Tortoise (name etymology + species longevity)
- `docs/mascots/networking/index.md` — Buzz the Honey Bee (waggle dance as protocol metaphor)
- `docs/mascots/information-systems/index.md` — Iris the Hummingbird (species behavior + dual-meaning name)
- `docs/mascots/bioinformatics/index.md` — Olli the Octopus (distributed nervous system as parallel pipelines)

### What NOT to do

- Do not write a generic paragraph that could equally describe any mascot in the gallery. Each paragraph must be specific to its character and discipline.
- Do not reproduce text verbatim from the source prompt file — paraphrase and add the pedagogical framing.
- Do not write more than one paragraph; longer treatments belong in `docs/mascot-effectivness.md`, not on the per-mascot page.
- Do not include emojis or marketing flourishes.

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

## Pose ordering

Every per-mascot `index.md` displays poses in this canonical order, regardless of how the source PNGs are named or alphabetized:

1. **neutral** — default / general purpose
2. **welcome** — chapter openings
3. **tip** — hints
4. **thinking** — key concepts
5. **encouraging** — difficult content (also matches `encouragement`)
6. **warning** — common mistakes
7. **celebration** — achievements

This ordering follows the rough emotional arc of a chapter (introduction → guidance → reflection → support → caution → reward) and is more pedagogically meaningful than alphabetical order. The `write_index_md` function in `update_mascots.py` enforces this via the `CANONICAL_POSE_ORDER` constant and the `canonical_pose_key` sort function.

Non-canonical poses found in some source projects (e.g. `caution`, `explain`, `beer`) sort to the end of the grid in alphabetical order so they remain visible without disrupting the canonical first-seven layout.

## Files in this skill

- `SKILL.md` — this file
- `update_mascots.py` — the worker script
