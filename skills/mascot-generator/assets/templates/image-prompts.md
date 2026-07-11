# Image Prompts for {{mascot_name}}

I am about to generate seven different poses and one character sheet for a book mascot. Use a consistent drawing style for every image.

Every pose image should be generated at 1024x1024. If chroma-key post-processing is needed, use a perfectly flat `#00FF00` background, convert it to a fully transparent alpha channel, trim to the visible character, and optimize the final PNG when practical.

## Base Character Description

{{base_character_description}}

## 1. Neutral - `neutral.png`

Use case: educational. Asset type: pedagogical mascot pose for an interactive textbook. {{base_character_description}} {{neutral_pose_detail}}

{{background_rule}}

## 2. Welcome - `welcome.png`

Use case: educational. Asset type: pedagogical mascot pose for an interactive textbook. {{base_character_description}} {{welcome_pose_detail}}

{{background_rule}}

## 3. Tip - `tip.png`

Use case: educational. Asset type: pedagogical mascot pose for an interactive textbook. {{base_character_description}} {{tip_pose_detail}}

{{background_rule}}

## 4. Thinking - `thinking.png`

Use case: educational. Asset type: pedagogical mascot pose for an interactive textbook. {{base_character_description}} {{thinking_pose_detail}}

{{background_rule}}

## 5. Encouraging - `encouraging.png`

Use case: educational. Asset type: pedagogical mascot pose for an interactive textbook. {{base_character_description}} {{encouraging_pose_detail}}

{{background_rule}}

## 6. Warning - `warning.png`

Use case: educational. Asset type: pedagogical mascot pose for an interactive textbook. {{base_character_description}} {{warning_pose_detail}}

{{background_rule}}

## 7. Celebration - `celebration.png`

Use case: educational. Asset type: pedagogical mascot pose for an interactive textbook. {{base_character_description}} {{celebration_pose_detail}}

{{background_rule}}

## Character Sheet - `character-sheet.png`

Create a clean character reference sheet for {{mascot_name}}. Include one large neutral full-body view and smaller pose or detail callouts if the generator can do this cleanly. Preserve the same palette, proportions, anatomy, expression language, and art style described above. {{character_sheet_label_rule}}

{{background_rule}}

## Post-processing

For each generated source image, remove the background if needed, trim excess transparent padding, and verify that the visible character remains uncropped and centered.
