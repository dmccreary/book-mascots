---
name: generate-mascot-codex
description: Generate a new pedagogical textbook mascot with Codex. Use when the user asks to create, design, or generate a new mascot; produce mascot image prompts; generate the seven standard mascot poses; create a character sheet; or add a mascot gallery entry in a book-mascots-style MkDocs project. Guides intake dialog, concept selection, collision checks, image generation, post-processing, and output files for neutral, welcome, tip, thinking, encouraging, warning, and celebration poses.
---

# Generate Mascot Codex

## Overview

Create a complete textbook mascot package: a concept grounded in the course, a canonical character sheet, seven consistent pose images, image prompts, and a gallery page. Prefer repo conventions over generic mascot advice.

## Required Intake

Start with a short dialog before designing unless the user already supplied every required field. Use `request_user_input` when it is available; otherwise ask concise plain-text questions and wait for the answers.

Read `references/intake-dialog.md` before asking. Gather:

- textbook title, topic, and learner audience
- mascot role, tone, and pedagogical purpose
- preferred or forbidden species/object/personification
- visual style and palette constraints
- output slug/path and whether to update gallery navigation
- any name, pronoun, accessibility, or cultural constraints

If the user has no mascot idea, propose 3 concepts and ask them to choose before generating images. Favor concepts whose species, object, or name encodes a real disciplinary idea.

## Workflow

1. Confirm the destination. Default to `docs/mascots/<slug>/` in the current repo unless the user names another path.
2. Inspect existing mascots before naming:
   - `find docs/mascots -maxdepth 2 -name index.md`
   - `rg -n "^#|Name|Species|Mascot|the " docs/mascots`
   - Note the known two-Sylvia collision: `statistics-course` and `personal-finance` both use squirrel mascots named Sylvia. Do not add another ambiguous first-name collision unless the user explicitly chooses it.
3. Design the mascot concept. Choose a name, form/species, role, and visual anchors that are specific to the textbook.
4. Create a canonical `character-sheet.md` from `assets/templates/character-sheet.md`.
5. Create `image-prompts.md` from `assets/templates/image-prompts.md`. Read `references/pose-and-prompt-rules.md` before writing the prompts.
6. Generate all seven pose images with the image generation tool or imagegen skill:
   - `neutral.png`
   - `welcome.png`
   - `tip.png`
   - `thinking.png`
   - `encouraging.png`
   - `warning.png`
   - `celebration.png`
7. Generate one character sheet image named `character-sheet.png` unless the user requests markdown only.
8. Post-process each pose to transparent PNG when needed. If chroma key is used, remove `#00FF00`, trim transparent padding, and verify alpha at all four corners.
9. Create or update `index.md` from `assets/templates/index.md`.
10. If requested, update `docs/list-mascots.md` and the `Mascots:` section of `mkdocs.yml`; otherwise report the new mascot path and any skipped gallery wiring.

## Image Generation Rules

Keep the seven pose prompts visually consistent. Every prompt must repeat the canonical base description from the character sheet: name, form/species, colors, distinctive anatomy, expression style, accessories, no-text rule, and composition.

Use a flat chroma-key background when the image tool cannot reliably create transparency:

```text
Create the subject on a perfectly flat solid #00FF00 chroma-key background for background removal. The background must be one uniform color with no shadows, gradients, texture, floor plane, reflections, or lighting variation. Do not use green anywhere in the character.
```

Avoid props unless they are core identifiers. Hands, paws, wings, fins, or other expressive features should be visible and available for gestures across the pose set.

## Output Contract

The destination folder should contain at minimum:

```text
character-sheet.md
character-sheet.png
image-prompts.md
index.md
neutral.png
welcome.png
tip.png
thinking.png
encouraging.png
warning.png
celebration.png
```

If image generation is unavailable, still create `character-sheet.md`, `image-prompts.md`, and `index.md`, then clearly state that the PNGs remain to be generated.

## Validation

Before finishing:

- Confirm every required file exists.
- Inspect generated images visually or with a screenshot/contact sheet.
- Check that the seven pose images share the same character design, palette, and style.
- Check for accidental text, watermarks, cropped limbs, extra characters, props that contradict the sheet, green remnants, or opaque corners.
- Run `git diff --check` when files were edited.
- If this is a MkDocs gallery change, run the repo's normal MkDocs build command when available.

## Resources

- `references/intake-dialog.md` - dialog fields and staged question plan.
- `references/pose-and-prompt-rules.md` - pose meanings, prompt constraints, and quality checks.
- `assets/templates/character-sheet.md` - canonical character sheet template.
- `assets/templates/image-prompts.md` - seven-pose prompt template.
- `assets/templates/index.md` - gallery page template.
