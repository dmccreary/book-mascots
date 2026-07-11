# Intake Dialog

Use this reference before asking the user for mascot details.

## Required Fields

- `textbook_title`: title of the book/course.
- `subject_summary`: 1-3 sentence description of the subject and its central habits of mind.
- `learner_audience`: grade level, professional role, or background.
- `mascot_purpose`: what the mascot should help learners remember or practice.
- `concept_preference`: user-specified species, object, personification, or "suggest options".
- `avoid`: forbidden species, names, colors, cultural references, visual tropes, or accessibility concerns.
- `style`: flat vector, chibi, storybook, realistic, line art, etc.
- `palette`: exact colors or a general palette.
- `name_constraints`: preferred names, pronouns, alliteration, etymology, or naming rules.
- `destination`: output path/slug.
- `gallery_wiring`: whether to update list pages and nav.

## Dialog Pattern

Ask in stages so the user is not hit with a wall of questions.

Stage 1:

1. What textbook/course is this for, and who are the learners?
2. Should I suggest mascot concepts, or do you already have a species/object/name in mind?
3. Are there any names, species, colors, or cultural references to avoid?

Stage 2, after concept direction is clear:

1. Which visual style should the mascot use?
2. Should the mascot use an existing course palette or new colors?
3. Where should I write the mascot files, and should I update the gallery navigation?

When a dialog UI is available, use it for these stages. If only plain chat is available, ask the same questions directly.

## Concept Selection

When the user asks for suggestions, propose exactly 3 options. For each option include:

- character name
- species/object/form
- one-sentence course connection
- one-sentence visual hook
- any collision risk with existing mascots

Ask the user to pick one before generating images.
